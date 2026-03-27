import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from helper import get_completion

# Input text (same for all patterns)
text = """
Naruto Uzumaki is a ninja from the Hidden Leaf Village. 
He dreams of becoming Hokage and is known for his determination and strong will.
"""

# -----------------------------
# 1. Classification
# -----------------------------
prompt_classification = f"""
Classify the genre of this anime character description:

{text}
"""

# -----------------------------
# 2. Extraction
# -----------------------------
prompt_extraction = f"""
Extract the following details from the text:
- Character Name
- Goal

Text:
{text}
"""

# -----------------------------
# 3. Transformation
# -----------------------------
prompt_transformation = f"""
Rewrite the following text in a very simple way for a 10-year-old:

{text}
"""

# -----------------------------
# 4. Generation
# -----------------------------
prompt_generation = f"""
Create a short anime story based on this character:

{text}
"""

# Get responses
response_classification = get_completion(prompt_classification)
response_extraction = get_completion(prompt_extraction)
response_transformation = get_completion(prompt_transformation)
response_generation = get_completion(prompt_generation)

# Print outputs
print("CLASSIFICATION:")
print("-" * 50)
print(response_classification)

print("\nEXTRACTION:")
print("-" * 50)
print(response_extraction)

print("\nTRANSFORMATION:")
print("-" * 50)
print(response_transformation)

print("\nGENERATION:")
print("-" * 50)
print(response_generation)