# Learning AI 🤖

My step-by-step journey of learning AI with Python, using a free model that runs on my own laptop (Ollama).
One folder = one concept. Inside it: a short note + small step files.

## Chapters

| # | Concept | Steps |
|---|---|---|
| 00 | [Python Basics](00_python_basics/) | Just enough Python to follow the AI code |
| 01 | [Chat with Local AI](01_chat_with_local_ai/) | ✅ 1. First call · ✅ 2. User input · ✅ 3. Chat loop + .env · ⏳ 4. Memory · ⏳ 5. System prompt · ⏳ 6. Streaming |

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
open -a Ollama
python 01_chat_with_local_ai/step3_chat_loop.py
```
