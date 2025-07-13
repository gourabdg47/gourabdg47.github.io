---
title: Data Protection
author: gourabdg47
date: 2025-04-04 15:17
categories:
  - Information
  - Security +
tags:
  - reading
  - certification
render_with_liquid: true
---
I am following [Jason Dion's Security+ course on Udemy](https://www.udemy.com/course/securityplus/learn/lecture/40324620#overview) to prepare for the CompTIA Security+ certification.

## Data Protection
The process of protecting/safeguarding important information from corruption, compromise, or loss.

### Data Classifications
Category based on the organization's value and the sensitivity of the information if disclosed:
1. **Sensitive Data**: Information that could lead to security loss or competitive disadvantage if accessed by unauthorized parties
2. **Confidential Data**: Trade secrets, intellectual property, and source code that impact business operations if exposed
3. **Public Data**: Information that can be freely shared without organizational impact
4. **Restricted Data**: Requires special authorization for access
5. **Private Data**: Internal-only information (e.g., salary data)
6. **Critical Data**: High-value assets (e.g., credit card numbers)

### Government Data Classifications
1. **Unclassified**: Publicly releasable under FOIA
2. **Sensitive but Unclassified**: Non-national security data that could impact individuals
3. **Confidential**: Could cause serious government damage if leaked
4. **Secret**: Could significantly damage national security
5. **Top Secret**: Would severely compromise national security

### Data Ownership
Responsibility for information assets' confidentiality, integrity, availability, and privacy:
- **Data Owners**: Senior executives responsible for information security
- **Data Controllers**: Decide data storage/usage methods and ensure legality
- **Data Processors**: Entities handling data collection/processing
- **Data Stewards**: Ensure data quality and metadata management
- **Data Custodians**: Manage storage systems (e.g., sysadmins)
- **Data Privacy Officers**: Oversee PII, SPII, and PHI compliance

### Data States
#### Data at Rest
Stored in databases/filesystems:
- **Encryption Methods**:
  - Full Disk Encryption (FDE)
  - Partition/File/Volume Encryption
  - Database/Record Encryption

#### Data in Transit
Moving between locations (e.g., email):
- **Encryption Methods**:
  - SSL/TLS
  - VPNs
  - IPSec

#### Data in Use
Being created/processed:
- **Protection Methods**:
  - Application-level security
  - Access controls
  - Secure enclaves (e.g., Intel SGX)

### Data Types
1. **Regulated Data**: PII/PHI governed by laws (GDPR, HIPAA)
2. **Trade Secrets**: Proprietary business information
3. **Intellectual Property**: Inventions, creative works, trademarks
4. **Legal Information**: Contracts/compliance documents
5. **Financial Data**: Transactions, invoices, tax records
6. **Human/Non-human Readable**: Structured vs raw data

### Data Sovereignty
Information subject to laws of the nation where collected (e.g., GDPR requirements).

---

## Data Lifecycle
1. **Collection**
2. **Retention**
3. **Disposal**

---

## Data Security Measures
1. **Geographic Restrictions**
2. **Encryption** (AES, RSA)
3. **Hashing** (SHA-256)
4. **Masking** (Partial data redaction)
5. **Tokenization** (Data substitution)
6. **Obfuscation** (Deliberate ambiguity)
7. **Segmentation** (Network zoning)
8. **Permission Restrictions** (RBAC, ABAC)

---

## Data Loss Prevention (DLP)
Strategies to prevent sensitive data exfiltration:
- **Endpoint DLP**: Monitor data in use
- **Network DLP**: Inspect data in transit
- **Storage DLP**: Scan data at rest
- **Cloud DLP**: SaaS-based protection

---

> 💡 **Join the discussion**:  
> For questions or collaboration opportunities, visit our [ZeroDayMindset Discussion Board](https://github.com/orgs/X3N0-G0D/discussions/1)
{: .prompt-info }