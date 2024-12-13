const apiBaseUrl = 'http://localhost:5000';

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

    // Proceed to the game area
    document.getElementById('menu').style.display = 'none';
    document.getElementById('game-area').style.display = 'block';
    document.getElementById('player-info').innerText = `Player: ${username}`;
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
}

// Proceed to the game area
function proceedToGame() {
    document.getElementById('story-section').style.display = 'none';
    document.getElementById('game-area').style.display = 'block';
}

function proceedToDestination() {
    document.getElementById('story-section').style.display = 'none';
    document.getElementById('choose-destination').style.display = 'block';

}

function proceedToGame() {
    document.getElementById('choose-destination').style.display = 'none';
    document.getElementById('game-area').style.display = 'block';
}
// Show the main menu
function showMenu() {
    document.getElementById('menu').style.display = 'block';
    document.getElementById('game-start').style.display = 'none';
    document.getElementById('game-area').style.display = 'none';
    document.getElementById('leaderboard-area').style.display = 'none';
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

// Fetch and Display Airports
async function getAirports() {
    try {
        const response = await fetch(`${apiBaseUrl}/get_airports`);
        const data = await response.json();

        if (response.ok) {
            const airportList = data.map(
                airport => `<li>${airport.name} (${airport.iso_country})</li>`
            ).join('');
            document.getElementById('airports').innerHTML = `<ul>${airportList}</ul>`;
        } else {
            alert('Failed to fetch airports.');
        }
    } catch (error) {
        alert('Error fetching airports.');
        console.error(error);
    }
}

// Perform a Task in the Game
async function performTask() {
    try {
        const response = await fetch(`${apiBaseUrl}/perform_task`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        const data = await response.json();
        if (response.ok) {
            document.getElementById('task-result').innerText = `Task: ${data.task}, Result: ${data.result}`;
        } else {
            alert('Failed to perform task.');
        }
    } catch (error) {
        alert('Error performing task.');
        console.error(error);
    }
}

// Fetch and Display Leaderboard
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
            alert('Failed to fetch leaderboard.');
        }
    } catch (error) {
        alert('Error fetching leaderboard.');
        console.error(error);
    }
}
function returnToMenu() {
    document.getElementById('menu').style.display = 'block';
    document.getElementById('leaderboard-area').style.display = 'none';
}
