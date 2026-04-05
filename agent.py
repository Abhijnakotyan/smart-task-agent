tools={}

def register_tools(tool_dict):
    global tools
    tools=tool_dict

def run_action(action,inputs):
    if action in tools:
        return tools[action](**inputs)
    return "Invalid action"

    