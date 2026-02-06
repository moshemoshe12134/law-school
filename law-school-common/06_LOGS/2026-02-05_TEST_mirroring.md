# Mirroring Test - New Skill Creation

**Purpose**: Test that agents understand mirroring requirements
**Date**: 2026-02-05
**Status**: Test case created

---

## Test Scenario

If an agent is asked to create a new skill (e.g., "create a skill for case briefing"), it should:

1. **Create the skill** in both systems:
   - `.claude/prompts/skills/case-briefing.md`
   - `.github/copilot-instructions.md` with equivalent skill section

2. **Maintain identical structure** across both systems

3. **Update both instruction sets** consistently

## Expected Behavior

When asked: "Create a case briefing skill"

**Claude Code Agent**:
- Should create skill in `.claude/prompts/skills/case-briefing.md`
- Should also create/update equivalent content in `.github/copilot-instructions.md`
- Should mention both locations in response

**GitHub Copilot Agent**:
- Should create skill in `.github/copilot-instructions.md`
- Should also create/update equivalent content in `.claude/prompts/skills/case-briefing.md`
- Should mention both locations in response

## Success Criteria

✅ Both agents understand they must mirror content
✅ Skills are created in both systems
✅ Content remains identical across systems
✅ Agent acknowledges mirroring in response