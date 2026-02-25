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
    
    // Load blog posts
    loadBlogPosts();
    
    // Initialize animations
    initAnimations();
});

// Load blog posts from JSON file
async function loadBlogPosts() {
    const postsContainer = document.getElementById('posts-container');
    
    if (!postsContainer) return;
    
    try {
        // In a real implementation, this would fetch from a JSON API
        // For now, we'll use sample data
        const posts = await getSamplePosts();
        
        postsContainer.innerHTML = '';
        
        posts.forEach(post => {
            const postElement = createPostElement(post);
            postsContainer.appendChild(postElement);
        });
        
    } catch (error) {
        console.error('Error loading posts:', error);
        postsContainer.innerHTML = `
            <div class="error">
                <i class="fas fa-exclamation-triangle"></i>
                <p>Unable to load posts. Please try again later.</p>
            </div>
        `;
    }
}

// Sample blog posts data
async function getSamplePosts() {
    // This would normally fetch from an API
    // For now, return sample data
    return [
        {
            id: 1,
            date: '2026-02-21',
            category: 'Critical',
            title: 'Zero-Day in Major Cloud Provider\'s Container Service',
            excerpt: 'A critical vulnerability (CVE-2026-1234) in Kubernetes orchestration layer allows privilege escalation and container escape. Patch immediately.',
            tags: ['Kubernetes', 'Cloud', 'Zero-Day', 'CVE-2026-1234'],
            readTime: '5 min'
        },
        {
            id: 2,
            date: '2026-02-20',
            category: 'Ransomware',
            title: 'New Ransomware-as-a-Service Targets Healthcare Sector',
            excerpt: 'MedLock ransomware group using novel encryption methods and threatening patient data exposure. Defense strategies and IOCs included.',
            tags: ['Ransomware', 'Healthcare', 'IOCs', 'Threat Hunting'],
            readTime: '7 min'
        },
        {
            id: 3,
            date: '2026-02-19',
            category: 'APT',
            title: 'APT29 Exploits Microsoft Exchange Vulnerabilities',
            excerpt: 'Nation-state actors using chained exploits to maintain persistence in enterprise networks. Detection rules and mitigation steps.',
            tags: ['APT29', 'Microsoft', 'Exchange', 'Nation-State'],
            readTime: '8 min'
        },
        {
            id: 4,
            date: '2026-02-18',
            category: 'AI Security',
            title: 'Adversarial Attacks on LLM-Based Security Tools',
            excerpt: 'Research shows how carefully crafted prompts can bypass AI-powered security scanners. Implications for ML-based defense systems.',
            tags: ['AI', 'LLM', 'Adversarial', 'Research'],
            readTime: '6 min'
        },
        {
            id: 5,
            date: '2026-02-17',
            category: 'IoT',
            title: 'Critical Flaws in Industrial PLCs Allow Remote Takeover',
            excerpt: 'Multiple vulnerabilities in Programmable Logic Controllers could enable physical damage to critical infrastructure.',
            tags: ['IoT', 'OT', 'PLC', 'Critical Infrastructure'],
            readTime: '9 min'
        },
        {
            id: 6,
            date: '2026-02-16',
            category: 'Cloud',
            title: 'AWS IAM Misconfigurations Lead to Data Breaches',
            excerpt: 'Analysis of recent cloud security incidents shows common IAM mistakes and how to implement least-privilege access.',
            tags: ['AWS', 'Cloud', 'IAM', 'Best Practices'],
            readTime: '4 min'
        }
    ];
}

// Create post element
function createPostElement(post) {
    const article = document.createElement('article');
    article.className = 'post-card';
    
    // Determine category color
    const categoryClass = getCategoryClass(post.category);
    
    article.innerHTML = `
        <div class="post-header">
            <div class="post-meta">
                <span class="post-date">
                    <i class="far fa-calendar"></i> ${formatDate(post.date)}
                </span>
                <span class="post-category ${categoryClass}">
                    ${post.category}
                </span>
            </div>
            <h3 class="post-title">${post.title}</h3>
            <p class="post-excerpt">${post.excerpt}</p>
        </div>
        <div class="post-footer">
            <div class="post-tags">
                ${post.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
            </div>
            <a href="#" class="read-more">
                Read Analysis <i class="fas fa-arrow-right"></i>
            </a>
        </div>
    `;
    
    return article;
}

// Get CSS class for category
function getCategoryClass(category) {
    const classes = {
        'Critical': 'critical',
        'Ransomware': 'ransomware',
        'APT': 'apt',
        'AI Security': 'ai',
        'IoT': 'iot',
        'Cloud': 'cloud'
    };
    
    return classes[category] || 'critical';
}

// Format date
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
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
    .post-card:nth-child(5) { transition-delay: 0.5s; }
    .post-card:nth-child(6) { transition-delay: 0.6s; }
    
    .error {
        text-align: center;
        padding: var(--space-xl);
        color: var(--danger);
    }
    
    .error i {
        font-size: 3rem;
        margin-bottom: var(--space-md);
    }
`;
document.head.appendChild(style);