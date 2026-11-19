# 06 - RAG Basics ⏳

🔗 **Pichle chapters se connection:** LLM ko sirf apna training data pata hai (tumhari files nahi), aur context window bhi limited hai (01). Solution: Vector DB (05) se sirf **relevant tukde** dhoondho aur context window mein daal do. Isi ko RAG kehte hain.

## Kya seekhenge
- **RAG = Retrieval-Augmented Generation**
- Pipeline: **Load → Chunk → Embed → Store → Retrieve → Augment → Generate**
- Chunking basics: bade document ko chhote tukdon mein todna
- Mile hue tukde prompt mein daal ke jawab banwana
- "Mujhe nahi pata" bolna sikhana (jab answer docs mein na ho)

## 🌍 Real world
- Company ka HR policy bot ("meri kitni leaves bachi hain?")
- Perplexity: web se dhoondh ke jawab deta hai
- "Chat with PDF" apps, help-docs pe chalne wale support bots

## 🛠️ Mini project
**Chat with my notes**: is repo ke saare README pe sawal pucho.
