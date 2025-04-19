---
title: Revision Topics
author: gourabdg47
date: 2025-04-10 18:32
categories:
  - Information
  - Security +
tags:
  - reading
  - certification
  - imp
render_with_liquid: true
pin: "false"
---
# **Revision Topics**

So here's what happening, I doubt that I will pass the exam (CompTIA Security+). There are so many topics, I am getting confused. I will pickup some topics I think I am weak at and study them from different sources. 

The chapter "**Risk Management & Privacy**" have something called " *different data roles* ". These roles helps to clarify responsibilities for **managing & protecting** data within an organization. 

#### Different data roles outlined

1. **Data Owners**  : These are senior executives who are designated responsibility for different data types. E.G. VP of HR might be the data owner of employment and payroll data. Data owners understands the impact of there decisions about there data on there business. They delegate responsibilities and rely of advice from subject matter experts. 
2. **Data Subjects** : These are individuals whose data is being processed. This includes customers, employee and partners. Data subjects often have rights to there data like right to *access*, *correct* & *request deletion*.
3. **Data Controllers** : These are individuals who defines the reason from processing personal information and direct the method of processing the data. They serves as the substitute of **Data Owners** to avoid the presumption of ownership.
4. **Data Stewards** : There are induvial who carry out the intent of "**Data Controller**" and are delegated responsibility from the controller.
5. **Data Custodian** : These are individuals or teams responsible for the secure safekeeping of the information but do not have **controller**    or **stewardship** responsibility.
6. **Data Processors** : These are service providers that process personal information on behalf of a data controller. E.G. A credit card processing service for a retailer. The retailer remains a data controller while the service acts as a data processor. 
7. **Data Protection Officer (DPO)** : A specific individual who bears the overall responsible for an organization's data privacy efforts. The chief privacy officer often holds this role. 
8. **Continuous Integration** (CI) is a software development practice where developers frequently merge code changes into a shared repository, often several times a day. Each integration is then automatically verified by building the software and running automated tests to detect issues early.

---

#### From Security Governance and Compliance, different agreement types

1. **Service-Level Agreements (SLA)** : Written contracts that specify the conditions of service that will be provided by the vendor and the remedies available to the customer if the vendor fails to meet the SLA. Covered issues such as **system availability**, **data durability**, and **response time**.
2. **Memorandum of agreement (MOA)** : This is a letter written to document aspects of a relationship. In simple term this is like a pre-contract where everyone involved agrees on certain terms, responsibilities, and rules before working together.
3. **Master Service Agreement (MSA)** : This provides an umbrella contract for the work the vender does with an organization over an extended period of time. This agreement typically includes detailed security and privacy requirements 
4. **Work Order (WO) / Statement of work (SOW)** : When an organization have a **MSA** with a vendor, they may create a **WO** or **SOW** for new project. The SOW outlines the specific services to be provided by the vendor, along with associated timelines and costs.
5. **Non-Disclosure Agreement (NDA)** : This is an agreement used to protect sensitive information. NDA are crucial when sharing confidential data with the vendors and should be included in the vender agreements. 
6. **Business Partner Agreement (BPA)** : It is an agreement outlining the terms of a partnership between two or more business entities.

---

#### Categories of modern encryption algorithms

- **Symmetric Key Algorithms**  : These algorithms use single, shared secret key from encryption & decryption. All communicating parties possess a copy of this secret key. 
	1. **Data Encryption Standard (DES)** : Published in 1977, it was once a standard but is no longer considered secure due to flaws in the algorithm and short key length . It has been superseded by AES
	2. **Triple DES (3DES)**: An improvement over DES,  but still considered less secure and efficient than AES
	3. **Advanced Encryption Standard (AES)** : This is a strong symmetric encryption algorithm and the successor to DES7 .... It is widely used in various applications, including wireless network security (WPA3), TLS, and file/disk encryption
	
