import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# One-shot prompt
prompt = """
Convert informal anime sentences into professional descriptions.

Example:
Input: Naruto is super strong and never gives up.
Output: Naruto Uzumaki is a determined ninja known for his resilience and strength.

Now do this:

Input: Luffy wants to be the king of pirates and loves adventure.
Output:
"""

response = get_completion(prompt)

print("PROMPT:")
print("-" * 50)
print(prompt)

print("\nRESPONSE:")
print("-" * 50)
print(response)