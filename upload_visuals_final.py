"""
ITP 326 Visual Library Uploader - FINAL VERSION
Simple 4-folder structure organized by type

Folder structure:
  images/
    templates/    - Blank forms, structures
    examples/     - Filled-in samples, real work
    diagrams/     - Process flows, concepts
    reference/    - Rubrics, guides, syllabi

Usage:
1. Name files descriptively (include type keyword if possible)
   - needs-statement-template.png
   - persona-drew-example.png
   - design-thinking-diagram.png
2. Put in Desktop/326_screenshots/
3. Run: python upload_visuals_final.py
"""

import shutil
from pathlib import Path
from git import Repo
import re
import yaml

# ========== CONFIGURATION ==========

SOURCE_FOLDER = Path.home() / "Desktop" / "326_screenshots"
REPO_PATH = Path("C:/Users/Kendrick/Desktop/Repos/itp-326-agent")
GITHUB_USERNAME = "kdlin"
REPO_NAME = "itp-326-agent"
OUTPUT_MD = Path.home() / "Documents" / "L.2. Vault" / "visual_reference_library.md"
DESCRIPTIONS_FILE = SOURCE_FOLDER / "descriptions.yaml"

# 2 simple folders
FOLDERS = {
    "examples": "examples",
    "reference": "reference"
}

# ========== HELPER FUNCTIONS ==========

def detect_folder(filename):
    """Auto-detect which folder based on filename keywords"""
    lower = filename.lower()

    # Check prefix first (reference_ or example_)
    if lower.startswith("reference_") or lower.startswith("reference__"):
        return "reference"
    elif lower.startswith("example_") or lower.startswith("examples_") or lower.startswith("example__") or lower.startswith("examples__"):
        return "examples"

    # Then check keywords in filename
    # Reference - guides, rules, diagrams, frameworks, processes
    if any(word in lower for word in ["diagram", "rule", "guide", "framework", "process", "rubric", "checklist", "criteria", "instruction"]):
        return "reference"

    # Examples - templates, personas, filled work (default)
    else:
        return "examples"

def get_github_url(filename, folder):
    """Generate GitHub raw URL"""
    return f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/main/images/{folder}/{filename}"

def sanitize_name(filename):
    """Convert filename to readable title"""
    name = filename.replace(".png", "").replace(".jpg", "").replace(".jpeg", "")
    name = name.replace("-", " ").replace("_", " ")
    # Remove type keywords from title
    for keyword in ["template", "example", "diagram", "reference"]:
        name = name.replace(keyword, "")
    return name.strip().title()

def get_category_title(folder):
    """Get markdown section title from folder name"""
    titles = {
        "examples": "✨ Examples",
        "reference": "📚 Reference"
    }
    return titles.get(folder, folder.capitalize())

# ========== MAIN SCRIPT ==========

