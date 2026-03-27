import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Chain-of-Thought prompt
prompt = """
Who would win in a fight: Naruto or Sasuke?

Think step by step:
1. Compare their abilities
2. Compare their strengths and weaknesses
3. Consider different battle scenarios
4. Then give the final answer
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