---
title: Email fundamentals
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
### Email Fundamentals

To effectively analyze phishing attempts, a deep understanding of email fundamentals is absolutely critical. Phishing attacks inherently exploit the underlying mechanisms and trust models of email communication. By dissecting the various components and protocols, an analyst can uncover clues about the attacker's identity, methods, and intent.

### 1. Email Message Structure

An email message, at its core, consists of two main parts:

- **Headers:** These contain metadata about the email, including sender, recipient, subject, timestamps, mail servers involved in routing, and authentication results. Headers are crucial for phishing analysis.
- **Body:** This is the actual content of the email, which can be plain text, HTML (rich text), or a combination. The body is where the social engineering aspect of phishing primarily resides, containing malicious links, attachments, or deceptive narratives.

### 2. Key Email Headers for Phishing Analysis

Understanding and meticulously examining email headers is often the first and most vital step in phishing analysis.

- **`From:` Header:** This is what the user _sees_ as the sender. It's easily spoofed. Attackers manipulate this to impersonate legitimate senders.
    
    - **Phishing relevance:** Always cross-reference this with technical headers to determine the _actual_ sender.
        
- **`Reply-To:` Header:** Specifies the address to which replies should be sent. Attackers might use this to direct replies to an address they control, even if the `From:` header is spoofed.
    
    - **Phishing relevance:** Check if this differs suspiciously from the `From:` address.
        
- **`To:`, `Cc:`, `Bcc:` Headers:** Indicate the primary recipients, carbon copy recipients, and blind carbon copy recipients respectively.8 `Bcc:` recipients are not visible to others.
    
    - **Phishing relevance:** Look for suspicious or numerous recipients, or if your address is the only one in `To:` for a broad announcement, which might indicate a targeted attack. If your address is in `Bcc:`, it's common for spam, but can also be used in mass phishing campaigns.
        
- **`Subject:` Header:** The topic of the email.
    
    - **Phishing relevance:** Often crafted to create urgency, fear, or curiosity (e.g., "Account Suspended," "Invoice Payment Due," "Password Reset Required," "Urgent Delivery Information").
        
- **`Date:` Header:** The date and time the email was sent.
    
    - **Phishing relevance:** Look for emails sent at unusual times for the supposed sender (e.g., an internal company email sent at 3 AM).
        
- **`Received:` Headers:** These are perhaps the _most important_ for tracing an email's path. Each `Received` header is added by a mail server as it processes the email, showing where it came _from_ and where it's going _to_. They are listed in reverse chronological order (the top `Received` header is the last server to handle the email before it reached your inbox).
    
    - **Phishing relevance:**
        
        - **Trace the path:** Identify the originating server (the bottom-most `Received` header).14 Does it match the legitimate sender's domain?
            
        - **IP addresses:** Extract IP addresses from `Received` headers and perform WHOIS lookups to identify the associated organization or region. Unexpected IP addresses (e.g., from a known spamming region) are red flags.
            
        - **Server names:** Look for legitimate server names versus generic or suspicious ones.
            
- **`Message-ID:` Header:** A unique identifier assigned to the email by the sending server.
    
    - **Phishing relevance:** Useful for tracking and correlating emails in logs, though less directly indicative of phishing by itself.
        
- **`MIME-Version:` Header:** Indicates the MIME (Multipurpose Internet Mail Extensions) version used.
    
- **`Content-Type:` Header:** Specifies the type of content in the body (e.g., `text/plain`, `text/html`).
    
    - **Phishing relevance:** HTML content allows for embedded links, images, and other styling that can be used for deception. Look for encoded content (`base64`) that might hide malicious code.
        
- **`User-Agent:` Header (less common for direct analysis):** Sometimes indicates the email client used by the sender.
    
    - **Phishing relevance:** Less direct, but inconsistencies could be a minor indicator.
        
### 3. Email Authentication Protocols

These protocols help verify the legitimacy of an email sender and prevent spoofing. Their presence and results in email headers are crucial for phishing analysis.

