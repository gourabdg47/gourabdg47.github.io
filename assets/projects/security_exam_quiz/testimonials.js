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
            <a href="" target="_blank" class="resource-link">
                Security+ Resources
                <span class="discount">Get Exam Ready for $13!</span>
            </a>
        </div>
    `;
}