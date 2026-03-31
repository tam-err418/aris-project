import os
import json
import google.generativeai as genai

def handler(event, context):
    api_key = os.environ.get("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="Bạn là ARIS, AI lạnh lùng điều khiển Radar. Chỉ gợi ý, không cho đáp án. Trạm 1: REV-280. Trạm 2: VOLT-4.5."
    )

    if event['httpMethod'] == 'POST':
        try:
            body = json.loads(event['body'])
            user_msg = body.get("message", "")
            response = model.generate_content(user_msg)
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json; charset=utf-8"},
                "body": json.dumps({"reply": response.text}, ensure_ascii=False)
            }
        except Exception as e:
            return {"statusCode": 500, "body": str(e)}
    return {"statusCode": 405}

