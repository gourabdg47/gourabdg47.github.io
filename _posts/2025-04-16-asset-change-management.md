---
title: Asset & Change management
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

### **Asset Management**

**Cybersecurity asset management** (CSAM) is the process created to *continuously discover*, *inventory*, *monitor*, *manage*, and *track* an organization’s assets to determine what those assets do and identify gaps in its cybersecurity protections.  
A systematic approach to ***developing***, ***operating***, ***maintaining***, and ***retiring*** assets cost‑effectively while aligning with security goals is critical to reducing risk and ensuring compliance with industry frameworks

1. **Assignment**
    
    - Assigning **ownership** (e.g., an IT manager) and **responsibilities** (e.g., updates, patching) to ensure accountability.
    - Example: Tagging a server to a specific team for maintenance.
        
2. **Accounting**
    
    - Maintaining a **comprehensive inventory** (hardware, software, licenses) and tracking asset value for budgeting and compliance.
    - Tools: CMDB (Configuration Management Database).
        
3. **Monitoring**
    
    - Continuously tracking asset **performance, health, and security status** (e.g., vulnerability scans, uptime metrics).
        
4. **Asset Tracking**
    
    - Using tools like **RFID tags, barcodes, or GPS** to log physical/virtual asset locations and movements.

---

### **Change Management**

A structured process to **transition systems, teams, or workflows** securely from current to future states.

- **Key Steps**:
    
    1. Request submission (e.g., firewall rule change).
    2. **Risk assessment & approval** (CAB – Change Advisory Board).
    3. Testing in a sandboxed environment.
    4. Documentation and post-implementation review.
        
- **Security Impact**: Prevents outages, misconfigurations, and vulnerabilities (e.g., unapproved changes leading to breaches).
    
---

### **Acquisition & Procurement**

Structured process to **source and implement secure technologies/services** while managing third-party risks.

- **Phases**:
    
    1. **Needs Assessment**: Define requirements (e.g., encryption capabilities).
    2. **Vendor Vetting**: Evaluate security practices (e.g., SOC 2 reports, pen-test results).
    3. **Contracts**: Include SLAs (Service-Level Agreements) and data protection clauses.
    4. **Deployment**: Integrate with existing systems securely.
        
---

### **Mobile Asset Deployment**

Strategies to manage mobile devices while balancing productivity and security:

1. **BYOD (Bring Your Own Device)**
    
    - Employees use **personal devices** for work.
    - **Pros**: Cost savings. **Cons**: Data leakage risks (enforce MDM policies).
        
2. **COPE (Corporate-Owned, Personally Enabled)**
    
    - **Company-owned devices** allowing limited personal use.
    - Balances control with flexibility (e.g., pre-installed security apps).
        
3. **CYOD (Choose Your Own Device)**
    
    - Employees select from a **pre-approved list** of devices.
    - Reduces support complexity while maintaining security standards.
        
---

### **Mobile Device Management (MDM)**

MDM software enables IT administrators to control, secure, and enforce policies on smartphones, tablets, and other endpoints—critical for BYOD and CYOD environments . 
*Key features include*  :

- **Remote Wipe**: Erase corporate data on lost or stolen devices.
- **App Whitelisting/Blacklisting**: Control which applications can be installed.
- **Geolocation Tracking**: Monitor device location for compliance and recovery.
- **Encryption Enforcement**: Ensure data‑at‑rest encryption on devices.
- **Containerization**: Isolate corporate data from personal apps in BYOD scenarios

---

### **Asset Disposal & Decommissioning**

Securely retiring assets to prevent data breaches:

- **Sanitization**:
	Media sanitization processes—such as data wiping, degaussing, and crypto‑shredding—render data irrecoverable based on the confidentiality requirements of the informationS
        
- **Destruction**:
	Physical destruction methods—shredding, incineration, or drilling—provide final assurance that media cannot be reused
        
- **Certification**:
    Obtain a Certificate of Destruction or Sanitization, documenting methods used and providing audit evidence as outlined in NIST SP 800‑88
        
- **Data Retention**:
    Follow legal and regulatory requirements—such as GDPR and HIPAA—to determine retention periods and ensure that data is kept or deleted appropriately. For example, HIPAA mandates retaining patient records for at least six years

---

> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions/1) 
{: .prompt-info }