// CyberPulse Insights - Main JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Mobile Navigation Toggle
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            navToggle.innerHTML = navMenu.classList.contains('active') 
                ? '<i class="fas fa-times"></i>' 
                : '<i class="fas fa-bars"></i>';
        });
        
        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!navMenu.contains(event.target) && !navToggle.contains(event.target)) {
                navMenu.classList.remove('active');
                navToggle.innerHTML = '<i class="fas fa-bars"></i>';
            }
        });
        
        // Close mobile menu when clicking a link
        navMenu.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
                navToggle.innerHTML = '<i class="fas fa-bars"></i>';
            });
        });
        
        // Handle window resize
        window.addEventListener('resize', function() {
            if (window.innerWidth > 768) {
                navMenu.classList.remove('active');
                navToggle.innerHTML = '<i class="fas fa-bars"></i>';
            }
        });
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Only handle anchor links (not external links)
            if (href.startsWith('#') && href.length > 1) {
                e.preventDefault();
                const targetId = href.substring(1);
                const targetElement = document.getElementById(targetId);
                
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 80,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
    
    // Initialize animations
    initAnimations();
    
    // Add active class to current nav link
    updateActiveNavLink();
    
    // Add scroll effect to navbar
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.style.boxShadow = '0 4px 30px rgba(0, 0, 0, 0.5)';
            navbar.style.backdropFilter = 'blur(30px) saturate(200%)';
        } else {
            navbar.style.boxShadow = '0 4px 30px rgba(0, 0, 0, 0.3)';
            navbar.style.backdropFilter = 'blur(20px) saturate(180%)';
        }
    });
});

// Update active navigation link based on scroll position
function updateActiveNavLink() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link[href^="#"]');
    
    window.addEventListener('scroll', function() {
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            
            if (scrollY >= (sectionTop - 150)) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });
}

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
    document.querySelectorAll('.post-card, .category-card, .training-cta, .stat').forEach(el => {
        observer.observe(el);
    });
}

// Add CSS for animations
const style = document.createElement('style');
style.textContent = `
    /* Scroll animations */
    .post-card, .category-card, .training-cta, .stat {
        opacity: 0;
        transform: translateY(30px);
        transition: opacity 0.6s ease, transform 0.6s ease;
    }
    
    .post-card.animate-in, 
    .category-card.animate-in, 
    .training-cta.animate-in,
    .stat.animate-in {
        opacity: 1;
        transform: translateY(0);
    }
    
    /* Staggered animation delays */
    .post-card:nth-child(1) { transition-delay: 0.1s; }
    .post-card:nth-child(2) { transition-delay: 0.2s; }
    .post-card:nth-child(3) { transition-delay: 0.3s; }
    .post-card:nth-child(4) { transition-delay: 0.4s; }
    
    .stat:nth-child(1) { transition-delay: 0.1s; }
    .stat:nth-child(2) { transition-delay: 0.2s; }
    .stat:nth-child(3) { transition-delay: 0.3s; }
    
    /* Hero title animation */
    .hero-title {
        animation: fadeInUp 1s ease forwards;
    }
    
    .hero-subtitle {
        animation: fadeInUp 1s ease 0.3s forwards;
        opacity: 0;
    }
    
    .hero-stats {
        animation: fadeInUp 1s ease 0.6s forwards;
        opacity: 0;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Post title hover effect enhancement */
    .post-title a {
        position: relative;
        display: inline-block;
    }
    
    .post-title a:hover {
        transform: translateX(5px);
        transition: transform 0.3s ease;
    }
    
    /* Loading state for images */
    .post-card img {
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .post-card img.loaded {
        opacity: 1;
    }
    
    /* Error states */
    .error {
        text-align: center;
        padding: var(--space-xl);
        color: var(--danger);
        background: rgba(239, 68, 68, 0.1);
        border-radius: var(--radius-lg);
        border: 1px solid rgba(239, 68, 68, 0.2);
    }
    
    .error i {
        font-size: 3rem;
        margin-bottom: var(--space-md);
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .post-meta-right {
            flex-direction: column;
            align-items: flex-start;
            gap: var(--space-sm);
        }
        
        .hero-title {
            font-size: 2.5rem;
        }
        
        .hero-subtitle {
            font-size: 1.1rem;
        }
        
        .stat {
            min-width: 120px;
            padding: var(--space-md);
        }
        
        .stat-number {
            font-size: 2rem;
        }
    }
    
    @media (max-width: 480px) {
        .hero-title {
            font-size: 2rem;
        }
        
        .hero-subtitle {
            font-size: 1rem;
        }
        
        .hero-stats {
            flex-direction: column;
            gap: var(--space-md);
        }
        
        .stat {
            width: 100%;
            max-width: 200px;
        }
    }
`;
document.head.appendChild(style);