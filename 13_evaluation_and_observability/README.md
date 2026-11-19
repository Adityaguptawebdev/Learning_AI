# 13 - Evaluation & Observability ⏳

🔗 **Pichle chapters se connection:** Bot ban gaya, par kaise pata chale ki woh **sahi** jawab de raha hai? "Lag raha hai theek hai" se kaam nahi chalega, measure karna padega.

## Kya seekhenge
- Eval kyun zaroori hai (AI har baar alag jawab de sakta hai)
- **Test dataset**: sawal + sahi jawab ki list (golden set)
- **LLM-as-a-judge**: ek AI dusre AI ka jawab check kare
- RAG metrics: **faithfulness** (docs se hi bola?), **relevance** (sawal ka jawab diya?)
- **Tracing**: har step ka input/output, time aur cost dekhna
- Tools: Langfuse, LangSmith, Arize Phoenix, RAGAS

## 🌍 Real world
- Companies har prompt ya model change se pehle evals chalati hain, bilkul software tests jaise
- Production mein tracing se pata chalta hai ki kaunsa step slow ya mehenga hai

## 🛠️ Mini project
Apne RAG bot ka 20-sawaal wala eval banao aur score nikalo.
