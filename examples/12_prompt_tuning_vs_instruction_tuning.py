import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Prompt for explanation
prompt = """
Explain the difference between:
1. Prompt Engineering
2. Prompt Tuning
3. Instruction Tuning

Keep it simple and beginner-friendly.
"""

# Get response
response = get_completion(prompt)

# Print model explanation
print("MODEL EXPLANATION:")
print("-" * 50)
print(response)

# Add your own note
print("\nMY UNDERSTANDING:")
print("-" * 50)
print("""
Prompt Engineering:
- Writing better prompts to guide AI (no training needed)

Prompt Tuning:
- Adjusting prompts using training techniques (uses model weights)

Instruction Tuning:
- Training the model on many instructions to improve behavior
""")