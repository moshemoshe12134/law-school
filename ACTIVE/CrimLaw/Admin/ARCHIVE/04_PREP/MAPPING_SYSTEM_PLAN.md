# Outline Mapping System Plan
**To align past outlines with daily classes without hallucination**

---

## THE PROBLEM

We need to map comprehensive outlines (organized by topic) to daily classes (organized by schedule). The challenge: **we must NOT summarize or paraphrase** outlines—that risks introducing inaccuracies. We must stay exactly true to the source material.

---

## THE SOLUTION: SPLIT MARKERS

Insert verbatim markers into outline files to indicate class boundaries. Preps will reference these markers to know which content applies.

### Marker Format
```
%% CLASS N START %%
[Outline content here - verbatim, unchanged]
%% CLASS N END %%
```

### Example
```markdown
# ACTUS REUS

%% CLASS 2 START %%

The commission of some voluntary act that is prohibited by law.

+----------+-----------------------------------------------------------+
| MPC      | **General Definitions.**                                  |
...

***Martin v. State* (AL 1944)**

- **Facts**: Martin was drunk on a highway...

[All Martin content]

***People v. Newton* (CA 1970)**

[All Newton content]

%% CLASS 2 END %%

%% CLASS 3 START %%

# MENS REA

[Mens rea content]
%% CLASS 3 END %%
```

---

## ADVANTAGES OF THIS APPROACH

1. **No hallucination**: We never rewrite or summarize outline content
2. **Verifiable**: Anyone can check that markers are in right place
3. **Reversible**: Markers can be added/removed without altering content
4. **Cross-referencable**: Preps link directly to markers
5. **Source-truth**: Outline remains single source of truth

---

## MAPPING WORKFLOW

### Step 1: Identify Class Topics
From [Class_Schedule.csv](../Admin/Syllabus/Class_Schedule.csv), extract:
- Class number
- Date
- Title
- MPC sections (if any)

### Step 2: Scan Outline for Matching Content
Read through outline(s) and identify where each class topic is covered.

**Example:**
- Class 2 (Actus Reus) → Outline sections "# ACTUS REUS" through Omissions, before Mens Rea
- Class 3 (Mens Rea) → Outline section "# MENS REA" through Hazelwood/Santillanes
- Class 4 (Intended Killings) → Outline subsection "# Intended Killings — Premeditation"

### Step 3: Insert Split Markers
Add `%% CLASS N START %%` and `%% CLASS N END %%` markers around relevant content.

