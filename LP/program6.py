def ask_question(question):
    """Function to ask a question and get user input."""
    return input(question).lower().strip()


def recommend_facility(symptoms):
    """Function to recommend a medical facility based on symptoms."""
    if 'chest pain' in symptoms:
        return "You should go to the nearest hospital's emergency department immediately."
    elif 'fever' in symptoms or 'cough' in symptoms:
        return "You can visit a nearby clinic or see your primary care physician."
    else:
        return "You might consider scheduling an appointment with a specialist."


def main():
    print("Welcome to the Hospital and Medical Facility Expert System!")
    print("I can help you find the appropriate medical facility based on your symptoms.")

    symptoms = []

    # Ask the user about their symptoms
    while True:
        symptom = ask_question("What symptom are you experiencing? (Enter 'done' when finished): ")
        if symptom == 'done':
            break
        symptoms.append(symptom)

    # Recommend a medical facility based on symptoms
    recommendation = recommend_facility(symptoms)

    # Output recommendation
    print("\nRecommendation:", recommendation)


if __name__ == "__main__":
    main()
