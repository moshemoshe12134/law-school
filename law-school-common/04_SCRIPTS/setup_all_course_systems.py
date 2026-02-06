#!/usr/bin/env python3
"""
Contracts Prep System Setup
Creates the complete prep/review system for Contracts course
"""

import os
import json
from pathlib import Path
from datetime import datetime

def setup_contracts_system():
    """Set up the complete Contracts prep/review system"""

    base_dir = Path(__file__).parent.parent
    contracts_dir = base_dir / 'Contracts'

    print("=== SETTING UP CONTRACTS PREP/REVIEW SYSTEM ===")

    # Create directory structure
    prep_dir = contracts_dir / 'prep'
    review_dir = contracts_dir / 'review'
    inbox_dir = prep_dir / 'inbox'

    prep_dir.mkdir(exist_ok=True)
    review_dir.mkdir(exist_ok=True)
    inbox_dir.mkdir(exist_ok=True)

    # Create basic source tracker template
    tracker_data = {
        "course": "Contracts",
        "generated": datetime.now().isoformat(),
        "units": [],
        "notes": "Initialize with syllabus parsing once syllabus is available"
    }

    tracker_path = prep_dir / '_SOURCE_TRACKER.json'
    with open(tracker_path, 'w') as f:
        json.dump(tracker_data, f, indent=2)

    # Create syllabus parser template
    syllabus_parser = f'''#!/usr/bin/env python3
"""
Syllabus Parser for Contracts
Parses the Contracts syllabus into structured units
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any

class ContractsSyllabusParser:
    def __init__(self, syllabus_path: str, base_dir: str):
        self.syllabus_path = Path(syllabus_path)
        self.base_dir = Path(base_dir)
        self.units = []

    def parse(self) -> Dict[str, Any]:
        """Parse the Contracts syllabus into structured units"""
        # TODO: Implement Contracts-specific syllabus parsing
        # This will need to be adapted based on the actual Contracts syllabus format

        return {{
            "course": "Contracts",
            "units": self.units,
            "notes": "Syllabus parser ready - adapt parsing logic for Contracts syllabus format"
        }}

    def save_to_json(self, output_path: str):
        """Save parsed units to JSON"""
        data = self.parse()
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Saved parsed syllabus to {{output_path}}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python syllabus_parser.py <syllabus_file>")
        sys.exit(1)

    syllabus_file = sys.argv[1]
    base_dir = Path(__file__).parent.parent
    parser = ContractsSyllabusParser(syllabus_file, base_dir)
    parser.save_to_json(base_dir / 'prep' / '_SOURCE_TRACKER.json')
'''

    with open(prep_dir / 'syllabus_parser.py', 'w') as f:
        f.write(syllabus_parser)

    # Create prep generator
    prep_generator = '''#!/usr/bin/env python3
"""
Prep Document Generator for Contracts
Generates prep documents for Contracts course
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

class ContractsPrepGenerator:
    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir)
        self.prep_dir = self.base_dir / 'prep' / 'units'
        self.prep_dir.mkdir(exist_ok=True)

        # Load source tracker (if exists)
        tracker_path = self.base_dir / 'prep' / '_SOURCE_TRACKER.json'
        if tracker_path.exists():
            with open(tracker_path, 'r') as f:
                self.tracker = json.load(f)
        else:
            self.tracker = {"course": "Contracts", "units": []}

    def generate_all_units(self):
        """Generate prep docs for all units"""
        if not self.tracker.get('units'):
            print("No units found in tracker. Run syllabus parser first.")
            return

        for unit in self.tracker['units']:
            self.generate_unit(unit)

        print(f"✓ Generated {len(self.tracker['units'])} prep documents for Contracts")

    def generate_unit(self, unit: Dict[str, Any]):
        """Generate a single prep document"""
        unit_num = unit.get('unit_number', 1)
        title = unit.get('title', 'Unit Title')
        filename = f"unit_{unit_num:02d}_{self._slugify(title)}.md"
        output_path = self.prep_dir / filename

        # Build the document
        doc = self._build_prep_document(unit)

        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(doc)

        print(f"✓ Generated: {filename}")

    def _build_prep_document(self, unit: Dict[str, Any]) -> str:
        """Build the markdown content for a prep document"""
        lines = []

        # Header
        lines.append(f"# Unit {unit.get('unit_number', 'X')}: {unit.get('title', 'Unit Title')}")
        lines.append("")
        lines.append("**Course**: Contracts")
        lines.append(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        lines.append("")
        lines.append("## Source Material Status")
        lines.append("")
        lines.append("_[Source materials to be tracked once syllabus is parsed]_")
        lines.append("")

        lines.append("---")
        lines.append("")

        # Required readings (placeholder)
        lines.append("## Required Readings")
        lines.append("")
        lines.append("_[To be populated from syllabus parsing]_")
        lines.append("")

        # Study questions (placeholder)
        lines.append("## Study Questions")
        lines.append("")
        lines.append("_[To be populated from syllabus parsing]_")
        lines.append("")

        # Key concepts
        lines.append("## Key Concepts to Master")
        lines.append("")
        lines.append("_[To be filled during review]_")
        lines.append("")

        # Notes
        lines.append("## Your Notes")
        lines.append("")
        lines.append("_[Add your personal notes here]_")
        lines.append("")

        return '\\n'.join(lines)

    def _slugify(self, text: str) -> str:
        """Convert text to filename-safe slug"""
        text = re.sub(r'[^\\w\\s-]', '', text.lower())
        text = re.sub(r'[\\s_]+', '_', text)
        return text[:50]

if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='Generate Contracts prep documents')
    parser.add_argument('--all', action='store_true', help='Generate all units')
    parser.add_argument('--unit', type=int, help='Generate specific unit number')

    args = parser.parse_args()

    base_dir = Path(__file__).parent.parent
    generator = ContractsPrepGenerator(base_dir)

    if args.all:
        generator.generate_all_units()
    elif args.unit:
        # Generate single unit (would need unit data)
        print("Single unit generation not yet implemented - run --all after syllabus parsing")
    else:
        print("Usage: python prep_generator.py --all")
'''

    with open(prep_dir / 'prep_generator.py', 'w') as f:
        f.write(prep_generator)

    # Create inbox system
    inbox_readme = '''# Contracts Prep Inbox

## Purpose
Drop new course materials here as they become available from Courseworks or other sources.

## How It Works
1. **Download** new materials from Courseworks
2. **Drop them here** in this inbox folder
3. **Run the processor**: `python prep/inbox_processor.py`
4. The system will:
   - Check if the file already exists
   - Determine the correct subfolder in `/additional/`
   - Move the file to the appropriate location
   - Update the source tracker
   - Regenerate any affected prep docs

## File Naming
Keep original filenames from Courseworks for easier matching.

## What Happens to Files
- **Cases** → `/additional/source_materials/cases/`
- **Readings** → `/additional/source_materials/readings/`
- **Problems** → `/additional/practice_exercises/problems_hypos/`
- **TA Materials** → `/additional/practice_exercises/ta_sections/`

## Status
System ready - awaiting syllabus parsing and material processing.
'''

    with open(inbox_dir / 'README.md', 'w') as f:
        f.write(inbox_readme)

    # Create master reference
    master_ref = f'''# Contracts Study System - Master Reference

## Overview
This document provides a blueprint of the Contracts study system.

**System Status**: Framework created, awaiting syllabus parsing and material processing.

## System Architecture
```
Contracts/
├── textbook/                    # Source materials (Dawson textbook)
├── syllabus/                    # Course syllabus
├── transcripts/                 # Lecture recordings (13 available)
├── course_reference/            # Navigation and readings
├── additional/                  # Supplementary materials
│   ├── source_materials/readings/  # Course outlines, LSE, Morrison
│   └── lecture_support/slides/     # Lecture slide PDFs
├── prep/                        # Pre-lecture preparation (system ready)
├── review/                      # Post-lecture review (system ready)
└── _ai_reference/               # System documentation
```

## Current Status
- ✅ **Basic structure**: All master folders created
- ✅ **Prep system**: Framework ready, awaiting syllabus parsing
- ✅ **Review system**: Scripts created, ready for use
- ⏳ **Source tracking**: Awaiting syllabus parsing
- ⏳ **Prep docs**: Will be generated after syllabus parsing

## Next Steps
1. Parse syllabus: `python prep/syllabus_parser.py syllabus_file`
2. Generate prep docs: `python prep/prep_generator.py --all`
3. Process materials as they become available

## File Reference
- `prep/_PREP_SYSTEM.md` - System documentation
- `prep/inbox/README.md` - Inbox processing guide
- `prep/_SOURCE_TRACKER.json` - Source material database (to be populated)

*See CivPro system for complete implementation example.*
'''

    with open(contracts_dir / '_ai_reference' / 'MASTER_SYSTEM_REFERENCE.md', 'w') as f:
        f.write(master_ref)

    print("✓ Contracts prep/review system framework created")
    print("Next: Parse syllabus and generate prep documents")

