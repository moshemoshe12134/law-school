# Law School Monorepo

**Purpose:** Unified system for all law school courses, shared resources, and career materials  
**Structure:** Monorepo for maximum AI integration and cross-course learning  
**Started:** January 2026

---

## 📁 Repository Structure

```
law-school/
├── .git/                    ← Git repository root
├── .gitignore              ← Excludes PDFs, binaries, system files
│
├── law-school-common/      ← Shared templates, scripts, and guides
│   ├── .git/               ← Separate GitHub repo (git submodule candidate)
│   ├── TEMPLATES/          ← Reusable document templates
│   ├── scripts/            ← Automation scripts
│   ├── OPTIMIZATION_QUEUE.md
│   └── _MASTER_STRUCTURE.md
│
├── ACTIVE/                 ← Current semester courses (2026 Spring)
│   ├── CrimLaw/           ← Move here: law-school-CrimLaw/
│   ├── Property/          ← Move here: law-school-Property/
│   ├── Torts/             ← Move here: law-school-Torts/
│   ├── Deals/             ← Move here: law-school-Deals/
│   └── LPW-II/            ← Move here: law-school-LPW-II/
│
├── ARCHIVE/                ← Completed courses (still searchable!)
│   ├── 2025-fall/
│   │   ├── Contracts/
│   │   ├── CivPro/
│   │   └── ConLaw/
│   └── 2025-spring/
│       └── LPW-I/
│
├── SHARED/                 ← Cross-course resources
│   ├── LEGAL_RULES_LIBRARY/  ← Atomic legal doctrines
│   └── README.md
│
├── Career misc/            ← Career development
├── Private Sector Application/
└── School misc/
```

---

## 🎯 Why Monorepo?

### Advantages for Your Workflow:

1. **AI Full-Context Access**
   - AI can analyze your entire law school system at once
   - Cross-course search: `grep -r "personal jurisdiction" ACTIVE/`
   - System-wide refactoring in one pass

2. **Unified Version Control**
   - One commit tracks changes across all courses
   - See evolution of your entire system over time
   - Easy rollback if system changes break something

3. **Cross-Course Learning**
   - Compare professor emphasis across courses
   - Shared rules library (jurisdiction, standing, etc.)
   - Exam pattern analysis across all courses

4. **Simplified Workflow**
   - One `git status` to see all work
   - One sync operation (Google Drive + Git)
   - No submodule pain

5. **System Optimization**
   - Refactor folder structures across all courses at once
   - Test workflow improvements across multiple courses
   - Maintain consistency automatically

---

## 🔄 Migration Plan (Next Steps)

**Current state:**
- Courses at root level: `law-school-CrimLaw/`, `law-school-Property/`, etc.
- `law-school-common/` is a separate Git repo

**To complete migration:**

### Option 1: Keep Flat Structure (Simpler)
```bash
# Just initialize Git and start committing
# Keep courses at root level (no need to move)
git add .gitignore README.md law-school-common/
git commit -m "Initial commit: Law school monorepo setup"
```

### Option 2: Organize into ACTIVE/ (Cleaner)
```bash
# Move courses into ACTIVE/ folder
mv law-school-CrimLaw ACTIVE/CrimLaw
mv law-school-Property ACTIVE/Property
mv law-school-Torts ACTIVE/Torts
mv law-school-Deals ACTIVE/Deals
mv law-school-LPW-II ACTIVE/LPW-II

# Initial commit
git add .
git commit -m "Initial commit: Law school monorepo setup"
```

**Recommendation:** Option 2 (ACTIVE/ folder) for cleaner organization.

---

## 📊 What Gets Tracked

### ✅ DO COMMIT:
- Markdown files (`.md`) - notes, prep, reviews, outlines
- Text files (`.txt`) - transcripts, extracted text
- Python scripts (`.py`) - automation tools
- JSON/YAML configs - source trackers, course configs
- Small templates and guides

