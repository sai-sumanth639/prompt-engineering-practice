import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Zero-shot CoT prompt
prompt = """
Compare Goku and Saitama.

Think step by step and decide who is stronger.
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