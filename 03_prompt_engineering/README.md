# 03 - Prompt Engineering ⏳

🔗 **Pichle chapters se connection:** 01 mein `system` role dekha, aur 02 mein samjha ki LLM bas next token predict karta hai. Ab seekhenge ki achha prompt likhkar achha jawab kaise nikalwayein.

## Kya seekhenge
- **Zero-shot vs Few-shot**: bina example vs examples dekar sikhana
- **Role prompting**: system prompt se AI ko role dena
- **Chain-of-thought**: "step by step socho" se better reasoning
- **Structured output**: jawab **JSON** mein lena, taaki code use kar sake
- **Prompt templates**: variables wale reusable prompts

## 🌍 Real world
- Customer support bots ka tone ("polite, short, Hindi mein") system prompt se set hota hai
- HR tools resume se, aur expense apps bill se, data nikal ke JSON banate hain

## 🛠️ Mini project
Resume ka text do → AI se `{name, skills, experience}` JSON nikalwao.
