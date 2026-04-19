#!/usr/bin/env python3
"""Validate all SKILL.md — GitHub Actions CI ready."""
import re, sys, json
from pathlib import Path

def out(msg, tag=""):
    colors = {"ok": "\033[92m", "fail": "\033[91m", "warn": "\033[93m", "info": "\033[96m", "": "\033[0m"}
    print(f"{colors.get(tag,'')}{msg}\033[0m")

def parse_frontmatter(content):
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return None
    result, lines = {}, m.group(1).splitlines()
    current_key, buf, in_ml = None, [], False
    for line in lines:
        sm = re.match(r'^(\w[\w-]*):\s*(.*)$', line)
        if sm and not in_ml:
            if current_key:
                result[current_key] = " ".join(buf).strip('"\', ')
            current_key, val = sm.group(1), sm.group(2).strip('"\', ')
            if val in ('|', '>'):
                in_ml, buf = True, []
            else:
                result[current_key] = val
                current_key = None
        elif in_ml:
            if line.startswith((' ', '\t')) or (line and not line[0].isalnum()):
                buf.append(line.strip())
            else:
                result[current_key] = " ".join(buf).strip()
                in_ml, current_key = False, None
                sm2 = re.match(r'^(\w[\w-]*):\s*(.*)$', line)
                if sm2:
                    current_key, val = sm2.group(1), sm2.group(2).strip('"\', ')
                    if val in ('|', '>'):
                        in_ml, buf = True, []
                    else:
                        result[current_key] = val
                        current_key = None
    if current_key:
        result[current_key] = " ".join(buf).strip() if in_ml else result.get(current_key, "")
    return result

SENSITIVE = [
    (r'ghp_[A-Za-z0-9]{36}',          "GitHub PAT"),
    (r'AKIA[A-Z0-9]{16}',             "AWS Access Key"),
    (r'sk-[A-Za-z0-9]{48}',           "OpenAI API Key"),
    (r'["\'\s]1[3-9]\d{9}["\'\s]',  "手机号"),
    (r'o9cq800ctutTAqr5F98FlVHPTvbw', "微信号"),
]

def validate_skill(path):
    content = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(content)
    errors, warns = [], []

    if fm is None:
        return False, ["无 YAML frontmatter"], []

    for field in ["name", "description"]:
        if field not in fm or not str(fm.get(field, "")).strip():
            errors.append(f"缺少字段: {field}")

    # name: at least 3 chars
    name = fm.get("name", "")
    if name and len(name) < 3:
        errors.append(f"name 过短: '{name}'")

    # description: at least 15 chars (or allow multiline brief)
    desc = fm.get("description", "")
    if desc and len(desc) < 10:
        warns.append("description 可能偏短")

    # Sensitive data check
    for pat, label in SENSITIVE:
        if re.search(pat, content):
            if label == "手机号":
                if not re.findall(r'["\'\s]1[3-9]\d{9}["\'\s]', content):
                    continue
            warns.append(f"⚠ 含敏感信息: {label}")
            break

    return len(errors) == 0, errors, warns

def main():
    # Resolve skills_dir relative to the script location
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent  # .github/scripts → .github → repo root
    skills_dir = repo_root  # scan from repo root
    passed, failed, warn_list = [], [], []

    skill_mds = sorted([p for p in skills_dir.rglob("SKILL.md")
                        if "node_modules" not in str(p)])

    for skill_path in skill_mds:
        ok, errs, w = validate_skill(skill_path)
        rel = str(skill_path.relative_to(skills_dir))
        if ok:
            tag = "warn" if w else "ok"
            out(f"{'✓' + (' ⚠' if w else '')} {rel}", tag)
            passed.append(rel)
            for x in w: out(f"  {x}", "warn")
            warn_list.extend([rel, x] for x in w)
        else:
            out(f"✗ {rel}", "fail")
            failed.append(rel)
            for e in errs: out(f"  → {e}", "fail")

    out(f"\n{'─'*48}")
    out(f"  总计 {len(passed)+len(failed)}  |  ✓ {len(passed)}  |  ✗ {len(failed)}  |  ⚠ {len(warn_list)}")

    report = {
        "total": len(passed)+len(failed), "passed": len(passed),
        "failed": len(failed), "warnings": len(warn_list),
        "failed_skills": failed,
        "warning_skills": [[s, w] for s, w in warn_list],
    }
    with open(repo_root/"validation_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    if failed:
        out(f"\n❌ CI FAILED — {len(failed)} 个技能未通过", "fail")
        sys.exit(1)
    elif warn_list:
        out(f"\n⚠  PASSED with warnings — 见 validation_report.json", "warn")
        sys.exit(0)
    else:
        out(f"\n✅ ALL PASSED — {len(passed)} 个技能全部合格", "ok")
        sys.exit(0)

if __name__ == "__main__":
    main()
