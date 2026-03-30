
---

## 🎌 `13_07_input_guardrails.md`

```md
# 13_07 — Input Guardrails

## 🧠 Concept
Validate input before calling the model.

---

## 🎯 Task
- check required fields
- block invalid input

---

## 💻 Code

```python
if not issue:
    print("Invalid input")
else:
    response = get_completion(prompt)