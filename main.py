import json
import re
from agent import  ask_llm
from tools import add, multiply, get_date

llm_output = ask_llm(user)

try:
    json_str = re.search(r'\{.*\}', llm_output, re.DOTALL).group()
    parsed = json.loads(json_str)

    action = parsed["action"]
    inputs = parsed["action_input"]

    result = run_action(action, inputs)

except Exception as e:
    result = f"Error parsing LLM output: {llm_output}"

print("Agent:", result)