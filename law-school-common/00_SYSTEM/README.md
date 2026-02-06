# 00_SYSTEM - Core System Documentation

**Purpose:** Contains foundational system documentation, rules, and specifications for the entire law school study system.

## Contents

### Core Specifications
- `FOLDER_STRUCTURE_SPEC.md` - Definitive specification for all course folder structures
- `COMMAND_INTERFACE.md` - Standard commands for AI interactions
- `AI_SYSTEM_RULES.md` - AI guardrails and system rules
- `SYSTEM_DIAGNOSIS_2026-01-19.md` - System analysis and recommendations

### Reference Materials (Archived)
- `_MASTER_STRUCTURE.md` - Previous structure specification (archived)
- `STRUCTURE_DESIGN_EXPLORATION.md` - Design exploration notes
- `ADMIN_CLEANUP_PLAN.md` - Cleanup planning documents

## Usage

1. **When setting up a new course:** Reference `FOLDER_STRUCTURE_SPEC.md`
2. **When giving AI commands:** Use `COMMAND_INTERFACE.md` for standard prompts
3. **When system behaves unexpectedly:** Check `AI_SYSTEM_RULES.md`
4. **When making system changes:** Review this folder first to understand existing patterns

## Principles

- All courses follow the same structure defined in `FOLDER_STRUCTURE_SPEC.md`
- Commands are course-agnostic and work across all 5 courses
- AI rules apply uniformly to prevent context drift and quality degradation
- This folder contains NO course-specific content (only universal rules)

## Maintenance

- Update `FOLDER_STRUCTURE_SPEC.md` when structure changes
- Update `COMMAND_INTERFACE.md` when adding new workflows
- Keep old specs in archive when replacing them (don't delete immediately)