**Important rules:**
- Markers go OUTSIDE headers (don't break header formatting)
- Content between markers remains VERBATIM
- Markers don't overlap (each section belongs to one class)
- When content spans multiple classes, split at logical break points

### Step 4: Create Mapping Metadata
In `sources_mapped/`, create a text file for each class:

```markdown
# Class 2 Source Mapping

## Primary Source
[Admin/Sources/Past_Outlines/Crim_Spring 2025_Harcourt_Full.docx.md](../../Outlines%20(past%20years)/Crim_Spring%202025_Harcourt_Full.docx.md)

## Markers
Start: Line 91 (after "# ACTUS REUS")
End: Line 404 (before "# MENS REA")

## Content Covered
- Actus Reus definition
- MPC §1.13(2), §1.13(9), §2.01
- Martin v. State
- People v. Newton
- People v. Decina
- Jones v. U.S.
- Omissions
- Time Framing (Kelman)

## Confirms With
- Syllabus: Admin/Syllabus/Assignments/2026-01-22_class02.md
- MPC sections: 1.13(2); 1.13(9); 2.01

## Additional Sources
- [Other outline name](path) — sections [X-Y] (optional backup)
```

---

## HANDLING OVERLAP AND GAPS

### Overlap (Same content in multiple outlines)
**Solution**: Use primary outline for mapping, note others as "supplementary" in mapping file.

Example:
- Primary: Crim_Spring 2025_Harcourt_Full.docx.md (most recent)
- Supplementary: Criminal Law_Spring 2023_Harcourt_Full Outline - Ilana Dutton.pdf.md (alternative perspective)

### Gaps (Topic not in outline)
**Solution**: Mark as "not in outline" in mapping file, note where content will come from (casebook, supplement, created fresh).

Example:
```markdown
## Gap Handling
Topic: "Reminder re. the Criminal Justice Process" (Class 9)
Status: Not covered in outlines
Source: KSSB10 1-19 (casebook), create fresh content
```

### Split Decisions (One topic spans multiple classes)
**Solution**: Split at logical break point within outline section.

Example: If Homicide spans Classes 4-8:
- Class 4: Intended Killings (stop before Felony Murder)
- Class 5: Heat of Passion (stop before Unintended Killings)
- Class 6: Felony Murder (stop before Causation intro)
- etc.

Markers reflect these splits:
```
%% CLASS 4 START %%
[Common Law Murder]
[Intended Killings - Premeditation]
%% CLASS 4 END %%

%% CLASS 5 START %%
[Intended Killings - Heat of Passion]
%% CLASS 5 END %%

%% CLASS 6 START %%
[Felony Murder]
%% CLASS 6 END %%
```

---

## PREP INTEGRATION

### Audio Prep
At end of audio prep, include:
```markdown
---

## SOURCE NOTE
This audio prep covers material from:
- [Crim_Spring 2025_Harcourt_Full.docx.md](../../Outlines%20(past%20years)/Crim_Spring%202025_Harcourt_Full.docx.md) — lines 91-404

For deeper dive, search in outline for: `%% CLASS 2 START %%`
```

### Class Reference
At end of class reference, include:
```markdown
---

## SOURCE MAPPING
**Primary outline**: [Crim_Spring 2025_Harcourt_Full.docx.md](../../Outlines%20(past%20years)/Crim_Spring%202025_Harcourt_Full.docx.md)

**Marker boundaries**:
- `%% CLASS 2 START %%` at line 91
- `%% CLASS 2 END %%` at line 404

**Full mapping file**: [sources_mapped/class_002_mapping.txt](sources_mapped/class_002_mapping.txt)
```

---

## VALIDATION PROTOCOLS

### Before Finalizing Markers

1. **Cross-check with syllabus**: Does content between markers match assigned reading?
2. **Cross-check with schedule**: Does it fit class time constraints?
3. **Check for gaps**: Any topics from assignment not in outline?
4. **Check for overlaps**: Any content assigned to multiple classes?
5. **Verify line numbers**: After insertion, do line numbers still match?

### After Inserting Markers

1. **Test search**: Can you search `%% CLASS N START %%` and find right spot?
2. **Test extraction**: If you copy from start to end marker, does it make sense?
3. **Test boundaries**: Does content flow naturally at boundaries?

### Peer Review (Optional but Recommended)

Have someone else verify:
- Markers in right locations
- No important content cut off
- Boundaries at logical breaks

---

## MARKER PLACEMENT RULES (Detailed)

### DO place markers:
- AFTER section headers (`##`, `###`)
- BEFORE next major topic starts
- Around complete case briefs
- Around complete MPC sections
- At logical thematic breaks

### DON'T place markers:
- In middle of sentences
- In middle of case briefs
- In middle of lists
- Inside tables (breaks formatting)
- Inside code blocks

### Examples

**GOOD placement:**
```markdown
## ACTUS REUS

The commission of some voluntary act...

***Martin v. State* (AL 1944)**

[Full case brief]

***People v. Newton* (CA 1970)***

%% CLASS 2 END %%

%% CLASS 3 START %%

# MENS REA

%% CLASS 3 END %%
```

**BAD placement:**
```markdown
The commission of some %% CLASS 2 END %% voluntary act...  <!-- NO -->
```

---

## IMPLEMENTATION ORDER

### Phase 1: Early Classes (Already Have Preps)
Classes 1-6, 8:
1. Read existing prep to identify topics covered
2. Scan outline for those topics
3. Insert markers
4. Create mapping files
5. Update preps with source references

### Phase 2: Remaining Classes
Classes 7, 9-27:
1. Read syllabus assignment
2. Scan outline for matching content
3. Insert markers
4. Create mapping files
5. Create audio + class reference preps

---

## FILE ORGANIZATION

```
Lectures/Prep/
├── audio_preps/
│   ├── 2026-01-20_class01_audio_prep.md
│   ├── 2026-01-22_class02_audio_prep.md
│   └── ...
├── class_references/
│   ├── 2026-01-20_class01_class_reference.md
│   ├── 2026-01-22_class02_class_reference.md
│   └── ...
├── sources_mapped/
│   ├── class_001_mapping.txt
│   ├── class_002_mapping.txt
│   └── ...
├── AUDIO_PREP_STYLE_GUIDE.md
├── CLASS_REFERENCE_STYLE_GUIDE.md
└── MAPPING_SYSTEM_PLAN.md

Admin/Sources/Past_Outlines/
├── Crim_Spring 2025_Harcourt_Full.docx.md
│   ├── %% CLASS 1 START %%
│   ├── %% CLASS 1 END %%
│   ├── %% CLASS 2 START %%
│   ├── %% CLASS 2 END %%
│   └── ...
```

---

## SUMMARY

The mapping system is simple but powerful:
1. **Markers** in outline files show class boundaries
2. **Mapping files** document which outline sections map to which class
3. **Preps reference** the markers and mapping files
4. **No rewriting** of outline content—ever

This ensures accuracy, verifiability, and reversibility while giving us a clear path to create comprehensive preps aligned with proven outline content.
