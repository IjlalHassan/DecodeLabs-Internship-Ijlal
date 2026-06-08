# Ijlal's Bot — Rule-Based AI Chatbot

> Project 1 | DecodeLabs Industrial Training Kit | Batch 2026

---

## What It Does

Terminal chatbot using pure if-else logic and dictionary-based intent matching. No ML. No APIs. Just deterministic control flow — the foundation every AI engineer must master before touching neural networks.

Responds to 13+ predefined intents. Handles unknown inputs gracefully. Exits cleanly on command.

---

## Tech Stack

- Python 3.x
- Zero external dependencies

---

## How to Run

```bash
# Clone or download the project
git clone https://github.com/yourusername/ijlals-bot.git
cd ijlals-bot

# Run the chatbot
python "Project 1_Rule Based-Chatbot.py"
```

---

## Example Session

```
Ijlal's Bot | Rule-Based AI Chatbot
Type 'exit' to quit.

You: hello
Ijlal's Bot: Hello! I'm Ijlal's Bot. How can I help you today?

You: what is ai
Ijlal's Bot: AI is the simulation of human intelligence by machines using logic, learning, and reasoning.

You: what is machine learning
Ijlal's Bot: ML is a subset of AI where systems learn from data without being explicitly programmed.

You: random stuff
Ijlal's Bot: I don't understand that yet. Type 'help' to see what I know.

You: exit
Ijlal's Bot: Session terminated. Build something great.
```

---

## Supported Commands

| Input | Response |
|---|---|
| `hello` / `hi` / `hey` | Greeting |
| `how are you` | Status reply |
| `what is ai` | AI definition |
| `what is machine learning` | ML definition |
| `what is deep learning` | Deep learning definition |
| `what can you do` | Capability list |
| `who made you` | Creator info |
| `help` | Shows available commands |
| `thanks` / `thank you` | Acknowledgement |
| `bye` | Farewell message |
| `exit` / `quit` / `q` | Terminates session |

---

## Project Architecture

```
Input → Sanitize (lower + strip) → Intent Match (if-else + dict) → Output
```

- **Sanitization** — handles case and whitespace variations
- **if-else logic** — exit detection, known intent, fallback
- **Dictionary lookup** — O(1) response retrieval for known intents
- **while True loop** — continuous session until exit command

---

## Key Concepts Demonstrated

- Control flow and decision-making logic
- IPO Model (Input → Process → Output)
- Rule-based AI vs probabilistic AI
- White-box / explainable AI systems
- Deterministic guardrails (foundation of AI safety)

---

## Author

**Ijlal Hassan**
BS Artificial Intelligence
DecodeLabs Intern — Batch 2026
