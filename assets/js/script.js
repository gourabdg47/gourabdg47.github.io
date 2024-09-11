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

    // Menu toggle
    elements.menuToggle.addEventListener('click', () => {
        elements.menuContent.classList.toggle('hidden');
        elements.aside.classList.toggle('expanded');
    });

    // Initialize
    typeNextCharacter();
    updateDateTime();
    setInterval(updateDateTime, 1000);
});