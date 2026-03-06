# Future Modifications Guide

## 🎯 Critical Things to Know

### 1. **The 5,000 Character Rule**
**Most Important Constraint:**
- ChatGPT truncates knowledge base files that are too large
- Keep each knowledge file **under 5,000 characters**
- If a file exceeds this, split it into separate files

**Check file size:**
```bash
wc -c "C:/Users/Kendrick/Documents/L.2. Vault/visual_reference_DESIGN_LANGUAGE.md"
# Output: 4745 (safe - under 5,000)
```

### 2. **The 8,000 Character Limit for Instructions**
- Custom GPT instructions have hard limit: **8,000 characters**
- Current usage: 4,617 characters (58% used)
- **You have ~3,400 characters of buffer**

**Check instruction size:**
```bash
wc -c GPT_INSTRUCTIONS.md
# Output: 4617 (safe - under 8,000)
```

### 3. **File Locations Matter**

**Knowledge files MUST be in Obsidian Vault:**
```
C:\Users\Kendrick\Documents\L.2. Vault\
├── visual_reference_QUICK_LOOKUP.md
├── visual_reference_PRODUCT_ARCHITECTURE.md
├── visual_reference_DESIGN_LANGUAGE.md
└── ITP 326 - Sp25 - Product Brief.pdf
```

**Code/docs in GitHub repo:**
```
C:\Users\Kendrick\Desktop\itp-326-agent\
├── GPT_INSTRUCTIONS.md
├── README.md
└── upload_visuals_final.py
```

**Images in repo (for GitHub URLs):**
```
C:\Users\Kendrick\Desktop\itp-326-agent\images/
├── examples/
└── reference/
```

---

## 🔄 Common Modifications

### A. Adding a New Simple Concept (Single/Dual Image)

**When:** You want to add "Concept Selection Checklist" with 1 image

**Steps:**
1. **Add image to screenshots folder**
   ```bash
   # Name it: reference_concept-selection-checklist.png
   # Place in: ~/Desktop/326_screenshots/
   ```

2. **Run upload script**
   ```bash
   python ~/upload_visuals_final.py
   # This uploads to GitHub and generates URL
   ```

3. **Add section to QUICK_LOOKUP.md**
   ```markdown
   ## Concept Selection Checklist
   **Keywords:** "concept selection", "checklist", "selection criteria"

   ![Concept Selection Checklist](https://raw.githubusercontent.com/kdlin/itp-326-agent/main/images/reference/reference_concept-selection-checklist.png)

   ---
   ```

4. **Check file size**
   ```bash
   wc -c "C:/Users/Kendrick/Documents/L.2. Vault/visual_reference_QUICK_LOOKUP.md"
   # Make sure it's still under 5,000 chars
   ```

5. **Re-upload to Custom GPT**
   - Go to Custom GPT editor
   - Delete old `visual_reference_QUICK_LOOKUP.md`
   - Upload new version
   - Test with query

**No need to change GPT_INSTRUCTIONS.md** (unless adding new stage/guidance)

---

### B. Adding a New Complex Process (Multi-step, 5+ images)

**When:** You want to add "Manufacturing Process" with 8 steps

**Steps:**
1. **Create new knowledge file**
   ```bash
   # Create: visual_reference_MANUFACTURING.md
   # Location: ~/Documents/L.2. Vault/
   ```

2. **Structure it like existing ones**
   ```markdown
   # ITP 326 - Manufacturing Process Visual Reference

   **TRIGGER KEYWORDS:** "manufacturing", "fabrication", "production process"

   **CRITICAL:** This section has 8 images across 8 steps. You MUST show ALL 8 images.

   ## 🏭 MANUFACTURING PROCESS

   ### Step 1: Material Selection
   ![Step 1](URL)
   Description...

   ### Step 2: Tooling
   ![Step 2](URL)
   Description...

   ... (continue for all 8 steps)
   ```

3. **Keep under 5,000 characters**
   ```bash
   wc -c visual_reference_MANUFACTURING.md
   # If over 5,000, split into two files
   ```

4. **Update GPT_INSTRUCTIONS.md**
   ```markdown
   ## VISUAL REFERENCE SYSTEM

   You have 5 knowledge base files:  # ← Change from 4 to 5

   **`visual_reference_MANUFACTURING.md`** - Manufacturing process  # ← Add this
   - **REQUIRED for:** Any "manufacturing" query
   - 8 steps with 8 images - show ALL images in sequence
   - Follow format EXACTLY as written in file
   ```

