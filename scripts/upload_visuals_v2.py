"""
ITP 326 Visual Library Uploader v2.0
Exercise A-F Structure with Smart Categorization

File naming convention:
  <stage>__<type>__<topic>__v<##>.png

Examples:
  C__template__needs-statement__v01.png
  D__example__concept-sketches__v01.png
  shared__diagram__design-thinking__v01.png

Usage:
1. Name your screenshots using the convention above
2. Put them in Desktop/326_screenshots/
3. Run: python upload_visuals_v2.py
"""

import shutil
from pathlib import Path
from git import Repo
import re

# ========== CONFIGURATION ==========

SOURCE_FOLDER = Path.home() / "Desktop" / "326_screenshots"
REPO_PATH = Path("/c/Users/Kendrick/Desktop/Repos/itp-326-agent")
GITHUB_USERNAME = "kdlin"
REPO_NAME = "itp-326-agent"
OUTPUT_MD = Path.home() / "Documents" / "L.2. Vault" / "visual_reference_library.md"

# ========== FOLDER STRUCTURE ==========

STAGE_FOLDERS = {
    "A": "A_user-identification",
    "B": "B_mission-statement",
    "C": "C_user-research-synthesis",
    "D": "D_ideation-concept-development",
    "E": "E_prototyping-testing",
    "F": "F_finalization-presentation",
    "shared": "shared"
}

TYPE_FOLDERS = ["templates", "examples", "diagrams", "checklists", "rubrics"]

STAGE_TITLES = {
    "A": "📋 EXERCISE A: User Identification",
    "B": "🎯 EXERCISE B: Mission Statement",
    "C": "🔍 EXERCISE C: User Research & Synthesis",
    "D": "💡 EXERCISE D: Ideation & Concept Development",
    "E": "🧪 EXERCISE E: Prototyping & Testing",
    "F": "🎨 EXERCISE F: Finalization & Presentation",
    "shared": "🔧 SHARED: Core Methods & Templates"
}

# ========== HELPER FUNCTIONS ==========

def parse_filename(filename):
    """
    Parse filename following convention: <stage>__<type>__<topic>__v<##>.png
    Returns: (stage, type, topic, version) or (None, None, None, None) if invalid
    """
    # Remove extension
    name = filename.replace(".png", "").replace(".jpg", "").replace(".jpeg", "")

    # Split by double underscore
    parts = name.split("__")

    if len(parts) >= 3:
        stage = parts[0].upper()
        type_ = parts[1].lower()
        topic = parts[2] if len(parts) >= 3 else "unnamed"
        version = parts[3] if len(parts) >= 4 else "v01"

        # Validate stage
        if stage not in STAGE_FOLDERS and stage != "SHARED":
            return None, None, None, None

        # Validate type
        if type_ not in TYPE_FOLDERS:
            # Try to guess type from common keywords
            if "template" in filename.lower():
                type_ = "templates"
            elif "example" in filename.lower():
                type_ = "examples"
            elif "diagram" in filename.lower():
                type_ = "diagrams"
            else:
                type_ = "examples"  # default

        return stage, type_, topic, version

    return None, None, None, None

def get_destination_path(filename):
    """Get the destination path in repo based on filename convention"""
    stage, type_, topic, version = parse_filename(filename)

    if stage is None:
        # Fallback for badly named files
        return REPO_PATH / "images" / "uncategorized" / filename

    stage_folder = STAGE_FOLDERS.get(stage, STAGE_FOLDERS.get(stage.lower(), "shared"))
    return REPO_PATH / "images" / stage_folder / type_ / filename

def get_github_url(filename):
    """Generate GitHub raw URL based on file's destination path"""
    stage, type_, topic, version = parse_filename(filename)

    if stage is None:
        return f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/main/images/uncategorized/{filename}"

    stage_folder = STAGE_FOLDERS.get(stage, STAGE_FOLDERS.get(stage.lower(), "shared"))
    return f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/main/images/{stage_folder}/{type_}/{filename}"

def sanitize_name(topic):
    """Convert topic to readable title"""
    return topic.replace("-", " ").replace("_", " ").title()

def create_folder_structure():
    """Create the Exercise A-F folder structure in the repo"""
    images_root = REPO_PATH / "images"

    for stage_key, stage_folder in STAGE_FOLDERS.items():
        for type_folder in TYPE_FOLDERS:
            folder_path = images_root / stage_folder / type_folder
            folder_path.mkdir(parents=True, exist_ok=True)

    # Also create uncategorized folder for fallback
    (images_root / "uncategorized").mkdir(parents=True, exist_ok=True)

# ========== MAIN SCRIPT ==========

