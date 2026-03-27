import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Role-based prompt (simulated)
prompt = """
System: You are an anime expert who explains things clearly and concisely.

User: Explain who Sasuke Uchiha is.

Assistant:
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