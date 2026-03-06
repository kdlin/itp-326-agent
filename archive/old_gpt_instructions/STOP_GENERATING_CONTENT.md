# CRITICAL FIX: GPT Is Generating Content Instead of Using File

## 🚨 PROBLEM

The GPT is **NOT using the file at all**. It's generating brand new educational content.

**What the GPT is currently outputting:**
```
A User Persona is a fictional, research-based profile that represents a key segment of your users. It captures the human behind your data—what they do, think, feel, and need.

Personas help design teams:
- Focus on real user goals and behaviors
- Prevent designing for themselves
...
```

**What it SHOULD be outputting (from the file):**
```
Here are user persona examples from Professor Tim's materials:

**Drew - Event Influencer**

![User Persona - Drew](https://raw.githubusercontent.com/.../drew.jpeg)

Drew represents an influencer focused on event attendance (25-34, $50K-$75K income...)

**Asaf - Market Shopper**

![User Persona - Asaf](https://raw.githubusercontent.com/.../asaf.jpeg)

Asaf represents a market shopper with dietary needs (28yo, Tel Aviv...)
```

## ✅ FIX APPLIED

Added **ABSOLUTE RULE** section at the very top with:

1. **Direct callout:**
   ```
   YOU ARE CURRENTLY GENERATING YOUR OWN CONTENT INSTEAD OF USING THE FILE.
   STOP DOING THIS.
   ```

2. **Explicit steps:**
   - STEP 1: Use knowledge base retrieval function
   - STEP 2: Read entire file contents
   - STEP 3: Search for section header
   - STEP 4: Copy EXACTLY what appears after "Response:"
   - STEP 5: Output ONLY that copied text

3. **Visual comparison:**
   - ❌ WRONG: Shows what it's currently doing
   - ✅ CORRECT: Shows what it should do (with actual example from file)

## 📤 UPLOAD

Copy entire `CUSTOM_GPT_INSTRUCTIONS.md` → paste into GPT → save

## 🧪 TEST

Ask: "What is a user persona?"

**Should output:**
- "Here are user persona examples from Professor Tim's materials:"
- Drew image
- Drew description
- Asaf image
- Asaf description

**Should NOT output:**
- "A User Persona is a fictional, research-based profile..."
- Generic educational content
- No images

---

If this still doesn't work, the GPT may have a technical issue accessing the knowledge base file.

---
