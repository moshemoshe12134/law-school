# Shared Legal Resources

This folder contains resources used across multiple law school courses.

---

## 📁 Folders

### LEGAL_RULES_LIBRARY/
Cross-cutting legal doctrines that appear in multiple courses.

**Purpose:** DRY (Don't Repeat Yourself) for legal concepts

**Examples:**
- Personal jurisdiction (CivPro, Conflicts)
- Standing (ConLaw, CivPro)
- Burden of proof (CrimLaw, CivPro, Torts)
- Statutory interpretation (all courses)
- Policy analysis frameworks (all courses)

**Format:** One file per concept
- `personal_jurisdiction.md`
- `standing.md`
- `burden_of_proof.md`

Each file includes:
- Black letter rule
- Key cases
- Course-specific applications
- Cross-references

---

## 🎯 When to Add Here

Add a concept to `LEGAL_RULES_LIBRARY/` when:
- ✅ It appears in 2+ courses
- ✅ It's a foundational legal concept
- ✅ It has cross-course variations worth tracking

Don't add:
- ❌ Course-specific doctrines (keep in course outline)
- ❌ Case-specific rules (keep in course notes)
- ❌ One-off concepts

---

## 🔄 Workflow

1. **Recognize cross-cutting concept** in class or prep
2. **Create atomic file** in `LEGAL_RULES_LIBRARY/`
3. **Link from course outlines** using relative paths
4. **Update shared file** when new course adds nuance

**Example:**
```markdown
<!-- In Property/07_OUTLINE/outline.md -->
See [shared resource on standing](../../SHARED/LEGAL_RULES_LIBRARY/standing.md) 
for the general framework. Property-specific application: ...
```

---

## 📚 Future Folders (Add as needed)

- `EXAM_STRATEGIES/` - General exam-taking techniques
- `WRITING_SAMPLES/` - Model legal writing across courses
- `PROFESSOR_PATTERNS/` - Meta-patterns across all professors
- `STUDY_TECHNIQUES/` - What works for you

---

## 💡 Philosophy

**Goal:** Build a personal "legal knowledge base" that compounds over 3 years.

Instead of repeating the same jurisdiction analysis in 3 different outlines, write it once here and link to it. Update it as your understanding deepens.
