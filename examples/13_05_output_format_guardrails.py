import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Anime-themed prompt with output-format guardrails
prompt = """
You are an anime mission report assistant.

TASK:
Analyze the mission details and return a structured mission report.

OUTPUT FORMAT RULES:
1. Follow the exact section headings given below
2. Do NOT change section names
3. Do NOT add extra sections
4. Keep each section short (1-2 lines)

REQUIRED FORMAT:

Mission Type:
Risk Level:
Key Strength:
Main Concern:
Recommended Action:

-------------------------

MISSION DETAILS:
A young warrior is assigned to defeat a forest beast.
The warrior has strong attack power but lacks defensive skills.
The beast is fast and unpredictable.

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