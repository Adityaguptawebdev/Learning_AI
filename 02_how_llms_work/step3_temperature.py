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


# ---------- Part A: HOW temperature changes the chances ----------
# Get the top 5 options for the first token (same as step 2), then re-calculate
# their chances at different temperatures: chance = exp(logprob / temperature)

print("=== Part A: 'Python is a' ke baad pehle token ke chances ===")
response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Complete in a few words: Python is a"}],
    max_tokens=1,
    logprobs=True,
    top_logprobs=5,
)
candidates = response.choices[0].logprobs.content[0].top_logprobs

for temperature in [0.2, 1.0, 2.0]:
    print(f"\n🌡️ temperature = {temperature}")
    weights = [math.exp(c.logprob / temperature) for c in candidates]
    total = sum(weights)
    for c, w in zip(candidates, weights):
        percent = w / total * 100
        print(f"  {c.token!r:14} {percent:5.1f}%  " + "█" * int(percent / 5))


# ---------- Part B: REAL replies at different temperatures ----------

prompt = "Write a one-line slogan for a chai shop."

for temperature in [0, 0.8, 1.8]:
    print(f"\n=== Part B: temperature = {temperature} (3 tries) ===")
    for attempt in range(3):
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,  # NEW - controls the randomness
            max_tokens=40,
        )
        print(f"  {attempt + 1}.", response.choices[0].message.content.strip())
