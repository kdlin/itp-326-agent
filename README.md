# ITP 326 Visual Reference Library

> Automated visual reference management system for ITP 326 (Product Design & Development) Custom GPT

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 📖 Overview

This project automates the workflow for managing a visual reference library for an ITP 326 course Custom GPT. It replaces a manual 3-4 hour process with a **10-minute automated workflow** that:

- Auto-categorizes and uploads 80+ educational screenshots
- Generates AI-powered contextual descriptions
- Pushes images to GitHub for permanent URLs
- Creates markdown knowledge base files for ChatGPT Custom GPT integration

**Result:** Students get instant access to relevant templates, examples, and reference diagrams through natural language queries.

## ✨ Features

- **🤖 AI-Powered Descriptions**: Uses Claude's vision capabilities to generate contextual descriptions for each image
- **📁 Smart Auto-Categorization**: Automatically organizes images into `examples/` or `reference/` based on filename prefixes
- **🔗 Permanent URLs**: GitHub raw URLs that never expire (unlike Imgur or other hosting services)
- **📝 Markdown Generation**: Creates formatted knowledge base files ready for ChatGPT upload
- **🔄 Append-Only Updates**: Preserves existing entries, only adds new images
- **🎯 Simple Workflow**: Drop screenshots in folder → Run script → Upload to GPT

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Git installed and configured
- GitHub account with repository access

### Installation

1. Clone the repository:
```bash
git clone https://github.com/kdlin/itp-326-agent.git
cd itp-326-agent
```

2. Install dependencies:
```bash
pip install gitpython pyyaml pillow
```

3. Configure the script:

Edit `upload_visuals_final.py` with your paths:
```python
SOURCE_FOLDER = Path.home() / "Desktop" / "326_screenshots"
REPO_PATH = Path("C:/Users/YourName/Desktop/Repos/itp-326-agent")
GITHUB_USERNAME = "yourusername"
REPO_NAME = "itp-326-agent"
```

### Usage

#### Step 1: Add Screenshots

Drop screenshots into `~/Desktop/326_screenshots/`

**Naming Convention:**
- Start with `examples_` for templates, personas, student-facing work
- Start with `reference_` for diagrams, guides, frameworks, rules

Examples:
- `examples_needs-statement.png`
- `examples__user-persona-drew.jpeg`
- `reference_brainstorming-rules.png`
- `reference_problem-decomposition.png`

#### Step 2: Generate AI Descriptions (Optional but Recommended)

Open Claude Code and say:
> "Generate descriptions for new images in 326_screenshots"

Claude will:
- Read all new images visually
- Generate contextual descriptions based on course content
- Update `descriptions.yaml`
- Update the Quick Image Index in markdown

#### Step 3: Run Upload Script

```bash
python ~/upload_visuals_final.py
```

This will:
- ✓ Auto-categorize images (examples/ or reference/)
- ✓ Copy to GitHub repo
- ✓ Commit and push to GitHub
- ✓ Generate markdown with AI descriptions
- ✓ Create permanent URLs

#### Step 4: Update ChatGPT Custom GPT

1. Go to your ITP 326 Custom GPT settings
2. Delete old `visual_reference_library_v2.md`
3. Upload new version from `~/Documents/L.2. Vault/`
4. Save GPT

**Done!** Images now work in ChatGPT.

## 📂 Repository Structure

```
itp-326-agent/
├── images/
│   ├── examples/          # Templates, personas, filled student work
│   │   ├── examples_needs-statement__v01.png
│   │   ├── examples__problem-statement__v01.png
│   │   └── examples__user-persona-drew__v01.jpeg
│   └── reference/         # Diagrams, guides, frameworks, rules
│       ├── reference_problem-decomposition.png
│       ├── reference_steps-design-thinking.png
│       └── reference__brainstorming-rules.png
├── upload_visuals_final.py    # Main automation script
├── descriptions.yaml          # AI-generated image descriptions
└── README.md
```

## 🎯 How It Works

### Architecture

```
Screenshots Folder
       ↓
   [AI Vision]
       ↓
 descriptions.yaml
       ↓
upload_visuals_final.py
       ↓
   [GitHub Push]
       ↓
  Permanent URLs
       ↓
  Markdown File
       ↓
 ChatGPT Custom GPT
```

### The Table-Based Lookup System

The breakthrough for reliable ChatGPT image display was using a **Quick Image Index table** in the markdown:

```markdown
| Student Keywords                    | Image to Show |
| ----------------------------------- | ------------- |
| "user persona", "persona example"   | ![User Persona Drew](URL) |
| "needs statement", "needs format"   | ![Needs Statement](URL)   |
```

This simple lookup table eliminates semantic search ambiguity. ChatGPT just looks up keywords and copies the markdown verbatim.

## 📊 Current System Status

**Total Images:** 8
- Examples: 4 (needs statement, problem statement, 2 personas)
- Reference: 4 (problem decomposition, design thinking, see-solve-scale, brainstorming)

**GitHub URLs:** All working at `https://raw.githubusercontent.com/kdlin/itp-326-agent/main/images/...`

**ChatGPT:** Using `visual_reference_library_v2.md` with Quick Image Index table

## 🛠️ Configuration

### Script Configuration (`upload_visuals_final.py`)

```python
# ========== CONFIGURATION ==========

SOURCE_FOLDER = Path.home() / "Desktop" / "326_screenshots"
REPO_PATH = Path("C:/Users/Kendrick/Desktop/Repos/itp-326-agent")
GITHUB_USERNAME = "kdlin"
REPO_NAME = "itp-326-agent"
OUTPUT_MD = Path.home() / "Documents" / "L.2. Vault" / "visual_reference_library.md"
DESCRIPTIONS_FILE = SOURCE_FOLDER / "descriptions.yaml"
```

### Folder Detection Logic

The script uses prefix-first detection:

1. **Check prefix:** `reference_` → reference/, `examples_` → examples/
2. **Check keywords:** "diagram", "rule", "guide", "framework" → reference/
3. **Default:** → examples/

## 🔧 Troubleshooting

### Images not displaying in ChatGPT

1. Check URLs work in browser
2. Re-upload markdown to ChatGPT
3. Verify table format is intact (no extra columns/rows)

### Script errors

1. Make sure you're in Git Bash (not PowerShell)
2. Use `python ~/upload_visuals_final.py` (with tilde)
3. Check file naming starts with `examples_` or `reference_`

### Need to regenerate markdown

```bash
rm "C:/Users/Kendrick/Documents/L.2. Vault/visual_reference_library_v2.md"
python ~/upload_visuals_final.py
```

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Course Context

This system was built for **ITP 326: Product Design & Development** at USC. The course follows the design thinking framework:

1. **Empathize** - User research, personas (Exercise A)
2. **Define** - Needs statements, problem statements (Exercise C)
3. **Ideate** - Brainstorming, concept development (Exercise D)
4. **Prototype** - CAD, manufacturing (Exercise E)
5. **Test** - User testing, iteration (Exercise F)

The visual library provides students with templates, examples, and reference materials for each stage.

## 🙏 Acknowledgments

- Built with [GitPython](https://gitpython.readthedocs.io/) for Git automation
- AI descriptions powered by [Claude](https://claude.ai/)
- Designed for ChatGPT Custom GPT integration

## 📧 Contact

**Kendrick Lin** - [@kdlin](https://github.com/kdlin)

Project Link: [https://github.com/kdlin/itp-326-agent](https://github.com/kdlin/itp-326-agent)

---

**Ready to add 70+ more images!** The system is production-ready. Just follow the 4-step workflow above.
