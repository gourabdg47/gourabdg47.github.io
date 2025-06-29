// Zenith Health - Main JavaScript File

// DOM Elements
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');
const donationModal = document.getElementById('donation-modal');
const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');
const navLinks = document.querySelectorAll('.nav-link');

// Initialize application
document.addEventListener('DOMContentLoaded', function() {
    initializeScrollAnimations();
    initializeSmoothScroll();
    initializeMobileMenu();
    initializeNavigation();
    initializeModal();
    
    // Add loading animation completion
    setTimeout(() => {
        document.body.classList.add('loaded');
    }, 500);
});

// Mobile Menu Functionality
function initializeMobileMenu() {
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', toggleMobileMenu);
        
        // Close mobile menu when clicking on links
        mobileNavLinks.forEach(link => {
            link.addEventListener('click', closeMobileMenu);
        });
        
        // Close mobile menu when clicking outside
        mobileMenu.addEventListener('click', (e) => {
            if (e.target === mobileMenu) {
                closeMobileMenu();
            }
        });
        
        // Close mobile menu on escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && !mobileMenu.classList.contains('translate-x-full')) {
                closeMobileMenu();
            }
        });
    }
}

function toggleMobileMenu() {
    const icon = mobileMenuBtn.querySelector('i');
    
    if (mobileMenu.classList.contains('translate-x-full')) {
        mobileMenu.classList.remove('translate-x-full');
        mobileMenu.classList.add('translate-x-0');
        icon.classList.remove('fa-bars');
        icon.classList.add('fa-times');
        document.body.style.overflow = 'hidden';
    } else {
        closeMobileMenu();
    }
}

function closeMobileMenu() {
    const icon = mobileMenuBtn.querySelector('i');
    mobileMenu.classList.remove('translate-x-0');
    mobileMenu.classList.add('translate-x-full');
    icon.classList.remove('fa-times');
    icon.classList.add('fa-bars');
    document.body.style.overflow = '';
}

// Smooth Scrolling
function initializeSmoothScroll() {
    // Handle all navigation links
    const allNavLinks = [...navLinks, ...mobileNavLinks];
    
    allNavLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            if (href.startsWith('#')) {
                e.preventDefault();
                const targetId = href.substring(1);
                const targetElement = document.getElementById(targetId);
                
                if (targetElement) {
                    const headerOffset = 80;
                    const elementPosition = targetElement.offsetTop;
                    const offsetPosition = elementPosition - headerOffset;
                    
                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });
                    
                    // Close mobile menu if open
                    if (!mobileMenu.classList.contains('translate-x-full')) {
                        closeMobileMenu();
                    }
                }
            }
        });
    });
}

// Navigation Active State
function initializeNavigation() {
    const sections = document.querySelectorAll('section[id]');
    
    function updateActiveNavigation() {
        const scrollPosition = window.scrollY + 100;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                // Remove active class from all nav links
                navLinks.forEach(link => link.classList.remove('active'));
                mobileNavLinks.forEach(link => link.classList.remove('active'));
                
                // Add active class to current section link
                const activeNavLink = document.querySelector(`.nav-link[href="#${sectionId}"]`);
                const activeMobileLink = document.querySelector(`.mobile-nav-link[href="#${sectionId}"]`);
                
                if (activeNavLink) activeNavLink.classList.add('active');
                if (activeMobileLink) activeMobileLink.classList.add('active');
            }
        });
    }
    
    // Throttled scroll listener
    let ticking = false;
    window.addEventListener('scroll', () => {
        if (!ticking) {
            requestAnimationFrame(() => {
                updateActiveNavigation();
                ticking = false;
            });
            ticking = true;
        }
    });
}

