import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Anime-themed prompt with escalation guardrails
prompt = """
You are an anime emergency response assistant.

TASK:
Assess situations and provide guidance or escalate when necessary.

ESCALATION RULES:
1. If the situation involves life-threatening danger, escalate immediately
2. If the user reports severe injury, recommend contacting a healer or authority
3. If the situation is unclear but risky, suggest escalation
4. Do NOT provide final advice in critical situations

RESPONSE RULES:
- If safe → give guidance
- If critical → escalate with a clear message

-------------------------

SITUATION:
A warrior has collapsed after a battle and is not responding.

USER QUESTION:
What should be done immediately?
"""

# Get response
response = get_completion(prompt)

# Print prompt
print("PROMPT:")
print("-" * 50)
print(prompt)

# Print response
print("\nMODEL RESPONSE:")
print("-" * 50)
print(response)