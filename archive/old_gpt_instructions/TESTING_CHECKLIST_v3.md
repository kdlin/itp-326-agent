# ITP 326 GPT - Testing Checklist v3

After uploading `visual_reference_library_v3.md` and updating GPT instructions, test with these queries:

---

## PART 1 TESTS (Quick Reference Table)

These should insert a SINGLE image contextually into an educational response:

### Test 1: Needs Statement
**Query:** "What's a needs statement?"
**Expected:** GPT explains needs statements AND includes the image from the table naturally in the explanation
**URL should appear:** `examples_needs-statement__v01.png`

### Test 2: Edge Case User
**Query:** "Can you explain edge case users?"
**Expected:** GPT explains edge cases AND shows the Eagle Scout example image
**URL should appear:** `example_User_interview_edge_case.png`

### Test 3: Brainstorming Rules
**Query:** "What are the seven rules of brainstorming?"
**Expected:** GPT lists the rules AND shows the reference image
**URL should appear:** `reference__brainstorming-rules.png`

### Test 4: Concept Selection Matrix
**Query:** "How do I score my concepts?"
**Expected:** GPT explains scoring matrices AND shows the example image
**URL should appear:** `reference_Concept_selection_matrix.png`

---

## PART 2 TESTS (Structured Templates)

These should output the EXACT template content between BEGIN/END markers:

### Test 5: User Personas
**Query:** "Show me user persona examples"
**Expected output (EXACT):**
```
Here are two user persona examples from ITP 326:

**Drew - The Influencer**
![User Persona Drew](https://raw.githubusercontent.com/kdlin/itp-326-agent/main/images/examples/examples__user-persona-drew__v01.jpeg)
- Age: 25-34
- Income: $50K-$75K
- Tech proficiency: High
- Focus: Event attendance, social sharing, early access
- Pain points: Finding time and staying on budget

**Asaf - The Market Shopper**
![User Persona Asaf](https://raw.githubusercontent.com/kdlin/itp-326-agent/main/images/examples/examples__user-persona-asaf__v01.jpeg)
- Age: 28
- Income: 9K/month
- Location: Tel Aviv
- Tech proficiency: Medium-high
- Focus: Variety, dietary needs, time-efficiency
- Pain point: Hard time finding vegetarian restaurants
```

**Check:**
- [ ] Both personas shown
- [ ] Both images render
- [ ] No extra GPT commentary mixed in
- [ ] Order is Drew then Asaf

---

### Test 6: Product Architecture
**Query:** "Explain product architecture"
**Expected:** Template with ALL 6 images in exact order:
1. Step 1 - Schematic
2. Step 2 - Cluster Elements
3. Step 3 - Configuration Matrix
4. Step 4 - BOM & Interactions
5. Step 4B - Final Design
6. Architecture Types - Modular vs Integral

**Check:**
- [ ] All 6 images shown
- [ ] In correct sequence
- [ ] No images skipped
- [ ] Starts with "The product architecture process uses a systematic 4-step method with 6 key visuals:"
- [ ] No GPT paraphrasing

---

### Test 7: Design Language
**Query:** "How do I create a design language board?"
**Expected:** Step-by-step template with 6 embedded images:
1. 4-Type Framework with Product Examples
2. 4-Type Framework with Visual Metaphors
3. Product Matrix Examples
4. What to Include in Design Language Board
5. Mood Board Example - Minimalist
6. Mood Board Example - Natural Textures
7. Mood Board Example - Abstract Materials

**Check:**
- [ ] All steps 1-6 shown
- [ ] All 6+ images embedded in correct positions
- [ ] Ends with "Our product feels like ______ because..."
- [ ] No modifications to template text

---

### Test 8: Concept Combination Tables
**Query:** "Show me concept combination table examples"
**Expected:** BOTH examples:
- Example 1 - Camping Pan
- Example 2 - Flashlight

**Check:**
- [ ] Both examples shown
- [ ] Both images render
- [ ] Descriptions intact
- [ ] No paraphrasing

---

### Test 9: Hierarchical Needs
**Query:** "Show me hierarchical needs examples"
**Expected:** BOTH examples:
- Example 1 - Camping Pan Needs Table
- Example 2 - Pen Design Summary

**Check:**
- [ ] Both examples shown
- [ ] Both images render
- [ ] Starts with "Hierarchical needs structures organize user needs by importance and type"
- [ ] No modifications

---

## FAILURE SCENARIOS TO WATCH FOR

**❌ BAD:** GPT says "Here are some examples..." then paraphrases
**✅ GOOD:** GPT outputs template exactly as written

**❌ BAD:** GPT skips images in multi-image templates
**✅ GOOD:** All images in correct order

**❌ BAD:** GPT adds its own commentary between template sections
**✅ GOOD:** Template copied verbatim with no additions

**❌ BAD:** Images don't render (broken URLs)
**✅ GOOD:** All images display correctly

---

## QUICK VALIDATION

**If templates still fail:**
1. Check if GPT is reading the BEGIN/END markers
2. Verify visual_reference_library_v3.md uploaded correctly
3. Confirm GPT instructions reference "visual_reference_library_v3.md" (not v2 or v1)
4. Test with exact trigger phrases from the templates

---

## SUCCESS CRITERIA

✅ **PASS:** All Part 1 tests show images contextually
✅ **PASS:** All Part 2 tests output exact template content
✅ **PASS:** Zero paraphrasing in templates
✅ **PASS:** All images render correctly

---
