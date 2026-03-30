import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Anime-themed prompt with combined guardrails
prompt = """
You are an anime incident management assistant.

TASK:
Analyze the situation and provide a structured response.

-------------------------
SCOPE GUARDRAILS:
- Only handle anime-related incidents
- Do NOT answer real-world unrelated queries

-------------------------
SAFETY GUARDRAILS:
- Do NOT provide harmful or dangerous instructions
- Refuse unsafe requests clearly

-------------------------
BEHAVIOR GUARDRAILS:
- Use a calm and professional tone
- Keep answers concise (max 4 lines)

-------------------------
ESCALATION RULES:
- If situation is critical, recommend immediate escalation
- Do NOT give final advice in life-threatening cases

-------------------------
OUTPUT FORMAT (STRICT):

Incident Type:
Risk Level:
Recommended Action:

-------------------------

SITUATION:
A warrior is severely injured after a battle and is losing consciousness.

USER QUESTION:
What should be done?
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