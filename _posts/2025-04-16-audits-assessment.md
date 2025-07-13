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

## **Audits**

_Systematic evaluations to verify adherence to security policies, regulations, and best practices._

### **1. Types of Audits**

#### **A. Internal Audits**

**Purpose & Scope**

- Provides independent assurance to management that risks are managed within the organization’s risk appetite.
- Covers IT governance, patch management, insider threats, and third-party relationships.
    

**Methodology**

1. **Planning & Risk Assessment**
    
    - Define objectives, scope, and risk-based criteria (e.g., high-value systems).
        
2. **Fieldwork**
    
    - Test controls via interviews, walkthroughs, and technical validation (e.g., patch management against NIST SP 800-40).
        
3. **Reporting**
    
    - Document findings with risk ratings (High/Medium/Low) and remediation recommendations.
        
4. **Follow-Up**
    
    - Track remediation until closure.

**Framework Alignment**

- Align with ISO 27001 Annex A (e.g., access control, operations security).
    
**Live Example – Patch Management Audit**

1. **Identify**: Review patch policy and schedule.
2. **Sample**: Select 10 critical servers.
3. **Verify**: Confirm patches applied within SLA using vulnerability scans.
4. **Interview**: Discuss deviations with system admins.
5. **Report**: Flag unpatched servers (>30 days) as High-risk.
    

---

#### **B. External Audits**

**Purpose & Types**

- Conducted by third parties (e.g., QSAs) for compliance (PCI DSS, SOC 2, HIPAA, GDPR).
    
- **[Reference: PCI DSS Audit Process](https://scytale.ai/resources/pci-dss-audit/)**
    

**Typical Process**

1. **Engagement & Scoping**: Define systems, data flows, and controls.
2. **Gap Analysis**: Identify compliance gaps.
3. **Control Testing**: Validate encryption, access logs, etc.
4. **Remediation Support**: Provide a fix roadmap.
5. **Final Report**: Issue certification (e.g., PCI DSS RoC).
    

**Live Example – PCI DSS Audit**

- **Gap Analysis**: Inventory cardholder data repositories.
- **Testing**: Verify encryption (in transit/at rest) and firewall rules.
- **Evidence**: Collect network diagrams, config files, and policies.
- **Outcome**: QSA issues Report on Compliance (RoC).
    

---

## **Identifying Security Gaps**

_Weaknesses in policies, procedures, or controls:_

1. **Policies**: Missing incident response plan for ransomware.
2. **Procedures**: Password sharing via unencrypted email.
3. **Controls**: No MFA for privileged accounts.
    
- **Real-World Example**: Equifax breach (unpatched Apache Struts).
    
---

## **Internal Processes**

- **Processes**: Patch management cycles, access reviews.
- **Controls**: Firewalls, encryption, MFA.
- **Compliance**: HIPAA, NIST CSF, SOC 2.

---

## **Penetration Testing**

_Simulating attacks to exploit vulnerabilities._

### **Types of Penetration Testing**

#### **1. Physical Penetration Testing**

- **Focus**: Locks, sensors, guards.
- **Methods**: Tailgating, RFID bypass, dumpster diving.
- **Use Case**: Data centers, corporate offices.

#### **2. Offensive Penetration Testing**

- **Focus**: Exploiting misconfigurations, weak credentials.
- **Tools**: Metasploit, Burp Suite.
- **Use Case**: Banks, tech firms.
    
#### **3. Defensive Penetration Testing**

- **Focus**: SOC detection/response.
- **Methods**: Purple teaming, SIEM monitoring.
- **Use Case**: Mature security teams.
    
#### **4. Integrated Penetration Testing**

- **Focus**: Holistic assessment (phishing + network + physical).
- **Framework**: MITRE ATT&CK.
- **Use Case**: ISO 27001/NIST compliance.

---

### **5-Phase Penetration Testing Approach**

#### **1. Reconnaissance**

- **Passive**: WHOIS, Shodan, social media.
- **Active**: Nmap (`nmap -sV 192.168.1.1`), theHarvester.

#### **2. Scanning & Vulnerability Analysis**

- **Tools**: Nessus, OpenVAS,  Nikto.
- **Example**: Detecting unpatched MS17-010 (EternalBlue).

#### **3. Exploitation**

- **Black Box Example**:
```Bash
msfconsole
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 10.0.0.5
exploit
```
    
- **Outcome**: Gain meterpreter shell → dump credentials.

#### **4. Post-Exploitation**

- **Tools**: Mimikatz, Cobalt Strike.
- **Example**: Extracting Kerberos tickets for lateral movement.
    
#### **5. Reporting**

- Prioritize fixes (e.g., patch EternalBlue, disable SMBv1).

---

### **Key Tools**

1. **Nmap**: `nmap -sS -A -T4 192.168.1.1`
2. **Metasploit**: Exploit development.
3. **Burp Suite**: SQLi/XSS testing.
4. **Wireshark**: Traffic analysis.
    

---

### **Mitigation Strategies**

- **Patching**: Update systems (e.g., EternalBlue patch).
- **Network Segmentation**: Limit lateral movement.
- **WAFs**: Block SQLi/XSS.
    

---

**Exam Tips**

- Memorize the **5 phases** (Recon → Reporting).
- Know **passive** (no interaction) vs. **active** (direct probing) recon.
- Practice Nmap flags: `-sS` (stealth), `-A` (aggressive)

---

> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions/1) 
{: .prompt-info }