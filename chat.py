import os
import json
import google.generativeai as genai

def handler(event, context):
    api_key = os.environ.get("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    
    # Kịch bản AI của bạn
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="Bạn là ARIS, AI lạnh lùng của hệ thống Radar. Chỉ gợi ý, không cho đáp án. Trạm 1: REV-280. Trạm 2: VOLT-4.5."
    )

    if event['httpMethod'] == 'POST':
        body = json.loads(event['body'])
        user_query = body.get("query", "")
        response = model.generate_content(user_query)
        return {
            "statusCode": 200,
            "body": json.dumps({"reply": response.text})
        }
    return {"statusCode": 405}
