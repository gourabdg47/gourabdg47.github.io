---
title: Introduction to Phishing
author: gourabdg47
date: 25-07-11 01:23:00 +0500
categories:
  - Breach Detected
  - SOC-101
tags:
  - study
  - cybersecurity
  - phishing_analysis
render_with_liquid: false
---
### Introduction to Phishing

#### Phishing 
Phishing is the act of attempting to obtain sensitive information from individuals by using social engineering tactics over various communication platforms such as email, SMS, phone calls and internet. 

- **Impersonation** : Posing as legitimate organization or individuals
- **Stealing sensitive information** : Passwords, credit card numbers, sensitive files
- **Deliver and install malware** : Via attachments, embedded files or URLs
- **Exploiting humans** : Preys on emotions, Human psychology

#### How does Phishing works ?
-  **Authority** : Spoofing executives, managers, IT staff
- **Trust** : Spoofing customers, bank, partners
- **Intimidation** : Install a sense of fear of consequences
- **Social Proof** : Validate legitimacy through consensus
- **Urgency** : "Act Now!"
- **Scarcity** : Install a fear of missing out
- **Familiarity** : Establish credibility through recognition 

#### Case studies
###### 1. Colonial Pipeline cyberattack in May 2021

The Colonial Pipeline cyberattack in May 2021 was a significant incident that highlighted the vulnerabilities of critical infrastructure to ransomware. While it's often referred to as a "phishing case study," the initial access vector was more specifically a **compromised Virtual Private Network (VPN) password that lacked multi-factor authentication (MFA).** However, it's crucial to understand that **phishing is a common method for obtaining such credentials.**

Here's a breakdown of the Colonial Pipeline incident as a case study:

**The Attack:**

- **Target:** Colonial Pipeline Company, the largest refined oil products pipeline in the United States, supplying about 45% of the East Coast's fuel.
    
- **Attacker:** DarkSide, a Russian-based cybercriminal group operating a "ransomware-as-a-service" (RaaS) model.
    
- **Initial Access:** The attackers gained entry to Colonial Pipeline's network through a compromised password for an inactive VPN account. Crucially, this VPN account **did not have multi-factor authentication (MFA) enabled.** While the exact method of obtaining this password hasn't been definitively stated as direct phishing _in this specific instance_, it's a highly probable and common scenario for credential theft. It's often suggested the password may have been found on the dark web after a previous breach, which could have originated from a past phishing incident.
    
- **Lateral Movement and Ransomware Deployment:** Once inside, DarkSide actors moved laterally through Colonial's IT network, stealing approximately 100 gigabytes of data and then deploying their ransomware, encrypting critical business data.
    
- **Impact:** Colonial Pipeline proactively shut down its entire pipeline system as a precaution to contain the spread of the ransomware. This led to widespread fuel shortages, panic buying, and significant price increases across the southeastern United States, impacting millions of people and causing a national state of emergency.
    
