# New Approach: Separate Flexibility Section

## 🔧 STRATEGY

Keep the visual library rules **completely rigid** (don't touch them), but add flexibility in a **separate section**.

## ✅ WHAT I DID

### 1. Reverted Visual Library Rules to Exact Rigid Version
- Rule 7 is back to: "Do NOT add your own explanation - the file response is complete"
- No modifications to the 7 rigid rules
- This keeps User Persona, Needs Statement, and everything working

### 2. Added NEW Section AFTER Visual Library Rules

```markdown
## 💬 GENERAL COACHING & FOLLOW-UP QUESTIONS

For questions NOT covered by the visual library, or for follow-up questions after sharing a visual library response:
- Provide helpful coaching and guidance
- Answer specific questions about their project
- Offer additional context and examples
- Be a collaborative design coach
```

## 🎯 WHY THIS SHOULD WORK

**The visual library section stays untouched:**
- Rule 7 remains rigid
- Forces GPT to read file
- User Persona and Needs Statement work

**The flexibility comes from a separate section:**
- Not part of the 7 rigid rules
- Applies to follow-up questions
- Applies to questions NOT in visual library
- Doesn't interfere with the file reading mechanism

## 📋 EXPECTED BEHAVIOR

**Initial question:** "What's a user persona?"
- GPT follows rigid rules 1-7
- Opens file, copies response verbatim
- Shows both images
- No additional explanation (rule 7 is strict)

**Follow-up question:** "Which persona should I use for my coffee app?"
- This is a follow-up question after sharing visual library response
- GPT can now use the "GENERAL COACHING" section
- Can provide helpful specific guidance

**Non-library question:** "How should I organize my user research data?"
- Not a visual library topic
- GPT uses "GENERAL COACHING" section
- Provides helpful coaching

## 📤 UPLOAD

Copy entire `CUSTOM_GPT_INSTRUCTIONS.md` → paste into GPT → save

## 🧪 TEST

1. "What's a user persona?" → Should show both images (rigid)
2. "What's a needs statement?" → Should show image (rigid)
3. "How do I choose between the two personas?" → Can answer flexibly
4. "How do I analyze my interview data?" → Can coach flexibly

---
