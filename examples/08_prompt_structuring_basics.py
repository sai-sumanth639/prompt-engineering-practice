import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Structured prompt
prompt = """
Role:
You are an anime expert.

Task:
Explain the character Naruto Uzumaki.

Context:
Naruto is the main character of the Naruto series.

Constraints:
- Keep the explanation simple
- Use bullet points
- Maximum 3 points

Output Format:
- Point 1
- Point 2
- Point 3
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