- **Sender Policy Framework (SPF):**
    
    - **Purpose:** Allows a domain owner to specify which mail servers are authorized to send email on behalf of their domain. This is done via a DNS TXT record.
    - **How it works:** Receiving mail servers check the SPF record of the `Return-Path` (also known as `Mail From` or `Envelope From`) domain against the IP address of the sending server.
        
    - **Phishing relevance:**
        
        - **`SPF=fail` or `softfail`:** A strong indicator of spoofing, meaning the email came from an unauthorized server.
        - **`SPF=pass`:** Means the sender's IP is authorized for the `Return-Path` domain. _However_, attackers can still register look-alike domains and pass SPF for those domains. SPF only protects the `Return-Path` domain, not necessarily the `From:` header.
            
- **DomainKeys Identified Mail (DKIM):**
    
    - **Purpose:** Allows the sender to digitally sign emails, verifying that the email content hasn't been tampered with in transit and that the sender is authorized to use the domain in the signature. This involves public/private key cryptography.
    - **How it works:** The sending server signs parts of the email (headers and body) with a private key. The receiving server uses the public key (published in the sender's DNS) to verify the signature.
    - **Phishing relevance:**
        
        - **`DKIM=fail`:** Indicates tampering or an unauthorized sender.
        - **`DKIM=pass`:** Means the signature is valid. Again, attackers can use their own domains with valid DKIM or compromise legitimate accounts to send signed emails.
            
- **Domain-based Message Authentication, Reporting & Conformance (DMARC):**
    
    - **Purpose:** Builds on SPF and DKIM by allowing domain owners to specify policy for how receiving servers should handle emails that fail SPF or DKIM checks, and to receive reports on email authentication failures. DMARC aligns the `From:` header domain with the domains checked by SPF and DKIM.
    - **How it works:** A DMARC policy (published in DNS) instructs receiving servers whether to quarantine, reject, or do nothing (monitor) with emails that fail authentication.
    - **Phishing relevance:**
        
        - **`DMARC=fail`:** A strong indicator of a phishing attempt, especially if the policy is "reject" or "quarantine." This directly targets the spoofing of the visible `From:` address.
        - **`DMARC=pass`:** Means the email passed authentication and the `From:` domain is aligned. However, sophisticated phishing can still pass DMARC if the attacker compromises a legitimate account or uses a carefully crafted look-alike domain.
            
### 4. Email Body Analysis

Once headers are examined, the email body provides the context for social engineering and often the direct attack vectors.

- **Text and Language:**
    
    - **Urgency/Threats:** "Immediate action required," "Account will be closed," "Payment overdue."
    - **Grammar/Spelling Errors:** Often a tell-tale sign of non-native English speakers or carelessness by attackers.
    - **Generic Greetings:** "Dear Customer" instead of your name, indicating a mass phishing campaign.
    - **Unusual Requests:** Asking for sensitive information, financial transfers, or password resets outside normal procedures.
        
- **Links (URLs):**
    
    - **Hover and Inspect:** _Always_ hover over links without clicking to see the actual destination URL.
    - **Discrepancies:** The displayed text of the link may differ from the actual URL.
    - **Malicious Domains:** Look for misspellings of legitimate domains (typosquatting), unusual subdomains, or completely unrelated domains.
    - **URL Shorteners:** While legitimate, these can obscure malicious destinations. Be extremely wary.
    - **HTTPS:** While desirable, HTTPS does _not_ guarantee legitimacy; attackers can obtain SSL certificates for their malicious sites.
        
- **Attachments:**
    
    - **Suspicious File Types:** `.exe`, `.scr`, `.zip` (containing executables), `.js`, `.vbs`, `.docm`, `.xlsm` (macro-enabled documents).
    - **Unsolicited Attachments:** Especially from unknown senders or with generic names (e.g., "Invoice.zip," "OrderConfirmation.doc").
    - **Macros:** Documents prompting users to "Enable Content" or "Enable Macros" are highly suspicious.
        
- **Images and Logos:**
    
    - **Embedded vs. Linked:** Attackers may link to images hosted on legitimate sites to appear authentic, but inspect the source of these images.
    - **Pixelation/Low Quality:** May indicate a copied logo.
        
### 5. Email Protocols (Underlying Mechanisms)

###### SMTP (Simple Mail Transfer Protocol) 

**SMTP** is the workhorse of email **sending** and **relaying**. Think of it as the postal service for email. When you hit "send" on an email, your email client (like Outlook or Gmail in your browser) doesn't deliver it directly to the recipient's inbox. Instead, it hands the email off to your mail server using SMTP.

Your mail server then uses SMTP to communicate with the recipient's mail server. This process involves a series of "handshakes" where the sending server identifies itself, the recipient server acknowledges the request, and the email content is transferred. Each server involved in this relay process adds a "Received" header to the email, essentially stamping it with information about its journey. These headers are crucial for tracing the path of an email and are often analyzed in cases of spam or phishing to identify the origin.

###### Ports for SMTP:

- **Port 25 (SMTP):** This is the **original, standard port** for SMTP. It's primarily used for **server-to-server email relay**. However, due to its historical use and susceptibility to spam, many Internet Service Providers (ISPs) block or restrict outbound connections on port 25 for residential users.
    
- **Port 587 (Submission):** This is the **recommended port** for **client-to-server email submission**. When your email client sends an email to your mail server, it typically uses port 587. It often requires **authentication** (your username and password) to prevent unauthorized relaying.
    
- **Port 465 (SMTPS):** This port was historically used for SMTP over SSL/TLS (Secure Sockets Layer/Transport Layer Security), providing encrypted communication. While still supported by some servers, **Port 587 with STARTTLS** (a command that upgrades an insecure connection to a secure one) is now the preferred method for secure client-to-server communication.

###### POP3 (Post Office Protocol 3) 

**POP3** is a protocol used by email clients to **retrieve emails from a mail server**. Its name, "Post Office Protocol," gives a good analogy: it's like going to the post office to pick up your mail.

The key characteristic of POP3 is that it typically **downloads emails from the server to your local device and then deletes them from the server**. This means that once you've downloaded an email to your computer, it might not be accessible from other devices unless you've configured your client to leave a copy on the server (an option many clients provide). POP3 is simpler and generally requires less storage on the server since emails are moved to the client.

###### Ports for POP3:

- **Port 110 (POP3):** This is the **standard, unencrypted port** for POP3.
- **Port 995 (POP3S):** This port is used for **POP3 over SSL/TLS**, providing an encrypted connection for retrieving your emails.

###### IMAP (Internet Message Access Protocol) 

**IMAP** is another protocol used by email clients to **retrieve emails from a mail server**. Unlike POP3, IMAP is designed for **synchronization** and **keeping emails on the server**. Think of IMAP as accessing a shared filing cabinet.

With IMAP, your email client essentially acts as a "window" to your mailbox on the server. When you read an email, move it to a different folder, or delete it, those changes are reflected on the server. This means your email experience is **consistent across all your devices** (computer, phone, tablet) because all devices are accessing the same central copy of your emails on the server. IMAP is more feature-rich than POP3, allowing for server-side folders, flagging, and searching.

###### Ports for IMAP:

- **Port 143 (IMAP):** This is the **standard, unencrypted port** for IMAP.
- **Port 993 (IMAPS):** This port is used for **IMAP over SSL/TLS**, providing an encrypted connection for accessing your emails.
    
### 6. Tools and Techniques for Phishing Analysis

- **"Show Original" / "View Source":** Most email clients offer an option to view the raw email, including all headers. This is your primary tool.
- **Online Header Analyzers:** Websites like MXToolbox's Email Header Analyzer, Google Admin Toolbox Message header, or mail-tester.com allow you to paste raw headers and get a parsed, human-readable output, often with SPF/DKIM/DMARC results.
- **WHOIS Lookup:** To find information about IP addresses and domain registrations.
- **URL Scanners:** Services like VirusTotal, URLScan.io, or Google Safe Browse can analyze suspicious URLs for malicious content.
- **Sandbox Environments:** For safely opening suspicious attachments or visiting malicious links without infecting your own system.
- **OSINT (Open Source Intelligence):** Searching for attacker email addresses, domain names, or IP addresses online can reveal if they are known malicious entities.
    
By meticulously applying these fundamental email principles and analysis techniques, you can significantly enhance your ability to identify, understand, and defend against phishing attacks.



> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions/1) 
{: .prompt-info }