// Scroll Animations
function initializeScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                
                // Add staggered animation for child elements
                const children = entry.target.querySelectorAll('.fade-in-up');
                children.forEach((child, index) => {
                    setTimeout(() => {
                        child.style.opacity = '1';
                        child.style.transform = 'translateY(0)';
                    }, index * 100);
                });
            }
        });
    }, observerOptions);
    
    // Observe all sections and animated elements
    const animatedElements = document.querySelectorAll('.fade-in-up, section');
    animatedElements.forEach(element => {
        observer.observe(element);
        element.classList.add('scroll-reveal');
    });
}

// Modal Functionality
function initializeModal() {
    if (donationModal) {
        donationModal.addEventListener('click', (e) => {
            if (e.target === donationModal) {
                hideDonationModal();
            }
        });
        
        // Close modal on escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && !donationModal.classList.contains('hidden')) {
                hideDonationModal();
            }
        });
    }
}

// Modal Functions (called from HTML)
function showDonationModal() {
    if (donationModal) {
        donationModal.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
        
        // Focus management for accessibility
        const firstFocusable = donationModal.querySelector('button');
        if (firstFocusable) {
            firstFocusable.focus();
        }
    }
}

function hideDonationModal() {
    if (donationModal) {
        donationModal.classList.add('hidden');
        document.body.style.overflow = '';
    }
}

// Utility Functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Performance Monitoring
function trackPagePerformance() {
    if ('performance' in window) {
        window.addEventListener('load', () => {
            const perfData = performance.getEntriesByType('navigation')[0];
            console.log('Page Load Time:', perfData.loadEventEnd - perfData.loadEventStart + 'ms');
        });
    }
}

// Error Handling
window.addEventListener('error', function(e) {
    console.error('JavaScript Error:', e.error);
    // In production, you might want to send this to an error tracking service
});

window.addEventListener('unhandledrejection', function(e) {
    console.error('Unhandled Promise Rejection:', e.reason);
    e.preventDefault();
});

// Accessibility Enhancements
function initializeAccessibility() {
    // Skip to main content link
    const skipLink = document.createElement('a');
    skipLink.href = '#main';
    skipLink.textContent = 'Skip to main content';
    skipLink.className = 'sr-only focus:not-sr-only focus:absolute focus:top-0 focus:left-0 bg-calm-blue text-white p-2 z-50';
    document.body.insertBefore(skipLink, document.body.firstChild);
    
    // Keyboard navigation for Discord button
    const discordButton = document.querySelector('.btn-discord');
    if (discordButton) {
        discordButton.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                discordButton.click();
            }
        });
    }
    
    // Announce route changes to screen readers
    const announcer = document.createElement('div');
    announcer.setAttribute('aria-live', 'polite');
    announcer.setAttribute('aria-atomic', 'true');
    announcer.className = 'sr-only';
    document.body.appendChild(announcer);
    
    // Update announcer when sections come into view
    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const sectionTitle = entry.target.querySelector('h2');
                if (sectionTitle) {
                    announcer.textContent = `Now viewing: ${sectionTitle.textContent}`;
                }
            }
        });
    }, { threshold: 0.5 });
    
    document.querySelectorAll('section[id]').forEach(section => {
        sectionObserver.observe(section);
    });
}

// Initialize accessibility features
document.addEventListener('DOMContentLoaded', initializeAccessibility);

// Analytics (placeholder for future implementation)
function trackEvent(eventName, properties = {}) {
    // Placeholder for analytics tracking
    console.log('Event:', eventName, properties);
}

// Track important user interactions
document.addEventListener('click', (e) => {
    if (e.target.matches('.btn-discord')) {
        trackEvent('discord_join_clicked');
    }
    if (e.target.matches('.btn-primary')) {
        trackEvent('cta_button_clicked', { text: e.target.textContent.trim() });
    }
});

// Service Worker Registration (for future PWA capabilities)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        // Placeholder for service worker registration
        console.log('Service Worker support detected');
    });
}

// Initialize performance tracking
trackPagePerformance();

// Export functions for testing (if needed)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        showDonationModal,
        hideDonationModal,
        toggleMobileMenu,
        closeMobileMenu
    };
}
