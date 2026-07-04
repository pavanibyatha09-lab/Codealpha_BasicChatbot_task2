print("Welcome to Basic Chatbot!")
print("Type 'bye' to exit the chatbot.")

while True:
    user_input = input("you: ").lower()

    if user_input == "hello" or user_input == "hi" or user_input == "hey" :
        print("Bot: Hi welcome.!")
    
    elif user_input == "how are you":
        print("Bot: I'm fine, thanks! How can i help you?")

    elif user_input == "thank you":
        print("Bot: you're welcome!")

    elif user_input == "bye" :
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("bot: Sorry, I don't understand that.")