5. **Update file list at bottom**
   ```markdown
   ## KNOWLEDGE BASE FILES REQUIRED
   1. visual_reference_QUICK_LOOKUP.md (16 concepts)
   2. visual_reference_PRODUCT_ARCHITECTURE.md (6-step process)
   3. visual_reference_DESIGN_LANGUAGE.md (6-step process)
   4. visual_reference_MANUFACTURING.md (8-step process)  # ← Add this
   5. ITP 326 - Sp25 - Product Brief.pdf (course briefs)
   ```

6. **Check instruction size**
   ```bash
   wc -c GPT_INSTRUCTIONS.md
   # Make sure still under 8,000 chars
   ```

7. **Upload to Custom GPT**
   - Upload new `visual_reference_MANUFACTURING.md`
   - Update instructions with new `GPT_INSTRUCTIONS.md`
   - Test

---

### C. Modifying Existing Instructions/Coaching

**When:** You want to change how GPT coaches students on brainstorming

**Steps:**
1. **Edit GPT_INSTRUCTIONS.md**
   ```markdown
   ## STAGE 2: IDEATION (Exercise D)

   **3. Internal Search** - Brainstorming (Visual: Brainstorming Rules)
   Ask: "Which ideas are furthest apart? Which challenges assumptions?"

   # Add your new coaching questions here
   Also ask: "Have you considered reverse brainstorming?"
   ```

2. **Check character count**
   ```bash
   wc -c GPT_INSTRUCTIONS.md
   # Stay under 8,000
   ```

3. **Update Custom GPT**
   - Paste updated `GPT_INSTRUCTIONS.md` into instructions field
   - Save
   - Test with student query

**Note:** You do NOT need to re-upload knowledge files unless images changed

---

### D. Replacing/Updating an Image

**When:** You have a better version of "Needs Statement" template

**Steps:**
1. **Use EXACT same filename**
   ```bash
   # Old: examples_needs-statement__v01.png
   # New: examples_needs-statement__v01.png  (same name!)
   ```

2. **Place in screenshots folder**
   ```bash
   ~/Desktop/326_screenshots/examples_needs-statement__v01.png
   ```

3. **Run upload script**
   ```bash
   python ~/upload_visuals_final.py
   # This overwrites old image in GitHub
   ```

4. **Wait 5 minutes** (GitHub CDN cache)

5. **Test in Custom GPT**
   - Ask: "What's a needs statement?"
   - Should show new image

**No need to change knowledge files** (URL stays the same)

---

## ⚠️ Common Pitfalls to Avoid

### 1. File Too Large → GPT Can't Read It All
**Symptom:** GPT says "I can see Steps 1-4" but file has 8 steps

**Fix:**
```bash
wc -c problem_file.md
# If over 5,000 chars, split into 2 files
```

### 2. Instructions Too Long → Can't Save
**Symptom:** Custom GPT editor says "Instructions too long"

**Fix:**
- Remove verbose explanations
- Use bullet points instead of paragraphs
- Move detailed info to knowledge files

### 3. Wrong File Location → GPT Can't Find Knowledge
**Symptom:** "I don't have that visual"

**Fix:**
- Knowledge files MUST be uploaded to Custom GPT settings
- Check: Settings → Knowledge → Should see 4 files listed

### 4. Forgot to Re-upload After Edit
**Symptom:** Changes don't appear when testing

**Fix:**
- Delete old file from Custom GPT
- Upload new version
- Always test after uploading

### 5. Image URL Broken → Image Doesn't Display
**Symptom:** GPT shows markdown link instead of image

**Fix:**
```bash
# Test URL in browser:
https://raw.githubusercontent.com/kdlin/itp-326-agent/main/images/examples/filename.png

# If 404, check GitHub repo images/ folder
ls images/examples/
```

---

## 🧪 Testing Workflow

After ANY modification:

### 1. Test Simple Concept
```
Ask: "What's a needs statement?"
Expected: Shows 1 image immediately
```

### 2. Test Complex Process
```
Ask: "Explain product architecture"
Expected: Shows all 6 images with step-by-step
```

### 3. Test Your New Addition
```
Ask: [Query for new concept]
Expected: Shows expected images/content
```

### 4. Check No Regressions
```
Ask 2-3 random existing queries
Expected: All still work correctly
```

---

## 📊 File Size Budget

**Current usage:**

| File | Size | Limit | Buffer |
|------|------|-------|--------|
| GPT_INSTRUCTIONS.md | 4,617 | 8,000 | 3,383 ✅ |
| QUICK_LOOKUP.md | ~4,000 | 5,000 | 1,000 ✅ |
| PRODUCT_ARCHITECTURE.md | 3,535 | 5,000 | 1,465 ✅ |
| DESIGN_LANGUAGE.md | 4,745 | 5,000 | 255 ⚠️ |

