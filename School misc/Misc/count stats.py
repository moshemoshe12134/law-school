"""
Name Frequency Charts from CSV files in a folder
---------------------------------------------------------
This script pulls all CSV files in a specific folder, aggregates
rows that contain first/last names, and plots the most common first names and
last names.

Quick start
1) pip install pandas matplotlib
2) Run:  python count\ stats.py --folder YOUR_FOLDER_PATH --top 25

Notes
- Columns expected (case-insensitive): "First Name" and "Last Name". If missing,
  the script will try to split a single "Name" column (last word = last name).
- Outputs two PNG files next to the script and shows the charts interactively.
"""

from __future__ import annotations
import argparse
import os
import sys
from dataclasses import dataclass
from typing import List
from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt


@dataclass
class NameRow:
    first: str
    last: str


def _normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Return a DataFrame with columns First Name / Last Name populated.

    Accepts (case-insensitive): First Name, Last Name; if missing, tries Name.
    """
    # Standardize column names (strip, lowercase)
    lower_cols = {c: c.strip().lower() for c in df.columns}
    df = df.rename(columns=lower_cols)

    # If we have first/last already
    first_col = next((c for c in df.columns if c.lower() in ("first name", "first_name", "firstname")), None)
    last_col = next((c for c in df.columns if c.lower() in ("last name", "last_name", "lastname", "surname")), None)

    if first_col and last_col:
        out = pd.DataFrame({
            "First Name": df[first_col].astype(str).str.strip(),
            "Last Name": df[last_col].astype(str).str.strip(),
        })
        return out

    # Otherwise try to split a single Name column
    name_col = next((c for c in df.columns if c.lower() in ("name", "full name", "full_name", "fullname")), None)
    if name_col:
        names = df[name_col].astype(str).str.strip()
        firsts: List[str] = []
        lasts: List[str] = []
        for val in names:
            parts = val.split()
            if len(parts) == 0:
                firsts.append("")
                lasts.append("")
            elif len(parts) == 1:
                firsts.append(parts[0])
                lasts.append("")
            else:
                # Heuristic: last token is last name
                firsts.append(" ".join(parts[:-1]))
                lasts.append(parts[-1])
        return pd.DataFrame({"First Name": firsts, "Last Name": lasts})

    # If nothing matches, return empty
    return pd.DataFrame({"First Name": [], "Last Name": []})


def _read_all_rows_from_csv_files(folder_path: str) -> pd.DataFrame:
    """Read all CSV files from folder, normalize and concatenate."""
    frames: List[pd.DataFrame] = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".csv"):
            filepath = os.path.join(folder_path, filename)
            try:
                df = pd.read_csv(filepath)
            except Exception as e:
                print(f"Warning: Failed to read {filepath}: {e}", file=sys.stderr)
                continue
            std = _normalize_columns(df)
            if not std.empty:
                frames.append(std)
    if frames:
        return pd.concat(frames, ignore_index=True)
    return pd.DataFrame({"First Name": [], "Last Name": []})


def _aggregate_from_folder(folder_path: str) -> List[NameRow]:
    df = _read_all_rows_from_csv_files(folder_path)
    rows: List[NameRow] = []
    for _, r in df.iterrows():
        first = str(r.get("First Name", "")).strip()
        last = str(r.get("Last Name", "")).strip()
        if first or last:
            rows.append(NameRow(first=first, last=last))
    return rows


def _plot_bar(counts: Counter, title: str, top_n: int, outfile: str) -> None:
    data = counts.most_common(top_n)
    if not data:
        print(f"No data to plot for {title}.")
        return
    labels, values = zip(*data)

    plt.figure(figsize=(14, 7))
    bars = plt.bar(range(len(labels)), values, alpha=0.9)
    plt.title(title, fontsize=16, fontweight="bold")
    plt.ylabel("Frequency")
    plt.xticks(range(len(labels)), labels, rotation=45, ha="right")

    # Value labels
    for b in bars:
        h = b.get_height()
        plt.text(b.get_x() + b.get_width() / 2, h, f"{int(h)}", ha="center", va="bottom")

    plt.tight_layout()
    plt.savefig(outfile, dpi=200)
    plt.show()
    print(f"Saved: {outfile}")


def main():
    ap = argparse.ArgumentParser(description="Aggregate name frequencies from CSV files in a folder.")
    ap.add_argument("--folder", required=False, default=".",
                   help="Folder path containing CSV files.")
    ap.add_argument("--top", type=int, default=25, help="Top N names to display.")
    args = ap.parse_args()

    folder_path = args.folder.strip()
    if not os.path.isdir(folder_path):
        print(f"ERROR: Folder path '{folder_path}' does not exist or is not a directory.", file=sys.stderr)
        sys.exit(1)

    rows = _aggregate_from_folder(folder_path)
    if not rows:
        print("No rows found. Exiting.")
        sys.exit(0)

    # Build counters
    first_counts = Counter([r.first for r in rows if r.first])
    last_counts = Counter([r.last for r in rows if r.last])

    total = len(rows)
    print(f"Total rows aggregated: {total}")
    print(f"Unique first names: {len(first_counts)} | Unique last names: {len(last_counts)}")

    # Plot
    _plot_bar(first_counts, f"Top {args.top} First Names", args.top, "top_first_names.png")
    _plot_bar(last_counts, f"Top {args.top} Last Names", args.top, "top_last_names.png")

    # Print quick tables
    print("\nTop First Names:")
    for i, (name, c) in enumerate(first_counts.most_common(args.top), 1):
        print(f"{i:2d}. {name} — {c}")

    print("\nTop Last Names:")
    for i, (name, c) in enumerate(last_counts.most_common(args.top), 1):
        print(f"{i:2d}. {name} — {c}")


if __name__ == "__main__":
    main()
