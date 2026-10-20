
import random

print("=" * 45)
print("       TURING TEST EXPERIMENT")
print("=" * 45)
print("You are talking to a hidden participant.")
print("Ask questions and decide if it is human or AI.")
print("Type 'exit' to finish the test.\n")

responses = {
    "hello": ["Hey! How are you?", "Hi there!", "Hello! What's up?"],
    "name": ["You can call me Alex.", "I'm Alex. What about you?"],
    "age": ["I'm 20 years old.", "Old enough to know better!"],
    "study": ["I'm studying computer science.", "I have been learning Python lately."],
    "food": ["I love pizza!", "Probably pasta. What's your favorite?"],
    "hobby": ["I enjoy music and movies.", "I like reading and exploring new things."],
    "sad": ["I'm sorry. Want to talk about it?", "That sounds difficult. I'm listening."],
    "love": ["That's a big question!", "I think trust matters most."],
    "why": ["Interesting question. What do you think?", "There could be many reasons."],
    "default": [
        "Hmm, why do you think that?",
        "That's interesting. Tell me more.",
        "I never thought about it that way.",
        "Can you explain what you mean?",
        "What makes you ask that?"
    ]
}

def reply(message):
    message = message.lower()

    for keyword in responses:
        if keyword != "default" and keyword in message:
            return random.choice(responses[keyword])

    return random.choice(responses["default"])


questions = 0

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    print("Participant:", reply(user))
    questions += 1

print("\n" + "=" * 45)
print("           TEST COMPLETED")
print("=" * 45)
print("Questions asked:", questions)

if questions < 3:
    print("Ask more questions for a better evaluation.")
else:
    print("\nNow make your judgment:")
    print("1. Human")
    print("2. Artificial Intelligence")

    choice = input("Your decision (1 or 2): ")

    if choice == "1":
        print("You judged the participant as HUMAN.")
    elif choice == "2":
        print("You judged the participant as AI.")
    else:
        print("Invalid choice.")

print("Thank you for participating in the Turing Test!")
