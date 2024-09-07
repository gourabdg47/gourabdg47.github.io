document.addEventListener('DOMContentLoaded', function() {
    // Display current time
    const timeDisplay = document.getElementById('time');
    const now = new Date();
    timeDisplay.innerHTML = now.toLocaleTimeString();
});
