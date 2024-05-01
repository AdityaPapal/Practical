import random

def greet():
    greetings = ["Hi there!", "Hello!", "Hey!"]
    print(random.choice(greetings))

def farewell():
    farewells = ["Goodbye!", "See you later!", "Bye!"]
    print(random.choice(farewells))

def age_guesser():
    print("I'm going to guess your age!")
    name = input("Firstly, what's your name? ")
    print(f"Nice to meet you, {name}!")

    gender = input("What is your gender? ")
    age_guess = random.randint(18, 40)  # Random initial guess

    if gender.lower() == "male":
        age_guess += 5
    elif gender.lower() == "female":
        age_guess -= 3

    print(f"I'm guessing you're around {age_guess} years old based on your gender.")

def chat():
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            greet()
        elif "bye" in user_input or "goodbye" in user_input:
            farewell()
            break
        elif "age" in user_input or "guess" in user_input:
            age_guesser()
        else:
            responses = ["I'm not sure I understand.", "Could you please repeat that?", "Tell me more!"]
            print(random.choice(responses))

if __name__ == "__main__":
    print("Welcome to the Simple Chatbot!")
    print("Feel free to say hello, ask me to guess your age, or just chat with me.")
    chat()
