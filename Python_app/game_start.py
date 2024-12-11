import random
import mysql.connector
import json
from Python_app.taskit import find_clue_on_board, help_an_airport_mechanic, solve_a_broken_luggage_machine, \
    participate_in_a_quiz, help_a_lost_child, retrieve_lost_passenger_documents, navigate_power_outage, \
    find_hidden_message, candy_deal_task

from Python_app.events import apple_offer, wallet_discovery, free_coffee_offer, storm_alert, outfit_compliment

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='m3615virus_alpha',
    user='root',
    password='mexicana',
    autocommit=True
)


# Select from 20 airports in Europe for the game
def get_airport():
    sql = """SELECT iso_country, ident, name, type, latitude_deg, longitude_deg
FROM airport
WHERE continent = 'EU'
AND type = 'large_airport'
AND iso_country IN ('FI', 'SE', 'NO', 'EE', 'LV', 'LT', 'PL', 'SK',
                    'HU', 'AT', 'DE', 'CH', 'CZ', 'BE', 'NL',
                    'FR', 'DK', 'GB', 'IE', 'IS')
ORDER BY RAND()
LIMIT 20;"""
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results











# Get all goals
def get_antidotes():
    sql = "SELECT * FROM antidotes"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


def country():
    sql = "SELECT * FROM countries"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


def event():
    sql = "SELECT * FROM events"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


def leaderboard():
    sql = "SELECT * FROM leaderboard"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


def players():
    sql = "SELECT * FROM players"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


def tasks():
    sql = "SELECT * FROM tasks"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results








# Create a new game
def create_game(username):
    health_bar = 10
    current_airport = random.randint(1, 20)
    countries_visited = 0
    collected_antidotes = {}
    sql = (
        "INSERT INTO player(username, health_bar, current_airport, countries_visited, collected_antidotes) VALUES (%s, %s, %s, %s, %s)"
    )
    data = (username, health_bar, current_airport, countries_visited, collected_antidotes)
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, data)
    conn.commit()

completed_tasks = set()
completed_events = set()

def create_random_task():
    global completed_tasks
    all_tasks = [
        find_clue_on_board, help_an_airport_mechanic, solve_a_broken_luggage_machine,
        participate_in_a_quiz, help_a_lost_child, retrieve_lost_passenger_documents,
        navigate_power_outage, find_hidden_message, candy_deal_task
    ]

    remaining_tasks = [task for task in all_tasks if task.__name__ not in completed_tasks]
    if not remaining_tasks:
        print("No more tasks available!")
        return None

    task = random.choice(remaining_tasks)
    completed_tasks.add(task.__name__)
    return task()



def create_random_event():
    global completed_events
    all_events = [
        apple_offer, wallet_discovery, free_coffee_offer, storm_alert, outfit_compliment
    ]

    remaining_events = [event for event in all_events if event.__name__ not in completed_events]
    if not remaining_events:
        print("No more events available!")
        return None

    event = random.choice(remaining_events)
    completed_events.add(event.__name__)
    return event()


def travel():
    outcomes = ["task"] * 9 + ["event"] * 5 + ["nothing"] * 6
    outcome = random.choice(outcomes)

    if outcome == "task":
        return create_random_task()
    elif outcome == "event":
        return create_random_event()
    else:
        print("Nothing happened during this travel.")
        return None



# Add player to leaderboard
def add_to_leaderboard(username, time, health):
    sql = "INSERT INTO leaderboard (username, time) VALUES (%s, %s, %s)"
    data = (username, time, health)
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()



def update_player_progress(player_id, health, visited_countries, antidotes_collected):
    sql = """
    UPDATE player
    SET healthbar = %s,
        countries_visited = JSON_ARRAY_APPEND(countries_visited, '$', CAST(%s AS CHAR)),
        collected_antidotes = %s
    WHERE player_id = %s
    """
    data = (health, json.dumps(visited_countries), json.dumps(antidotes_collected), player_id)
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()






# Show menu
def show_menu():
    while True:
        print("\n==============================")
        print("     WELCOME TO M3615 VIRUS")
        print("==============================")
        print("1. Start Game")
        print("2. Leaderboard")
        print("3. Quit")
        print("==============================")

        choice = input("Select an option (1/2/3): ")

        if choice == "1":
            main_game()
        elif choice == "2":
            display_leaderboard()
        elif choice == "3":
            quit_confirmation()
        else:
            print("\nInvalid option! Please choose again.")



# Name input screen
def name_input_screen():
    print("\n==============================")
    print("      ENTER YOUR NAME")
    print("==============================")
    user_name = input("Enter your name: ").strip()

    if user_name:
        print(f"\nWelcome, {user_name}! Get ready for the game.")
        return user_name
    else:
        print("\nYou must enter a name to continue!")
        return None



def display_leaderboard():
    sql = "SELECT * FROM leaderboard ORDER BY time ASC"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()

    print("\n==============================")
    print("        LEADERBOARD")
    print("==============================")
    print(f"{'Username':<20}{'Time (Seconds)':<20}{'Health'}")
    print("==============================")

    for row in results:
        print(f"{row['username']:<20}{row['time']:<20}{row['Health']}")

    print("==============================")
    print("1. Return to Menu")
    choice = input("Select an option (1): ")
    if choice == "1":
        show_menu()
    else:
        print("\nInvalid choice! Returning to menu...")
        show_menu()