**Key management**,  including secure creation, distribution, storage, destruction, recovery and  <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Escrow of secret keys refers to a system where a third party securely stores a protected copy of an encryption key">Escrow of secret keys</span> , is crucial for symmetric cryptography .  Key exchange is a significant challenge, with methods including offline distribution, public key encryption, and the Diffie-Hellman key exchange algorithm
**Symmetric encryption** is *generally fast and efficient* for bulk encryption.  However,  it does not provide 
<span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Non-Repudiation means that someone who performed an action cannot later deny having taken that action">Non-Repudiation</span> 

- **Asymmetric Key Algorithms** :  Also known as public key algorithms, these systems use two mathematically related keys for each user: a public key, which can be shared with anyone, and a private key, which is kept secret by the owner.

**Asymmetric cryptography** solves the key exchange problem of symmetric cryptography as public keys can be freely shared. It also provides <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Authentication is the process of verifying the claimed identity of a subject. It ensures that the subject (typically a person, application, device, system, or organization) is who or what they claim to be">Authentication</span>  and <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Non-Repudiation means that someone who performed an action cannot later deny having taken that action">Non-Repudiation</span>  through the use of digital signatures.

#### Importance of Choosing Appropriate Cryptographic Solutions
- <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="You must choose a system that aligns with the specific security requirements, whether it's confidentiality, integrity, authentication, or non-repudiation">Meeting Security Goals</span>
- <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Using weak or deprecated algorithms (like DES) can leave data vulnerable">Strength of the Algorithm</span>
- <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Longer keys generally require more computational power to break">Key Length</span>
- <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Even with a strong algorithm and long key, weak key management can compromise security. Secure creation, distribution, storage, and destruction of keys are crucial">Key Management Practices</span>
- <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Understanding common attacks like downgrade attacks, collision attacks, brute-force attacks, and chosen plaintext attacks helps in selecting algorithms and configurations that offer better resistance">Resistance to Attacks</span>
- <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Symmetric encryption is generally faster and more suitable for encrypting large amounts of data, while asymmetric encryption is slower but offers advantages in key management and non-repudiation">Performance Requirements</span>
- <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Organizations may be required to use specific cryptographic standards and algorithms to comply with regulations">Compliance and Standards</span>

---
#### Mitigation Techniques for Endpoints

1. **Patching**

	- Ensure operating systems and software are up to date to remove known vulnerabilities.
	- Timely patching reduces the window of opportunity for exploits.
	- Implement patch management processes to control and streamline updates.
    
2.  **Encryption**

	- Encrypt data on endpoints (full disk or specific files) to prevent unauthorized access.
	- Use tools like **Trusted Platform Modules (TPM)** and **Hardware Security Modules (HSM)** to manage encryption keys securely.
    
3. **Configuration Enforcement**

	- Maintain secure baselines and enforce configurations to reduce vulnerabilities.
	- Leverage tools like **Group Policy** (Windows) and **SELinux** (Linux) for policy enforcement.
    
4. **Decommissioning**
	
	- Sanitize or destroy data on retired systems.
	- Securely handle hardware to prevent exposure of sensitive data.
    
##### Hardening Techniques

Harden systems by reducing attack surfaces and enhancing security settings:

- **Encryption**: (Already covered above, but also part of hardening).
- **Installation of endpoint protection**: Deploy antivirus, antimalware, EDR, and XDR tools to detect, prevent, and remediate threats.
- **Host-based firewall**: Enable firewalls on endpoints to filter traffic by applications, ports, protocols, and services.
- **Host-based intrusion prevention system (HIPS)**: Monitor and block malicious endpoint activities.
- **Disabling ports/protocols**: Close unnecessary ports and protocols; limit interactions to essential services.
- **Default password changes**: Replace vendor defaults with strong, unique passwords.
- **Removal of unnecessary software**: Uninstall unused applications/services to minimize vulnerabilities.

---

#### Security controls
###### Categories 
1. <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Enforce confidentiality, integrity, and availability in the digital space . Examples include firewall rules, access control lists (ACLs), intrusion prevention systems (IPS) and encryption">Technical Controls</span>
2. <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Consist of the high-level plans and programs that direct the security efforts of an organization. They often involve risk assessment, security awareness training, and the development and implementation of security policies">Managerial Controls</span>
3. <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Processes put in place to manage technology in a secure manner. Examples include user access reviews , log monitoring, and vulnerability management">Operational Controls</span>
4. <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Tangible protection mechanisms designed to guard physical assets and access to them. Examples include biometric locks4 , access control vestibules, fencing, video surveillance , security guards, access badges, and lighting">Physical Controls </span>

