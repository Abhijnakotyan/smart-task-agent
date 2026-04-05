import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

tools={}

def register_tools(tool_dict):
    global tools
    tools=tool_dict


def ask_llm(user_input):
    prompt = f"""
You are an AI agent.

You must respond ONLY in JSON:
{{
  "action": "tool_name",
  "action_input": {{ }}
}}

Available tools:
- add(a, b)
- multiply(a, b)
- get_date()

User query: {user_input}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def run_action(action, inputs):
    if action in tools:
        return tools[action](**inputs)
    return "Invalid action"