import datetime

# Knowledge Base (domain-specific Q&A)
knowledge_base = {
    "what is python": "Python is a high-level programming language used for web development, AI, and more.",
    "what is ai": "AI (Artificial Intelligence) is the simulation of human intelligence in machines.",
    "what is chatbot": "A chatbot is a software application that can simulate conversation with users."
}
    

# Log file
log_file = "chat_history.txt"

# Function to log conversation
def log_chat(user, bot):
    with open(log_file, "a") as file:
        time = datetime.datetime.now()
        file.write(f"{time} | You: {user} | Bot: {bot}\n")

# Function to get chatbot response
def get_response(user_input):
    user_input = user_input.lower()

    # Greeting Intent
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I help you?"

    # Help Intent
    elif "help" in user_input:
        return "I can answer questions about Python, AI, and chatbots. You can also ask me small talk questions."

    # Small Talk
    elif "how are you" in user_input:
        return "Perfect! WBU?"

    elif "your name" in user_input:
        return "I am a rule-based chatbot created for a project. You can call me Harry :)"

    elif "time" in user_input:
        return "Current time is: " + str(datetime.datetime.now().strftime("%H:%M:%S"))

    elif "date" in user_input:
        return "Today's date is: " + str(datetime.date.today())

    # Knowledge Base
    elif user_input in knowledge_base:
        return knowledge_base[user_input]

    # Exit Intent
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a nice day!"

    # Default
    else:
        return "Sorry, I don't understand that. Try asking something else."

# Main chatbot loop
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    response = get_response(user_input)
    print("Chatbot:", response)

    # Log conversation
    log_chat(user_input, response)

    # Exit condition
    if user_input.lower() in ["bye", "exit", "quit"]:
        break