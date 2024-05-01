class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hi": "Hello! How can I assist you today?",
            "how are you": "I'm just a bot, but thanks for asking!",
            "bye": "Goodbye! Have a great day!"
        }

    def respond(self, message):
        message = message.lower()
        if message in self.responses:
            return self.responses[message]
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Example usage:
chatbot = SimpleChatbot()

print("Customer: Hi!")
print("Chatbot: Hello! How can I assist you today?")
while True:
    customer_input = input("Customer: ")
    response = chatbot.respond(customer_input)
    print("Chatbot:", response)
    if customer_input.lower() == 'bye':
        print("Customer: Bye!")
        break
