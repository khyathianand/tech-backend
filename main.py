from fastapi import FastAPI
import requests
from datetime import date

app = FastAPI()
# Temporary in-memory storage
users = {}



@app.get("/")
def home():
    return {"message": "Backend is working 🚀"}

@app.get("/daily-update")
def daily_update():
    try:
        url = "https://newsapi.org/v2/top-headlines?category=technology&apiKey=demo"
        res = requests.get(url)
        data = res.json()

        if "articles" in data and len(data["articles"]) > 0:
            article = data["articles"][0]
            return {
                "date": str(date.today()),
                "title": article["title"],
                "source": article["source"]["name"],
                "impact": "This affects how tech is evolving today.",
                "link": article["url"]
            }

    except:
        pass

    # 🔥 FALLBACK DATA (THIS IS IMPORTANT)
    return {
        "date": str(date.today()),
        "title": "AI tools are reshaping how students build apps",
        "source": "Tech Digest",
        "impact": "Faster development, lower barriers, more creators.",
        "tip": "Learning FastAPI + AI now puts you ahead of 90% people."
    }



@app.get("/quiz")
def quiz():
    return {
        "question": "Which framework is used here?",
        "options": ["Django", "Flask", "FastAPI", "Spring"],
        "answer": "FastAPI"
    }
@app.post("/login/{username}")
def login(username: str):
    if username not in users:
        users[username] = {
            "streak": 1,
            "last_login": str(date.today())
        }
    else:
        users[username]["streak"] += 1
        users[username]["last_login"] = str(date.today())

    return {
        "user": username,
        "streak": users[username]["streak"],
        "message": "Keep going 🔥"
    }

