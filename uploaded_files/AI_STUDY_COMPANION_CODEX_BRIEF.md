# AI Study Companion - Codex Project Brief

## 1. Project Name
**AI Study Companion**

## 2. Project Goal
Build a beginner-friendly local AI study assistant using only the concepts Rakshith is learning right now.

The first version should help a student ask study questions and receive clear answers from a local Ollama model through a simple Streamlit interface.

The project must be small, understandable, and easy for a first-time project builder to explain.

---

## 3. Current Student Context
Rakshith is a CSE student preparing to build his first real coding project.

Current knowledge:
- Basic Python from 11th and 12th
- Some NumPy and Pandas experience
- Beginner AI knowledge from OpenAI and Anthropic courses
- New to full project development
- New to GitHub project workflow
- No OpenAI or Anthropic API keys currently

Therefore, the project must use **Ollama locally**, not paid cloud APIs.

---

## 4. Main Rule for Codex
Do **not** over-engineer this project.

This is a first project. Build it in small working versions.

Codex should prioritize:
- Simple structure
- Clear file names
- Beginner-readable code
- Small functions
- Helpful comments only where needed
- Easy debugging
- Friendly error messages
- No advanced architecture

---

## 5. Allowed Topics Only
Use only these topics and technologies:

### Python Basics
- Variables
- Functions
- Lists
- Dictionaries
- File handling
- Error handling with try/except
- Imports and modules
- Virtual environment
- pip packages

### Git and GitHub
- Repository
- Commit
- Push
- README
- .gitignore

### APIs and JSON
- Request
- Response
- JSON-like data
- Localhost
- Error handling

### Ollama Local AI
- Local model running on the user's PC
- Python app sends prompt to Ollama
- Ollama returns answer
- No paid OpenAI or Anthropic API key required

### Streamlit UI
- Page title
- Text input
- Button
- Output area
- Sidebar settings
- Session state for chat history
- File uploader later

---

## 6. Topics to Avoid for Version 1
Do not use these in the first version:

- TensorFlow
- PyTorch
- LangChain
- LlamaIndex
- RAG
- Vector databases
- Docker
- Kubernetes
- Cloud deployment
- Authentication system
- Database
- User login
- Advanced agents
- Fine-tuning
- Complex frontend frameworks
- OpenAI API
- Anthropic API

These can be added later after the basic project works.

---

## 7. Version Plan

### Version 0 - Setup Only
Goal: Prepare the project folder.

Tasks:
- Create project folder
- Create README.md
- Create .gitignore
- Create virtual environment
- Install required packages
- Confirm Ollama is installed and running separately
- Confirm at least one Ollama model is available

Success condition:
- Project folder is clean
- README exists
- .gitignore protects unnecessary files
- Python environment is ready

---

### Version 1 - Terminal AI Chat
Goal: Prove Python can talk to Ollama.

User flow:
1. User types a study question in terminal
2. Python sends the question to Ollama
3. Ollama returns an answer
4. Python prints the answer

Success condition:
- One question can be sent successfully
- One answer is received successfully
- Errors are shown clearly if Ollama is not running

---

### Version 2 - Streamlit AI Chat
Goal: Turn the terminal chat into a simple browser app.

User flow:
1. User opens Streamlit app
2. User types a question
3. User clicks a button
4. App sends question to Ollama
5. App displays the answer

Success condition:
- App opens in browser
- User can ask one question
- AI answer appears on screen
- Blank input is handled politely

---

### Version 3 - Study Tutor Behavior
Goal: Make responses useful for students.

The assistant should answer like a beginner-friendly study tutor.

Expected answer style:
- Simple explanation first
- Example if useful
- Short summary at the end
- Admit uncertainty when needed
- Avoid overly long answers unless asked

Success condition:
- Answers feel suitable for a CSE student
- Output is structured and easy to read

---

### Version 4 - Chat History
Goal: Keep previous questions and answers visible during the session.

Use Streamlit session state.

Success condition:
- Previous messages remain visible after asking a new question
- Chat history does not disappear after normal Streamlit reruns

---

### Version 5 - Save Study Notes Locally
Goal: Save useful answers to a local text file.

