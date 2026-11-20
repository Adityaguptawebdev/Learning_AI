# Step 1: Import libraries
import os
from dotenv import load_dotenv
from openai import OpenAI

# Step 2: Connect to Ollama (same as chapter 01)
load_dotenv()
client = OpenAI(
    base_url=os.getenv("OLLAMA_BASE_URL"),
    api_key=os.getenv("OLLAMA_API_KEY"),
)
model = os.getenv("MODEL_NAME")

# ---------- Part A: SEE the tokens ----------
# Streaming sends one token per chunk, so we print " | " between them

print("=== Part A: AI ka jawab, token by token ===")
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "Write one short sentence about Python."}],
    stream=True,
)
for chunk in stream:
    piece = chunk.choices[0].delta.content
    if piece:
        print(piece, end=" | ", flush=True)
print("\n")


# ---------- Part B: COUNT the tokens ----------
# The server tells us how many tokens our message used: response.usage.prompt_tokens

def count_tokens(text):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": text}],
        max_tokens=1,  # we only want the count, so ask for a 1-token reply
    )
    return response.usage.prompt_tokens


# Every request has some hidden tokens (role markers etc). Measure them once and subtract.
hidden = count_tokens("")

texts = [
    "Hello, how are you?",
    "Namaste, aap kaise ho?",
    "नमस्ते, आप कैसे हैं?",
    "48271 multiplied by 9183",
]

print("=== Part B: kaun sa text kitne tokens leta hai ===")
print("(hidden tokens har request mein:", hidden, ")")
for text in texts:
    print(count_tokens(text) - hidden, "tokens ->", text)
