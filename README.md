# 🎌 Prompt Engineering Practice (Anime Edition)

## 📌 Project Title
Prompt Engineering Practice using Python and AI (Anime-Based Examples)

---

## 📚 Topics Covered

This project demonstrates the following prompt engineering techniques:

- Zero-shot prompting  
- One-shot prompting  
- Few-shot prompting  
- Multi-shot prompting  
- Chain-of-thought prompting  
- Zero-shot chain-of-thought  
- System, user, assistant roles  
- Prompt structuring basics  
- Prompt reuse and versioning  
- JSON prompting (structured outputs)  
- Prompt design patterns (classification, extraction, transformation, generation)  
- Prompt engineering vs prompt tuning vs instruction tuning  

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
### 💡 Summary

This project focuses on mastering prompt engineering techniques to effectively control and optimize AI outputs.

It builds practical, hands-on skills required to work with large language models in real-world applications such as automation, content generation, and intelligent systems.