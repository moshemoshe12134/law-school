import re

filepath = "ACTIVE/LPW-II/99_Assignments/Draft #1/EMERGENCY_DRAFT_1_UNVERIFIED.md"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Fix "See" signal word - should be italicized per Bluebook Rule 2.1(a)
# Match "See " at start of a sentence or after ". " that is NOT already italicized
# We want to replace "See *" with "*See* *" (where See starts a citation signal)
# but NOT inside quotes or within case names

# Specifically fix the three known patterns:
# 1. "See *Campbell*" -> "*See* *Campbell*"
# 2. "See *TCA Television" -> "*See* *TCA Television"
# 3. "See *Authors Guild" -> "*See* *Authors Guild"

# General pattern: "See *" at start of citation -> "*See* *"
# But only when "See" is not already italicized
content = re.sub(r'(?<!\*)See \*', '*See* *', content)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed 'See' signal italicization.")
# Verify
count = content.count('*See*')
print(f"Found {count} italicized 'See' signals.")
