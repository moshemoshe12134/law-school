# Review Index — Property

**Purpose:** Track transcript availability, review status, and integration progress.

**Last Updated:** 2026-01-22

---

## Quick Stats

| Metric | Count |
|--------|-------|
| Total Classes Scheduled | 2 |
| Transcripts Available | 1 |
| Reviews Completed | 1 |
| Sources Extracted | 0 |
| Prewrites Generated | 0 |

---

## Pending Queue

> Transcripts waiting to be processed (oldest first)

| Priority | Date | File | Matched Class | Status | Notes |
|----------|------|------|---------------|--------|-------|

*(empty)*

---

## Completed Reviews

| Class# | Date | Title | Transcript File | Review File | Sources Added | Prewrites | Completed |
|--------|------|-------|-----------------|-------------|---------------|-----------|-----------|
| 1 | 2026-01-20 | First Possession — Wild Animals and (Intro) Custom | `03_TRANSCRIPTS/raw/Property-transcript-01-20.txt` | `04_REVIEWS/2026-01-20_class01_review.md` | 0 | 0 | 2026-01-22 |

---

## Unmatched Transcripts

> Files in `03_TRANSCRIPTS/raw/` that couldn't be auto-matched to a class

| File | Date Extracted | Probable Match | Action Needed |
|------|----------------|----------------|---------------|

*(none)*

---

## Status Codes

- `unprocessed` — Transcript downloaded but not registered
- `pending` — Registered, awaiting review creation
- `in_progress` — Review being created
- `review_done` — Review completed
- `integrated` — Sources table + outline updated
- `prewrites_done` — Prewrite fragments extracted

---

## Transcript Matching Rules

This index uses **date-based matching** to pair transcripts with classes:

1. Extract date from transcript filename (supports `YYYY-MM-DD` or `MM-DD` anywhere in the filename)
2. Look up date in MASTER_LOG to find class number and title (if filename only has `MM-DD`, match on month/day)
3. If no exact match, flag in "Unmatched Transcripts" for manual resolution
4. Alternative filename patterns supported:
   - `{CourseName}-transcript-MM-DD.txt` (preferred; e.g., `Property-transcript-01-20.txt`)
   - `{CourseName}-transcript-YYYY-MM-DD.txt`
   - `YYYY-MM-DD_CourseName.txt` (e.g., `2025-09-02_CivPro.txt`)
   - `MM-DD-YYYY_*.txt` (alternate date format)

---

## Usage

**Scan for new transcripts:**
```
ingest transcripts [COURSE]
```

**Process pending reviews:**
```
review [COURSE]          # Process next pending transcript
review [COURSE] all      # Batch process all pending
```

**Check status:**
```
review status [COURSE]
```

---

*Template: law-school-common/03_TEMPLATES/review_index_template.md*
