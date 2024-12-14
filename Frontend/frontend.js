// Base API URL
const apiBaseUrl = 'http://localhost:5000';

// Stats variables
let health = 10;
let antidotes = 0;
let visitedCountries = 0;

// Show the name entry modal
function showNameModal() {
    document.getElementById('name-entry-modal').style.display = 'flex';
}

// Close the name entry modal
function closeNameModal() {
    document.getElementById('name-entry-modal').style.display = 'none';
}

// Handle name submission
function submitName() {
    const username = document.getElementById('username').value.trim();
    if (!username) {
        alert('Please enter your name.');
        return;
    }
    console.log(`Game started with username: ${username}`);
    document.getElementById('name-entry-modal').style.display = 'none';

    // Show story section
    document.getElementById('menu').style.display = 'none';
    document.getElementById('story-section').style.display = 'block';

    // Hide stats during the story section
    document.getElementById('stats-display').style.display = 'none';
}

// Proceed to the destination selection
function proceedToDestination() {
    document.getElementById('story-section').style.display = 'none';
    document.getElementById('choose-destination').style.display = 'block';
     // Show the title at the top of the screen
    document.getElementById('flight-title').style.display = 'none';
    // Hide stats during the choose destination phase
    document.getElementById('stats-display').style.display = 'none';
}

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

        listItem.addEventListener("click", () => handleCountryClick(country)); // Attach click event
        countryList.appendChild(listItem);
    });
}

function showFlightTitle() {
    document.getElementById('flight-title').style.display = 'block';
    populateCountryList();
}
// Proceed to the game area
function proceedToGame() {
    document.getElementById('choose-destination').style.display = 'none';
    document.getElementById('game-area').style.display = 'block';

    showFlightTitle();

     // Show the title on the last page
    document.getElementById('flight-title').style.display = 'block';

    // Show stats only in the game area
    document.getElementById('stats-display').style.display = 'block';
    updateStats();
}
// Show the outcome page
function showOutcomePage(title, description) {
    // Hide other sections
    document.getElementById("choose-destination").style.display = "none";
    document.getElementById("flight-title").style.display = "none";

    // Show the outcome page and set the content
    document.getElementById("outcome-page").style.display = "block";
    document.getElementById("outcome-title").textContent = title;
    document.getElementById("outcome-description").textContent = description;
}

// Return to the destination selection
function returnToDestination() {
    // Hide the outcome page and any other sections
    document.getElementById("outcome-page").style.display = "none";
    document.getElementById("choose-destination").style.display = "none";

    // Show the flight title and country list
    document.getElementById("flight-title").style.display = "block";

    // Ensure the country list is correctly populated
    const countryList = document.getElementById("country-list");
    countryList.innerHTML = ""; // Clear existing list
    populateCountryList(); // Repopulate the list

    // Show stats (if required)
    document.getElementById("stats-display").style.display = "block";
}


// Show the main menu
function showMenu() {
    document.getElementById('menu').style.display = 'block';
    document.getElementById('story-section').style.display = 'none';
    document.getElementById('choose-destination').style.display = 'none';
    document.getElementById('game-area').style.display = 'none';
    document.getElementById('leaderboard-area').style.display = 'none';

    // Hide the title
    document.getElementById('flight-title').style.display = 'none';

    // Hide stats when returning to the menu
    document.getElementById('stats-display').style.display = 'none';
}

async function showLeaderboard() {
    try {
        const response = await fetch(`${apiBaseUrl}/leaderboard`); // Backend API endpoint
        const data = await response.json();

        if (response.ok) {
            const tableBody = document.getElementById('leaderboard-table').querySelector('tbody');
            tableBody.innerHTML = ''; // Clear existing rows

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
    // Hide the leaderboard area
    document.getElementById('leaderboard-area').style.display = 'none';

    // Show the main menu
    document.getElementById('menu').style.display = 'block';
}

// Update stats display
function updateStats() {
    document.getElementById("health-bar").innerText = `${health}/10`;
    document.getElementById("antidotes-count").innerText = `${antidotes}/5`;
    document.getElementById("visited-countries-count").innerText = `${visitedCountries}`;
}

// Quit Modal Functions
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