import random
from random import choice

import mysql.connector
import taskit

from Python_app.taskit import find_clue_on_board, help_an_airport_mechanic, solve_a_broken_luggage_machine, \
    participate_in_a_quiz, help_a_lost_child, retrieve_lost_passenger_documents, navigate_power_outage, \
    find_hidden_message, candy_deal_task

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


def create_random_task():
    tasks = {
        1: find_clue_on_board,
        2: help_an_airport_mechanic,
        3: solve_a_broken_luggage_machine,
        4: participate_in_a_quiz,
        5: help_a_lost_child,
        6: retrieve_lost_passenger_documents,
        7: navigate_power_outage,
        8: find_hidden_message,
        10: candy_deal_task
    }
    previous_tasks = []
    random_task = random.randint(1, 10)
    while random_task in previous_tasks:
        random_task = random.randint(1, 10)
    previous_tasks.append(random_task)
    result = tasks[random_task]()
    #sql = "SELECT * FROM tasks WHERE id = random_task"
    #cursor = conn.cursor(dictionary=True)
    #cursor.execute(sql)
    #task = cursor.fetchall()
    return result


def create_random_event():
    random_event = random.randint(1, 5)
    previous_events = []
    while random_event in previous_events:
        random_event = random.randint(1, 5)
    previous_events.append(random_event)
    sql = "SELECT * FROM events WHERE id = random_event"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    event = cursor.fetchall()
    return event


def travel(airport_id):
    task_event = random.randint(1, 3)
    if task_event == 1:
        task = create_random_task()
    if task_event == 2:
        task = create_random_event()
    else:
        task = None


# Add player to leaderboard
def add_to_leaderboard(username, time):
    sql = "INSERT INTO leaderboard (username, time) VALUES (%s, %s)"
    data = (username, time)
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()


# You Survived screen
def survived_screen(username, time):
    print("\n==============================")
    print("         CONGRATULATIONS!")
    print("==============================")
    print(f"Congratulations, {username}! You survived the deadly M3615 Virus.")
    print(f"Your final time: {time}")
    print("==============================")
    print("1. Add to Leaderboard")
    print("2. Return to Menu")
    print("==============================")

    choice = input("Select an option (1/2): ")
    if choice == "1":
        add_to_leaderboard(username, time)
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


# Placeholder story
def start_game_story():
    print("\n==============================")
    print("         GAME START")
    print("==============================")
    print("You have been infected by the deadly M3615 Virus!")
    print("To survive, you must travel across Europe to collect antidotes.")
    print("But beware, your health will decrease if you fail to collect antidotes in time.")
    print("Complete tasks and overcome random events in each country to get antidotes.")
    print("Good luck, your journey starts now!")
    print("==============================")

def start_game_story():
    print("\n==============================")
    print("         GAME START")
    print("==============================")
    print("You have been infected by the deadly M3615 Virus!")
    print("To survive, you must travel across Europe to collect antidotes.")
    print("Select a country on the map to travel to. Complete tasks to collect antidotes.")
    print("Good luck, your journey starts now!")
    print("==============================")

    airports = get_airport()
    visited_countries = set()
    health = 10
    antidotes_collected = 0
    max_antidotes = 9

    while health > 0 and antidotes_collected < max_antidotes:
        print("\nYour current health:", health)
        print("Antidotes collected:", antidotes_collected, "/", max_antidotes)

        print("\nAvailable airports:")
        for idx, airport in enumerate(airports, start=1):
            print(f"{idx}. {airport['name']} ({airport['iso_country']})")

        choice = input("\nSelect a country to travel to (1-20): ").strip()

        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(airports):
            print("\nInvalid selection. Please choose a valid number.")
            continue

        choice = int(choice) - 1
        selected_airport = airports[choice]
        country_name = selected_airport['iso_country']

        if country_name in visited_countries:
            print("\nYou have already visited this country! Choose another.")
            continue

        visited_countries.add(country_name)
        print(f"\nTraveling to {selected_airport['name']} in {country_name}...")

        task_result = create_random_task()
        if task_result:
            print("\nTask completed successfully!")
            antidotes_collected += 1
        else:
            print("\nTask failed. You lose 1 health point.")
            health -= 1

    if antidotes_collected >= max_antidotes:
        survived_screen("Player", health * 10 + antidotes_collected)
    else:
        lost_screen()

# Main game logic
def main_game():
    user_name = name_input_screen()
    if not user_name:
        return

    start_game_story()
    create_random_task()

    health = 10
    antidotes_collected = 0
    max_antidotes = 9

    while health > 0 and antidotes_collected < max_antidotes:
        print(f"\nHealth: {health} | Antidotes Collected: {antidotes_collected}/{max_antidotes}")
        health -= 1
        antidotes_collected += 1

    if antidotes_collected >= max_antidotes:
        survived_screen(user_name, health * 10 + antidotes_collected)
    else:
        lost_screen()


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


if __name__ == "__main__":
    show_menu()





