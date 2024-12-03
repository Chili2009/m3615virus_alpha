import random
import mysql.connector


# ==============================
# DATABASE CONNECTION HANDLER
# ==============================
class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            port=3306,
            database='m3615virus_alpha',
            user='root',
            password='mexicana',
            autocommit=True
        )

    def fetch_all(self, query, params=None):
        """Fetch all results for a query."""
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(query, params or ())
            return cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return []

    def execute(self, query, params=None):
        """Execute a query that modifies data."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params or ())
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Database error: {e}")


# ==============================
# GAME LOGIC
# ==============================
class M3615VirusGame:
    def __init__(self, db):
        self.db = db
        self.health = 10
        self.antidotes_collected = 0
        self.max_antidotes = 9
        self.visited_countries = 0

    def get_airports(self):
        """Fetch a list of airports for the game."""
        query = """SELECT iso_country, ident, name FROM airport
                   WHERE continent = 'EU' AND type = 'large_airport'
                   ORDER BY RAND() LIMIT 20"""
        return self.db.fetch_all(query)

    def travel_to_airport(self, airport):
        """Travel to the selected airport and complete a task."""
        print(f"\nTraveling to {airport['name']} in {airport['iso_country']}...")
        task_result = self.create_random_task()
        self.visited_countries += 1
        if task_result:
            print("Task completed successfully!")
            self.antidotes_collected += 1
        else:
            print("Task failed. You lose 1 health point.")
            self.health -= 1

    def create_random_task(self):
        """Generate and execute a random task."""
        tasks = [
            self.find_clue_on_board,
            self.help_an_airport_mechanic,
            self.solve_a_broken_luggage_machine,
        ]
        random_task = random.choice(tasks)
        return random_task()

    def find_clue_on_board(self):
        print("Finding clue on board...")
        return random.choice([True, False])

    def help_an_airport_mechanic(self):
        print("Helping an airport mechanic...")
        return random.choice([True, False])

    def solve_a_broken_luggage_machine(self):
        print("Solving a broken luggage machine...")
        return random.choice([True, False])

    def play(self):
        """Main game loop."""
        airports = self.get_airports()
        while self.health > 0 and self.visited_countries < 9:
            print(f"\nHealth: {self.health} | Antidotes: {self.antidotes_collected}/{self.max_antidotes}")
            print(f"Countries visited: {self.visited_countries}/9")

            for idx, airport in enumerate(airports, start=1):
                print(f"{idx}. {airport['name']} ({airport['iso_country']})")

            choice = input("\nSelect a country (1-20): ").strip()
            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(airports):
                print("Invalid choice. Try again.")
                continue

            selected_airport = airports[int(choice) - 1]
            self.travel_to_airport(selected_airport)

        if self.visited_countries >= 9:
            print("\nCongratulations! You visited 9 countries and survived.")
        else:
            print("\nGame Over. You succumbed to the virus.")


# ==============================
# USER INTERFACE (UI)
# ==============================
def show_menu(db):
    """Display the main menu and handle user input."""
    game = M3615VirusGame(db)

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
            user_name = input("\nEnter your name: ").strip()
            if user_name:
                print(f"\nWelcome {user_name}! Get ready.")
                game.play()
            else:
                print("Name cannot be empty.")
        elif choice == "2":
            display_leaderboard(db)
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("Invalid option! Please choose again.")


def display_leaderboard(db):
    """Fetch and display the leaderboard."""
    leaderboard = db.fetch_all("SELECT username, time FROM leaderboard ORDER BY time ASC")
    print("\nLeaderboard:")
    for entry in leaderboard:
        print(f"{entry['username']} - {entry['time']}s")


# ==============================
# MAIN ENTRY POINT
# ==============================
if __name__ == "__main__":
    db = Database()
    show_menu(db)