def main():
    # Fix Windows console encoding
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("=" * 60)
    print("ITP 326 VISUAL LIBRARY UPLOADER v2.0")
    print("Exercise A-F Structure")
    print("=" * 60)

    # Check source folder
    if not SOURCE_FOLDER.exists():
        print(f"\n❌ Source folder not found: {SOURCE_FOLDER}")
        print("Creating folder...")
        SOURCE_FOLDER.mkdir(parents=True)
        print(f"✓ Created! Put screenshots there using naming convention:")
        print(f"   Example: C__template__needs-statement__v01.png")
        return

    # Find images
    image_files = list(SOURCE_FOLDER.glob("*.png")) + \
                  list(SOURCE_FOLDER.glob("*.jpg")) + \
                  list(SOURCE_FOLDER.glob("*.jpeg"))

    if not image_files:
        print(f"\n❌ No images found in {SOURCE_FOLDER}")
        return

    print(f"\n📸 Found {len(image_files)} images")

    # Check which are already in markdown
    existing_images = set()
    if OUTPUT_MD.exists():
        with open(OUTPUT_MD, "r", encoding="utf-8") as f:
            content = f.read()
            existing_images = set(re.findall(r'images/[^)]+/([^)]+\.(?:png|jpg|jpeg))', content))

    new_images = [img for img in image_files if img.name not in existing_images]

    if not new_images:
        print(f"\n✓ All {len(image_files)} images already in markdown. Nothing to do!")
        return

    print(f"📦 {len(new_images)} new images to process")

    # Create folder structure
    print(f"\n📂 Setting up folder structure...")
    create_folder_structure()

    # Copy images to proper locations
    print(f"\n📂 Copying images to categorized folders...")
    badly_named = []

    for i, img in enumerate(new_images, 1):
        dest = get_destination_path(img.name)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(img, dest)

        stage, type_, topic, version = parse_filename(img.name)
        if stage is None:
            badly_named.append(img.name)
            print(f"  [{i}/{len(new_images)}] ⚠️  {img.name} (badly named → uncategorized)")
        else:
            print(f"  [{i}/{len(new_images)}] ✓ {img.name} → {STAGE_FOLDERS[stage]}/{type_}")

    if badly_named:
        print(f"\n⚠️  {len(badly_named)} files don't follow naming convention:")
        for name in badly_named:
            print(f"    - {name}")
        print(f"\n   Rename using: <stage>__<type>__<topic>__v01.png")
        print(f"   Example: C__template__needs-statement__v01.png")

    # Git operations
    print(f"\n🔄 Committing to Git...")
    try:
        repo = Repo(REPO_PATH)
        repo.index.add(["images/*"])
        repo.index.commit(f"Add {len(new_images)} visual references")
        origin = repo.remote(name='origin')
        origin.push()
        print(f"  ✓ Pushed to GitHub!")
    except Exception as e:
        print(f"  ❌ Git error: {e}")
        return

    # Generate/update markdown
    print(f"\n📝 Updating markdown file...")

    # Organize by stage
    by_stage = {}
    for img in new_images:
        stage, type_, topic, version = parse_filename(img.name)
        stage_key = stage if stage else "uncategorized"

        if stage_key not in by_stage:
            by_stage[stage_key] = []
        by_stage[stage_key].append(img)

    # Append to file
    mode = "a" if OUTPUT_MD.exists() else "w"
    with open(OUTPUT_MD, mode, encoding="utf-8") as f:
        if mode == "w":
            f.write("# ITP 326 Visual Reference Library\n\n")
            f.write("*Organized by Exercise Stage (A-F)*\n\n")
            f.write("---\n\n")

        for stage_key in sorted(by_stage.keys()):
            if stage_key == "uncategorized":
                f.write(f"\n## ⚠️  UNCATEGORIZED\n\n")
            else:
                f.write(f"\n## {STAGE_TITLES.get(stage_key, stage_key)}\n\n")

            for img in by_stage[stage_key]:
                stage, type_, topic, version = parse_filename(img.name)
                name = sanitize_name(topic) if topic else img.stem
                url = get_github_url(img.name)

                f.write(f"### {name}\n")
                f.write(f"**Type:** {type_ or 'Unknown'}\n")
                f.write(f"**Triggers:** \"{name.lower()}\", \"{type_}\", \"example\"\n")
                f.write(f"**Description:** [ADD DESCRIPTION]\n")
                f.write(f"**Image:** ![{name}]({url})\n\n")

            f.write("---\n\n")

    print(f"✓ Updated: {OUTPUT_MD}")

    # Summary
    print(f"\n" + "=" * 60)
    print(f"🎉 SUCCESS! Added {len(new_images)} images")
    print(f"=" * 60)
    print(f"\n📋 Next steps:")
    print(f"1. Open: {OUTPUT_MD}")
    print(f"2. Add descriptions for new images")
    print(f"3. Re-upload to Custom GPT knowledge base")

    if badly_named:
        print(f"\n⚠️  Fix {len(badly_named)} badly named files and re-run")

if __name__ == "__main__":
    main()
