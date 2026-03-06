# Table Format - Upload Guide

## ✅ WHAT CHANGED

**Old approach:**
- Sections with full content
- GPT retrieval only getting first few sections
- User Persona buried at position 5 → not retrieved

**New approach:**
- Single unified table with 32 rows
- Each image is its own row
- Keywords trigger individual rows
- GPT can match any row by keywords

---

## 📤 UPLOAD INSTRUCTIONS

### Step 1: Remove old file
- Go to GPT Configuration → Knowledge
- Delete `visual_reference_library_v2_COMPLETE.md` (or keep as backup)

### Step 2: Upload new table file
- Upload `visual_reference_library_TABLE_FORMAT.md` from:
```
C:\Users\Kendrick\Documents\L.2. Vault\visual_reference_library_TABLE_FORMAT.md
```

### Step 3: Update instructions
- Copy entire contents of `GPT_INSTRUCTIONS_TABLE_FORMAT.md`
- Paste into GPT Instructions field
- Save

---

## 🧪 TESTING

After uploading, test these queries:

### Test 1: Single image query
```
What's a needs statement?
```
**Expected:**
- Shows 1 image (needs statement template)
- Brief description
- Continues tutoring

### Test 2: Multi-image query (Product Architecture)
```
Explain product architecture
```
**Expected:**
- Shows all 6 images (Steps 1-4B + Types)
- Brief description for each
- Keywords "product architecture" match all 6 rows

### Test 3: Multi-image query (User Persona)
```
What is a user persona?
```
**Expected:**
- Shows Drew image
- Shows Asaf image
- Keywords "user persona" match both rows

### Test 4: Design Language
```
How do I create a design language board?
```
**Expected:**
- Shows all 7 design language images
- Keywords match all design language rows

---

## 🎯 WHY THIS SHOULD WORK

**Solves the retrieval problem:**
- Each row is independently searchable
- GPT doesn't need to retrieve "sections"
- Just matches keywords → finds rows → displays images

**Example:**
Student asks: "What is a user persona?"

GPT process:
1. Scans table for keyword "user persona"
2. Finds 2 rows: Drew and Asaf
3. Outputs both image markdowns
4. Adds descriptions
5. Continues

**No section retrieval needed!**

---

## 📊 TABLE STRUCTURE

The table has 32 rows:

**Product Architecture:** 6 rows (one per step/type)
**Design Language:** 7 rows (framework, metaphors, examples)
**User Persona:** 2 rows (Drew, Asaf)
**Single-image concepts:** 17 rows (needs statement, brainstorming rules, etc.)

Each row is independently triggered by keywords.

---

## ⚠️ POTENTIAL ISSUE

When students ask "What is product architecture?", they'll get ALL 6 images at once.

**Solutions if this is too much:**
1. Students will naturally see the progression
2. We can add a "Priority" column later to show only top 3 first
3. The comprehensive view might actually be better for learning

---

## 🔧 IF IT DOESN'T WORK

If images still don't show:

**Diagnostic test:**
```
Search visual_reference_library_TABLE_FORMAT.md for the keyword "user persona" and show me all matching rows from the table
```

This will tell us if:
- GPT can access the table
- Keyword matching is working
- The issue is with image rendering vs retrieval

---
