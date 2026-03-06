# ITP 326 GPT - Testing Guide v4 UNIFIED

**New approach:** Everything in one table. GPT scans, finds row, outputs all images.

---

## QUICK TESTS

### Test 1: Single Image (Needs Statement)
**Query:** "What's a needs statement?"
**Expected:**
- ✅ 1 image shown
- ✅ Subject-Verb-Attribute explanation
- ✅ Image integrated naturally in response

---

### Test 2: Two Images (User Personas)
**Query:** "Show me user persona examples"
**Expected:**
- ✅ Drew persona image
- ✅ Asaf persona image
- ✅ Demographics for both (age, income, tech level, focus)
- ✅ Both images shown in order

---

### Test 3: Six Images (Product Architecture)
**Query:** "Explain product architecture"
**Expected:**
- ✅ All 6 images in sequence:
  1. Schematic
  2. Cluster elements
  3. Configuration matrix
  4. BOM
  5. Final design
  6. Modular vs Integral
- ✅ Kettle example descriptions
- ✅ No images skipped

---

### Test 4: Seven Images (Design Language)
**Query:** "How do I create a design language?"
**Expected:**
- ✅ Presented as 6-step process
- ✅ All 7 images embedded correctly:
  - 3 images in Step 2 (4-type framework)
  - 1 image in Step 3 (what to include)
  - 3 mood board examples
- ✅ Ends with "Our product feels like..." statement

---

### Test 5: Contextual Intelligence
**Query:** "I'm working on user personas, what else should I know?"
**Expected:**
- ✅ Shows user persona images
- ✅ Potentially mentions needs statements and shows that image too
- ✅ GPT connects concepts intelligently

This tests if GPT can use table contextually, not just on exact triggers.

---

## SUCCESS CRITERIA

✅ **All images in row are shown** (no skipping)
✅ **Output instructions are followed** (GPT uses the guidance in table)
✅ **Images render correctly** (URLs work)
✅ **Fast and consistent** (table approach should be quick every time)

---

## WHY THIS WORKS BETTER

**Before (v3):** Two systems (table + templates) → GPT confused about when to use each

**Now (v4):** One system (unified table) → GPT always does the same thing:
1. Scan table
2. Find row
3. Output all images
4. Follow instructions

Simple = Reliable.

---

## IF IT FAILS

Check:
1. Is `visual_reference_library_v4_UNIFIED.md` uploaded?
2. Do GPT instructions reference v4?
3. Are you using exact trigger keywords from table?
4. Does the table render correctly in GPT's knowledge view?

---
