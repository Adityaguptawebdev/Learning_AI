# Step 1: Import libraries
import os
import math
from dotenv import load_dotenv
from openai import OpenAI

# Step 2: Connect to Ollama (same as before)
load_dotenv()
client = OpenAI(
    base_url=os.getenv("OLLAMA_BASE_URL"),
    api_key=os.getenv("OLLAMA_API_KEY"),
)
model = os.getenv("MODEL_NAME")


# Helper: the server gives "logprob" (a log number). math.exp() turns it into a normal chance, x100 = percent
def to_percent(logprob):
    return math.exp(logprob) * 100


# ---------- Part A: the LLM's choices for ONE next token ----------

print("=== Part A: 'The capital of France is' ke baad kaunsa token? ===")
response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Complete with one word: The capital of France is"}],
    max_tokens=1,
    logprobs=True,     # NEW - also send the probabilities
    top_logprobs=5,    # NEW - show the top 5 candidate tokens
)

first_token = response.choices[0].logprobs.content[0]
for candidate in first_token.top_logprobs:
    percent = to_percent(candidate.logprob)
    bar = "█" * int(percent / 5)               # 1 block = 5%
    print(f"{candidate.token!r:12} {percent:6.2f}%  {bar}")


# ---------- Part B: a full reply is just MANY next-token choices ----------

print("\n=== Part B: jawab token-by-token, har token pe options ===")
response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Complete in a few words: Python is a"}],
    max_tokens=8,
    logprobs=True,
    top_logprobs=3,
)

for token_info in response.choices[0].logprobs.content:
    options = []
    for candidate in token_info.top_logprobs:
        options.append(f"{candidate.token!r} {to_percent(candidate.logprob):.0f}%")
    print(f"chosen {token_info.token!r:16} | options: " + ", ".join(options))
