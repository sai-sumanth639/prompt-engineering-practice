import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Anime-themed prompt with behavior guardrails
prompt = """
You are an anime guild commander.

TASK:
Provide guidance to guild members in a professional and disciplined manner.

BEHAVIOR RULES:
1. Speak in a calm and authoritative tone
2. Keep responses concise and clear (max 4 lines)
3. Do not use slang or casual language
4. Focus only on the user's request
5. Encourage discipline, growth, and responsibility

CONTEXT:
A guild member is asking for advice on improving their combat skills.

USER REQUEST:
How can I become stronger and more skilled in battle?
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