document.addEventListener('DOMContentLoaded', function() {
    // Display current time
    const timeDisplay = document.getElementById('time');
    const now = new Date();
    timeDisplay.innerHTML = now.toLocaleTimeString();
});

document.addEventListener('DOMContentLoaded', () => {
    // const text = "Seeking to unravel the hidden truths that bind all things . . ";
    const text = "Creativity, curiosity, and code . . .";
    const typewriter = document.querySelector('.typewriter');
    let i = 0;

    function typeNextCharacter() {
        if (i < text.length) {
            typewriter.textContent += text.charAt(i);
            i++;
            setTimeout(typeNextCharacter, 100); // Adjust typing speed here (milliseconds)
        } else {
            typewriter.classList.add('finished');
        }
    }

    // Start typing after a short delay
    setTimeout(typeNextCharacter, 1000); // 1 second delay before starting

    // Display current time and date
    const timeDisplay = document.getElementById('time');
    const dateDisplay = document.getElementById('date');

    function updateDateTime() {
        const now = new Date();
        
        // Format time: 12-hour with AM/PM, hours and minutes only
        const timeOptions = { hour: 'numeric', minute: '2-digit', hour12: true };
        timeDisplay.innerHTML = now.toLocaleTimeString('en-US', timeOptions);
        
        // Format date: 26 September 2024
        const dateOptions = { day: 'numeric', month: 'long', year: 'numeric' };
        dateDisplay.innerHTML = now.toLocaleDateString('en-US', dateOptions);
    }

    // Initial update
    updateDateTime();

    // Update every minute
    setInterval(updateDateTime, 60000);

    // ... existing code ...
});