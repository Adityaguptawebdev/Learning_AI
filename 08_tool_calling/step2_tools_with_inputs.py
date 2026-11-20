# Step 1: Import libraries
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Our tools come from tools.py: 2 schemas + run_tool() to run any tool by its name
from tools import time_tool_schema, calculator_tool_schema, run_tool

# Step 2: Connect to Ollama (same as before)
load_dotenv()
client = OpenAI(
    base_url=os.getenv("OLLAMA_BASE_URL"),
    api_key=os.getenv("OLLAMA_API_KEY"),
)
model = os.getenv("MODEL_NAME")

# Step 3: NEW - give the LLM BOTH tools. It picks the right one.
tools = [time_tool_schema, calculator_tool_schema]

user_prompt = input("You: ")
messages = [{"role": "user", "content": user_prompt}]

# Step 4: FIRST call - LLM decides which tool, and fills in the inputs
response = client.chat.completions.create(model=model, messages=messages, tools=tools)
ai_message = response.choices[0].message

if ai_message.tool_calls:
    messages.append(ai_message)

    # Step 5: NEW - the LLM can ask for more than one tool, so loop over them
    for tool_call in ai_message.tool_calls:
        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)  # NEW - text '{"a": 2}' -> dictionary {"a": 2}
        print("🧠 LLM says: run", name, "with inputs", args)

        # Step 6: Run the matching Python function (see run_tool in tools.py)
        result = run_tool(name, args)
        print("🐍 Python ran it. Result:", result)

        messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": result})

    # Step 7: SECOND call - LLM writes the final answer using the results
    final = client.chat.completions.create(model=model, messages=messages, tools=tools)
    print("🤖 AI:", final.choices[0].message.content)
else:
    print("🤖 AI:", ai_message.content)
