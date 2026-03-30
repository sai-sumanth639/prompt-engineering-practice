import sys
import os
import re

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion


# 🛡️ Application-Level Guardrail (clean input)
def clean_input(text):
    """
    Remove sensitive details like phone numbers
    """
    # Remove phone numbers (simple pattern)
    text = re.sub(r'\b\d{10}\b', '[REDACTED]', text)
    return text


# 🔹 Raw Input (contains sensitive info)
raw_input_text = """
Hero Name: Asta
Phone: 9876543210
Issue: Injured during battle and needs help
"""


# 🔹 Apply guardrail
processed_input = clean_input(raw_input_text)


# 🔹 Build prompt using cleaned input
prompt = f"""
You are an anime support assistant.

TASK:
Summarize the issue without exposing sensitive details.

INPUT:
{processed_input}
"""


# Get response
response = get_completion(prompt)


# 🖨️ Print before and after
print("RAW INPUT:")
print("-" * 50)
print(raw_input_text)

print("\nPROCESSED INPUT:")
print("-" * 50)
print(processed_input)

print("\nPROMPT:")
print("-" * 50)
print(prompt)

print("\nMODEL RESPONSE:")
print("-" * 50)
print(response)