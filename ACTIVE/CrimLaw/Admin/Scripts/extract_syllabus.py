#!/usr/bin/env python3
"""
Extracts per-class assignment blocks from the Harcourt Criminal Law syllabus PDF.

Outputs:
  - Admin/Syllabus/Harcourt_CrimLaw_Syllabus_2026.txt (pdftotext output)
  - Admin/Syllabus/Class_Schedule.csv
  - Admin/Syllabus/Assignments/YYYY-MM-DD_classNN.md (one per class)

This is intentionally "lossy but useful": it captures the syllabus blocks that drive prep/review,
without trying to perfectly re-create the PDF layout.
"""

from __future__ import annotations

import csv
import dataclasses
import datetime as dt
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable, List, Optional


@dataclasses.dataclass(frozen=True)
class ClassEntry:
    class_number: int
    date: dt.date
    day_of_week: str
    title_raw: str
    title: str
    block_text: str
    mpc_sections: List[str]
    assignment_path: Path


MONTHS = {
    "JANUARY": 1,
    "JAN": 1,
    "FEBRUARY": 2,
    "FEB": 2,
    "MARCH": 3,
    "MAR": 3,
    "APRIL": 4,
    "APR": 4,
    "MAY": 5,
    "JUNE": 6,
    "JUN": 6,
    "JULY": 7,
    "JUL": 7,
    "AUGUST": 8,
    "AUG": 8,
    "SEPTEMBER": 9,
    "SEPT": 9,
    "SEP": 9,
    "OCTOBER": 10,
    "OCT": 10,
    "NOVEMBER": 11,
    "NOV": 11,
    "DECEMBER": 12,
    "DEC": 12,
}


CLASS_HEADER_RE = re.compile(
    r"""
    ^
    (?P<title>.*?)
    \s*
    \[
    \#\s*(?P<num>\d+)
    \s*[–-]\s*
    (?P<dow>[A-Za-z]+)\.?
    ,\s*(?P<month>[A-Za-z]+)\.?\s+(?P<day>\d{1,2})
    ,\s*(?P<year>\d{4})
    \]
    \s*$
    """,
    re.VERBOSE,
)


def _run_pdftotext(pdf_path: Path, out_txt_path: Path) -> None:
    out_txt_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["pdftotext", "-layout", str(pdf_path), str(out_txt_path)]
    subprocess.run(cmd, check=True)


def _normalize_text(raw: str) -> str:
    text = raw.replace("\f", "\n")
    lines: List[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            lines.append("")
            continue
        if stripped in {"Spring 2026"}:
            continue
        if stripped.startswith("Syllabus: Criminal Law"):
            continue
        if re.fullmatch(r"[.\u2026_—–-]{6,}", stripped):
            continue
        if re.fullmatch(r"\d+", stripped):
            continue
        lines.append(line.rstrip())
    normalized = "\n".join(lines)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized).strip() + "\n"
    return normalized


def _clean_title(title_raw: str) -> str:
    title = " ".join(title_raw.split())
    title = re.sub(r"^[IVXLC]+\.\s+", "", title)
    title = re.sub(r"^[A-Z]\.\s+", "", title)
    title = re.sub(r"^\d+\.\s+", "", title)
    return title.strip() or title_raw.strip()


def _extract_mpc_sections(block_text: str) -> List[str]:
    seen = set()
    sections: List[str] = []
    for line in block_text.splitlines():
        if "MPC" not in line.upper():
            continue
        for match in re.findall(r"\d+(?:\.\d+)?(?:\(\d+\))?", line):
            if match not in seen:
                seen.add(match)
                sections.append(match)
    return sections


