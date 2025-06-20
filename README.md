# 📅 GenAI Content Calendar Builder

> Generate a 30-day social media content calendar using FastAPI + OpenAI.  
> Built for educational purposes as part of a Generative AI learning journey.

---

## 🚀 Overview

This project uses a simple FastAPI backend to generate content ideas, captions, hooks, and hashtags based on your **brand**, **platform**, and **tone of voice** — all powered by the OpenAI API.

Whether you're a solo creator or just learning GenAI apps, this tool shows how to:

- Accept structured user input  
- Prompt an LLM with chained logic  
- Return clean JSON for frontend or export use  

---

## ✨ Features

- 🧠 Generates 30 unique post ideas using AI  
- ✍️ Returns captions, hooks, and hashtags  
- 🎯 Customizable by brand, platform, and tone  
- ⚡ FastAPI-powered backend with simple API  
- 🔒 `.env` file support for secure API key usage  

---

## 🧰 Tech Stack

- **Backend**: FastAPI  
- **AI**: OpenAI API (GPT-4-turbo or similar)  
- **Language**: Python 3.11+  
- **Other**: Pydantic, Uvicorn, dotenv  

---

## 🛠 Step 1: Clone & Install

```bash
git clone https://github.com/YOUR_USERNAME/content_calendar_builder.git
cd content_calendar_builder
pip install -r requirements.txt
```

---

## 🔑 Step 2: Set Up Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
```

This keeps your credentials safe and out of version control.

---

## ▶️ Step 3: Run the App

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) to test the API in your browser.

---

## 🧪 Step 4: Example API Usage

### 🔗 POST `/generate-calendar`

#### 📥 Request

```json
{
  "brand_name": "FitFuel",
  "platform": "Instagram",
  "tone": "motivational"
}
```

#### 💻 curl Example

```bash
curl -X POST http://localhost:8000/generate-calendar \
  -H "Content-Type: application/json" \
  -d '{"brand_name":"FitFuel", "platform":"Instagram", "tone":"motivational"}'
```

#### 📤 Response

```json
{
  "calendar": [
    {
      "day": 1,
      "idea": "Share your brand origin story.",
      "caption": "From a passion project to a movement: how FitFuel started 💪 #FoundersStory #FitFuel",
      "hook": "Ever wondered how FitFuel was born?",
      "hashtags": ["#FitFuel", "#FitnessJourney", "#StartupStory"]
    },
    ...
  ]
}
```

---

## 🧱 Step 5: Project Structure

```
content_calendar_builder/
├── app/
│   ├── main.py             # FastAPI entry point with endpoint logic
│   ├── generator.py        # Core logic for generating the calendar content
│   ├── prompts.py          # Prompt templates for the OpenAI API
│   └── models.py           # Pydantic models for request/response validation
├── .env                    # Stores API keys and environment variables (excluded from GitHub)
├── requirements.txt        # All required Python packages
├── README.md               # This file you're reading
└── .gitignore              # Ignores .env and other non-essential files
```

---

## 🙌 Credits

Built by **JP** as part of a Generative AI learning journey  
with guidance from ChatGPT (*aka Yugi 🧠✨*)

> *"Tools should teach you as they work for you."*

---

## 🧠 Learning Milestones

- ✅ FastAPI routing & request handling  
- ✅ OpenAI prompt design and chaining  
- ✅ Secure API key management with `.env`  
- ✅ JSON response formatting for frontend consumption  
- ✅ Structuring small-scale GenAI apps for reuse and growth

---

## 📬 Feedback

If you learned something or improved this project, feel free to **fork**, ⭐ **star**, or open a **pull request**!

---

**Now is the Time.**
