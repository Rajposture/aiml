# Simple ChatBot Program

bot = {
    "hello": "Hello! How are you?",
    "hi": "Hi! Nice to meet you.",
    "what is your name": "My name is little james.",
    "who made you": "I was made by students.",
    "what is python": "Python is a programming language.",
    "what is a chatbot": "A chatbot is a program that talks with users.",
    "tell me a joke": "Why did the programmer quit? He didn't get arrays!",
    "what is 2 + 2": "2 + 2 = 4",
    "thanks": "You're welcome!",
    "bye": "Goodbye! See you again."
}

print("Welcome! I am little james.")
print("Type 'bye' to exit.")
print("Type 'teach me' to teach me something.")

while True:
    user = input("\nYou: ").lower()

    if user == "bye":
        print("Bot:", bot["bye"])
        break

    elif user == "teach me":
        question = input("Question: ").lower()
        answer = input("Answer: ")

        bot[question] = answer
        print("Bot: Okay! I learned something new.")

    elif user in bot:
        print("Bot:", bot[user])

    else:
        print("Bot: Sorry, I don't know that.")