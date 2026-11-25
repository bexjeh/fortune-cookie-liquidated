#!/usr/bin/env python3
"""Fortune cookie for the liquidated trader — single-line entry writer."""
import os

FORTUNE = "The stars declare your fortune tonight: this cookie, the only asset you still own."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(FORTUNE)

if __name__ == "__main__":
    main()
