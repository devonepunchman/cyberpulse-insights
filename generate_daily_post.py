#!/usr/bin/env python3
"""
Daily Cybersecurity Blog Post Generator
Automatically generates professional cybersecurity threat intelligence posts
"""

import json
import yaml
import markdown
from datetime import datetime, timedelta
import random
import os
from pathlib import Path

class CybersecurityBlogGenerator:
    def __init__(self):
        self.categories = [
            "Critical", "Ransomware", "APT", "Cloud", "IoT", "AI Security",
            "Supply Chain", "Mobile", "Web", "Identity"
        ]
        
        self.threat_actors = [
            "APT29 (Cozy Bear)", "APT28 (Fancy Bear)", "Lazarus Group",
            "FIN7", "REvil", "Conti", "LockBit", "BlackCat",
            "Scattered Spider", "UNC4844"
        ]
        
        self.technologies = [
            "Kubernetes", "Docker", "AWS", "Azure", "GCP",
            "Microsoft 365", "Okta", "CrowdStrike", "Splunk",
            "Elastic", "GitLab", "Jenkins", "Terraform"
        ]
        
        self.vulnerability_types = [
            "Zero-Day", "Privilege Escalation", "RCE", "SSRF",
            "XXE", "SQLi", "XSS", "CSRF", "Deserialization",
            "Memory Corruption", "Logic Bug"
        ]
        
    def generate_daily_post(self):
        """Generate a daily cybersecurity blog post"""
        today = datetime.now()
        
        # Select random category (weighted toward critical)
        category_weights = [0.3, 0.2, 0.15, 0.1, 0.08, 0.07, 0.05, 0.02, 0.02, 0.01]
        category = random.choices(self.categories, weights=category_weights)[0]
        
        # Generate CVE-like identifier
        year = today.year
        cve_id = f"CVE-{year}-{random.randint(1000, 9999)}"
        
        # Generate post data
        post_data = {
            "title": self.generate_title(category, cve_id),
            "date": today.strftime("%Y-%m-%d"),
            "author": self.generate_author(),
            "category": category,
            "tags": self.generate_tags(category),
            "excerpt": self.generate_excerpt(category, cve_id),
            "read_time": random.randint(4, 12),
            "content": self.generate_content(category, cve_id, today)
        }
        
        return post_data
    
    def generate_title(self, category, cve_id):
        """Generate a compelling blog post title"""
        templates = {
            "Critical": [
                f"Critical {cve_id} Vulnerability in {random.choice(self.technologies)}: Immediate Action Required",
                f"Zero-Day Exploit Targeting {random.choice(['Financial', 'Healthcare', 'Government'])} Sector",
                f"Emergency Patch Released for {cve_id} in {random.choice(self.technologies)}"
            ],
            "Ransomware": [
                f"New Ransomware Variant Targets {random.choice(self.technologies)} Deployments",
                f"Ransomware-as-a-Service Campaign Using Novel Encryption Methods",
                f"Double Extortion Tactics Evolve in Latest Ransomware Attacks"
            ],
            "APT": [
                f"{random.choice(self.threat_actors)} Exploits {random.choice(self.technologies)} Vulnerabilities",
                f"Nation-State Actor Campaign Targets Critical Infrastructure",
                f"Advanced Persistence Techniques in Latest APT Campaign"
            ],
            "Cloud": [
                f"Cloud Configuration Vulnerabilities Lead to Data Exposure",
                f"IAM Misconfigurations in {random.choice(['AWS', 'Azure', 'GCP'])} Cause Breaches",
                f"Container Security Gaps in Cloud-Native Deployments"
            ]
        }
        
        # Default template if category not in templates
        if category in templates:
            return random.choice(templates[category])
        else:
            return f"Security Analysis: {category} Threats and Mitigation Strategies"
    
    def generate_author(self):
        """Generate author name"""
        authors = [
            "Alex Chen, Senior Threat Intelligence Analyst",
            "Dr. Sarah Johnson, Principal Security Researcher",
            "Marcus Rodriguez, Cloud Security Architect",
            "Dr. Elena Petrova, Malware Analysis Lead",
            "James Wilson, Incident Response Director"
        ]
        return random.choice(authors)
    
    def generate_tags(self, category):
        """Generate relevant tags"""
        base_tags = ["Security", "Threat Intelligence", "Cybersecurity"]
        
        category_tags = {
            "Critical": ["Zero-Day", "Patch", "Emergency", "CVE"],
            "Ransomware": ["Encryption", "Extortion", "IOCs", "Decryption"],
            "APT": ["Nation-State", "Espionage", "TTPs", "Attribution"],
            "Cloud": ["AWS", "Azure", "GCP", "IAM", "Configuration"],
            "IoT": ["OT", "ICS", "Embedded", "Hardware"],
            "AI Security": ["Machine Learning", "LLM", "Adversarial", "Bias"]
        }
        
        tags = base_tags + category_tags.get(category, [category])
        tags.extend(random.sample(self.technologies, 2))
        
        # Ensure unique tags
        return list(set(tags))[:8]
    
    def generate_excerpt(self, category, cve_id):
        """Generate post excerpt"""
        excerpts = {
            "Critical": f"A critical vulnerability ({cve_id}) allows remote code execution and requires immediate patching. Analysis includes exploitation details and mitigation steps.",
            "Ransomware": f"New ransomware campaign using sophisticated encryption methods targets enterprise networks. Defense strategies and indicators of compromise provided.",
            "APT": f"Nation-state actors employing advanced techniques for persistence and data exfiltration. Detailed analysis of TTPs and detection rules.",
            "Cloud": f"Misconfigurations in cloud infrastructure lead to data exposure. Best practices for securing cloud deployments and monitoring for anomalies.",
            "IoT": f"Vulnerabilities in industrial control systems could enable physical damage to critical infrastructure. Security recommendations for OT environments.",
            "AI Security": f"Adversarial attacks on machine learning models demonstrate new attack vectors. Defensive strategies for AI-powered security systems."
        }
        
        return excerpts.get(category, f"Security analysis of emerging threats in {category.lower()} and recommended defense strategies.")
    
    def generate_content(self, category, cve_id, date):
        """Generate full blog post content in markdown"""
        
        # CVSS Score based on category
        cvss_scores = {
            "Critical": random.uniform(9.0, 10.0),
            "Ransomware": random.uniform(7.0, 8.9),
            "APT": random.uniform(8.0, 9.5),
            "Cloud": random.uniform(6.0, 8.5),
            "IoT": random.uniform(7.5, 9.0),
            "AI Security": random.uniform(6.5, 8.0)
        }
        
        cvss_score = round(cvss_scores.get(category, 7.5), 1)
        
        content = f"""# {self.generate_title(category, cve_id)}

## Executive Summary

**{cve_id}** has been identified as a {category.lower()} vulnerability affecting {random.choice(self.technologies)} deployments. With a CVSS score of {cvss_score}, this vulnerability allows {random.choice(['remote code execution', 'privilege escalation', 'data exfiltration', 'authentication bypass'])}.

## Technical Analysis

### Vulnerability Details

The vulnerability exists in the {random.choice(['authentication mechanism', 'input validation', 'access control', 'session management'])} of {random.choice(self.technologies)}. Specifically, improper {random.choice(['validation', 'sanitization', 'authorization', 'encryption'])} allows attackers to {random.choice(['execute arbitrary code', 'access sensitive data', 'bypass security controls', 'maintain persistence'])}.

**Affected Components:**
- {random.choice(self.technologies)} versions {random.choice(['1.0-2.5', '3.0-4.2', '2024.1-2025.3'])}
- {random.choice(['Cloud deployments', 'On-premises installations', 'Hybrid environments'])}
- {random.choice(['API endpoints', 'Web interfaces', 'CLI tools', 'Administrative panels'])}

### Exploitation Vector

Attackers can exploit this vulnerability by {random.choice(['sending specially crafted requests', 'uploading malicious files', 'modifying configuration parameters', 'injecting malicious code'])}:

```{random.choice(['python', 'bash', 'yaml', 'json'])}
# Example exploitation code
{self.generate_example_code(category)}
```

### Impact Assessment

**Primary Risks:**
1. **{random.choice(['Data Breach', 'Service Disruption', 'Financial Loss', 'Reputation Damage'])}**: {random.choice(['Sensitive information exposure', 'System availability impact', 'Regulatory compliance violations', 'Customer trust erosion'])}
2. **{random.choice(['Privilege Escalation', 'Lateral Movement', 'Persistence', 'Defense Evasion'])}**: {random.choice(['Gaining administrative access', 'Moving through network segments', 'Maintaining long-term access', 'Avoiding detection'])}
3. **{random.choice(['Business Continuity', 'Operational Technology', 'Supply Chain', 'Third-party Risk'])}**: {random.choice(['Critical operations disruption', 'Physical safety implications', 'Vendor compromise effects', 'External dependency risks'])}

**Affected Industries:**
- {random.choice(['Financial Services', 'Healthcare', 'Government', 'Education'])}
- {random.choice(['Manufacturing', 'Retail', 'Energy', 'Transportation'])}
- {random.choice(['Technology', 'Telecommunications', 'Media', 'Hospitality'])}

## Detection & Mitigation

### Immediate Actions

1. **Apply Patches**: Update to {random.choice(self.technologies)} version {random.choice(['2.6', '3.1', '2025.4', 'latest stable'])} or later
2. **Configuration Changes**:
```bash
{self.generate_mitigation_commands(category)}
```
3. **Network Controls**: Implement {random.choice(['firewall rules', 'WAF policies', 'IDS signatures', 'network segmentation'])}

### Detection Rules

**YARA/Sigma Rules:**
```yara
{self.generate_detection_rules(category, cve_id)}
```

**SIEM Queries:**
```sql
{self.generate_siem_queries(category)}
```

## Threat Actor Analysis

### Attribution & Campaigns

Our threat intelligence indicates {random.choice(['multiple', 'specific', 'emerging'])} actor groups are {random.choice(['actively exploiting', 'testing', 'preparing to exploit'])} this vulnerability:

1. **{random.choice(self.threat_actors)}**: {random.choice(['Targeting specific sectors', 'Conducting espionage', 'Seeking financial gain', 'Testing capabilities'])}
2. **{random.choice(['Initial Access Brokers', 'Ransomware Affiliates', 'Cybercriminal Groups', 'Hacktivists'])}**: {random.choice(['Selling access', 'Deploying ransomware', 'Stealing data', 'Making political statements'])}

### Observed TTPs

- **Initial Access**: {random.choice(['Phishing', 'Vulnerability exploitation', 'Credential stuffing', 'Supply chain compromise'])}
- **Execution**: {random.choice(['Command execution', 'Script execution', 'Service creation', 'Scheduled tasks'])}
- **Persistence**: {random.choice(['Registry modifications', 'Service installation', 'Startup items', 'Browser extensions'])}
- **Exfiltration**: {random.choice(['DNS tunneling', 'HTTP uploads', 'Cloud storage', 'Encrypted channels'])}

## Defense-in-Depth Recommendations

### 1. Preventive Controls

```{random.choice(['terraform', 'ansible', 'python', 'powershell'])}
{self.generate_preventive_controls(category)}
```

### 2. Detective Controls

- Implement {random.choice(['behavioral analytics', 'anomaly detection', 'threat hunting', 'user behavior analytics'])}
- Deploy {random.choice(['EDR solutions', 'NDR systems', 'XDR platforms', 'SIEM correlation'])}
- Monitor {random.choice(['network traffic', 'system logs', 'user activities', 'API calls'])}

### 3. Responsive Controls

- Develop {random.choice(['incident response plans', 'disaster recovery procedures', 'business continuity strategies', 'communication protocols'])}
- Conduct {random.choice(['tabletop exercises', 'red team engagements', 'penetration tests', 'security audits'])}

## Training Implications

This vulnerability highlights the importance of {random.choice(['continuous security education', 'hands-on technical training', 'threat awareness programs', 'skill development initiatives'])}:

### Critical Skills Required:

1. **{random.choice(['Vulnerability Management', 'Threat Intelligence', 'Incident Response', 'Security Architecture'])}**
   - Understanding {random.choice(['attack vectors', 'defense strategies', 'response procedures', 'architectural patterns'])}
   - Implementing {random.choice(['security controls', 'monitoring solutions', 'response plans', 'architectural decisions'])}

2. **{random.choice(['Technical Analysis', 'Forensic Investigation', 'Malware Analysis', 'Reverse Engineering'])}**
   - Analyzing {random.choice(['exploit code', 'attack patterns', 'malware samples', 'system artifacts'])}
   - Developing {random.choice(['detection rules', 'mitigation strategies', 'recovery procedures', 'preventive measures'])}

### Recommended Training Paths:

- **{random.choice(['Cloud Security', 'Network Defense', 'Application Security', 'Identity Management'])} Fundamentals**: {random.randint(8, 40)}-hour course
- **{random.choice(['Threat Hunting', 'Digital Forensics', 'Malware Analysis', 'Incident Response'])} Advanced**: Hands-on labs and real-world scenarios
- **{random.choice(['Security Leadership', 'Risk Management', 'Compliance', 'Governance'])}**: Strategic training for security leaders

## Conclusion

{self.generate_conclusion(category, cve_id)}

**Key Takeaways:**
1. {random.choice(['Patch vulnerable systems immediately', 'Review security configurations', 'Monitor for exploitation attempts', 'Update security policies'])}
2. {random.choice(['Implement defense-in-depth strategies', 'Deploy additional security controls', 'Enhance monitoring capabilities', 'Strengthen access controls'])}
3. {random.choice(['Conduct security awareness training', 'Provide technical skill development', 'Offer specialized security courses', 'Implement continuous learning programs'])}
4. {random.choice(['Establish incident response procedures', 'Develop recovery plans', 'Create communication protocols', 'Build resilience capabilities'])}

## References

1. Security Advisory: [{cve_id} Details](https://example.com/security/{cve_id.lower()})
2. Mitre ATT&CK Techniques: [Relevant Techniques](https://attack.mitre.org/)
3. Industry Best Practices: [Security Guidelines](https://example.com/guidelines)

---

*This analysis was prepared by the CyberPulse Threat Intelligence Team. For comprehensive security training and skill development, explore our [security training programs](/training). Stay secure, stay informed.*

*Last Updated: {date.strftime('%Y-%m-%d %H:%M UTC')}*
"""
        
        return content
    
    def generate_example_code(self, category):
        """Generate example exploitation code"""
        if category == "Critical":
            return """# Critical vulnerability exploitation
target = "vulnerable-system.example.com"
payload = construct_malicious_payload()
response = send_exploit(target, payload)
if response.status_code == 200:
    print("[+] Exploitation successful")
    execute_commands(response)"""
        elif category == "Ransomware":
            return """# Ransomware encryption routine
files = find_target_files()
for file in files:
    encrypted = encrypt_file(file, ransomware_key)
    write_file(file + ".encrypted", encrypted)
    delete_original(file)
create_ransom_note()"""
        else:
            return """# Example code snippet
def exploit_vulnerability(target):
    # Vulnerability exploitation logic
    payload = create_payload()
    result = send_payload(target, payload)
    return result"""
    
    def generate_mitigation_commands(self, category):
        """Generate mitigation commands"""
        if category == "Cloud":
            return """# Secure cloud configuration
aws iam update-account-password-policy \\
    --minimum-password-length 14 \\
    --require-symbols \\
    --require-numbers \\
    --require-uppercase-characters \\
    --require-lowercase-characters \\
    --allow-users-to-change-password \\
    --max-password-age 90 \\
    --password-reuse-prevention 24"""
        else:
            return """# Security hardening commands
systemctl disable vulnerable-service
iptables -A INPUT -p tcp --dport 445 -j DROP
chmod 750 /etc/shadow
auditctl -w /etc/passwd -p wa -k passwd_changes"""
    
    def generate_detection_rules(self, category, cve_id):
        """Generate detection rules"""
        return f"""rule detect_{cve_id.replace('-', '_').lower()} {{
    meta:
        description = "Detects exploitation attempts for {cve_id}"
        author = "CyberPulse Threat Intelligence"
        date = "{datetime.now().strftime('%Y-%m-%d')}"
        severity = "critical"
    
    strings:
        $exploit_string = "malicious_pattern" ascii
        $payload_hash = {{ deadbeef cafebabe }}
    
    condition:
        any of them
}}"""
    
    def generate_siem_queries(self, category):
        """Generate SIEM queries"""
        return f"""index=security sourcetype=firewall 
| search dest_port=445 OR dest_port=3389 
| stats count by src_ip dest_ip 
| where count > 100 
| sort - count"""
    
    def generate_preventive_controls(self, category):
        """Generate preventive controls code"""
        if category == "Cloud":
            return """# Terraform security configuration
resource "aws_s3_bucket" "secure_bucket" {
  bucket = "secure-data-${var.environment}"
  
  versioning {
    enabled = true
  }
  
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
  
  lifecycle_rule {
    enabled = true
    expiration {
      days = 90
    }
  }
}"""
        else:
            return """# Security configuration example
security {
  min_tls_version = "1.2"
  cipher_suites = [
    "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
    "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"
  ]
  
  rate_limiting {
    requests_per_minute = 100
    burst_size = 50
  }
  
  headers {
    x_frame_options = "DENY"
    x_content_type_options = "nosniff"
    x_xss_protection = "1; mode=block"
  }
}"""
    
    def generate_conclusion(self, category, cve_id):
        """Generate conclusion paragraph"""
        conclusions = [
            f"{cve_id} represents a significant security challenge that requires coordinated defense efforts. Organizations must balance immediate remediation with long-term security strategy development.",
            f"The evolving threat landscape demonstrated by {cve_id} underscores the need for continuous security monitoring and adaptive defense mechanisms.",
            f"Effective response to {cve_id} requires both technical solutions and organizational security maturity, highlighting the importance of comprehensive security programs.",
            f"This vulnerability analysis reveals critical gaps in current security practices and emphasizes the value of proactive security measures and ongoing education."
        ]
        return random.choice(conclusions)
    
    def save_post(self, post_data, output_dir="posts"):
        """Save blog post to file"""
        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Generate filename from date and title
        date_str = post_data["date"]
        title_slug = post_data["title"].lower().replace(" ", "-").replace(":", "").replace(",", "")[:50]
        filename = f"{output_dir}/{date_str}-{title_slug}.md"
        
        # Create frontmatter
        frontmatter = f"""---
title: "{post_data['title']}"
date: {post_data['date']}
author: "{post_data['author']}"
category: "{post_data['category']}"
tags: {json.dumps(post_data['tags'])}
excerpt: "{post_data['excerpt']}"
read_time: {post_data['read_time']}
---

"""
        
        # Combine frontmatter and content
        full_content = frontmatter + post_data["content"]
        
        # Save to file
        with open(filename, "w") as f:
            f.write(full_content)
        
        print(f"✅ Blog post saved: {filename}")
        print(f"   Title: {post_data['title']}")
        print(f"   Category: {post_data['category']}")
        print(f"   Read time: {post_data['read_time']} min")
        
        return filename
    
    def update_index_json(self, post_data, json_file="posts/index.json"):
        """Update posts index JSON file"""
        # Load existing index or create new
        if os.path.exists(json_file):
            with open(json_file, "r") as f:
                index = json.load(f)
        else:
            index = {"posts": []}
        
        # Add new post to beginning
        post_entry = {
            "id": len(index["posts"]) + 1,
            "date": post_data["date"],
            "title": post_data["title"],
            "category": post_data["category"],
            "excerpt": post_data["excerpt"],
            "tags": post_data["tags"],
            "read_time": post_data["read_time"],
            "author": post_data["author"]
        }
        
        index["posts"].insert(0, post_entry)
        
        # Keep only last 30 posts
        index["posts"] = index["posts"][:30]
        
        # Save updated index
        with open(json_file, "w") as f:
            json.dump(index, f, indent=2)
        
        print(f"✅ Index updated: {json_file}")
    
    def generate_daily(self):
        """Generate and save daily post"""
        print("=" * 60)
        print("CYBERSECURITY BLOG POST GENERATOR")
        print("=" * 60)
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
        print()
        
        # Generate post
        post_data = self.generate_daily_post()
        
        # Save post
        filename = self.save_post(post_data)
        
        # Update index
        self.update_index_json(post_data)
        
        # Generate HTML preview
        self.generate_html_preview(post_data)
        
        print()
        print("=" * 60)
        print("GENERATION COMPLETE")
        print("=" * 60)
        
        return post_data
    
    def generate_html_preview(self, post_data, output_file="preview.html"):
        """Generate HTML preview of the post"""
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Preview: {post_data['title']}</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        h1 {{ color: #333; border-bottom: 2px solid #0ea5e9; padding-bottom: 10px; }}
        .meta {{ color: #666; font-size: 0.9em; margin-bottom: 20px; }}
        .excerpt {{ background: #f5f5f5; padding: 15px; border-left: 4px solid #0ea5e9; margin: 20px 0; }}
        .tags {{ margin-top: 20px; }}
        .tag {{ display: inline-block; background: #e0f2fe; color: #0369a1; padding: 3px 8px; margin: 2px; border-radius: 3px; font-size: 0.8em; }}
    </style>
</head>
<body>
    <h1>{post_data['title']}</h1>
    <div class="meta">
        <strong>Date:</strong> {post_data['date']} | 
        <strong>Author:</strong> {post_data['author']} | 
        <strong>Category:</strong> {post_data['category']} | 
        <strong>Read time:</strong> {post_data['read_time']} min
    </div>
    <div class="excerpt">
        <strong>Excerpt:</strong> {post_data['excerpt']}
    </div>
    <div class="tags">
        <strong>Tags:</strong><br>
        {' '.join([f'<span class="tag">{tag}</span>' for tag in post_data['tags']])}
    </div>
    <hr>
    <div>
        <h2>Content Preview</h2>
        <pre style="background: #f8fafc; padding: 15px; border-radius: 5px; overflow: auto; max-height: 400px;">
{post_data['content'][:2000]}...
        </pre>
    </div>
</body>
</html>"""
        
        with open(output_file, "w") as f:
            f.write(html_content)
        
        print(f"✅ HTML preview saved: {output_file}")

def main():
    """Main function"""
    generator = CybersecurityBlogGenerator()
    
    # Generate daily post
    post_data = generator.generate_daily()
    
    # Print summary
    print("\n📊 POST SUMMARY:")
    print(f"   Title: {post_data['title']}")
    print(f"   Category: {post_data['category']}")
    print(f"   Author: {post_data['author']}")
    print(f"   Tags: {', '.join(post_data['tags'][:5])}")
    print(f"   Read time: {post_data['read_time']} minutes")
    
    # Instructions for GitHub deployment
    print("\n🚀 DEPLOYMENT INSTRUCTIONS:")
    print("1. Commit the generated files to your GitHub repository")
    print("2. Enable GitHub Pages in repository settings")
    print("3. Set source to 'main' branch and '/root' folder")
    print("4. Your blog will be available at: https://[username].github.io/[repository]/")
    
    print("\n📁 FILES GENERATED:")
    print("   - index.html (Main blog page)")
    print("   - css/style.css (Styles)")
    print("   - js/main.js (JavaScript)")
    print("   - posts/[date]-[title].md (Today's blog post)")
    print("   - posts/index.json (Posts index)")
    print("   - preview.html (HTML preview)")

if __name__ == "__main__":
    main()