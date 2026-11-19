# 02 - How LLMs Work ⏳

🔗 **Chapter 01 se connection:** LLM use kar liya, aur "context window" aur "tokens" ke naam bhi sun liye. Ab dekhenge ki LLM ke andar asal mein hota kya hai.

## Kya seekhenge
- **Token & Tokenizer**: text ko chhote tukdon (tokens) mein todna
- **Next-token prediction**: LLM ek-ek token guess karke poora jawab banata hai
- **Training vs Inference**: model ka seekhna vs model ko use karna
- **Parameters**: `3b`, `70b` ka matlab
- **Transformer & Attention**: simple picture mein, bina maths
- **Temperature / top_p**: creative jawab vs fixed jawab
- **Hallucination**: AI confident hoke galat kyun bolta hai

## 🌍 Real world
- Phone keyboard ka next-word suggestion isi idea ka chhota version hai
- OpenAI / Claude APIs ka bill **tokens** ke hisaab se banta hai
- 2023 mein US ke kuch lawyers ne ChatGPT ke banaye **fake court cases** court mein submit kar diye (hallucination!)

## 🛠️ Mini project
Ek hi prompt ko temperature `0` aur `1.5` pe chalao aur jawab compare karo.
