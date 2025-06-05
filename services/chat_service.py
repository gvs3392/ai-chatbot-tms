from openai import OpenAI
from services.salesforce_service import query_salesforce
import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def handle_user_query(user_input):
    try:
        prompt = f"""
        Extract the origin and destination cities from this shipping-related message.
        Return ONLY a valid JSON object with two keys: 'origin' and 'destination'.
        Do NOT include any explanation or additional text.
        Example: {{"origin": "Chicago", "destination": "Euclid"}}

        Message: '{user_input}'
        """

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a logistics assistant that extracts shipment route details."},
                {"role": "user", "content": prompt}
            ]
        )

        parsed_text = response.choices[0].message.content.strip()
        print("GPT response:", parsed_text)  # Debug log for Railway

        # Validate JSON
        try:
            cities = json.loads(parsed_text)
            origin = cities.get("origin", "").strip()
            destination = cities.get("destination", "").strip()
            if not origin or not destination:
                raise ValueError("Missing origin or destination in GPT response.")
        except Exception as parse_error:
            return {"error": f"Failed to parse OpenAI response as JSON: {parsed_text}"}

        result = query_salesforce(origin, destination)
        return {"response": result}

    except Exception as e:
        return {"error": str(e)}
