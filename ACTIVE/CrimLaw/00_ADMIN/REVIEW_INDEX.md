# Review Index — CrimLaw

**Purpose:** Track transcript availability, review status, and integration progress.

**Last Updated:** 2026-02-08

---

## Quick Stats

| Metric | Count |
|--------|-------|
| Total Classes Scheduled | 27 |
| Transcripts Available | 8 |
| Reviews Completed | 8 |
| Sources Extracted | TBD |
| Prewrites Generated | TBD |

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
| 1 | 2026-01-20 | Criminal Law and Justice | `03_TRANSCRIPTS/raw/Criminal Law-transcript-01-20.txt` | `04_REVIEWS/CrimLaw-Review-2026-01-20_class01_review.md` | 0 | 0 | 2026-01-22 |
| 2 | 2026-01-22 | Actus Reus | `03_TRANSCRIPTS/raw/Criminal Law-transcript-01-22.txt` | `04_REVIEWS/CrimLaw-Review-2026-01-22_class02_review.md` | 7 | 1 | 2026-01-22 |
| 3 | 2026-01-23 | Mens Rea | `03_TRANSCRIPTS/raw/Criminal Law-transcript-01-23.txt` | `04_REVIEWS/CrimLaw-Review-2026-01-23_class03_review.md` | TBD | TBD | TBD |
| 4 | 2026-01-27 | Intended Killings | `03_TRANSCRIPTS/raw/Criminal Law-transcript-01-27.txt` | `04_REVIEWS/CrimLaw-Review-2026-01-27_class04_review.md` | TBD | TBD | TBD |
| 5 | 2026-01-29 | Heat of Passion | `03_TRANSCRIPTS/raw/Criminal Law-transcript-01-29.txt` | `04_REVIEWS/CrimLaw-Review-2026-01-29_class05_review.md` | TBD | TBD | TBD |
| 6 | 2026-01-30 | Felony Murder | `03_TRANSCRIPTS/raw/Criminal Law-transcript-01-30.txt` | `04_REVIEWS/CrimLaw-Review-2026-01-30_class06_review.md` | TBD | TBD | TBD |
| 7 | 2026-02-03 | Unintended Killings | `03_TRANSCRIPTS/raw/Criminal Law-transcript-02-03.txt` | `04_REVIEWS/CrimLaw-Review-2026-02-03_class07_review.md` | TBD | TBD | TBD |
| 8 | 2026-02-05 | Issues of Causation | `03_TRANSCRIPTS/raw/Criminal Law-transcript-02-05.txt` | `04_REVIEWS/CrimLaw-Review-2026-02-05_class08_review.md` | TBD | TBD | TBD |
| 9 | 2026-02-10 | Reminder re. the Criminal Justice Process | `03_TRANSCRIPTS/raw/Criminal Law-transcript-02-10.txt` | `04_REVIEWS/CrimLaw-Review-2026-02-10_class09_review.md` | TBD | TBD | 2026-02-13 |
| 10 | 2026-02-12 | Michel Foucault, Discipline and Punish | `03_TRANSCRIPTS/raw/Criminal Law-transcript-02-12.txt` | `04_REVIEWS/CrimLaw-Review-2026-02-12_class10_review.md` | 0 | 0 | 2026-02-13 |

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
   - `{CourseName}-transcript-MM-DD.txt` (preferred; e.g., `Criminal Law-transcript-01-22.txt`)
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
