# 🎌 Prompt Engineering Practice (Anime Edition)

## 📌 Project Title
Prompt Engineering Practice using Python and AI (Anime-Based Examples)

---
## 🚀 Overview

This project is a hands-on exploration of **prompt engineering techniques**, extended with **guardrails, safety systems, and production-style AI workflows**.

Instead of just learning theory, this repo focuses on:
- building real prompts  
- writing Python workflows  
- designing safe and reliable AI systems  

All examples follow a consistent 🎌 **anime-themed world** for better clarity and creativity.

---
### 🔹 Core Prompting Techniques
- Zero-shot prompting  
- One-shot prompting  
- Few-shot prompting  
- Multi-shot prompting  
- Chain-of-thought prompting  
- Zero-shot chain-of-thought  

---

### 🛡️ Guardrails & Safety (Production-Level)

- Instruction guardrails  
- Scope guardrails  
- Safety guardrails  
- Behavior guardrails  
- Output format guardrails  
- Fallback guardrails  
- Input validation guardrails  
- Output validation guardrails  
- Application-level guardrails  
- Escalation / handoff guardrails  
- Privacy guardrails  
- Tool / action guardrails  
- Combined guardrail workflows  

---

### ⚙️ Advanced Prompt Engineering

- Bias, fairness & ethical AI  
- Behavior control (tone, style)  
- JSON prompting (API-ready output)  
- Safe prompt workflows (constraints + fallback)  

---

## ⚙️ Setup Steps

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd prompt-engineering-practice

```

### 2. Create virtual environment
```bash
Windows
python -m venv .venv
.venv\Scripts\activate
Mac/Linux
python3 -m venv .venv
source .venv/bin/activate

```

### 3. Install dependencies
```bash
pip install -r requirements.txt

```

### 4. Add API key

Create a .env file in the root directory:
```bash
GEMINI_API_KEY=your_api_key_here

```

### ▶️ How to Run Example Files

Run any example file using:
```bash
python examples/<filename>.py
```
Example:
```bash
python examples/01_zero_shot.py
python examples/02_one_shot.py
python examples/03_few_shot.py
```
Each file demonstrates a different prompt engineering concept.

### 📁 Folder Structure
```bash
prompt-engineering-practice/
│
├── examples/        # Python files demonstrating prompting techniques
├── prompts/         # Notes and explanations for each topic
├── assignments/     # Practice tasks for each concept
├── helper.py        # Reusable function to call AI model
├── requirements.txt # Project dependencies
├── .env.example     # Example API key file
├── .gitignore       # Ignore sensitive and unnecessary files
└── README.md        # Project documentation
```

### 💡 Key Highlights

- 🎌 Built with a consistent anime-themed world for engaging, structured learning  
- 🛡️ Covers complete guardrail system (instruction → combined workflows)  
- ⚙️ Includes production-level concepts like validation, escalation, and safe workflows  
- 🧪 Demonstrates real-world issues (e.g., JSON parsing and output handling)  
- 🧱 Combines prompt design with Python-based workflow logic  
- 🚀 Focuses on building reliable, safe, and structured AI systems (not just basic prompting)
