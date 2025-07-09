from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

API_KEY = "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"  # replace this
API_URL = "https://api.groq.com/openai/v1/chat/completions"

@app.route("/ask", methods=["POST"])
def ask():
    prompt = request.json.get("prompt", "")

    res = requests.post(API_URL, json={
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 512
    }, headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    })

    return jsonify(res.json())

app.run(host="0.0.0.0", port=8080)
