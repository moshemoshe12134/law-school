#!/usr/bin/env python3
"""
Lightweight QC for prep/review markdown docs (structure + required sections).

Examples:
  python3 Admin/Scripts/qc_doc.py Lectures/Prep/Packets/2026-01-20_class01_prep.md
  python3 Admin/Scripts/qc_doc.py --type review Lectures/Reviews/2026-01-20_class01_review.md
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import List, Tuple


PREP_REQUIRED_HEADINGS = [
    "## 1) Assignment Snapshot",
    "## 2) MPC Parsing Sheet (primary)",
    "## 3) Policy / Theory Brief (co-primary; ~50% exam)",
    "## 4) Minimal Case Cards (tertiary)",
    "## 5) Cold Call / Co‑Counsel Script (2 minutes)",
    "## 6) Predictions (explicit + falsifiable)",
    "## 7) TA / Office Hours Questions (if any)",
]

REVIEW_REQUIRED_HEADINGS = [
    "## 1) What Actually Happened (5 bullets max)",
    "## 2) Deltas vs Prep Packet",
    "## 3) MPC “Moves” Harcourt Modeled",
    "## 4) Policy / Theory Integration",
    "## 5) Exam Signals",
    "## 6) Outline Inserts (copy-ready)",
    "## 7) Spaced Reinforcement (10–15 minutes later)",
]

AUDIO_REQUIRED_HEADINGS = [
    "## INTRO",
    "## COLD CALL PREP",
    "## CLOSING",
]

CLASS_REFERENCE_REQUIRED_HEADINGS = [
    "## QUICK NAVIGATION",
    "## CORE DOCTRINE",
    "## EXPECTED HARCOURT QUESTIONS (Q→A)",
    "## CASE BRIEFS",
    "## POLICY / THEORY",
    "## QUICK HYPOS",
    "## SEARCH TERMS",
]


def _detect_type(text: str) -> str:
    for line in text.splitlines():
        if line.strip().startswith("doc_type:"):
            v = line.split(":", 1)[1].strip()
            if v == "prep_packet":
                return "prep"
            if v == "review_doc":
                return "review"
            if v == "audio_prep":
                return "audio"
            if v == "class_reference":
                return "class_reference"
    return "unknown"


def _frontmatter_present(text: str) -> bool:
    lines = text.splitlines()
    return len(lines) >= 3 and lines[0].strip() == "---" and "---" in lines[1:]


def _frontmatter_keys_missing(text: str, keys: List[str]) -> List[str]:
    missing = []
    for k in keys:
        if k not in text:
            missing.append(k)
    return missing


def _headings_missing(text: str, headings: List[str]) -> List[str]:
    missing = []
    for h in headings:
        if h not in text:
            missing.append(h)
    return missing


def _qc(text: str, doc_type: str) -> Tuple[bool, List[str]]:
    issues: List[str] = []
    if not _frontmatter_present(text):
        issues.append("Missing YAML frontmatter (--- ... --- at top).")

    if doc_type == "prep":
        issues.extend(
            [f"Missing frontmatter key/token: {m}" for m in _frontmatter_keys_missing(text, ["doc_type:", "class_number:", "date:", "title:", "status:", "syllabus_assignment:"])]
        )
        issues.extend([f"Missing heading: {h}" for h in _headings_missing(text, PREP_REQUIRED_HEADINGS)])
    elif doc_type == "review":
        issues.extend(
            [f"Missing frontmatter key/token: {m}" for m in _frontmatter_keys_missing(text, ["doc_type:", "class_number:", "date:", "title:", "status:", "prep_packet:", "class_notes_raw:"])]
        )
        issues.extend([f"Missing heading: {h}" for h in _headings_missing(text, REVIEW_REQUIRED_HEADINGS)])
    elif doc_type == "audio":
        issues.extend(
            [
                f"Missing frontmatter key/token: {m}"
                for m in _frontmatter_keys_missing(
                    text,
                    ["doc_type:", "class_number:", "date:", "title:", "status:"],
                )
            ]
        )
        issues.extend(
            [f"Missing heading: {h}" for h in _headings_missing(text, AUDIO_REQUIRED_HEADINGS)]
        )
    elif doc_type == "class_reference":
        issues.extend(
            [
                f"Missing frontmatter key/token: {m}"
                for m in _frontmatter_keys_missing(
                    text,
                    ["doc_type:", "class_number:", "date:", "title:", "status:", "syllabus_assignment:"],
                )
            ]
        )
        issues.extend(
            [
                f"Missing heading: {h}"
                for h in _headings_missing(text, CLASS_REFERENCE_REQUIRED_HEADINGS)
            ]
        )
    else:
        issues.append(
            "Could not detect doc_type (expected doc_type: prep_packet|review_doc|audio_prep|class_reference)."
        )

    return (len(issues) == 0, issues)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="Markdown doc path")
    ap.add_argument(
        "--type",
        choices=["prep", "review", "audio", "class_reference"],
        help="Override doc type",
    )
    args = ap.parse_args()

    path = Path(args.path)
    text = path.read_text(encoding="utf-8")
    doc_type = args.type or _detect_type(text)

    ok, issues = _qc(text, doc_type)
    if ok:
        print("QC_PASS")
        return 0
    print("QC_FAIL")
    for issue in issues:
        print(f"- {issue}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