def _parse_class_entries(
    normalized_text: str,
    syllabus_pdf_rel: str,
    assignments_dir: Path,
) -> List[ClassEntry]:
    lines = normalized_text.splitlines()
    header_idxs: List[int] = []
    header_matches: List[re.Match] = []
    for idx, line in enumerate(lines):
        m = CLASS_HEADER_RE.match(line)
        if not m:
            continue
        header_idxs.append(idx)
        header_matches.append(m)

    entries: List[ClassEntry] = []
    for i, (idx, m) in enumerate(zip(header_idxs, header_matches)):
        next_idx = header_idxs[i + 1] if i + 1 < len(header_idxs) else len(lines)
        block_lines = lines[idx:next_idx]
        block_text = "\n".join(block_lines).strip() + "\n"

        class_number = int(m.group("num"))
        day_of_week_raw = m.group("dow")
        day_of_week = _normalize_day_of_week(day_of_week_raw)
        month = _normalize_month(m.group("month"))
        day = int(m.group("day"))
        year = int(m.group("year"))
        date = dt.date(year, month, day)
        title_raw = (m.group("title") or "").strip()
        title = _clean_title(title_raw)
        mpc_sections = _extract_mpc_sections(block_text)

        assignment_filename = f"{date.isoformat()}_class{class_number:02d}.md"
        assignment_path = assignments_dir / assignment_filename

        frontmatter = [
            "---",
            f"class_number: {class_number}",
            f"date: {date.isoformat()}",
            f"day_of_week: {day_of_week}",
            f"title: {title}",
            f"title_raw: {title_raw}",
            f"syllabus_pdf: {syllabus_pdf_rel}",
            f"mpc_sections: [{', '.join(mpc_sections)}]",
            "---",
            "",
            f"# Class #{class_number} — {day_of_week}, {date.isoformat()} — {title}",
            "",
            "## Syllabus Extract (verbatim-ish)",
            "",
            block_text.strip(),
            "",
        ]
        assignment_path.parent.mkdir(parents=True, exist_ok=True)
        assignment_path.write_text("\n".join(frontmatter), encoding="utf-8")

        entries.append(
            ClassEntry(
                class_number=class_number,
                date=date,
                day_of_week=day_of_week,
                title_raw=title_raw,
                title=title,
                block_text=block_text,
                mpc_sections=mpc_sections,
                assignment_path=assignment_path,
            )
        )

    entries.sort(key=lambda e: (e.date, e.class_number))
    return entries


def _write_schedule_csv(entries: Iterable[ClassEntry], out_csv: Path) -> None:
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "class_number",
                "date",
                "day_of_week",
                "title",
                "assignment_path",
                "mpc_sections",
            ]
        )
        for e in entries:
            w.writerow(
                [
                    e.class_number,
                    e.date.isoformat(),
                    e.day_of_week,
                    e.title,
                    os.path.relpath(e.assignment_path, Path.cwd()),
                    ";".join(e.mpc_sections),
                ]
            )


def _normalize_month(month_raw: str) -> int:
    key = re.sub(r"[^A-Za-z]", "", month_raw).upper()
    if key not in MONTHS:
        raise KeyError(f"Unrecognized month: {month_raw!r}")
    return MONTHS[key]


def _normalize_day_of_week(day_raw: str) -> str:
    key = re.sub(r"[^A-Za-z]", "", day_raw).upper()
    mapping = {
        "MON": "Monday",
        "MONDAY": "Monday",
        "TUE": "Tuesday",
        "TUES": "Tuesday",
        "TUESDAY": "Tuesday",
        "WED": "Wednesday",
        "WEDS": "Wednesday",
        "WEDNESDAY": "Wednesday",
        "THU": "Thursday",
        "THUR": "Thursday",
        "THURS": "Thursday",
        "THURSDAY": "Thursday",
        "FRI": "Friday",
        "FRIDAY": "Friday",
        "SAT": "Saturday",
        "SATURDAY": "Saturday",
        "SUN": "Sunday",
        "SUNDAY": "Sunday",
    }
    if key not in mapping:
        # Fall back to human-ish capitalization.
        return (day_raw or "").strip().capitalize()
    return mapping[key]


def main(argv: List[str]) -> int:
    repo_root = Path.cwd()
    pdf_path = repo_root / "Admin/Sources/Source_Material/syllabus/Harcourt Criminal Law Syllabus 2026.pdf"
    if len(argv) >= 2:
        pdf_path = Path(argv[1]).expanduser()
        if not pdf_path.is_absolute():
            pdf_path = (repo_root / pdf_path).resolve()
    if not pdf_path.exists():
        print(f"ERROR: syllabus PDF not found at: {pdf_path}", file=sys.stderr)
        return 2

    syllabus_pdf_rel = os.path.relpath(pdf_path, repo_root)
    out_txt = repo_root / "Admin/Syllabus/Harcourt_CrimLaw_Syllabus_2026.txt"
    _run_pdftotext(pdf_path, out_txt)
    normalized = _normalize_text(out_txt.read_text(encoding="utf-8", errors="replace"))
    out_txt.write_text(normalized, encoding="utf-8")

    assignments_dir = repo_root / "Admin/Syllabus/Assignments"
    entries = _parse_class_entries(normalized, syllabus_pdf_rel, assignments_dir)
    if not entries:
        print(
            "ERROR: Found 0 class headers. The PDF format may have changed.",
            file=sys.stderr,
        )
        return 3

    schedule_csv = repo_root / "Admin/Syllabus/Class_Schedule.csv"
    _write_schedule_csv(entries, schedule_csv)
    print(f"Wrote: {out_txt}")
    print(f"Wrote: {schedule_csv}")
    print(f"Wrote: {assignments_dir} ({len(entries)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