def main():
    # Fix Windows encoding
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("=" * 60)
    print("ITP 326 VISUAL LIBRARY UPLOADER")
    print("4-Folder Structure (templates/examples/diagrams/reference)")
    print("=" * 60)

    # Check source folder
    if not SOURCE_FOLDER.exists():
        print(f"\n❌ Folder not found: {SOURCE_FOLDER}")
        SOURCE_FOLDER.mkdir(parents=True)
        print(f"✓ Created! Add screenshots there.")
        return

    # Find images
    image_files = list(SOURCE_FOLDER.glob("*.png")) + \
                  list(SOURCE_FOLDER.glob("*.jpg")) + \
                  list(SOURCE_FOLDER.glob("*.jpeg"))

    if not image_files:
        print(f"\n❌ No images in {SOURCE_FOLDER}")
        return

    print(f"\n📸 Found {len(image_files)} images")

    # Check which are new
    existing_images = set()
    if OUTPUT_MD.exists():
        with open(OUTPUT_MD, "r", encoding="utf-8") as f:
            content = f.read()
            # Match images in any subfolder
            existing_images = set(re.findall(r'images/[^/]+/([^)]+\.(?:png|jpg|jpeg))', content))

    new_images = [img for img in image_files if img.name not in existing_images]

    if not new_images:
        print(f"\n✓ All {len(image_files)} images already uploaded!")
        return

    print(f"📦 {len(new_images)} new images to upload")

    # Create folder structure
    images_root = REPO_PATH / "images"
    for folder in FOLDERS.values():
        (images_root / folder).mkdir(parents=True, exist_ok=True)

    # Copy to appropriate folders
    print(f"\n📂 Organizing by type...")
    file_locations = {}

    for i, img in enumerate(new_images, 1):
        folder = detect_folder(img.name)
        dest = images_root / folder / img.name
        shutil.copy2(img, dest)
        file_locations[img.name] = folder
        print(f"  [{i}/{len(new_images)}] ✓ {img.name} → {folder}/")

    # Git push
    print(f"\n🔄 Pushing to GitHub...")
    try:
        repo = Repo(REPO_PATH)
        repo.index.add(["images/*"])
        repo.index.commit(f"Add {len(new_images)} visual references")
        origin = repo.remote(name='origin')
        origin.push()
        print(f"  ✓ Pushed!")
    except Exception as e:
        print(f"  ❌ Git error: {e}")
        return

    # Load AI-generated descriptions if available
    descriptions = {}
    if DESCRIPTIONS_FILE.exists():
        print(f"\n📖 Loading AI-generated descriptions...")
        try:
            with open(DESCRIPTIONS_FILE, "r", encoding="utf-8") as f:
                descriptions = yaml.safe_load(f) or {}
            print(f"  ✓ Loaded {len(descriptions)} descriptions")
        except Exception as e:
            print(f"  ⚠️  Could not load descriptions: {e}")

    # Generate markdown
    print(f"\n📝 Updating markdown...")

    # Organize by folder (not by topic)
    by_folder = {}
    for img in new_images:
        folder = file_locations[img.name]
        if folder not in by_folder:
            by_folder[folder] = []
        by_folder[folder].append(img)

    # Append to file
    mode = "a" if OUTPUT_MD.exists() else "w"
    with open(OUTPUT_MD, mode, encoding="utf-8") as f:
        if mode == "w":
            f.write("# ITP 326 Visual Reference Library\n\n")
            f.write("*Organized by type (templates/examples/diagrams/reference)*\n\n")
            f.write("---\n\n")

        # Write in consistent folder order
        folder_order = ["examples", "reference"]
        for folder in folder_order:
            if folder not in by_folder:
                continue

            category_title = get_category_title(folder)
            f.write(f"\n## {category_title}\n\n")

            for img in by_folder[folder]:
                name = sanitize_name(img.name)
                url = get_github_url(img.name, folder)

                # Get AI-generated description if available
                desc_data = descriptions.get(img.name, {})
                triggers = desc_data.get("triggers", f"\"{name.lower()}\", \"{folder}\"")
                description = desc_data.get("description", "[ADD DESCRIPTION]")
                use_when = desc_data.get("use_when", "")
                best_for = desc_data.get("best_for", "")

                f.write(f"### {name}\n")
                f.write(f"**Triggers:** {triggers}\n")
                f.write(f"**Description:** {description}\n")
                if use_when:
                    f.write(f"**Use When:** {use_when}\n")
                if best_for:
                    f.write(f"**Best For:** {best_for}\n")
                f.write(f"**Image:** ![{name}]({url})\n\n")

            f.write("---\n\n")

    print(f"✓ Updated: {OUTPUT_MD}")

    # Summary
    print(f"\n" + "=" * 60)
    print(f"🎉 SUCCESS! Uploaded {len(new_images)} images")
    print(f"=" * 60)
    print(f"\n📂 Folder breakdown:")
    folder_counts = {}
    for folder in file_locations.values():
        folder_counts[folder] = folder_counts.get(folder, 0) + 1
    for folder, count in sorted(folder_counts.items()):
        print(f"  {folder}/: {count} images")

    print(f"\n📋 Next steps:")
    print(f"1. Open: {OUTPUT_MD}")
    print(f"2. Add better triggers + descriptions")
    print(f"3. Upload to Custom GPT")

if __name__ == "__main__":
    main()
