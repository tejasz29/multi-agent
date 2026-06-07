# 📚 Intelligent Multi-Agent Adaptive Exam Planner

A smart AI-powered exam preparation system that generates personalized day-wise study plans using a multi-agent architecture. Built for students who want structured, topic-wise planning — not generic study tips.

---

## ✨ Features

- **Planner Agent** — Generates a structured day-wise plan across multiple subjects, progressing from basics to advanced with built-in revision days
- **Explainer Agent** — Explains planned topics in beginner-friendly language using bullet points
- **Adaptive Coach** — Tracks progress, detects missed sessions, and provides smart catch-up recommendations
- **Dashboard** — Visual analytics with progress charts, subject-wise stats, and smart insights

---

## 🛠️ Tech Stack

- **Frontend** — Streamlit with sidebar navigation
- **LLM** — LLaMA 3.3 70B via Groq API (fast inference)
- **Database** — SQLite for persistent study plan & progress
- **Charts** — Matplotlib (pie + bar charts)

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/tejasz29/multi-agent.git
cd multi-agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Groq API key
```bash
cp .env.example .env
# Open .env and paste your key from https://console.groq.com/keys
```

### 4. Run the app
```bash
streamlit run app.py
```

---

## 📁 Project Structure
```
multi-agent/
├── app.py                  ← Main Streamlit UI
├── agents/
│   ├── planner_agent.py    ← Generates study plan
│   ├── explainer_agent.py  ← Explains topics
│   └── adaptive_agent.py   ← Adaptive recommendations
├── database/
│   └── db.py               ← SQLite CRUD operations
├── utils/
│   ├── groq_client.py      ← Groq API wrapper
│   └── charts.py           ← Matplotlib charts
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## 📚 Subjects Covered

- Machine Learning
- Operating Systems
- Microprocessors
- Advanced Mathematics for Computer Engineering
- Drone Technology
- Environmental Studies

---

## 🚀 How It Works

1. Student selects subjects and available study days
2. Planner Agent creates a balanced day-wise schedule
3. Explainer Agent breaks down each session's topics
4. Student marks sessions as complete in the UI
5. Adaptive Coach adjusts recommendations based on progress
6. Dashboard visualizes performance with charts and insights

---

**Tejas Eklare** · B.Tech Computer Engineering 
