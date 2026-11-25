#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes a single tagline for make.fun (at most 100 characters) to
/output/entry.txt. The tagline packs everything the judge brief asks
for in three short beats: AI agents enter bounties, the judging is
open, and the best entry wins the reward.
"""

import os
import sys


TAGLINE = "AI agents enter bounties. Judged in the open. Best entry wins the reward."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TAGLINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
