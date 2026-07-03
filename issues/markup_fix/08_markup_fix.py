"""
Markup fixer + audit for ae.txt (ApteES).
Counterpart of PWG#175, PWK#113, and siblings.

ApteES-specific notes: 0 whitespace hits. <s> main tag (72,856). 3 non-standard <ab n>.

Inputs: ../../../csl-orig/v02/ae/ae.txt
        or argv[1] (any path)
Outputs: ae_fixed.txt, markup_fix_changes.txt, markup_audit.txt
"""
import sys, re
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")

HERE = Path(__file__).resolve().parent
if len(sys.argv) >= 3:
    PW_TXT, OUT_FIX = Path(sys.argv[1]), Path(sys.argv[2])
else:
    candidates = [HERE.parent.parent.parent / "csl-orig" / "v02" / "ae" / "ae.txt", HERE / "ae.txt"]
    PW_TXT = next((p for p in candidates if p.exists()), candidates[0])
    OUT_FIX = HERE / "ae_fixed.txt"
OUT_LOG, OUT_AUDIT = HERE / "markup_fix_changes.txt", HERE / "markup_audit.txt"

NEST_RX = re.compile(r"<ab(?P<oa>\b[^>]*)>(?P<pre>[^<]*)<ab(?P<ia>\b[^>]*)>(?P<inner>[^<]*)</ab>(?P<post>[^<]*)</ab>")

def fix_nested_ab(line):
    n = 0
    while True:
        m = NEST_RX.search(line)
        if not m: return line, n
        line = line[:m.start()] + f"<ab{m.group('oa')}>{m.group('pre')}{m.group('inner')}{m.group('post')}</ab>" + line[m.end():]
        n += 1

TRIM_TAGS = ['s', 'ab', 'lex', 'i', 'ls']

def fix_trim_whitespace(line):
    n = 0
    for tag in TRIM_TAGS:
        p1 = re.compile(rf"(<{tag}\b[^>]*>)(\s+)([^<]*?)(\s*)(</{tag}>)")
        def _r1(m):
            nonlocal n
            inside = m.group(3).rstrip()
            if inside != m.group(2)+m.group(3)+m.group(4): n += 1
            return f"{m.group(1)}{inside}{m.group(5)}"
        line = p1.sub(_r1, line)
        p2 = re.compile(rf"(<{tag}\b[^>]*>)([^<]*?)(\s+)(</{tag}>)")
        def _r2(m):
            nonlocal n
            inside = m.group(2).rstrip(); n += 1
            return f"{m.group(1)}{inside}{m.group(4)}"
        line = p2.sub(_r2, line)
    return line, n

def _ls_nested_classify(line):
    inside, outside = [], []
    for m in re.finditer(r"<ls\b[^>]*>([^<]*<ls\b[^>]*>)", line):
        io = m.group(1).find("<ls"); ip = m.start(1)+(io if io>=0 else 0)
        pfx = line[:ip]
        (inside if pfx.rfind("{{") > pfx.rfind("}}") else outside).append(m)
    return outside, inside

AUDIT_CHECKS = [
    ("Adjacent </ab> <ab>", re.compile(r"</ab>\s*<ab")),
    ("Nested <ls> outside correction record", None),
    ("Nested <ls> INSIDE correction record (informational)", None),
    ("<ab n=\"?\"> placeholder", re.compile(r'<ab\s+n="\?+">') ),
    ("<ab n=\"\"> empty attribute", re.compile(r'<ab\s+n="">') ),
    ("<ab n=\"..\"> non-standard expansion", re.compile(r'<ab\s+n="(?!")[^"]{2,}">') ),
    ("Empty content tag", re.compile(r"<(s|ab|lex|i|ls)\b[^>]*></\1>") if TRIM_TAGS else re.compile(r"(?!x)x")),
    ("{#}brace before <ab>/<ls>/<is>", re.compile(r"#\}<(?:ab|ls|is)\b")),
    ("{%}brace before <is>", re.compile(r"%\}<is\b")),
    ("</ls>.[Page glued", re.compile(r"</ls>\.\[Page\d")),
    ("Malformed tag", re.compile(r'<[A-Za-z][A-Za-z0-9]*\s+[A-Za-z]+="[^"]*<[^"]*"\s*[^>]*>')),
]

def main():
    print(f"Reading {PW_TXT} ...", flush=True)
    lines = PW_TXT.read_text(encoding="utf-8").splitlines()
    print(f"  {len(lines):,} lines", flush=True)
    out_lines, fix_log, tot_nested, tot_trim = [], [], 0, 0
    audit_hits = {label: [] for label, _ in AUDIT_CHECKS}
    for lineno, line in enumerate(lines, 1):
        orig = line
        line, n1 = fix_nested_ab(line); line, n2 = fix_trim_whitespace(line)
        tot_nested += n1; tot_trim += n2
        if line != orig: fix_log.append((lineno, orig, line))
        out_lines.append(line)
        outside_hits, inside_hits = _ls_nested_classify(orig)
        for m in outside_hits:
            s,e = max(0,m.start()-40), min(len(orig),m.end()+40)
            audit_hits["Nested <ls> outside correction record"].append((lineno, orig[s:e].replace("\t"," ")))
        for m in inside_hits:
            s,e = max(0,m.start()-40), min(len(orig),m.end()+40)
            audit_hits["Nested <ls> INSIDE correction record (informational)"].append((lineno, orig[s:e].replace("\t"," ")))
        for label, pat in AUDIT_CHECKS:
            if pat is None: continue
            for m in pat.finditer(orig):
                s,e = max(0,m.start()-40), min(len(orig),m.end()+40)
                audit_hits[label].append((lineno, orig[s:e].replace("\t"," ")))
                if len(audit_hits[label]) >= 5000: break
        if lineno % 200000 == 0: print(f"  {lineno:,}/{len(lines):,}", flush=True)
    print(f"nested={tot_nested} whitespace={tot_trim} changed={len(fix_log)}", flush=True)
    with OUT_FIX.open("w", encoding="utf-8", newline="\n") as f:
        for line in out_lines: f.write(line+"\n")
    with OUT_LOG.open("w", encoding="utf-8") as f:
        f.write(f"; markup_fix log for ae.txt\n; nested: {tot_nested}\n; whitespace: {tot_trim}\n; changed: {len(fix_log)}\n;\n")
        for ln,old,new in fix_log: f.write(f"{ln} old {old}\n{ln} new {new}\n")
    with OUT_AUDIT.open("w", encoding="utf-8") as f:
        f.write(f"ApteES markup audit\n" + "="*60 + "\n\n")
        f.write(f"Generated by 08_markup_fix.py against ae.txt.\n")
        f.write(f"Paired tags: <s>, <ab>, <lex>, <i>, <ls>\n")
        f.write(f"Notes: 0 whitespace hits. <s> main tag (72,856). 3 non-standard <ab n>.\n\n")
        f.write("AUTO-FIXES: nested <ab> + whitespace in <s>, <ab>, <lex>, <i>, <ls>\n\n")
        for label, _ in AUDIT_CHECKS:
            hits = audit_hits[label]
            f.write(f"## {label}\n   matches: {len(hits)} (showing up to 200)\n")
            for ln, snippet in hits[:200]: f.write(f"   L{ln}: {snippet}\n")
            f.write("\n")
    print("DONE", flush=True)

if __name__ == "__main__":
    main()
