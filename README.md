# 🎧 Customer Support Escalation Agent

[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.27+-orange?style=flat-square)](https://streamlit.io/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.1.15-red?style=flat-square)](https://www.langgraph.com/)

---

## 🚀 Project Overview

This is a **multi-agent customer support system** built with **LangGraph** and **LLMs**, capable of:

- Classifying user issues: **billing**, **technical**, or **general**
- Generating **AI-powered responses**
- Self-evaluating response **confidence**
- **Conditional human escalation** for low-confidence or high-urgency issues
- Interactive **Streamlit UI** for real-time demonstration

The project uses **Pydantic** for schema enforcement, ensuring reliable and type-safe outputs from the LLM.

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **LangGraph** – multi-agent orchestration
- **LangChain** + Google Gemini or OpenAI GPT
- **Streamlit** – frontend UI
- **Pydantic** – structured output schemas
- **python-dotenv** – environment variable management

---

## 📁 Project Structure

```bash
Customer Support Escalation Agent/
├── app.py # CLI test runner
├── ui.py # Streamlit interactive demo
├── graph.py # LangGraph orchestration
├── state.py # Shared state TypedDict
├── routing.py # Conditional routing logic
├── schemas.py # Pydantic schemas
├── nodes/ # Multi-agent reasoning nodes
│ ├── classifier.py
│ ├── resolver.py
│ ├── confidence.py
│ └── escalate.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚡ Features

- **Dynamic issue classification**: AI decides billing, technical, or general
- **Context-aware AI responses**: Resolves user issues automatically
- **Reflection agent**: Self-evaluates response confidence
- **Conditional routing**: Escalates low-confidence or urgent issues
- **Interactive UI**: Shows response, category, urgency, confidence, escalation
- **Safe structured output**: Pydantic enforces types and ranges

---

## 🔧 Installation

1. Clone the repo:

```bash
git clone https://github.com/MohitMurarka/customer_support_escalation_agent
cd "Customer Support Escalation Agent"
```

2.  Create virtual environment:

```bash
python -m venv venv
.\venv\Scripts\Activate     # Windows
pip install --upgrade pip
pip install -r requirements.txt
```

3.  Setup environment variables:

```bash
cp .env.example .env
```

Add your API key(s) to .env:

```bash
GOOGLE_API_KEY=your_google_genai_key_here
# or
OPENAI_API_KEY=your_openai_key_here
```

4.  Run the UI:

```bash
streamlit run ui.py
```

---

# Demo Examples

Below are some demo inputs for the Customer Support Escalation Agent, along with their category, urgency, and whether they require escalation.

| Input                                                             | Category  | Urgency | Escalation |
| ----------------------------------------------------------------- | --------- | ------- | ---------- |
| “I was charged twice for my subscription and need a refund ASAP!” | billing   | high    | ✅         |
| “My account keeps logging me out every 5 minutes.”                | technical | high    | ✅         |
| “How can I change my profile picture in the app?”                 | general   | low     | ❌         |
| “I upgraded my plan but features aren’t showing.”                 | technical | medium  | ✅         |
| “My dog walked on the keyboard and deleted my messages.”          | general   | low     | ❌         |

---

# 🚀 Multi-Agent AI System Demo

A production-grade, resume-ready multi-agent AI system showcasing reflection-based reasoning, conditional escalation, and type-safe outputs with an interactive Streamlit interface.

---

## 📸 Screenshots / Demo GIF

Example:

![Demo GIF](https://github.com/MohitMurarka/customer_support_escalation_agent/blob/main/Screenshot%202026-01-12%20161628.png?raw=true)

---

## 💡 Key Takeaways

- Built a **production-grade multi-agent AI system**
- Demonstrates **reflection-based reasoning** and **conditional escalation**
- Ensures **type-safe outputs** using **Pydantic**
- Includes an **interactive Streamlit demo**
- Ideal for **hackathons, portfolios, and technical interviews**

---

## 📌 Optional Enhancements

- Chat-style conversation history
- Confidence-based progress bar
- Metrics dashboard for AI performance
- Retry logic for low-confidence predictions

---

## Author

This project was created by **MR. MOHIT MURARKA**.  

- **GitHub:** [https://github.com/MohitMurarka](https://github.com/MohitMurarka)
- **LinkedIn:** [https://www.linkedin.com/in/Mohit-Murarka](https://www.linkedin.com/in/mohit-murarka-b165882aa/)  

Feel free to reach out for collaboration, feedback, or project inquiries.
