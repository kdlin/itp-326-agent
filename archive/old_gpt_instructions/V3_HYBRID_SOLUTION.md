# V3 HYBRID - Best of Both Worlds

## THE PROBLEM

**Single images:** Table scanning works perfectly ✓
**Multiple images:** Not displaying, templates failing ✗

## THE SOLUTION

Put **formatted templates inside the table** with a type flag.

---

## TABLE STRUCTURE

| Concept | Triggers | Type | Content |
|---------|----------|------|---------|
| Needs Statement | "needs statement" | SINGLE | ![Image](URL)<br>Brief description |
| User Personas | "user persona" | TEMPLATE | [Full formatted template with both personas] |
| Product Architecture | "product architecture" | TEMPLATE | [Full 6-step formatted template] |

---

## HOW IT WORKS

**GPT behavior:**
1. Scans table for trigger keywords (already working)
2. Finds matching row
3. Checks "Type" column:
   - **SINGLE** → Use image contextually (GPT intelligence)
   - **TEMPLATE** → Copy Content cell exactly (verbatim)

---

## WHY THIS WORKS

✅ **Leverages what's working:** Table scanning was fast and reliable
✅ **Fixes what failed:** Templates are now IN the table (not separate section)
✅ **Consistent behavior:** GPT always scans table, no branching logic
✅ **Simple decision:** Just check Type flag

---

## SINGLE vs TEMPLATE

### SINGLE (13 concepts)
- Needs Statement
- Problem Statement
- Edge Case User
- Brainstorming Rules
- Design Thinking
- Three-S Framework
- Problem Decomposition
- Concept Selection Matrix
- Ethnographic Research
- Ranking Needs
- Top Insights
- User Needs Summary
- User Problem Analysis

**Behavior:** GPT inserts image intelligently into educational response

### TEMPLATE (5 concepts)
- User Personas (2 images)
- Product Architecture (6 images)
- Design Language (7 images)
- Concept Combination Tables (2 images)
- Hierarchical Needs (2 images)

**Behavior:** GPT copies formatted template exactly as written

---

## FILES TO UPLOAD

**Knowledge Base:**
```
visual_reference_library_v3_HYBRID.md
```

**System Instructions:**
```
GPT_INSTRUCTIONS_v3.md (updated with HYBRID protocol)
```

---

## TESTING

**Test SINGLE (should work - already working):**
- "What's a needs statement?" → Image inserted contextually

**Test TEMPLATE (should now work):**
- "Show me user persona examples" → Both personas with formatting
- "Explain product architecture" → All 6 steps in sequence

---

## KEY INSIGHT

You observed:
> "Single link rows are all working though"

So we kept that approach for single-image concepts, and embedded the templates directly in the table for multi-image concepts. Same table-scanning behavior, just different content types.

---
