import random
import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def tokenize_input(input_text):
    # Tokenize the input text using spaCy
    doc = nlp(input_text)
    return [token.text.lower() for token in doc if not token.is_punct]

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

    year = int(input("What year were you born? "))
    age_guess = 2024 - year

    print(f"I'm guessing you're around {age_guess} years old based on your birth year.")

def numgame():
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = int(input("You have to guess the number I have in my mind\nEnter your guess between 0-9 : "))
    b = random.choice(number)

    print("Alright Your Guessed Number was :", a)

    if a == b:
        print("OMG,,,,Perfect guess")
    else:
        while a != b:
            if a < b:
                print("Oops....Guess a little bit higher : ")
                a = int(input())
            elif a > b:
                print("Hehehe....Guess a little bit lower : ")
                a = int(input())
            if a == b:
                print("Yoooooooo...Finally guessed it")
                break

def chat():
    while True:
        user_input = input("You: ").lower()
        tokens = tokenize_input(user_input)
        # print("Tokens:", tokens)

        if "hello" in tokens or "hi" in tokens:
            greet()
        elif "bye" in tokens or "goodbye" in tokens:
            farewell()
            break
        elif "guess" in tokens:
            print("What do you want? 'Me to guess your age' OR 'Wanna play a number guessing game?' Tell me.")
        elif "age" in tokens:
            age_guesser()
        elif "number" in tokens or "game" in tokens:
            numgame()
        else:
            responses = ["I'm not sure I understand.", "Could you please repeat that?", "Tell me more!"]
            print(random.choice(responses))

if __name__ == "__main__":
    print("Welcome to the Simple Chatbot!")
    print("Feel free to say hello, ask me to guess your age, or just chat with me.")
    chat()




# pip install spacy
# python -m spacy download en_core_web_sm



#     Integration of spaCy: I imported the spaCy library and loaded its English language model (en_core_web_sm).
#     This model is used for tokenization of user inputs.
#
#     Tokenization function: The tokenize_input function was modified to utilize spaCy for tokenization.
#     Now, the function takes the input text, processes it using spaCy, and returns a list of lowercase tokens without punctuation.
#
#     Usage in chatbot: Throughout the chatbot code, the tokenize_input function is used to tokenize user inputs before processing them.
#     This allows for more accurate handling of user commands and responses.

# Example of how spaCy uses tokens
# Feel free to say hello, ask me to guess your age, or just chat with me.
# You: hi
# Tokens: ['hi']
# Hi there!
# You: hello!, how are you doing?
# Tokens: ['hello', 'how', 'are', 'you', 'doing']
# Hi there!
# You: