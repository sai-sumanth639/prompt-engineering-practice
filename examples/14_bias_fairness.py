import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Anime-themed prompt with fairness guardrails
prompt = """
You are an anime guild selection assistant.

TASK:
Evaluate candidates for a special mission based only on relevant skills and experience.

FAIRNESS RULES:
1. Do NOT consider name, background, or identity
2. Focus only on skills, experience, and mission readiness
3. Avoid assumptions unrelated to performance
4. Provide a fair and objective evaluation

-------------------------

CANDIDATE A:
Name: Hiro
Background: From a small village
Skills: Excellent swordsmanship, strong combat experience

CANDIDATE B:
Name: Kazuki
Background: From a royal family
Skills: Moderate combat skills, limited experience

USER QUESTION:
Who is better suited for the mission and why?
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