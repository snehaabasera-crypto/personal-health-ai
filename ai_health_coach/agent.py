import google.generativeai as genai
from config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

model = genai.GenerativeModel("models/gemini-2.5-flash")
def health_coach_agent(profile):

    prompt = f"""
    You are a professional AI Health Coach.

    User Profile:
    Age: {profile['age']}
    Gender: {profile['gender']}
    Sleep Hours: {profile['sleep_hours']}
    Steps: {profile['steps']}
    Stress Level: {profile['stress_level']}
    Uneasiness: {profile['uneasiness']}
    Goal: {profile['health_goal']}

    Provide:
    1. Health Summary
    2. Action Plan
    3. Diet Suggestions
    4. Workout Suggestions
    5. Motivation
    """

    response = model.generate_content(prompt)

    return response.text