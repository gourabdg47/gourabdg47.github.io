---
title: Vulnerabilities & Attacks
author: gourabdg47
date: 2025-04-02 09:05:00
categories:
  - Information
  - Security +
tags:
  - reading
  - certification
render_with_liquid: true
---
I am following [Udemy Jason Dion](https://www.udemy.com/course/securityplus/learn/lecture/40324620#overview)'s course for Security +

## **Vulnerabilities & Attacks**

### **Vulnerabilities**

**Definition**: Weaknesses in hardware, software, configurations, or processes that can be exploited to compromise confidentiality, integrity, or availability (CIA triad).  
**Examples**:

- **Unpatched software**: Missing security updates (e.g., Apache Struts vulnerability in Equifax breach).
    
- **Default credentials**: IoT devices using admin/password (e.g., Mirai botnet).
    
- **Open ports/services**: Exposed RDP ports leading to ransomware attacks.
    

### **Attacks**

**Definition**: Deliberate actions by threat actors (hackers, insiders) to exploit vulnerabilities for malicious purposes.  
**Examples**:

- **Malware**: WannaCry ransomware (2017) exploiting EternalBlue vulnerability.
    
- **Phishing**: 2016 DNC email hack via spear-phishing.
    
- **DDoS**: 2016 Dyn DNS attack using IoT botnets.
    

---

## **Fixing Vulnerabilities**

1. **Hardening**:
    
    - Remove unnecessary services (e.g., disable SMBv1 to prevent WannaCry).
        
    - Use CIS Benchmarks or DISA STIGs for secure configurations.
        
2. **Patching**:
    
    - **Patch Tuesday**: Microsoft’s monthly update cycle.
        
    - **Zero-day mitigation**: Virtual patching via WAFs/IPS (e.g., ProxyLogon vulnerability).
        
3. **Baseline Configurations**:
    
    - Enforce via Group Policy (Windows) or Ansible/Puppet (Linux).
        
4. **Decommissioning**:
    
    - Legacy systems (e.g., Windows XP) lack modern security controls.
        
5. **Segmentation**:
    
    - Use VLANs or microsegmentation (VMware NSX) to isolate critical assets.
        

---

## **Bluetooth Attacks**

1. **Bluesnarfing**:
    
    - **Definition**: Unauthorized access to data (contacts, emails) via Bluetooth OBEX protocol.
        
    - **Example**: 2003–2004 attacks on Nokia 6310i devices.
        
2. **Bluejacking**:
    
    - **Definition**: Sending unsolicited messages (spam) to nearby devices.
        
    - **Example**: Spamming “Buy this product!” via Bluetooth.
        
3. **Bluebugging**:
    
    - **Definition**: Full device takeover (e.g., making calls, sending SMS).
        
    - **Example**: 2004 Siemens phones compromised via Bluetooth.
        
4. **Bluesmack**:
    
    - **Definition**: Bluetooth DoS using oversized L2CAP packets.
        
5. **Blueborne** (2017):
    
    - **Definition**: Exploits Bluetooth stack (CVE-2017-1000251) for RCE.
        
    - **Impact**: 5.3 billion devices at risk.
        

**Mitigation**:

- Disable Bluetooth discoverability.
    
- Use Bluetooth Low Energy (BLE) with secure pairing (e.g., LE Secure Connections).
    

---

## **Mobile Vulnerabilities**

1. **Sideloading**:
    
    - **Definition**: Installing apps outside official stores (e.g., APK files).
        
    - **Risk**: Pegasus spyware (2016) via malicious sideloaded apps.
        
2. **Jailbreaking/Rooting**:
    
    - **Definition**: Bypassing OS restrictions to gain root access.
        
    - **Risk**: Triada malware (2016) on rooted Android devices.
        
3. **Insecure Connections**:
    
    - **Example**: Man-in-the-Middle (MITM) attacks on public Wi-Fi (e.g., DarkHotel APT group).
        

**Mitigation**:

- **MDM Solutions**: Microsoft Intune or Jamf for policy enforcement.
    
- **Network Security**: Always use VPNs (e.g., WireGuard) on public networks.
    

---

## **OS Vulnerabilities**

1. **Unpatched Systems**:
    
    - **Example**: WannaCry (2017) exploiting EternalBlue (MS17-010).
        
2. **Zero-Days**:
    
    - **Example**: Stuxnet (2010) targeting Windows print spooler (CVE-2010-2568).
        
3. **Misconfigurations**:
    
    - **Example**: 2019 Capital One breach via misconfigured AWS S3 bucket.
        
4. **Data Exfiltration**:
    
    - **Example**: SolarWinds (2020) stealing data via compromised updates.
        
5. **Malicious Updates**:
    
    - **Example**: NotPetya (2017) disguised as a Ukrainian tax software update.
        

**Protection**:

- **Host-Based Firewall**: Block unauthorized ports (e.g., Windows Defender Firewall).
    
- **Application Allow Listing**: Only permit trusted executables (e.g., AppLocker).
    

---

## **Attack Types**

### 1. **SQL Injection (SQLi)**

- **Definition**: Injecting malicious SQL queries into input fields to manipulate databases.
    
- **Example**:
    
    - **2017 Equifax Breach**: Attackers used SQLi to access 143 million records.
        
    - **Payload**: `' OR 1=1--` to bypass authentication.
        
- **Mitigation**: Prepared statements (parameterized queries), input validation.
    

### 2. **XML Injection**

- **Definition**: Injecting malicious XML code to alter data or logic.
    
- **Example**:
    
    - Forged XML entities to crash systems (e.g., Billion Laughs attack).
        
- **Mitigation**: Disable external entity parsing (e.g., `XMLInputFactory.setProperty(XMLConstants.ACCESS_EXTERNAL_DTD, "")`).
    

### 3. **Cross-Site Scripting (XSS)**

- **Definition**: Injecting client-side scripts into web pages viewed by others.
    
- **Types**:
    
    - **Stored XSS**: Malicious script saved on a server (e.g., Samy Worm on MySpace, 2005).
        
    - **Reflected XSS**: Scripts embedded in URLs (e.g., phishing links).
        
- **Mitigation**: Output encoding, Content Security Policy (CSP).
    

### 4. **Cross-Site Request Forgery (CSRF/XSRF)**

- **Definition**: Forcing users to execute unwanted actions while authenticated.
    
- **Example**:
    
    - Changing a user’s email/password via forged requests.
        
    - **2008 Netflix CSRF**: Attackers could add DVDs to users’ queues.
        
- **Mitigation**: Anti-CSRF tokens, SameSite cookies.
    

### 5. **Buffer Overflow**

- **Definition**: Overwriting memory beyond allocated buffer space to execute arbitrary code.
    
- **Types**:
    
    - **Stack-Based**: Overwriting return addresses (e.g., Morris Worm, 1988).
        
    - **Heap-Based**: Exploiting dynamically allocated memory.
        
- **Mitigation**: ASLR, DEP, bounds checking (e.g., `strncpy` instead of `strcpy`).
    

### 6. **Race Condition**

- **Definition**: Exploiting timing gaps between checks and actions (TOCTOU).
    
- **Example**:
    
    - **Symlink races**: Replace a temporary file with a symlink to escalate privileges.
        
    - **2016 Dirty COW**: Linux kernel race condition for root access (CVE-2016-5195).
        
- **Mitigation**: File locking, atomic operations.





> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions/1) 
{: .prompt-info }