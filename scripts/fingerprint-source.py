#!/usr/bin/env python3
"""Print a streaming SHA-256 fingerprint for one local source artifact."""

import argparse
import hashlib
import sys
from pathlib import Path


CHUNK_SIZE = 1024 * 1024


def fingerprint(path: Path) -> tuple[int, str]:
    digest = hashlib.sha256()
    size = 0

    with path.open("rb") as source:
        while chunk := source.read(CHUNK_SIZE):
            size += len(chunk)
            digest.update(chunk)

    return size, digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Print the path, byte size, and SHA-256 of one source file."
    )
    parser.add_argument("path", type=Path, help="source file to fingerprint")
    args = parser.parse_args()

    try:
        size, sha256 = fingerprint(args.path)
    except OSError as error:
        print(f"error: cannot read '{args.path}': {error}", file=sys.stderr)
        return 1

    print(f"path: {args.path}")
    print(f"size_bytes: {size}")
    print(f"sha256: {sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
