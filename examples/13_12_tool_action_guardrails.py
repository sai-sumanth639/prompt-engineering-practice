import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Anime-themed prompt with tool/action guardrails
prompt = """
You are an anime system support assistant.

TASK:
Help users with account and access-related issues.

TOOL / ACTION GUARDRAILS:
1. You may recommend actions (like resetting access, contacting support)
2. You must NOT claim that you have already performed any action
3. Do NOT say you fixed, unlocked, or changed anything directly
4. If action is needed, guide the user with clear next steps

-------------------------

USER REQUEST:
I am unable to access my guild account. Can you fix it?
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