# ITP 326 Custom GPT - Project Structure

## 📁 Directory Layout

```
itp-326-agent/
├── images/
│   ├── examples/              # 7 images - Templates, filled work, personas
│   │   ├── examples_needs-statement__v01.png
│   │   ├── examples__problem-statement__v01.png
│   │   ├── examples__user-persona-drew__v01.jpeg
│   │   ├── examples__user-persona-asaf__v01.jpeg
│   │   ├── example_User_interview_edge_case.png
│   │   └── example_Design_Language_-_layout_example_2.png
│   │
│   └── reference/             # 20 images - Diagrams, guides, frameworks
│       ├── reference_product_architecture_step1_schematic.png
│       ├── reference_product_architecture_step2_cluster.png
│       ├── reference_product_architecture_step3_matrix.png
│       ├── reference_product_architecture_step4_bom.png
│       ├── reference_product_architecture_step4b_final.png
│       ├── reference_product_architecture_types.png
│       ├── reference_Design_Language_-_4_types_with_product_examples.png
│       ├── reference_Design_language_-_4_types_explained_with_visual_metaphors.png
│       ├── reference_Design_Language_-_types_of_products_in_matrix.png
│       ├── reference_Design_Language_-_what_to_include.png
│       ├── reference_Design_Language.png
│       ├── reference_Design_Language_-_layout_example_1.png
│       ├── reference__brainstorming-rules.png
│       ├── reference_steps-design-thinking.png
│       ├── reference_three-S-see-solve-scale.png
│       ├── reference_problem-decomposition.png
│       ├── reference_Concept_selection_matrix.png
│       ├── reference_ethnographic_research_process_summary_research_guide.png
│       ├── reference_ranking_of_needs.png
│       ├── reference_top_three_insights.png
│       ├── reference_user_needs_summary.png
│       ├── reference_user_problem_analysis_needs.png
│       ├── reference_Concept_combination_table.png
│       ├── reference_concept_combination_table_alt.png
│       ├── reference_hierarchial_needs_table.png
│       └── reference_hierarchical_needs_summary.png
│
├── archive/
│   └── old_gpt_instructions/  # Previous iterations (v1-v4, troubleshooting docs)
│
├── GPT_INSTRUCTIONS.md        # Main GPT instructions (upload to Custom GPT)
├── DEPLOYMENT_GUIDE.md        # Step-by-step deployment instructions
├── README.md                  # Project overview
├── CONTRIBUTING.md            # Contribution guidelines
├── LICENSE                    # MIT license
└── upload_visuals_final.py    # Automated image upload script
```

---

## 📄 Key Files

### Core System Files

**`GPT_INSTRUCTIONS.md`**
- Main instructions for Custom GPT
- Defines coaching behavior, feedback model, and stage-by-stage guidance
- References the two knowledge base files
- **Usage:** Copy entire contents into ChatGPT Custom GPT Instructions field

**`upload_visuals_final.py`**
- Automated image upload and organization script
- Auto-categorizes images into examples/ or reference/
- Pushes to GitHub and generates markdown
- **Usage:** `python ~/upload_visuals_final.py`

---

## 📚 Knowledge Base Files (in Obsidian Vault)

These files live in `~/Documents/L.2. Vault/` and are uploaded to Custom GPT:

**`visual_reference_QUICK_LOOKUP.md`**
- 16 standard design concepts
- Simple markdown sections with embedded images
- Each section: heading + keywords + images
- Covers: needs statements, personas, matrices, frameworks, processes

**`visual_reference_CUSTOM_RESPONSES.md`**
- 2 complex multi-step processes
- Product Architecture (6 steps, 6 images)
- Design Language (6 steps, 7 images)
- Detailed presentation instructions for each step

**`ITP 326 - Sp25 - Product Brief.pdf`**
- Course product briefs
- Student assignment context
- Used by GPT to provide relevant advice

---

## 🔄 Workflow

### Adding New Images

1. **Capture** → Take screenshots, name with prefix:
   - `examples_concept-name.png` for filled templates, student work
   - `reference_concept-name.png` for diagrams, guides, rules

2. **Upload** → Place in `~/Desktop/326_screenshots/`

3. **Process** → Run upload script:
   ```bash
   python ~/upload_visuals_final.py
   ```

4. **Update Markdown**:
   - For simple concepts → Add section to `visual_reference_QUICK_LOOKUP.md`
   - For complex concepts → Add to `visual_reference_CUSTOM_RESPONSES.md`

5. **Deploy** → Re-upload knowledge file to Custom GPT

---

## 🎯 System Architecture

### Hybrid Design

The system splits visual references into two files to solve the rendering problem:

**Problem:** Single large file with table → GPT couldn't read entire file due to token limits

**Solution:** Two specialized files:

```
Student Query
     ↓
"needs statement"? → QUICK_LOOKUP.md → Show 1 image
"persona"? → QUICK_LOOKUP.md → Show 2 images
"product architecture"? → CUSTOM_RESPONSES.md → Show 6 images with steps
"design language"? → CUSTOM_RESPONSES.md → Show 7 images with steps
```

### Why This Works

✅ **Simple queries** (80% of cases) → Quick Lookup file is small, loads instantly
✅ **Complex queries** (20% of cases) → Custom Responses has detailed instructions
✅ **No token limits** → Each file stays under GPT's reading limit
✅ **100% image display** → All images render correctly

---

## 📦 Dependencies

### Python Script
- `gitpython` - Git automation
- `pyyaml` - Description file parsing
- `pillow` - Image handling

Install:
```bash
pip install gitpython pyyaml pillow
```

### GitHub
- Repository: `kdlin/itp-326-agent`
- Branch: `main`
- Image hosting via GitHub raw URLs

---

## 🧹 Archive System

Old iterations are preserved in `archive/old_gpt_instructions/`:
- Version 1-4 iterations
- Table-based approaches
- Troubleshooting documentation
- Migration guides

**Do not delete** - useful for understanding system evolution and rollback if needed.

---

## 🔧 Configuration

### Upload Script Settings

Edit `upload_visuals_final.py`:

```python
SOURCE_FOLDER = Path.home() / "Desktop" / "326_screenshots"
REPO_PATH = Path("C:/Users/Kendrick/Desktop/Repos/itp-326-agent")
GITHUB_USERNAME = "kdlin"
REPO_NAME = "itp-326-agent"
OUTPUT_MD = Path.home() / "Documents" / "L.2. Vault" / "visual_reference_library.md"
```

### Folder Detection

Images are auto-categorized by:
1. **Prefix:** `reference_` → reference/, `examples_` → examples/
2. **Keywords:** "diagram", "rule", "guide" → reference/
3. **Default:** → examples/

---

## 📊 Current Stats

- **Total Images:** 27 (7 examples + 20 reference)
- **Concepts Covered:** 18 (16 standard + 2 complex)
- **GitHub URLs:** All working at `raw.githubusercontent.com/kdlin/itp-326-agent/main/images/...`
- **System Version:** Hybrid v1.0
- **Last Updated:** March 6, 2026

---

## 🚀 Quick Start

1. Clone repo: `git clone https://github.com/kdlin/itp-326-agent.git`
2. Install deps: `pip install gitpython pyyaml pillow`
3. Configure script paths
4. Follow `DEPLOYMENT_GUIDE.md` to set up Custom GPT

---
