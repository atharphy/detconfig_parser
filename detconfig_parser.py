#!/usr/bin/env python3
import re, sys, os
from pathlib import Path
from datetime import datetime

DISABLE = {"noinit", "noanalogsignal"}
ROOT = Path("/pixelscratch/pixelscratch/config/Pix/detconfig")

def ts(path: Path):
    try:
        return datetime.fromtimestamp(os.stat(path).st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return "n/a"

def compress(nums):
    nums = sorted(set(int(x) for x in nums))
    if not nums:
        return ""
    out = []
    s = e = nums[0]
    for n in nums[1:]:
        if n == e + 1:
            e = n
        else:
            out.append((s, e))
            s = e = n
    out.append((s, e))
    return ",".join(f"{a}" if a == b else f"{a}:{b}" for a, b in out)

def parse_file(path: Path):
    comps = {}
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for ln in f:
            parts = ln.strip().split()
            if len(parts) > 1 and parts[1].lower() in DISABLE:
                name = parts[0]
                i = name.rfind("_ROC")
                if i == -1:
                    continue
                comp = name[:i]
                n = name[i+4:]
                if n.isdigit():
                    comps.setdefault(comp, set()).add(int(n))
    return comps

_LYR = re.compile(r'(?:^|_)LYR([1-4])(?:_|$)')
_RNG = re.compile(r'(?:^|_)RNG([1-2])(?:_|$)')

def section_key(comp):
    if "BPix" in comp:
        m = _LYR.search(comp)
        if m: return ("Layer", int(m.group(1)))
    if "FPix" in comp:
        m = _RNG.search(comp)
        if m: return ("Ring", int(m.group(1)))
    return ("Other", 0)

def build_by_component(files_data):
    by_comp = {}
    for label, comps in files_data.items():
        for comp, rocs in comps.items():
            by_comp.setdefault(comp, {})[label] = rocs
    return by_comp

def print_section(title, comps, labels, out):
    print(f"---+++ {title}", file=out)
    hdr = "| *detector component* | *ROCs* " + "".join(f"| *{lab}* " for lab in labels) + "|"
    print(hdr, file=out)
    for comp in sorted(comps):
        per_label = comps[comp]
        groups = {}
        for lab in labels:
            spec = compress(per_label.get(lab, set()))
            if spec:
                groups.setdefault(spec, []).append(lab)
        if not groups:
            continue
        for spec, labs in sorted(groups.items()):
            row = f"| {comp} | {spec} "
            for lab in labels:
                row += "| x " if lab in labs else "|   "
            row += "|"
            print(row, file=out)
    print("", file=out)

def generate(runs, out):
    files = []
    for r in runs:
        p = ROOT / r / "detectconfig.dat"
        if p.exists():
            files.append((r, p))
    if not files:
        return
    labels = [r for r, _ in files]
    print("---+++ detconfig timestamps", file=out)
    for r, p in files:
        print(f"| *{r}* | {ts(p)} |", file=out)
    print("", file=out)
    files_data = {r: parse_file(p) for r, p in files}
    by_comp = build_by_component(files_data)
    sections = {}
    for comp, per_label in by_comp.items():
        kind, idx = section_key(comp)
        key = f"{kind} {idx}" if kind != "Other" else "Other"
        sections.setdefault(key, {})[comp] = per_label
    for lyr in range(1, 5):
        key = f"Layer {lyr}"
        if key in sections: print_section(key, sections[key], labels, out)
    for rng in range(1, 3):
        key = f"Ring {rng}"
        if key in sections: print_section(key, sections[key], labels, out)
    if "Other" in sections: print_section("Other", sections["Other"], labels, out)

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    args = sys.argv[1:]
    out_file = None
    if "-o" in args:
        i = args.index("-o")
        if i + 1 < len(args):
            out_file = args[i + 1]
            del args[i:i+2]
    runs = [r for r in args if r.isdigit()]
    if not runs:
        sys.exit(1)
    if out_file:
        with open(out_file, "w") as f:
            generate(runs, f)
        print(f"Saved output to {out_file}")
    else:
        generate(runs, sys.stdout)

if __name__ == "__main__":
    main()
