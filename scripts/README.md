# ITP 326 Visual Library Scripts

Automation scripts for managing the visual reference library.

## `upload_visuals_v2.py`

Automates uploading screenshots to GitHub and generating the markdown reference library.

### File Naming Convention

All screenshots must follow this format:

```
<stage>__<type>__<topic>__v<##>.<ext>
```

**Examples:**
- `C__template__needs-statement__v01.png`
- `D__example__concept-sketches__v01.png`
- `shared__diagram__design-thinking__v01.png`

**Stages:**
- `A` = User Identification
- `B` = Mission Statement
- `C` = User Research & Synthesis
- `D` = Ideation & Concept Development
- `E` = Prototyping & Testing
- `F` = Finalization & Presentation
- `shared` = Core Methods & Templates

**Types:**
- `template` → Blank forms/structures
- `example` → Filled-in samples
- `diagram` → Process flows, concepts
- `checklist` → Step-by-step guides
- `rubric` → Grading criteria

### Usage

1. **Name your screenshots** using the convention above
2. **Put them in:** `~/Desktop/326_screenshots/`
3. **Run the script:**
   ```bash
   python scripts/upload_visuals_v2.py
   ```

### What It Does

1. ✓ Validates filenames
2. ✓ Creates Exercise A-F folder structure
3. ✓ Copies images to categorized folders
4. ✓ Commits and pushes to GitHub
5. ✓ Generates/updates `visual_reference_library.md`
6. ✓ Only adds NEW images (preserves existing descriptions)

### Output

- **Images:** Organized in `/images/<stage>/<type>/`
- **Markdown:** Generated in Obsidian vault
- **URLs:** Permanent GitHub raw links

### Setup

**Install dependencies:**
```bash
pip install gitpython
```

**Configure paths in script:**
- `SOURCE_FOLDER` = Where you save screenshots
- `REPO_PATH` = Path to this repo
- `OUTPUT_MD` = Where markdown file goes

## Folder Structure

```
images/
├── A_user-identification/
│   ├── templates/
│   ├── examples/
│   └── diagrams/
├── B_mission-statement/
│   ├── templates/
│   └── examples/
├── C_user-research-synthesis/
│   ├── templates/
│   ├── examples/
│   └── diagrams/
├── D_ideation-concept-development/
│   ├── templates/
│   ├── examples/
│   └── diagrams/
├── E_prototyping-testing/
│   ├── templates/
│   ├── examples/
│   └── diagrams/
├── F_finalization-presentation/
│   ├── templates/
│   └── examples/
└── shared/
    ├── templates/
    ├── examples/
    └── diagrams/
```

## Maintenance

**Adding more images:**
1. Put new screenshots in source folder
2. Run script again
3. Script adds only new images
4. Re-upload markdown to ChatGPT

**Renaming badly named files:**
- Script will warn you
- Rename following convention
- Re-run script

## For Other Tutors

1. Clone this repo
2. Install dependencies
3. Update paths in script for your system
4. Run script to generate your own markdown
