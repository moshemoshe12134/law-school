#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path


KEEP_EXTS = {
    ".md",
    ".markdown",
    ".mdx",
    ".txt",
    ".json",
    ".yml",
    ".yaml",
    ".csv",
    ".tsv",
    ".py",
    ".sh",
}

SKIP_DIR_NAMES = {"converted_md", "original_sources"}
SKIP_FILE_NAMES = {".DS_Store"}


def _is_under(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except Exception:
        return False


def _unique_dest_path(dest: Path) -> Path:
    if not dest.exists():
        return dest

    stem = dest.stem
    suffix = dest.suffix
    parent = dest.parent
    for i in range(1, 10_000):
        candidate = parent / f"{stem}__dup{i}{suffix}"
        if not candidate.exists():
            return candidate
    raise RuntimeError(f"Could not find unique destination for: {dest}")


def _safe_move(src: Path, dest: Path, dry_run: bool) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    final_dest = _unique_dest_path(dest)
    if dry_run:
        return final_dest
    final_dest.parent.mkdir(parents=True, exist_ok=True)
    os.replace(src, final_dest)
    return final_dest


def _prune_empty_dirs(root: Path, protected: set[Path], dry_run: bool) -> None:
    # Walk bottom-up.
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        p = Path(dirpath)
        if p in protected:
            continue
        if any((p / name) in protected for name in dirnames):
            continue
        if filenames:
            continue
        # If directory is empty, remove it.
        try:
            if dry_run:
                continue
            p.rmdir()
        except OSError:
            pass


def _merge_converted_md(sources_dir: Path, dry_run: bool) -> list[tuple[Path, Path]]:
    converted_dir = sources_dir / "converted_md"
    if not converted_dir.exists():
        return []

    original_sources_dir = sources_dir / "original_sources"
    conflict_root = original_sources_dir / "_converted_md_conflicts"

    moves: list[tuple[Path, Path]] = []
    for dirpath, _, filenames in os.walk(converted_dir):
        dirpath_p = Path(dirpath)
        rel_dir = dirpath_p.relative_to(converted_dir)
        for filename in filenames:
            if filename in SKIP_FILE_NAMES:
                continue
            src = dirpath_p / filename
            rel = rel_dir / filename
            dest = sources_dir / rel
            if dest.exists():
                conflict_dest = conflict_root / rel
                final_dest = _safe_move(src, conflict_dest, dry_run=dry_run)
                moves.append((src, final_dest))
            else:
                final_dest = _safe_move(src, dest, dry_run=dry_run)
                moves.append((src, final_dest))

    # Remove emptied subdirectories under converted_md (but keep the folder itself).
    protected = {converted_dir}
    _prune_empty_dirs(converted_dir, protected=protected, dry_run=dry_run)

    # Leave a small note for humans/agents.
    readme = converted_dir / "README.md"
    note = (
        "# converted_md (deprecated)\n\n"
        "Converted markdown/text sources have been promoted to the parent `01_SOURCES/` folder.\n\n"
        "If you were looking for converted materials, start in the parent directory.\n"
    )
    if dry_run:
        return moves
    try:
        if not readme.exists():
            readme.write_text(note, encoding="utf-8")
    except Exception:
        pass

    return moves


def _move_originals_to_original_sources(sources_dir: Path, dry_run: bool) -> list[tuple[Path, Path]]:
    original_sources_dir = sources_dir / "original_sources"
    original_sources_dir.mkdir(parents=True, exist_ok=True)

    moves: list[tuple[Path, Path]] = []

    for dirpath, dirnames, filenames in os.walk(sources_dir):
        dirpath_p = Path(dirpath)

        # Skip walking into converted_md/original_sources.
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIR_NAMES]

        for filename in filenames:
            if filename in SKIP_FILE_NAMES:
                continue
            src = dirpath_p / filename
            if _is_under(src, original_sources_dir):
                continue
            if _is_under(src, sources_dir / "converted_md"):
                continue

            ext = src.suffix.lower()
            if ext in KEEP_EXTS:
                continue

            rel = src.relative_to(sources_dir)
            dest = original_sources_dir / rel
            final_dest = _safe_move(src, dest, dry_run=dry_run)
            moves.append((src, final_dest))

    protected = {sources_dir, sources_dir / "converted_md", original_sources_dir}
    _prune_empty_dirs(sources_dir, protected=protected, dry_run=dry_run)

    return moves


def _iter_course_sources_dirs(active_root: Path) -> list[Path]:
    sources_dirs: list[Path] = []
    if not active_root.exists():
        return sources_dirs
    for course_dir in sorted(p for p in active_root.iterdir() if p.is_dir()):
        sources_dir = course_dir / "01_SOURCES"
        if sources_dir.exists() and sources_dir.is_dir():
            sources_dirs.append(sources_dir)
    return sources_dirs


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Promote converted markdown/text sources to `01_SOURCES/` and move binary originals "
            "into `01_SOURCES/original_sources/`."
        )
    )
    parser.add_argument(
        "--active-root",
        default="ACTIVE",
        help="Root directory containing course folders (default: ACTIVE).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without moving files.",
    )
    args = parser.parse_args()

    repo_root = Path.cwd()
    active_root = (repo_root / args.active_root).resolve()
    sources_dirs = _iter_course_sources_dirs(active_root)
    if not sources_dirs:
        print(f"No course `01_SOURCES` directories found under: {active_root}")
        return 1

    for sources_dir in sources_dirs:
        print(f"\n==> {sources_dir}")

        merged = _merge_converted_md(sources_dir, dry_run=args.dry_run)
        if merged:
            print(f"  merged from converted_md: {len(merged)} files")

        moved = _move_originals_to_original_sources(sources_dir, dry_run=args.dry_run)
        if moved:
            print(f"  moved originals: {len(moved)} files")

        if args.dry_run:
            # Show a small sample for confidence.
            for src, dest in (merged + moved)[:10]:
                print(f"  would move: {src} -> {dest}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