# Quit screen
def quit_confirmation():
    print("\n==============================")
    print("       QUIT THE GAME?")
    print("==============================")
    print("Do you really want to quit the game?")
    print("1. Yes")
    print("2. No")
    print("==============================")

    choice = input("Select an option (1/2): ")
    if choice == "1":
        print("\nThank you for playing! Goodbye.")
        exit()
    elif choice == "2":
        print("\nReturning to the game...")
    else:
        print("\nInvalid choice! Returning to the game...")



# You Survived screen
def survived_screen(username, time, health):
    print("\n==============================")
    print("         CONGRATULATIONS!")
    print("==============================")
    print(f"Congratulations, {username}! You survived the deadly M3615 Virus.")
    print(f"Your final time: {time}")
    print(f"Your health: {health}")
    print("==============================")
    print("1. Add to Leaderboard")
    print("2. Return to Menu")
    print("==============================")

    choice = input("Select an option (1/2): ")
    if choice == "1":
        add_to_leaderboard(username, time, health)
        print("\nYour time has been added to the leaderboard!")
    elif choice == "2":
        show_menu()
    else:
        print("\nInvalid choice! Returning to menu...")
        show_menu()


# Game Over screen
def lost_screen():
    print("\n==============================")
    print("           GAME OVER")
    print("==============================")
    print("You have succumbed to the deadly M3615 Virus.")
    print("Better luck next time!")
    print("==============================")
    print("1. Return to Menu")
    print("==============================")

    choice = input("Select an option (1): ")
    if choice == "1":
        show_menu()
    else:
        print("\nInvalid choice! Returning to menu...")
        show_menu()


# Placeholder story
def start_game_story(player_id):
    print("\n==============================")
    print("         GAME START")
    print("==============================")
    print("You have been infected by the deadly M3615 Virus!")
    print("To survive, you must travel across Europe to collect antidotes.")
    print("But beware, your health will decrease if you fail to collect antidotes in time.")
    print("Complete tasks and overcome random events in each country to get antidotes.")
    print("Good luck, your journey starts now!")
    print("==============================")

    airports = get_airport()
    health = 10
    antidotes_collected = 0
    visited_countries = set()

    while health > 0 and antidotes_collected < 9 and len(visited_countries) < 9:
        print(f"\nHealth: {health}, Antidotes Collected: {antidotes_collected}/9")
        print("Available Airports:")
        for idx, airport in enumerate(airports, start=1):
            print(f"{idx}. {airport['name']} ({airport['iso_country']})")

        choice = input("Select an airport (1-20): ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= len(airports)):
            print("Invalid choice. Try again.")
            continue

        selected_airport = airports[int(choice) - 1]
        country = selected_airport['iso_country'].strip().upper()  # Normalize

        if country in visited_countries:
            print("You have already visited this country. Choose another.")
            continue

        visited_countries.add(country)  # Add to visited set
        print(f"\nTraveling to {selected_airport['name']} in {country}...")

        outcome = travel()
        if outcome == "task":
            print("You successfully completed a task and gained an antidote!")
            antidotes_collected += 1
        elif outcome == "event":
            print("An event occurred during your travel.")
            # Event outcomes may already update health based on implementation
        else:
            print("Nothing happened during this visit.")

        health -= 1  # Deduct health for traveling
        if health <= 0:
            print("You have run out of health!")

    if antidotes_collected >= 9:
        print("\nCongratulations! You collected all antidotes and survived!")
    else:
        print("\nGame Over. You were unable to collect enough antidotes in time.")



# Main game logic
def main_game():
    user_name = name_input_screen()
    if not user_name:
        return

    health = 10
    antidotes_collected = 0
    max_antidotes = 9
    visited_countries = set()
    airports = get_airport()

    while health > 0 and antidotes_collected < max_antidotes and len(visited_countries) < 9:
        print(f"\nHealth: {health} | Antidotes Collected: {antidotes_collected}/{max_antidotes}")
        print("\nAvailable Airports:")
        for idx, airport in enumerate(airports, start=1):
            print(f"{idx}. {airport['name']} ({airport['iso_country']})")

        choice = input("\nSelect an airport to travel to (1-20): ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= len(airports)):
            print("Invalid choice. Please try again.")
            continue

        choice = int(choice) - 1
        selected_airport = airports[choice]
        country = selected_airport['iso_country']

        if country in visited_countries:
            print("You have already visited this country! Choose another.")
            continue

        visited_countries.add(country)
        print(f"\nTraveling to {selected_airport['name']} in {country}...")

        # Random outcome: task, event, or nothing
        outcome = random.choice(["task", "event", "nothing"])
        if outcome == "task":
            task_success = create_random_task()
            if task_success:
                print("Task completed successfully! You gain an antidote.")
                antidotes_collected += 1
            else:
                print("Task failed. You lose 1 health point.")
                health -= 1
        elif outcome == "event":
            print("An event occurred during your travel.")
            create_random_event()
        else:
            print("Nothing happened during this visit.")

        #health -= 1  # Deduct health for traveling

    if antidotes_collected >= max_antidotes:
        survived_screen(user_name, antidotes_collected * 10, health)
    else:
        lost_screen()



if __name__ == "__main__":
    show_menu()




