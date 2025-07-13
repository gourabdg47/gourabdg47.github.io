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

###### Examples:

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

###### Examples:

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

###### Examples:

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

###### Examples:

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

###### Examples:

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

###### Example:

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

## What Are TTPs?

- **Tactics**: The _goals_ of an attacker (e.g., gaining initial access, exfiltrating data).
    
- **Techniques**: The _methods_ used to achieve those goals (e.g., phishing, credential dumping).
    
- **Procedures**: The _step-by-step actions_ taken to execute techniques (e.g., specific malware code, exploit chains).

#### **Real-World Examples with TTP Breakdowns**

##### **1. SolarWinds Hack (2020)**

**Threat Actor**: APT29 (Cozy Bear, Russian SVR)  
**Objective**: Espionage and persistent access to U.S. government and corporate networks.

- **Tactics**:
    
    - **Initial Access**: Compromise software supply chain.
    - **Persistence**: Establish backdoor for long-term access.
    - **Exfiltration**: Steal sensitive data.
        
- **Techniques**:
    
    - **Supply Chain Compromise**: Trojanized SolarWinds Orion software updates.
    - **Credential Access**: Forged SAML tokens to bypass authentication.
    - **Lateral Movement**: Used compromised credentials to pivot across networks.
        
- **Procedures**:
    
    - Injected malicious code (`SUNBURST` backdoor) into Orion’s update process.
    - Used DNS tunneling to communicate with command-and-control (C2) servers.
    - Masqueraded as legitimate traffic to avoid detection.
        

**Mitigation**:

- Code signing for software updates.
- Network segmentation and zero-trust architecture.
    

---

##### **2. WannaCry Ransomware (2017)**

**Threat Actor**: Lazarus Group (North Korea)  
**Objective**: Financial gain via ransomware and disruption.

- **Tactics**:
    
    - **Initial Access**: Exploit unpatched vulnerabilities.
    - **Impact**: Encrypt data and demand ransom.
        
- **Techniques**:
    
    - **Exploitation of Public-Facing Apps**: EternalBlue SMBv1 exploit.
    - **Data Encryption**: Ransomware payload (AES-128 encryption).
    - **Command and Control**: Kill switch domain to halt propagation.
        
- **Procedures**:
    
    - Scanned for vulnerable Windows systems (port 445).
    - Deployed ransomware via DoublePulsar backdoor.
    - Demanded Bitcoin payments for decryption keys.
        

**Mitigation**:

- Patch management (MS17-010).
- Disable legacy protocols (SMBv1).
    

---

##### **3. Twitter Bitcoin Scam (2020)**

**Threat Actor**: Social engineering hackers  
**Objective**: Financial fraud via hijacked accounts.

- **Tactics**:
    
    - **Credential Access**: Phish employee credentials.
    - **Privilege Escalation**: Abuse internal admin tools.
        
- **Techniques**:
    
    - **Spear Phishing**: Targeted Twitter employees via phone/email.
    - **Internal Tool Abuse**: Used "Twitter Admin" panel to reset account passwords.
        
- **Procedures**:
    
    - Convinced employees via fake "IT department" calls to share credentials.
    - Accessed internal Slack channels to find admin tool locations.
    - Posted Bitcoin scam tweets from high-profile accounts (Elon Musk, Obama).
        

**Mitigation**:

- Multi-factor authentication (MFA) for admin tools.
- Employee security awareness training.
    

---

##### **4. NotPetya (2017)**

**Threat Actor**: Sandworm Team (Russian GRU)  
**Objective**: Destructive cyberattack disguised as ransomware.

- **Tactics**:
    
    - **Initial Access**: Compromise Ukrainian accounting software (M.E.Doc).
    - **Impact**: Wipe data and disrupt critical infrastructure.
        
- **Techniques**:
    
    - **Supply Chain Compromise**: Trojanized M.E.Doc updates.
    - **Credential Dumping**: Mimikatz tool to extract passwords.
    - **Disk Wiping**: Overwrite Master Boot Record (MBR).
        
- **Procedures**:
    
    - Used EternalBlue exploit to spread laterally.
    - Deployed fake ransomware payload (no decryption possible).
    - Targeted Ukrainian businesses, but spread globally (Maersk, Merck).
        
**Mitigation**:

- Air-gap critical systems.
- Segment networks to limit lateral movement.
    

---

##### **5. MOVEit Transfer Exploit (2023)**

