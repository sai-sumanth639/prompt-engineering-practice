import sys
import os
import json  # for parsing JSON

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# JSON prompt
prompt = """
Provide information about the anime Naruto.

Return ONLY valid JSON.
Do NOT include markdown, backticks, or explanations.

Format:
{
  "title": "",
  "genre": "",
  "main_character": ""
}
"""

# Get response
response = get_completion(prompt)

# Print raw response
print("RAW RESPONSE:")
print("-" * 50)
print(response)

# Try parsing JSON
try:
    data = json.loads(response)

    print("\nPARSED OUTPUT:")
    print("-" * 50)
    print("Title:", data["title"])
    print("Genre:", data["genre"])
    print("Main Character:", data["main_character"])

except json.JSONDecodeError:
    print("\n❌ Failed to parse JSON. Model output was not valid JSON.")