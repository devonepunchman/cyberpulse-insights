#!/bin/bash

# Create post-container-security.html
cat > post-container-security.html << 'HTML'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Container Security Gaps - CyberPulse Insights</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        .post-content { max-width: 800px; margin: 0 auto; padding: var(--space-xl) 0; }
        .post-header { margin-bottom: var(--space-xl); border-bottom: 2px solid var(--dark-light); padding-bottom: var(--space-lg); }
        .post-title { font-size: 2.5rem; margin-bottom: var(--space-md); color: var(--light); }
        .post-meta { display: flex; gap: var(--space-md); flex-wrap: wrap; margin-bottom: var(--space-md); }
        .post-author { font-size: 1.1rem; color: var(--primary); display: flex; align-items: center; gap: var(--space-sm); }
        .post-body { line-height: 1.8; }
        .post-body h2 { margin-top: var(--space-xl); margin-bottom: var(--space-md); color: var(--primary); border-bottom: 1px solid var(--dark-light); padding-bottom: var(--space-sm); }
        .post-body h3 { margin-top: var(--space-lg); margin-bottom: var(--space-sm); color: var(--light); }
        .post-body p { margin-bottom: var(--space-md); color: var(--gray-light); }
        .post-body ul, .post-body ol { margin-bottom: var(--space-md); padding-left: var(--space-lg); color: var(--gray-light); }
        .post-body li { margin-bottom: var(--space-sm); }
        .code-block { background: var(--dark-light); border: 1px solid var(--gray); border-radius: var(--radius-md); padding: var(--space-md); margin: var(--space-md) 0; overflow-x: auto; font-family: 'JetBrains Mono', monospace; font-size: 0.9rem; }
        .code-block pre { margin: 0; color: var(--light); }
        .alert { background: var(--dark-light); border-left: 4px solid var(--danger); padding: var(--space-md); margin: var(--space-md) 0; border-radius: var(--radius-sm); }
        .alert.warning { border-left-color: var(--warning); }
        .alert.info { border-left-color: var(--primary); }
        .back-button { display: inline-flex; align-items: center; gap: var(--space-sm); margin-bottom: var(--space-xl); color: var(--primary); text-decoration: none; font-weight: 500; }
        .back-button:hover { color: var(--primary-dark); }
        @media (max-width: 768px) { .post-title { font-size: 2rem; } .post-meta { flex-direction: column; gap: var(--space-sm); } }
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
                    <span class="post-category cloud">Cloud</span>
                    <span class="read-time"><i class="far fa-clock"></i> 10 min read</span>
                </div>
                <h1 class="post-title">Container Security Gaps in Cloud-Native Deployments</h1>
                <div class="post-author"><i class="fas fa-user"></i> Dr. Sarah Johnson, Principal Security Researcher</div>
                <div class="post-tags">
                    <span class="tag">GCP</span><span class="tag">Threat Intelligence</span><span class="tag">Microsoft 365</span>
                    <span class="tag">Azure</span><span class="tag">Security</span><span class="tag">Container Security</span>
                </div>
            </div>
            
            <div class="post-body">
                <div class="alert">
                    <strong>Analysis of recent container security incidents</strong> reveals critical gaps in cloud-native deployments. Multiple vulnerabilities in container orchestration layers could enable privilege escalation and data exfiltration.
                </div>
                
                <h2>Executive Summary</h2>
                <p>Container security vulnerabilities in major cloud platforms have exposed critical gaps in cloud-native deployment security postures. This analysis covers recent incidents across AWS ECS, Google Kubernetes Engine, and Azure Container Instances.</p>
                
                <h2>Technical Findings</h2>
                <h3>Privilege Escalation Vulnerabilities</h3>
                <p>Multiple container runtime vulnerabilities allow attackers to break out of container isolation and gain host-level access:</p>
                
                <div class="code-block">
                    <pre># Example of vulnerable Docker configuration
FROM ubuntu:latest
USER root  # Running as root increases attack surface
COPY app /app
RUN chmod +x /app
CMD ["/app"]</pre>
                </div>
                
                <h3>Misconfigured Network Policies</h3>
                <p>Default network policies in Kubernetes clusters often allow excessive east-west traffic:</p>
                
                <div class="code-block">
                    <pre># Insecure default network policy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-all
spec:
  podSelector: {}
  ingress:
  - {}
  egress:
  - {}</pre>
                </div>
                
                <h2>Cloud Platform Specific Issues</h2>
                
                <h3>AWS ECS Security Gaps</h3>
                <ul>
                    <li>Task role permissions often overly permissive</li>
                    <li>Container insights logging disabled by default</li>
                    <li>Missing network isolation between tasks</li>
                </ul>
                
                <h3>Google Kubernetes Engine (GKE)</h3>
                <ul>
                    <li>Workload Identity misconfigurations</li>
                    <li>Binary Authorization not enforced</li>
                    <li>Node auto-upgrade disabled</li>
                </ul>
                
                <h3>Azure Container Instances</h3>
                <ul>
                    <li>Managed identity scope too broad</li>
                    <li>Container group network exposure</li>
                    <li>Log analytics integration gaps</li>
                </ul>
                
                <h2>Detection & Remediation</h2>
                
                <div class="code-block">
                    <pre># Scan for container vulnerabilities
