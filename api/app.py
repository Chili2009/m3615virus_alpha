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

@app.route("/perform_task", methods=["POST"])
def perform_task():
    tasks = ["Find a clue", "Fix a luggage machine"]
    selected_task = random.choice(tasks)
    result = random.choice(["success", "failure"])
    return jsonify({"task": selected_task, "result": result})

@app.route("/")
def home():
    return "<h1>Welcome to the M3615 Virus Flight Game API!</h1><p>Use the available endpoints to interact with the game.</p>"

if __name__ == "__main__":
    app.run(debug=True)
