from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/api/ask", methods=["POST"])
def ask():
    user_question = request.json.get("user_question")
    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_question}
        ]
    )
    answer = response['choices'][0]['message']['content']
    return jsonify({"answer": answer})
