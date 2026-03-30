import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Anime-themed prompt with safe workflow
prompt = """
You are an anime emergency routing assistant.

TASK:
Analyze the situation and provide a safe, structured response.

-------------------------
CONSTRAINTS:
1. Only handle anime-related emergency situations
2. Do NOT provide medical or dangerous instructions
3. Keep responses concise (max 4 lines)
4. Do NOT make assumptions if details are missing

-------------------------
FALLBACK RULES:
1. If information is missing, ask for clarification
2. If situation is unclear, suggest a safe next step
3. If situation is critical, recommend immediate escalation

-------------------------
OUTPUT FORMAT (STRICT):

Situation Summary:
Risk Level:
Next Step:

-------------------------

SITUATION:
A warrior collapsed during a mission, but the cause is unknown.

USER QUESTION:
What should be done next?
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