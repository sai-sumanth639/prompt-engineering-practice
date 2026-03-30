import sys
import os
import json

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Anime-themed prompt with JSON output requirement
prompt = """
You are an anime mission classification assistant.

TASK:
Analyze the situation and return a JSON response.

JSON RULES:
1. Output must be valid JSON only
2. Do NOT include any extra text
3. Do NOT wrap the response in markdown or code blocks
4. Use exactly the keys provided
5. Allowed values:
   - risk_level: low, medium, high

REQUIRED JSON FORMAT:
{
  "mission_type": "",
  "risk_level": "",
  "next_action": ""
}

-------------------------

MISSION DETAILS:
A warrior is sent to explore a dark cave with unknown creatures.
The situation is unpredictable and potentially dangerous.
"""

# Get response
response = get_completion(prompt)

# Print prompt
print("PROMPT:")
print("-" * 50)
print(prompt)

# Print raw response
print("\nRAW MODEL RESPONSE:")
print("-" * 50)
print(response)


# 🛠️ Clean response (handle markdown issue)
cleaned_response = response.strip()

if cleaned_response.startswith("```"):
    cleaned_response = cleaned_response.replace("```json", "").replace("```", "").strip()


# 🧪 Parse JSON
print("\nPARSED JSON:")
print("-" * 50)

try:
    parsed = json.loads(cleaned_response)
    print(parsed)
    print("\nSTATUS: JSON is valid ✅")
except Exception as e:
    print("JSON parsing failed ❌")
    print("Error:", e)