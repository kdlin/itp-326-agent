# Reverted to Rigid Instructions (with flexibility after)

## ✅ CHANGE MADE

Reverted back to the rigid structure that was working, but changed ONE line:

### Before (too restrictive):
```
7. Do NOT add your own explanation - the file response is complete
```

### After (allows flexibility):
```
7. After sharing the response from the file, you CAN add additional explanations or answer follow-up questions
```

## 📋 CURRENT INSTRUCTIONS

The GPT now:
1. MUST open the file when it sees trigger keywords
2. MUST copy the Response section VERBATIM
3. MUST include all image markdown lines
4. MUST NOT include the "Triggers:" line
5. **CAN add additional context AFTER sharing the file response**

## 🎯 EXPECTED BEHAVIOR

**Student asks:** "What's a needs statement?"

**GPT will:**
1. Find the Needs Statement section in the file
2. Copy the entire Response (including image markdown)
3. Skip the "Triggers:" line
4. Share that response
5. Optionally add more explanation if helpful

**Student asks:** "What's a needs statement for a water bottle?"

**GPT will:**
1. Share the needs statement response from file (with image)
2. Then provide specific guidance about water bottle needs statements

## 📤 UPLOAD

Copy entire `CUSTOM_GPT_INSTRUCTIONS.md` → paste into GPT Instructions → save

## ✅ THIS SHOULD FIX

- ✅ User Persona will show both images
- ✅ Needs Statement will show image
- ✅ All sections will use the file response
- ✅ No "Triggers:" line will appear
- ✅ GPT can still answer follow-up/specific questions

---