docker scan my-container:latest
trivy image my-container:latest
grype my-container:latest</pre>
                </div>
                
                <div class="code-block">
                    <pre># Kubernetes security context best practices
apiVersion: v1
kind: Pod
metadata:
  name: security-context-demo
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: sec-ctx-demo
    image: nginx:latest
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: ["ALL"]</pre>
                </div>
                
                <h2>Training Implications</h2>
                
                <div class="alert warning">
                    <strong>Required Skills:</strong> Container security hardening, Kubernetes network policies, cloud-native security controls, runtime security monitoring.
                </div>
                
                <h3>Recommended Training:</h3>
                <ul>
                    <li><strong>Container Security Fundamentals:</strong> 8-hour course covering Docker and Kubernetes security</li>
                    <li><strong>Cloud-Native Security:</strong> Platform-specific security for AWS, GCP, and Azure</li>
                    <li><strong>DevSecOps for Containers:</strong> Integrating security into CI/CD pipelines</li>
                </ul>
                
                <div class="alert info">
                    <p><strong>About This Analysis:</strong> Prepared by CyberPulse Threat Intelligence Team. For container security training, visit our <a href="https://cyberpulse.ai/training">training programs</a>.</p>
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
</html>
HTML

echo "Created post-container-security.html"

# Create post-iam-misconfigurations.html
cat > post-iam-misconfigurations.html << 'HTML'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IAM Misconfigurations - CyberPulse Insights</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        .post-content { max-width: 800px; margin: 0 auto; padding: var(--space-xl) 0; }
        .post-header { margin-bottom: var(--space-xl); border-bottom: 2px solid var(--dark-light); padding-bottom: var(--space-lg); }
        .post-title { font-size: 2.5rem; margin-bottom: var(--space-md); color: var(--light); }
        .post-meta { display: flex; gap: var(--space-md); flex-wrap: wrap; margin-bottom: var(--space-md); }
        .post-author { font-size: 1.1rem; color: var(--primary); display: flex; align-items: center; gap: var(--space-sm); }
        .post-body { line-height: 1.8; }
        .post-body h2 { margin-top: var(--space-xl); margin-bottom: var(--space-md); color: var(--primary); border-bottom: 1px solid var(--dark-light); padding-bottom: var(--space-sm); }
        .post-body h3 { margin-top: var(--space-lg); margin-bottom: var(--space-sm); color: var(--light); }
        .post-body p { margin-bottom: var(--space-md); color: var(--gray-light); }
        .post-body ul, .post-body ol { margin-bottom: var(--space-md); padding-left: var(--space-lg); color: var(--gray-light); }
        .post-body li { margin-bottom: var(--space-sm); }
        .code-block { background: var(--dark-light); border: 1px solid var(--gray); border-radius: var(--radius-md); padding: var(--space-md); margin: var(--space-md) 0; overflow-x: auto; font-family: 'JetBrains Mono', monospace; font-size: 0.9rem; }
        .code-block pre { margin: 0; color: var(--light); }
        .alert { background: var(--dark-light); border-left: 4px solid var(--danger); padding: var(--space-md); margin: var(--space-md) 0; border-radius: var(--radius-sm); }
        .alert.warning { border-left-color: var(--warning); }
        .alert.info { border-left-color: var(--primary); }
        .back-button { display: inline-flex; align-items: center; gap: var(--space-sm); margin-bottom: var(--space-xl); color: var(--primary); text-decoration: none; font-weight: 500; }
        .back-button:hover { color: var(--primary-dark); }
        @media (max-width: 768px) { .post-title { font-size: 2rem; } .post-meta { flex-direction: column; gap: var(--space-sm); } }
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
                    <span class="post-category cloud">Cloud</span>
                    <span class="read-time"><i class="far fa-clock"></i> 8 min read</span>
                </div>
                <h1 class="post-title">IAM Misconfigurations in Azure Cause Breaches</h1>
                <div class="post-author"><i class="fas fa-user"></i> Marcus Rodriguez, Cloud Security Architect</div>
                <div class="post-tags">
                    <span class="tag">IAM</span><span class="tag">Threat Intelligence</span><span class="tag">Security</span>
                    <span class="tag">Cybersecurity</span><span class="tag">Azure</span><span class="tag">Identity Management</span>
                </div>
            </div>
            
            <div class="post-body">
                <div class="alert">
                    <strong>Recent security