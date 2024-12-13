const apiBaseUrl = 'http://localhost:5000';

async function startGame() {
    const username = document.getElementById('username').value;
    if (!username) {
        alert('Please enter a username.');
        return;
    }

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
}

async function getAirports() {
    const response = await fetch(`${apiBaseUrl}/get_airports`);
    const data = await response.json();

    if (response.ok) {
        const airportList = data.map(airport => `<li>${airport.name} (${airport.iso_country})</li>`).join('');
        document.getElementById('airports').innerHTML = `<ul>${airportList}</ul>`;
    } else {
        alert('Failed to fetch airports.');
    }
}

async function performTask() {
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
}

async function showLeaderboard() {
    const response = await fetch(`${apiBaseUrl}/leaderboard`);
    const data = await response.json();

    if (response.ok) {
        const leaderboardList = data.map(player => `<li>${player.username}: ${player.health_bar}</li>`).join('');
        document.getElementById('leaderboard').innerHTML = leaderboardList;
        document.getElementById('leaderboard-area').style.display = 'block';
    } else {
        alert('Failed to fetch leaderboard.');
    }
}
