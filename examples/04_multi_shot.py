import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Multi-shot prompt (many examples)
prompt = """
Classify the anime into one word genre.

Examples:
Naruto → Action
One Piece → Adventure
Your Name → Romance
Death Note → Thriller
Demon Slayer → Action
Jujutsu Kaisen → Action
Spy x Family → Comedy
Tokyo Revengers → Drama

Now classify:

Attack on Titan →
"""

# Send prompt
response = get_completion(prompt)

# Print prompt
print("PROMPT:")
print("-" * 50)
print(prompt)

print("\nRESPONSE:")
print("-" * 50)
print(response)