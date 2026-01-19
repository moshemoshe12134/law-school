# Two‑Doc Prep System (Audio + Class Reference)

## What you’re optimizing for

You want to walk into each Harcourt class able to:
- Answer cold calls confidently (even with no reading).
- Track Harcourt’s “moves” (MPC close reading + policy/theory).
- Convert class time into exam-ready material with minimal effort.

This system produces **two deliverables per class** (and treats everything else as internal scaffolding).

---

## The two deliverables (per class)

### 1) Audio prep script (listen before class)
- **File**: `Lectures/Prep/Audio/YYYY-MM-DD_classNN_audio_prep.md`
- **Purpose**: TTS-friendly, conversational, “walk-in ready” framing.
- **Target length**: ~4,000–5,000 words (~25–30 minutes spoken).
- **What it must include**:
  - The *one* central question of the day (“what this class is really about”).
  - The minimal doctrine/policy you need to speak in class.
  - 5–10 likely cold-call prompts + short answer starters.
  - 2–3 hypos (tiny) to anchor the concepts.

### 2) Class reference (read/search during class)
- **File**: `Lectures/Prep/Reference/YYYY-MM-DD_classNN_class_reference.md`
- **Purpose**: Comprehensive, searchable, formatted for fast lookup mid‑Socratic dialogue.
- **What it must include**:
  - “Expected Harcourt questions” as Q→A blocks (with alternative plausible answers + how he might push back).
  - Core doctrine: rule statements + element breakdowns + MPC hooks.
  - Cases: concise briefs + the “why this case exists” + hypo-able trigger facts.
  - Policy/theory: thesis, arguments, critiques, and **exam‑ready** policy paragraphs.
  - A mini hypo bank (≥5) with best prosecution/defense angles.
  - Search terms + cross-links to past outlines / MPC supplement sections.

---

## Source hierarchy (when things conflict)
Use this priority order **every time**:
1. **Professor statements / class notes** (once you have them).
2. **Assigned primary law** (cases/statutes/MPC text you actually have).
3. **Syllabus assignment block** (`Admin/Syllabus/Assignments/...`) for what’s “in scope.”
4. **Past outlines** (`Admin/Sources/Past_Outlines/`) as priors (organization + emphasis).
5. **Treatises/summaries** (Dressler, keyed case summaries) as scaffolding.

If an assigned supplement is missing from the repo, the reference doc should **explicitly flag** it as missing and rely on priors + known themes (without pretending to quote it).

---

## Recommended generation order (per class)

### Default (highest accuracy)
1. Generate **class reference** first (it’s the source of truth for that day).
2. Generate **audio prep** by transforming the class reference into narrative.

### When you’re time-crunched (night before / morning of)
1. Generate **audio prep** first (minimum viable).
2. Generate **class reference** later (same day / weekend) and then patch audio if needed.

---

## Daily operating procedure (minimal time, no reading)

### Before class (15–25 minutes total)
1. Listen to that day’s audio prep at `1.5x–2.0x`.
2. Skim only the **Quick Navigation** section of the class reference so you know what to search.

### During class
1. Keep the **class reference** open; search it when called on.
2. Capture only “deltas” (what Harcourt emphasized, corrected, or reframed).

### After class (5 minutes)
Write a tiny debrief (can be voice-to-text) with:
- 3 things he *actually* cared about
- 1 doctrinal move (MPC syntax, element parsing, mens rea distribution, etc.)
- 1 policy move (what argument he rewarded)
- 1 “exam signal” (explicit or implied)

That’s enough for the agent to update the class reference + feed the outline system later.

---

## What you need in the repo for the system to be accurate

### Already present (good)
- Syllabus blocks + schedule: `Admin/Syllabus/`
- Core doctrine scaffolding: `Admin/Sources/Source_Material/`
- Past outlines (excellent priors): `Admin/Sources/Past_Outlines/`
- Audio/reference style guides: `Lectures/Prep/Style_Guides/`

### Missing or incomplete (limits accuracy)
Many syllabus “Supp.” readings and course links are not stored locally.

**Fix**: Save PDFs (or text) into `Admin/Sources/Source_Material/Supplement/` (or a subfolder) so the agent can quote/paraphrase reliably.

---

## Quality control (what “done” means)

### Audio prep must-pass
- Conversational, TTS‑friendly formatting (short paragraphs, no tables).
- Time estimates per section; total ~25–30 minutes.
- Explicit cold call questions + answer starters.

### Class reference must-pass
- Quick nav + search terms.
- Q→A blocks for predicted professor prompts.
- Case briefs + MPC hooks.
- ≥5 hypos with both-side arguments.
- Clear flags for missing sources (no silent guessing).
