# Update: Fixing Images Not Displaying

## 🎯 ISSUE

GPT is now reading the file and using responses (good progress!), but:

1. ❌ Images aren't showing - just text descriptions
2. ❌ "Triggers:" line is being included in responses

## 🔍 ROOT CAUSE

The file DOES have markdown image syntax like:
```markdown
![User Persona - Drew](https://raw.githubusercontent.com/kdlin/itp-326-agent/main/images/examples/examples__user-persona-drew__v01.jpeg)
```

But the GPT is **skipping these lines** when copying the response. It's only copying the text descriptions, not the image markdown.

## ✅ FIXES APPLIED

### Updated `CUSTOM_GPT_INSTRUCTIONS.md` with:

**1. Added to FIRST RULE section:**
```
CRITICAL: When copying from the file, you MUST include ALL markdown image syntax.
- Lines that look like ![text](url) are images - copy them EXACTLY
- Do NOT skip or paraphrase these lines
- Copy the ENTIRE Response section word-for-word
```

**2. Updated the workflow example:**
```
- Copy EVERYTHING after Response: including:
  - ALL text
  - ALL lines that start with ![
  - ALL markdown formatting
- Skip ONLY the "Triggers:" line
- Do NOT paraphrase or skip image lines
```

**3. Made protocol more explicit:**
```
3. Copy the entire Response section VERBATIM - word for word, character for character
4. Include ALL markdown image lines (they look like ![description](url))
5. Do NOT skip, paraphrase, or summarize ANY part
```

## 📤 WHAT TO DO NOW

**1. Re-upload instructions:**
- Copy entire `CUSTOM_GPT_INSTRUCTIONS.md`
- Paste into GPT Instructions field
- Save

**2. Test with:**
```
"What's a user persona?"
```

**Expected output should include:**
```markdown
Here are user persona examples from Professor Tim's materials:

**Drew - Event Influencer**

![User Persona - Drew](...)

Drew represents...

**Asaf - Market Shopper**

![User Persona - Asaf](...)

Asaf represents...
```

**Should NOT include:**
- The "Triggers:" line
- Should include the `![...]` markdown image lines

## 🎯 WHY THIS SHOULD WORK

The instructions now:
- Use "VERBATIM" and "EXACTLY"
- Explicitly mention image markdown syntax
- Show what the syntax looks like (`![text](url)`)
- Say "Do NOT skip" multiple times
- Emphasize "word for word, character for character"

The GPT should now understand it needs to copy the ENTIRE response including image lines, not just the text.

---
