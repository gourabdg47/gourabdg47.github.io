// Testimonials data
const testimonials = [
    {
        content: "This quiz app helped me pass my Security+ exam on the first try! The questions are spot-on and the explanations are clear.",
        author: "Sarah K.",
        rating: 5
    },
    {
        content: "The practice questions are very similar to the actual exam. Great resource for preparation!",
        author: "Michael R.",
        rating: 4
    },
    {
        content: "I love how the questions are organized by domain. Makes it easy to focus on weak areas.",
        author: "David L.",
        rating: 5
    },
    {
        content: "The explanations after each question really help reinforce the concepts. Highly recommended!",
        author: "Jennifer M.",
        rating: 5
    },
    {
        content: "Perfect for last-minute review before the exam. The timer feature is especially helpful.",
        author: "Robert T.",
        rating: 5
    },
    {
        content: "Great resource for Security+ preparation. The questions are challenging but fair.",
        author: "Lisa P.",
        rating: 4
    },
    {
        content: "The domain-based organization makes it easy to track progress. Very well structured!",
        author: "James W.",
        rating: 4
    },
    {
        content: "I appreciate the detailed explanations. They help understand the concepts better.",
        author: "Emily S.",
        rating: 5
    },
    {
        content: "The practice mode is excellent for learning. Exam mode helps with time management.",
        author: "Thomas B.",
        rating: 4
    },
    {
        content: "Very comprehensive coverage of Security+ topics. A must-have study tool!",
        author: "Rachel H.",
        rating: 5
    },
    {
        content: "The questions are well-written and cover all the important topics.",
        author: "Daniel K.",
        rating: 4
    },
    {
        content: "Great for both beginners and those with some experience. Very helpful!",
        author: "Amanda R.",
        rating: 5
    },
    {
        content: "The explanations are clear and concise. Makes learning easier.",
        author: "Christopher M.",
        rating: 4
    },
    {
        content: "I like how the questions are updated regularly. Keeps the content fresh.",
        author: "Jessica L.",
        rating: 4
    },
    {
        content: "The interface is user-friendly and the questions are well-organized.",
        author: "Matthew S.",
        rating: 5
    },
    {
        content: "Good practice questions, though some could be more challenging.",
        author: "Nicole W.",
        rating: 4
    },
    {
        content: "Decent resource, but could use more questions in some domains.",
        author: "Kevin P.",
        rating: 4
    },
    {
        content: "The explanations are helpful, but some could be more detailed.",
        author: "Michelle B.",
        rating: 4
    },
    {
        content: "Some questions seem a bit basic, but overall good for practice.",
        author: "Andrew H.",
        rating: 3
    },
    {
        content: "The interface is good, but the question bank could be larger.",
        author: "Stephanie K.",
        rating: 3
    }
];

// Function to create star rating HTML
function createStarRating(rating) {
    let stars = '';
    for (let i = 1; i <= 5; i++) {
        stars += i <= rating ? '★' : '☆';
    }
    return stars;
}

// Function to create testimonial bubble
function createTestimonialBubble(testimonial) {
    const bubble = document.createElement('div');
    bubble.className = 'testimonial-bubble';
    bubble.innerHTML = `
        <div class="dismiss-btn" title="Dismiss">×</div>
        <div class="testimonial-content">${testimonial.content}</div>
        <div class="testimonial-author">${testimonial.author}</div>
        <div class="testimonial-rating">${createStarRating(testimonial.rating)}</div>
        <div class="testimonial-resources">
            <a href="https://buymeacoffee.com/gourabdg/e/420396" target="_blank" class="resource-link">
                Security+ Resources
                <span class="discount">30% OFF</span>
            </a>
        </div>
    `;

    // Add click event for dismiss button
    const dismissBtn = bubble.querySelector('.dismiss-btn');
    dismissBtn.addEventListener('click', () => {
        bubble.classList.add('hide');
        setTimeout(() => {
            if (bubble.parentNode) {
                bubble.remove();
                // Show next testimonial after 3 seconds
                setTimeout(showTestimonial, 3000);
            }
        }, 300);
    });

    // Add click event for the resource link
    const resourceLink = bubble.querySelector('.resource-link');
    if (resourceLink) {
        resourceLink.addEventListener('click', () => {
            if (typeof gtag === 'function') {
                gtag('event', 'click', {
                    'event_category': 'Resources',
                    'event_label': 'Access Security+ Resources Notification'
                });
            }
        });
    }

    return bubble;
}

// Function to show testimonial
function showTestimonial() {
    const container = document.querySelector('.testimonial-container');
    if (!container) return;

    // Check if there's already a testimonial showing
    const existingBubble = container.querySelector('.testimonial-bubble');
    if (existingBubble) {
        return; // Don't show a new one if there's already one visible
    }

    // Get random testimonial
    const testimonial = testimonials[Math.floor(Math.random() * testimonials.length)];
    const bubble = createTestimonialBubble(testimonial);
    container.appendChild(bubble);

    // Set timeout for next testimonial only if not dismissed
    const minTime = 60000; // 1 minute
    const maxTime = 300000; // 5 minutes
    const nextTime = Math.floor(Math.random() * (maxTime - minTime + 1)) + minTime;
    
    // Store the timeout ID on the bubble element
    bubble.timeoutId = setTimeout(() => {
        // Only show next testimonial if this one is still the last one
        if (container.lastChild === bubble) {
            bubble.classList.add('hide');
            setTimeout(() => {
                if (container.lastChild === bubble) {
                    bubble.remove();
                    // Show next testimonial after 3 seconds
                    setTimeout(showTestimonial, 3000);
                }
            }, 300);
        }
    }, nextTime);

    // Clear the timeout if the bubble is dismissed
    bubble.addEventListener('remove', () => {
        if (bubble.timeoutId) {
            clearTimeout(bubble.timeoutId);
        }
    });
}

// Initialize testimonials when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Create testimonial container
    const container = document.createElement('div');
    container.className = 'testimonial-container';
    // document.body.appendChild(container); // Commented out to temporarily disable notifications

    // Start showing testimonials
    // showTestimonial(); // Also comment out the call to showTestimonial()
}); 