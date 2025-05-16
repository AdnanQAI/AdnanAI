from http.server import BaseHTTPRequestHandler
import json
import openai
import os

openai.api_key = os.environ["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"]

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            body = json.loads(post_data)

            question = body.get("question", "").strip()

            if not question:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'{"error": "No question provided."}')
                return

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question}
                ]
            )

            answer = response.choices[0].message.content.strip()

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"answer": answer}).encode())

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
