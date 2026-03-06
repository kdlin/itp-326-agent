# ITP 326 Custom GPT - Deployment Guide

This guide walks you through deploying the hybrid visual reference system to your ChatGPT Custom GPT.

---

## 📋 Pre-Deployment Checklist

Before deploying, ensure you have:

- [ ] All 27 images uploaded to GitHub (`images/examples/` and `images/reference/`)
- [ ] 3 knowledge base files ready in `~/Documents/L.2. Vault/`:
  - `visual_reference_QUICK_LOOKUP.md`
  - `visual_reference_CUSTOM_RESPONSES.md`
  - `ITP 326 - Sp25 - Product Brief.pdf`
- [ ] GPT instructions file: `GPT_INSTRUCTIONS.md`

---

## 🚀 Deployment Steps

### Step 1: Verify GitHub Images

1. Open browser and test a few image URLs:
   ```
   https://raw.githubusercontent.com/kdlin/itp-326-agent/main/images/examples/examples_needs-statement__v01.png
   https://raw.githubusercontent.com/kdlin/itp-326-agent/main/images/reference/reference_product_architecture_step1_schematic.png
   ```

2. Confirm images load correctly

### Step 2: Open Custom GPT Settings

1. Go to https://chat.openai.com/gpts/editor
2. Select your **ITP 326 – Product Design & Development** GPT
3. Click **Configure**

### Step 3: Update Instructions

1. In the **Instructions** field, delete all existing instructions
2. Open `GPT_INSTRUCTIONS.md` from this repo
3. Copy the entire contents
4. Paste into the Instructions field

### Step 4: Upload Knowledge Base Files

1. Scroll to **Knowledge** section
2. **Delete all old visual reference library files** (v1, v2, v3, v4, etc.)
3. Upload the 3 new files:
   - Click **Upload files**
   - Select `visual_reference_QUICK_LOOKUP.md`
   - Click **Upload files** again
   - Select `visual_reference_CUSTOM_RESPONSES.md`
   - Click **Upload files** again
   - Select `ITP 326 - Sp25 - Product Brief.pdf`

4. Verify all 3 files appear in the Knowledge section

### Step 5: Configure Settings

Ensure these settings:
- **Name:** ITP 326 – Product Design & Development
- **Description:** "Collaborative design coach for Cal Poly's ITP 326 course. Guides students through user research, ideation, and prototyping without generating deliverables."
- **Conversation starters:**
  - "What's a needs statement?"
  - "How do I create a design language?"
  - "Explain product architecture"
  - "Show me user persona examples"

### Step 6: Save and Test

1. Click **Save** in top right
2. Click **View GPT** to test
3. Run through the test cases below

---

## ✅ Testing Protocol

Test these queries to ensure everything works:

### Simple Queries (Quick Lookup)
- [ ] "What's a needs statement?" → Should show 1 image
- [ ] "Show me user personas" → Should show 2 images (Drew + Asaf)
- [ ] "What are the brainstorming rules?" → Should show 1 image
- [ ] "Concept combination table?" → Should show 2 images

### Complex Queries (Custom Responses)
- [ ] "Explain product architecture" → Should show 6 images in sequence with step-by-step explanation
- [ ] "How do I create a design language?" → Should show 7 images with 6-step process

### Edge Cases
- [ ] "Help me with hierarchical needs" → Should show 2 images
- [ ] "Product architecture for Exercise E" → Should trigger custom response (6 steps)

---

## 🐛 Troubleshooting

### Images not displaying

**Problem:** GPT describes images but doesn't show them

**Solution:**
1. Check that knowledge files are uploaded (not just referenced)
2. Verify GitHub URLs work in browser
3. Re-upload the Quick Lookup file
4. Test with a simple query like "needs statement"

### Complex topics show no images

**Problem:** Product Architecture or Design Language show no visuals

**Solution:**
1. Verify `visual_reference_CUSTOM_RESPONSES.md` is uploaded
2. Check that GPT instructions mention both files
3. Manually ask: "Check the CUSTOM_RESPONSES file for product architecture"

### GPT can't find a concept

**Problem:** GPT says "I don't have a visual for that"

**Solution:**
1. Check if concept is in Quick Lookup (most common)
2. Check if it's in Custom Responses (Product Arch / Design Language only)
3. Verify keyword matching (e.g., "persona" vs "user persona")

### Only first 3 sections show

**Problem:** GPT stops reading the knowledge file partway through

**Solution:**
This was the OLD problem with table-based format. The new hybrid system fixes this by:
- Using simple markdown sections (not wide tables)
- Splitting complex content into separate file
- Keeping both files under token limits

If this happens:
1. Verify you uploaded the NEW files (QUICK_LOOKUP + CUSTOM_RESPONSES)
2. Delete any old visual_reference_library files (v1-v4, TABLE_FORMAT, etc.)

---

## 📊 Success Metrics

After deployment, your GPT should:

✅ Display images for 100% of standard concepts (16 total)
✅ Show complete 6-step Product Architecture sequence
✅ Show complete 6-step Design Language sequence
✅ Respond to student queries in <5 seconds
✅ Never skip images in multi-image concepts

---

## 🔄 Updating the System

When you add new images:

1. Add screenshots to `~/Desktop/326_screenshots/`
2. Run `python ~/upload_visuals_final.py`
3. Update `visual_reference_QUICK_LOOKUP.md` with new section
4. Re-upload to Custom GPT
5. Test new concept

---

## 📞 Support

If issues persist:
1. Check `archive/old_gpt_instructions/` for iteration history
2. Review GitHub issues: https://github.com/kdlin/itp-326-agent/issues
3. Test URLs directly in browser
4. Verify all 3 knowledge files are uploaded

---

**Last Updated:** March 6, 2026
**System Version:** Hybrid v1.0 (Quick Lookup + Custom Responses)
