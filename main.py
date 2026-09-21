def get_response(user_input):
    user_input = user_input.lower()
        
    if "hello" in user_input:
        return "AI: Hello! How are you doing!"
        
    elif "how are you" in user_input:
        return "AI: I'm doing great! How can I help you?"
        
    elif "what is python" in user_input:
        return "AI: Python is a programming language used for many things, including software development, automation, and AI."
        
    else:
        return "AI: I'm not sure how to respond to that yet."

print("===== AI CHATBOT =====")
print("Type 'quit' to exit.")

while True: 
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        print("AI: Goodbye!")
        break
        
    response = get_response(user_input)
    print("AI:", response)
    