# Step 1: Import the OpenAI client (Ollama speaks the same API format)
from openai import OpenAI

# Step 2: Point the client at your local Ollama server
client = OpenAI(
    base_url="http://127.0.0.1:11434/v1",
    api_key="dummy_key",  # Ollama ignores this, but the library requires a value
)

# Step 3: Send a prompt to the model
response = client.chat.completions.create(
    model="llama3.2:3b",
    messages=[
        {"role": "user", "content": "Explain what AI is in one sentence."},
    ],
)

# Step 4: Print the model's reply
print(response.choices[0].message.content)
