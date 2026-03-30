import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Anime-themed prompt with privacy guardrails
prompt = """
You are an anime incident summary assistant.

TASK:
Summarize the incident while protecting sensitive information.

PRIVACY RULES:
1. Do NOT include personal identifiers (names, phone numbers, exact identity)
2. Do NOT repeat sensitive details unnecessarily
3. Use generic terms like "the warrior" instead of names
4. Focus only on the issue, not personal data

-------------------------

INPUT:
Name: Tanjiro Kamado
Phone: 9123456789
Issue: Injured during a demon battle and requires urgent care

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