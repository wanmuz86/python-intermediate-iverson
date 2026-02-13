import os
import json
from dataclasses import dataclass, asdict
from datetime import date
from dotenv import load_dotenv
from openai import OpenAI

#Open .env file (to retrieve the API KEY)
load_dotenv()

#Connect to OpenAI based on the key given in .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Request models Class [ normally create in models.vacation_request ]
# name, how many day, budget, luxury,CNY, constraint: In Malaysia
@dataclass
class VacationRequest:
    name: str
    days: int
    budget: int
    style: str
    destination_type: str
    constraints: str

# Method/ function to create the prompt to be sent to OPEN AI (Identify the RCCT)
def build_prompt(req: VacationRequest) -> str:
    return f"""
You are a professional travel planner.

Create a {req.days}-day vacation plan.

Traveler: {req.name}
Budget: {req.budget}
Travel style: {req.style}
Destination type: {req.destination_type}
Constraints: {req.constraints}

Output format:
1) Summary (3 bullets)
2) Day-by-day itinerary
3) Budget breakdown
4) Packing list
5) Safety tips
"""

# Call the OPEN AI API
# connntecting to API/ DB - Service  service.planner.py
def call_openai(prompt: str) -> str:
    try:
        # OpenAI client (with the given API Key)
        # You can replace this part with page 10 of the use case lab
        # If you are connection to your own InfineonOpenAI Sertver
        response = client.chat.completions.create(
            model="gpt-4o-mini", # model selected gpt-4o-mini
            # data that is sent to the API
            messages=[
                # Role
                {"role": "system", "content": "You are a structured travel planner."},
                # Message / Prompt
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        #Response from Open AI
        return response.choices[0].message.content

    except Exception as e:
        return f"[ERROR] OpenAI API call failed: {e}"
    
        #     # OpenAI client (with the given API key)
        # # You can replace this part with page 10 of the use case lab.
        # # If you are connecting to your own Infineon OpenAI server:
        # # url = "https://infineon.com.my"

        # data = {
        #     "model": "gpt-4o-mini",  # Selected model
        #     # Data sent to the API
        #     "messages": [
        #         # System role
        #         {"role": "system", "content": "You are a structured travel planner."},
        #         # User message / prompt
        #         {"role": "user", "content": prompt}
        #     ],
        #     "temperature": 0.7,
        # }

        # # response = requests.post(url, json=data)
        # # response.raise_for_status()

# Method that is going to be called to create the itinerary by FASTAPI or StreamLit
def make_plan(req: VacationRequest) -> dict:
    prompt = build_prompt(req) # create the prompt
    plan_text = call_openai(prompt) # get the result from OpenAPI

    #Return the result to StreamLit   
    return {
        "generated_on": str(date.today()),
        "request": asdict(req),
        "plan_text": plan_text,
    }
# Write the response from OPEN AI
def save_reports(plan: dict, base_name="vacation_report"):
    # in .txt file
    with open(f"{base_name}.txt", "w", encoding="utf-8") as f:
        f.write(plan["plan_text"])

    #in json file
    with open(f"{base_name}.json", "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=2)

    print("✅ Reports saved.")
