# Step 1: Import libraries
import os
from dotenv import load_dotenv
from openai import OpenAI

# NEW - our tool comes from tools.py (function + its schema)
from tools import get_current_time, time_tool_schema

# Step 2: Connect to Ollama (same as chapter 01)
load_dotenv()
client = OpenAI(
    base_url=os.getenv("OLLAMA_BASE_URL"),
    api_key=os.getenv("OLLAMA_API_KEY"),
)
model = os.getenv("MODEL_NAME")

# Step 3: The list of tools the LLM is allowed to use
tools = [time_tool_schema]

user_prompt = input("You: ")
messages = [{"role": "user", "content": user_prompt}]

# Step 4: FIRST call - send the question + the list of tools. The LLM decides.
response = client.chat.completions.create(model=model, messages=messages, tools=tools)
ai_message = response.choices[0].message

# Step 5: Did the LLM ask us to run a tool?
if ai_message.tool_calls:
    tool_call = ai_message.tool_calls[0]
    print("🧠 LLM says: please run", tool_call.function.name + "()")

    # Step 6: WE run the function (the LLM can't run code itself)
    result = get_current_time()
    print("🐍 Python ran it. Result:", result)

    # Step 7: Put the LLM's request and the tool's result into memory
    messages.append(ai_message)
    messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": result})

    # Step 8: SECOND call - the LLM reads the result and writes the final answer
    final = client.chat.completions.create(model=model, messages=messages, tools=tools)
    print("🤖 AI:", final.choices[0].message.content)
else:
    # The LLM decided no tool was needed
    print("🤖 AI:", ai_message.content)
