# 💬 Chat with SQL DB

A natural language interface for querying SQL databases using LangChain and Groq LLM. This project allows users to interact with SQL databases conversationally, eliminating the need for SQL expertise.

---

## 📌 Project Overview

**Project Title:** Chat with SQL DB  
**Domain:** Generative AI | NLP | Natural Language to SQL | Data Analytics  

---

## 🧠 Problem Statement

Non-technical users often face challenges interacting with relational databases due to a lack of SQL knowledge. This project aims to bridge that gap by allowing users to query SQL databases using plain English.

---

## 💡 Proposed Solution

An intelligent chatbot powered by **LangChain** and **Groq’s LLM** to:
- Accept natural language queries from users
- Translate them into SQL using LLM
- Execute the SQL query on SQLite or MySQL databases
- Display results in a conversational format
- Maintain context to support follow-up questions
- Support dynamic schemas and multi-database connections

---

## 🎯 Objectives

- Create a chat-based web app to interact with databases using natural language
- Integrate LangChain’s SQL agent with Groq’s LLM
- Enable both local (SQLite) and remote (MySQL) database queries
- Ensure robust and context-aware interaction

---

## 🛠️ Tech Stack

| Tool / Technology | Purpose |
|-------------------|---------|
| Python            | Backend logic and integration |
| LangChain         | LLM-based SQL generation |
| Groq LLM          | Fast natural language processing |
| Streamlit         | Web interface (chat UI) |
| SQLite / MySQL    | Databases |
| SQLAlchemy        | Database abstraction layer |
| dotenv / .env     | Environment variable management |

---

## 🚀 Features

- 🧠 Natural language to SQL translation
- 🔁 Dual support for SQLite and MySQL
- ⏱️ Fast response time (~3 seconds)
- 🧩 Context-aware multi-turn conversation
- 🛡️ Robust error handling and fallback messaging

---

## 📊 Results (Initial Testing)

| Metric              | Outcome |
|---------------------|---------|
| Query Accuracy      | High (e.g., "List employees older than 50" translated correctly) |
| Response Time       | < 3 seconds |
| Edge Case Handling  | Graceful degradation with clear error messages |
| Robustness          | Handled disconnections and missing credentials |

---


