# Testing Guide - v3 Self-Contained Approach

## 🎯 THE APPROACH

**GPT Instructions:** Ultra-minimal → "Reference visual_reference_library_v3_SELF_CONTAINED.md"

**Knowledge File:** Self-contained with:
1. Usage instructions at top
2. Templates for Product Architecture & Design Language (with embedded images)
3. Table for everything else (single URLs)

---

## 📤 UPLOAD STEPS

1. **Upload Knowledge File:**
   - File: `visual_reference_library_v3_SELF_CONTAINED.md`
   - Location: GPT Knowledge section

2. **Update Instructions:**
   - Copy content from: `GPT_INSTRUCTIONS_v3_MINIMAL.md`
   - Paste into: GPT Instructions field

3. Save and test

---

## ✅ TEST QUERIES

### Test 1: Template Query (Product Architecture)
**Query:** "Explain product architecture"

**Expected Result:**
- GPT reads template section at top of file
- Uses entire template structure
- All 6 images display in sequence:
  - Step 1 schematic
  - Step 2 clustering
  - Step 3 matrix
  - Step 4 BOM
  - Step 4B final design
  - Architecture types comparison

### Test 2: Template Query (Design Language)
**Query:** "How do I create a design language board?"

**Expected Result:**
- GPT uses design language template
- All 7 images display:
  - 4-type framework
  - Visual metaphors
  - Product matrix
  - What to include
  - 3 mood board examples

### Test 3: Table Query (Single Image)
**Query:** "What's a needs statement?"

**Expected Result:**
- GPT scans IMAGE TABLE
- Finds Needs Statement row
- Displays 1 image with explanation

### Test 4: Table Query (Multi-Image)
**Query:** "Show me user persona examples"

**Expected Result:**
- GPT scans IMAGE TABLE
- Finds Drew AND Asaf rows
- Displays both persona images

### Test 5: Table Query (Concept Combination)
**Query:** "Show me concept combination table examples"

**Expected Result:**
- GPT scans IMAGE TABLE
- Finds both rows (Camping Pan + Flashlight)
- Displays 2 example images

---

## 🔍 WHAT TO CHECK

**For Templates:**
- ✅ All images display (not broken)
- ✅ Structure follows template exactly
- ✅ Images appear in correct order

**For Table Queries:**
- ✅ Images display correctly
- ✅ GPT pulls related images together when appropriate
- ✅ Contextual explanation around images

**If Images Don't Display:**
- Check markdown syntax in file
- Verify GitHub URLs are accessible
- Test one URL directly in browser

---

## 🧪 WHY THIS MIGHT WORK

**Theory:**
- GPT reads entire .md file into context
- Instructions are RIGHT THERE at the top
- Templates have images already embedded (no multi-step lookup)
- Table uses proven single-URL-per-row approach

**Previous failures:**
- Multi-URL rows → Failed
- Reference placeholders → Failed
- Separate instruction file → GPT ignored templates

**This approach:**
- Self-contained (all in one file)
- Instructions + data together
- Templates ready to copy
- Table proven to work

---

## 📊 RESULTS TRACKING

After testing, document:

| Test | Query | Images Display? | Notes |
|------|-------|-----------------|-------|
| 1 | Product Architecture | ☐ Yes ☐ No | |
| 2 | Design Language | ☐ Yes ☐ No | |
| 3 | Needs Statement | ☐ Yes ☐ No | |
| 4 | User Personas | ☐ Yes ☐ No | |
| 5 | Concept Combination | ☐ Yes ☐ No | |

---

## 🚨 TROUBLESHOOTING

**If templates don't show images:**
- Check if GPT is reading the template at all
- Verify markdown image syntax: `![alt](url)`
- Test if changing to HTML `<img>` tag works

**If table queries don't work:**
- Revert to SIMPLE version (proven to work)
- This confirms table approach is solid

**If nothing works:**
- Test if ChatGPT itself can render images from GitHub raw URLs
- May be a platform limitation

---
