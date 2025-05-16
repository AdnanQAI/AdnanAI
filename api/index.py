import os
import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# استخدام مفتاح OpenAI من متغير البيئة
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        answer = response["choices"][0]["message"]["content"]
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
