import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Anime-themed prompt with fallback guardrails
prompt = """
You are an anime council advisor.

TASK:
Provide guidance based on the given situation.

FALLBACK RULES:
1. If important details are missing, ask for more information
2. Do NOT guess or assume missing facts
3. If the situation is unclear, suggest a safe next step
4. If the issue seems serious or risky, recommend consulting a higher authority

-------------------------

SITUATION:
A warrior reports feeling unwell after a battle but does not describe symptoms.

USER QUESTION:
What should the warrior do next?
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