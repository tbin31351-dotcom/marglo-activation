#!/usr/bin/env python3
"""Add / remove / list activated HWIDs in activated.txt (works in Termux too).

  python manage.py add    A1B2-C3D4-E5F6-0789 "Ali - 26 Oct"
  python manage.py remove A1B2-C3D4-E5F6-0789
  python manage.py list
"""
import re, sys, pathlib

FILE = pathlib.Path(__file__).with_name("activated.txt")
PAT = re.compile(r"^[0-9A-F]{4}(-[0-9A-F]{4}){3}$")

def norm(h): return h.strip().upper()

def lines(): return FILE.read_text(encoding="utf-8").splitlines()

def ids():
    return [l.split("#")[0].strip().upper() for l in lines() if l.strip() and not l.lstrip().startswith("#")]

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("add", "remove", "list"):
        print(__doc__); sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "list":
        print("\n".join(ids()) or "(empty)"); return
    if len(sys.argv) < 3: print(__doc__); sys.exit(1)
    h = norm(sys.argv[2])
    if not PAT.match(h):
        sys.exit(f"Invalid HWID '{h}'. Expected XXXX-XXXX-XXXX-XXXX (hex).")
    if cmd == "add":
        if h in ids(): sys.exit("Already activated.")
        note = sys.argv[3] if len(sys.argv) > 3 else ""
        FILE.write_text("\n".join(lines() + [f"{h}  # {note}".rstrip(" #")]) + "\n", encoding="utf-8")
        print("Activated:", h)
    else:
        keep = [l for l in lines() if l.split("#")[0].strip().upper() != h]
        if len(keep) == len(lines()): sys.exit("HWID not found.")
        FILE.write_text("\n".join(keep) + "\n", encoding="utf-8")
        print("Revoked:", h)

main()
