# Step 1: Import libraries
import os
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# Step 2: Connect to Ollama (same as chapter 01)
load_dotenv()
client = OpenAI(
    base_url=os.getenv("OLLAMA_BASE_URL"),
    api_key=os.getenv("OLLAMA_API_KEY"),
)
model = os.getenv("MODEL_NAME")


# Step 3: NEW - a normal Python function (the actual "tool")
def get_current_time():
    return datetime.now().strftime("%I:%M %p, %d %B %Y")


# Step 4: NEW - describe the tool to the LLM (it reads this, not your code)
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current local time and date. Use ONLY when the user asks about the current time, date or day.",
            "parameters": {"type": "object", "properties": {}},  # this tool needs no inputs
        },
    }
]

user_prompt = input("You: ")
messages = [{"role": "user", "content": user_prompt}]

# Step 5: FIRST call - send the question + the list of tools. The LLM decides.
response = client.chat.completions.create(model=model, messages=messages, tools=tools)
ai_message = response.choices[0].message

# Step 6: Did the LLM ask us to run a tool?
if ai_message.tool_calls:
    tool_call = ai_message.tool_calls[0]
    print("🧠 LLM says: please run", tool_call.function.name + "()")

    # Step 7: WE run the function (the LLM can't run code itself)
    result = get_current_time()
    print("🐍 Python ran it. Result:", result)

    # Step 8: Put the LLM's request and the tool's result into memory
    messages.append(ai_message)
    messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": result})

    # Step 9: SECOND call - the LLM reads the result and writes the final answer
    final = client.chat.completions.create(model=model, messages=messages, tools=tools)
    print("🤖 AI:", final.choices[0].message.content)
else:
    # The LLM decided no tool was needed
    print("🤖 AI:", ai_message.content)
