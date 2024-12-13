const apiBaseUrl = 'http://localhost:5000';

// Start Game
async function startGame() {
    const username = document.getElementById('username').value;
    if (!username) {
        alert('Please enter a username.');
        return;
    }

    try {
        const response = await fetch(`${apiBaseUrl}/start_game`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username }),
        });

        const data = await response.json();
        if (response.ok) {
            document.getElementById('game-start').style.display = 'none';
            document.getElementById('game-area').style.display = 'block';
            document.getElementById('player-info').innerText = `Player: ${username}`;
        } else {
            alert(data.error);
        }
    } catch (error) {
        alert('Failed to start the game. Please try again.');
        console.error(error);
    }
}

// Navigation Functions
function showMenu() {
    document.getElementById('menu').style.display = 'block';
    document.getElementById('game-start').style.display = 'none';
    document.getElementById('game-area').style.display = 'none';
    document.getElementById('leaderboard-area').style.display = 'none';
}

function showGame() {
    document.getElementById('menu').style.display = 'none';
    document.getElementById('game-start').style.display = 'block';
}

function returnToMenu() {
    showMenu();
}

// Name Entry Modal
function showNameModal() {
    document.getElementById('name-modal').style.display = 'flex';
}

function closeNameModal() {
    document.getElementById('name-modal').style.display = 'none';
}

async function submitNameAndStart() {
    const username = document.getElementById('username').value;
    if (!username) {
        alert('Please enter your name.');
        return;
    }

    console.log(`Game started with username: ${username}`);

    try {
        const response = await fetch(`${apiBaseUrl}/start_game`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username }),
        });

        const data = await response.json();
        if (response.ok) {
            closeNameModal();
            document.getElementById('game-start').style.display = 'none';
            document.getElementById('game-area').style.display = 'block';
            document.getElementById('player-info').innerText = `Player: ${username}`;
        } else {
            alert(data.error);
        }
    } catch (error) {
        alert('Failed to start the game. Please try again.');
        console.error(error);
    }
}

// Quit Modal
function showQuitModal() {
    document.getElementById('quit-modal').style.display = 'flex';
}

function closeModal() {
    document.getElementById('quit-modal').style.display = 'none';
}

function confirmQuit() {
    alert("Thanks for playing!");
    window.location.href = '/';
}

// Fetch Data Functions
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
