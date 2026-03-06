# ITP 326 Custom GPT - Visual Reference System

> Hybrid visual reference system for Cal Poly's ITP 326 (Product Design & Development) Custom GPT with 100% reliable image rendering

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## 📖 Overview

Production-ready Custom GPT system that provides **100% reliable visual reference delivery** for design concepts through a hybrid file architecture.

**Problem Solved:** ChatGPT knowledge base file reading has token limits that caused image truncation. This system uses strategically split files to ensure complete content delivery.

**Key Features:**
- ✅ 27 images across 18 design concepts - all render reliably
- ✅ Hybrid architecture: simple lookups + complex multi-step processes
- ✅ Under 8,000 character instruction limit
- ✅ Files under 5,000 chars each (prevents truncation)
- ✅ Automated upload workflow
- ✅ Self-documenting system

---

## 🚀 Quick Start (5 Minutes)

### 1. Open Custom GPT Editor
https://chat.openai.com/gpts/editor → Select your ITP 326 GPT

### 2. Paste Instructions
- Copy entire contents of `GPT_INSTRUCTIONS.md` (4,617 characters)
- Paste into Instructions field

### 3. Upload Knowledge Files
From `~/Documents/L.2. Vault/`, upload these **4 files**:
- ✅ `visual_reference_QUICK_LOOKUP.md` (16 simple concepts)
- ✅ `visual_reference_PRODUCT_ARCHITECTURE.md` (6-step process)
- ✅ `visual_reference_DESIGN_LANGUAGE.md` (6-step process)
- ✅ `ITP 326 - Sp25 - Product Brief.pdf` (course briefs)

### 4. Test Deployment
```
"What's a needs statement?" → Should show 1 image
"Show me personas" → Should show 2 images
"Explain product architecture" → Should show 6 images
"How do I create a design language?" → Should show 7 images
```

**Done!** All images should display correctly.

---

## 🏗️ System Architecture

### The Hybrid Approach

**Why 4 separate knowledge files?**

ChatGPT has internal token limits when reading knowledge base files. A single large file gets truncated mid-read. Our solution:

```
Student Query
     ↓
GPT checks 4 knowledge files:

1. QUICK_LOOKUP.md (simple concepts, 16 total)
   └─ Needs statements, personas, matrices, frameworks

2. PRODUCT_ARCHITECTURE.md (3,535 chars)
   └─ 6-step process with 6 images

3. DESIGN_LANGUAGE.md (4,745 chars)
   └─ 6-step process with 7 images

4. Product Brief PDF
   └─ Course context
```

**Key Design Decision:** Split complex processes into separate files to prevent truncation while keeping simple concepts together for efficiency.

---

## 📂 Repository Structure

```
itp-326-agent/
├── images/
│   ├── examples/              # 7 images - Templates, filled work, personas
│   └── reference/             # 20 images - Diagrams, processes, frameworks
│
├── archive/
│   └── old_gpt_instructions/  # 19 previous iterations (for context)
│
├── GPT_INSTRUCTIONS.md        # Main instructions (paste into Custom GPT)
├── upload_visuals_final.py    # Automated image upload script
├── CONTRIBUTING.md            # How to contribute
├── LICENSE                    # MIT license
└── README.md                  # This file
```

---

## 🔄 Workflow: Adding New Images

### Step 1: Capture & Name
Add screenshots to `~/Desktop/326_screenshots/` with prefix:
- `examples_concept-name.png` → Student-facing templates, filled work
- `reference_concept-name.png` → Diagrams, guides, frameworks

### Step 2: Upload to GitHub
```bash
python ~/upload_visuals_final.py
```

This script:
- Auto-categorizes images (examples/ or reference/)
- Copies to repository
- Commits and pushes to GitHub
- Generates permanent URLs

### Step 3: Update Knowledge Files

**For simple concepts (single/dual image):**
Add section to `visual_reference_QUICK_LOOKUP.md`:
```markdown
## Concept Name
**Keywords:** "trigger words", "alternate phrases"

![Concept](https://raw.githubusercontent.com/kdlin/itp-326-agent/main/images/folder/filename.png)

---
```

**For complex multi-step processes:**
Create new file or add to existing (keep under 5,000 chars each)

### Step 4: Re-upload to Custom GPT
Upload updated knowledge file to Custom GPT settings

---

## 🐛 Troubleshooting

### Images Not Displaying

**Check 1:** Are all 4 knowledge files uploaded?
- `visual_reference_QUICK_LOOKUP.md`
- `visual_reference_PRODUCT_ARCHITECTURE.md`
- `visual_reference_DESIGN_LANGUAGE.md`
- Product brief PDF

**Check 2:** Do GitHub URLs work in browser?
Test: `https://raw.githubusercontent.com/kdlin/itp-326-agent/main/images/examples/examples_needs-statement__v01.png`

