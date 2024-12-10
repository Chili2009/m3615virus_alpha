document.addEventListener('DOMContentLoaded', () => {
    const startBtn = document.getElementById('startBtn');
    const goToCockpitBtn = document.getElementById('goToCockpitBtn');
    const startJourneyBtn = document.getElementById('startJourneyBtn');
    const nextBtn = document.getElementById('nextBtn');

    const leaderboardBtn = document.getElementById('leaderboardBtn');
    const quitBtn = document.getElementById('quitBtn');
    const gameSection = document.getElementById('game-section');
    const leaderboardSection = document.getElementById('leaderboard-section');
    const menuSection = document.getElementById('menu-section');
    const leaderboardList = document.getElementById('leaderboard-list');
    const cockpitSection = document.getElementById('cockpit-section');
    const eventSection = document.getElementById('event-section');

    startBtn.addEventListener('click', () => {
        menuSection.style.display = 'none';
        gameSection.style.display = 'block';
    });

    leaderboardBtn.addEventListener('click', () => {
        menuSection.style.display = 'none';
        leaderboardSection.style.display = 'block';
        showLeaderboard();
    });

    // Handle Quit button click
    quitBtn.addEventListener('click', () => {
        alert("Thank you for playing!");
        window.close();  // Close the browser window
    });

    document.getElementById('backToMenuBtn').addEventListener('click', () => {
        leaderboardSection.style.display = 'none';
        menuSection.style.display = 'block';
    });

      // Go to cockpit screen
    goToCockpitBtn.addEventListener('click', () => {
        gameSection.style.display = 'none';  // Hide game placeholder
        cockpitSection.style.display = 'block';  // Show cockpit screen
    });

     // Start journey and show a random event or task
    startJourneyBtn.addEventListener('click', () => {
        // Hide cockpit and show event/task section
        cockpitSection.style.display = 'none';
        eventSection.style.display = 'block';

          // Trigger random task or event
        fetchTaskOrEvent();  // Fetch and display either task or event
    });

    // Fetch random task or event from Python backend
    function fetchTaskOrEvent() {
    fetch('http://127.0.0.1:5000/api/task_or_event')
        .then(response => response.json())
        .then(data => {
            const item = data.item;
            const itemType = data.type;
            
            if (itemType === 'task') {
                // Display task
                console.log('Task:', item.task_description);
                // Display the task description on the UI
            } else if (itemType === 'event') {
                // Display event description and choices
                console.log('Event:', item.description);
                console.log('Choices:', item.choices);
                // Display the event description and choices on the UI
            }
        })
        .catch(error => {
            console.error('Error fetching task or event:', error);
        });
    }

    function showLeaderboard() {
    fetch('http://127.0.0.1:5000/api/leaderboard')
        .then(response => response.json())
        .then(data => {
            const leaderboardList = document.getElementById('leaderboard-list');
            leaderboardList.innerHTML = ''; // Clear existing leaderboard
            
            data.forEach(player => {
                const li = document.createElement('li');
                li.textContent = `${player.username}: ${player.score}`;
                leaderboardList.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Error fetching leaderboard:', error);
        });
}
nextBtn.addEventListener('click', () => {
        eventSection.style.display = 'none';  // Hide event section
        menuSection.style.display = 'block';  // Show menu again
    });
});

