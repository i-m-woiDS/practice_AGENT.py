import os
from google import genai
from google.genai import types

# Initialize the Gemini Client 
# here It reads the GEMINI_API_KEY from your environment variables automatically
client = genai.Client()

def ai_agent_brain(raw_application_text):
    """
    This is the core 'Agent Brain'. 
    It reasons over messy data using the correct SDK syntax.
    """
    
    prompt = f"""
    You are an AI admin agent for an advocacy group. 
    Analyze the following volunteer message. Extract their Name, Primary Skill, and Language.
    
    Volunteer Message: "{raw_application_text}"
    
    Return the output EXACTLY in this format, with no extra text:
    NAME: [Name] | SKILL: [Skill] | LANGUAGE: [Languages spoken]
    """
    
    
    response = client.models.generate_content(
        model='gemini-3.6-flash',
        contents=prompt
    )
    return response.text.strip()

# --- SIMULATED INCOMING DATA ---
messy_inputs = [
    "Hey! I am Sarah. I want to help with translating graphics from English to Arabic. I have a lot of free time.",
    "Salam, my name is Ahmed Malik. I do professional video editing and graphic design. I speak English and Urdu.",
    "Hi team, I am John. I can help organize events or do web development if needed. Mostly speak English."
]

print("Starting AI Agent Sorting Loop...\n")

for item in messy_inputs:
    print(f"Processing raw input...")
    structured_data = ai_agent_brain(item)
    
    print(f"Agent Output: {structured_data}")
    print("-" * 50)
