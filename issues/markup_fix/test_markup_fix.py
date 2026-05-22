"""Synthetic tests for 08_markup_fix.py (ApteES)."""
import sys; sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent))
from importlib import import_module
mod = import_module("08_markup_fix")
fix_nested_ab, fix_trim_whitespace = mod.fix_nested_ab, mod.fix_trim_whitespace
PASS = FAIL = 0
def check(desc, got, want):
    global PASS, FAIL
    if got == want: print(f"  PASS  {desc}"); PASS += 1
    else: print(f"  FAIL  {desc}\n        got:  {got!r}\n        want: {want!r}"); FAIL += 1

print("=== nested <ab> (guard) ===")
line, n = fix_nested_ab("<ab><ab>X</ab></ab>"); check("dup flat", line, "<ab>X</ab>"); check("dup n", n, 1)
line, n = fix_nested_ab("<ab>clean</ab>"); check("no-op", line, "<ab>clean</ab>"); check("no-op n", n, 0)

print("=== whitespace trim ===")
line, n = fix_trim_whitespace("<s> word </s>")
check("<s> trim", line, "<s>word</s>")
check("<s> trim n>=1", n>=1, True)
line, n = fix_trim_whitespace("<s>clean</s>")
check("<s> no-op", line, "<s>clean</s>")
check("<s> no-op n", n, 0)
print(f"\n{'='*40}\nResults: {PASS}/{PASS+FAIL} passed", ("v" if FAIL==0 else "x"))
if FAIL: sys.exit(1)
