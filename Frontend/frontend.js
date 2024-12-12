document.addEventListener('DOMContentLoaded', () => {
    const taskSection = document.getElementById('taskSection');
    const eventSection = document.getElementById('eventSection');
    const taskContent = document.getElementById('taskContent');
    const eventContent = document.getElementById('eventContent');

    const showTaskBtn = document.getElementById('showTaskBtn');
    const showEventBtn = document.getElementById('showEventBtn');

    document.addEventListener('DOMContentLoaded', () => {
            const screens = document.querySelectorAll('.screen');
            const showScreen = (id) => {
                screens.forEach(screen => screen.classList.remove('active'));
                document.getElementById(id).classList.add('active');
            };

            document.getElementById('start').addEventListener('click', () => showScreen('name-entry'));
            document.getElementById('submit-name').addEventListener('click', () => {
                const name = document.getElementById('player-name').value.trim();
                if (name) {
                    fetch('http://localhost:5000/api/start', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ name })
                    }).then(() => showScreen('cockpit'));
                }
            });

            document.getElementById('map').addEventListener('click', () => {
                fetch('http://localhost:5000/api/events')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('event-content').textContent = data[0].name + ": " + data[0].effect;
                        showScreen('events');
                    });
            });

            document.getElementById('back-to-cockpit').addEventListener('click', () => showScreen('cockpit'));
        });

    // Fetch Task
    showTaskBtn.addEventListener('click', () => {
        fetch('http://127.0.0.1:5000/api/task')
            .then(response => response.json())
            .then(data => {
                taskContent.innerHTML = data.message;
                taskSection.style.display = 'block';
                eventSection.style.display = 'none';
            })
            .catch(error => console.error('Error fetching task:', error));
    });

    // Fetch Event
    showEventBtn.addEventListener('click', () => {
        fetch('http://127.0.0.1:5000/api/event')
            .then(response => response.json())
            .then(data => {
                eventContent.innerHTML = data.message;
                eventSection.style.display = 'block';
                taskSection.style.display = 'none';
            })
            .catch(error => console.error('Error fetching event:', error));
    });
});

const countryList = document.getElementById('countryList');
        const taskContainer = document.getElementById('taskContainer');
        const tasksSection = document.getElementById('tasks');

        // Dynamically populate country buttons
        const countries = ['FI', 'SE', 'NO', 'EE', 'LV', 'LT', 'PL', 'SK', 'HU', 'AT', 'DE', 'CH', 'CZ', 'BE', 'NL',  'FR', 'DK', 'GB', 'IE', 'IS']; // myöhemmin fetch from API
        countries.forEach((country) => {
            const button = document.createElement('button');
            button.textContent = country;
            button.onclick = () => fetchTasksForCountry(country);
            countryList.appendChild(button);
        });

        // Fetch tasks for selected country
        function fetchTasksForCountry(country) {
            fetch(`http://localhost:5000/api/tasks/${country}`)
                .then((response) => response.json())
                .then((tasks) => {
                    taskContainer.innerHTML = '';
                    tasks.forEach((task) => {
                        const taskDiv = document.createElement('div');
                        taskDiv.innerHTML = `
                            <h3>${task.name}</h3>
                            <p>${task.description}</p>
                        `;
                        taskContainer.appendChild(taskDiv);
                    });
                    tasksSection.style.display = 'block';
                })
                .catch((error) => console.error('Error fetching tasks:', error));
        }

        document.addEventListener('DOMContentLoaded', () => {
    const views = document.querySelectorAll('.view');
    const playerNameInput = document.getElementById('playerName');
    const countryList = document.getElementById('countryList');
    const inventoryList = document.getElementById('inventoryList');
    const leaderboardList = document.getElementById('leaderboardList');
    const taskEventDescription = document.getElementById('taskEventDescription');

    let playerName = '';
    let inventory = [];

    function showView(viewId) {
        views.forEach(view => view.classList.remove('active'));
        document.getElementById(viewId).classList.add('active');
    }

    window.startGame = () => {
        playerName = playerNameInput.value.trim();
        if (playerName) {
            showView('cockpit');
        } else {
            alert('Please enter your name!');
        }
    };

    window.populateMap = () => {
        const countries = ['FI', 'SE', 'NO', 'EE', 'LV', 'LT', 'PL', 'SK', 'HU', 'AT', 'DE', 'CH', 'CZ', 'BE', 'NL',  'FR', 'DK', 'GB', 'IE', 'IS']; // Example
        countryList.innerHTML = '';
        countries.forEach(country => {
            const li = document.createElement('li');
            li.textContent = country;
            li.addEventListener('click', () => openTaskOrEvent(country));
            countryList.appendChild(li);
        });
    };

    async function openTaskOrEvent(country) {
        showView('taskEvent');
        taskEventDescription.textContent = `Fetching task/event for ${country}...`;
        try {
            const response = await fetch('http://localhost:5000/api/random_event_or_task'); // API endpoint
            const data = await response.json();
            taskEventDescription.textContent = `${data.name}: ${data.description}`;
        } catch (error) {
            taskEventDescription.textContent = 'Error fetching task/event.';
        }
    }

    async function fetchLeaderboard() {
        try {
            const response = await fetch('http://localhost:5000/api/leaderboard');
            const data = await response.json();
            leaderboardList.innerHTML = '';
            data.forEach(entry => {
                const li = document.createElement('li');
                li.textContent = `${entry.username}: ${entry.score}`;
                leaderboardList.appendChild(li);
            });
        } catch (error) {
            leaderboardList.innerHTML = '<li>Error fetching leaderboard</li>';
        }
    }

    function populateInventory() {
        inventoryList.innerHTML = '';
        inventory.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item;
            inventoryList.appendChild(li);
        });
    }

    populateMap();
    fetchLeaderboard();
    populateInventory();

    window.showView = showView;
});