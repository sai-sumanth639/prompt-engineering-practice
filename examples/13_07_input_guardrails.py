import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion


# 🛡️ Input Guardrail Function
def validate_input(character_name, issue, severity):
    """
    Validate required fields before calling AI
    """

    # Check required fields
    if not character_name:
        return False, "Character name is missing."
    
    if not issue:
        return False, "Issue description is missing."

    if severity not in ["low", "medium", "high"]:
        return False, "Severity must be: low, medium, or high."

    return True, "Input is valid."


# 🔹 Test Case 1 (INVALID INPUT)
print("TEST CASE 1: INVALID INPUT")
print("-" * 50)

character_name = "Naruto"
issue = ""
severity = "high"

is_valid, message = validate_input(character_name, issue, severity)

print("Validation Result:", message)

if is_valid:
    prompt = f"""
    You are an anime incident assistant.

    Character: {character_name}
    Issue: {issue}
    Severity: {severity}

    Provide guidance.
    """

    response = get_completion(prompt)
    print(response)
else:
    print("Model not called due to invalid input.")


# 🔹 Test Case 2 (VALID INPUT)
print("\nTEST CASE 2: VALID INPUT")
print("-" * 50)

character_name = "Sasuke"
issue = "Injured during battle"
severity = "medium"

is_valid, message = validate_input(character_name, issue, severity)

print("Validation Result:", message)

if is_valid:
    prompt = f"""
    You are an anime incident assistant.

    Character: {character_name}
    Issue: {issue}
    Severity: {severity}

    Provide safe guidance.
    """

    print("\nPROMPT:")
    print("-" * 50)
    print(prompt)

    response = get_completion(prompt)

    print("\nMODEL RESPONSE:")
    print("-" * 50)
    print(response)
else:
    print("Model not called due to invalid input.")