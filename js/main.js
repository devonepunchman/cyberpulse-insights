// CyberPulse Insights - Main JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Mobile Navigation Toggle
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (navToggle) {
        navToggle.addEventListener('click', function() {
            navMenu.style.display = navMenu.style.display === 'flex' ? 'none' : 'flex';
        });
        
        // Handle window resize
        window.addEventListener('resize', function() {
            if (window.innerWidth > 768) {
                navMenu.style.display = 'flex';
            } else {
                navMenu.style.display = 'none';
            }
        });
    }
    
    // Initialize animations
    initAnimations();
});

// Initialize animations
function initAnimations() {
    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);
    
    // Observe elements
    document.querySelectorAll('.post-card, .category-card, .training-cta').forEach(el => {
        observer.observe(el);
    });
}

// Add CSS for animations
const style = document.createElement('style');
style.textContent = `
    .post-card, .category-card, .training-cta {
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s ease, transform 0.6s ease;
    }
    
    .post-card.animate-in, 
    .category-card.animate-in, 
    .training-cta.animate-in {
        opacity: 1;
        transform: translateY(0);
    }
    
    .post-card:nth-child(1) { transition-delay: 0.1s; }
    .post-card:nth-child(2) { transition-delay: 0.2s; }
    .post-card:nth-child(3) { transition-delay: 0.3s; }
    .post-card:nth-child(4) { transition-delay: 0.4s; }
    
    .error {
        text-align: center;
        padding: var(--space-xl);
        color: var(--danger);
    }
    
    .error i {
        font-size: 3rem;
        margin-bottom: var(--space-md);
    }
    
    .post-author {
        color: var(--gray);
        font-size: 0.9rem;
        margin-top: var(--space-sm);
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .post-author i {
        color: var(--primary);
    }
    
    .post-meta-right {
        display: flex;
        align-items: center;
        gap: var(--space-md);
    }
    
    .read-time {
        color: var(--gray);
        font-size: 0.875rem;
        display: flex;
        align-items: center;
        gap: 0.25rem;
    }
    
    .read-time i {
        color: var(--primary);
    }
    
    @media (max-width: 768px) {
        .post-meta-right {
            flex-direction: column;
            align-items: flex-start;
            gap: var(--space-sm);
        }
    }
`;
document.head.appendChild(style);