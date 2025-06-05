from openai import OpenAI
from services.salesforce_service import query_salesforce
import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def handle_user_query(user_input):
    try:
        prompt = f"""
        Extract the origin and destination cities from this shipping-related message.
        Return your answer as a JSON object with keys: origin and destination.
        Example: {{ "origin": "Chicago", "destination": "Euclid" }}
        Message: '{user_input}'
        """
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a logistics assistant that extracts shipment route details."},
                {"role": "user", "content": prompt}
            ]
        )
        parsed_text = response.choices[0].message.content
        cities = json.loads(parsed_text)

        result = query_salesforce(cities["origin"], cities["destination"])
        return {"response": result}
    except Exception as e:
        return {"error": str(e)}
