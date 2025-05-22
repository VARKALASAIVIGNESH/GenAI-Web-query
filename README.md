
# 🧠 AI Query Generator (Flask + Groq + JSON)

A lightweight Flask web app that generates both **casual** and **formal** AI responses to user queries using the **Groq LLaMA API**, and stores query history automatically in a local JSON file.

---

## 🚀 Features

- 🔍 Accepts user input (User ID + Query)
- 🤖 Generates **two styles of responses**:
  - Casual (fun, friendly tone)
  - Formal (detailed, academic tone)
- 🗃️ Stores all queries and responses in `prompts.json` (no database required)
- 📜 Displays complete query history for reference
- 🌐 Minimal HTML UI with internal CSS (no external dependencies)
- 🛠️ Simple structure: only essential files included

---

## 📁 Project Structure

```

├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # Frontend with embedded CSS
├── .env                   # Environment variables (Groq API Key)
├── prompts.json           # Auto-generated query-response history
├── requirements.txt       # Dependencies
└── README.md              # You're here!

````

---

## 🧪 How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/VARKALASAIVIGNESH/GenAI-Web-query.git
cd ai-query-generator
````

### 2. Set Up the Environment

#### Create a `.env` file

```env
GROQ_API_KEY=your-groq-api-key-here
```

> 🛑 **Important:** Never share your API key publicly.

#### Install Requirements

```bash
pip install -r requirements.txt
```

---

### 3. Run the App

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🧠 Example Usage

* Enter your **User ID** (for tracking)
* Ask a question (e.g., *"What is blockchain?"*)
* View both **casual** and **formal** responses
* Check below for **previous interactions**

All queries are saved to `prompts.json` in this format:

```json
[
  {
    "user_id": "vickey",
    "query": "explain python",
    "casual_response": "...",
    "formal_response": "...",
    "timestamp": "2025-05-22T13:55:57.574008"
  }
]
```

---

## 🔐 Security Note

* `.env` is used for API key management
* Add `.env` and `prompts.json` to `.gitignore` before pushing to public repos

---

## ✨ Future Ideas

* Add dark mode toggle
* Export history to CSV or Markdown
* Per-user JSON history files
* Query filters (date/user/topic)

---

## 📜 License

MIT License — use freely, modify smartly, and deploy proudly 🚀

---

## 🙋‍♂️ Author

**Vickey** — [GitHub](https://github.com/VARKALASAIVIGNESH)
Built with ❤️ using Flask and Groq's LLaMA models


Let me know if you want this tailored for deployment (e.g. Heroku or Docker), or want a visual badge-rich version for GitHub!

