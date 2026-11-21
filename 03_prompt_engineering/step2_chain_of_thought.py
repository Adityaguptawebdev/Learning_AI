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


# Helper: ask one question. Returns (answer text, how many tokens the model wrote)
def ask(question, max_tokens=300):
    messages = [{"role": "user", "content": question}]
    response = client.chat.completions.create(model=model, messages=messages, temperature=0, max_tokens=max_tokens)
    return response.choices[0].message.content.strip(), response.usage.completion_tokens


# NEW - pick only the last line "Answer: ..." so our code gets a clean answer
def final_answer(text):
    return text.split("Answer:")[-1].strip()


# Questions where you must THINK (with the correct answer, so we can check)
chai = "A chai stall sells 24 cups in the morning. In the afternoon it sells 6 less than twice the morning. In the evening it sells half of the afternoon. How many cups in total?"
questions = [
    (chai, "87"),
    ("A bat and a ball cost Rs 110 in total. The bat costs Rs 100 more than the ball. How much does the ball cost?", "5"),
    ("When I was 6, my sister was half my age. Now I am 70. How old is my sister?", "67"),
]

direct = " Reply with only the final answer, no explanation."
think = " Let's think step by step. At the end write 'Answer: <answer>'."  # NEW - the chain-of-thought line


# ---------- Part A: direct answer vs step-by-step ----------
print("=== Part A: Direct vs Step-by-step (sahi jawab bracket mein) ===")
for question, correct in questions:
    direct_text, direct_tokens = ask(question + direct, max_tokens=20)
    cot_text, cot_tokens = ask(question + think)
    print("❓", question[:60] + "...", f"(sahi: {correct})")
    print(f"   ⚡ Direct       → {direct_text:<10} ({direct_tokens} tokens)")
    print(f"   🧠 Step-by-step → {final_answer(cot_text):<10} ({cot_tokens} tokens)\n")


# ---------- Part B: see the thinking ----------
print("=== Part B: Model ki 'rough copy' dekho ===")
text, _ = ask(chai + think)
print(text)


# ---------- Part C: limit - step-by-step is not magic ----------
print("\n=== Part C: Limit - yahan step-by-step bhi fail ===")
text, _ = ask("Which number is bigger: 9.11 or 9.9?" + think)
print("🔢 9.11 vs 9.9 (sahi: 9.9) →", final_answer(text))
print("🐍 Python says:", max(9.11, 9.9))