### ❌ DON'T COMMIT (in .gitignore):
- PDFs - too large, use Google Drive
- Audio/video files - too large
- PowerPoints - too large
- System files (`.DS_Store`, `.vscode/`)
- Generated files (OCR outputs - regenerate as needed)
- Private/sensitive notes (`*_PRIVATE.md`)

**Philosophy:** Git tracks your *structure and process*, Google Drive stores *large source materials*.

---

## 🔧 Common Git Operations

### Daily Workflow:
```bash
# Check what changed
git status

# Stage specific files
git add ACTIVE/Property/06_REVIEW/Lecture_05_review.md
git add law-school-common/OPTIMIZATION_QUEUE.md

# Or stage all changes
git add .

# Commit with descriptive message
git commit -m "Property: Complete Lecture 5 review + transcript extraction"

# Optional: Push to GitHub (if you set up remote)
git push origin main
```

### Track Progress:
```bash
# View commit history
git log --oneline --graph

# See what changed in last commit
git show

# See changes in working directory
git diff
```

### Archive a Course:
```bash
# End of semester
mkdir -p ARCHIVE/2026-spring
git mv ACTIVE/CrimLaw ARCHIVE/2026-spring/
git commit -m "Archive CrimLaw - course complete"
```

---

## 🚀 Optional: GitHub Remote

If you want cloud backup (beyond Google Drive):

```bash
# Create repo on GitHub: law-school
# Then:
git remote add origin https://github.com/YOUR_USERNAME/law-school.git
git branch -M main
git push -u origin main
```

**Note:** Make sure it's a **private repo** if you're pushing course notes.

---

## 🛡️ Handling law-school-common

Currently `law-school-common/` has its own `.git/` folder (separate repo). You have 3 options:

### Option A: Keep Separate (Git Submodule)
```bash
# Remove common's .git, make it a submodule
cd law-school-common
rm -rf .git
cd ..
git submodule add https://github.com/moshemoshe12134/law-school-common.git law-school-common
```

### Option B: Merge Into Monorepo
```bash
# Remove common's git history, treat as regular folder
cd law-school-common
rm -rf .git
cd ..
git add law-school-common/
git commit -m "Merge law-school-common into monorepo"
```

### Option C: Keep Separate, Just Reference
```bash
# Keep common as independent repo
# Add it to .gitignore in main repo
echo "law-school-common/" >> .gitignore
```

**Recommendation:** Option B (merge) for simplicity, unless you plan to use `common/` across multiple machines/projects.

---

## 📈 Workflow: From Now On

1. **Work on courses** (in ACTIVE/)
2. **`git add .` + `git commit -m "message"`** daily or weekly
3. **AI runs optimizations** (tracked in commits)
4. **End of semester:** `git mv ACTIVE/CrimLaw ARCHIVE/2026-spring/`
5. **Google Drive syncs** everything (PDFs, git repo, all files)

**Result:** Version-controlled system + cloud-backed source materials.

---

## 🎯 Next Steps

1. **Choose migration option:** Flat vs. ACTIVE/ structure
2. **Run initial commit:** `git add . && git commit -m "Initial commit"`
3. **Optional:** Set up GitHub remote for cloud backup
4. **Decide on law-school-common:** Submodule, merge, or separate
5. **Start committing regularly:** Track your system evolution

---

## 💡 Tips

- **Commit frequently:** Daily or after major work sessions
- **Descriptive messages:** "Property: Complete Lecture 5 review" not "update"
- **Use branches sparingly:** Main branch is fine for solo work
- **`.gitignore` is your friend:** Keeps repo small and fast
- **Google Drive + Git = Full backup:** Structure in Git, files in Drive

---

## 📚 Learn More

- Git basics: https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control
- Monorepo patterns: https://monorepo.tools/
- `.gitignore` patterns: https://git-scm.com/docs/gitignore