**When to split QUICK_LOOKUP.md:**
- When it reaches ~4,800 characters
- Split by category (e.g., Research vs Ideation vs Prototyping)

**When to split DESIGN_LANGUAGE.md:**
- It's already near limit (4,745 / 5,000)
- If adding content, consider splitting into:
  - DESIGN_LANGUAGE_PART1.md (Steps 1-3)
  - DESIGN_LANGUAGE_PART2.md (Steps 4-6)

---

## 🔍 Debugging Checklist

**GPT not showing images?**
- [ ] Are all 4 knowledge files uploaded to Custom GPT?
- [ ] Did you test GitHub URL in browser?
- [ ] Did you use exact markdown format: `![alt](URL)`?
- [ ] Is Custom GPT using latest instructions?

**GPT missing steps in complex process?**
- [ ] Check file size: `wc -c filename.md`
- [ ] If over 5,000 chars, split into 2 files
- [ ] Re-upload both files to Custom GPT

**Can't save GPT instructions?**
- [ ] Check char count: `wc -c GPT_INSTRUCTIONS.md`
- [ ] If over 8,000, remove verbose text
- [ ] Move details to knowledge files instead

**GPT says "I don't have that visual"?**
- [ ] Check trigger keywords in knowledge file
- [ ] Try exact phrasing from keywords list
- [ ] Verify file is uploaded to Custom GPT

---

## 💡 Best Practices

### 1. Always Check File Sizes
```bash
# Before uploading to Custom GPT:
wc -c GPT_INSTRUCTIONS.md
wc -c ~/Documents/L.2.\ Vault/visual_reference_*.md
```

### 2. Test Before Committing
- Make changes
- Upload to Custom GPT
- Test 3-4 queries
- If works, commit to GitHub

### 3. Document Your Changes
```bash
git commit -m "Add Manufacturing Process visual reference

- Created visual_reference_MANUFACTURING.md (4,200 chars)
- Added 8-step process with 8 images
- Updated GPT_INSTRUCTIONS.md to reference new file
- Tested: All images display correctly
"
```

### 4. Keep Archive Updated
When you make significant changes, save context:
```bash
cp GPT_INSTRUCTIONS.md archive/GPT_INSTRUCTIONS_v3_with_manufacturing.md
echo "Added manufacturing on March 15, 2026" >> archive/CHANGELOG.md
```

### 5. Use Version Control
```bash
# Before major changes:
git checkout -b add-manufacturing-process

# Make changes, test

# If works:
git checkout main
git merge add-manufacturing-process
git push

# If breaks:
git checkout main  # Revert to working version
```

---

## 🆘 Emergency Rollback

**If you break something and need to revert:**

### Option 1: Revert Git Commit
```bash
git log  # Find last good commit
git revert <commit-hash>
git push
```

### Option 2: Use Archive Files
```bash
# Copy last known good version:
cp archive/GPT_INSTRUCTIONS_LAST_WORKING.md GPT_INSTRUCTIONS.md

# Re-upload to Custom GPT
```

### Option 3: Check GitHub History
```bash
# View file at previous commit:
git show <commit-hash>:GPT_INSTRUCTIONS.md

# Restore entire file from history:
git checkout <commit-hash> GPT_INSTRUCTIONS.md
```

---

## 📞 Quick Reference Commands

```bash
# Check file sizes
wc -c GPT_INSTRUCTIONS.md
wc -c ~/Documents/L.2.\ Vault/visual_reference_*.md

# Upload new images
python ~/upload_visuals_final.py

# Test GitHub URL
curl -I https://raw.githubusercontent.com/kdlin/itp-326-agent/main/images/examples/filename.png

# View recent commits
git log --oneline -5

# Check what changed
git diff GPT_INSTRUCTIONS.md

# See file at specific commit
git show <commit>:GPT_INSTRUCTIONS.md
```

---

## 🎯 Summary

**Golden Rules:**
1. Keep knowledge files under 5,000 characters
2. Keep instructions under 8,000 characters
3. Always test after uploading
4. Commit working versions to git
5. Document what you changed

**Modification Pattern:**
1. Make change (edit file)
2. Check file size (wc -c)
3. Upload to Custom GPT
4. Test (3-4 queries)
5. Commit to GitHub (if works)

**When in doubt:**
- Check `archive/` for historical context
- Test in Custom GPT before committing
- Keep backups of working versions

---

**You're ready for any future modifications!** 🚀
