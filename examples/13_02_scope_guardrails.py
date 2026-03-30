import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Anime-themed prompt with scope guardrails
prompt = """
You are an anime mission assistant.

TASK:
Answer only anime-related questions.

ALLOWED SCOPE:
- missions
- character abilities
- training
- power systems
- anime world rules

OUT OF SCOPE:
- programming
- finance
- politics
- medical advice
- real-world personal issues

RULES:
1. Answer only if the question is within scope
2. Do NOT answer out-of-scope questions
3. If out-of-scope, say:
   "This is beyond my anime world knowledge. Ask something related to anime."

-------------------------

USER QUESTION 1:
How can I train like an anime warrior?

USER QUESTION 2:
How do I invest money?
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