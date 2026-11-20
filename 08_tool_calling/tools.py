# tools.py - ALL our tools live in this one file.
#
# Every tool has 2 parts:
#   1. Python function -> does the real work (WE run it, not the LLM)
#   2. Schema          -> a description of the function for the LLM (the LLM only reads this)
#
# The step files import from here, so they only show HOW tool calling works.

from datetime import datetime


# ---------- Tool 1: current time ----------

def get_current_time():
    return datetime.now().strftime("%I:%M %p, %d %B %Y")


time_tool_schema = {
    "type": "function",
    "function": {
        "name": "get_current_time",
        "description": "Get the current local time and date. Use ONLY when the user asks about the current time, date or day.",
        "parameters": {"type": "object", "properties": {}},  # this tool needs no inputs
    },
}


# ---------- Tool 2: calculator ----------

def calculate(a, b, operation):
    a = float(a)
    b = float(b)
    if operation == "add":
        return str(a + b)
    if operation == "subtract":
        return str(a - b)
    if operation == "multiply":
        return str(a * b)
    if operation == "divide":
        return str(a / b)
    return "Unknown operation"


calculator_tool_schema = {
    "type": "function",
    "function": {
        "name": "calculate",
        "description": "Do exact math on two numbers.",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "First number"},
                "b": {"type": "number", "description": "Second number"},
                "operation": {
                    "type": "string",
                    "enum": ["add", "subtract", "multiply", "divide"],  # only these values allowed
                },
            },
            "required": ["a", "b", "operation"],
        },
    },
}


# ---------- Run a tool by its name ----------
# The LLM only gives us the tool's NAME + inputs. This picks the matching Python function.

def run_tool(name, args):
    if name == "get_current_time":
        return get_current_time()
    if name == "calculate":
        return calculate(args["a"], args["b"], args["operation"])
    return "Unknown tool"