###### Security Control Types
1. <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Aim to stop a security issue before it occurs2 . Firewalls and encryption are examples">Preventive controls</span>
2. <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Seeks to prevent an attacker from attempting to violate security policies. E.G. Sign board, fence">Deterrent controls</span>
3. <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Identify security events that have already occurred. E.G. Intrusion detection systems (IDS)">Detective controls</span>
4. <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Remediate security issues that have already occurred. E.G. Restoring backups after a ransomware attack">Corrective controls</span>
5. <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="Mitigate the risk associated with exceptions made to a security policy">Compensating controls</span>
6. <span style="border-bottom: 1px dotted; cursor: help; font-weight: bold;" title="inform employees and others what they should do to achieve security objectives. E.G. Policies and procedures">Directive controls</span>

---
#### Difference between stateful and stateless firewalls

###### Stateless Firewall
A **stateless firewall** filters packets based only on predefined rules like IP address, port, or protocol **without keeping track of connection state**.

**Key Characteristics:**

- Examines **each packet individually**
- Doesn't remember past traffic
- Faster, but less secure
- Commonly used for **simple packet filtering**
    
**Example Rule:**  
Allow TCP traffic from IP `192.168.1.5` on port `80`.

###### Stateful Firewall
A **stateful firewall** tracks the **state of active connections** and makes decisions based on the context of traffic (e.g., whether a packet is part of an existing connection).

**Key Characteristics:**

- Maintains a **state table** (connection tracking)
- Smarter, more secure
- Can detect and block **unauthorized or suspicious traffic**
- Used in **modern firewalls and enterprise setups**

**Example Behavior:**  
Allows a response packet only if it matches a previously initiated and allowed connection.


| Feature            | Stateless Firewall        | Stateful Firewall            |
| ------------------ | ------------------------- | ---------------------------- |
| Tracks connections | ❌ No                      | ✅ Yes                        |
| Performance        | ⚡ Faster                  | 🛡️ More resource-intensive  |
| Security           | 🚧 Basic filtering only   | 🔒 Context-aware filtering   |
| Use Case           | Simple, low-risk networks | Enterprise, complex networks |

---

#### Podcast of Security Controls & Security Operations  (AI Generated)


