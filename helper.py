# Import required libraries
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create client using API key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Function to send prompt to Gemini
def get_completion(prompt, model="gemini-2.5-flash"):
    
    # Send request to model
    response = client.models.generate_content(
        model=model,
        contents=prompt
    )
    
    # Return only text output
    return response.text