import os
import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
JSON_FILE = "prompts.json"

# Ensure the JSON file exists
if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "w") as f:
        json.dump([], f)

# Groq API call to LLaMA
def call_groq(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

# Save interaction to JSON
def save_to_json(entry):
    with open(JSON_FILE, "r+") as f:
        data = json.load(f)
        data.insert(0, entry)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

# Load history
def load_history(user_id):
    with open(JSON_FILE, "r") as f:
        data = json.load(f)
    return [d for d in data if d["user_id"] == user_id]

@app.route("/", methods=["GET", "POST"])
def index():
    casual_response = formal_response = ""
    history = []
    if request.method == "POST":
        user_id = request.form["user_id"]
        query = request.form["query"]
        if not query.strip():
            return redirect(url_for("index"))

        casual_prompt = f"Explain this in a fun, casual way: {query}"
        formal_prompt = f"Provide a formal, analytical explanation of: {query}"

        try:
            casual_response = call_groq(casual_prompt)
            formal_response = call_groq(formal_prompt)
        except Exception as e:
            casual_response = formal_response = f"Error: {str(e)}"

        entry = {
            "user_id": user_id,
            "query": query,
            "casual_response": casual_response,
            "formal_response": formal_response,
            "timestamp": datetime.utcnow().isoformat()
        }
        save_to_json(entry)
        history = load_history(user_id)
    elif request.method == "GET":
        user_id = request.args.get("user_id", "")
        if user_id:
            history = load_history(user_id)

    return render_template("index.html", casual=casual_response, formal=formal_response, history=history)

if __name__ == "__main__":
    app.run(debug=True)
