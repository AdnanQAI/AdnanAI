import os
import openai

def handler(request):
    openai.api_key = os.environ["OPENAI_API_KEY"]
    
    data = request.json()
    user_input = data.get("question", "")

    if not user_input:
        return {
            "statusCode": 400,
            "body": "No question provided"
        }

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        answer = response["choices"][0]["message"]["content"]
        return {
            "statusCode": 200,
            "body": answer
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
