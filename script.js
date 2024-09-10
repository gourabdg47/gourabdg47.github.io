document.addEventListener('DOMContentLoaded', () => {
    const elements = {
        typewriter: document.querySelector('.typewriter'),
        timeDisplay: document.getElementById('time'),
        dateDisplay: document.getElementById('date'),
        ipDisplay: document.getElementById('ip-address'),
        menuToggle: document.getElementById('menuToggle'),
        menuContent: document.getElementById('menuContent'),
        aside: document.querySelector('aside')
    };

    // Typewriter effect
    const typewriterText = "Creativity, curiosity and code . . .";
    let typewriterIndex = 0;

    function typeNextCharacter() {
        if (typewriterIndex === 0) {
            elements.typewriter.classList.add('visible');
        }
        if (typewriterIndex < typewriterText.length) {
            elements.typewriter.textContent += typewriterText[typewriterIndex++];
            setTimeout(typeNextCharacter, 100);
        } else {
            elements.typewriter.classList.add('finished');
        }
    }

    // Date and time display
    function updateDateTime() {
        const now = new Date();
        elements.timeDisplay.textContent = now.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit', hour12: true });
        elements.dateDisplay.textContent = now.toLocaleDateString('en-US', { day: 'numeric', month: 'long', year: 'numeric' });
    }

    // IP address fetch
    fetch('https://api.ipify.org?format=json')
        .then(response => response.json())
        .then(data => elements.ipDisplay.textContent = data.ip)
        .catch(error => {
            console.error('Error fetching IP:', error);
            elements.ipDisplay.textContent = 'Unable to fetch';
        });

    // Menu toggle
    elements.menuToggle.addEventListener('click', () => {
        elements.aside.classList.toggle('expanded');
        elements.menuContent.classList.toggle('hidden');
        
        if (elements.aside.classList.contains('expanded')) {
            setTimeout(() => elements.menuContent.classList.add('visible'), 300);
        } else {
            elements.menuContent.classList.remove('visible');
        }
    });

    // Initialize
    setTimeout(typeNextCharacter, 1000);
    updateDateTime();
    setInterval(updateDateTime, 60000);
});