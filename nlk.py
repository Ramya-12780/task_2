import nltk
from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses
pairs = [
    (r"my name is (.*)", ["Hello %1, how can I help you today?"]),
    (r"this is(.*)", ["Hello ramya!"]),
    (r"hi|hello|hey", ["Hello! How can I assist you today?"]),
    (r"what is your name?", ["I am lisa created by OpenAI."]),
    (r"how are you?", ["I'm just a computer program, but I'm doing great!"]),
    (r"sorry (.*)", ["No problem. How can I assist you?"]),
    (r"quit", ["Bye! Have a great day!"]),
    (r"(.*)", ["Sorry, I didn't understand that. Can you rephrase?"])
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I'm a  lisa. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print(f"lisa: {response}")
        if user_input.lower() == "quit":
            break

# Start the chatbot
if __name__ == "__main__":
    chat()