
---

## 🎌 `13_08_output_validation_guardrails.md`

```md
# 13_08 — Output Validation Guardrails

## 🧠 Concept
Check output after generation.

---

## 🎯 Task
- validate required sections
- pass/fail logic

---

## 💻 Code

```python
if "Risk Level:" in response:
    print("Valid")