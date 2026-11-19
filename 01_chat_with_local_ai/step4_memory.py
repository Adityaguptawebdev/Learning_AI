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

# Step 3: NEW - one list that keeps the whole conversation
messages = []

print("Chat started! Type 'exit' to stop.\n")

while True:
    user_prompt = input("You: ")

    if user_prompt.lower() == "exit":
        print("Bye!")
        break

    # Step 4: NEW - save your message in the list
    messages.append({"role": "user", "content": user_prompt})

    # Step 5: Send the WHOLE list (not just the latest message)
    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    reply = response.choices[0].message.content

    # Step 6: NEW - save the AI's reply in the list too
    messages.append({"role": "assistant", "content": reply})

    print("AI:", reply, "\n")
