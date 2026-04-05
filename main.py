import json
from tools import add, multiply, get_date
from agent import register_tools, run_action, ask_llm

tools = {
    "add": add,
    "multiply": multiply,
    "get_date": get_date
}

register_tools(tools)

while True:
    user = input("You: ")

    llm_output = ask_llm(user)

    try:
        parsed = json.loads(llm_output)
        action = parsed["action"]
        inputs = parsed["action_input"]

        result = run_action(action, inputs)

    except Exception as e:
        result = "Error understanding response"

    print("Agent:", result)