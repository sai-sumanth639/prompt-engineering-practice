import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# -----------------------------
# Prompt Version 1 (basic)
# -----------------------------
prompt_v1 = """
Explain Itachi Uchiha.
"""

# -----------------------------
# Prompt Version 2 (improved)
# -----------------------------
prompt_v2 = """
Role:
You are an anime expert.

Task:
Explain Itachi Uchiha.

Constraints:
- Use bullet points
- Keep it concise
- Maximum 3 points

Output Format:
- Point 1
- Point 2
- Point 3
"""

# Get responses
response_v1 = get_completion(prompt_v1)
response_v2 = get_completion(prompt_v2)

# Print V1
print("PROMPT V1:")
print("-" * 50)
print(prompt_v1)

print("\nRESPONSE V1:")
print("-" * 50)
print(response_v1)

# Print V2
print("\n\nPROMPT V2:")
print("-" * 50)
print(prompt_v2)

print("\nRESPONSE V2:")
print("-" * 50)
print(response_v2)