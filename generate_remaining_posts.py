#!/usr/bin/env python3

posts = [
    {
        "filename": "post-container-security.html",
        "title": "Container Security Gaps in Cloud-Native Deployments",
        "category": "Cloud",
        "author": "Dr. Sarah Johnson, Principal Security Researcher",
        "read_time": 10,
        "tags": ["GCP", "Threat Intelligence", "Microsoft 365", "Azure", "Security", "Container Security"],
        "content": """
                <div class="alert">
                    <strong>Analysis of recent container security incidents</strong> reveals critical gaps in cloud-native deployments. Multiple vulnerabilities in container orchestration layers could enable privilege escalation and data exfiltration.
                </div>
                
                <h2>Executive Summary</h2>
                <p>Container security vulnerabilities in major cloud platforms have exposed critical gaps in cloud-native deployment security postures.</p>
                
                <h2>Technical Findings</h2>
                <h3>Privilege Escalation Vulnerabilities</h3>
                <p>Multiple container runtime vulnerabilities allow attackers to break out of container isolation.</p>
                
                <div class="code-block">
                    <pre># Example of vulnerable Docker configuration
FROM ubuntu:latest
USER root
COPY app /app
RUN chmod +x /app
CMD ["/app"]</pre>
                </div>
                
                <h2>Training Implications</h2>
                <div class="alert warning">
                    <strong>Required Skills:</strong> Container security hardening, Kubernetes network policies.
                </div>
        """
    },
    {
        "filename": "post-iam-misconfigurations.html",
        "title": "IAM Misconfigurations in Azure Cause Breaches",
        "category": "Cloud",
        "author": "Marcus Rodriguez, Cloud Security Architect",
        "read_time": 8,
        "tags": ["IAM", "Threat Intelligence", "Security", "Cybersecurity", "Azure", "Identity Management"],
        "content": """
                <div class="alert">
                    <strong>Recent security incidents</strong> highlight critical IAM misconfigurations in Azure deployments leading to data exposure.
                </div>
                
                <h2>Executive Summary</h2>
                <p>Identity and Access Management misconfigurations in Azure have led to multiple data breaches across organizations.</p>
                
                <h2>Common Misconfigurations</h2>
                <ul>
                    <li>Overly permissive role assignments</li>
                    <li>Missing conditional access policies</li>
                    <li>Inadequate privilege management</li>
                </ul>
                
                <div class="code-block">
                    <pre># Example of overly permissive role assignment
az role assignment create \\
  --assignee "user@company.com" \\
  --role "Owner" \\
  --scope "/subscriptions/{subscription-id}"</pre>
                </div>
                
                <h2>Training Implications</h2>
                <div class="alert warning">
                    <strong>Required Skills:</strong> Azure IAM, Privileged Identity Management, Conditional Access.
                </div>
        """
    },
    {
        "filename": "post-kubernetes-zero-day.html",
        "title": "Zero-Day in Major Cloud Provider's Container Service",
        "category": "Critical",
        "author": "Alex Chen, Senior Threat Intelligence Analyst",
        "read_time": 8,
        "tags": ["Kubernetes", "Cloud Security", "Zero-Day", "CVE-2026-1234", "Container Escape", "Privilege Escalation"],
        "content": """
                <div class="alert">
                    <strong>CVE-2026-1234</strong> - A critical vulnerability in Kubernetes orchestration layer allows privilege escalation and container escape.
                </div>
                
                <h2>Executive Summary</h2>
                <p>A zero-day vulnerability in Kubernetes affects all major cloud providers' managed services.</p>
                
                <h2>Technical Details</h2>
                <p>The vulnerability allows attackers to escape container isolation and gain host-level access.</p>
                
                <div class="code-block">
                    <pre># Proof of concept exploit
kubectl exec -it vulnerable-pod -- bash
# Exploit code here...</pre>
                </div>
                
                <h2>Affected Platforms</h2>
                <ul>
                    <li>Amazon EKS</li>
                    <li>Google GKE</li>
                    <li>Azure AKS</li>
                    <li>Self-managed Kubernetes</li>
                </ul>
                
                <h2>Training Implications</h2>
                <div class="alert warning">
                    <strong>Required Skills:</strong> Kubernetes security, container runtime security, vulnerability management.
                </div>
        """
    }
]

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - CyberPulse Insights</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        .post-content {{ max-width: 800px; margin: 0 auto; padding: var(--space-xl) 0; }}
        .post-header {{ margin-bottom: var(--space-xl); border-bottom: 2px solid var(--dark-light); padding-bottom: var(--space-lg); }}
        .post-title {{ font-size: 2.5rem; margin-bottom: var(--space-md); color: var(--light); }}
        .post-meta {{ display: flex; gap: var(--space-md); flex-wrap: wrap; margin-bottom: var(--space-md); }}
        .post-author {{ font-size: 1.1rem; color: var(--primary); display: flex; align-items: center; gap: var(--space-sm); }}
        .post-body {{ line-height: 1.8; }}
        .post-body h2 {{ margin-top: var(--space-xl); margin-bottom: var(--space-md); color: var(--primary); border-bottom: 1px solid var(--dark-light); padding-bottom: var(--space-sm); }}
        .post-body h3 {{ margin-top: var(--space-lg); margin-bottom: var(--space-sm); color: var(--light); }}
        .post-body p {{ margin-bottom: var(--space-md); color: var(--gray-light); }}
        .post-body ul, .post-body ol {{ margin-bottom: var(--space-md); padding-left: var(--space-lg); color: var(--gray-light); }}
        .post-body li {{ margin-bottom: var(--space-sm); }}
        .code-block {{ background: var(--dark-light); border: 1px solid var(--gray); border-radius: var(--radius-md); padding: var(--space-md); margin: var(--space-md) 0; overflow-x: auto; font-family: 'JetBrains Mono', monospace; font-size: 0.9rem; }}
        .code-block pre {{ margin: 0; color: var(--light); }}
        .alert {{ background: var(--dark-light); border-left: 4px solid var(--danger); padding: var(--space-md); margin: var(--space-md) 0; border-radius: var(--radius-sm); }}
        .alert.warning {{ border-left-color: var(--warning); }}
        .alert.info {{ border-left-color: var(--primary); }}
        .back-button {{ display: inline-flex; align-items: center; gap: var(--space-sm); margin-bottom: var(--space-xl); color: var(--primary); text-decoration: none; font-weight: 500; }}
        .back-button:hover {{ color: var(--primary-dark); }}
        @media (max-width: 768px) {{ .post-title {{ font-size: 2rem; }} .post-meta {{ flex-direction: column; gap: var(--space-sm); }} }}
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-brand">
                <a href="/">
                    <i class="fas fa-shield-alt"></i>
                    <span>CyberPulse <strong>Insights</strong></span>
                </a>
            </div>
            <button class="nav-toggle" aria-label="Toggle navigation"><i class="fas fa-bars"></i></button>
            <div class="nav-menu">
                <a href="/" class="nav-link"><i class="fas fa-home"></i> Home</a>
                <a href="/#threats" class="nav-link"><i class="fas fa-fire"></i> Threats</a>
                <a href="/#training" class="nav-link"><i class="fas fa-graduation-cap"></i> Training</a>
            </div>
        </div>
    </nav>

    <main class="container">
        <div class="post-content">
            <a href="/" class="back-button"><i class="fas fa-arrow-left"></i> Back to All Posts</a>
            <div class="post-header">
                <div class="post-meta">
                    <span class="post-date"><i class="far fa-calendar"></i> February 25, 2026</span>
                    <span class="post-category {category_lower}">{category}</span>
                    <span class="read-time"><i class="far fa-clock"></i> {read_time} min read</span>
                </div>
                <h1 class="post-title">{title}</h1>
                <div class="post-author"><i class="fas fa-user"></i> {author}</div>
                <div class="post-tags">
                    {tags_html}
                </div>
            </div>
            
            <div class="post-body">
                {content}
                
                <div class="alert info">
                    <p><strong>About This Analysis:</strong> Prepared by CyberPulse Threat Intelligence Team. For comprehensive security training, visit our <a href="https://cyberpulse.ai/training">training programs</a>.</p>
                    <p><em>Last Updated: 2026-02-25</em></p>
                </div>
            </div>
            
            <div style="margin-top: var(--space-xl); padding-top: var(--space-lg); border-top: 1px solid var(--dark-light);">
                <a href="/" class="back-button"><i class="fas fa-arrow-left"></i> Back to All Posts</a>
            </div>
        </div>
    </main>

    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-brand">
                    <i class="fas fa-shield-alt"></i>
                    <span>CyberPulse <strong>Insights</strong></span>
                    <p class="footer-tagline">Daily cybersecurity threat intelligence for security professionals.</p>
                </div>
                <div class="footer-links">
                    <div class="footer-column"><h4>Threat Categories</h4><a href="#">Critical Vulnerabilities</a><a href="#">Cloud Security</a><a href="#">Ransomware</a><a href="#">APT Groups</a></div>
                    <div class="footer-column"><h4>Resources</h4><a href="#">Threat Reports</a><a href="#">Detection Rules</a><a href="#">Incident Response</a><a href="#">Training Materials</a></div>
                    <div class="footer-column"><h4>Connect</h4><a href="#"><i class="fab fa-twitter"></i> Twitter</a><a href="#"><i class="fab fa-linkedin"></i> LinkedIn</a><a href="#"><i class="fab fa-github"></i> GitHub</a><a href="#"><i class="fas fa-envelope"></i> Newsletter</a></div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 CyberPulse Insights. All rights reserved. | <a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a></p>
                <p class="footer-note">This blog is updated daily with the latest cybersecurity threat intelligence.</p>
            </div>
        </div>
    </footer>
    <script src="js/main.js"></script>
</body>
</html>"""

for post in posts:
    tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in post["tags"]])
    category_lower = post["category"].lower()
    
    html = template.format(
        title=post["title"],
        category=post["category"],
        category_lower=category_lower,
        author=post["author"],
        read_time=post["read_time"],
        tags_html=tags_html,
        content=post["content"]
    )
    
    with open(post["filename"], "w") as f:
        f.write(html)
    
    print(f"Created {post['filename']}")

print("All post pages created successfully!")
