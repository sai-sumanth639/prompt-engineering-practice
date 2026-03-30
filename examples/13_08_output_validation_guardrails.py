import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion


# 🛡️ Output Validation Function
def validate_output(response):
    """
    Check if required sections exist in response
    """
    required_sections = ["Mission Type:", "Risk Level:", "Recommended Action:"]

    for section in required_sections:
        if section not in response:
            return False, f"Missing section: {section}"

    return True, "Output format is valid."


# 🎌 Prompt with required structure
prompt = """
You are an anime mission report assistant.

TASK:
Generate a structured mission report.

REQUIRED FORMAT:

Mission Type:
Risk Level:
Recommended Action:

-------------------------

MISSION DETAILS:
A warrior is sent to investigate a mysterious cave.
The cave may contain hidden dangers and unknown enemies.
"""

# Get response
response = get_completion(prompt)

# Print prompt
print("PROMPT:")
print("-" * 50)
print(prompt)

# Print response
print("\nMODEL RESPONSE:")
print("-" * 50)
print(response)


# 🧪 Validate output
print("\nVALIDATION RESULT:")
print("-" * 50)

is_valid, message = validate_output(response)

if is_valid:
    print("PASS ✅:", message)
else:
    print("FAIL ❌:", message)