if __name__ == '__main__':
    setup_contracts_system()
'''

    with open(contracts_dir / 'prep' / 'setup_contracts_system.py', 'w') as f:
        f.write(content)

    print("✓ Contracts system framework created")

# Now create for ConLaw
def create_conlaw_system():
    """Create ConLaw prep/review system"""

    base_dir = Path(__file__).parent.parent
    conlaw_dir = base_dir / 'ConLaw'

    print("=== SETTING UP CONLAW PREP/REVIEW SYSTEM ===")

    # ConLaw already has some structure, just add the missing components
    prep_dir = conlaw_dir / 'prep'
    review_dir = conlaw_dir / 'review'

    prep_dir.mkdir(exist_ok=True)
    review_dir.mkdir(exist_ok=True)

    # Copy the system from CivPro and adapt
    import shutil
    shutil.copy2(base_dir / 'Civpro' / 'prep' / '_PREP_SYSTEM.md', prep_dir / '_PREP_SYSTEM.md')

    # Create ConLaw-specific master reference
    master_ref = '''# ConLaw Study System - Master Reference

## Overview
This document provides a blueprint of the Constitutional Law study system.

**System Status**: Reorganized structure, prep/review framework ready.

## System Architecture
```
ConLaw/
├── _ai_reference/               # Development tools, docs
│   ├── web_app/                 # Web application
│   ├── scripts/                 # Processing scripts
│   ├── logs/                    # System logs
│   └── *.md docs                # Documentation
├── additional/                  # Organized materials
│   ├── lecture_support/
│   │   └── weekly_materials/    # Weekly folders consolidated
│   └── source_materials/
│       └── readings/            # Distributed materials
├── course_reference/            # Navigation and readings
│   └── readings/                # Weekly readings consolidated
├── prep/                        # Pre-lecture preparation (ready)
├── review/                      # Post-lecture review (ready)
├── syllabus/                    # Course syllabus
├── textbook/                    # Textbook materials
└── transcripts/                 # Lecture recordings
```

