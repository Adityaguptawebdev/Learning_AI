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

# Step 3: System prompt + memory (same as step 5)
system_prompt = """You are a friendly Python teacher for beginners.
Always reply in Hinglish (Hindi written in English letters).
Keep every answer under 3 sentences and give one tiny example."""

messages = [
    {"role": "system", "content": system_prompt},
]

print("Chat started! Type 'exit' to stop.\n")

while True:
    user_prompt = input("You: ")

    if user_prompt.lower() == "exit":
        print("Bye!")
        break

    messages.append({"role": "user", "content": user_prompt})

    # Step 4: NEW - stream=True means "send me the reply piece by piece"
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

    # Step 5: NEW - print each piece as soon as it arrives, and also join them all
    print("AI: ", end="")
    reply = ""
    for chunk in stream:
        piece = chunk.choices[0].delta.content   # a small piece of text (or None)
        if piece:
            print(piece, end="", flush=True)     # print on the same line, show it right away
            reply = reply + piece                # keep building the full reply
    print("\n")

    # Step 6: Save the FULL reply in memory (same as step 4)
    messages.append({"role": "assistant", "content": reply})
