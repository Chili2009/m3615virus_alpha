import random
player = {
    "name": "...",
    "health": 0,
    "current_location": "FI",
    "collected_antidotes": []
}

# 1 task
def find_clue_on_board():
    print("\nYou find a mysterious board in the airport lounge.")
    print("It has multiple clues written in code.")
    codes = ["X32YZ", "M3615", "H2S99"]
    correct_code = "M3615"
    print(f"The codes are: {', '.join(codes)}")
    print("\nYou must choose the correct code to find the antidote.")

    player_code = input("\nEnter the code you think is correct: ").strip().upper()
    if player_code == correct_code:
        print(f"Correct! The code '{correct_code}' reveals the antidote location.")
        return True
    else:
        print(f"Wrong! The correct code was '{correct_code}'. You missed the antidote.")
        return False

# 2 antidote
def help_an_airport_mechanic():
    print("\nYou notice an airport mechanic struggling to repair an important system.")
    print("They ask you to help solve a problem before the system overheats.")
    print("You have 3 attempts to guess the right fix.")

    correct_fix = random.randint(1, 10)
    for attempt in range(3):
        try:
            guess = int(input(f"\nAttempt {attempt + 1}/3 - Enter a number (1-10) to fix the system: "))
            if guess == correct_fix:
                print("You guessed correctly! The mechanic thanks you with an antidote!")
                return True
            else:
                print("Wrong fix. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"The correct fix was {correct_fix}. The system fails, and you leave empty-handed.")
    return False


# 3 antidote
def solve_a_broken_luggage_machine():
    print("\nYou notice that the airport's luggage sorting system is malfunctioning.")
    print("The line is getting longer, and passengers are frustrated.")
    print("You decide to step in and fix the problem.")

    print("\nWhat will you do?")
    print("1. Try to fix the mechanical issue")
    print("2. Work on the software issue")
    print("3. Ask the airport staff for help")

    try:
        player_choice = int(input("\nChoose an option (1, 2, 3): "))
        if player_choice == 1:
            print("You fix the mechanical issue and the system starts working again. You gain access to an antidote!")
            return True
        elif player_choice == 2:
            print("You repair the software and the luggage system operates smoothly. You find a hidden antidote!")
            return True
        elif player_choice == 3:
            print("You ask for help, and the staff give you a map with an antidote location.")
            return True
        else:
            print("Invalid choice. Try again.")
            return False
    except ValueError:
        print("Invalid input. Try again.")
        return False


# 4 task
def participate_in_a_quiz():
    print("\nYou come across a travel trivia quiz being held at the airport.")
    print("The winner gets a special prize. You decide to join and answer some questions.")

    questions = [
        ("What is the capital of Germany?", "Berlin"),
        ("Which country is famous for the Eiffel Tower?", "France"),
        ("Where is megis from?", "Finland")
    ]

    question, correct_answer = random.choice(questions)
    print(f"\nQuestion: {question}")
    player_answer = input("\nYour answer: ")

    # lower tekee niin että vaikka pelaaja kirjottais esim berlin tai bERLIN nii se vastaus ois silti oikein
    if player_answer.lower() == correct_answer.lower():
        print("Correct! You win the prize, which includes an antidote!")
        return True
    else:
        print("Incorrect answer. Better luck next time!")
        return False


# 5 task
def help_a_lost_child():
    print("\nA child approaches you at the airport, looking lost and scared.")
    print("They ask you to help them find their parents. You decide to assist them.")

    print("\nWhere will you look for the parents?")
    print("1. The lost and found section")
    print("2. The waiting area near the gates")
    print("3. Ask the airport staff to make an announcement")

    try:
        player_choice = int(input("\nChoose an option (1, 2, 3): "))
        if player_choice == 1:
            print("You find the parents in the lost and found section. They give you an antidote in gratitude!")
            return True
        elif player_choice == 2:
            print("The parents are waiting in the lounge. They thank you and give you an antidote!")
            return True
        elif player_choice == 3:
            print(
                "The staff help make an announcement. The parents come to pick up the child, and they give you an antidote!")
            return True
        else:
            print("Invalid choice. Try again.")
            return False
    except ValueError:
        print("Invalid input. Try again.")
        return False


# 6 task
def retrieve_lost_passenger_documents():
    print("\nA passenger approaches you, looking stressed. They've lost their documents.")
    print("You decide to help by following a series of clues.")

    print("\nThe first clue: 'The documents are hidden where people rest.'")
    print("1. Luggage storage area")
    print("2. Airport lounge")
    print("3. Bathrooms")

    try:
        choice = int(input("Your choice: "))
        if choice == 2:
            print("You find the documents in the lounge! The passenger rewards you with an antidote.")
            return True
        else:
            print("Wrong choice. The documents remain missing.")
            return False
    except ValueError:
        print("Invalid input. Try again.")
        return False


# 7 task
def navigate_power_outage():
    print("\nThe airport experiences a sudden power outage.")
    print("You must navigate to safety.")

    paths = ["main hallway", "emergency stairs", "lounge"]
    safe_path = random.choice(paths)

    print("\nChoose your path:")
    print("1. Main hallway")
    print("2. Emergency stairs")
    print("3. Lounge")

    try:
        choice = int(input("\nYour choice (1, 2, or 3): "))
        if paths[choice - 1] == safe_path:
            print(f"You safely navigate through the {paths[choice - 1]} and find an antidote!")
            return True
        else:
            print(f"You chose the {paths[choice - 1]}, but you get lost in the dark.")
            return False
    except (ValueError, IndexError):
        print("Invalid choice. You remain stuck in the dark.")
        return False


# 8 task
def find_hidden_message():
    print("\nYou overhear a cryptic message being announced in the airport.")
    print("It might lead to an antidote!")

    print("\nSolve the riddle: What month of the year has 28 days?")
    print("The options are:\n 1 - All of them \n 2 - February \n 3 - December")
    answer = input("Your answer: ").strip().lower()
    if answer == "1":
        print("Correct! The riddle reveals the antidote location.")
        return True
    else:
        print("Wrong answer. The message remains a mystery.")
        return False


# 9 task
def pharmacy_backroom_task():
    print("As you sit in the airport café, you overhear two employees whispering:")
    print('"There’s an antidote in the pharmacy backroom near Gate 12. It’s hidden with the other experimental meds."')
    print("You notice the pharmacy staff leaving for lunch. This might be your only chance.")
    input("Press Enter to 'Sneak into the backroom'...")

    print("\nYou carefully make your way to the pharmacy, avoiding prying eyes.")
    print("The backroom door is slightly ajar, and you slip inside. There it is—the antidote!")
    print("You grab the antidote and quickly leave before anyone notices.")
    return True


# 10 task
def candy_deal_task():
    print(
        "\nYou are sitting in the airport lounge, and suddenly, you spot something shiny under a bench. It's an antidote!")
    print(
        "You reach down to grab it, but just as your hand touches it, a little child rushes over and snatches it away.")
    print("The child looks at you with a big grin and says:")
    print("\n'If you want this antidote, you have to buy me candy first! I want the biggest candy bar in the store!'")
    print("\nWhat will you do?")
    print("1. Agree to buy the candy and go to the store.")
    print("2. Refuse and try to take the antidote from the child.")
    print("3. Try to convince the child that the antidote is more important than candy.")

    try:
        player_choice = int(input("\nChoose an option (1, 2, 3): "))
        if player_choice == 1:
            print("You go to the store, buy the biggest candy bar you can find, and return to the child.")
            print("The child is happy and hands you the antidote with a big smile!")
            return True
        elif player_choice == 2:
            print("The child refuses to give you the antidote and runs away with it. You lost your chance!")
            return False
        elif player_choice == 3:
            print("The child laughs and says, 'No way! Candy is way cooler than that!'")
            print("Looks like you'll have to buy the candy after all.")
            return False
        else:
            print("Invalid choice. Try again.")
            return False
    except ValueError:
        print("Invalid input. Try again.")
        return False