**Threat Actor**: Clop ransomware gang  
**Objective**: Extortion via mass data theft.

- **Tactics**:
    
    - **Initial Access**: Exploit zero-day in MOVEit file-transfer software.
    - **Collection**: Steal sensitive data for double extortion.
        
- **Techniques**:
    
    - **SQL Injection**: Exploited CVE-2023-34362 to gain admin access.
    - **Data Theft**: Downloaded files from compromised MOVEit instances.
    - **Extortion**: Threatened to leak data unless ransom paid.
        
- **Procedures**:
    
    - Scanned for vulnerable MOVEit Transfer servers.
    - Deployed web shells (e.g., `LemonDuck`) to maintain access.
    - Exfiltrated data via HTTPS to avoid detection.
        

**Mitigation**:

- Patch critical vulnerabilities immediately.
- Monitor for unusual outbound traffic (data exfiltration).

##### **Key Takeaways for Defenders**

1. **Map to MITRE ATT&CK**: Use frameworks to identify TTPs in your environment.
    
2. **Behavioral Detection**: Focus on anomalous activities (e.g., credential dumping, lateral movement).
    
3. **Proactive Hunting**: Assume breach and look for Indicators of Compromise (IoCs).


## Outsmarting Threat Actors:

#### **1. Deception Technologies**

Deception technologies create fake assets, data, or environments to mislead attackers, waste their time, and gather intelligence on their tactics.
##### **1. Honeypot**

**What it is**: A decoy system or service designed to mimic real assets to attract attackers.  
**How it works**:

- Simulates vulnerabilities (e.g., outdated software, open ports).
    
- Monitors and logs attacker interactions.  
    **Purpose**:
- Detect unauthorized access attempts.
- Study attacker behavior and tools.
    
---
##### **2. Honeynet**

**What it is**: A network of interconnected honeypots replicating a full operational environment.  
**How it works**:

- Mimics real-world infrastructure (e.g., databases, user endpoints).
- Uses monitoring tools ("honeywalls") to track lateral movement.  
    **Purpose**:
- Analyze advanced attack workflows (e.g., pivoting, data exfiltration).
    
---
##### **3. Honey Token**

**What it is**: Fake credentials, API keys, or data snippets planted to trigger alerts.  
**How it works**:

- Embedded in code repositories, databases, or logs.
- Alerts defenders if accessed or used.  
    **Purpose**:
- Detect credential theft or insider threats.

---
##### **4. Honeyfile**

**What it is**: A monitored decoy file placed in sensitive directories.  
**How it works**:

- Appears valuable (e.g., "confidential.docx" or "passwords.txt").
- Triggers alerts if opened, copied, or modified.  
    **Purpose**:
- Identify unauthorized access or data theft.
    
---
##### **5. Honeyclient**

**What it is**: A client-side tool (e.g., browser) that interacts with malicious websites.  
**How it works**:

- Automatically visits suspicious URLs to detect exploits.
- Analyzes code for malicious payloads.  
    **Purpose**:
- Map phishing or malware-delivery infrastructure.
    
##### **Examples**

**A. Honeypots and Honeynets**

- **What it does**: Fake servers, databases, or entire networks designed to lure attackers.
    
- **Example**:
    
    - **Operation Cobalt Kitty (2017)**: APT Group (OceanLotus) targeted an Asian corporation. The company deployed a **honeynet** mimicking its R&D environment. Attackers wasted weeks stealing fake data, allowing defenders to study their TTPs.
        
    - **Tactical Insight**: Honeypots can track attacker behavior, such as lateral movement and exploit preferences.
        
**B. Honey Tokens/Canary Tokens**

- **What it does**: Fake credentials, files, or API keys that trigger alerts when touched.
    
- **Example**:
    
    - **Twitter API Breach (2022)**: A company planted **fake API keys** in a public GitHub repo. When attackers used them, defenders received alerts and traced the intrusion to a compromised third-party vendor.
        
**C. Deception Grids**

- **What it does**: Distributed decoy systems across an organization’s network to confuse attackers.
    
- **Example**:
    
    - **IllusionBLACK (U.S. DoD)**: The Pentagon uses a deception grid with fake operational plans and dummy military contracts. When Chinese state-sponsored hackers (APT40) attempted to exfiltrate data in 2020, they stole decoy files, allowing the DoD to identify their infrastructure.
        
**D. AI-Generated Decoys**

- **What it does**: Use generative AI to create fake personas, documents, or communication trails.
    
