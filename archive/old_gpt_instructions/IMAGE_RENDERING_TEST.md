# Image Rendering Test - Different Formats

## Test which format ChatGPT renders best

### Format 1: Standard Markdown
```
![User Persona Drew](https://raw.githubusercontent.com/kdlin/itp-326-agent/main/images/examples/examples__user-persona-drew__v01.jpeg)
```

### Format 2: Markdown on separate line
```
Drew - The Influencer

![User Persona Drew](https://raw.githubusercontent.com/kdlin/itp-326-agent/main/images/examples/examples__user-persona-drew__v01.jpeg)
```

### Format 3: Bare URL
```
https://raw.githubusercontent.com/kdlin/itp-326-agent/main/images/examples/examples__user-persona-drew__v01.jpeg
```

### Format 4: Markdown with blank lines
```
Drew - The Influencer

![User Persona Drew](https://raw.githubusercontent.com/kdlin/itp-326-agent/main/images/examples/examples__user-persona-drew__v01.jpeg)

Description text here
```

---

## RECOMMENDATION

Ask your GPT to output a template and see which image format actually displays.

Then we'll update all TEMPLATE rows to use that exact format.

The issue is probably that ChatGPT's markdown renderer has specific requirements for image display that differ from standard markdown.

---

## Quick Test Query

Ask your GPT: "Show me user persona examples"

Then check:
- ✅ Is the structure correct? (both personas, demographic info)
- ❌ Are images displaying?
- If not, what format should we use instead?

---
