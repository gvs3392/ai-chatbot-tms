import openai
from services.salesforce_service import query_salesforce
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

async def handle_user_query(user_input):
    prompt = f"Extract the intent, origin, destination, and equipment from: '{user_input}'"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a transportation assistant for a TMS."},
            {"role": "user", "content": prompt}
        ]
    )
    parsed = response['choices'][0]['message']['content']
    result = query_salesforce(parsed)
    return {"response": result}
