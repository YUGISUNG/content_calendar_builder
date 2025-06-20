from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from openai import OpenAI  # ✅ Correct import

load_dotenv()

client = OpenAI()  # ✅ Correct capitalization

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Content Calendar Builder API!"}

class CalendarRequest(BaseModel):
    brand: str
    platform: str
    tone: str

@app.post("/generate-calendar/")
def generate_calendar(request: CalendarRequest):
    prompt = (
        f"You are a creative content strategist. "
        f"Generate a 30-day content calendar for a {request.brand} brand, "
        f"on {request.platform}, using a {request.tone} tone. "
        f"Include Post Idea, Caption, and Hashtags for each day, clearly labeled like:\n"
        f"Day 1:\nPost Idea: ...\nCaption: ...\nHashtags: ..."
    )

    # 🧠 Send to OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert social media strategist."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=2000
    )

    raw_text = response.choices[0].message.content

    # 🧼 Split & clean the response
    days = raw_text.strip().split("Day ")
    calendar = []

    for entry in days:
        if entry.strip() == "":
            continue
        try:
            day_number = int(entry.split(":")[0])
            lines = entry.splitlines()
            post_idea = next((line.replace("Post Idea:", "").strip() for line in lines if "Post Idea:" in line), "")
            caption = next((line.replace("Caption:", "").strip() for line in lines if "Caption:" in line), "")
            hashtags = next((line.replace("Hashtags:", "").strip() for line in lines if "Hashtags:" in line), "")

            calendar.append({
                "day": day_number,
                "post_idea": post_idea,
                "caption": caption,
                "hashtags": hashtags
            })
        except Exception as e:
            print(f"Error parsing entry: {entry[:30]}... — {e}")
            continue

    return {"calendar": calendar}
