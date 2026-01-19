#!/usr/bin/env python3
"""
Finds the next class in Admin/Master_Log.md for a given pipeline stage.

Examples:
  python3 Admin/Scripts/next_class.py prep
  python3 Admin/Scripts/next_class.py review
  python3 Admin/Scripts/next_class.py outline
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional


@dataclass(frozen=True)
class Row:
    data: Dict[str, str]

    def get(self, key: str) -> str:
        return (self.data.get(key) or "").strip()


def _strip_ticks(value: str) -> str:
    v = value.strip()
    if v.startswith("`") and v.endswith("`") and len(v) >= 2:
        return v[1:-1]
    return v


def _parse_master_log(master_log: Path) -> List[Row]:
    text = master_log.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Find the Class Pipeline header row.
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "## Class Pipeline":
            start_idx = i
            break
    if start_idx is None:
        raise SystemExit("Could not find '## Class Pipeline' section in Master_Log.md")

    # Find the first table header line after the section heading.
    header_line = None
    header_idx = None
    for i in range(start_idx + 1, len(lines)):
        if lines[i].startswith("|") and "Class#" in lines[i]:
            header_line = lines[i]
            header_idx = i
            break
    if header_line is None or header_idx is None:
        raise SystemExit("Could not find table header row under '## Class Pipeline'")

    headers = [c.strip() for c in header_line.strip().strip("|").split("|")]

    rows: List[Row] = []
    for line in lines[header_idx + 2 :]:
        if not line.startswith("|"):
            break
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != len(headers):
            continue
        data = dict(zip(headers, cells))
        rows.append(Row(data=data))
    return rows


def _date_leq_today(date_iso: str) -> bool:
    try:
        d = dt.date.fromisoformat(date_iso)
    except ValueError:
        return False
    return d <= dt.date.today()


def _select(rows: List[Row], stage: str) -> Optional[Row]:
    stage = stage.lower()
    if stage == "prep":
        for r in rows:
            if r.get("Prep Status") == "todo":
                return r
        return None

    if stage == "review":
        for r in rows:
            if r.get("Review Status") != "todo":
                continue
            if r.get("Prep Status") != "final":
                continue
            date_iso = r.get("Date")
            if date_iso and not _date_leq_today(date_iso):
                continue
            notes_path = _strip_ticks(r.get("Notes"))
            if notes_path and not Path(notes_path).exists():
                continue
            return r
        return None

    if stage == "outline":
        for r in rows:
            if r.get("Review Status") != "final":
                continue
            if r.get("Outline Updated") != "N":
                continue
            return r
        return None

    raise SystemExit(f"Unknown stage: {stage}. Use prep|review|outline.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", nargs="?", default="prep", help="prep|review|outline")
    ap.add_argument(
        "--master-log",
        default="Admin/Master_Log.md",
        help="Path to Master_Log.md",
    )
    args = ap.parse_args()

    master_log = Path(args.master_log)
    rows = _parse_master_log(master_log)
    row = _select(rows, args.stage)
    if row is None:
        print("NONE")
        return 1

    # Print a stable, easy-to-copy summary.
    class_no = row.get("Class#")
    date_iso = row.get("Date")
    title = row.get("Title")
    assignment = _strip_ticks(row.get("Assignment"))
    prep_doc = _strip_ticks(row.get("Prep Doc"))
    review_doc = _strip_ticks(row.get("Review Doc"))
    notes = _strip_ticks(row.get("Notes"))

    print(f"class_number={class_no}")
    print(f"date={date_iso}")
    print(f"title={title}")
    print(f"assignment={assignment}")
    print(f"prep_doc={prep_doc}")
    print(f"review_doc={review_doc}")
    print(f"notes={notes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
