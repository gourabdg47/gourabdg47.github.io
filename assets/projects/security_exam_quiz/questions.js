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
    }
]