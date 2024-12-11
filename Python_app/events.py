import random
player = {
    "name": "Traveler",
    "health": 0,
    "current_location": "FI",
    "collected_antidotes": []
}

# 1 event
def apple_offer():
    print("\nYou feel someone staring at you. An elderly woman comes to you and offers you an apple. That apple really looks delicious.")
    choice = input("Do you accept the apple? (yes/no): ").strip().lower()
    if choice == "yes":
        outcome = random.choice(["success", "failure"])
        if outcome == "success":
            print("After eating the apple, you feel refreshed and full of energy.")
            player["health"] += 1
            return True
        else:
            print("After eating the apple, you start feeling sick. You must get to the plane.")
            player["health"] -= 1
            return False
    else:
        print("You politely decline the apple. Nothing changes.")
        return False
# 2 event
def wallet_discovery():
    print("\nYou find a wallet lying near a vending machine. You should probably check that out.")
    choice = input("Do you pick up the wallet? (yes/no): ").strip().lower()
    if choice == "yes":
        outcome = random.choice(["success", "failure"])
        if outcome == "success":
            print("You return the wallet to its owner, who rewards you with gratitude and a snack.")
            player["health"] += 1
            return True
        else:
            print("While picking up the wallet, security questions your actions, causing unnecessary stress.")
            player["health"] -= 1
            return False
    else:
        print("You ignore the wallet and move on. Nothing changes.")
        return False

# 3 event
def free_coffee_offer():
    print("\nA staff member offers you a cup of coffee for free. A cup of coffee would do good for ya, no?")
    choice = input("Do you accept the coffee? (yes/no): ").strip().lower()
    if choice == "yes":
        outcome = random.choice(["success", "failure"])
        if outcome == "success":
            print("The coffee is energizing and warms you up, making you feel great.")
            player["health"] += 1
            return True
        else:
            print("The coffee is too strong, making you anxious.")
            player["health"] -= 1
            return False
    else:
        print("You politely decline the coffee. Nothing changes.")
        return False

# 4 event
def storm_alert():
    print("\nAttention! There is a storm, and it is unsafe to travel for the next 2 hours.")
    choice = input("Do you wait for the storm to pass? (yes/no): ").strip().lower()
    if choice == "yes":
        print("You wait for the storm to pass. You take a little nap, boosting your energy.")
        player["health"] += 1
        return True
    else:
        print("You decide to travel anyway. You get lost, causing a delay and health loss.")
        player["health"] -= 1
        return False

# 5 event
def outfit_compliment():
    print("\nSomeone looks at you and compliments your outfit.")
    choice = input("Do you respond positively? (yes/no): ").strip().lower()
    if choice == "yes":
        print("You feel great and thank the person, returning the compliment.")
        player["health"] += 1
        return True
    else:
        print("You feel like they are mocking you and leave without a word.")
        player["health"] -= 1
        return False



