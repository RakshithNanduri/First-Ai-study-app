<div align="center">

# 🤖 AI Study Companion

### A beginner-friendly AI-powered study assistant built with **Python, Streamlit, and Ollama**

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-000000?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas)
![PyPDF](https://img.shields.io/badge/PyPDF-PDF%20Support-blue?style=for-the-badge)

---

**My first complete AI application built completely from scratch during my AI engineering journey.**

This project helped me understand how to build a real application using local LLMs, manage chat history, process PDFs, and create an interactive user interface using Streamlit.

</div>

---

# 📖 Overview

AI Study Companion is a lightweight study assistant that runs entirely on **local AI models through Ollama**.

Instead of relying on paid cloud APIs, the application allows users to chat with local language models, upload study material, maintain conversation history, and receive beginner-friendly explanations.

The goal of this project was not just to build an AI chatbot, but to understand how modern AI applications are structured from frontend to backend.

---

# ✨ Features

## ✅ Version 1

- AI Chat Interface
- Beautiful Homepage
- Custom App Logo
- Chat Memory
- CSV Chat History
- Beginner Friendly UI

---

## ✅ Version 2

- Load Previous Chats
- File Upload Support
- PDF Reading using PyPDF
- Select Files as AI Context
- Resource Management Page

---

## ✅ Version 3

- Beginner Study Tutor Prompt
- Better Error Handling
- Empty Input Validation
- Model Switching
- Improved Homepage
- Better Sidebar Layout
- Better Chat Experience

---

# 🏗 Project Architecture

```text
                User
                  │
                  ▼
          Streamlit Interface
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
 Chat System   File Upload   CSV Memory
      │           │
      ▼           ▼
   Ollama      PDF Reader
      │
      ▼
 Local AI Model
```

---

# 📂 Project Structure

```text
AI Study Companion
│
├── pages/
├── uploaded_files/
├── Main.py
├── Database.csv
├── requirements.txt
├── Readme.md
└── .gitignore
```

---

# 🚀 Technologies Used

- Python
- Streamlit
- Ollama
- Pandas
- PyPDF
- CSV Storage

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/RakshithNanduri/First-Ai-study-app.git
```

Move into the project

```bash
cd First-Ai-study-app
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start Ollama

```bash
ollama serve
```

Run the application

```bash
streamlit run Main.py
```

---

# 💡 What I Learned

This project taught me

- Building complete Streamlit applications
- Integrating local LLMs with Ollama
- Managing chat history
- Working with CSV databases
- Reading PDF files
- Organizing Python projects
- Debugging real-world problems
- Building AI applications without paid APIs

---

# 🎯 Why I Built This

I wanted my first AI project to be something practical rather than another simple chatbot.

Instead of using cloud APIs, I challenged myself to build an AI application powered entirely by local language models using Ollama. Along the way I learned application structure, debugging, state management, file handling, and how different components work together in a real AI project.

Although this is my first AI application, it represents the beginning of my journey toward becoming an AI Engineer.

---

<div align="center">

### Built with by Rakshith

**Learning • Building • Improving**

</div>