<audio controls>
  <source src="https://github.com/gourabdg47/gourabdg47.github.io/raw/main/assets/audio_vids/Security_controls_Security_operations_podcast.wav" type="audio/wav">
  Your browser doesn’t support audio. [Download instead](https://github.com/gourabdg47/gourabdg47.github.io/raw/main/assets/audio_vids/CTI%20Resume.wav).
</audio>

---

##### Practices 

- Regulatory audit : A systematic examination of an organization's compliance with regulations 
- Sender Policy Framework (SPF) : A framework to prevent e-mail spoofing 
- Network Access Control (NAC) : A security solution that enforces policies on device accessing the network
- Domain Based Message Authentication (DMARC) : Referring to **email authentication techniques** that verify if an email was genuinely sent from a domain it claims to come from
- Domain Key Identified Main (DKIM) : It is an **email authentication method** that allows the receiver of an email to **verify that it was sent by an authorized mail server** and **was not altered in transit**
- E-Discovery : The process of identifying, collecting and producing electronically stored information
- Supervisory Control and Data Acquisition (SCADA) : It is a  control system architecture used to monitor and manage industrial processes. It combines hardware and software to collect real-time data from sensors and devices, process and analyze it, and provide operators with a graphical interface to supervise and control operations.
- Deauthentication : Commonly associated with wireless network. This attack mostly cause loss of connectivity. 
- Federation : Allows members of an organization to authenticate using credentials from another organization
- Mean Time Before Failures (MTBF) : Prediction on how often a repairable system will fail
- Recovery Time Objectives (RTO) : Objectives required to restore a particular service level
- Mean Time To Restore (MTTR) : The amount of time requires to restore a component
- Segmenting : Segmenting the servers to their own protected network would allow for additional security controls while still maintaining the uptime and availability of the systems.
- Journaling : Writes data to a temporary journal before writing the information to the database. If power is lost, the system can recover the last transaction from the journal when power is restored.
- Mobile Device Management (MDM) : A centralized management system for mobile device.
- Corporately Owned and Personally Enabled (COPE) : Is commonly purchased by the corporation and allows the use of the mobile device for both business and personal use.
- Escalation : Automation can recognize a security event and security related ticket to the incident response team without any additional human interaction.
- Guard Rails : They are set by application developers to provide a set of automated validations to user input and behavior. 
- 802.1X : A centralized authentication server, and this allows all users to use their corporate credentials during the login process.
- Pre-Shared Key (PSK) : A wireless authentication configuration that allows each user on the network to connect using same key / password
- Configuration enforcement : A posture assessment evaluates the configuration of a system to ensure all configurations and applications are up to date and secure as possible.
- Discretionary Access Model : This models allows the owner of the resource to control who has access. 
- Mandatory Access Control : Allows access to the resource based on the security level assigned to an object. Only users with object's assigned  security clearance or above can access. 
- Supervisor Control and Data Acquisition (SCADA) : Is a data **`Hardning`** process for industrial system might include network segmentation, additional firewall and access control list.
- Configuration enforcement : Many organizations will perform a posture assessment during the login process to verify the proper security controls are in place. If the device does not pass the assessment, the system can be quarantined and any missing security updates can then be installed.
- Account lockout : In this example, there were no errors or notifications regarding the account or authentication status.
- Decommissioning : The decommissioning process is often used to permanently remove devices from the network. In this example, the laptop mitigation would allow the device to return to the network once the updates were complete.
- Sideloading : Sideloading describes the installation of software on a mobile device through the use of third-party operating systems or websites.
- Compensating Security Control : This control does not prevent an attack but does restore from attack using other means 
- Responsibility matrix : A cloud responsibility matrix is usually published by the provider to document the responsibilities for all cloud-based services.
- Playbook : A playbook provides conditional steps to follow when managing an organization's processes and procedures.
*Well from time to time, you can see my thoughts pouring here or just raw opinions. Well its my dam blog, I can write what ever tf I want but I do make sure the information I write here are accurate because I am also studying from them for this dam exam ...*  
- Instant messaging : Instant messaging is commonly used as an attack vector, and one way to help protect against malicious links delivered by instant messaging is a host-based firewall.
- Web Application Firewall (WAF) : Protects against web application attacks like XSS, SQL Injection
- Content Delivery Network (CDN) : Helps to distribute and absorb large volume of traffic (DDOS attack),  mitigating its impact  and keeping web server available to legitimate users.
- Diffie-Hellman key exchange : Key exchange is a cryptographic protocol that allows two parties to securely exchange cryptographic keys over an unsecured communication channel
- Cross-site request forgery (CSRF) : Exploits the trust that a web application has in the user's browser. It tricks the user into submitting a request, such as clicking a link or loading a page, that performs an action on a site where the user is authenticated.
- Enable remote wipe : Allows the data on a mobile device to be erased remotely in case the device is lost or stolen, thus preventing unauthorized access to sensitive information.
- Secure/Multipurpose Internet Mail Extensions (S/MIME) :  Provides end-to-end encryption for email messages.
- Kerberos protocol : Kerberos is a network authentication protocol designed to provide strong authentication for user access to network services, often implemented as a single sign-on (SSO) system. It uses secret-key cryptography to authenticate users and services.
- File Integrity Monitoring (FIM) :  Detects and reports unauthorized changes to critical files.
- Public Key Infrastructure (PKI) : Provides a framework for managing digital certificates and encryption keys, ensuring secure communications.
- **Hardware tokens generate OTPs** that do not rely on an internet connection, providing a reliable MFA method for remote employees with unreliable internet access.
- Trusted Platform Module (TPM) :  Is a hardware component that provides secure generation and storage of cryptographic keys. It ensures that keys are stored securely and can only be accessed by authorized software.
- **Steganography** : Hiding messages within other non-secret text or data to avoid detection.
- **Obfuscation** : Makes data difficult to understand but does not hide it.
- Deprovisioning  : It is the process of removing or deactivating users access rights when there are no longer needed. 
- **Spraying attack** is a type of password attack that involves trying common passwords against multiple accounts.
- **Fileless malware** operates in memory, often leveraging legitimate system tools to evade detection. It might adjust registry values for persistence and can run within its own process or use tools like PowerShell to achieve its objectives.
- In **digital forensics**, the *acquisition process* refers to the methodical steps taken to collect digital evidence from a device or system in a way that ensures its integrity and usability in an investigation. This involves creating a bit-by-bit copy (or forensic image) of the original data to preserve its content while preventing any alterations during analysis.
- **Risk register** is a comprehensive record that lists all identified risks, their potential impacts, assigned risk owners, and current risk status. It serves as a central repository for tracking and monitoring risks over time.
- **Exposure factor** (EF) is the fraction of the asset value that is at risk in the event of a security incident. Asset impact can refer to the general effect on an asset but doesn't provide a quantifiable percentage like the exposure factor does.
- **Real-Time Operating System** (RTOS) prioritize performance, sometimes at the expense of security features like buffer overflow protections, potentially leaving the system susceptible to certain attacks. While cloud access can pose risks, it's not an inherent security implication of using an RTOS. RTOSs are designed for efficiency and generally don't involve the overheads from virtualization layers.
-  A **proxy server** stands between the user's computer and the internet, intercepting requests and potentially reducing the public-facing attack surface by masking the internal server, meeting the scenario requirements.
- **Session Initiation Protocol** (SIP), port 5060, is used for signaling in Voice over IP (VoIP) services. Unauthorized access to this port can result in toll fraud or unauthorized call control. Simple **Network Management Protocol** (SNMP), port 161, is used for collecting and organizing information about managed devices, and it's unrelated to VoIP services. NetBIOS, port 139, is used for file and print sharing over local networks, not for VoIP signaling. **Post Office Protocol** (POP3), port 110, is used for retrieving emails from a mail server, unrelated to VoIP services.
-  **Risk appetite** refers to an organization's willingness to take on risk in pursuit of its business objectives. It reflects the organization's strategic approach to risk and how much risk it is willing to undertake to achieve specific goals. **Risk acceptance** means that an organization understands the level of risk that in involved in an activity and is willing to accept the outcomes of taking the risk. The risk is either accepted or not, there aren't levels of risk acceptance. In this case they are not making a decision about a level of risk for a specific activity. **Risk tolerance** is the extent to which an organization is comfortable with the level of risk it is willing to take. It represents the organization's ability to withstand potential losses or disruptions. **Risk deterrence** involves taking measures to reduce or mitigate the impact of an event.
- ARO (Annualized rate of occurrence) quantifies the expected frequency of a risk occurring within a one-year time frame. While SLE (Single loss expectancy) calculates the cost of a single occurrence of a risk event, it does not account for the frequency of that event over time, which is necessary to calculate ALE. Exposure Factor (EF) determines the proportion of asset value lost per risk event, a component of SLE calculation, but not directly related to the annualized expected loss. Annualized Loss Expectancy (ALE) represents the yearly financial loss a company can expect from a specific risk, factoring in both the severity and frequency of the event.
-  Next Generation Firewall (NGFW) has several improvements over the company's previous stateful firewall, such as application awareness that can distinguish between different types of traffic, can conduct deep packet inspection and use signature-based intrusion detection, and has the ability to be integrated with various other security products. Tracking of connections and requests, allowing return traffic for outbound requests, and improving awareness of connection states on layer 4 were already features on the stateful firewall that was replaced.

 

So much is there, the thing is its not tough just that so much information ... I do love this subject and all the information ... But since I am changing my career at so late age, i believe that getting this cert might confirm my entry into cyber security field. Maybe its just a false hope, maybe it's the right step ... Time will answer the questions  !!!

---

> 💡 **Join the discussion**:  
> For questions or collaboration opportunities, visit our [ZeroDayMindset Discussion Board](https://github.com/orgs/X3N0-G0D/discussions)
{: .prompt-info }