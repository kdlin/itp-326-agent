# Final Fix - Search Entire File

## ✅ WHAT I DID

Created **CUSTOM_GPT_INSTRUCTIONS_FINAL.md** with explicit instructions to:

1. **Search by section name:** Use retrieval to find "## User Persona" specifically (not just load initial chunks)
2. **Request full section:** Get content from that header until next "---"
3. **Don't assume absence:** Just because initial retrieval didn't find it doesn't mean it's not there
4. **Search through 400+ lines:** Explicitly mentions file has 19 sections throughout entire file

## 🔑 KEY INSTRUCTION

The critical part:
```
Use retrieval to search `visual_reference_library_v2_COMPLETE.md` for the EXACT section name (e.g., "## User Persona")

Request the FULL section content from that specific section header until the next "---" divider

The file has 19 sections spread throughout 400+ lines. Do NOT assume a section isn't there just because your initial retrieval didn't find it. Search specifically for the section header by name.
```

## 📤 UPLOAD

**1. Keep the original file:**
- Keep `visual_reference_library_v2_COMPLETE.md` uploaded (don't change it)

**2. Replace instructions:**
- Copy content from: `CUSTOM_GPT_INSTRUCTIONS_FINAL.md`
- Paste into GPT Instructions field
- Save

**3. Test:**
Ask: "What is a user persona?"

**Expected:**
- GPT searches specifically for "## User Persona" in the file
- Retrieves that full section
- Shows Drew and Asaf with images

## 🎯 WHY THIS SHOULD WORK

Instead of relying on default retrieval (which only gets top chunks), this forces the GPT to:
- Search by specific section header name
- Request the full content of that section
- Not give up if it doesn't find it in the initial chunks

This is a targeted search approach rather than sequential reading.

---
