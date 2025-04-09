---
title: Application Security
author: gourabdg47
date: 2025-04-09 09:05:00
categories:
  - Information
  - Security +
tags:
  - reading
  - certification
render_with_liquid: true
---

# Application  security
This chapter covers 
1. Domain 2.0: Threats, Vulnerabilities, and Mitigations
2. Domain 4.0: Security Operations
3. Domain 5.0: Security Program Management and Oversight

---
### Software development life cycle 
**SDLC** describes  the steps in a model for software development throughout its life. From idea to requirement gathering, analysis to design, coding, testing & rollout. Once the software is in production, it includes from user training, maintenance and decommissioning.

<img src="https://raw.githubusercontent.com/gourabdg47/gourabdg47.github.io/refs/heads/main/assets/images/SDLC.png" alt="High-level SDLC view" width="500" title="High-level SDLC view" />

#### Phases of SDLC
1. **Planning** : Initial investigation into weather the effort should occur. Here we looks for alternative solutions and high-level cost for each solutions 
2. **Requirements** : Getting customer input to determine the desired functionality and what improvements are required. Requirements may be ranked to determine which of them are the most critical to the success of the project. 
3. **Design** : Design for functionality, architecture, integration points, dataflow, business process and other required design consideration.
4. **Coding** : Development of the parts of the software, testing mainly unite testing (the testing of small components).
5. **Testing** : Majority of the testing occurs outside the coding phase, like testing with the customers, others outside of the development team
6. **Maintains**  : Making sure the software keeps on working as intended 

---

**DevOps** combines software development and IT operations with the goal of optimizing the SDLC. This is done by using collections of tools called toolchains to improve SDLC processes. The toolchain includes tools that assist with coding, building, testing, packaging, releasing, configuring monitoring software.
#### The Role of Security Practitioners in DevSecOps 🔒

In a **DevSecOps** model, security teams don’t just “check boxes” – they actively shape secure development workflows. Here’s what they do:
##### Key Responsibilities 🛠️

- **Threat Analysis**: Identify risks early in the development lifecycle.
- **Communication**: Bridge gaps between developers, ops, and leadership.
- **Planning & Testing**: Embed security into design and automate security checks.
- **Feedback Loops**: Improve processes by sharing insights with teams.
- **Continuous Improvement**: Update tools, policies, and training as threats evolve.

##### Collaboration & Awareness 🤝

- Understand the **organization’s risk tolerance** to prioritize effectively.
- Stay synced with **DevSecOps workflows** (who’s doing what, and when).

##### Integration with CI/CD Pipelines ⚙️

DevSecOps thrives in automated environments:

- **Automated Security Testing**: Scans for vulnerabilities during code commits.
- **Tooling**:

    - Configuration management (e.g., Ansible, Terraform).
    - Dependency scanners (e.g., Snyk, OWASP).
    - Patch management tools.

##### Key Takeaways 💡
Security in DevSecOps isn’t a gatekeeper – it’s a **continuous partner** that:

1. Adapts to agile workflows.
2. Balances speed with safety.
3. Leverages automation to scale securely.

---

#### Secure Designing & Coding
Being part of a SDLC as a security professional is a significant opportunity to improve the security of the application.  During the gathering and designing phase, when the security can be build as a part of the requirements then design according to the requirements. 
##### Secure Coding Practices: A Guide with OWASP 🔒

###### **Why OWASP?**

The **Open Worldwide Application Security Project (OWASP)** is a gold-standard resource for developers and security teams. It offers:

- Community-driven standards, guides, and tools.
- Up-to-date best practices for web application security.
- Insights into evolving cyber threats.

📌 _Tip_: OWASP’s Proactive Controls list is a must-read to stay ahead of risks !
### OWASP’s Top 10 Proactive Controls

1. **Define Security Requirements**  
    Bake security into _every_ phase of development, not as an afterthought.
    
2. **Leverage Security Frameworks**  
    Use trusted libraries (e.g., OAuth, Spring Security) to avoid reinventing the wheel.
    
3. **Secure Database Access**
    
    - Use prebuilt queries to block SQL injection.
    - Restrict database permissions strictly.
        
4. **Encode & Escape Data**  
    Sanitize inputs by stripping special characters (e.g., `<script>` becomes harmless).
    
5. **Validate All Inputs**  
    Treat _all_ user-provided data as untrusted—filter rigorously.
    
6. **Implement Digital Identity**
    
    - Enforce MFA and secure password hashing.
    - Manage sessions with timeouts and encryption.
        
7. **Enforce Access Controls**
    
    - Apply "deny by default" and the principle of **least privilege**.
    - Audit permissions regularly.
        
8. **Protect Data Everywhere**  
    Encrypt data _both_ in transit (HTTPS/TLS) and at rest (AES-256).
    
9. **Enable Logging & Monitoring**  
    Track anomalies to detect breaches early and investigate incidents.
    
10. **Handle Errors Gracefully**
    
    - Never expose sensitive info in error messages.
    - Test failure scenarios to ensure smooth recovery.
        
##### **Resources to Level Up**

- 📜 [OWASP Proactive Controls](https://owasp.org/www-project-proactive-controls)
- 🚀 [Secure Coding Quick Reference Guide](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide)

##### **Key Takeaway**

OWASP’s guidelines aren’t just rules—they’re a **mindset shift**. By embedding these practices early, teams build security into their DNA, reducing risks without slowing innovation.

---
### Injection Vulnerabilities: The Hacker’s Gateway
Let's turn our attention to the motivating force behind putting these mechanisms in place: the vulnerabilities that attackers may exploit to undermine our security.
**Injection flaws** rank among the _top attack vectors_ for breaching web applications. They let attackers inject malicious code into input fields, tricking servers into executing unintended commands—often with catastrophic results.

#### Why It Matters

- **Common Targets**: Login forms, search bars, APIs.
- **Impact**: Data theft, system takeover, or backend server compromise.
- **Examples**: SQL injection, OS command injection, LDAP injection.
#### How Attackers Exploit Injections

1. **Malicious Input**: Attackers submit code (e.g., SQL queries, shell commands) into vulnerable fields.
2. **Server Deception**: The server processes the input as a legitimate command.
3. **Execution**: The code runs on the server _or_ passes to downstream systems (e.g., databases).

#### SQL Injections Attacks
Web apps often take user input (like search terms) and use it to build database queries. For example, an e-commerce site might process a search for **"orange tiger pillow"** like this :

<pre><code>
SELECT ItemName, ItemDescription, ItemPrice  
FROM Products  
WHERE ItemName LIKE '%orange%'  
AND ItemName LIKE '%tiger%'  
AND ItemName LIKE '%pillow%'; 
</code></pre>  

##### What’s Happening Here?

1. The app breaks the search into keywords.
2. It queries the database for items matching **all** terms.
3. Results are returned to the user.

##### Bypassing Security
An attacker submits this search term :
<pre><code>
' OR 1=1; --  
</code></pre>  

The app naively converts this into :

<pre><code>
SELECT ItemName, ItemDescription, ItemPrice  
FROM Products  
WHERE ItemName LIKE '%' OR 1=1; --%'  
AND ItemName LIKE '%tiger%'  
AND ItemName LIKE '%pillow%';  
</code></pre>  




---

> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions) 
{: .prompt-info }