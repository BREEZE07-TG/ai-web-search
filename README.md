# 🌐 AI Web Search

A simple Python script that combines **Tavily's real-time web search** with a **free GPT endpoint** to answer any question using live internet data.

---

## 🚀 How It Works

```
Your Question
     │
     ▼
🔍 Tavily API  ──►  Fetches top 10 real web results
     │
     ▼
📝 Context Builder  ──►  Combines page content into a text block
     │
     ▼
🤖 Binjie AI  ──►  Reads context and answers concisely
     │
     ▼
💡 Answer + 📚 Sources
```

---

## ✨ Features

- 🔍 **Real-time web search** via Tavily — not outdated training data
- 🤖 **AI-generated answers** grounded in actual web content
- 📚 **Sources listed** so every answer is verifiable
- 🖥️ **Clean terminal UI** with step-by-step progress

---

## 📦 Requirements

- Python 3.8+
- A free [Tavily API key](https://app.tavily.com)

Install dependencies:

```bash
pip install requests aiohttp python-dotenv
```

---

## ⚙️ Setup

1. **Clone the repo**
```bash
git clone https://github.com/BREEZE07-TG/ai-web-search.git
cd ai-web-search
```

2. **Run it**
```bash
python ai-web-search.py
```

---

## 📁 Project Structure

```
ai-web-search
|-- ai-web-search.py
|-- Readme.md
```
---

## 🛠️ Built With

- [Tavily API](https://tavily.com) — Real-time web search
- [aiohttp](https://docs.aiohttp.org) — Async HTTP client

---

## 📄 License

MIT — free to use and modify.
