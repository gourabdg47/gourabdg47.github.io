window.quizQuestions = [
    {
        "question": "Which of the following ensures that a sender cannot deny sending a message?",
        "options": ["Encryption", "Hashing", "Digital Signature", "Symmetric Key Exchange"],
        "answer": "Digital Signature",
        "domain": "General Security Concepts",
        "explanation": "A digital signature provides non-repudiation, which means the sender cannot deny having sent the message. It uses the sender's private key to sign the message, and anyone with the public key can verify it."
    },
    {
        "question": "Which type of threat actor is MOST likely to have the greatest resources and patience for an extended attack?",
        "options": ["Insider", "Nation-State", "Script Kiddie", "Hacktivist"],
        "answer": "Nation-State",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "Nation-state actors are sponsored by governments and have significant financial and technical resources, allowing them to conduct long-term, sophisticated campaigns (APTs)."
    },
    {
        "question": "What type of attack involves inserting malicious code into a legitimate web application to steal information from users?",
        "options": ["Phishing", "SQL Injection", "Cross-Site Scripting (XSS)", "DNS Spoofing"],
        "answer": "Cross-Site Scripting (XSS)",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "Cross-Site Scripting (XSS) is a web security vulnerability that allows an attacker to inject malicious scripts into content from otherwise trusted websites, which then execute on the victim's browser."
    },
    {
        "question": "A company needs to prevent unauthorized devices from connecting to its internal network. What technology should be used?",
        "options": ["Firewall", "VPN", "NAC (Network Access Control)", "IDS"],
        "answer": "NAC (Network Access Control)",
        "domain": "Security Architecture",
        "explanation": "Network Access Control (NAC) solutions are designed to enforce security policies on all devices seeking to access network resources, thereby preventing unauthorized devices from connecting."
    },
    {
        "question": "Which backup type saves only the changes made since the last full backup?",
        "options": ["Incremental", "Differential", "Full", "Snapshot"],
        "answer": "Differential",
        "domain": "Security Operations",
        "explanation": "A differential backup copies all files that have changed since the last full backup. This means restore times are faster than incremental, as only the last full backup and the latest differential backup are needed."
    },
    {
        "question": "What control type is a biometric fingerprint scanner?",
        "options": ["Technical", "Administrative", "Physical", "Compensating"],
        "answer": "Physical",
        "domain": "General Security Concepts",
        "explanation": "A biometric scanner is a physical control because it is a tangible device used to control physical access to a location or system."
    },
    {
        "question": "Which wireless security protocol is the most secure for corporate environments?",
        "options": ["WEP", "WPA", "WPA2-PSK", "WPA3-Enterprise"],
        "answer": "WPA3-Enterprise",
        "domain": "Security Architecture",
        "explanation": "WPA3-Enterprise provides the highest level of wireless security by using 802.1X authentication, which requires each user to authenticate with unique credentials, typically via a RADIUS server."
    },
    {
        "question": "Which of the following would BEST help mitigate risks associated with phishing attacks?",
        "options": ["IDS", "Security Awareness Training", "Firewall Rules", "Password Complexity Requirements"],
        "answer": "Security Awareness Training",
        "domain": "Security Program Management and Oversight",
        "explanation": "While technical controls help, the most effective defense against phishing is educating users. Security awareness training teaches them how to recognize and report phishing attempts."
    },
    {
        "question": "Which risk response involves buying cyber insurance?",
        "options": ["Accept", "Mitigate", "Transfer", "Avoid"],
        "answer": "Transfer",
        "domain": "Security Program Management and Oversight",
        "explanation": "Risk transference is the practice of passing a risk to a third party. Buying insurance is a classic example of transferring financial risk."
    },
    {
        "question": "Which concept is being applied when access to files is based on job roles such as HR, IT, or Accounting?",
        "options": ["MAC", "DAC", "RBAC", "ABAC"],
        "answer": "RBAC",
        "domain": "General Security Concepts",
        "explanation": "Role-Based Access Control (RBAC) assigns permissions to users based on their role within an organization, simplifying the management of user access rights."
    },
    {
        "question": "What type of malware disguises itself as a legitimate program but delivers a malicious payload?",
        "options": ["Worm", "Ransomware", "Trojan", "Rootkit"],
        "answer": "Trojan",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "A Trojan, or Trojan horse, is a type of malware that is often disguised as legitimate software. Trojans can be used by cyber-thieves and hackers trying to gain access to users' systems."
    },
    {
        "question": "Which process helps ensure that only needed ports and services are running on a server?",
        "options": ["Network segmentation", "Baseline configuration", "Change management", "Hardening"],
        "answer": "Hardening",
        "domain": "Security Operations",
        "explanation": "System hardening is the process of securing a system by reducing its surface of vulnerability. This includes disabling unnecessary ports and services to minimize potential attack vectors."
    },
    {
        "question": "A database administrator is setting access so that users only have permission to view certain data. Which principle is being applied?",
        "options": ["Separation of Duties", "Need-to-Know", "Non-repudiation", "Risk Transference"],
        "answer": "Need-to-Know",
        "domain": "General Security Concepts",
        "explanation": "The principle of need-to-know restricts access to sensitive information to only those individuals who require it to perform their job duties."
    },
    {
        "question": "What is the primary purpose of a honeypot?",
        "options": ["Encrypt sensitive data", "Divert attackers away from real systems", "Patch vulnerabilities", "Enforce firewall rules"],
        "answer": "Divert attackers away from real systems",
        "domain": "Security Operations",
        "explanation": "A honeypot is a decoy computer system designed to attract and trap attackers, diverting them from legitimate targets and allowing security teams to study their methods."
    },
    {
        "question": "During which incident response phase would you isolate a compromised server?",
        "options": ["Recovery", "Containment", "Lessons Learned", "Identification"],
        "answer": "Containment",
        "domain": "Security Operations",
        "explanation": "The containment phase of incident response focuses on limiting the damage of an attack. Isolating a compromised server from the network prevents the attack from spreading to other systems."
    },
    {
        "question": "A company is using older operating systems for their web servers and are concerned of their stability during periods of high use. Which of the following should the company use to maximize the uptime and availability of this service?",
        "options": ["Cold site", "UPS", "Redundant routers", "Load balancer"],
        "answer": "Load balancer",
        "domain": "Security Architecture",
        "explanation": "A load balancer distributes network traffic across multiple servers to ensure no single server becomes overwhelmed, thereby improving availability and responsiveness."
    },
    {
        "question": "A system administrator would like to segment the network to give the marketing, accounting, and manufacturing departments their own private network. Which of the following should be configured on this network?",
        "options": ["VPN", "RBAC", "VLAN", "SDN"],
        "answer": "VLAN",
        "domain": "Security Architecture",
        "explanation": "A Virtual LAN (VLAN) allows a network administrator to create logical subgroupings of devices on the same physical network, effectively segmenting them from each other for security and management purposes."
    },
    {
        "question": "Which of the following is used to describe how cautious an organization might be to taking a specific risk?",
        "options": ["Risk appetite", "Risk register", "Risk transfer", "Risk reporting"],
        "answer": "Risk appetite",
        "domain": "Security Program Management and Oversight",
        "explanation": "Risk appetite is the level of risk an organization is willing to accept in pursuit of its objectives, before action is deemed necessary to reduce the risk."
    },
    {
        "question": "A security administrator has found a keylogger installed in an update of the company's accounting software. Which of the following would prevent the transmission of the collected logs?",
        "options": ["Prevent the installation of all software", "Block all unknown outbound network traffic at the Internet firewall", "Install host-based anti-virus software", "Scan all incoming email attachments at the email gateway"],
        "answer": "Block all unknown outbound network traffic at the Internet firewall",
        "domain": "Security Operations",
        "explanation": "Keyloggers need to send the data they collect back to the attacker. Blocking unknown outbound traffic at the firewall (an egress filtering policy) is an effective way to prevent this data exfiltration."
    },
    {
        "question": "An attacker has gained access to an application through the use of packet captures. Which of the following would be MOST likely used by the attacker?",
        "options": ["Overflow", "Forgery", "Replay", "Injection"],
        "answer": "Replay",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "A replay attack involves capturing network packets and then re-transmitting them to impersonate the original user or repeat a transaction. This is a common attack when authentication tokens are captured."
    },
    {
        "question": "A company must comply with legal requirements for storing customer data in the same country as the customer's mailing address. Which of the following would describe this requirement?",
        "options": ["Geographic dispersion", "Least privilege", "Data sovereignty", "Exfiltration"],
        "answer": "Data sovereignty",
        "domain": "Security Program Management and Oversight",
        "explanation": "Data sovereignty is the concept that data is subject to the laws and legal jurisdiction of the country in which it is located."
    },
    {
        "question": "What is the key difference between a worm and a virus?",
        "options": ["What operating system they run on", "How they spread", "What their potential impact is", "The number of infections"],
        "answer": "How they spread",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "The primary difference is that a virus requires user interaction to spread (e.g., opening an infected file), while a worm can self-replicate and spread across networks without any user action."
    },
    {
        "question": "An organization has identified a security breach and has removed the affected servers from the network. Which of the following is the NEXT step in the incident response process?",
        "options": ["Eradication", "Preparation", "Recovery", "Detection"],
        "answer": "Eradication",
        "domain": "Security Operations",
        "explanation": "After containing an incident (e.g., by taking servers offline), the next phase is eradication, which involves removing the malware or threat from the affected systems completely."
    },
    {
        "question": "A security administrator has configured a virtual machine in a screened subnet with a guest login account and no password. Which of the following would be the MOST likely reason for this configuration?",
        "options": ["The server is a honeypot for attracting potential attackers", "The server is a cloud storage service for remote users", "The server will be used as a VPN concentrator", "The server is a development sandbox for third-party programming projects"],
        "answer": "The server is a honeypot for attracting potential attackers",
        "domain": "Security Operations",
        "explanation": "A system that is intentionally left insecure and placed in a monitored environment (like a screened subnet or DMZ) is characteristic of a honeypot, designed to lure and analyze attackers."
    },
    {
        "question": "A security administrator needs to block users from visiting websites hosting malicious software. Which of the following would be the BEST way to control this access?",
        "options": ["Honeynet", "Data masking", "DNS filtering", "Data loss prevention"],
        "answer": "DNS filtering",
        "domain": "Security Architecture",
        "explanation": "DNS filtering services prevent users from connecting to known malicious websites by blocking the DNS resolution for those domains at the network level."
    },
    {
        "question": "A user connects to a third-party website and receives this message: 'Your connection is not private. NET::ERR_CERT_INVALID'. Which of the following attacks would be the MOST likely reason for this message?",
        "options": ["Brute force", "DoS", "On-path", "Deauthentication"],
        "answer": "On-path",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "An on-path (formerly man-in-the-middle) attack can intercept traffic and present a fraudulent SSL/TLS certificate, causing the browser to display a certificate invalid error."
    },
    {
        "question": "What kind of security control is associated with a login banner?",
        "options": ["Preventive", "Deterrent", "Corrective", "Detective"],
        "answer": "Deterrent",
        "domain": "General Security Concepts",
        "explanation": "A login banner that warns against unauthorized access acts as a deterrent control. It discourages potential attackers by reminding them of the legal consequences."
    },
    {
        "question": "Which of the following describes two-factor authentication?",
        "options": ["A printer uses a password and a PIN", "The door to a building requires a fingerprint scan", "An application requires a pseudo-random code", "A Windows Domain requires a password and smart card"],
        "answer": "A Windows Domain requires a password and smart card",
        "domain": "General Security Concepts",
        "explanation": "Two-factor authentication requires two different types of authentication factors. A password is 'something you know' and a smart card is 'something you have', satisfying the requirement."
    },
    {
        "question": "A Linux administrator is downloading an updated version of her Linux distribution. The download site shows a link to the ISO and a SHA256 hash value. Which of these would describe the use of this hash value?",
        "options": ["Verifies that the file was not corrupted during the file transfer", "Provides a key for decrypting the ISO after download", "Authenticates the site as an official ISO distribution site", "Confirms that the file does not contain any malware"],
        "answer": "Verifies that the file was not corrupted during the file transfer",
        "domain": "General Security Concepts",
        "explanation": "A hash value provides integrity. By calculating the hash of the downloaded file and comparing it to the one provided on the website, the administrator can verify that the file has not been altered or corrupted."
    },
    {
        "question": "Which of the following would be the main reasons why a system administrator would use a TPM when configuring full disk encryption? (Select TWO)",
        "options": ["Allows the encryption of multiple volumes", "Uses burned-in cryptographic keys", "Stores certificates in a hardware security module", "Includes built-in protections against brute-force attacks"],
        "answer": ["Uses burned-in cryptographic keys", "Includes built-in protections against brute-force attacks"],
        "domain": "Security Architecture",
        "explanation": "A Trusted Platform Module (TPM) is a hardware-based security solution. It securely stores cryptographic keys (burned into the hardware) and can protect against brute-force attacks on disk encryption keys."
    },
    {
        "question": "An attacker is using a tool to intercept and modify traffic between a user and a web server. This is an example of what kind of attack?",
        "options": ["Phishing", "Man-in-the-Middle (MITM)", "Denial of Service (DoS)", "SQL Injection"],
        "answer": "Man-in-the-Middle (MITM)",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "A Man-in-the-Middle (MITM) or On-Path attack is where the attacker secretly relays and possibly alters the communications between two parties who believe they are directly communicating with each other."
    },
    {
        "question": "What is the primary purpose of salting passwords before hashing them?",
        "options": ["To make the hash shorter", "To prevent rainbow table attacks", "To make passwords easier to remember", "To encrypt the password hash"],
        "answer": "To prevent rainbow table attacks",
        "domain": "General Security Concepts",
        "explanation": "A salt is a random value added to a password before hashing. This ensures that even identical passwords have different hashes, rendering pre-computed hash lists (rainbow tables) ineffective."
    },
    {
        "question": "Which of the following is a symmetric encryption algorithm?",
        "options": ["RSA", "ECC", "AES", "Diffie-Hellman"],
        "answer": "AES",
        "domain": "General Security Concepts",
        "explanation": "The Advanced Encryption Standard (AES) is a widely used symmetric encryption algorithm, meaning it uses the same key for both encryption and decryption. RSA, ECC, and Diffie-Hellman are all asymmetric."
    },
    {
        "question": "A company policy states that all employees must change their passwords every 90 days. This is an example of what kind of control?",
        "options": ["Technical", "Physical", "Administrative", "Corrective"],
        "answer": "Administrative",
        "domain": "Security Program Management and Oversight",
        "explanation": "Administrative controls are organizational policies, procedures, and standards that dictate how security is managed. A password expiration policy is a classic example."
    },
    {
        "question": "Which type of firewall filters traffic based on session information and connection state?",
        "options": ["Packet-filtering", "Stateful inspection", "Application-layer", "Proxy"],
        "answer": "Stateful inspection",
        "domain": "Security Architecture",
        "explanation": "A stateful inspection firewall monitors the state of active connections and uses this information to determine which network packets to allow through the firewall."
    },
    {
        "question": "Which security principle suggests that a system should be secure by default?",
        "options": ["Least privilege", "Fail-safe defaults", "Defense in depth", "Open design"],
        "answer": "Fail-safe defaults",
        "domain": "Security Architecture",
        "explanation": "Fail-safe defaults means that unless a subject is explicitly granted access to an object, access should be denied. It ensures that the default configuration is a secure one."
    },
    {
        "question": "An unauthorized access point is configured to mimic a legitimate corporate network to trick users into connecting. What is this access point called?",
        "options": ["Honeypot", "Rogue AP", "Evil Twin", "Ad hoc network"],
        "answer": "Evil Twin",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "An evil twin is a fraudulent Wi-Fi access point that appears to be legitimate but is set up to eavesdrop on wireless communications."
    },
    {
        "question": "What is the term for an attack that exploits a previously unknown vulnerability?",
        "options": ["Zero-day attack", "Replay attack", "Buffer overflow", "Brute-force attack"],
        "answer": "Zero-day attack",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "A zero-day attack occurs on the same day a vulnerability is discovered by the vendor, meaning no patch is available, leaving systems vulnerable."
    },
    {
        "question": "Which of the following provides integrity for a message?",
        "options": ["AES", "RSA", "SHA-256", "WPA3"],
        "answer": "SHA-256",
        "domain": "General Security Concepts",
        "explanation": "Hashing algorithms like SHA-256 produce a fixed-size hash value from input data. Any change to the data will result in a different hash, thus providing data integrity."
    },
    {
        "question": "A company wants to outsource its IT infrastructure, including servers, storage, and networking, to a cloud provider. Which service model should it choose?",
        "options": ["SaaS", "PaaS", "IaaS", "DaaS"],
        "answer": "IaaS",
        "domain": "Security Architecture",
        "explanation": "Infrastructure as a Service (IaaS) is a cloud computing model where a vendor provides users with access to computing resources such as servers, storage, and networking."
    },
    {
        "question": "Which of the following is used to manage and enforce policies on employees' smartphones and tablets?",
        "options": ["MDM (Mobile Device Management)", "SIEM (Security Information and Event Management)", "DLP (Data Loss Prevention)", "NAC (Network Access Control)"],
        "answer": "MDM (Mobile Device Management)",
        "domain": "Security Architecture",
        "explanation": "Mobile Device Management (MDM) software is used to monitor, manage, and secure employees' mobile devices that are used for both personal and business purposes."
    },
    {
        "question": "What is the name of an attack where the attacker sends a flood of ICMP echo request packets to a broadcast address?",
        "options": ["Ping of death", "Smurf attack", "SYN flood", "Teardrop attack"],
        "answer": "Smurf attack",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "A Smurf attack is a type of DDoS attack in which an attacker sends a large number of ICMP echo requests to a network broadcast address, all spoofed to appear as if they came from the victim's IP address."
    },
    {
        "question": "Which of the following is a physical security control?",
        "options": ["Password policy", "Mantrap", "Firewall", "Antivirus"],
        "answer": "Mantrap",
        "domain": "General Security Concepts",
        "explanation": "A mantrap is a physical security device with two sets of interlocking doors, where the first set must close before the second set opens, controlling access to a secure area."
    },
    {
        "question": "A developer is writing code and wants to prevent users from entering malicious scripts into input fields. What vulnerability is the developer trying to mitigate?",
        "options": ["SQL Injection", "Cross-Site Scripting (XSS)", "Cross-Site Request Forgery (CSRF)", "Buffer Overflow"],
        "answer": "Cross-Site Scripting (XSS)",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "Preventing malicious scripts from being entered into input fields is a primary defense against Cross-Site Scripting (XSS), where attackers inject client-side scripts into web pages viewed by other users."
    },
    {
        "question": "Which type of backup strategy involves backing up all data that has changed since the last backup of any kind?",
        "options": ["Full", "Differential", "Incremental", "Snapshot"],
        "answer": "Incremental",
        "domain": "Security Operations",
        "explanation": "An incremental backup saves only the data that has changed since the last backup, whether it was a full or another incremental backup. This results in smaller, faster backups but a more complex restore process."
    },
    {
        "question": "Which of the following describes the 'A' in the CIA triad?",
        "options": ["Authentication", "Authorization", "Availability", "Accounting"],
        "answer": "Availability",
        "domain": "General Security Concepts",
        "explanation": "The CIA triad stands for Confidentiality, Integrity, and Availability. Availability ensures that data and services are accessible to authorized users when needed."
    },
    {
        "question": "A security team is performing a test where they have no prior knowledge of the target system. What type of test is this?",
        "options": ["White-box", "Gray-box", "Black-box", "Red team"],
        "answer": "Black-box",
        "domain": "Security Operations",
        "explanation": "In a black-box penetration test, the tester has no prior knowledge of the target system's internal workings. They must approach the test from an external attacker's perspective."
    },
    {
        "question": "What is the process of verifying a user's identity?",
        "options": ["Authorization", "Authentication", "Accounting", "Auditing"],
        "answer": "Authentication",
        "domain": "General Security Concepts",
        "explanation": "Authentication is the process of confirming a user's identity to ensure they are who they claim to be. Authorization, which happens after authentication, is the process of granting access to resources."
    },
    {
        "question": "An attacker spoofs the MAC address of a trusted device to gain access to a network. This is an example of:",
        "options": ["ARP poisoning", "MAC flooding", "IP spoofing", "DNS poisoning"],
        "answer": "ARP poisoning",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "ARP poisoning (or MAC spoofing) is an attack where an attacker sends falsified ARP messages over a local area network. This links an attacker's MAC address with the IP address of a legitimate computer or server on the network."
    },
    {
        "question": "A company wants to ensure that a single employee cannot carry out a critical task alone. Which security principle should be implemented?",
        "options": ["Least privilege", "Separation of duties", "Job rotation", "Need-to-know"],
        "answer": "Separation of duties",
        "domain": "Security Program Management and Oversight",
        "explanation": "Separation of duties is a security principle that prevents any single individual from having too much control, thereby reducing the risk of fraud and error. It requires that critical tasks be divided among multiple people."
    },
    {
        "question": "Which of the following is a characteristic of an advanced persistent threat (APT)?",
        "options": ["Low skill level", "Short-term objectives", "High level of resources and patience", "Targets individuals, not organizations"],
        "answer": "High level of resources and patience",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "APTs are sophisticated, long-term attacks, often sponsored by nation-states. They are characterized by their stealth, persistence, and significant resources."
    },
    {
        "question": "Which biometric authentication method is considered the most unique and difficult to forge?",
        "options": ["Fingerprint scan", "Facial recognition", "Iris scan", "Voice recognition"],
        "answer": "Iris scan",
        "domain": "General Security Concepts",
        "explanation": "Iris scanning is considered one of the most accurate and reliable biometric authentication methods due to the unique and complex patterns of the human iris, which are stable throughout a person's life."
    },
    {
        "question": "What type of social engineering attack involves an attacker sending a fraudulent email that appears to be from a legitimate source?",
        "options": ["Vishing", "Smishing", "Phishing", "Tailgating"],
        "answer": "Phishing",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "Phishing is a social engineering attack that uses deceptive emails and websites to trick victims into revealing sensitive personal or financial information."
    },
    {
        "question": "In cryptography, what is a public key used for?",
        "options": ["To encrypt data that only the private key can decrypt", "To decrypt data that was encrypted with the same public key", "To create a digital signature", "To generate a symmetric key"],
        "answer": "To encrypt data that only the private key can decrypt",
        "domain": "General Security Concepts",
        "explanation": "In asymmetric cryptography, a public key is used to encrypt data, and only the corresponding private key can decrypt it. This ensures confidentiality."
    },
    {
        "question": "A company wants to monitor and filter web traffic for its employees. Which of the following would be the most suitable solution?",
        "options": ["VPN concentrator", "Web application firewall", "Proxy server", "IDS"],
        "answer": "Proxy server",
        "domain": "Security Architecture",
        "explanation": "A proxy server acts as an intermediary for requests from clients seeking resources from other servers. It can be used to filter content, log traffic, and improve performance through caching."
    },
    {
        "question": "What is the primary goal of a Business Continuity Plan (BCP)?",
        "options": ["To restore IT systems after a disaster", "To ensure critical business functions can continue during a disruption", "To investigate the cause of an incident", "To prosecute attackers"],
        "answer": "To ensure critical business functions can continue during a disruption",
        "domain": "Security Program Management and Oversight",
        "explanation": "A Business Continuity Plan (BCP) focuses on keeping essential business operations running during a disaster. A Disaster Recovery Plan (DRP), a component of BCP, focuses on restoring IT infrastructure."
    },
    {
        "question": "Which type of intrusion detection system (IDS) analyzes traffic for signatures of known attacks?",
        "options": ["Signature-based", "Anomaly-based", "Behavior-based", "Heuristic-based"],
        "answer": "Signature-based",
        "domain": "Security Operations",
        "explanation": "A signature-based IDS (also known as misuse-detection IDS) compares network traffic against a database of known attack patterns (signatures). It is effective against known threats but cannot detect new attacks."
    },
    {
        "question": "A user receives a text message with a malicious link. This is an example of what type of attack?",
        "options": ["Phishing", "Vishing", "Smishing", "Spear phishing"],
        "answer": "Smishing",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "Smishing is a form of phishing that uses mobile phone text messages (SMS) to trick victims into clicking malicious links or revealing sensitive information."
    },
    {
        "question": "Which of the following policies specifies how employees should handle sensitive company data?",
        "options": ["Acceptable Use Policy (AUP)", "Information Classification Policy", "Password Policy", "Incident Response Policy"],
        "answer": "Information Classification Policy",
        "domain": "Security Program Management and Oversight",
        "explanation": "An information classification policy provides a framework for categorizing data based on its sensitivity (e.g., Public, Internal, Confidential) and defines handling requirements for each level."
    },
    {
        "question": "Which deployment model requires a company to purchase and own the device, but allows the user to select the device they prefer?",
        "options": ["BYOD", "COPE", "CYOD", "VDI"],
        "answer": "CYOD",
        "domain": "Security Architecture",
        "explanation": "In a Choose Your Own Device (CYOD) model, the company owns and manages the device, but the employee can choose from a pre-approved list of devices, offering a balance between user preference and corporate control."
    },
    {
        "question": "A security operations center (SOC) has identified an ongoing denial-of-service attack against their primary web server. Which of the following should be the IMMEDIATE next step?",
        "options": ["Perform a full backup of the web server", "Contact law enforcement", "Isolate the web server from the network", "Analyze the server logs to identify the attack source"],
        "answer": "Isolate the web server from the network",
        "domain": "Security Operations",
        "explanation": "The immediate priority during an active attack is containment. Isolating the server prevents the attack from potentially spreading or causing further damage to other network resources."
    },
    {
        "question": "Which of the following is a detective security control?",
        "options": ["Firewall", "Encryption", "Security guard", "Log monitoring"],
        "answer": "Log monitoring",
        "domain": "Security Program Management and Oversight",
        "explanation": "Detective controls are used to identify and record security incidents that have already occurred. Log monitoring and analysis are key detective activities."
    },
    {
        "question": "Which of the following is an example of a watering hole attack?",
        "options": ["An attacker sends a phishing email to all employees of a company", "An attacker compromises a website frequently visited by a specific group of users", "An attacker sets up a fake wireless access point in a coffee shop", "An attacker calls an employee pretending to be from the IT department"],
        "answer": "An attacker compromises a website frequently visited by a specific group of users",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "In a watering hole attack, the attacker compromises a legitimate website that they know their target group frequents, and then infects visitors from that group."
    },
    {
        "question": "A company wants to ensure that data in transit is protected from eavesdropping. Which technology should be used?",
        "options": ["Hashing", "Digital signatures", "TLS", "Steganography"],
        "answer": "TLS",
        "domain": "Security Architecture",
        "explanation": "Transport Layer Security (TLS), and its predecessor SSL, are cryptographic protocols that provide secure communication over a computer network, encrypting data in transit."
    },
    {
        "question": "A system administrator has configured a new server and wants to ensure it has the correct security settings before deploying it to the production network. What should the administrator use?",
        "options": ["Vulnerability scanner", "Configuration baseline", "Honeypot", "Penetration test"],
        "answer": "Configuration baseline",
        "domain": "Security Operations",
        "explanation": "A configuration baseline is a standardized level of security settings that should be applied to all similar systems. The administrator should compare the new server against this baseline."
    },
    {
        "question": "Which of the following is a common vector for ransomware infections?",
        "options": ["Phishing emails", "DDoS attacks", "SQL injection", "Man-in-the-middle attacks"],
        "answer": "Phishing emails",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "Phishing emails with malicious attachments or links are one of the most common and effective delivery mechanisms for ransomware."
    },
    {
        "question": "Which authentication factor is a user's fingerprint an example of?",
        "options": ["Something you know", "Something you have", "Something you are", "Somewhere you are"],
        "answer": "Something you are",
        "domain": "General Security Concepts",
        "explanation": "Biometric data, such as a fingerprint, iris scan, or facial recognition, is classified as the 'something you are' authentication factor."
    },
    {
        "question": "What is the purpose of a Faraday cage?",
        "options": ["To block electromagnetic fields", "To prevent unauthorized physical access", "To provide redundant power", "To suppress fires"],
        "answer": "To block electromagnetic fields",
        "domain": "Security Architecture",
        "explanation": "A Faraday cage is an enclosure used to block electromagnetic fields (EMF). In security, it can be used to prevent wireless signals from entering or leaving a secure area, thus preventing eavesdropping and data leakage."
    },
    {
        "question": "A security analyst is reviewing logs and notices a large number of failed login attempts from a single IP address. This could be an indication of what type of attack?",
        "options": ["Phishing", "Brute-force", "Denial-of-service", "Cross-site scripting"],
        "answer": "Brute-force",
        "domain": "Security Operations",
        "explanation": "A brute-force attack involves systematically trying all possible combinations of passwords for a given username. A high volume of failed logins from one source is a strong indicator of this activity."
    },
    {
        "question": "Which of the following is the BEST way to protect against tailgating?",
        "options": ["Security guards and mantraps", "CCTV cameras", "Biometric locks", "Employee training"],
        "answer": "Security guards and mantraps",
        "domain": "General Security Concepts",
        "explanation": "Tailgating is a physical security breach. While training helps, the most effective preventative controls are physical ones like mantraps that only allow one person through at a time, or security guards who verify credentials."
    },
    {
        "question": "Which of the following cloud computing models provides a fully functional application to users over the internet?",
        "options": ["IaaS", "PaaS", "SaaS", "DaaS"],
        "answer": "SaaS",
        "domain": "Security Architecture",
        "explanation": "Software as a Service (SaaS) is a delivery model where software is licensed on a subscription basis and is centrally hosted. Users access it via a web browser, e.g., Google Docs or Office 365."
    },
    {
        "question": "An organization wants to implement a policy that requires employees to take a mandatory vacation of at least one week per year. What is the primary security benefit of this policy?",
        "options": ["It reduces employee burnout", "It helps to detect fraudulent activity", "It improves employee morale", "It is required for compliance with labor laws"],
        "answer": "It helps to detect fraudulent activity",
        "domain": "Security Program Management and Oversight",
        "explanation": "Mandatory vacation policies are a key administrative control for detecting fraud. If an employee is engaged in ongoing fraudulent activity, their absence makes it more likely that the activity will be discovered by the person covering their duties."
    },
    {
        "question": "Which of the following is a key component of a successful defense-in-depth strategy?",
        "options": ["Using a single, strong security control", "Implementing layered security controls", "Focusing only on perimeter security", "Relying on security through obscurity"],
        "answer": "Implementing layered security controls",
        "domain": "Security Architecture",
        "explanation": "Defense-in-depth is the strategy of having multiple, layered security controls. If one layer fails, another layer is already in place to protect the asset."
    },
    {
        "question": "A user is granted the minimum level of access required to perform their job duties. This is an example of which security principle?",
        "options": ["Need-to-know", "Least privilege", "Separation of duties", "Defense in depth"],
        "answer": "Least privilege",
        "domain": "General Security Concepts",
        "explanation": "The principle of least privilege dictates that a user should be given only the minimum permissions necessary to perform their job function, and no more."
    },
    {
        "question": "What type of malware is designed to steal sensitive information, such as credit card numbers and passwords, from a user's computer?",
        "options": ["Ransomware", "Spyware", "Adware", "Worm"],
        "answer": "Spyware",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "Spyware is a type of malware that secretly gathers information about a person or organization and sends it to another entity. This can include login credentials, financial information, and other sensitive data."
    },
    {
        "question": "Which of the following is a common technique used in social engineering?",
        "options": ["Exploiting a software vulnerability", "Using a brute-force attack to guess a password", "Creating a sense of urgency to trick a user into taking an action", "Intercepting network traffic"],
        "answer": "Creating a sense of urgency to trick a user into taking an action",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "Social engineers often manipulate human emotions. Creating a false sense of urgency (e.g., 'Your account will be suspended in one hour!') pressures the victim into making a hasty decision without thinking."
    },
    {
        "question": "A company has a policy that prohibits employees from using personal email accounts for business purposes. This is an example of what type of control?",
        "options": ["Technical", "Physical", "Administrative", "Corrective"],
        "answer": "Administrative",
        "domain": "Security Program Management and Oversight",
        "explanation": "This is an administrative (or managerial) control because it's a policy that dictates user behavior. It's not enforced by technology (technical) or a physical barrier (physical)."
    },
    {
        "question": "Which of the following is a primary benefit of using a SIEM system?",
        "options": ["To prevent intrusions from occurring", "To automatically patch software vulnerabilities", "To centralize and analyze security logs from multiple sources", "To provide a secure way for remote users to access the network"],
        "answer": "To centralize and analyze security logs from multiple sources",
        "domain": "Security Operations",
        "explanation": "A Security Information and Event Management (SIEM) system's main purpose is to aggregate log data from many sources, identify activity that deviates from the norm, and take appropriate action."
    },
    {
        "question": "What is the main purpose of a disaster recovery plan (DRP)?",
        "options": ["To ensure business continuity during a disruption", "To restore IT services and infrastructure after a disaster", "To investigate the cause of a security incident", "To comply with regulatory requirements"],
        "answer": "To restore IT services and infrastructure after a disaster",
        "domain": "Security Program Management and Oversight",
        "explanation": "While a DRP is part of overall business continuity, its specific focus is on the technical aspect of getting IT systems and services back online after a major disruption."
    },
    {
        "question": "A network administrator wants to allow HTTP traffic but block all other traffic. Which of the following firewall rules should be implemented?",
        "options": ["Allow TCP port 80, deny all others", "Deny TCP port 80, allow all others", "Allow UDP port 53, deny all others", "Deny TCP port 22, allow all others"],
        "answer": "Allow TCP port 80, deny all others",
        "domain": "Security Architecture",
        "explanation": "Firewall rules are often based on an implicit deny policy. To allow only HTTP (which uses TCP port 80), you would create a specific rule to allow that traffic and let the implicit deny rule block everything else."
    },
    {
        "question": "An organization is using a key stretching algorithm to make their password hashes more resistant to brute-force attacks. Which of the following would be an example of this type of algorithm?",
        "options": ["SHA-256", "MD5", "PBKDF2", "AES"],
        "answer": "PBKDF2",
        "domain": "General Security Concepts",
        "explanation": "PBKDF2 (Password-Based Key Derivation Function 2) is a key stretching technique designed to be computationally intensive, which slows down brute-force and dictionary attacks on password hashes."
    },
    {
        "question": "Which of the following is a primary concern when using a public Wi-Fi hotspot?",
        "options": ["Low bandwidth", "Man-in-the-middle attacks", "IP address exhaustion", "Power outages"],
        "answer": "Man-in-the-middle attacks",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "Public Wi-Fi networks are often unencrypted, making it easy for attackers on the same network to intercept, eavesdrop on, or modify your traffic in a Man-in-the-Middle (On-Path) attack."
    },
    {
        "question": "A company wants to implement a system that will automatically block network traffic from known malicious IP addresses. Which of the following would be the most effective solution?",
        "options": ["Honeypot", "Intrusion Prevention System (IPS)", "Vulnerability scanner", "Log analysis server"],
        "answer": "Intrusion Prevention System (IPS)",
        "domain": "Security Operations",
        "explanation": "An Intrusion Prevention System (IPS) is a network security tool that monitors network traffic for malicious activity and can take automated action to block it, unlike an IDS which only detects and alerts."
    },
    {
        "question": "Which of the following is the most effective way to prevent SQL injection attacks?",
        "options": ["Using strong passwords for the database", "Implementing a web application firewall", "Using parameterized queries or prepared statements", "Disabling JavaScript in the browser"],
        "answer": "Using parameterized queries or prepared statements",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "Using parameterized queries (or prepared statements) is a programming technique that separates the SQL command structure from the user-provided data, preventing the data from being interpreted as executable code."
    },
    {
        "question": "A company has a secure area that requires employees to swipe a badge to enter. An unauthorized person follows an employee into the secure area without swiping a badge. This is an example of:",
        "options": ["Shoulder surfing", "Tailgating", "Dumpster diving", "Vishing"],
        "answer": "Tailgating",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "Tailgating (or piggybacking) is a physical security breach where an unauthorized person follows an authorized individual into a restricted area."
    },
    {
        "question": "Which of the following is an example of a preventive security control?",
        "options": ["CCTV cameras", "Log analysis", "Incident response plan", "Firewall"],
        "answer": "Firewall",
        "domain": "Security Architecture",
        "explanation": "Preventive controls are designed to stop a security incident from happening in the first place. A firewall is a classic example, as it proactively blocks unauthorized network traffic."
    },
    {
        "question": "A user's web browser is redirected to a malicious website without their knowledge. This is an example of what type of attack?",
        "options": ["Pharming", "Phishing", "Clickjacking", "Session hijacking"],
        "answer": "Pharming",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "Pharming is an attack that redirects a website's traffic to another, bogus site, typically by compromising DNS servers or modifying the host file on a victim's computer."
    },
    {
        "question": "What is the purpose of a certificate revocation list (CRL)?",
        "options": ["To list all valid digital certificates", "To list all expired digital certificates", "To list all revoked digital certificates", "To list all self-signed digital certificates"],
        "answer": "To list all revoked digital certificates",
        "domain": "Security Architecture",
        "explanation": "A Certificate Revocation List (CRL) is a list of digital certificates that have been revoked by the issuing Certificate Authority (CA) before their scheduled expiration date and should no longer be trusted."
    },
    {
        "question": "Which of the following is a hashing algorithm?",
        "options": ["AES", "RSA", "SHA-512", "ECC"],
        "answer": "SHA-512",
        "domain": "General Security Concepts",
        "explanation": "SHA-512 (Secure Hash Algorithm 512-bit) is a cryptographic hash function that produces a 512-bit hash value. AES is for encryption, while RSA and ECC are asymmetric cryptographic algorithms."
    },
    {
        "question": "A company wants to ensure that employees do not share sensitive information outside of the organization via email. Which of the following technologies would be most effective in preventing this?",
        "options": ["Spam filter", "Data Loss Prevention (DLP)", "Web application firewall", "Network intrusion detection system"],
        "answer": "Data Loss Prevention (DLP)",
        "domain": "Security Operations",
        "explanation": "Data Loss Prevention (DLP) systems are designed to detect and prevent data breaches or data exfiltration transmissions. They monitor, detect, and block sensitive data while in-use, in-motion, and at-rest."
    },
    {
        "question": "Which of the following is a primary goal of a red team exercise?",
        "options": ["To test the effectiveness of an organization's security defenses", "To train employees on how to respond to security incidents", "To comply with industry regulations", "To identify and patch software vulnerabilities"],
        "answer": "To test the effectiveness of an organization's security defenses",
        "domain": "Security Operations",
        "explanation": "A red team exercise is a full-scope, multi-layered attack simulation designed to measure how well a company's people, networks, applications and physical security controls can withstand an attack from a real-life adversary."
    },
    {
        "question": "Which of the following is a common symptom of a system that has been infected with adware?",
        "options": ["The system runs slower than usual", "Files on the system are encrypted", "The user is unable to access the internet", "The system displays unwanted pop-up advertisements"],
        "answer": "The system displays unwanted pop-up advertisements",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "Adware is software that generates revenue for its developer by automatically generating online advertisements in the user interface of the software or on a screen presented to the user during the installation process."
    },
    {
        "question": "A company wants to provide remote access to its employees. Which of the following technologies would provide the most secure connection?",
        "options": ["Telnet", "FTP", "VPN", "RDP"],
        "answer": "VPN",
        "domain": "Security Architecture",
        "explanation": "A Virtual Private Network (VPN) creates a secure, encrypted tunnel over a public network (like the internet), ensuring that data transmitted between the remote user and the corporate network is confidential and has integrity."
    },
    {
        "question": "Which of the following is an example of a compensating control?",
        "options": ["Implementing a firewall to protect the network perimeter", "Requiring employees to use strong passwords", "Placing a security guard at the entrance to a building", "Reviewing audit logs to detect unauthorized activity"],
        "answer": "Reviewing audit logs to detect unauthorized activity",
        "domain": "Security Program Management and Oversight",
        "explanation": "A compensating control is an alternative measure used when a primary control is not feasible. If a system cannot enforce a certain policy (a primary control), regularly reviewing audit logs for violations acts as a compensating control."
    },
    {
        "question": "An attacker is attempting to gain unauthorized access to a system by trying all possible password combinations. This is an example of what type of attack?",
        "options": ["Dictionary attack", "Brute-force attack", "Rainbow table attack", "Password spraying attack"],
        "answer": "Brute-force attack",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "A brute-force attack consists of an attacker submitting many passwords or passphrases with the hope of eventually guessing a combination correctly. The attacker systematically checks all possible passwords and passphrases until the correct one is found."
    },
    {
        "question": "A company wants to test its incident response plan to ensure that it is effective. Which of the following would be the most appropriate method?",
        "options": ["Conducting a tabletop exercise", "Performing a vulnerability scan", "Implementing a new security control", "Hiring a third-party penetration testing firm"],
        "answer": "Conducting a tabletop exercise",
        "domain": "Security Operations",
        "explanation": "A tabletop exercise is a discussion-based session where team members meet in an informal setting to discuss their roles during an emergency and their responses to a particular emergency situation. It's a perfect way to test an incident response plan without a real incident."
    },
    {
        "question": "Which of the following is the BEST way to mitigate the risk of a single point of failure in a network?",
        "options": ["Implementing a firewall", "Using strong encryption", "Implementing redundancy", "Conducting regular backups"],
        "answer": "Implementing redundancy",
        "domain": "Security Architecture",
        "explanation": "Redundancy involves duplicating critical components or functions of a system with the intention of increasing reliability of the system, usually in the form of a backup or fail-safe, or to improve actual system performance."
    },
    {
        "question": "A company is concerned about the risk of employees writing down their passwords on sticky notes. Which of the following policies would be most effective in mitigating this risk?",
        "options": ["Password complexity policy", "Clean desk policy", "Acceptable use policy", "Password rotation policy"],
        "answer": "Clean desk policy",
        "domain": "Security Program Management and Oversight",
        "explanation": "A clean desk policy requires employees to clear their desks of all sensitive information (including password sticky notes) when they leave their workspace, which directly mitigates this risk."
    },
    {
        "question": "Which of the following is an example of a threat intelligence source?",
        "options": ["A company's internal security logs", "A vendor's security advisory", "An industry information sharing and analysis center (ISAC)", "A news article about a recent data breach"],
        "answer": "An industry information sharing and analysis center (ISAC)",
        "domain": "Security Program Management and Oversight",
        "explanation": "ISACs are sector-specific organizations that gather, analyze, and disseminate cyber threat information. They are a formal source of curated threat intelligence."
    },
    {
        "question": "What is the primary purpose of a web application firewall (WAF)?",
        "options": ["To protect against network-layer attacks", "To protect against application-layer attacks such as SQL injection and XSS", "To filter spam and phishing emails", "To provide secure remote access to the network"],
        "answer": "To protect against application-layer attacks such as SQL injection and XSS",
        "domain": "Security Architecture",
        "explanation": "A WAF is specifically designed to protect web applications from common application-layer attacks by inspecting HTTP traffic between a web application and the Internet."
    },
    {
        "question": "Which of the following is a benefit of using a trusted platform module (TPM)?",
        "options": ["It provides a secure way to store cryptographic keys", "It allows for faster network speeds", "It protects against power outages", "It can be used to run virtual machines"],
        "answer": "It provides a secure way to store cryptographic keys",
        "domain": "Security Architecture",
        "explanation": "A TPM is a secure crypto-processor that is designed to carry out cryptographic operations. The module includes multiple physical security mechanisms to make it tamper-resistant, and software is not able to tamper with the security functions of the TPM."
    },
    {
        "question": "A security analyst is investigating a security incident and needs to preserve evidence from a compromised system. Which of the following should be the first step?",
        "options": ["Create a forensic image of the system's hard drive", "Shut down the system to prevent further damage", "Disconnect the system from the network", "Install antivirus software on the system"],
        "answer": "Create a forensic image of the system's hard drive",
        "domain": "Security Operations",
        "explanation": "The first step in digital forensics is to preserve the evidence in its original state. Creating a bit-for-bit forensic image of the storage media ensures that the original evidence remains untouched while the investigation proceeds on the copy."
    },
    {
        "question": "Which of the following is a common security concern associated with the Internet of Things (IoT)?",
        "options": ["Lack of strong security controls and regular patching", "High bandwidth consumption", "Limited processing power", "Physical theft of devices"],
        "answer": "Lack of strong security controls and regular patching",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "Many IoT devices are shipped with default credentials, lack robust security features, and are difficult or impossible to patch, making them easy targets for attackers."
    },
    {
        "question": "A company wants to ensure that only authorized users are able to access its wireless network. Which of the following would be the most secure method?",
        "options": ["Hiding the SSID of the wireless network", "Using MAC address filtering", "Implementing WPA3-Enterprise with 802.1X authentication", "Using a pre-shared key (PSK)"],
        "answer": "Implementing WPA3-Enterprise with 802.1X authentication",
        "domain": "Security Architecture",
        "explanation": "WPA3-Enterprise combined with 802.1X provides the most robust security for wireless networks by requiring each user to authenticate individually against a central authentication server (like RADIUS), rather than using a shared password."
    },
    {
        "question": "Which of the following is an example of a detective control?",
        "options": ["A security policy that requires all employees to attend annual security awareness training", "A firewall that blocks traffic from known malicious IP addresses", "A security guard who patrols the perimeter of a building", "A log monitoring system that generates alerts for suspicious activity"],
        "answer": "A log monitoring system that generates alerts for suspicious activity",
        "domain": "Security Operations",
        "explanation": "Detective controls are designed to find and report on unwanted events that have already occurred. A log monitoring system that alerts on suspicious activity is a prime example."
    },
    {
        "question": "What is the purpose of a sandboxed environment?",
        "options": ["To run and analyze suspicious code in an isolated environment", "To store and manage cryptographic keys", "To provide a secure way for remote users to access the network", "To test the performance of a new application"],
        "answer": "To run and analyze suspicious code in an isolated environment",
        "domain": "Security Operations",
        "explanation": "A sandbox is an isolated testing environment that enables users to run programs or open files without affecting the application or system on which they run. It's often used to safely analyze malware."
    },
    {
        "question": "A company is required to comply with the Payment Card Industry Data Security Standard (PCI DSS). Which of the following is a key requirement of this standard?",
        "options": ["Encrypting all sensitive data at rest and in transit", "Conducting annual penetration tests", "Implementing a security awareness training program for all employees", "All of the above"],
        "answer": "All of the above",
        "domain": "Security Program Management and Oversight",
        "explanation": "PCI DSS is a comprehensive standard that includes requirements for building and maintaining a secure network, protecting cardholder data (including encryption), implementing strong access control measures, and maintaining an information security policy, which includes training."
    },
    {
        "question": "Which of the following is a common indicator of a compromised system?",
        "options": ["Unusual outbound network traffic", "Increased CPU or memory usage", "Unexpected changes to system files or configurations", "All of the above"],
        "answer": "All of the above",
        "domain": "Security Operations",
        "explanation": "All of these can be indicators of compromise (IoCs). Malware can generate unusual network traffic, consume system resources, and modify files or settings to maintain persistence."
    },
    {
        "question": "A company wants to implement a system that will allow it to remotely wipe data from lost or stolen mobile devices. Which of the following technologies would be most appropriate?",
        "options": ["Full disk encryption", "Mobile device management (MDM)", "Virtual private network (VPN)", "Data loss prevention (DLP)"],
        "answer": "Mobile device management (MDM)",
        "domain": "Security Architecture",
        "explanation": "MDM solutions provide a wide range of capabilities for managing mobile devices, including the ability to enforce security policies, locate devices, and remotely wipe data if a device is lost or stolen."
    },
    {
        "question": "Which of the following is a primary goal of a continuity of operations plan (COOP)?",
        "options": ["To ensure that an organization can continue to perform its essential functions during a disruption", "To restore IT services and infrastructure after a disaster", "To investigate the cause of a security incident", "To comply with regulatory requirements"],
        "answer": "To ensure that an organization can continue to perform its essential functions during a disruption",
        "domain": "Security Program Management and Oversight",
        "explanation": "A COOP is a plan focused on maintaining the performance of essential functions (not all functions) during a wide range of potential emergencies. It's a key part of overall business continuity."
    },
    {
        "question": "An attacker has gained access to a user's session cookie and is using it to impersonate the user. This is an example of what type of attack?",
        "options": ["Session hijacking", "Cross-site scripting (XSS)", "Cross-site request forgery (CSRF)", "Clickjacking"],
        "answer": "Session hijacking",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "Session hijacking is the exploitation of a valid computer session—sometimes also called a session key—to gain unauthorized access to information or services in a computer system."
    },
    {
        "question": "A company wants to implement a system that will provide a single point of authentication for multiple applications. Which of the following would be the most appropriate solution?",
        "options": ["Kerberos", "RADIUS", "TACACS+", "SAML"],
        "answer": "SAML",
        "domain": "Security Architecture",
        "explanation": "Security Assertion Markup Language (SAML) is an open standard for exchanging authentication and authorization data between parties, in particular, between an identity provider and a service provider. It is commonly used for web-based single sign-on (SSO)."
    },
    {
        "question": "Which of the following is a common method for exfiltrating data from a compromised network?",
        "options": ["Using DNS tunneling", "Encrypting the data and sending it via email", "Uploading the data to a cloud storage service", "All of the above"],
        "answer": "All of the above",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "Attackers use many methods to exfiltrate data. DNS tunneling hides data in DNS queries, while sending encrypted data via email or uploading to cloud services are also common, often less conspicuous, methods."
    },
    {
        "question": "A company wants to ensure that its employees are aware of the latest security threats and best practices. Which of the following would be the most effective method?",
        "options": ["Sending out a monthly security newsletter", "Requiring all employees to attend an annual security awareness training session", "Conducting regular phishing simulations", "All of the above"],
        "answer": "All of the above",
        "domain": "Security Program Management and Oversight",
        "explanation": "A comprehensive security awareness program uses multiple methods to reinforce learning. A combination of regular training, practical simulations, and continuous communication is most effective."
    },
    {
        "question": "Which of the following is a key consideration when developing a secure software development lifecycle (SDLC)?",
        "options": ["Incorporating security into every phase of the development process", "Performing a security review of the code before it is deployed", "Conducting a penetration test of the application after it is deployed", "All of the above"],
        "answer": "All of the above",
        "domain": "Security Program Management and Oversight",
        "explanation": "A secure SDLC involves integrating security activities throughout the entire development process, from requirements gathering and design (threat modeling) to coding (static analysis) and testing (pen testing), rather than treating security as an afterthought."
    },
    {
        "question": "A company is concerned about the risk of an attacker gaining access to its internal network by compromising a user's home computer. Which of the following would be the most effective way to mitigate this risk?",
        "options": ["Requiring all employees to use a VPN when connecting to the corporate network from home", "Providing all employees with a company-owned laptop for work purposes", "Implementing a security awareness training program that covers the risks of using home computers for work", "All of the above"],
        "answer": "All of the above",
        "domain": "Security Architecture",
        "explanation": "A layered, defense-in-depth approach is most effective. A VPN secures the connection, a company-owned device ensures a hardened endpoint, and training addresses the human element."
    },
    {
        "question": "Which of the following is a common security risk associated with cloud computing?",
        "options": ["Misconfigured security settings", "Lack of visibility into the cloud provider's security controls", "Shared tenancy", "All of the above"],
        "answer": "All of the above",
        "domain": "Security Architecture",
        "explanation": "All of these are significant risks. Misconfigurations by the customer are a leading cause of cloud breaches, lack of visibility can hinder incident response, and shared tenancy creates a risk of side-channel attacks."
    },
    {
        "question": "A company wants to implement a system that will allow it to track and manage changes to its IT infrastructure. Which of the following would be the most appropriate solution?",
        "options": ["A configuration management database (CMDB)", "A change management system", "A version control system", "All of the above"],
        "answer": "All of the above",
        "domain": "Security Operations",
        "explanation": "These systems work together. A CMDB tracks assets and their configurations, a change management system provides the process for making changes, and a version control system can track the specific changes to configuration files or code."
    },
    {
        "question": "A user has received an email that appears to be from their bank, asking them to click on a link to verify their account information. This is an example of what type of attack?",
        "options": ["Spear phishing", "Whaling", "Phishing", "Vishing"],
        "answer": "Phishing",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "This is a classic example of a phishing attack, which uses fraudulent emails to trick individuals into revealing personal information. Spear phishing is a more targeted version, and whaling targets high-profile individuals."
    },
    {
        "question": "Which of the following is a key benefit of using a bug bounty program?",
        "options": ["It allows a company to leverage the expertise of a large number of security researchers", "It can be a cost-effective way to identify and fix vulnerabilities", "It can help to improve a company's security posture and reputation", "All of the above"],
        "answer": "All of the above",
        "domain": "Security Operations",
        "explanation": "Bug bounty programs crowdsource vulnerability discovery from a global pool of researchers, providing a continuous and cost-effective way to improve security and demonstrate a commitment to it."
    },
    {
        "question": "An attacker has sent more information than expected in a single API call, and this has allowed the execution of arbitrary code. Which of the following would BEST describe this attack?",
        "options": ["Buffer overflow", "Replay attack", "Cross-site scripting", "DDoS"],
        "answer": "Buffer overflow",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "The results of a buffer overflow can cause random results, but sometimes the actions can be repeatable and controlled. In the best possible case for the hacker, a buffer overflow can be manipulated to execute code on the remote device."
    },
    {
        "question": "Which of the following is a key component of a security information and event management (SIEM) system?",
        "options": ["A log management system", "A vulnerability scanner", "A firewall", "A patch management system"],
        "answer": "A log management system",
        "domain": "Security Operations",
        "explanation": "A SIEM system collects, analyzes, and correlates security events from various sources to detect and respond to threats."
    },
    {
        "question": "A finance company is legally required to maintain seven years of tax records for all of their customers. Which of the following would be the BEST way to implement this requirement?",
        "options": [
            "Automate a script to remove all tax information more than seven years old",
            "Print and store all tax records in a seven-year cycle",
            "Allow users to download tax records from their account login",
            "Create a separate daily backup archive for all applicable tax records"
        ],
        "answer": "Create a separate daily backup archive for all applicable tax records",
        "domain": "Security Operations",
        "explanation": "An important consideration for a data retention mandate is to always have access to the information over the proposed time frame. In this example, a daily backup would ensure tax information is constantly archived over a seven year period and could always be retrieved if needed. If data was inadvertently deleted from the primary storage, the backup would still maintain a copy."
    },
    {
        "question": "A system administrator is designing a data center for an insurance company's new public cloud and would like to automatically rotate encryption keys on a regular basis. Which of the following would provide this functionality?",
        "options": [
            "TPM",
            "Key management system",
            "Secure enclave",
            "XDR"
        ],
        "answer": "Key management system",
        "domain": "Security Architecture",
        "explanation": "A key management system is used to manage large security key implementations from a central console. This includes creating keys, associating keys with individuals, rotating keys on regular intervals, and logging all key use."
    },
    {
        "question": "A security administrator has identified an internally developed application which allows modification of SQL queries through the web-based frontend. Which of the following changes would resolve this vulnerability?",
        "options": [
            "Store all credentials as salted hashes",
            "Verify the application's digital signature",
            "Validate all application input",
            "Obfuscate the application's source code"
        ],
        "answer": "Validate all application input",
        "domain": "Security Operations",
        "explanation": "Input validation would examine the input from the client and make sure that the input is expected and not malicious. In this example, validating the input would prevent any SQL (Structured Query Language) injection through the web front-end."
    },
    {
        "question": "A system administrator is implementing a fingerprint scanner to provide access to the data center. Which of the following authentication technologies would be associated with this access?",
        "options": [
            "Digital signature",
            "Hard authentication token",
            "Security key",
            "Something you are"
        ],
        "answer": "Something you are",
        "domain": "Security Operations",
        "explanation": "An authentication factor of 'something you are' often refers to a physical characteristic. This factor commonly uses fingerprints, facial recognition, or some other biometric characteristic to match a user to an authentication attempt."
    },
    {
        "question": "The IT department of a transportation company maintains an on-site inventory of chassis-based network switch interface cards. If a failure occurs, the on-site technician can replace the interface card and have the system running again in sixty minutes. Which of the following BEST describes this recovery metric?",
        "options": [
            "MTBF",
            "MTTR",
            "RPO",
            "RTO"
        ],
        "answer": "MTTR",
        "domain": "Governance, Risk, and Compliance",
        "explanation": "MTTR (Mean Time To Restore) is the amount of time required to get back up and running. This is sometimes called Mean Time To Repair."
    },
    {
        "question": "A company maintains a server farm in a large data center. These servers are used internally and are not accessible from outside of the data center. The security team has discovered a group of servers was breached before the latest security patches were applied. Breach attempts were not logged on any other servers. Which of these threat actors would be MOST likely involved in this breach?",
        "options": [
            "Organized crime",
            "Insider",
            "Nation state",
            "Unskilled attacker"
        ],
        "answer": "Insider",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "None of these servers are accessible from the outside, and the only servers with any logged connections were also susceptible to the latest vulnerabilities. To complete this attack, there would need a very specific knowledge of the vulnerable systems and a way to communicate with those servers."
    },
    {
        "question": "An organization has received a vulnerability scan report of their Internet-facing web servers. The report shows the servers have multiple Sun Java Runtime Environment (JRE) vulnerabilities, but the server administrator has verified that JRE is not installed. Which of the following would be the BEST way to handle this report?",
        "options": [
            "Install the latest version of JRE on the server",
            "Quarantine the server and scan for malware",
            "Harden the operating system of the web server",
            "Ignore the JRE vulnerability alert"
        ],
        "answer": "Ignore the JRE vulnerability alert",
        "domain": "Security Operations",
        "explanation": "It's relatively common for vulnerability scans to show vulnerabilities that don't actually exist, especially if the scans are not credentialed. An issue that is identified but does not actually exist is a false positive, and it can be dismissed once the alert has been properly researched."
    },
    {
        "question": "A user downloaded and installed a utility for compressing and decompressing files. Immediately after installing the utility, the user's overall workstation performance degraded and it now takes twice as much time to perform any tasks on the computer. Which of the following is the BEST description of this malware infection?",
        "options": [
            "Ransomware",
            "Bloatware",
            "Logic bomb",
            "Trojan"
        ],
        "answer": "Trojan",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "A Trojan horse is malicious software that pretends to be something benign. The user will install the software with the expectation that it will perform a particular function, but in reality it is installing malware on the computer."
    },
    {
        "question": "Which of the following is the process for replacing sensitive data with a non-sensitive and functional placeholder?",
        "options": [
            "Steganography",
            "Tokenization",
            "Retention",
            "Masking"
        ],
        "answer": "Tokenization",
        "domain": "Infrastructure Security",
        "explanation": "Tokenization replaces sensitive data with a token, and this token can be used as a functional placeholder for the original data. Tokenization is commonly used with credit card processing and mobile devices."
    },
    {
        "question": "A security administrator has installed a new firewall to protect a web server VLAN. The application owner requires all web server sessions communicate over an encrypted channel. Which rule should the security administrator add to the firewall rulebase?",
        "options": [
            "Source: ANY, Destination: ANY, Protocol: TCP, Port: 23, Deny",
            "Source: ANY, Destination: ANY, Protocol: TCP, Port: 22, Allow",
            "Source: ANY, Destination: ANY, Protocol: TCP, Port: 80, Allow",
            "Source: ANY, Destination: ANY, Protocol: TCP, Port: 443, Allow"
        ],
        "answer": "Source: ANY, Destination: ANY, Protocol: TCP, Port: 443, Allow",
        "domain": "Security Operations",
        "explanation": "Most web servers use tcp/443 for HTTPS (Hypertext Transfer Protocol Secure) for encrypted web server communication This rule allows HTTPS encrypted traffic to be forwarded to the web server over tcp/443."
    },
    {
        "question": "Which of these would be used to provide multi-factor authentication?",
        "options": [
            "USB-connected storage drive with FDE",
            "Employee policy manual",
            "Just-in-time permissions",
            "Smart card with picture ID"
        ],
        "answer": "Smart card with picture ID",
        "domain": "Security Operations",
        "explanation": "A smart card commonly includes a certificate that can be used as a multi-factor authentication of something you have. These smart cards are commonly combined with an employee identification card, and often require a separate PIN (Personal Identification Number) as an additional authentication factor."
    },
    {
        "question": "A company's network team has been asked to build an IPsec tunnel to a new business partner. Which of the following security risks would be the MOST important to consider?",
        "options": [
            "Supply chain attack",
            "Unsupported systems",
            "Business email compromise",
            "Typosquatting"
        ],
        "answer": "Supply chain attack",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "A direct connection to a third-party creates potential access for an attacker. Most organizations will include a firewall to help monitor and protect against any supply chain attacks."
    },
    {
        "question": "A company's human resources team maintains a list of all employees participating in the corporate savings plan. A third-party financial company uses this information to manage stock investments for the employees. Which of the following would describe this financial company?",
        "options": [
            "Processor",
            "Owner",
            "Controller",
            "Custodian"
        ],
        "answer": "Processor",
        "domain": "Governance, Risk, and Compliance",
        "explanation": "A data processor performs some type of action to the data, and this is often a different group within the organization or a third-party company. In this example, the third-party financial organization is the data processor of the employee's financial data."
    },
    {
        "question": "A technology company is manufacturing a military-grade radar tracking system designed to identify any nearby unmanned aerial vehicles (UAVs). The UAV detector must be able to instantly identify and react to a vehicle without delay. Which of the following would BEST describe this tracking system?",
        "options": [
            "RTOS",
            "IoT",
            "ICS",
            "SDN"
        ],
        "answer": "RTOS",
        "domain": "Infrastructure Security",
        "explanation": "This tracking system requires an RTOS (Real-Time Operating System) to instantly react to input without any significant delays or queuing in the operating system. Operating systems used by the military, automobile manufacturers, and industrial equipment companies often use RTOS to process certain transactions without any significant delays."
    },
    {
        "question": "An administrator is writing a script to convert an email message to a help desk ticket and assign the ticket to the correct department. Which of the following should be administrator use to complete this script?",
        "options": [
            "Role-based access controls",
            "Federation",
            "Due diligence",
            "Orchestration"
        ],
        "answer": "Orchestration",
        "domain": "Security Operations",
        "explanation": "Orchestration describes the process of automation, and is commonly associated with large scale automation or automating processes between different systems."
    },
    {
        "question": "A security administrator would like a report showing how many attackers are attempting to use a known vulnerability to gain access to a corporate web server. Which of the following should be used to gather this information?",
        "options": [
            "Application log",
            "Metadata",
            "IPS log",
            "Windows log"
        ],
        "answer": "IPS log",
        "domain": "Security Operations",
        "explanation": "An IPS (Intrusion Prevention System) commonly uses a database of known vulnerabilities to identify and block malicious network traffic. This log of attempted exploits would provide the required report information."
    },
    {
        "question": "During a ransomware outbreak, an organization was forced to rebuild database servers from known good backup systems. In which of the following incident response phases were these database servers brought back online?",
        "options": [
            "Recovery",
            "Lessons learned",
            "Containment",
            "Detection"
        ],
        "answer": "Recovery",
        "domain": "Security Operations",
        "explanation": "The recovery phase focuses on getting things back to normal after an attack. This is the phase that removes malware, fixes vulnerabilities, and recovers the damaged systems."
    },
    {
        "question": "A security administrator is installing a web server with a newly built operating system. Which of the following would be the best way to harden this OS?",
        "options": [
            "Create a backup schedule",
            "Install a device certificate",
            "Remove unnecessary software",
            "Disable power management features"
        ],
        "answer": "Remove unnecessary software",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "The process of hardening an operating system makes it more difficult to attack. In this example, the only step that would limit the attack surface is to remove any unnecessary or unused software."
    },
    {
        "question": "A network IPS has created this log entry:\nFrame 4: 937 bytes on wire (7496 bits), 937 bytes captured Ethernet II, Src: HewlettP_82:d8:31, Dst: Cisco_a1:b0:d1 Internet Protocol Version 4, Src: 172.16.22.7, Dst: 10.8.122.244 Transmission Control Protocol, Src Port: 3863, Dst Port: 1433 Application Data: SELECT * FROM users WHERE username='x' or 'x'='x' AND password='x' or 'x'='x'\nWhich of the following would describe this log entry?",
        "options": [
            "Phishing",
            "Brute force",
            "SQL injection",
            "Cross-site scripting"
        ],
        "answer": "SQL injection",
        "domain": "Threats, Vulnerabilities, and Mitigations",
        "explanation": "The SQL injection is contained in the application data. The attacker was attempting to circumvent the authentication through the use of equivalent SQL statements ('x'='x')."
    },
    {
        "question": "An incident response team would like to validate their disaster recovery plans without making any changes to the infrastructure. Which of the following would be the best course of action?",
        "options": [
            "Tabletop exercise",
            "Hot site fail-over",
            "Simulation",
            "Penetration test"
        ],
        "answer": "Tabletop exercise",
        "domain": "Infrastructure Security",
        "explanation": "A tabletop exercise is a walk-through exercise where the disaster recovery process can be discussed in a conference room without making any changes to the existing systems."
    },
    {
        "question": "A system administrator has installed a new firewall between the corporate user network and the data center network. When the firewall is turned on with the default settings, users complain the application in the data center is no longer working. Which of the following would be the BEST way to correct this application issue?",
        "options": [
            "Create a single firewall rule with an explicit deny",
            "Build a separate VLAN for the application",
            "Create firewall rules that match the application traffic flow",
            "Enable firewall threat blocking"
        ],
        "answer": "Create firewall rules that match the application traffic flow",
        "domain": "Security Operations",
        "explanation": "By default, most firewalls implicitly deny all traffic. Firewall rules must be built to match the traffic flows, and only then will traffic pass through the firewall."
    },
    {
        "question": "Which of these would be used to provide HA for a web-based database application?",
        "options": [
            "SIEM",
            "UPS",
            "DLP",
            "VPN concentrator"
        ],
        "answer": "UPS",
        "domain": "Infrastructure Security",
        "explanation": "HA (High Availability) means the service should always be on and available. The only device on this list providing HA is the UPS (Uninterruptible Power Supply). If power is lost, the UPS will provide electricity using battery power or a gas-powered generator."
    },
    {
        "question": "Which of the following would be the BEST way to prevent unauthorized access to a wireless network?",
        "options": [
            "Disable SSID broadcasting",
            "Enable MAC filtering",
            "Use WPA3 with 802.1X authentication",
            "Change the default admin password"
        ],
        "answer": "Use WPA3 with 802.1X authentication",
        "domain": "Security Architecture",
        "explanation": "WPA3 with 802.1X provides the strongest wireless security by requiring each user to authenticate with unique credentials through a RADIUS server, making it much harder for unauthorized users to gain access."
    },
    {
        "question": "A security analyst notices unusual network traffic patterns during non-business hours. Which of the following would be the BEST way to investigate this?",
        "options": [
            "Review firewall logs",
            "Check system backups",
            "Update antivirus signatures",
            "Perform a vulnerability scan"
        ],
        "answer": "Review firewall logs",
        "domain": "Security Operations",
        "explanation": "Firewall logs contain detailed information about network traffic, including source/destination IPs, ports, and timestamps, making them the best resource for investigating unusual network activity."
    },
    {
        "question": "Which of the following is the MOST important reason to implement a change management process?",
        "options": [
            "To reduce system downtime",
            "To track system changes",
            "To prevent unauthorized modifications",
            "To improve system performance"
        ],
        "answer": "To prevent unauthorized modifications",
        "domain": "Security Program Management and Oversight",
        "explanation": "The primary purpose of change management is to prevent unauthorized or unplanned changes that could introduce security vulnerabilities or system instability."
    },
    {
        "question": "Which of the following would be the MOST effective way to prevent data exfiltration through USB devices?",
        "options": [
            "Implement DLP software",
            "Disable USB ports in BIOS",
            "Use encrypted USB drives",
            "Monitor USB usage"
        ],
        "answer": "Disable USB ports in BIOS",
        "domain": "Security Operations",
        "explanation": "While all options provide some level of protection, physically disabling USB ports at the BIOS level is the most effective as it completely prevents the use of USB devices, eliminating the risk of data exfiltration through this vector."
    },
    {
        "question": "A company wants to ensure their cloud storage solution meets compliance requirements. Which of the following would be the MOST important to verify?",
        "options": [
            "Data encryption at rest",
            "Geographic location of data centers",
            "Backup frequency",
            "Access control methods"
        ],
        "answer": "Geographic location of data centers",
        "domain": "Security Program Management and Oversight",
        "explanation": "Data sovereignty and compliance requirements often mandate that data be stored in specific geographic locations. This is a fundamental requirement that must be met before other security controls can be considered."
    },
    {
        "question": "Which of the following would be the BEST way to protect against zero-day vulnerabilities?",
        "options": [
            "Keep systems patched",
            "Use antivirus software",
            "Implement network segmentation",
            "Enable host-based firewalls"
        ],
        "answer": "Implement network segmentation",
        "domain": "Security Architecture",
        "explanation": "While all options are important, network segmentation is the most effective against zero-day vulnerabilities as it limits the potential impact by containing any successful exploit to a specific network segment."
    },
    {
        "question": "Which of the following would be the MOST effective way to prevent social engineering attacks?",
        "options": [
            "Implement strong password policies",
            "Conduct regular security awareness training",
            "Use multi-factor authentication",
            "Deploy email filtering"
        ],
        "answer": "Conduct regular security awareness training",
        "domain": "Security Program Management and Oversight",
        "explanation": "While technical controls help, the most effective defense against social engineering is educating users. Regular security awareness training helps employees recognize and respond appropriately to social engineering attempts."
    },
    {
        "question": "A security team needs to monitor for potential data breaches. Which of the following would be the MOST comprehensive solution?",
        "options": [
            "Implement a SIEM",
            "Deploy an IDS",
            "Use network monitoring tools",
            "Enable system logging"
        ],
        "answer": "Implement a SIEM",
        "domain": "Security Operations",
        "explanation": "A Security Information and Event Management (SIEM) system provides comprehensive monitoring by collecting and analyzing security events from multiple sources, correlating them, and providing real-time alerts."
    },
    {
        "question": "Which of the following would be the BEST way to ensure secure communication between two offices?",
        "options": [
            "Use a site-to-site VPN",
            "Implement a DMZ",
            "Deploy a proxy server",
            "Configure a firewall"
        ],
        "answer": "Use a site-to-site VPN",
        "domain": "Security Architecture",
        "explanation": "A site-to-site VPN creates an encrypted tunnel between two networks, ensuring that all traffic between the offices is secure and protected from interception."
    },
    {
        "question": "Which of the following would be the MOST effective way to prevent unauthorized access to a server room?",
        "options": [
            "Install security cameras",
            "Use biometric access control",
            "Post security guards",
            "Implement key card access"
        ],
        "answer": "Use biometric access control",
        "domain": "Physical Security",
        "explanation": "Biometric access control provides the highest level of security as it cannot be shared, lost, or stolen like keys or access cards. It ensures that only authorized personnel can access the server room."
    },
    {
        "question": "A company needs to ensure their web application is secure against common attacks. Which of the following would be the MOST comprehensive approach?",
        "options": [
            "Implement input validation",
            "Use HTTPS",
            "Conduct regular penetration testing",
            "Enable WAF"
        ],
        "answer": "Conduct regular penetration testing",
        "domain": "Security Operations",
        "explanation": "While all options are important, regular penetration testing provides the most comprehensive security assessment by actively attempting to exploit vulnerabilities in the application, helping identify and fix security issues before attackers can find them."
    },
    {
        "question": "Which of the following would be the BEST way to protect against ransomware attacks?",
        "options": [
            "Implement email filtering",
            "Use antivirus software",
            "Maintain regular backups",
            "Enable system restore points"
        ],
        "answer": "Maintain regular backups",
        "domain": "Security Operations",
        "explanation": "While all options help prevent ransomware, maintaining regular backups is the most effective recovery strategy. If systems are encrypted by ransomware, having recent backups allows for quick recovery without paying the ransom."
    },
    {
        "question": "Which of the following would be the MOST effective way to prevent data breaches in a cloud environment?",
        "options": [
            "Use strong passwords",
            "Implement encryption",
            "Enable multi-factor authentication",
            "Configure proper IAM policies"
        ],
        "answer": "Configure proper IAM policies",
        "domain": "Cloud Security",
        "explanation": "While all options are important, proper Identity and Access Management (IAM) policies are fundamental to cloud security. They ensure that users and services have only the permissions they need, following the principle of least privilege."
    },
    {
        "question": "A company needs to ensure their mobile devices are secure. Which of the following would be the MOST comprehensive solution?",
        "options": [
            "Implement screen locks",
            "Use MDM software",
            "Enable device encryption",
            "Install antivirus"
        ],
        "answer": "Use MDM software",
        "domain": "Mobile Security",
        "explanation": "Mobile Device Management (MDM) software provides comprehensive security by allowing centralized management of mobile devices, including enforcing security policies, remote wiping, and monitoring device compliance."
    },
    {
        "question": "Which of the following would be the BEST way to protect against insider threats?",
        "options": [
            "Implement DLP",
            "Use access logs",
            "Conduct background checks",
            "Enable system monitoring"
        ],
        "answer": "Implement DLP",
        "domain": "Security Operations",
        "explanation": "Data Loss Prevention (DLP) solutions are specifically designed to prevent sensitive data from being accessed, used, or transmitted inappropriately by insiders, making it the most effective tool against insider threats."
    },
    // --- NEW QUESTIONS (deduplicated) ---
    {
        "question": "A security administrator has performed an audit of the organization's production web servers, and the results have identified default configurations, web services running from a privileged account, and inconsistencies with SSL certificates. Which of the following would be the BEST way to resolve these issues?",
        "options": ["Server hardening", "Multi-factor authentication", "Enable HTTPS", "Run operating system updates"],
        "answer": "Server hardening",
        "domain": "Hardening Techniques",
        "explanation": "The correct answer is Server hardening. Many applications and services include secure configuration guides to assist in hardening the system. These hardening steps will make the system as secure as possible while simultaneously allowing the application to run efficiently. Multi-factor authentication, while a good practice, would not resolve these specific configuration issues. Enabling HTTPS encrypts traffic but does not correct the underlying audit findings. Similarly, OS updates are crucial but don't address the specific web server configuration problems identified."
    },
    {
        "question": "A shipping company stores information in small regional warehouses around the country. The company maintains an IPS at each warehouse to watch for suspicious traffic patterns. Which of the following would BEST describe the security control used at the warehouse?",
        "options": ["Deterrent", "Compensating", "Directive", "Detective"],
        "answer": "Detective",
        "domain": "Security Controls",
        "explanation": "The correct answer is Detective. An IPS can detect, alert, and log an intrusion attempt, which is a detective function. It can also be categorized as a preventive control since it can actively block known attacks. A deterrent control discourages attempts (like a warning sign). A compensating control is an alternative measure when a primary control fails (like re-imaging a server). A directive control provides guidance (like user training)."
    },
    {
        "question": "The Vice President of Sales has asked the IT team to create daily backups of the sales data. The Vice President is an example of a:",
        "options": ["Data owner", "Data controller", "Data steward", "Data processor"],
        "answer": "Data owner",
        "domain": "Data Roles and Responsibilities",
        "explanation": "The correct answer is Data owner. The data owner is accountable for specific data, and this role is often held by a senior officer of the organization, like a Vice President. A data controller manages how data is processed. A data steward manages access rights. A data processor is often a third-party that processes data on behalf of the controller."
    },
    {
        "question": "A security engineer is preparing to conduct a penetration test of a third-party website. Part of the preparation involves reading through social media posts for information about this site. Which of the following describes this practice?",
        "options": ["Partially known environment", "OSINT", "Exfiltration", "Active reconnaissance"],
        "answer": "OSINT",
        "domain": "Threat Intelligence",
        "explanation": "The correct answer is OSINT (Open Source Intelligence). OSINT describes the process of obtaining information from open sources such as social media sites, corporate websites, and other publicly available locations. This is a form of passive reconnaissance. Active reconnaissance involves direct interaction with the target (like a port scan) that could be detected. Exfiltration is the act of stealing data. A partially known environment refers to the amount of information the tester is given beforehand."
    },
    {
        "question": "A company would like to orchestrate the response when a virus is detected on company devices. Which of the following would be the BEST way to implement this function?",
        "options": ["Active reconnaissance", "Log aggregation", "Vulnerability scan", "Escalation scripting"],
        "answer": "Escalation scripting",
        "domain": "Scripting and Automation",
        "explanation": "The correct answer is Escalation scripting. Scripting and automation can provide methods to automate or orchestrate the escalation and response when a security issue is detected. Log aggregation centralizes logs for analysis, vulnerability scanning identifies potential weaknesses, and active reconnaissance gathers information; none of these orchestrate a response."
    },
    {
        "question": "A user in the accounting department has received a text message from the CEO. The message requests payment by cryptocurrency for a recently purchased tablet. Which of the following would BEST describe this attack?",
        "options": ["Brand impersonation", "Watering hole attack", "Smishing", "Typosquatting"],
        "answer": "Smishing",
        "domain": "Phishing",
        "explanation": "The correct answer is Smishing. Smishing is phishing conducted via SMS (text messaging). A message allegedly from the CEO asking for an unusual payment method like cryptocurrency is a classic example. Brand impersonation involves pretending to be a well-known company. A watering hole attack compromises a website frequented by the target group. Typosquatting uses misspelled domain names to trick users."
    },
    {
        "question": "A company has been informed of a hypervisor vulnerability that could allow users on one virtual machine to access resources on another virtual machine. Which of the following would BEST describe this vulnerability?",
        "options": ["Containerization", "Jailbreaking", "SDN", "Escape"],
        "answer": "Escape",
        "domain": "Virtualization Vulnerabilities",
        "explanation": "The correct answer is Escape. A VM (Virtual Machine) escape is a vulnerability that allows an attacker to break out of a guest VM and interact with the host hypervisor or other VMs on the same host. Containerization is an application deployment method. Jailbreaking refers to removing restrictions on mobile devices. SDN is Software-Defined Networking."
    },
    {
        "question": "While working from home, users are attending a project meeting over a web conference. When typing in the meeting link, the browser is unexpectedly directed to a different website than the web conference. Users in the office do not have any issues accessing the conference site. Which of the following would be the MOST likely reason for this issue?",
        "options": ["Buffer overflow", "Wireless disassociation", "Amplified DDoS", "DNS poisoning"],
        "answer": "DNS poisoning",
        "domain": "DNS Attacks",
        "explanation": "The correct answer is DNS poisoning. In a DNS poisoning attack, an attacker modifies DNS records to redirect users to a malicious site. The fact that only remote users are affected suggests their DNS resolution (perhaps from their home ISP) has been compromised, while the office users, likely on a different DNS server, are unaffected."
    },
    {
        "question": "A company is launching a new internal application that will not start until a username and password is entered and a smart card is plugged into the computer. Which of the following BEST describes this process?",
        "options": ["Federation", "Accounting", "Authentication", "Authorization"],
        "answer": "Authentication",
        "domain": "Authentication, Authorization, and Accounting",
        "explanation": "The correct answer is Authentication. Authentication is the process of proving an identity. This example uses two factors of authentication: something you know (password) and something you have (smart card). Authorization determines what resources an authenticated user can access. Accounting tracks user actions. Federation provides authentication between different organizations."
    },
    {
        "question": "An online retailer is planning a penetration test as part of their PCI DSS validation. A third-party organization will be performing the test, and the online retailer has provided the Internet-facing IP addresses for their public web servers. No other details were provided. What penetration testing methodology is the online retailer using?",
        "options": ["Known environment", "Passive reconnaissance", "Partially known environment", "Benchmarks"],
        "answer": "Partially known environment",
        "domain": "Penetration Tests",
        "explanation": "The correct answer is Partially known environment. This type of test (also known as a gray-box test) is performed when the attacker is given some, but not all, information about the target. A known environment (white-box) provides full details. An unknown environment (black-box) provides no details. Passive reconnaissance is a technique for gathering information, not a testing methodology."
    },
    {
        "question": "A manufacturing company produces radar used by commercial and military organizations. A recently proposed policy change would allow the use of mobile devices inside the facility. Which of the following would be the MOST significant threat vector issue associated with this change in policy?",
        "options": ["Unauthorized software on rooted devices", "Remote access clients on the mobile devices", "Out of date mobile operating systems", "Loss of intellectual property"],
        "answer": "Loss of intellectual property",
        "domain": "Common Threat Vectors",
        "explanation": "The correct answer is Loss of intellectual property. The ability to easily take photos, videos, or transfer files makes mobile devices a significant vector for the exfiltration of confidential information and intellectual property. While the other options are valid security concerns, the direct threat of data theft in a sensitive environment is the most significant."
    },
    {
        "question": "Which of the following would be the BEST way for an organization to verify the digital signature provided by an external email server?",
        "options": ["Perform a vulnerability scan", "View the server's device certificate", "Authenticate to a RADIUS server", "Check the DKIM record"],
        "answer": "Check the DKIM record",
        "domain": "Email Security",
        "explanation": "The correct answer is Check the DKIM record. DKIM (Domain Keys Identified Mail) is an email authentication method that uses a digital signature linked to the domain. The public key for verification is published in the sender's DNS records. This allows a receiving server to verify that the email was authorized by the owner of that domain."
    },
    {
        "question": "A user in the accounting department would like to email a spreadsheet with sensitive information to a list of third-party vendors. Which of the following would be the BEST way to protect the data in this email?",
        "options": ["Full disk encryption", "Key exchange algorithm", "Salted hash", "Asymmetric encryption"],
        "answer": "Asymmetric encryption",
        "domain": "Encrypting Data",
        "explanation": "The correct answer is Asymmetric encryption. This method uses a public key (which can be shared with anyone) to encrypt data and a private key (kept secret by the recipient) to decrypt it. This is ideal for sending secure data to third parties, as they can provide their public key without compromising security. Technologies like PGP/GPG use this method."
    },
    {
        "question": "A system administrator would like to segment the network to give the marketing, accounting, and manufacturing departments their own private network. The network communication between departments would be restricted for additional security. Which of the following should be configured on this network?",
        "options": ["VPN", "RBAC", "VLAN", "SDN"],
        "answer": "VLAN",
        "domain": "Segmentation and Access Control",
        "explanation": "The correct answer is VLAN (Virtual Local Area Network). VLANs allow a network administrator to logically segment a single physical network into multiple separate broadcast domains. This is a common method for creating separate networks for different departments, and traffic between VLANs can be controlled with a router or Layer 3 switch."
    },
    {
        "question": "A technician at an MSP has been asked to manage devices on third-party private network. The technician needs command line access to internal routers, switches, and firewalls. Which of the following would provide the necessary access?",
        "options": ["HSM", "Jump server", "NAC", "Air gap"],
        "answer": "Jump server",
        "domain": "Network Appliances",
        "explanation": "The correct answer is Jump server. A jump server (or jump host) is a secure, hardened computer on a network that is used to access and manage devices in a separate security zone. An administrator connects to the jump server and then 'jumps' from there to the target devices. This provides a secure, controlled, and audited access point."
    },
    {
        "question": "A transportation company is installing new wireless access points in their corporate office. The manufacturer estimates the access points will operate an average of 100,000 hours before a hardware-related outage. Which of the following describes this estimate?",
        "options": ["MTTR", "RPO", "RTO", "MTBF"],
        "answer": "MTBF",
        "domain": "Business Impact Analysis",
        "explanation": "The correct answer is MTBF (Mean Time Between Failures). MTBF is a measure of the predicted elapsed time between inherent failures of a mechanical or electronic system during normal system operation. MTTR is Mean Time to Repair, RPO is Recovery Point Objective, and RTO is Recovery Time Objective."
    },
    {
        "question": "A security administrator is creating a policy to prevent the disclosure of credit card numbers in a customer support application. Users of the application would only be able to view the last four digits of a credit card number. Which of the following would provide this functionality?",
        "options": ["Hashing", "Tokenization", "Masking", "Salting"],
        "answer": "Masking",
        "domain": "Protecting Data",
        "explanation": "The correct answer is Masking. Data masking is a method of hiding the original data with modified content (e.g., characters like 'x' or '*'). Displaying only the last four digits of a credit card number is a common form of data masking. Tokenization replaces sensitive data with a non-sensitive equivalent (a token). Hashing creates a one-way representation of data."
    },
    {
        "question": "A user is authenticating through the use of a PIN and a fingerprint. Which of the following would describe these authentication factors?",
        "options": ["Something you know, something you are", "Something you are, somewhere you are", "Something you have, something you know", "Somewhere you are, something you are"],
        "answer": "Something you know, something you are",
        "domain": "Multi-factor Authentication",
        "explanation": "The correct answer is 'Something you know, something you are'. Authentication factors are categorized as something you know (e.g., password, PIN), something you have (e.g., smart card, phone), and something you are (e.g., fingerprint, facial scan). A PIN falls into the 'know' category, and a fingerprint falls into the 'are' category."
    },
    {
        "question": "A security administrator is configuring the authentication process used by technicians when logging into wireless access points and switches. Instead of using local accounts, the administrator would like to pass all login requests to a centralized database. Which of the following would be the BEST way to implement this requirement?",
        "options": ["COPE", "AAA", "IPsec", "SIEM"],
        "answer": "AAA",
        "domain": "Wireless Security Settings",
        "explanation": "The correct answer is AAA (Authentication, Authorization, and Accounting). AAA frameworks, often implemented with protocols like RADIUS or TACACS+, are used to provide centralized authentication services for network devices, preventing the need for separate local user accounts on each device."
    },
    {
        "question": "A recent audit has determined that many IT department accounts have been granted Administrator access. The audit recommends replacing these permissions with limited access rights. Which of the following would describe this policy?",
        "options": ["Password vaulting", "Offboarding", "Least privilege", "Discretionary access control"],
        "answer": "Least privilege",
        "domain": "Access Controls",
        "explanation": "The correct answer is Least privilege. The principle of least privilege requires that a user be given only the minimum levels of access – or permissions – needed to perform their job functions. Granting full administrator rights when not necessary violates this principle."
    },
    {
        "question": "A recent security audit has discovered usernames and passwords which can be easily viewed in a packet capture. Which of the following did the audit identify?",
        "options": ["Weak encryption", "Improper patch management", "Insecure protocols", "Open ports"],
        "answer": "Insecure protocols",
        "domain": "Secure Protocols",
        "explanation": "The correct answer is Insecure protocols. If usernames and passwords can be viewed in a packet capture, it means they are being transmitted in plaintext (unencrypted). This is a hallmark of insecure protocols like Telnet, FTP, or HTTP, which do not encrypt communications."
    },
    {
        "question": "Before deploying a new application, a company is performing an internal audit to ensure all of their servers are configured with the appropriate security features. Which of the following would BEST describe this process?",
        "options": ["Due care", "Active reconnaissance", "Data retention", "Statement of work"],
        "answer": "Due care",
        "domain": "Compliance",
        "explanation": "The correct answer is Due care. Due care is the action that a reasonable person would take to ensure security. Performing an internal audit to check for proper configurations before deployment is a perfect example of an organization exercising due care to protect its assets. Due diligence is the investigation and research before an action, while due care is the action itself."
    },
    {
        "question": "An organization has previously purchased insurance to cover a ransomware attack, but the costs of maintaining the policy have increased above the acceptable budget. The company has now decided to cancel the insurance policies and address potential ransomware issues internally. Which of the following would best describe this action?",
        "options": ["Mitigation", "Acceptance", "Transference", "Risk-avoidance"],
        "answer": "Acceptance",
        "domain": "Risk Management Strategies",
        "explanation": "The correct answer is Acceptance. Risk acceptance means acknowledging a risk and not taking any action to reduce it, either because the cost of mitigation is too high or the impact is deemed acceptable. By cancelling the insurance (which was a form of transference), the company is now accepting the financial risk of a ransomware attack."
    },
    {
        "question": "Which of these threat actors would be MOST likely to install a company's internal application on a public cloud provider?",
        "options": ["Organized crime", "Nation state", "Shadow IT", "Hacktivist"],
        "answer": "Shadow IT",
        "domain": "Threat Actors",
        "explanation": "The correct answer is Shadow IT. Shadow IT refers to IT systems and solutions built and used inside organizations without explicit organizational approval. Employees or departments might set up their own solutions on public cloud services to bypass corporate IT policies or processes, creating security risks."
    },
    {
        "question": "An IPS report shows a series of exploit attempts were made against externally facing web servers. The system administrator of the web servers has identified a number of unusual log entries on each system. Which of the following would be the NEXT step in the incident response process?",
        "options": ["Check the IPS logs for any other potential attacks", "Create a plan for removing malware from the web servers", "Disable any breached user accounts", "Disconnect the web servers from the network"],
        "answer": "Disconnect the web servers from the network",
        "domain": "Incident Response",
        "explanation": "The correct answer is to Disconnect the web servers from the network. This is the containment phase of incident response. Once a compromise is suspected or confirmed, the first priority is to isolate the affected systems to prevent the attack from spreading further across the network or exfiltrating more data."
    },
    {
        "question": "A security administrator is viewing the logs on a laptop in the shipping and receiving department and identifies these events:\n8:55:30 AM | D:\\Downloads\\ChangeLog-5.0.4.scr | Quarantine Success\n9:22:54 AM | C:\\Program Files\\Photo Viewer\\ViewerBase.dll | Quarantine Failure\n9:44:05 AM | C:\\Sales\\Sample32.dat | Quarantine Success\nWhich of the following would BEST describe the circumstances surrounding these events?",
        "options": ["The antivirus application identified three viruses and quarantined two viruses", "The host-based firewall blocked two traffic flows", "A host-based allow list has blocked two applications from executing", "A network-based IPS has identified two known vulnerabilities"],
        "answer": "The antivirus application identified three viruses and quarantined two viruses",
        "domain": "Log Data",
        "explanation": "The correct answer is A. The log entries show file paths and a 'Quarantine' disposition, which is a standard action for antivirus software. It indicates that the software detected malicious files and attempted to move them to a safe location (quarantine). Two attempts were successful, and one failed, likely because the file was in use by the system."
    },
    {
        "question": "In the past, an organization has relied on the curated Apple App Store to avoid issues associated with malware and insecure applications. However, the IT department has discovered an iPhone in the shipping department with applications not available on the Apple App Store. How did the shipping department user install these apps on their mobile device?",
        "options": ["Side loading", "Malicious update", "VM escape", "Cross-site scripting"],
        "answer": "Side loading",
        "domain": "Mobile Device Vulnerabilities",
        "explanation": "The correct answer is Side loading. Sideloading is the process of installing an application package in an APK or IPA format onto a mobile device, bypassing the official app store. This is often possible on devices that have been jailbroken (iOS) or have had their security settings changed (Android)."
    },
    {
        "question": "A company has noticed an increase in support calls from attackers. These attackers are using social engineering to gain unauthorized access to customer data. Which of the following would be the BEST way to prevent these attacks?",
        "options": ["User training", "Next-generation firewall", "Internal audit", "Penetration testing"],
        "answer": "User training",
        "domain": "User Training",
        "explanation": "The correct answer is User training. Social engineering attacks prey on human psychology. Technical controls like firewalls are often ineffective against them. The most effective defense is to train users to recognize social engineering tactics and follow proper procedures for verifying identity and handling sensitive information."
    },
    {
        "question": "As part of an internal audit, each department of a company has been asked to compile a list of all devices, operating systems, and applications in use. Which of the following would BEST describe this audit?",
        "options": ["Attestation", "Self-assessment", "Regulatory compliance", "Vendor monitoring"],
        "answer": "Self-assessment",
        "domain": "Audits and Assessments",
        "explanation": "The correct answer is Self-assessment. A self-assessment is an internal review where an organization evaluates its own security posture, policies, and controls against a set of standards. Having departments compile their own asset lists is a key part of this process."
    },
    {
        "question": "A company is concerned about security issues at their remote sites. Which of the following would provide the IT team with more information of potential shortcomings?",
        "options": ["Gap analysis", "Policy administrator", "Change management", "Dependency list"],
        "answer": "Gap analysis",
        "domain": "Gap Analysis",
        "explanation": "The correct answer is Gap analysis. A gap analysis is a formal process for comparing the actual performance or state of security with the desired state. It helps identify the 'gaps' or shortcomings between where the company currently is and where it needs to be, which is exactly what's needed for the remote sites."
    },
    {
        "question": "An attacker has identified a number of devices on a corporate network with the username of \"admin\" and the password of \"admin.\" Which of the following describes this situation?",
        "options": ["Open service ports", "Default credentials", "Unsupported systems", "Phishing"],
        "answer": "Default credentials",
        "domain": "Common Threat Vectors",
        "explanation": "The correct answer is Default credentials. Many devices are shipped from the manufacturer with a default username and password (like admin/admin). Failing to change these credentials upon installation is a major security vulnerability, as these defaults are widely known."
    },
    {
        "question": "A security administrator attends an annual industry convention with other security professionals from around the world. Which of the following attacks would be MOST likely in this situation?",
        "options": ["Smishing", "Supply chain", "SQL injection", "Watering hole"],
        "answer": "Watering hole",
        "domain": "Watering Hole Attacks",
        "explanation": "The correct answer is Watering hole. A watering hole attack targets a specific group of people by compromising a website or service they are known to frequent. An attacker might compromise the conference Wi-Fi, a related industry news site, or the conference's own website to target the attendees."
    },
    {
        "question": "A transportation company headquarters is located in an area with frequent power surges and outages. The security administrator is concerned about the potential for downtime and hardware failures. Which of the following would provide the most protection against these issues? Select TWO.",
        "options": ["UPS", "Parallel processing", "Snapshots", "Multi-cloud system", "Load balancing", "Generator"],
        "answer": ["UPS, Generator"],
        "domain": "Power Resiliency",
        "explanation": "The correct answers are UPS and Generator. A UPS (Uninterruptible Power Supply) provides immediate, short-term battery power to allow systems to shut down gracefully or to bridge the gap until a long-term power source comes online. A generator can provide long-term power for the duration of an extended outage, as long as it has fuel."
    },
    {
        "question": "An organization has developed an in-house mobile device app for order processing. The developers would like the app to identify revoked server certificates without sending any traffic over the corporate Internet connection. Which of the following must be configured to allow this functionality?",
        "options": ["CSR generation", "OCSP stapling", "Key escrow", "Wildcard"],
        "answer": "OCSP stapling",
        "domain": "Certificates",
        "explanation": "The correct answer is OCSP stapling. With OCSP stapling, the web server periodically queries the OCSP responder itself and 'staples' the timestamped response to the SSL/TLS handshake. This allows the client to get the revocation status directly from the server, eliminating the need for the client to make a separate, external connection to the Certificate Authority."
    },
    {
        "question": "A security administrator has been asked to build a network link to secure all communication between two remote locations. Which of the following would be the best choice for this task?",
        "options": ["SCAP", "Screened subnet", "IPsec", "Network access control"],
        "answer": "IPsec",
        "domain": "Secure Communication",
        "explanation": "The correct answer is IPsec (Internet Protocol Security). IPsec is a suite of protocols commonly used to secure communications between two points, typically by creating a site-to-site VPN (Virtual Private Network) tunnel. It provides confidentiality and integrity for all traffic sent between the two locations."
    },
    {
        "question": "A Linux administrator has received a ticket complaining of response issues with a database server. After connecting to the server, the administrator views this information:\nFilesystem Size Used Avail Use% Mounted on\n/dev/xvda1 158G 158G 0 100% /\nWhich of the following would BEST describe this information?",
        "options": ["Buffer overflow", "Resource consumption", "SQL injection", "Race condition"],
        "answer": "Resource consumption",
        "domain": "Indicators of Compromise",
        "explanation": "The correct answer is Resource consumption. The output clearly shows that the root filesystem ('/') has 0 bytes available and is at 100% utilization. This exhaustion of disk space is a form of resource consumption attack (or issue) that can cause services like a database to slow down or fail entirely."
    },
    {
        "question": "Which of the following can be used for credit card transactions from a mobile device without sending the actual credit card number across the network?",
        "options": ["Tokenization", "Hashing", "Steganography", "Masking"],
        "answer": "Tokenization",
        "domain": "Protecting Data",
        "explanation": "The correct answer is Tokenization. Tokenization is a process where sensitive data (like a credit card number) is replaced with a unique, non-sensitive equivalent referred to as a token. This token can be used for transactions without exposing the actual card number. This is the core technology behind mobile payment systems like Apple Pay and Google Pay."
    },
    {
        "question": "A security administrator receives a report each week showing a Linux vulnerability associated with a Windows server. Which of the following would prevent this information from appearing in the report?",
        "options": ["Alert tuning", "Application benchmarking", "SIEM aggregation", "Data archiving"],
        "answer": "Alert tuning",
        "domain": "Security Monitoring",
        "explanation": "The correct answer is Alert tuning. The report is generating a false positive – an alert for a vulnerability that doesn't apply to the target system (a Linux vulnerability on a Windows server). Alert tuning is the process of adjusting the rules and parameters of a monitoring system to reduce false positives and ensure that only relevant, actionable alerts are generated."
    },
    {
        "question": "Which of the following would a company use to calculate the loss of a business activity if a vulnerability is exploited?",
        "options": ["Risk tolerance", "Vulnerability classification", "Environmental variables", "Exposure factor"],
        "answer": "Exposure factor",
        "domain": "Analyzing Vulnerabilities",
        "explanation": "The correct answer is Exposure factor (EF). The Exposure Factor is the percentage of loss that an asset would suffer if a specific threat were realized. It's used in quantitative risk analysis along with the Asset Value (AV) to calculate the Single Loss Expectancy (SLE = AV * EF)."
    },
    {
        "question": "An administrator is designing a network to be compliant with a security standard for storing credit card numbers. Which of the following would be the BEST choice to provide this compliance?",
        "options": ["Implement RAID for all storage systems", "Connect a UPS to all servers", "DNS should be available on redundant servers", "Perform regular audits and vulnerability scans"],
        "answer": "Perform regular audits and vulnerability scans",
        "domain": "Compliance",
        "explanation": "The correct answer is Perform regular audits and vulnerability scans. Standards like the Payment Card Industry Data Security Standard (PCI DSS) explicitly require regular monitoring and testing of security controls, including frequent vulnerability scans and periodic audits, to ensure the ongoing protection of cardholder data."
    },
    {
        "question": "A company is accepting proposals for an upcoming project, and one of the responses is from a business owned by a board member. Which of the following would describe this situation?",
        "options": ["Due diligence", "Vendor monitoring", "Conflict of interest", "Right-to-audit"],
        "answer": "Conflict of interest",
        "domain": "Third-party Risk Assessment",
        "explanation": "The correct answer is Conflict of interest. A conflict of interest occurs when an individual's personal interests—family, friendships, financial, or social factors—could compromise their judgment, decisions, or actions in the workplace. A board member having a financial stake in a company bidding for a project is a classic example."
    },
    {
        "question": "A company has rolled out a new application that requires the use of a hardware-based token generator. Which of the following would be the BEST description of this access feature?",
        "options": ["Something you know", "Somewhere you are", "Something you are", "Something you have"],
        "answer": "Something you have",
        "domain": "Multi-factor Authentication",
        "explanation": "The correct answer is Something you have. A physical, hardware-based token generator is an object that the user must possess to authenticate. This falls into the 'something you have' category of authentication factors."
    },
    {
        "question": "A company has signed an SLA with an Internet service provider. Which of the following would BEST describe the requirements of this SLA?",
        "options": ["The customer will connect to remote sites over an IPsec tunnel", "The service provider will provide 99.99% uptime", "The customer applications use HTTPS over tcp/443", "Customer application use will be busiest on the 15th of each month"],
        "answer": "The service provider will provide 99.99% uptime",
        "domain": "Agreement Types",
        "explanation": "The correct answer is B. An SLA (Service Level Agreement) is a contract that defines the level of service expected from a provider. It typically includes specific, measurable metrics such as uptime guarantees (e.g., 99.99%), response times, and throughput. The other options describe how a customer might use the service, not the service level provided by the ISP."
    },
    {
        "question": "An attacker has created multiple social media accounts and is posting information in an attempt to get the attention of the media. Which of the following would BEST describe this attack?",
        "options": ["On-path", "Watering hole", "Misinformation campaign", "Phishing"],
        "answer": "Misinformation campaign",
        "domain": "Other Social Engineering Attacks",
        "explanation": "The correct answer is Misinformation campaign. This type of attack involves the deliberate spreading of false or misleading information to influence public opinion, cause confusion, or damage a reputation. Using multiple fake social media accounts to amplify the message is a common technique."
    },
    {
        "question": "Which of the following would be the BEST way to protect credit card account information when performing real-time purchase authorizations?",
        "options": ["Masking", "DLP", "Tokenization", "NGFW"],
        "answer": "Tokenization",
        "domain": "Protecting Data",
        "explanation": "The correct answer is Tokenization. Tokenization replaces the actual credit card number with a unique, single-use or limited-use token for the transaction. This means the sensitive card number is not transmitted or stored by the merchant, significantly reducing risk. Masking is for display, not transmission. DLP is for preventing data from leaving, not for securing transactions. An NGFW is a network security device."
    },
    {
        "question": "A company is installing access points in all of their remote sites. Which of the following would provide confidentiality for all wireless data?",
        "options": ["802.1X", "WPA3", "RADIUS", "MDM"],
        "answer": "WPA3",
        "domain": "Wireless Security Settings",
        "explanation": "The correct answer is WPA3 (Wi-Fi Protected Access 3). WPA3 is a security protocol that encrypts the data transmitted over a wireless network, providing confidentiality for the communication. 802.1X and RADIUS are used for authentication (verifying who can connect), not for encrypting the data itself. MDM is for managing devices."
    },
    {
        "question": "A user in the marketing department is unable to connect to the wireless network. After authenticating with a username and password, the user receives this message: 'The connection attempt could not be completed. The Credentials provided by the server could not be validated. Radius Server: radius.example.com Root CA: Example.com Internal CA Root Certificate' The access point is configured with WPA3 encryption and 802.1X authentication. Which of the following is the MOST likely reason for this login issue?",
        "options": ["The user's computer is in the incorrect VLAN", "The RADIUS server is not responding", "The user's computer does not support WPA3 encryption", "The user is in a location with an insufficient wireless signal", "The client computer does not have the proper certificate installed"],
        "answer": "The client computer does not have the proper certificate installed",
        "domain": "Certificates",
        "explanation": "The correct answer is E. The error message explicitly states that the server's credentials could not be validated and references a root CA certificate. In an 802.1X environment, the client needs to trust the RADIUS server. This is done by having the root certificate of the CA that issued the RADIUS server's certificate installed on the client machine. Without it, the client cannot validate the server's identity and will refuse the connection."
    },
    {
        "question": "A security administrator has created a new policy prohibiting the use of MD5 hashes due to collision problems. Which of the following describes the reason for this new policy?",
        "options": ["Two different messages have different hashes", "The original message can be derived from the hash", "Two identical messages have the same hash", "Two different messages share the same hash"],
        "answer": "Two different messages share the same hash",
        "domain": "Cryptographic Attacks",
        "explanation": "The correct answer is D. A hash collision occurs when two different inputs produce the exact same hash output. MD5 is known to be vulnerable to collision attacks, meaning an attacker can craft a malicious file that has the same MD5 hash as a legitimate one, undermining its use for integrity checking. A good hash algorithm should make it computationally infeasible to find collisions."
    },
    {
        "question": "A security administrator has been tasked with hardening all internal web servers to control access from certain IP address ranges and ensure all transferred data remains confidential. Which of the following should the administrator include in his project plan? (Select TWO)",
        "options": ["Change the administrator password", "Use HTTPS for all server communication", "Uninstall all unused software", "Enable a host-based firewall", "Install the latest operating system update"],
        "answer": ["Use HTTPS for all server communication", "Enable a host-based firewall"],
        "domain": "Hardening Techniques",
        "explanation": "The correct answers are B and D. To ensure data remains confidential during transfer, the administrator must use an encrypted protocol like HTTPS. To control access from specific IP address ranges, the administrator should enable a host-based firewall and create rules to allow or deny traffic based on source IP."
    },
    {
        "question": "A security administrator has identified the installation of ransomware on a database server and has quarantined the system. Which of the following should be followed to ensure that the integrity of the evidence is maintained?",
        "options": ["E-discovery", "Non-repudiation", "Chain of custody", "Legal hold"],
        "answer": "Chain of custody",
        "domain": "Digital Forensics",
        "explanation": "The correct answer is Chain of custody. The chain of custody is a chronological documentation or paper trail, showing the seizure, custody, control, transfer, analysis, and disposition of physical or electronic evidence. Maintaining a strict chain of custody is critical to ensure that the evidence is admissible in court and its integrity has not been compromised."
    },
    {
        "question": "Which of the following would be the BEST option for application testing in an environment completely separated from the production network?",
        "options": ["Virtualization", "VLANs", "Cloud computing", "Air gap"],
        "answer": "Air gap",
        "domain": "Network Infrastructure Concepts",
        "explanation": "The correct answer is Air gap. An air gap is a security measure that involves isolating a computer or network and preventing it from establishing an external connection. It is a physical separation, ensuring that the test environment has no network connectivity to the production network, providing the highest level of isolation."
    },
    {
        "question": "A security engineer is planning the installation of a new IPS. The network must remain operational if the IPS is turned off or disabled. Which of the following would describe this configuration?",
        "options": ["Containerization", "Load balancing", "Fail open", "Tunneling"],
        "answer": "Fail open",
        "domain": "Intrusion Prevention",
        "explanation": "The correct answer is Fail open. A 'fail open' state means that if the device fails, it will bypass the security function and allow traffic to continue flowing, prioritizing availability over security. The opposite is 'fail closed' or 'fail secure', which would block all traffic upon failure, prioritizing security over availability."
    },
    {
        "question": "Which of the following describes the process of hiding data from others by embedding the data inside of a different media type?",
        "options": ["Hashing", "Obfuscation", "Encryption", "Masking"],
        "answer": "Obfuscation",
        "domain": "Protecting Data",
        "explanation": "The correct answer is Obfuscation. Obfuscation is the practice of making something difficult to understand. Steganography is a form of obfuscation where data is hidden within another file, such as embedding a text document inside an image. The goal is to conceal the very existence of the message."
    },
    {
        "question": "Which of the following vulnerabilities would be the MOST significant security concern when protecting against a hacktivist?",
        "options": ["Data center access with only one authentication factor", "Spoofing of internal IP addresses when accessing an intranet server", "Employee VPN access uses a weak encryption cipher", "Lack of patch updates on an Internet-facing database server"],
        "answer": "Lack of patch updates on an Internet-facing database server",
        "domain": "Threat Actors",
        "explanation": "The correct answer is D. Hacktivists, as external threat actors, are most likely to attack public-facing systems. An unpatched, Internet-facing database server presents a direct and highly valuable target, as it likely contains data that could be stolen and leaked for political or social reasons. The other options are less likely vectors for an external hacktivist."
    },
    {
        "question": "A company is installing a security appliance to protect the organization's web-based applications from attacks such as SQL injections and unexpected input. Which of the following would BEST describe this appliance?",
        "options": ["WAF", "VPN concentrator", "UTM", "SASE"],
        "answer": "WAF",
        "domain": "Firewall Types",
        "explanation": "The correct answer is WAF (Web Application Firewall). A WAF is specifically designed to protect web applications by inspecting and filtering HTTP traffic between a web application and the Internet. It can detect and block common attacks like SQL injection, cross-site scripting (XSS), and other application-layer attacks."
    },
    {
        "question": "Which of the following would be the BEST way to determine if files have been modified after the forensics data acquisition process has occurred?",
        "options": ["Use a tamper seal on all storage devices", "Create a hash of the data", "Image each storage device for future comparison", "Take screenshots of file directories with file sizes"],
        "answer": "Create a hash of the data",
        "domain": "Digital Forensics",
        "explanation": "The correct answer is to create a hash of the data. During forensic acquisition, a cryptographic hash (e.g., SHA-256) of the original data is calculated. To verify the integrity of the evidence at any later time, the hash can be recalculated. If the new hash matches the original, it proves the data has not been altered."
    },
    {
        "question": "A system administrator is implementing a password policy that would require letters, numbers, and special characters to be included in every password. Which of the following controls MUST be in place to enforce this password policy?",
        "options": ["Length", "Expiration", "Reuse", "Complexity"],
        "answer": "Complexity",
        "domain": "Password Security",
        "explanation": "The correct answer is Complexity. Password complexity rules enforce the use of different character sets (uppercase letters, lowercase letters, numbers, and special characters). This makes passwords more resistant to brute-force and dictionary attacks."
    },
    {
        "question": "Which of the following would a company follow to deploy a weekly operating system patch?",
        "options": ["Tabletop exercise", "Penetration testing", "Change management", "Internal audit"],
        "answer": "Change management",
        "domain": "Change Management Process",
        "explanation": "The correct answer is Change management. Deploying a patch is a change to the IT environment. A formal change management process ensures that changes are documented, tested, approved, and implemented in a controlled manner to minimize disruption and unforeseen negative impacts."
    },
    {
        "question": "Which of the following would be the MOST likely result of plaintext application communication?",
        "options": ["Buffer overflow", "Replay attack", "Resource consumption", "Directory traversal"],
        "answer": "Replay attack",
        "domain": "Replay Attacks",
        "explanation": "The correct answer is Replay attack. In a replay attack, an attacker intercepts and re-transmits a valid data transmission. This is much easier to accomplish if the communication is in plaintext, as the attacker can capture and understand the traffic (e.g., an authentication session) and simply replay it to gain unauthorized access."
    },
    {
        "question": "A system administrator believes that certain configuration files on a Linux server have been modified from their original state. The administrator has reverted the configurations to their original state, but he would like to be notified if they are changed again. Which of the following would be the BEST way to provide this functionality?",
        "options": ["HIPS", "File integrity monitoring", "Application allow list", "WAF"],
        "answer": "File integrity monitoring",
        "domain": "Monitoring Data",
        "explanation": "The correct answer is File integrity monitoring (FIM). FIM tools work by creating a baseline hash of important files. They then periodically re-calculate the hashes and compare them to the baseline. If a hash changes, it indicates the file has been modified, and an alert is generated."
    },
    {
        "question": "A security administrator is updating the network infrastructure to support 802.1X. Which of the following would be the BEST choice for this configuration?",
        "options": ["LDAP", "SIEM", "SNMP traps", "SPF"],
        "answer": "LDAP",
        "domain": "Identity and Access Management",
        "explanation": "The correct answer is LDAP (Lightweight Directory Access Protocol). The 802.1X standard is for Port-Based Network Access Control and it requires a backend authentication server. LDAP is a common protocol used by directory services like Active Directory to provide the centralized user database that 802.1X can authenticate against. RADIUS is often the protocol that carries the authentication request from the switch/AP to the LDAP server."
    },
    {
        "question": "A company owns a time clock appliance, but the time clock doesn't provide any access to the operating system and it doesn't provide a method to upgrade the firmware. Which of the following describes this appliance?",
        "options": ["End-of-life", "ICS", "SDN", "Embedded system"],
        "answer": "Embedded system",
        "domain": "Other Infrastructure Concepts",
        "explanation": "The correct answer is Embedded system. An embedded system is a computer system with a dedicated function within a larger mechanical or electronic system. They often have a minimal user interface and limited or no user access to the underlying OS, and may not be designed for easy updates, making them a security challenge."
    },
    {
        "question": "A company has deployed laptops to all employees, and each laptop is enumerated during each login. Which of the following is supported with this configuration?",
        "options": ["If the laptop hardware is modified, the security team is alerted", "Any malware identified on the system is automatically deleted", "Users are required to use at least two factors of authentication", "The laptop is added to a private VLAN after the login process"],
        "answer": "If the laptop hardware is modified, the security team is alerted",
        "domain": "Asset Management",
        "explanation": "The correct answer is A. Enumeration is the process of identifying and listing the details of a system, including its hardware and software. By enumerating the laptop at login and comparing it to a known baseline, a security system can detect unauthorized hardware changes (e.g., a new USB device) and trigger an alert."
    },
    {
        "question": "A security manager believes that an employee is using their laptop to circumvent the corporate Internet security controls through the use of a cellular hotspot. Which of the following could be used to validate this belief? (Select TWO)",
        "options": ["HIPS", "UTM logs", "Web application firewall events", "Host-based firewall logs", "Next-generation firewall logs"],
        "answer": ["HIPS", "Host-based firewall logs"],
        "domain": "Hardening Techniques",
        "explanation": "The correct answers are A and D. Since the employee is using a cellular hotspot, the traffic is bypassing all network-based security controls (UTM, WAF, NGFW). The only place to find evidence of this traffic is on the endpoint itself. A HIPS (Host-based Intrusion Prevention System) and the logs from a host-based firewall could show network connections being made through an unexpected interface (the hotspot) to external destinations."
    },
    {
        "question": "An application developer is creating a mobile device app that will require a true random number generator real-time memory encryption. Which of the following technologies would be the BEST choice for this app?",
        "options": ["HSM", "Secure enclave", "NGFW", "Self-signed certificates"],
        "answer": "Secure enclave",
        "domain": "Encryption Technologies",
        "explanation": "The correct answer is Secure enclave. A secure enclave is a hardware-based security feature found in modern processors (like Apple's A-series or T-series chips). It's a dedicated, isolated processor that handles sensitive tasks like key management, cryptography, and can provide a hardware random number generator, making it ideal for the described requirements in a mobile app."
    },
    {
        "question": "Which of the following would be a common result of a successful vulnerability scan?",
        "options": ["Usernames and password hashes from a server", "A list of missing software patches", "A copy of image files from a private file share", "The BIOS configuration of a server"],
        "answer": "A list of missing software patches",
        "domain": "Vulnerability Scanning",
        "explanation": "The correct answer is B. A vulnerability scanner works by probing a system for known vulnerabilities. One of the most common findings is identifying services or applications that are out of date and missing critical security patches."
    },
    {
        "question": "When connected to the wireless network, users at a remote site receive an IP address which is not part of the corporate address scheme. Communication over this network is also slower than the wireless connections elsewhere in the building. Which of the following would be the MOST likely reason for these issues?",
        "options": ["Rogue access point", "Domain hijack", "DDoS", "Encryption is enabled"],
        "answer": "Rogue access point",
        "domain": "Common Threat Vectors",
        "explanation": "The correct answer is Rogue access point. A rogue AP is an unauthorized wireless access point connected to a network. The symptoms described—incorrect IP addressing (from the rogue AP's own DHCP server) and slow performance—are classic indicators of a rogue AP interfering with or supplanting the legitimate wireless network."
    },
    {
        "question": "A company has identified a compromised server, and the security team would like to know if an attacker has used this device to move between systems. Which of the following would be the BEST way to provide this information?",
        "options": ["DNS server logs", "Penetration test", "NetFlow logs", "Email metadata"],
        "answer": "NetFlow logs",
        "domain": "Security Tools",
        "explanation": "The correct answer is NetFlow logs. NetFlow is a protocol that collects metadata about IP traffic as it enters or exits an interface. It provides a high-level view of traffic patterns, including source/destination IPs, ports, and protocols. Analyzing NetFlow data from the compromised server would show all the other systems it communicated with, revealing lateral movement."
    },
    {
        "question": "A system administrator has protected a set of system backups with an encryption key. The system administrator used the same key when restoring files from this backup. Which of the following would BEST describe this encryption type?",
        "options": ["Asymmetric", "Key escrow", "Symmetric", "Out-of-band key exchange"],
        "answer": "Symmetric",
        "domain": "Public Key Infrastructure",
        "explanation": "The correct answer is Symmetric. Symmetric encryption uses a single, shared key for both the encryption and decryption processes. Since the administrator used the same key for both protecting (encrypting) and restoring (decrypting), it is symmetric encryption."
    },
    {
        "question": "A new malware variant takes advantage of a vulnerability in a popular email client. Once installed, the malware forwards all email attachments with credit card information to an external email address. Which of the following would limit the scope of this attack?",
        "options": ["Enable MFA on the email client", "Scan outgoing traffic with DLP", "Require users to enable the VPN when using email", "Update the list of malicious URLs in the firewall"],
        "answer": "Scan outgoing traffic with DLP",
        "domain": "Monitoring Data",
        "explanation": "The correct answer is B. A Data Loss Prevention (DLP) solution is designed to prevent sensitive data from leaving the network. It can inspect outbound traffic (including emails) for patterns matching sensitive information like credit card numbers and block the transmission, thus limiting the damage of the malware."
    },
    {
        "question": "A security administrator has been tasked with storing and protecting customer payment and shipping information for a three-year period. Which of the following would describe the source of this data?",
        "options": ["Controller", "Owner", "Data subject", "Processor"],
        "answer": "Data subject",
        "domain": "Privacy",
        "explanation": "The correct answer is Data subject. In privacy regulations like GDPR, the data subject is the individual to whom the personal data relates. The customer, whose payment and shipping information is being stored, is the data subject."
    },
    {
        "question": "A security administrator is using an access control where each file or folder is assigned a security clearance level, such as 'confidential' or 'secret.' The security administrator then assigns a maximum security level to each user. What type of access control is used in this network?",
        "options": ["Mandatory", "Rule-based", "Discretionary", "Role-based"],
        "answer": "Mandatory",
        "domain": "Access Controls",
        "explanation": "The correct answer is Mandatory Access Control (MAC). MAC is an access control model where the system, not the owner, controls access. It uses security labels (like Confidential, Secret, Top Secret) assigned to both subjects (users) and objects (files). Access is granted only if the subject's clearance level is equal to or higher than the object's classification."
    },
    {
        "question": "A security administrator is reviewing a report showing a number of devices on internal networks are connecting with servers in the data center network. Which of the following security systems should be added to prevent internal systems from accessing data center devices?",
        "options": ["VPN", "IPS", "SIEM", "ACL"],
        "answer": "ACL",
        "domain": "Segmentation and Access Control",
        "explanation": "The correct answer is ACL (Access Control List). An ACL is a list of permissions attached to an object. In a network context, ACLs are applied to router and firewall interfaces to control which traffic is allowed or denied based on criteria like source/destination IP address and port number. An ACL can be used to block traffic from internal networks to the data center network."
    },
    {
        "question": "A financial services company is headquartered in an area with a high occurrence of tropical storms and hurricanes. Which of the following would be MOST important when restoring services disabled by a storm?",
        "options": ["Disaster recovery plan", "Stakeholder management", "Change management", "Retention policies"],
        "answer": "Disaster recovery plan",
        "domain": "Incident Response Planning",
        "explanation": "The correct answer is Disaster recovery plan (DRP). A DRP is a documented, structured approach with instructions for responding to unplanned incidents that threaten an IT infrastructure, including natural disasters like hurricanes. It outlines the procedures to restore critical services and operations."
    },
    {
        "question": "A user in the mail room has reported an overall slowdown of his shipping management software. An anti-virus scan did not identify any issues, but a more thorough malware scan identified a kernel driver which is not part of the original operating system installation. Which of the following malware was installed on this system?",
        "options": ["Rootkit", "Logic bomb", "Bloatware", "Ransomware", "Keylogger"],
        "answer": "Rootkit",
        "domain": "Other Malware Types",
        "explanation": "The correct answer is Rootkit. Rootkits are a type of malware designed to gain administrative-level control over a computer system while remaining hidden from standard detection methods. They often modify core system files or install their own kernel-level drivers to achieve this stealth and control."
    },
    {
        "question": "A virus scanner has identified a macro virus in a word processing file attached to an email. Which of the following information could be obtained from the metadata of this file?",
        "options": ["IPS signature name and number", "Operating system version", "Date and time when the file was created", "Alert disposition"],
        "answer": "Date and time when the file was created",
        "domain": "Log Data",
        "explanation": "The correct answer is C. File metadata is data about data. For a word processing document, this typically includes information like the author, date created, date modified, and title. Information from security tools like an IPS or an antivirus alert would not be part of the file's intrinsic metadata."
    },
    {
        "question": "When a person enters a data center facility, they must check-in before they are allowed to move further into the building. People who are leaving must be formally checked-out before they are able to exit the building. Which of the following would BEST facilitate this process?",
        "options": ["Access control vestibule", "Air gap", "Pressure sensors", "Bollards"],
        "answer": "Access control vestibule",
        "domain": "Physical Security",
        "explanation": "The correct answer is Access control vestibule. Also known as a mantrap, this is a physical security control with two sets of interlocking doors, where the first set must close before the second set can open. This creates a small, secure space where a person can be authenticated (or checked in/out) before being granted further access."
    },
    {
        "question": "A security administrator has discovered an employee exfiltrating confidential company information by embedding data within image files and emailing the images to a third-party. Which of the following would best describe this activity?",
        "options": ["Digital signatures", "Steganography", "Salting", "Data masking"],
        "answer": "Steganography",
        "domain": "Obfuscation",
        "explanation": "The correct answer is Steganography. Steganography is the technique of hiding a secret message or file within an ordinary, non-secret file or message (the carrier) to avoid detection. Embedding data within image files is a classic example of steganography."
    },
    {
        "question": "A third-party has been contracted to perform a penetration test on a company's public web servers. The testing company has been provided with the external IP addresses of the servers. Which of the following would describe this scenario?",
        "options": ["Defensive", "Active reconnaissance", "Partially known environment", "Regulatory"],
        "answer": "Partially known environment",
        "domain": "Penetration Tests",
        "explanation": "The correct answer is Partially known environment. In a gray-box (partially known) penetration test, the testers are given limited information about the target environment, such as a list of IP addresses or basic network diagrams. This simulates an attack from someone with some level of insider knowledge."
    },
    {
        "question": "Which of the following would be the best way to describe the estimated number of laptops that might be stolen in a fiscal year?",
        "options": ["ALE", "SLE", "ARO", "MTTR"],
        "answer": "ARO",
        "domain": "Risk Management",
        "explanation": "The correct answer is ARO (Annualized Rate of Occurrence). The ARO is a value that represents how many times a specific threat is expected to occur in a single year. SLE is Single Loss Expectancy (cost of one event). ALE is Annual Loss Expectancy (SLE * ARO). MTTR is Mean Time to Repair."
    }
];