- **Ransom Payment:** Colonial Pipeline controversially paid the DarkSide group a ransom of approximately $4.4 million in Bitcoin to receive a decryption tool and restore their systems.10 The U.S. Department of Justice later recovered a significant portion of this ransom (around $2.3 million due to Bitcoin's fluctuating value).

**Key Takeaways and "Phishing" Relevance:**

While the direct "phishing email" might not have been the _final_ step, the incident underscores how easily initial access can be gained through weak authentication, which is often a downstream effect of successful phishing campaigns.

- **The "Human Factor" Remains Critical:** Even sophisticated cyberattacks often exploit human vulnerabilities. If the compromised password for the VPN account was obtained through a previous phishing scam targeting an employee, it perfectly illustrates how such seemingly small compromises can lead to massive disruptions.
    
- **Importance of Multi-Factor Authentication (MFA):** This was the single most glaring cybersecurity failing in the Colonial Pipeline case. Had MFA been enabled on that VPN account, even with a compromised password, the attackers would have been blocked from gaining access. This is a fundamental defense against credential theft, whether from phishing or other means.
    
- **Password Hygiene:** The use of an inactive account with a presumably weak or reused password was a critical vulnerability. Strong, unique passwords are essential, and their compromise, often via phishing, is a primary entry point for attackers.
    
- **Network Segmentation:** While the ransomware affected the IT network, Colonial Pipeline's operational technology (OT) network (which controls the physical pipeline) was reportedly not directly compromised. However, the company still had to shut down operations as a precaution due to the inability to manage billing and other IT-dependent functions, highlighting the interconnectedness and the importance of strong segmentation between IT and OT networks.
    
- **Incident Response and Business Continuity:** The attack exposed gaps in Colonial's incident response and recovery plans, leading to prolonged disruption.
    
- **Critical Infrastructure Vulnerability:** The incident served as a stark reminder of how vulnerable critical infrastructure is to cyberattacks and the cascading effects such attacks can have on national security, economy, and daily life.
    
In essence, while the Colonial Pipeline attack was a ransomware incident, its root cause (compromised credentials lacking MFA) is precisely the kind of vulnerability that phishing attacks are designed to exploit. It served as a powerful case study for the entire cybersecurity community on the need for basic cyber hygiene, especially MFA, to prevent devastating breaches.

*Read more* : [abnormal.ai](https://abnormal.ai/blog/colonial-pipeline-attack-phishing-email-likely-the-culprit)

###### 2. Levitas Capital  cyberattack in 2020

The Levitas Capital phishing case study in 2020 is a stark reminder of how a seemingly simple phishing attack can lead to devastating consequences, even for sophisticated financial institutions. This incident demonstrates a classic example of **Business Email Compromise (BEC)** initiated by a phishing attempt.

**The Attack on Levitas Capital:**

- **Target:** Levitas Capital, an Australian hedge fund.
    
- **Method:** A co-founder of Levitas Capital received a **spear-phishing email** containing a **fake Zoom meeting invitation**. Given the widespread adoption of Zoom during the 2020 pandemic, this social engineering tactic was highly effective and topical.
    
- **Initial Compromise:** When the co-founder clicked on the malicious link within the fake Zoom invite, **malware was installed on their computer and infiltrated the hedge fund's corporate network**. This malware specifically granted the attackers control over the co-founder's email system.
    
- **Business Email Compromise (BEC):** With access to the co-founder's email, the attackers were able to monitor email communications, understand the firm's payment procedures, and impersonate the co-founder. They then created and sent **fraudulent invoices** to the fund's trustee and third-party administrator (Apex, the fund administrator, and AET Corporate Trust, the trustee).
    
- **Fraudulent Transactions:**
    
    - The attackers sent a fake invoice requesting a $1.2 million "capital call" to a company called "Unique Star Trading" (a shell company controlled by the attackers).
        
    - The fund administrator, Apex, did make an initial call to the co-founder to verify the transaction. However, the co-founder was at the gym and said he would call back. In the interim, the hackers, having control of his email, sent a _fake email from his compromised account_ authorizing the transfer. This ultimately led to the transfer of $1.2 million. A portion of this, approximately $781,000, was withdrawn by an individual who then fled the country.
        
    - Subsequently, two more fraudulent transfers were initiated: $2.5 million to an account in Hong Kong and $5 million to an account in Singapore. Fortunately, the co-founder noticed the missing funds (over $8 million in total initiated payments) and was able to stop these later transfers before the money cleared, effectively saving $7.5 million.

**Consequences for Levitas Capital:**

- **Significant Financial Loss:** While $7.5 million was recovered, the firm still lost approximately **$800,000** (the portion of the initial $1.2 million that was withdrawn).
- **Reputational Damage:** The incident severely damaged Levitas Capital's reputation in the highly trust-dependent financial industry.
- **Loss of Major Client:** Their largest institutional client, Australian Catholic Super, which had a planned $16 million additional investment, pulled its funds due to concerns about the security breach.
- **Company Closure:** As a direct result of the financial losses and, more significantly, the severe reputational damage and client attrition, Levitas Capital was forced to **shut down its operations**. This demonstrates that even if direct monetary losses are partially recovered, the collateral damage from a cyberattack can be fatal for a business.

**Key Lessons from Levitas Capital:**

1. **Human Element as the Weakest Link:** This case perfectly illustrates that even with technological defenses, a single human error (clicking on a malicious link) can unravel an entire organization's security.
    
2. **Sophistication of Phishing:** The attackers used a highly relevant and convincing lure (Zoom invite during the pandemic) and combined it with Business Email Compromise (BEC) tactics, which involve deep knowledge of an organization's communication and payment workflows.
    
3. **Importance of Verification Processes:** The incident highlights the failure of established verification processes. While a phone call was made for the first transfer, the follow-up email from the compromised account was enough to bypass further scrutiny. This emphasizes the need for:
    
    - **Out-of-band verification:** If a high-value transfer is requested via email, a _separate and independent_ method (e.g., a phone call to a _known and verified_ number, not one provided in the email) should be used to confirm the request.
        
    - **Clear and strict payment authorization protocols:** These protocols should not be easily circumvented, even by C-level executives via email alone.
        
4. **Endpoint Security:** The malware installation points to a weakness in endpoint detection and protection. Robust anti-malware and Endpoint Detection and Response (EDR) solutions are crucial.
    
5. **Business Continuity and Incident Response:** Despite recovering most of the funds, the inability to manage the reputational fallout and retain clients demonstrates a lack of robust incident response planning that extended beyond technical recovery to business continuity and crisis communication.
    
6. **Consequences Beyond Direct Financial Loss:** The ultimate closure of the hedge fund underscores that financial theft is just one facet of cyber risk. Reputational damage and loss of trust can be far more destructive.

The Levitas Capital incident is a prime example of why comprehensive cybersecurity training, strong internal controls, and a robust incident response plan are essential, especially for organizations handling significant financial assets.

*Read more*: [www.secureworld.io](https://www.secureworld.io/industry-news/hedge-fund-closes-after-bec-cyber-attac)

###### 3. Ubiquiti Networks security incident in 2015

The Ubiquiti Networks security incident in 2015 is a crucial case study, primarily because it's a textbook example of a **Business Email Compromise (BEC) fraud**, often initiated or facilitated by **spear phishing**.1 While the term "phishing" is broadly applied, this specific incident highlights the targeted and sophisticated nature of BEC.

**The Attack on Ubiquiti Networks in 2015:**

- **Target:** Ubiquiti Networks, a well-known manufacturer of wireless networking products.
    
- **Attack Type:** Business Email Compromise (BEC) / CEO Fraud. This involves impersonating a high-ranking executive (like the CEO or CFO) to trick an employee into performing unauthorized wire transfers.
    
- **Initial Access/Method (Likely Phishing-Related):** While Ubiquiti's official statements were initially somewhat vague about the precise technical entry point, security experts and subsequent analysis strongly suggested that the fraud likely began with:
    
    - **Phishing or spear-phishing:** This is the most common method for attackers to gain access to an executive's email account. A targeted email (spear phishing) would have been sent to an executive, likely with a malicious link or attachment designed to steal credentials or install malware.
        
    - **Email spoofing or domain look-alike:** Attackers might have registered a domain name very similar to Ubiquiti's (e.g., "ubiquti.com" instead of "ubiquiti.com") to send convincing emails that appear to come from an internal executive. The "reply-to" address would be controlled by the attackers.
        
- **The Deception:** Once the attackers either compromised an executive's email account or successfully spoofed their identity, they sent **fraudulent wire transfer requests** to Ubiquiti's finance department. These requests appeared to come from a senior executive, demanding large sums of money to be wired to overseas accounts.
    
- **The Loss:** Ubiquiti Networks reported in an SEC filing that they were a victim of a criminal fraud that resulted in transfers of **$46.7 million** from a Hong Kong subsidiary to other overseas accounts held by third parties.
    
- **Recovery:** Through immediate action, Ubiquiti was able to recover approximately $8.1 million (and later expected to recover another $6.8 million), but a significant portion of the funds, around $31.8 million, was lost.
    
- **Internal Control Weaknesses:** An independent investigation concluded that Ubiquiti's internal control over financial reporting was **ineffective due to one or more material weaknesses** related to this incident. Their Chief Accounting Officer resigned following the breach.
    

**Key Lessons from the Ubiquiti Networks 2015 Incident:**

1. **Business Email Compromise (BEC) is a Major Threat:** This case, along with many others, solidified BEC as one of the most financially damaging cybercrime types for businesses. It doesn't necessarily involve technical hacking of systems, but rather sophisticated social engineering.
    
2. **The "Human Firewall" is Critical:** Even if technical systems are secure, the human element remains the primary vulnerability in BEC attacks. Employees, especially those in finance, need rigorous training to identify and respond to suspicious requests.
    
3. **Robust Financial Verification Processes are Paramount:** Relying solely on email for high-value financial transactions is a critical flaw. Organizations must implement **out-of-band verification** protocols, requiring confirmation of wire transfers via a separate, trusted communication channel (e.g., a direct phone call to a _known_ number of the requesting executive, not a number provided in the suspicious email).
    
4. **Awareness of Social Engineering Tactics:** Training should cover common BEC indicators, such as:
    
    - Requests for urgent, high-value transfers.
    - Unusual payment destinations (especially overseas).
    - Changes in vendor payment details.
    - Emails sent outside normal business hours.
    - Emails with subtle spelling errors in domain names (e.g., "ubiquti.com" instead of "ubiquiti.com").
    - Pressure tactics ("Don't tell anyone about this, it's confidential").
        
5. **Importance of Email Security:** While the _internal_ systems weren't necessarily "penetrated" in the way a malware attack would, robust email security (like DMARC, SPF, DKIM) can help prevent email spoofing, and advanced threat protection can flag suspicious emails before they reach employee inboxes.
    
6. **Consequences Beyond Financial Loss:** The significant financial hit and the resignation of a key executive highlight the severe impact these "non-technical" cyber frauds can have on a company's financial health and leadership.
    
The Ubiquiti 2015 case served as a major wake-up call for companies globally about the insidious nature of BEC and the absolute necessity of strengthening human and procedural controls, alongside technical defenses, to combat such sophisticated social engineering attacks.

*Read more* : [krebsonsecurity.com](https://krebsonsecurity.com/2015/08/tech-firm-ubiquiti-suffers-46m-cyberheist/)

###### 4. 2015 Ukraine power grid cyberattack

The 2015 Ukraine power grid cyberattack was a landmark event, recognized as the **first publicly acknowledged successful cyberattack to cause a power outage**. Phishing played a crucial role as the initial access vector in this highly sophisticated and coordinated attack

**The Attack on the Ukrainian Power Grid (December 23, 2015):**

- **Target:** Three regional power distribution companies in Ukraine (Kyivoblenergo, Prykarpattyaoblenergo, and Chernivtsioblenergo).
    
- **Attacker:** The attack is widely attributed to the Russian advanced persistent threat (APT) group known as **Sandworm** (also known as APT28 or Voodoo Bear).
    
- **Initial Access - Spear Phishing:** The "seeds" of the attack were planted months in advance, reportedly as early as **Spring 2015**. The attackers gained their initial foothold into the IT networks of the utilities through **spear-phishing emails**.
    
    - These emails contained **malicious Microsoft Office attachments** (likely Excel or Word documents).
        
    - When an unsuspecting employee opened the attachment, it triggered the installation of **BlackEnergy 3 malware**. The emails often appeared to be from trusted sources, like the Ukrainian parliament, leveraging social engineering to trick victims.
        
- **Reconnaissance and Lateral Movement:** Once the BlackEnergy malware was installed on an employee's computer, it allowed the attackers to:
    
    - Conduct extensive **reconnaissance** on both the IT (business) and OT (operational technology - SCADA/ICS) networks. This involved scanning networks, identifying vulnerabilities, mapping the infrastructure, and collecting credentials.
        
    - Gain access to **Virtual Private Network (VPN) credentials** used by grid operators to remotely access control centers
    - Move laterally from the IT network into the critical **SCADA/ICS networks**, which control the physical equipment of the power grid. This was possible due to insufficient segmentation between the IT and OT environments.
        
- **The Attack Execution:** On December 23, 2015, the attackers launched a coordinated multi-pronged assault:
    
    - **Remote Disconnection:** They used their access to the SCADA systems to remotely open circuit breakers at approximately 30 substations, cutting power to over 225,000 customers for several hours. In some cases, they remotely controlled the operator's Human-Machine Interface (HMI) mouse to switch off breakers.
        
    - **Impeding Recovery:** To further hinder recovery efforts, the attackers:
        
        - Used **KillDisk malware** to wipe data and render critical IT systems (servers, workstations) inoperable
        - Overwrote the firmware on serial-to-ethernet converters, making devices unrecoverable and blocking remote commands to restore power
        - Launched a **denial-of-service (DoS) attack** on the utilities' customer call centers, preventing customers from reporting outages and overwhelming response efforts
        - Even turned off uninterruptible power supplies (UPS) at some control centers.
            
- **Recovery:** Power was eventually restored, but largely through manual efforts, highlighting the resilience of human operators in the face of sophisticated cyberattacks.

**Key Lessons from the 2015 Ukraine Power Grid Attack:**

1. **Phishing as a Critical Initial Access Vector:** This attack definitively proved that seemingly simple spear-phishing campaigns can be the entry point for highly destructive attacks on critical infrastructure.
    
2. **Importance of IT/OT Segregation:** The ability of the attackers to traverse from the IT network to the OT network was a major vulnerability. Strict network segmentation, with firewalls and proper access controls between IT and OT, is crucial to prevent such lateral movement.
    
3. **Employee Training is Essential:** Despite sophisticated malware, the attack began with an employee opening a malicious attachment. Continuous, targeted cybersecurity awareness training for all employees, especially those with access to sensitive systems, is paramount.
    
4. **Multi-Factor Authentication (MFA):** Strong authentication for all remote access (like VPNs) and critical systems would have significantly hampered the attackers' ability to gain and maintain access.
    
5. **Robust Incident Response and Recovery:** The attack highlighted the need for comprehensive incident response plans that include not just technical recovery but also communication strategies and even manual override procedures for critical infrastructure.
    
6. **Supply Chain Risk:** While not the primary focus of this specific attack, the nature of industrial control systems often involves a complex supply chain. Malware introduced through vendor systems or updates remains a significant concern.
    
7. **Threat Intelligence Sharing:** The detailed analysis of this attack by cybersecurity researchers and government agencies provided invaluable insights for critical infrastructure operators worldwide, emphasizing the importance of threat intelligence sharing.
    
8. **The "Long Game" of APTs:** The attack wasn't a sudden burst; it involved months of reconnaissance and planning, demonstrating the patience and persistence of nation-state-backed threat actors. Organizations need continuous monitoring and threat hunting to detect such long-term intrusions.

The 2015 Ukraine power grid attack served as a wake-up call globally about the real-world, kinetic effects that cyberattacks can have, pushing critical infrastructure sectors to re-evaluate and strengthen their cybersecurity defenses against even the most basic, yet effective, tactics like phishing.

*Read more* : [wikipedia.org](https://en.wikipedia.org/wiki/2015_Ukraine_power_grid_hack)




> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions/1) 
{: .prompt-info }
