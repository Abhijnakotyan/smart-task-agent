from tools import add,multiply,get_date
from agent import register_tools,run_action

tools={
    "add":add,
    "multiply":multiply,
    "get_date":get_date
}

register_tools(tools)

while True:
    user=input("You: ")

    if "add" in user:
        result = run_action("add", {"a": 5, "b": 10})
    elif "multiply" in user:
        result = run_action("multiply", {"a": 5, "b": 10})
    elif "date" in user:
        result = run_action("get_date", {})
    else:
        result = "I don't understand yet."

    print("Agent:", result)