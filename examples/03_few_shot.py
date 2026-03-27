import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Few-shot prompt (multiple examples)
prompt = """
Classify the anime into its main genre.

Example:
Naruto → Action
Your Name → Romance
Death Note → Thriller

Now classify this:

Demon Slayer →
"""

# Send prompt
response = get_completion(prompt)

# Print prompt
print("PROMPT:")
print("-" * 50)
print(prompt)

# Print response
print("\nRESPONSE:")
print("-" * 50)
print(response)