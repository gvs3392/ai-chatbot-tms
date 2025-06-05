from openai import OpenAI
from services.salesforce_service import query_salesforce
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def handle_user_query(user_input):
    try:
        prompt = f"Extract the intent, origin, destination, and equipment from: '{user_input}'"
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a transportation assistant for a TMS."},
                {"role": "user", "content": prompt}
            ]
        )
        parsed = response.choices[0].message.content
        result = query_salesforce(parsed)
        return {"response": result}
    except Exception as e:
        return {"error": str(e)}
