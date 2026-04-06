import subprocess

def ask_llm(user_input):
    prompt = f"""
You are an AI agent.

You MUST respond ONLY in JSON format.
DO NOT talk.
DO NOT explain.

Format:
{{
  "action": "add | multiply | get_date",
  "action_input": {{
    "a": number,
    "b": number
  }}
}}

Rules:
- If user asks for addition → use "add"
- If multiplication → use "multiply"
- If date → use "get_date" and empty input {{}}
- Extract numbers from user input
- Return ONLY JSON (no text before/after)

User query: {user_input}
"""

    result = subprocess.run(
        ["ollama", "run", "phi3"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()