import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Anime-themed prompt with behavior control
prompt = """
You are an anime executive briefing assistant.

TASK:
Provide a high-level mission update to the guild leader.

BEHAVIOR RULES:
1. Use a formal and professional tone
2. Keep the response concise (max 4 lines)
3. Focus on key outcomes and risks only
4. Avoid storytelling or unnecessary details
5. Use clear and structured sentences

-------------------------

MISSION DETAILS:
A team was sent to defeat a group of rogue warriors.
The mission was successful, but two members were injured.
The area is now secure, but future threats are possible.

USER REQUEST:
Provide a mission update.
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