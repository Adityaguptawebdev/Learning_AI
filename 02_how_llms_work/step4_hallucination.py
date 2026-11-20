# Step 1: Import libraries
import os
from dotenv import load_dotenv
from openai import OpenAI

# Step 2: Connect to Ollama (same as before)
load_dotenv()
client = OpenAI(
    base_url=os.getenv("OLLAMA_BASE_URL"),
    api_key=os.getenv("OLLAMA_API_KEY"),
)
model = os.getenv("MODEL_NAME")


# Helper: ask one question, with an optional system prompt. temperature=0 so results repeat.
def ask(question, system_prompt=None):
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": question})
    response = client.chat.completions.create(model=model, messages=messages, temperature=0, max_tokens=80)
    return response.choices[0].message.content.strip()


compare = "Which number is bigger: 9.11 or 9.9? Answer in one line."
papers = "Give 1 research paper on Hindi tokenization with authors, year and title. Be specific. One line."
fake_movie = "Explain the plot of the 2019 Bollywood movie 'Chai Pe Charcha Express' in 1 line."
after_cutoff = "Who won the 2025 ICC Champions Trophy cricket final? Answer in one line."


# ---------- Part A: SEE hallucination ----------
print("=== Part A: Hallucination ===")
print("🔢 9.11 vs 9.9 (sahi jawab: 9.9):")
print("  ", ask(compare))
print("📄 Research paper (author/title/year check karna padega):")
print("  ", ask(papers))
print("🎬 Fake movie (exist nahi karti):")
print("  ", ask(fake_movie))
print("🏏 After training cutoff (model ka data Dec 2023 tak hai):")
print("  ", ask(after_cutoff))


# ---------- Part B: FIX 1 - allow the model to say "I don't know" ----------
honest = "Only answer if you are sure. If you don't know or are not sure, say exactly: Mujhe nahi pata."

print("\n=== Part B: Fix 1 - system prompt: 'nahi pata to bolo' ===")
print("🔢", ask(compare, honest))
print("📄", ask(papers, honest))


# ---------- Part C: FIX 2 - give the facts inside the prompt (this is the idea behind RAG) ----------
facts = "Fact: India won the 2025 ICC Champions Trophy, beating New Zealand in the final on 9 March 2025."

print("\n=== Part C: Fix 2 - facts prompt mein do ===")
print("🏏", ask(facts + "\n\nUsing only the fact above: " + after_cutoff))


# ---------- Part D: FIX 3 - let code do the exact work (this is the idea behind tools, chapter 08) ----------
print("\n=== Part D: Fix 3 - exact kaam code se karwao ===")
print("🔢 Python says bigger number is:", max(9.11, 9.9))