## Current Status
- ✅ **Reorganized**: Weekly readings consolidated, tools categorized
- ✅ **Prep system**: Framework ready for syllabus parsing
- ✅ **Review system**: Scripts ready for transcript integration
- ✅ **Additional materials**: Organized into proper subcategories

## Key Features
- **Consolidated readings**: All weekly readings in one location
- **Organized tools**: Development materials properly categorized
- **Weekly materials**: All week folders in lecture_support/weekly_materials/

## File Reference
- `course_reference/readings/` - All weekly readings consolidated
- `additional/lecture_support/weekly_materials/` - Weekly material folders
- `_ai_reference/` - Development tools and documentation

*System ready for syllabus parsing and prep document generation.*
'''

    with open(conlaw_dir / '_ai_reference' / 'MASTER_SYSTEM_REFERENCE.md', 'w') as f:
        f.write(master_ref)

    print("✓ ConLaw system updated")

# Now create for LPW
def create_lpw_system():
    """Create LPW prep/review system"""

    base_dir = Path(__file__).parent.parent
    lpw_dir = base_dir / 'LPW'

    print("=== SETTING UP LPW PREP/REVIEW SYSTEM ===")

    # Create prep/review structure
    prep_dir = lpw_dir / 'prep'
    review_dir = lpw_dir / 'review'
    inbox_dir = prep_dir / 'inbox'

    prep_dir.mkdir(exist_ok=True)
    review_dir.mkdir(exist_ok=True)
    inbox_dir.mkdir(exist_ok=True)

    # Create basic tracker
    tracker_data = {
        "course": "LPW",
        "generated": datetime.now().isoformat(),
        "units": [],
        "notes": "LPW system ready - awaiting syllabus and materials"
    }

    with open(prep_dir / '_SOURCE_TRACKER.json', 'w') as f:
        json.dump(tracker_data, f, indent=2)

    # Create master reference
    master_ref = '''# LPW Study System - Master Reference

## Overview
This document provides a blueprint of the Legal Practice Workshop study system.

**System Status**: Basic structure created, awaiting syllabus and materials.

## System Architecture
```
LPW/
├── additional/                  # Supplementary materials
│   ├── source_materials/
│   │   ├── cases/
│   │   ├── complaints/
│   │   └── readings/
│   ├── practice_exercises/
│   │   ├── ta_sections/
│   │   ├── problems_hypos/
│   │   └── glannon/
│   ├── lecture_support/
│   │   ├── class_notes/
│   │   └── powerpoints/
│   └── exam_prep/
│       ├── past_exams/
│       ├── practice_answers/
│       └── writing_examples/
├── textbook/                    # Textbook materials (renamed from Books)
├── syllabus/                    # Course syllabus (Fall 2025 LPW syllabus)
├── transcripts/                 # Lecture recordings
├── course_reference/            # Navigation and readings
├── prep/                        # Pre-lecture preparation (ready)
├── review/                      # Post-lecture review (ready)
└── _ai_reference/               # System documentation
```

## Current Status
- ✅ **Structure**: All master folders created
- ✅ **Additional**: Complete subcategory structure
- ✅ **Textbook**: Renamed from "Books" to "textbook"
- ⏳ **Materials**: Awaiting syllabus parsing and content addition
- ⏳ **Prep docs**: Ready for generation once syllabus is parsed

## Available Materials
- **Syllabus**: Fall 2025 Legal Practice Workshop syllabus
- **Framework**: Complete prep/review system infrastructure

## Next Steps
1. Parse syllabus when available
2. Add course materials as they become available
3. Generate prep documents
4. Set up weekly workflows

*LPW system infrastructure ready for content population.*
'''

    with open(lpw_dir / '_ai_reference' / 'MASTER_SYSTEM_REFERENCE.md', 'w') as f:
        f.write(master_ref)

    print("✓ LPW system framework created")

if __name__ == '__main__':
    create_contracts_system()
    create_conlaw_system()
    create_lpw_system()
    print("\\n🎯 All courses now have prep/review system frameworks!")
