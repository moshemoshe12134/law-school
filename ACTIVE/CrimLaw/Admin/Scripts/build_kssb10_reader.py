#!/usr/bin/env python3
"""
Build a per-class KSSB10 page list from the extracted syllabus artifacts.

Reads:
  - Admin/Syllabus/Class_Schedule.csv
  - Admin/Syllabus/Assignments/*.md

Writes:
  - Admin/Syllabus/KSSB10_Assigned_Pages.md
"""

from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Tuple


@dataclass(frozen=True)
class Kssb10Item:
    pages_raw: str
    description: str


@dataclass(frozen=True)
class ClassRow:
    class_number: int
    date: str
    day_of_week: str
    title: str
    assignment_path: Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _read_schedule(schedule_csv: Path) -> List[ClassRow]:
    rows: List[ClassRow] = []
    with schedule_csv.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(
                ClassRow(
                    class_number=int(r["class_number"]),
                    date=r["date"],
                    day_of_week=r["day_of_week"],
                    title=r["title"],
                    assignment_path=Path(r["assignment_path"]),
                )
            )
    rows.sort(key=lambda r: (r.date, r.class_number))
    return rows


def _extract_kssb10_items(assignment_md: Path) -> List[Kssb10Item]:
    items: List[Kssb10Item] = []
    text = assignment_md.read_text(encoding="utf-8", errors="replace")
    for line in text.splitlines():
        if "KSSB10" not in line:
            continue
        if not re.search(r"\bKSSB10\b", line):
            continue
        remainder = line.split("KSSB10", 1)[1].strip()
        parts = [p.strip() for p in re.split(r"\s{2,}", remainder) if p.strip()]
        if not parts:
            continue

        pages_raw = parts[0]
        description = parts[1] if len(parts) >= 2 else ""

        if len(parts) == 1:
            m = re.match(
                r"^([0-9][0-9\s\-–—,]*(?:\s+and\s+[0-9][0-9\s\-–—,]*)*)\s+(.*)$",
                remainder,
            )
            if m:
                pages_raw = m.group(1).strip()
                description = m.group(2).strip()

        items.append(Kssb10Item(pages_raw=pages_raw, description=description))
    return items


def _normalize_range_end(start: int, end_raw: str) -> int:
    end = int(end_raw)
    if end >= start:
        return end
    start_s = str(start)
    if len(end_raw) < len(start_s):
        return int(start_s[: -len(end_raw)] + end_raw)
    return end


def _parse_pages_field(pages_raw: str) -> List[Tuple[int, int]]:
    s = pages_raw.replace("–", "-").replace("—", "-")
    chunks = re.split(r"\s*(?:,|and)\s*", s)
    ranges: List[Tuple[int, int]] = []
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
        m = re.fullmatch(r"(\d+)\s*-\s*(\d+)", chunk)
        if m:
            start = int(m.group(1))
            end = _normalize_range_end(start, m.group(2))
            ranges.append((start, end))
            continue
        m = re.fullmatch(r"(\d+)", chunk)
        if m:
            p = int(m.group(1))
            ranges.append((p, p))
            continue
    return ranges


def _merge_ranges(ranges: Iterable[Tuple[int, int]]) -> List[Tuple[int, int]]:
    sorted_ranges = sorted((min(a, b), max(a, b)) for a, b in ranges)
    merged: List[Tuple[int, int]] = []
    for start, end in sorted_ranges:
        if not merged:
            merged.append((start, end))
            continue
        prev_start, prev_end = merged[-1]
        if start <= prev_end + 1:
            merged[-1] = (prev_start, max(prev_end, end))
        else:
            merged.append((start, end))
    return merged


def _format_ranges(ranges: Iterable[Tuple[int, int]]) -> str:
    parts: List[str] = []
    for start, end in ranges:
        parts.append(str(start) if start == end else f"{start}-{end}")
    return ", ".join(parts)


def _build_markdown(schedule: List[ClassRow], repo_root: Path) -> str:
    per_class: List[Tuple[ClassRow, List[Kssb10Item]]] = []
    all_ranges: List[Tuple[int, int]] = []

    for row in schedule:
        assignment_path = (repo_root / row.assignment_path).resolve()
        items = _extract_kssb10_items(assignment_path)
        per_class.append((row, items))
        for item in items:
            all_ranges.extend(_parse_pages_field(item.pages_raw))

    merged_all = _merge_ranges(all_ranges)
    lines: List[str] = []
    lines.append("# KSSB10 Assigned Pages (By Class Day)")
    lines.append("")
    lines.append(
        "This file lists the syllabus-assigned KSSB10 page ranges by class day (no textbook text included)."
    )
    lines.append("")
    lines.append("## All Assigned KSSB10 Pages (Merged)")
    lines.append("")
    lines.append(_format_ranges(merged_all) if merged_all else "(none found)")
    lines.append("")
    lines.append("## By Class")
    lines.append("")

    for row, items in per_class:
        if not items:
            continue
        lines.append(
            f"### Class #{row.class_number:02d} — {row.day_of_week}, {row.date} — {row.title}"
        )
        lines.append("")
        for item in items:
            desc = f" — {item.description}" if item.description else ""
            lines.append(f"- KSSB10 {item.pages_raw}{desc}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main(argv: List[str]) -> int:
    repo_root = _repo_root()
    schedule_csv = repo_root / "Admin/Syllabus/Class_Schedule.csv"
    if not schedule_csv.exists():
        print(f"ERROR: Missing: {schedule_csv}", file=sys.stderr)
        return 2

    schedule = _read_schedule(schedule_csv)
    out_path = repo_root / "Admin/Syllabus/KSSB10_Assigned_Pages.md"
    out_path.write_text(_build_markdown(schedule, repo_root), encoding="utf-8")
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
