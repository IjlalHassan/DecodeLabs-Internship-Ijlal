KNOWLEDGE_BASE = {
    "hello":                    "Hello! I'm Ijlal's Bot. How can I help you today?",
    "hi":                       "Hey there! What's on your mind?",
    "hey":                      "Hey! I'm listening.",
    "how are you":              "I'm a rule-based system — always running at 100%!",
    "what is ai":               "AI is the simulation of human intelligence by machines using logic, learning, and reasoning.",
    "what can you do":          "I can answer questions about AI and hold a basic conversation.",
    "who made you":             "Built by Ijlal Hassan.An AI Engineering intern at DecodeLabs, Batch 2026.",
    "what is machine learning": "ML is a subset of AI where systems learn from data without being explicitly programmed.",
    "what is deep learning":    "Deep learning uses multi-layered neural networks to model complex patterns in data.",
    "help":                     "Try asking: 'what is AI', 'what is machine learning', or just say 'hello'.",
    "bye":                      "Goodbye! Keep building.",
    "thanks":                   "You're welcome. Keep learning.",
    "thank you":                "Anytime. That's what I'm here for.",
}

EXIT_COMMANDS = {"exit", "quit", "q"}
FALLBACK = "I don't understand that yet. Type 'help' to see what I know."

def sanitize(raw):
    return raw.lower().strip()

def get_response(user_input):
    if user_input in EXIT_COMMANDS:
        return None

    elif user_input in KNOWLEDGE_BASE:
        return KNOWLEDGE_BASE[user_input]

    else:
        return FALLBACK

def run():
    print("Ijlal's Bot | Rule-Based AI Chatbot")
    print("Type 'exit' to quit.\n")

    while True:
        raw = input("You: ")
        clean = sanitize(raw)
        response = get_response(clean)

        if response is None:
            print("Ijlal's Bot: Session terminated. Build something great.")
            break
        else:
            print(f"Ijlal's Bot: {response}\n")

if __name__ == "__main__":
    run()