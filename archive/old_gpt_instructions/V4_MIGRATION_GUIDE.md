# V4 UNIFIED TABLE - Migration Guide

## WHAT CHANGED

**v3 System:**
- Part 1: Quick Reference Table (13 single-image concepts)
- Part 2: Structured Templates (5 multi-image sequences with BEGIN/END markers)
- **Problem:** GPT handled table perfectly but struggled with templates

**v4 System:**
- ONE unified table with all concepts (18 total)
- Single-image queries: 1 URL in row
- Multi-image queries: Multiple URLs in row (numbered 1, 2, 3...)
- "Output Instructions" column tells GPT how to present
- **Solution:** GPT uses same scanning behavior for everything

---

## WHY IT WORKS

You noticed the table was **fast and reliable** because:
- Structured data (GPT scans rows easily)
- Clear lookup mechanism
- No interpretation needed

So we put **everything in the table**, including multi-image concepts.

Now GPT:
1. Sees "user persona" trigger
2. Scans table
3. Finds row with 2 URLs
4. Outputs both images
5. Follows output instructions

Same fast, reliable behavior for ALL queries.

---

## FILE LOCATIONS

**Upload to GPT Knowledge Base:**
```
visual_reference_library_v4_UNIFIED.md
```

**Use for GPT Instructions:**
```
GPT_INSTRUCTIONS_v4_UNIFIED.md
```

**Testing:**
```
TESTING_v4_UNIFIED.md
```

---

## QUICK COMPARISON

### Single Image (works same as before)
**v3:** Table row → 1 URL → GPT inserts contextually ✅
**v4:** Table row → 1 URL → GPT inserts contextually ✅

### Multiple Images (NOW FIXED)
**v3:** Template with BEGIN/END markers → GPT paraphrases ❌
**v4:** Table row → 6 URLs → GPT outputs all 6 ✅

---

## TABLE STRUCTURE

| Concept | Trigger Keywords | Image URLs (output ALL in order) | Output Instructions |
|---------|-----------------|-----------------------------------|---------------------|
| Needs Statement | "needs statement"... | URL1 | Show image with explanation... |
| User Personas | "user persona"... | URL1 (Drew)<br>URL2 (Asaf) | Show BOTH personas with demographics... |
| Product Architecture | "product architecture"... | URL1 (Schematic)<br>URL2 (Cluster)<br>URL3 (Matrix)<br>URL4 (BOM)<br>URL5 (Final)<br>URL6 (Types) | Show ALL 6 images in order: Step 1... |

---

## UPDATED GPT PROTOCOL

**Old instruction (v3):**
> "Check if query matches table OR template. If template, find BEGIN marker and copy verbatim..."

**New instruction (v4):**
> "Scan table. Find row. Output ALL images. Follow output instructions."

**4 steps instead of complex branching logic.**

---

## BENEFITS

✅ **Faster** - No decision making about "is this a template or table query?"
✅ **More reliable** - Same behavior for all queries
✅ **Easier to maintain** - Add new concepts by adding table rows
✅ **Leverages GPT's strength** - Contextual intelligence around structured data
✅ **Modular** - Easy to add new visual references

---

## TESTING PRIORITY

Test these multi-image concepts first (they failed in v3):
1. User Personas (2 images)
2. Product Architecture (6 images)
3. Design Language (7 images)
4. Concept Combination Tables (2 images)
5. Hierarchical Needs (2 images)

If these work, everything else will work.

---

## WHAT YOU OBSERVED

> "The table is very fast and working quite well. It pulls the image quickly and is pretty good at using it in the response."

Exactly. So now **everything uses the table approach**.

> "Even when I asked about user personas it included that we then use needs statements and inserted the image from the table there"

This is GPT's contextual intelligence. It saw "personas" in the table, but also connected it to "needs statements" (also in table) and pulled both. **This is exactly what we want.**

The unified table lets GPT be smart while staying consistent.

---