**Check 3:** Are you using the NEW files (not old CUSTOM_RESPONSES.md)?

### Complex Topics Missing Steps

**Symptom:** Design Language only shows Steps 1-4 (missing 5-6)

**Cause:** File too large, getting truncated

**Fix:** Already implemented - separate DESIGN_LANGUAGE.md file (4,745 chars)

### GPT Says "I Don't Have That Visual"

**Check 1:** Is the keyword in QUICK_LOOKUP.md?
- Open file, search for concept name

**Check 2:** For Product Architecture or Design Language, are the separate files uploaded?

---

## 📊 Current System Status

**Images:** 27 total
- Examples: 7 (needs, problem statement, personas, edge case, design language layouts)
- Reference: 20 (processes, matrices, product architecture steps, design language framework)

**Concepts:** 18 total
- Quick Lookup: 16 (single or dual-image concepts)
- Multi-step: 2 (Product Architecture 6-step, Design Language 6-step)

**System Performance:**
- Image display rate: 100% (all 27 images)
- Load time: <5 seconds per query
- Instructions: 4,617 / 8,000 characters (58% used)

---

## 🧠 Design Decisions & Context

### Why Split Files?

**Initial Problem:** Single `visual_reference_library.md` file with table format
- Pro: All concepts in one place
- Con: Hit token limits, GPT couldn't read entire file

**V1 Solution:** Hybrid with QUICK_LOOKUP + CUSTOM_RESPONSES
- Pro: Separated simple from complex
- Con: CUSTOM_RESPONSES still got truncated (7,663 chars)

**V2 Solution (Current):** Split complex into separate files
- QUICK_LOOKUP.md (simple concepts)
- PRODUCT_ARCHITECTURE.md (3,535 chars)
- DESIGN_LANGUAGE.md (4,745 chars)
- Result: 100% read coverage, all images display

### Why This File Structure?

**Knowledge Files Location:** `~/Documents/L.2. Vault/` (Obsidian vault)
- Keeps knowledge separate from code
- Easy to edit in Obsidian
- Version controlled separately if needed

**Images Location:** `images/` in this repository
- GitHub raw URLs for permanent hosting
- No expiration (unlike Imgur, etc.)
- Version controlled with code

### Historical Context

See `archive/old_gpt_instructions/` for 19 previous iterations documenting:
- Table-based approaches (v1-v4)
- Various troubleshooting attempts
- Testing protocols
- Migration guides

These are preserved for understanding system evolution and potential rollback.

---

## 🛠️ Configuration

### Upload Script Settings

Edit `upload_visuals_final.py`:

```python
SOURCE_FOLDER = Path.home() / "Desktop" / "326_screenshots"
REPO_PATH = Path("C:/Users/Kendrick/Desktop/Repos/itp-326-agent")
GITHUB_USERNAME = "kdlin"
REPO_NAME = "itp-326-agent"
```

### Auto-Categorization Logic

Images are sorted by prefix (checked first):
- `reference_*` → `images/reference/`
- `examples_*` → `images/examples/`

Then by keywords (if no prefix):
- Contains "diagram", "rule", "guide", "framework" → `reference/`
- Default → `examples/`

---

## 📘 Course Context

**Course:** ITP 326: Product Design & Development (Cal Poly)

**Design Process:**
1. **Empathize** - User research, personas (Exercise A-C)
2. **Define** - Needs statements, problem statements
3. **Ideate** - Brainstorming, concept development (Exercise D)
4. **Prototype** - CAD, product architecture, design language (Exercise E)
5. **Test** - User testing, iteration (Exercise F)

**GPT Role:** Collaborative design coach that guides student reasoning without producing deliverables

---

## 🤝 Contributing

See `CONTRIBUTING.md` for guidelines.

**Common Contributions:**
- Adding new visual references
- Improving knowledge file organization
- Updating upload script
- Documentation improvements

---

## 📝 License

MIT License - see `LICENSE` file

---

## 📞 Support & Maintenance

**Adding Images:** Run `python ~/upload_visuals_final.py`

**Updating Knowledge:** Edit files in `~/Documents/L.2. Vault/`, re-upload to Custom GPT

**Troubleshooting:** Check this README's troubleshooting section

**Historical Context:** See `archive/old_gpt_instructions/` for iteration history

**Repository:** https://github.com/kdlin/itp-326-agent

---

## 🎯 Success Metrics

After deployment, your GPT should achieve:
- ✅ 100% image display rate (27/27 images)
- ✅ <5 second response time
- ✅ No "I don't have that visual" errors
- ✅ Complete multi-step processes (all 6-7 images)
- ✅ Consistent educational coaching tone

---

**Last Updated:** March 6, 2026
**System Version:** Hybrid v2.0 (4-file architecture)
**Status:** Production-ready ✅
