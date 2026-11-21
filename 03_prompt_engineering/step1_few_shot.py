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


def ask(messages):
    response = client.chat.completions.create(model=model, messages=messages, temperature=0, max_tokens=60)
    return response.choices[0].message.content.strip()


# Customer reviews we want to label
reviews = [
    "Paneer ekdum fresh tha, maza aa gaya 😋",
    "Paise waste, kabhi order mat karna",
    "Delivery time pe aayi, taste average tha",
]


# ---------- Way 1: vague zero-shot (no rules, no examples) ----------
print("=== Way 1: Vague prompt ===")
for review in reviews:
    messages = [{"role": "user", "content": "What is the sentiment of this review: " + review}]
    print("📝", review, "\n   →", ask(messages), "\n")


# ---------- Way 2: clear zero-shot (clear rules, still no examples) ----------
rules = "Classify the sentiment of the review. Reply with exactly one word: POSITIVE, NEGATIVE or NEUTRAL."

print("=== Way 2: Clear instructions (zero-shot) ===")
for review in reviews:
    messages = [
        {"role": "system", "content": rules},
        {"role": "user", "content": review},
    ]
    print("📝", review, "→", ask(messages))


# ---------- Way 3: few-shot (clear rules + a few solved examples) ----------
# NEW - examples are written as a fake past chat: user asks, assistant answers in the exact format we want
examples = [
    {"role": "user", "content": "Khana bahut tasty tha, delivery bhi fast thi!"},
    {"role": "assistant", "content": "POSITIVE"},
    {"role": "user", "content": "Order 2 ghante late aaya aur khana thanda tha."},
    {"role": "assistant", "content": "NEGATIVE"},
    {"role": "user", "content": "Theek tha, kuch khaas nahi."},
    {"role": "assistant", "content": "NEUTRAL"},
]

print("\n=== Way 3: Few-shot (rules + 3 examples) ===")
for review in reviews:
    messages = [{"role": "system", "content": rules}] + examples + [{"role": "user", "content": review}]
    print("📝", review, "→", ask(messages))
