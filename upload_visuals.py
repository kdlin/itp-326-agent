"""
ITP 326 Visual Library Uploader
Automates: Screenshots → GitHub → Markdown with permanent links

Usage:
1. Put screenshots in Desktop/326_screenshots/
2. Run: python upload_visuals.py
3. Script uploads to GitHub and generates visual_reference_library.md
"""

import shutil
from pathlib import Path
from git import Repo

# ========== CONFIGURATION ==========

# Where your screenshots are
SOURCE_FOLDER = Path.home() / "Desktop" / "326_screenshots"

# Where your GitHub repo is
REPO_PATH = Path("/c/Users/Kendrick/Desktop/Repos/itp-326-agent")
IMAGES_FOLDER = REPO_PATH / "images"

# Your GitHub info
GITHUB_USERNAME = "kdlin"
REPO_NAME = "itp-326-agent"

# Where to save the markdown file
OUTPUT_MD = Path.home() / "Documents" / "L.2. Vault" / "visual_reference_library.md"

# ========== HELPER FUNCTIONS ==========

def get_github_url(filename):
    """Generate GitHub raw URL for a file"""
    return f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{REPO_NAME}/main/images/{filename}"

def sanitize_name(filename):
    """Convert filename to readable title"""
    name = filename.replace(".png", "").replace(".jpg", "").replace("_", " ").replace("-", " ")
    return name.title()

def get_category_from_filename(filename):
    """Guess category from filename for organization"""
    lower = filename.lower()
    if any(word in lower for word in ["ethnographic", "needs", "affinity", "persona", "interview", "observation"]):
        return "user_research"
    elif any(word in lower for word in ["sketch", "concept", "idea", "combination", "matrix", "scoring"]):
        return "ideation"
    elif any(word in lower for word in ["prototype", "model", "test", "render", "cad"]):
        return "prototyping"
    else:
        return "general"

# ========== MAIN SCRIPT ==========

def main():
    # Fix Windows console encoding for emojis
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("=" * 60)
    print("ITP 326 VISUAL LIBRARY UPLOADER")
    print("=" * 60)

    # Step 1: Check if source folder exists
    if not SOURCE_FOLDER.exists():
        print(f"\n❌ Source folder not found: {SOURCE_FOLDER}")
        print("Creating folder...")
        SOURCE_FOLDER.mkdir(parents=True)
        print(f"✓ Created! Put your screenshots there and run again.")
        return

    # Step 2: Find all images
    image_files = list(SOURCE_FOLDER.glob("*.png")) + \
                  list(SOURCE_FOLDER.glob("*.jpg")) + \
                  list(SOURCE_FOLDER.glob("*.jpeg"))

    if not image_files:
        print(f"\n❌ No images found in {SOURCE_FOLDER}")
        print("Add .png or .jpg files and run again!")
        return

    print(f"\n📸 Found {len(image_files)} images to upload")

    # Step 3: Copy images to repo
    print(f"\n📂 Copying images to GitHub repo...")
    for i, img in enumerate(image_files, 1):
        dest = IMAGES_FOLDER / img.name
        shutil.copy2(img, dest)
        print(f"  [{i}/{len(image_files)}] ✓ {img.name}")

    # Step 4: Git operations
    print(f"\n🔄 Committing to Git...")
    try:
        repo = Repo(REPO_PATH)

        # Add all images
        repo.index.add(["images/*"])
        print(f"  ✓ Added {len(image_files)} images to staging")

        # Commit
        commit_message = f"Add {len(image_files)} visual reference images"
        repo.index.commit(commit_message)
        print(f"  ✓ Committed: {commit_message}")

        # Push to GitHub
        origin = repo.remote(name='origin')
        origin.push()
        print(f"  ✓ Pushed to GitHub!")

    except Exception as e:
        print(f"  ❌ Git error: {e}")
        print("  Images copied but not pushed. Check git status manually.")
        return

    # Step 5: Generate markdown file
    print(f"\n📝 Generating markdown file...")

    # Organize by category
    categories = {
        "user_research": ("📋 USER RESEARCH (Exercises A-C)", []),
        "ideation": ("💡 IDEATION (Exercise D)", []),
        "prototyping": ("🧪 PROTOTYPING (Exercises E-F)", []),
        "general": ("🔧 GENERAL TEMPLATES", [])
    }

    for img in image_files:
        category = get_category_from_filename(img.name)
        categories[category][1].append(img)

    # Write markdown file
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write("# ITP 326 Visual Reference Library\n\n")
        f.write("*Auto-generated visual references for tutoring GPT*\n\n")
        f.write(f"**Total Images:** {len(image_files)}\n\n")
        f.write("---\n\n")

        for cat_key, (cat_title, images) in categories.items():
            if not images:
                continue

            f.write(f"## {cat_title}\n\n")

            for img in images:
                name = sanitize_name(img.name)
                url = get_github_url(img.name)

                f.write(f"### {name}\n")
                f.write(f"**Triggers:** \"{name.lower()}\", \"example\", \"template\"\n")
                f.write(f"**Description:** [ADD DESCRIPTION - what does this show?]\n")
                f.write(f"**Image:** ![{name}]({url})\n\n")

            f.write("---\n\n")

    print(f"✓ Created: {OUTPUT_MD}")

    # Final summary
    print(f"\n" + "=" * 60)
    print(f"🎉 SUCCESS! Uploaded {len(image_files)} images")
    print(f"=" * 60)
    print(f"\n📋 Next steps:")
    print(f"1. Open: {OUTPUT_MD}")
    print(f"2. Edit **Triggers** and **Description** fields")
    print(f"3. Upload markdown to your ChatGPT knowledge base")
    print(f"\n💡 To add more images:")
    print(f"   - Put new screenshots in {SOURCE_FOLDER}")
    print(f"   - Run this script again")

if __name__ == "__main__":
    main()
