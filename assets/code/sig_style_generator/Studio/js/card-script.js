document.addEventListener('DOMContentLoaded', () => {
    const recipientNameEl = document.getElementById('cardRecipientName');
    const messageEl = document.getElementById('cardMessage');
    const senderNameEl = document.getElementById('cardSenderName');
    const animatedCard = document.getElementById('animatedCard');
    const stampEl = document.querySelector('.stamp');
    const cardDecorations = document.querySelectorAll('.card-decoration');
    const contentElements = [
        document.querySelector('.recipient-greeting'),
        document.querySelector('.card-message'),
        document.querySelector('.card-signature')
    ];

    // Get data from URL parameters
    const urlParams = new URLSearchParams(window.location.search);
    const to = urlParams.get('to') || 'Recipient';
    const msg = urlParams.get('msg') || 'A special message for you!';
    const from = urlParams.get('from') || 'A Friend';
    const template = urlParams.get('template') || 'default';

    // Populate the card
    recipientNameEl.textContent = to;
    messageEl.textContent = msg;
    senderNameEl.textContent = from;

    // Apply template class to body for specific styling
    document.body.classList.add(`template-${template}`);
    // If template is default, and you want a specific default style
    // if (template === 'default') document.body.classList.add('template-default-visual');

    // Animation with GSAP
    const tl = gsap.timeline();

    // Initial state (already set in CSS, but good for clarity if needed)
    // gsap.set(animatedCard, { scale: 0.8, rotationY: 15, rotationX:5, opacity: 0 });
    // gsap.set(contentElements, { opacity: 0, y: 20 });
    // gsap.set(stampEl, { scale: 0, rotation: 7, opacity: 0 });
    // gsap.set(cardDecorations, { opacity: 0 });

    tl.to(animatedCard, {
        duration: 1.2,
        scale: 1,
        rotationY: 0,
        rotationX: 0,
        opacity: 1,
        ease: "elastic.out(1, 0.75)"
    })
    .to(cardDecorations, {
        duration: 0.5,
        opacity: 1,
        stagger: 0.2,
        ease: "power2.inOut"
    }, "-=0.8") // Start this animation slightly before the card finishes its main animation
    .to(stampEl, {
        duration: 0.8,
        scale: 1,
        rotation: 7, // keep the slight tilt
        opacity: 1,
        ease: "elastic.out(1, 0.5)"
    }, "-=0.5") // Overlap with previous
    .to(contentElements, {
        duration: 0.7,
        opacity: 1,
        y: 0,
        stagger: 0.3, // Each element animates one after another
        ease: "power2.out"
    }, "-=0.4"); // Overlap slightly

    // Example of template-specific animation details (optional)
    if (template === 'birthday') {
        // Add a little confetti burst or sparkle effect if you have a particle library
        // For now, maybe a slight extra "pop" to the stamp
        tl.to(stampEl, { scale: 1.1, duration: 0.2, yoyo: true, repeat: 1, ease: "power1.inOut" }, "-=0.3");
    }
});