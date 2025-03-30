---
title: Threat Actors
author: gourabdg47
date: 2025-03-30T18:05:00
categories:
  - Information
  - Security +
tags:
  - reading
  - certification
render_with_liquid: true
---
I am following [Udemy Jason Dion](https://www.udemy.com/course/securityplus/learn/lecture/40324620#overview)'s course for Security +

## Threat Actors
An individual or entity responsible for incidents that impact security and data protection

* **Threat actor attributes :** Specific characteristics or property that define and differentiate various threat actors from one another

#### Breakdown of **Threat Actors**

##### 1. **Nation-State Actors**

**Description**: Government-sponsored groups conducting cyber espionage, sabotage, or warfare for political/military goals.  
**Motivation**: Geopolitical advantage, intelligence gathering, or disruption of adversaries.

#### Examples:

- **Stuxnet (2010)**
    
    - **Actor**: U.S. and Israel (allegedly).
        
    - **Attack**: Malware destroyed Iran’s nuclear centrifuges by causing physical damage.
        
    - **Impact**: Delayed Iran’s nuclear program by years.
        
- **SolarWinds Hack (2020)**
    
    - **Actor**: Russian APT29 (Cozy Bear).
        
    - **Attack**: Compromised software updates to infiltrate U.S. agencies and companies.
        
    - **Impact**: Breached 100+ organizations, including the Pentagon and Microsoft.
        
- **NotPetya (2017)**
    
    - **Actor**: Russian military (GRU).
        
    - **Attack**: Disguised ransomware wiped data in Ukraine, spreading globally.
        
    - **Impact**: Caused $10B+ in damages (e.g., Maersk, Merck).
        

---

##### 2. **Cybercriminals**

**Description**: Profit-driven individuals or groups using ransomware, phishing, or fraud.  
**Motivation**: Financial gain through extortion, data theft, or scams.

#### Examples:

- **WannaCry (2017)**
    
    - **Actor**: North Korea’s Lazarus Group.
        
    - **Attack**: Ransomware exploited Windows vulnerabilities, locking 300K+ devices.
        
    - **Impact**: Paralyzed UK’s NHS, FedEx, and global systems.
        
- **Colonial Pipeline Ransomware (2021)**
    
    - **Actor**: DarkSide (Russian-linked group).
        
    - **Attack**: Forced a major U.S. fuel pipeline to shut down for days.
        
    - **Impact**: Fuel shortages, $4.4M ransom paid.
        
- **MOVEit Data Theft (2023)**
    
    - **Actor**: Clop ransomware gang.
        
    - **Attack**: Exploited file-transfer software to steal data from 600+ organizations.
        
    - **Impact**: Affected BBC, British Airways, and U.S. government agencies.
        

---

##### 3. **Hacktivists**

**Description**: Activists using cyberattacks to promote political/social causes.  
**Motivation**: Ideological goals, such as exposing corruption or supporting social justice.

#### Examples:

- **Sony Pictures Hack (2014)**
    
    - **Actor**: Guardians of Peace (linked to North Korea).
        
    - **Attack**: Leaked emails/films to retaliate against _The Interview_ movie.
        
    - **Impact**: $35M in damages, reputational harm.
        
- **Anonymous vs. ISIS (2015)**
    
    - **Actor**: Anonymous collective.
        
    - **Attack**: Took down ISIS social media accounts and propaganda sites.
        
    - **Impact**: Disrupted recruitment and communication networks.
        

---

##### 4. **Insider Threats**

**Description**: Employees or contractors who intentionally or accidentally harm an organization.  
**Motivation**: Revenge, financial gain, or negligence.

#### Examples:

- **Edward Snowden Leaks (2013)**
    
    - **Actor**: NSA contractor.
        
    - **Attack**: Stole/leaked classified documents on global surveillance programs.
        
    - **Impact**: Global privacy debates, strained U.S. diplomatic relations.
        
- **Twitter Bitcoin Scam (2020)**
    
    - **Actor**: Insider colluding with hackers.
        
    - **Attack**: Hijacked high-profile accounts (e.g., Obama, Elon Musk) to promote crypto fraud.
        
    - **Impact**: Stole $118K in Bitcoin, damaged Twitter’s credibility.
        

---

##### 5. **Organized Crime Groups**

**Description**: Sophisticated networks conducting large-scale fraud, data theft, or ransomware.  
**Motivation**: Profit through illegal cyber operations.

#### Examples:

- **Target Data Breach (2013)**
    
    - **Actor**: Eastern European crime ring.
        
    - **Attack**: Stole 40M credit cards via compromised HVAC vendor credentials.
        
    - **Impact**: Cost Target $300M+ in settlements.
        
- **JBS Ransomware Attack (2021)**
    
    - **Actor**: REvil (Russian-speaking group).
        
    - **Attack**: Forced the world’s largest meat supplier to halt operations.
        
    - **Impact**: $11M ransom paid, global meat shortages.
        

---

##### 6. **Script Kiddies**

**Description**: Unskilled attackers using pre-made tools for low-level attacks.  
**Motivation**: Notoriety, curiosity, or minor disruption.

#### Example:

- **Mirai Botnet (2016)**
    
    - **Actor**: Young hackers experimenting with IoT exploits.
        
    - **Attack**: Hijacked 600K+ devices to launch DDoS attacks on Dyn DNS.
        
    - **Impact**: Took down Twitter, Netflix, and Reddit for hours.

---
#### Threat Actor Motivations 

It is important to remember that there is difference between the intent behind an attack and the motivation that fuels the attack
1. **Data exfiltration**
2. **Blackmail**
3. **Espionage**
4. **Service Disruption**
5. **Financial Gain**
6. **Philosophical or Political Beliefs** 
7. **Ethical Reasons**
8. **Revenge**
9. **Disruption**
10. **War**

---
#### Threat Actor Attributes 
###### Origin :
1. Internal vs External
2. Resources and Funding
	1. **Limited Resources:** Some threat actors operate on a shoestring budget, relying on low-cost or free hacking tools and tactics. These actors may primarily engage in opportunistic attacks.

	2. **Organized Cybercriminal Groups:** Organized cybercriminal groups have access to more substantial resources, such as funding from criminal activities, cryptocurrency payments, or the sale of stolen data on the dark web.
	
	3. **Nation-State and State-Sponsored Actors:** Nation-state and state-sponsored threat actors often have significant funding, advanced tools, and substantial human resources at their disposal. They are capable of conducting highly sophisticated and prolonged cyber campaigns.
3. Level of sophistication and capability
	1. **Script Kiddies:** These are individuals with limited technical expertise who use pre-packaged hacking tools or follow online tutorials to launch basic attacks.

	2. **Opportunistic Hackers:** Opportunistic hackers take advantage of known vulnerabilities or widely available attack tools to conduct attacks of opportunity without specific targets in mind.
	
	3. **Advanced Cybercriminals:** Advanced cybercriminals possess more sophisticated technical skills. They develop custom malware, engage in targeted attacks, and use advanced evasion techniques.
	
	4. **Nation-State Actors and APT Groups:** Nation-state actors and APT groups are among the most sophisticated threat actors. They have significant resources and conduct highly targeted and stealthy attacks, often focusing on long-term operations.

---

## Threat Vectors
The means or pathway by which an attacker can gain unauthorized access to a computer or network to deliver malicious payload or carry out an unwanted action
Below are common categories with examples:

##### **A. Email-Based Attacks**

**Description**: Phishing, spear-phishing, or malicious attachments sent via email.  
**Tactical Breakdown**:

- **Social Engineering**: Crafting convincing emails to trick users into sharing credentials.
    
- **Malware Delivery**: Attachments or links that install ransomware, spyware, or keyloggers.
    

**Example**: **2016 DNC Hack**

- **Vector**: Spear-phishing emails targeting Hillary Clinton’s campaign staff.
    
- **Tactic**: Emails mimicked Google security alerts, tricking users into sharing passwords.
    
- **Impact**: Leaked emails influenced U.S. elections; attributed to Russian APT28 (Fancy Bear).
    

---

##### **B. Network-Based Attacks**

**Description**: Exploiting vulnerabilities in network protocols, firewalls, or unsecured ports.  
**Tactical Breakdown**:

- **Exploiting Weak Protocols**: Using outdated protocols (e.g., SMBv1) to infiltrate systems.
    
- **Man-in-the-Middle (MitM)**: Intercepting unencrypted data over public Wi-Fi.
    

**Example**: **Colonial Pipeline Ransomware (2021)**

- **Vector**: Exploited a VPN vulnerability (no multi-factor authentication).
    
- **Tactic**: DarkSide group used stolen credentials to access the network and deploy ransomware.
    
- **Impact**: Forced shutdown of a major U.S. fuel pipeline; $4.4M ransom paid.
    

---

##### **C. Software Vulnerabilities**

**Description**: Exploiting flaws in code (e.g., zero-days, unpatched systems).  
**Tactical Breakdown**:

- **Zero-Day Exploits**: Using undisclosed vulnerabilities before a patch is available.
    
- **Credential Stuffing**: Automated attacks using leaked passwords.
    

**Example**: **SolarWinds Hack (2020)**

- **Vector**: Compromised software update mechanism of SolarWinds’ Orion platform.
    
- **Tactic**: APT29 (Cozy Bear) injected malware into updates, enabling backdoor access.
    
- **Impact**: Breached U.S. government agencies (e.g., Treasury, Pentagon).
    

---

##### **D. Physical Attacks**

**Description**: Gaining physical access to devices or facilities.  
**Tactical Breakdown**:

- **USB Drops**: Leaving infected USB drives in public areas for curious users.
    
- **Shoulder Surfing**: Stealing passwords by observing users in public spaces.
    

**Example**: **Stuxnet (2010)**

- **Vector**: Infected USB drives inserted into air-gapped Iranian nuclear facilities.
    
- **Tactic**: Malware spread via Windows zero-days to sabotage uranium centrifuges.
    
- **Impact**: Destroyed 1,000+ centrifuges; delayed Iran’s nuclear program.
    

---

##### **E. Social Engineering**

**Description**: Manipulating humans into divulging sensitive information.  
**Tactical Breakdown**:

- **Pretexting**: Fabricating scenarios (e.g., impersonating IT support).
    
- **Baiting**: Offering fake rewards (e.g., "free software" containing malware).
    

**Example**: **Twitter Bitcoin Scam (2020)**

- **Vector**: Phone-based spear-phishing targeting Twitter employees.
    
- **Tactic**: Hackers convinced an employee to share credentials via a fake internal portal.
    
- **Impact**: Hijacked accounts of Obama, Musk, and others to promote crypto scams.

## Attack Surface
Encompasses all the various points where an unauthorized user can try to enter data to or extract data from an environment
Key categories:

##### **A. Endpoints**

**Description**: Devices like laptops, smartphones, or IoT devices.  
**Example**: **WannaCry Ransomware (2017)**

- **Surface**: Unpatched Windows systems (EternalBlue vulnerability).
    
- **Tactic**: Ransomware propagated via SMB protocol, encrypting 300K+ devices.
    
- **Mitigation**: Regular patching and endpoint detection tools (EDR).
    

---

##### **B. Network Infrastructure**

**Description**: Routers, firewalls, VPNs, and unsecured Wi-Fi.  
**Example**: **Target Breach (2013)**

- **Surface**: Third-party HVAC vendor’s network credentials.
    
- **Tactic**: Attackers pivoted from vendor network to Target’s payment systems.
    
- **Mitigation**: Network segmentation and third-party risk assessments.
    

---

##### **C. Cloud Services**

**Description**: Misconfigured cloud storage, APIs, or weak access controls.  
**Example**: **Capital One Breach (2019)**

- **Surface**: Misconfigured AWS S3 bucket firewall.
    
- **Tactic**: Hacker exploited a web application firewall (WAF) vulnerability.
    
- **Impact**: Exposed 100M+ customer records; $190M in fines.
    

---

##### **D. APIs**

**Description**: Insecure APIs exposing data or functionality.  
**Example**: **Facebook API Abuse (2018)**

- **Surface**: Third-party app APIs harvesting user data.
    
- **Tactic**: Cambridge Analytica collected data of 87M users without consent.
    
- **Mitigation**: API rate limiting and strict OAuth scopes.
    

---

##### **E. Human Element**

**Description**: Employees falling for phishing, weak passwords, or insider threats.  
**Example**: **Edward Snowden Leaks (2013)**

- **Surface**: Insider access to classified NSA systems.
    
- **Tactic**: Snowden used legitimate credentials to exfiltrate data to external drives.
    
- **Mitigation**: Least-privilege access and user activity monitoring.


#### **Key Mitigation Strategies**

1. **Email Security**: Deploy DMARC, SPF, and phishing simulations for training.
    
2. **Patch Management**: Prioritize critical vulnerabilities (e.g., CVSS 9+).
    
3. **Zero Trust**: Enforce least-privilege access and multi-factor authentication (MFA).
    
4. **Attack Surface Reduction**: Disable unused services and segment networks.


> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions) 
{: .prompt-info }