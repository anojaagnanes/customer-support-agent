# customer-support-agent

GitAgent project for customer support AI.

---

## 🚀 Project Overview

This project implements a **GitAgent-powered AI agent** to handle customer support tasks such as greeting users, answering FAQs, and troubleshooting issues.

It also includes a **Streamlit-based chatbot UI** that allows real-time interaction with the agent.

---

## ✨ Features

### 🔹 Skills

* **greet** – Handles greetings like *good morning / evening*
* **hello-world** – Basic interaction ("Hello")
* **faq** – Answers common questions (pricing, products)
* **troubleshoot** – Helps resolve user issues step-by-step

---

### 🔹 Workflow

Deterministic execution of skills:

greet → hello-world → faq → troubleshoot

* Structured execution flow
* Easy to extend with new skills

---

### 🔹 Chatbot UI (Streamlit)

* Interactive web interface
* Real-time responses
* Maintains chat history
* Keyword-based intent detection

---

### 🔹 Agent Definition

* `agent.yaml` → configuration (model, runtime, skills)
* `SOUL.md` → agent behavior
* `skills/` → skill definitions
* `workflows/` → execution logic

---

### 🔹 Version Control

* Full Git-based tracking
* Supports rollback and branching
* Hosted on GitHub

---

## 📁 Project Structure

customer-support-agent/
├── agent.yaml
├── SOUL.md
├── skills/
│   ├── greet.md
│   ├── hello-world.md
│   ├── faq.md
│   └── troubleshoot.md
├── workflows/
│   └── customer-support.yaml
├── run_agent.py
├── README.md

---

## 🧠 How It Works

1. User enters a message in the chatbot UI
2. System checks keywords
3. Matches to a skill
4. Returns the appropriate response

### Example:

* "good morning" → greet
* "hello" → hello-world
* "price" → faq
* "issue" → troubleshoot

---

## ⚡ Quick Start

### 1. Clone the repository

git clone https://github.com/anojaagnanes/customer-support-agent.git
cd customer-support-agent

---

### 2. Install dependencies

pip install streamlit

---

### 3. Run the chatbot

python -m streamlit run run_agent.py

---

### 4. Open in browser

http://localhost:8501

---

## 💬 Example Inputs

* good morning
* hello
* price
* I have an issue

---

## 🛠 Tech Stack

* Python
* Streamlit
* Git / GitHub
* GitAgent architecture

---

## 🔮 Future Improvements

* Integrate real AI models (OpenAI / Claude)
* Add database for chat history
* Improve UI with chat bubbles
* Dynamic workflows
* Multi-agent system

---

## 👩‍💻 Author

Anojaa Gnanes

---

## ⭐ Notes

This project demonstrates how **GitAgent + AI + UI** can be combined to build a real-world chatbot system.
