# Step 1: Import the OpenAI client
from openai import OpenAI

# Step 2: Connect to local Ollama
client = OpenAI(
    base_url="http://127.0.0.1:11434/v1",
    api_key="dummy_key",
)

# Step 3: NEW - ask the user to type a prompt in the terminal
user_prompt = input("You: ")

# Step 4: Send that prompt to the model
response = client.chat.completions.create(
    model="llama3.2:3b",
    messages=[
        {"role": "user", "content": user_prompt},
    ],
)

# Step 5: Print the reply
print("AI:", response.choices[0].message.content)