- **Example**:
    
    - **Fake Employee Profiles (2023)**: A European energy company used CounterCraft’s AI to generate fake LinkedIn profiles and email trails. APT29 (Cozy Bear) spent months targeting these "employees," enabling defenders to redirect and study the attacks.
        
##### **How Honey* Technologies Help**

1. **Early Threat Detection**: Alerts defenders to intrusions before critical systems are breached.
    
2. **Threat Intelligence**: Reveals attacker TTPs (tools, exploits, workflows).
    
3. **Attack Diversion**: Distracts adversaries with decoys, reducing risk to real assets.
    
4. **Forensic Analysis**: Provides data to improve defenses and incident response.
    
---

##### **Challenges**

- **Resource Intensity**: Requires effort to maintain realistic decoys.
- **False Positives**: Legitimate users may accidentally trigger alerts.
- **Ethical/Legal Considerations**: Entrapment risks in certain jurisdictions.
    
---
##### **Key Takeaways**

- **Honeypots/Honeynets**: Ideal for researching advanced threats.
- **Honey Tokens/Files**: Simple to deploy for credential theft and insider threat detection.
- **Honey Credentials/DBs**: Effective against credential stuffing and data exfiltration.
- 
---
#### **2. Disruption Technologies**

Disruption technologies actively interfere with cyberattacks, rendering them ineffective or sabotaging attackers’ infrastructure.

##### **Examples**

**A. Ransomware Countermeasures**

- **What it does**: Tools that detect ransomware behavior (e.g., mass file encryption) and halt execution.
    
- **Example**:
    
    - **CryptoDrop (2020)**: A U.S. hospital used CryptoDrop to detect ransomware encrypting patient records. The tool automatically isolated infected devices, stopping the attack before critical systems were locked.
        

**B. Sinkholing Botnets**

- **What it does**: Redirect malicious traffic from botnet-infected devices to controlled servers.
    
- **Example**:
    
    - **Emotet Takedown (2021)**: Law enforcement agencies sinkholed Emotet’s command-and-control (C2) servers, redirecting traffic to government-controlled servers. This disrupted the botnet’s operations and led to its dismantling.
        

**C. Moving Target Defense (MTD)**

- **What it does**: Dynamically change system configurations (e.g., IP addresses, ports) to confuse attackers.
    
- **Example**:
    
    - **U.S. Air Force Cyber Avionics (2022)**: The Air Force deployed MTD to randomize network configurations in real-time. APT28 (Fancy Bear) failed to maintain persistence during a breach attempt, as their exploits became obsolete within minutes.
        

**D. Adversarial Machine Learning**

- **What it does**: Poison AI models used by attackers (e.g., to bypass malware detection).
    
- **Example**:
    
    - **Countering Deepfake Phishing (2023)**: A bank injected adversarial noise into its public-facing employee images, causing AI tools used by the Lazarus Group to generate distorted deepfakes. The fake videos were easily spotted by staff.
        

**E. Quantum Disruption**

- **What it does**: Use quantum computing to break encryption or secure communications.
    
- **Example**:
    
    - **Quantum Key Distribution (QKD)**: Companies like Toshiba use QKD to create unbreakable encryption keys. In 2023, a Chinese APT group’s attempt to intercept a financial transaction in Singapore was foiled when QKD detected eavesdropping and terminated the session.
        

---

#### **Key Takeaways for Defenders**

1. **Deception**:
    
    - Deploy honeypots to waste attackers’ time and gather intelligence.
        
    - Use honey tokens to detect insider threats or credential theft.
        
2. **Disruption**:
    
    - Integrate ransomware rollback tools (e.g., **CrowdStrike’s OverWatch**).
        
    - Partner with ISPs or law enforcement to sinkhole botnet traffic.
        
3. **Emerging Tech**:
    
    - Adopt AI-driven deception grids for dynamic, evolving traps.
        
    - Prepare for quantum-era threats by testing post-quantum cryptography.
        

---

#### **Real-World Case Study: Colonial Pipeline (2021)**

- **Deception**: After the DarkSide ransomware attack, Colonial Pipeline added **decoy SCADA systems** to their OT network. When attackers returned, they targeted fake controls, giving defenders time to respond.
    
- **Disruption**: The company partnered with Amazon AWS to sinkhole DarkSide’s payment portal, delaying ransom negotiations.



> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions/1) 
{: .prompt-info }