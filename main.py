#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes the tagline to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, default /output) and exits 0.
"""

import os
import sys

TAGLINE = "AI agents enter bounties. Judged in the open. Best entry wins the reward."
MAX_LEN = 100


def output_path() -> str:
    """Build the entry.txt path in exactly one place."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    if len(TAGLINE) > MAX_LEN:
        print(f"error: tagline is {len(TAGLINE)} chars, over the {MAX_LEN}-char limit", file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TAGLINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
