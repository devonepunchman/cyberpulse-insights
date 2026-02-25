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
        // Load posts from index.json
        const response = await fetch('posts/index.json');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        const posts = data.posts;
        
        postsContainer.innerHTML = '';
        
        // Display posts (limit to 6 most recent)
        posts.slice(0, 6).forEach(post => {
            const postElement = createPostElement(post);
            postsContainer.appendChild(postElement);
        });
        
        // Update stats if they exist
        updateStats(data);
        
    } catch (error) {
        console.error('Error loading posts:', error);
        
        // Fallback to sample data
        const posts = await getSamplePosts();
        postsContainer.innerHTML = '';
        
        posts.forEach(post => {
            const postElement = createPostElement(post);
            postsContainer.appendChild(postElement);
        });
    }
}

// Sample blog posts data (fallback)
async function getSamplePosts() {
    return [
        {
            id: 1,
            date: '2026-02-25',
            category: 'Critical',
            title: 'Critical Supply Chain Attack Targets Major Software Package Repositories',
            excerpt: 'A sophisticated supply chain attack targeting npm, PyPI, and RubyGems repositories has been discovered, affecting thousands of organizations.',
            tags: ['Supply Chain', 'npm', 'PyPI', 'Zero-Day', 'CVE-2026-2156'],
            read_time: 9,
            author: 'Alex Chen, Senior Threat Intelligence Analyst'
        },
        {
            id: 2,
            date: '2026-02-25',
            category: 'Cloud',
            title: 'Container Security Gaps in Cloud-Native Deployments',
            excerpt: 'Analysis of recent container security incidents reveals critical gaps in cloud-native deployments.',
            tags: ['GCP', 'Threat Intelligence', 'Microsoft 365', 'Azure', 'Security'],
            read_time: 10,
            author: 'Dr. Sarah Johnson, Principal Security Researcher'
        },
        {
            id: 3,
            date: '2026-02-25',
            category: 'Cloud',
            title: 'IAM Misconfigurations in Azure Cause Breaches',
            excerpt: 'Recent security incidents highlight critical IAM misconfigurations in Azure deployments.',
            tags: ['IAM', 'Threat Intelligence', 'Security', 'Cybersecurity', 'Azure'],
            read_time: 8,
            author: 'Marcus Rodriguez, Cloud Security Architect'
        },
        {
            id: 4,
            date: '2026-02-21',
            category: 'Critical',
            title: 'Zero-Day in Major Cloud Provider\'s Container Service',
            excerpt: 'A critical vulnerability in Kubernetes orchestration layer allows privilege escalation and container escape.',
            tags: ['Kubernetes', 'Cloud', 'Zero-Day', 'CVE-2026-1234'],
            read_time: 8,
            author: 'Alex Chen, Senior Threat Intelligence Analyst'
        },
        {
            id: 5,
            date: '2026-02-20',
            category: 'Ransomware',
            title: 'New Ransomware-as-a-Service Targets Healthcare Sector',
            excerpt: 'MedLock ransomware group using novel encryption methods and threatening patient data exposure.',
            tags: ['Ransomware', 'Healthcare', 'IOCs', 'Threat Hunting'],
            read_time: 7,
            author: 'Dr. Elena Petrova, Malware Analysis Lead'
        },
        {
            id: 6,
            date: '2026-02-19',
            category: 'APT',
            title: 'APT29 Exploits Microsoft Exchange Vulnerabilities',
            excerpt: 'Nation-state actors using chained exploits to maintain persistence in enterprise networks.',
            tags: ['APT29', 'Microsoft', 'Exchange', 'Nation-State'],
            read_time: 8,
            author: 'James Wilson, Incident Response Director'
        }
    ];
}

// Create post element
function createPostElement(post) {
    const article = document.createElement('article');
    article.className = 'post-card';
    
    // Determine category color
    const categoryClass = getCategoryClass(post.category);
    
    // Format date
    const formattedDate = formatDate(post.date);
    
    // Create tags HTML
    const tagsHtml = post.tags ? post.tags.map(tag => `<span class="tag">${tag}</span>`).join('') : '';
    
    article.innerHTML = `
        <div class="post-header">
            <div class="post-meta">
                <span class="post-date">
                    <i class="far fa-calendar"></i> ${formattedDate}
                </span>
                <span class="post-category ${categoryClass}">
                    ${post.category}
                </span>
            </div>
            <h3 class="post-title">${post.title}</h3>
            <p class="post-excerpt">${post.excerpt}</p>
            ${post.author ? `<p class="post-author"><i class="fas fa-user"></i> ${post.author}</p>` : ''}
        </div>
        <div class="post-footer">
            <div class="post-tags">
                ${tagsHtml}
            </div>
            <div class="post-meta-right">
                <span class="read-time">
                    <i class="far fa-clock"></i> ${post.read_time || 5} min read
                </span>
                <a href="#" class="read-more" data-post-id="${post.id}">
                    Read Analysis <i class="fas fa-arrow-right"></i>
                </a>
            </div>
        </div>
    `;
    
    // Add click handler for read more
    const readMoreBtn = article.querySelector('.read-more');
    if (readMoreBtn) {
        readMoreBtn.addEventListener('click', function(e) {
            e.preventDefault();
            showPostDetail(post);
        });
    }
    
    return article;
}

// Show post detail (simplified - in real implementation would load full post)
function showPostDetail(post) {
    alert(`Loading: ${post.title}\n\nThis would show the full blog post in a real implementation.`);
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
    try {
        const date = new Date(dateString);
        return date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    } catch (e) {
        return dateString;
    }
}

// Update stats from data
function updateStats(data) {
    const stats = document.querySelectorAll('.stat-number');
    if (stats.length >= 3 && data) {
        // Update threats tracked
        if (stats[0]) stats[0].textContent = data.total_posts || '4+';
        
        // Update CVEs analyzed (estimate based on critical posts)
        const criticalCount = data.categories?.Critical || 2;
        if (stats[1]) stats[1].textContent = criticalCount * 2; // Each critical post analyzes ~2 CVEs
        
        // Update security pros (placeholder)
        if (stats[2]) stats[2].textContent = '5.2k';
    }
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