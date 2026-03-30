# 13_01 — Instruction Guardrails

## 🧠 Concept
Instruction guardrails are rules inside the prompt that control how the model responds.

They help:
- prevent hallucination
- control output length
- ensure consistent behavior

---

## 🎯 Task
Create a prompt with at least 4 instruction guardrails.

---

## 🎌 Prompt

You are an anime shop assistant.

TASK:
Answer using the policy below.

RULES:
1. Only use policy information
2. Do NOT make up details
3. Keep answer under 3 lines
4. If unsure, say: "Please ask the guild master"

---

## 💻 Code

```python
response = get_completion(prompt)
print(response)