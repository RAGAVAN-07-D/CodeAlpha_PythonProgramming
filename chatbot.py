# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hi", "hello"]:
        return "Hi there!"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm fine, thanks! How can I help you?"
    elif user_input in ["bye", "goodbye"]:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that."

def main():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        
        if user_input.lower() in ["bye", "goodbye"]:
            break

# Run the chatbot
main()
