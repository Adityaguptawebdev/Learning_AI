# Step 1: Import libraries
import os
from dotenv import load_dotenv
from openai import OpenAI

# Step 2: NEW - load settings from the .env file
load_dotenv()

# Step 3: Connect to Ollama using values from .env
client = OpenAI(
    base_url=os.getenv("OLLAMA_BASE_URL"),
    api_key=os.getenv("OLLAMA_API_KEY"),
)
model = os.getenv("MODEL_NAME")

print("Chat started! Type 'exit' to stop.\n")

# Step 4: NEW - loop forever until the user types 'exit'
while True:
    user_prompt = input("You: ")

    if user_prompt.lower() == "exit":
        print("Bye!")
        break

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": user_prompt},
        ],
    )

    print("AI:", response.choices[0].message.content, "\n")
