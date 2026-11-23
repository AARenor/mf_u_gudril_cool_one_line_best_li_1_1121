#!/usr/bin/env python3
"""Write one short text for the make.fun bounty u-gudril-cool-one-line-best-line-b8c41f4d.

Python 3.13, standard library only, no network.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = "The waiting-room fish has a name tag on his bowl: Gerald. Gerald has been dead since Tuesday. The tag is new."


def output_dir() -> Path:
    """Return the folder the entry text is written into.

    MAKEFUN_OUTPUT_DIR wins; OUTPUT_DIR is accepted as a fallback; /output
    is used when neither is set.
    """
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"
    folder = output_dir()
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / "entry.txt"
    path.write_bytes(TEXT.encode("utf-8"))
    print(f"{len(TEXT)} characters", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
