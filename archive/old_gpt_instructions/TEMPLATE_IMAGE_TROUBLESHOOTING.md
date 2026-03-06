# Template Image Display Troubleshooting

## Current Status
- ✅ GPT using template structure correctly
- ✅ SINGLE image rows displaying images
- ❌ TEMPLATE rows NOT displaying images

---

## Diagnostic Questions

When you ask "Show me user persona examples", check:

### 1. Is the text structure correct?
- [ ] Both personas shown (Drew and Asaf)?
- [ ] Demographics listed correctly?
- [ ] Formatting preserved?

### 2. How are images being output?
Check if GPT is outputting images as:
- [ ] Regular markdown: `![Drew](URL)`
- [ ] In a code block: ` ```![Drew](URL)``` `
- [ ] As plain URLs without markdown
- [ ] Something else?

### 3. Compare to working SINGLE images
When you ask "What's a needs statement?":
- [ ] Does the image display?
- [ ] What format is it output in?
- [ ] Is it different from template images?

---

## Possible Solutions

### Solution 1: GPT is using code blocks
**If** GPT outputs templates in code blocks/quotes:
- Update instructions: "Never use code blocks for TEMPLATE content"
- Emphasize: "Output as regular markdown"

### Solution 2: Missing blank lines
**If** images need spacing:
- Update templates to have blank lines around each image
- Format: `text\n\n![image](url)\n\ntext`

### Solution 3: ChatGPT markdown rendering issue
**If** markdown isn't rendering at all:
- Try bare URLs instead: Just `https://...` on own line
- Update all TEMPLATE rows to use plain URLs

### Solution 4: Character encoding
**If** markdown syntax is being escaped:
- Check if `!` and `[]` are being escaped
- Update instructions to explicitly NOT escape

---

## Next Step

Please test and report back:
1. What format is GPT outputting images in for templates?
2. How does it compare to SINGLE image format (which works)?
3. Is there any difference in the markdown syntax?

Then we'll update templates to match whatever works for SINGLE rows.

---
