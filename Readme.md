# AI Study Companion

A small local study app built with Python, Streamlit, Ollama, Pandas, and PyPDF. It lets me chat with a local model, bring selected notes or PDFs into the conversation, switch models, and save earlier chats on the same machine.

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.11+">
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Ollama-Local%20LLM-111111?style=flat-square" alt="Ollama">
  <img src="https://img.shields.io/badge/Pandas-Chat%20history-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/PyPDF-PDF%20text-2563EB?style=flat-square" alt="PyPDF">
</p>

[Portfolio case study](https://rakshith-nanduri-portfolio.vercel.app/work/ai-study-companion)

## Why I built it

This was my first complete local-AI application.

I wanted to understand how a Python interface, a local language model, uploaded study material, and saved conversation history could fit together without depending on a paid cloud API.

The project is intentionally small. It is a learning app, not a production study platform or a machine-learning project.

## What it can do

- Chat with a local Ollama model
- Switch between a general model and a coding-focused model
- Keep the current conversation visible with Streamlit session state
- Save and reload chat history from a local CSV file
- Upload notes and PDFs
- Extract PDF text with PyPDF
- Add selected file text to the model prompt as study context
- Use a simple study-tutor prompt
- Handle empty input and common model/file errors

## How it works

```text
User
  |
  v
Streamlit interface
  |
  +--> Session state + saved chats ------> local CSV
  |
  +--> Uploaded study files -------------> PDF / text extraction
  |
  +--> Selected model + file text -------> Ollama
                                              |
                                              v
                                          Local LLM
```

Ollama handles inference locally. Streamlit handles the interface and session state. When the user selects uploaded material, the app reads that file and adds its text to the prompt sent to the model.

That is simple file-context injection. This version does **not** use embeddings, a vector database, or a retrieval pipeline.

## Project structure

```text
First-Ai-study-app/
├── Main.py
├── pages/
│   ├── 1_Chat.py
│   └── 3_resources.py
├── requirements.txt
├── Readme.md
└── .gitignore
```

`Database.csv` and `uploaded_files/` are runtime data. They are ignored by Git so saved conversations and uploaded study files stay out of the repository.

## Run it locally

### 1. Clone the repository

```bash
git clone https://github.com/RakshithNanduri/First-Ai-study-app.git
cd First-Ai-study-app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Ollama

Install Ollama, make sure the model you want is available locally, and start the service:

```bash
ollama serve
```

### 4. Start the app

```bash
streamlit run Main.py
```

## Using study material

1. Open the **Resources** page.
2. Upload a text file or PDF.
3. Open the **Chat** page.
4. Select the uploaded file from the sidebar.
5. Ask a question about it.

The app reads the selected file and includes its extracted text in the prompt. Image-only PDFs are outside the reliable scope of this version because PyPDF is being used for text extraction rather than OCR or multimodal document understanding.

## Chat history

Saved conversations use a local CSV file. That choice kept the storage easy to inspect while I was learning.

The file is created at runtime and is not committed to the repository.

## What I learned

This project was where several pieces first came together for me:

- calling a local model from Python;
- working with Streamlit session state;
- saving and loading chat history;
- handling uploaded files;
- extracting text from PDFs;
- building prompts with extra context;
- debugging problems that crossed the UI, files, and model calls.

## Limits of this version

AI Study Companion does **not**:

- train or fine-tune a model;
- implement a full RAG pipeline;
- understand image-only PDF content;
- use a production database;
- provide authentication or multi-user accounts;
- run as a hosted cloud service.

## Build context

I used AI assistance for parts of the implementation and debugging. I treat this as guided practical experience and as a record of what I learned, not as proof that I could reproduce every part independently from a blank file.

---

**Rakshith Nanduri** · Computer Science student  
[GitHub](https://github.com/RakshithNanduri) · [Portfolio](https://rakshith-nanduri-portfolio.vercel.app)
