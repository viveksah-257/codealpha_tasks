def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    # Rule-based response logic
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hi there! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm fine, thanks for asking! How about you?"
    elif "your name" in user_input:
        return "I am a simple rule-based Python chatbot created for CodeAlpha internship."
    elif "help" in user_input:
        return "You can greet me, ask how I am, or type 'bye' / 'exit' to end the chat."
    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye! Have a great day ahead!"
    else:
        return "I'm sorry, I don't understand that. Type 'help' to see what I can do."

def run_chatbot():
    print("=========================================")
    print("        CODEALPHA ASSISTANT BOT          ")
    print("=========================================")
    print("Chatbot started! Type 'bye' or 'exit' to quit.\n")

    while True:
        user_message = input("You: ")
        if not user_message.strip():
            continue

        response = get_bot_response(user_message)
        print(f"Bot: {response}\n")

        if user_message.lower().strip() in ["bye", "exit", "quit"]:
            break

if __name__ == "__main__":
    run_chatbot()
