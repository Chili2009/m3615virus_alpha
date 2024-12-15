
const apiBaseUrl = 'http://localhost:5000';

let health = 10;
let antidotes = 0;
let visitedCountries = 0;

/* ------------------------------
   Modal and UI Management
------------------------------ */
function showNameModal() {
    document.getElementById('name-entry-modal').style.display = 'flex';
}

function closeNameModal() {
    document.getElementById('name-entry-modal').style.display = 'none';
}

function showQuitModal() {
    document.getElementById('quit-modal').style.display = 'flex';
}

function closeModal() {
    document.getElementById('quit-modal').style.display = 'none';
}

function confirmQuit() {
    alert('Thanks for playing!');
    window.location.href = '/';
}


/* ------------------------------
   Name Submission
------------------------------ */
function submitName() {
    const username = document.getElementById('username').value.trim();
    if (!username) {
        alert('Please enter your name.');
        return;
    }
    console.log(`Game started with username: ${username}`);
    document.getElementById('name-entry-modal').style.display = 'none';
    document.getElementById('menu').style.display = 'none';
    document.getElementById('story-section').style.display = 'block';
    document.getElementById('stats-display').style.display = 'none';
}

/* ------------------------------
   Game Navigation
------------------------------ */
function proceedToDestination() {
    document.getElementById('story-section').style.display = 'none';
    document.getElementById('choose-destination').style.display = 'block';
    document.getElementById('flight-title').style.display = 'none';
    document.getElementById('stats-display').style.display = 'none';
}

function proceedToGame() {
    document.getElementById('choose-destination').style.display = 'none';
    document.getElementById('game-area').style.display = 'block';
    showFlightTitle();
    document.getElementById('flight-title').style.display = 'block';
    document.getElementById('stats-display').style.display = 'block';
    updateStats();
}

/* ------------------------------
   Destination Handling
------------------------------ */
const countries = [
    "Finland", "Sweden", "Norway", "Estonia", "Latvia",
    "Lithuania", "Poland", "Slovakia", "Hungary", "Austria",
    "Germany", "Switzerland", "Czech Republic", "Belgium",
    "Netherlands", "France", "Denmark", "United Kingdom",
    "Ireland", "Iceland"
];

function handleCountryClick(country) {
    console.log(`Traveling to: ${country}`);
    fetch(`${apiBaseUrl}/travel`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ country }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.outcome === "task") {
            showOutcomePage("Task", `You have a task: ${data.task}`);
        } else if (data.outcome === "event") {
            showOutcomePage("Event", `An event occurred: ${data.event}`);
        } else {
            showOutcomePage("Nothing", "Nothing happened during the travel.");
        }
    })
    .catch(error => console.error("Error:", error));
}

function populateCountryList() {
    const countryList = document.getElementById("country-list");
    countryList.innerHTML = ""; // Clear existing list
    countries.forEach(country => {
        const listItem = document.createElement("li");
        listItem.textContent = country;
        listItem.className = "country-item";
        listItem.addEventListener("click", () => handleCountryClick(country));
        countryList.appendChild(listItem);
    });
}

function showFlightTitle() {
    document.getElementById('flight-title').style.display = 'block';
    populateCountryList();
}

/* ------------------------------
   Outcome Handling
------------------------------ */
function showOutcomePage(title, description) {
    document.getElementById("choose-destination").style.display = "none";
    document.getElementById("flight-title").style.display = "none";
    document.getElementById("outcome-page").style.display = "block";
    document.getElementById("outcome-title").textContent = title;
    document.getElementById("outcome-description").textContent = description;
}

function returnToDestination() {
    document.getElementById("outcome-page").style.display = "none";
    document.getElementById("choose-destination").style.display = "none";
    document.getElementById("flight-title").style.display = "block";
    const countryList = document.getElementById("country-list");
    countryList.innerHTML = "";
    populateCountryList();
    document.getElementById("stats-display").style.display = "block";
}

/* ------------------------------
   Stats and Menu Management
------------------------------ */
function updateStats() {
    document.getElementById("health-bar").innerText = `${health}/10`;
    document.getElementById("antidotes-count").innerText = `${antidotes}/5`;
    document.getElementById("visited-countries-count").innerText = `${visitedCountries}`;
}

function showMenu() {
    document.getElementById('menu').style.display = 'block';
    document.getElementById('story-section').style.display = 'none';
    document.getElementById('choose-destination').style.display = 'none';
    document.getElementById('game-area').style.display = 'none';
    document.getElementById('leaderboard-area').style.display = 'none';
    document.getElementById('flight-title').style.display = 'none';
    document.getElementById('stats-display').style.display = 'none';
}

/* ------------------------------
   Leaderboard
------------------------------ */
async function showLeaderboard() {
    try {
        const response = await fetch(`${apiBaseUrl}/leaderboard`);
        const data = await response.json();
        if (response.ok) {
            const tableBody = document.getElementById('leaderboard-table').querySelector('tbody');
            tableBody.innerHTML = '';
            data.forEach(player => {
                const row = document.createElement('tr');
                const nameCell = document.createElement('td');
                nameCell.textContent = player.username;
                const timeCell = document.createElement('td');
                timeCell.textContent = player.time;
                const healthCell = document.createElement('td');
                healthCell.textContent = player.health_bar;
                row.appendChild(nameCell);
                row.appendChild(timeCell);
                row.appendChild(healthCell);
                tableBody.appendChild(row);
            });
            document.getElementById('menu').style.display = 'none';
            document.getElementById('leaderboard-area').style.display = 'block';
        } else {
            alert('Failed to fetch leaderboard data.');
        }
    } catch (error) {
        alert('Error fetching leaderboard data.');
        console.error(error);
    }
}

function returnToMenu() {
    document.getElementById('leaderboard-area').style.display = 'none';
    document.getElementById('menu').style.display = 'block';
}
