# Step 1: Import libraries
import os
from dotenv import load_dotenv
from openai import OpenAI

# Step 2: Load settings from .env and connect to Ollama
load_dotenv()
client = OpenAI(
    base_url=os.getenv("OLLAMA_BASE_URL"),
    api_key=os.getenv("OLLAMA_API_KEY"),
)
model = os.getenv("MODEL_NAME")

# Step 3: NEW - the system prompt (rules + personality for the AI)
system_prompt = """You are a friendly Python teacher for beginners.
Always reply in Hinglish (Hindi written in English letters).
Keep every answer under 3 sentences and give one tiny example."""

# Step 4: NEW - the list starts WITH the system message (it always stays at the top)
messages = [
    {"role": "system", "content": system_prompt},
]

print("Chat started! Type 'exit' to stop.\n")

while True:
    user_prompt = input("You: ")

    if user_prompt.lower() == "exit":
        print("Bye!")
        break

    # Same memory logic as step 4
    messages.append({"role": "user", "content": user_prompt})

    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    reply = response.choices[0].message.content

    messages.append({"role": "assistant", "content": reply})

    print("AI:", reply, "\n")