User flow:
1. User asks a question
2. AI answers
3. User can save the answer
4. App stores the saved answer locally

Success condition:
- Saved notes are written to a local file
- App does not crash if file writing fails

---

### Version 6 - Text File Upload
Goal: Allow the user to upload a plain `.txt` file.

User flow:
1. User uploads a text file
2. App reads the content
3. User chooses a task such as summarize or explain
4. Ollama generates the output

Success condition:
- Text file upload works
- Empty files are handled politely
- Large text is handled carefully

---

## 8. Project Folder Structure
Use this simple structure first:

```text
ai-study-companion/
  README.md
  .gitignore
  requirements.txt
  app.py
  ai_client.py
  file_utils.py
  prompt_templates.py
  saved_notes/
  sample_notes/
```

### File Purpose

#### README.md
Explain:
- What the project does
- Why it was built
- How to run it
- Current features
- Future improvements

#### .gitignore
Ignore:
- venv/
- __pycache__/
- *.pyc
- .env
- local temporary files

#### requirements.txt
List Python packages needed to run the project.

#### app.py
Main Streamlit interface.

Should handle:
- Page title
- User input
- Button clicks
- Displaying answers
- Chat history
- Save button later

#### ai_client.py
All Ollama communication should live here.

This file should handle:
- Sending prompt to Ollama
- Returning response text
- Handling Ollama errors

#### file_utils.py
File reading and writing helpers.

This file should handle:
- Reading uploaded text files
- Saving study notes locally
- Basic file-related errors

#### prompt_templates.py
Reusable prompt-building functions.

This file should handle:
- Study tutor prompt
- Summary prompt
- Explanation prompt
- Quiz prompt later

#### saved_notes/
Folder for locally saved study notes.

#### sample_notes/
Folder for small practice text files.

---

## 9. Ollama Requirements
The user should run Ollama locally before using the project.

Recommended beginner model:
- llama3.2

Alternative coding-focused model:
- qwen2.5-coder:7b

Codex should design the project so the model name can be changed easily from one place, preferably the Streamlit sidebar.

---

## 10. Beginner-Friendly Error Handling
The app should not crash for common beginner mistakes.

Handle these cases:
- User enters blank question
- Ollama is not running
- Model is not available
- Response is empty
- Text file is empty
- File cannot be saved

Error messages should be simple and helpful.

Example style:
- "Please enter a question first."
- "Ollama does not seem to be running. Start Ollama and try again."
- "This file looks empty. Please upload a text file with notes."

---

## 11. README Requirements
The README should be written for a recruiter, lecturer, and beginner developer.

Include these sections:

1. Project Title
2. Project Description
3. Why I Built This
4. Features
5. Tech Stack
6. How It Works
7. How to Run
8. Folder Structure
9. What I Learned
10. Future Improvements

The README should clearly say that this is a beginner AI project built to learn:
- Python project structure
- Local AI with Ollama
- APIs and JSON thinking
- Streamlit UI
- GitHub workflow

---

## 12. Development Rules for Codex
Follow these rules while building:

1. Build one version at a time.
2. Do not add features before the previous version works.
3. Keep functions small.
4. Use clear names.
5. Avoid unnecessary dependencies.
6. Avoid advanced tools not listed in this brief.
7. Do not use cloud APIs.
8. Do not require paid services.
9. Do not add complex database logic.
10. Make the project explainable to a beginner.

---

## 13. Commit Plan
Suggested commit messages:

```text
Add initial project README and gitignore
Set up Streamlit app skeleton
Add Ollama client wrapper
Add basic AI chat flow
Add study tutor prompt template
Add chat history with session state
Add local note saving
Add text file upload support
Polish README and project documentation
```

---

## 14. First Milestone Definition
The first milestone is complete when:

- Streamlit app opens
- User can type a study question
- App sends the question to Ollama
- Ollama response is displayed
- Blank input does not crash the app
- README explains the project
- Code is pushed to GitHub

This is enough for the first working version.

---

## 15. Final Reminder for Codex
This project is not meant to impress by being huge.

It should impress by being:
- Clear
- Useful
- Honest
- Well documented
- Easy to run
- Easy for Rakshith to explain

Build small. Commit often. Verify outputs.
