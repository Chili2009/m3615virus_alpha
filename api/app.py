from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)


@app.route("/start_game", methods=["POST"])
def start_game():
    data = request.json
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    return jsonify({"message": f"Game started for {username}"}), 200


@app.route("/get_airports", methods=["GET"])
def get_airports():
    airports = [
        {"name": "Helsinki Airport", "iso_country": "FI"},
        {"name": "Oslo Gardermoen", "iso_country": "NO"}
    ]
    return jsonify(airports)

@app.route("/travel", methods=["POST"])
def travel():
    outcomes = (
        ["task"] * 10 +
        ["event"] * 5 +
        ["nothing"] * 5
    )
    outcome = random.choice(outcomes)

    if outcome == "task":
        tasks = [
            "Find a missing item", "Assist a fellow traveler", "Fix a luggage issue",
            "Translate a document", "Help at the airport counter",
            "Navigate a map", "Carry an extra bag", "Guide someone to a terminal",
            "Report a suspicious activity", "Rebook a missed flight"
        ]
        task = random.choice(tasks)
        return jsonify({"outcome": "task", "task": task})
    elif outcome == "event":
        events = [
            "A free snack offer", "A lost wallet found", "Meeting an old friend",
            "A delayed flight announcement", "An unexpected upgrade"
        ]
        event = random.choice(events)
        return jsonify({"outcome": "event", "event": event})
    else:
        return jsonify({"outcome": "nothing", "message": "Nothing happened during the travel."})

@app.route("/perform_task", methods=["POST"])
def perform_task():
    tasks = ["Find a clue", "Fix a luggage machine"]
    selected_task = random.choice(tasks)
    result = random.choice(["success", "failure"])
    return jsonify({"task": selected_task, "result": result})


@app.route("/leaderboard", methods=["GET"])
def leaderboard():
    # Simulate data from database
    leaderboard_data = [
        {"username": "Player1", "time": 120, "health_bar": 10},
    ]
    return jsonify(leaderboard_data)


@app.route("/")
def home():
    return "<h1>Welcome to the M3615 Virus Flight Game API!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
