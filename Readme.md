# AI Study Companion

A local AI study assistant built with Python, Streamlit, Ollama, Pandas, and PyPDF. It combines local LLM chat, study-file context, model selection, and saved conversation history in a single desktop-friendly Streamlit application.

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.11+">
  <img src="https://img.shields.io/badge/Streamlit-Application-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Ollama-Local%20LLM-111111?style=flat-square" alt="Ollama local LLM">
  <img src="https://img.shields.io/badge/Pandas-Chat%20History-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/PyPDF-PDF%20Context-2563EB?style=flat-square" alt="PyPDF">
</p>

## Overview

AI Study Companion is a learning-focused application for working with local language models through Ollama. The interface supports ordinary chat, study resources, PDF and text context, previous conversation history, and model switching without requiring a paid cloud API.

The project was my first complete local-AI application. I built it to understand how a user interface, model calls, file processing, and persistent chat history fit together in one program.

## Key features

- Local AI chat through Ollama
- Streamlit-based interface
- General and coding model selection
- Session-based conversation display
- Chat history saved to CSV
- Previous chat loading
- Study-resource uploads
- PDF text extraction with PyPDF
- Selected files used as model context
- Study-tutor prompting
- Empty-input checks and basic exception handling

## How it works

```text
User
  |
  v
Streamlit interface
  |
  +--> Chat state and history ------> CSV storage
  |
  +--> Uploaded study resources ----> PDF / text extraction
  |
  +--> Selected model + context ----> Ollama
                                      |
                                      v
                                  Local LLM
```

The application runs locally. Ollama handles model inference, while Streamlit provides the interface and application state. Uploaded study material can be selected as additional context for a conversation.

## Project structure

```text
First-Ai-study-app/
├── Main.py
├── Database.csv
├── pages/
├── uploaded_files/
├── requirements.txt
├── Readme.md
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/RakshithNanduri/First-Ai-study-app.git
cd First-Ai-study-app
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Ollama

Install Ollama and make sure at least one compatible local model is available, then start the Ollama service:

```bash
ollama serve
```

### 4. Run the application

```bash
streamlit run Main.py
```

## Usage

1. Start the Streamlit application.
2. Choose a local Ollama model.
3. Chat directly, or upload study material.
4. Select the files you want to include as context.
5. Ask questions about the selected material.
6. Load an earlier conversation when you want to continue previous work.

## Technical notes

### Local inference

The project uses Ollama instead of a hosted API. Model availability and response quality therefore depend on the models installed on the user's machine.

### File context

PDF and text resources are converted into text that can be included in a prompt. Image-only PDF content is outside the current project's reliable scope.

### Conversation history

Chat history is stored in a CSV-based workflow. This keeps the implementation simple and inspectable, but it is not intended to replace a production database.

## What I learned

This project gave me practical experience with:

- connecting a Python application to a local LLM runtime;
- managing Streamlit session state;
- saving and loading chat history;
- processing uploaded files;
- extracting text from PDFs;
- constructing prompts with additional context;
- debugging interactions between UI, storage, and model calls.

The project was completed with AI-assisted debugging and implementation support. I treat it as guided project experience rather than evidence that every part can already be reproduced independently from memory.

## Current scope

AI Study Companion is a beginner local-AI application. It does not train or fine-tune models, provide multimodal PDF understanding, use a production database, or run as a hosted cloud service. Its purpose is to provide a working local study workflow and document the engineering lessons from building it.

## Author

**Rakshith Nanduri**  
Computer Science student building foundations in Python, C, software engineering, and local AI applications.

- GitHub: https://github.com/RakshithNanduri
- Portfolio: https://rakshith-nanduri-portfolio.vercel.app
