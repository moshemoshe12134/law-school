# Law School - Common Resources

Shared templates, workflows, and AI agent instructions for all law school courses.

---

## 🤖 AI Agent Setup (GitHub Copilot, Claude Code, Kilo Code)

**The workspace is configured for automatic context loading.** When you open this workspace and start a new conversation with any AI agent, it will automatically read the instructions file.

| Agent | Instructions File | Auto-loaded? |
|-------|-------------------|--------------|
| GitHub Copilot | `.github/copilot-instructions.md` | ✅ Yes |
| Claude Code | `CLAUDE.md` | ✅ Yes |
| Kilo Code | `.kilocode/rules/law-school-agent-rules.md` | ✅ Yes |
| Generic / Other | `AGENTS.md` | ✅ Yes (if supported) |

**How it works:** Each agent looks for its specific file and injects the contents as context at the start of every conversation. This means you can simply say:

> "Create a prep doc for CrimLaw class 3"

And the agent will know exactly:
- Where to find the MASTER_LOG
- What template to use
- Where to save the output
- How to name the file

---

## 📁 Folder Structure

```
law-school-common/
├── 00_SYSTEM/               # Core AI instructions
│   ├── COMMAND_INTERFACE.md # All commands + procedures
│   ├── AI_SYSTEM_RULES.md   # Agent behavior rules
│   └── FOLDER_STRUCTURE_SPEC.md # Definitive folder spec
│
├── 01_WORKFLOWS/            # Step-by-step workflows
│   ├── PRE_CLASS_WORKFLOW.md
│   ├── POST_CLASS_WORKFLOW.md
│   ├── QC_WORKFLOW.md
│   └── EXAM_PREP_WORKFLOW.md
│
├── 02_STYLE_GUIDES/         # Writing standards
│
├── 03_TEMPLATES/            # All templates
│   ├── text_prep_template.md
│   ├── audio_prep_template.md
│   ├── review_template.md
│   ├── prewrite_doctrinal_template.md
│   └── prewrite_policy_template.md
│
├── 04_SCRIPTS/              # Utility scripts
├── 05_ARCHIVE/              # Old/deprecated files
└── 06_LOGS/                 # Processing logs
```

---

## 🔑 Key Documents

| Document | Purpose | When to Read |
|----------|---------|--------------|
| `COMMAND_INTERFACE.md` | All AI commands + exact procedures | Before any task |
| `PRE_CLASS_WORKFLOW.md` | How to create prep docs | Creating preps |
| `POST_CLASS_WORKFLOW.md` | How to create review docs | After class |
| `text_prep_template.md` | Text prep structure | Creating text preps |
| `audio_prep_template.md` | Audio prep structure | Creating audio preps |

---

## 🚀 Quick Start for AI Agents

If you're an AI agent reading this, here's what you need to know:

1. **Command Interface**: Read `00_SYSTEM/COMMAND_INTERFACE.md` for all supported commands
2. **Course Data**: Each course has a MASTER_LOG at `ACTIVE/{Course}/00_ADMIN/MASTER_LOG.md`
3. **Templates**: All templates are in `03_TEMPLATES/`
4. **Naming Convention**: `YYYY-MM-DD_classNN_type.md` (e.g., `2026-01-22_class02_text.md`)

---

## Maintenance

Keep this repo minimal and well-documented. Each file should have a clear purpose that benefits multiple courses.
