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
I am following [Udemy Jason Dion](https://www.udemy.com/course/securityplus/learn/lecture/40324620#overview)'s course for Security +

## Data Protection
The process of protecting/safeguarding important information from corruption, compromise or loss.
##### Data Classifications 
Category based on the organization's value and the sensitivity of the information if it were to be disclosed
	1. **Sensitive Data**: Any information that can result in the loss of security or loss of advantage to a company if accessed by any unauthorized person
	2. **Confidential Data**: Contains items such as trade secrets, intellectual property data and source code that affect the business if disclosed
	3. **Public Data**: Has no impact on the company if released and is often posted in an open-source environment
	4. **Sensitive Data**: Has minimal impact if released (e.g. Organization's financial data)
	5. **Restricted Data**
	6. **Private Data**: Contains data that should only be used from within an organization (e.g. Salary data) 
	7. **Critical Data**: Contains valuable information (e.g. Credit card numbers)
##### Government Data Classifications
1. **Unclassified**: Data can be released to the public under the Freedom of Information Act
2. **Sensitive but unclassified**: Data that would not hurt national security if released but could impact those whose data was being used
3. **Confidential**: Data that would seriously effect the government if unauthorized disclosers happens 
4. **Secret**: Data that could seriously damage national security if disclosed
5. **Top Secret**: Data that would damage national security if disclosed
##### Data Ownerships
This is the process of identifying the person responsible for the confidentiality, integrity, availability and privacy of the information assets 
	1. **Data Owners**: Senior executive role that has the responsibility for maintaining the confidentiality, integrity and availability of the information asset
	2. **Data Controller**: Entity that holds responsibility for deciding the purpose and methods of data storage, collection, usage and guaranteeing the legality of the processes 
	3. **Data Processors**: Group of individual hired by the data controller to help with tasks like collecting, storing or analyzing data
	4. **Data Stewards**: Focuses on the quality of the data and associated metadata 
	5. **Data Custodian**: Responsible in handling the management of the system on which data assets are stored. System admin
	6. **Data Privacy Officer**: Role that is responsible for the oversight of any kind of privacy-related data like PII, SPII, PHI
##### Data States
1. **Data at rest**: Referred to data stored in database, file systems or other storage systems.
	__Encryption Methods__: 
		1. Full Disk Encryption (FDE)
		2. Partition Encryption
		3. File Encryption
		4. Volume Encryption
		5. Database Encryption
		6. Record Encryption
2. **Data in transit**: Data is moving from one location to another e.g. E-Mail
	__Encryption Methods__: 
		1. SSL & TLS
		2. VPNs
		3. IPSec
3. **Data in use**: Refers to data in the process of being created, retrieved, updated or deleted.
	__Encryption__:
		1. Application Level
		2. Access Controls
		3. Secure Enclaves
		4. Intel Software Guard
4. **How to protect data**
	- **Disk Encryption**
	- **Communication Tunneling** 
##### Data Types
1. **Regulated Data**: PII, PHI. Information Controlled by laws, regulations or industry standards. General Data Protection Regulation (GDPR) or Health Insurance Portability and Accountability (HIPPA)
2. **Trade Secrets**: Confidential Business Information
3. **Intellectual Property (IP)**: Creation of the mind like- Inventions, Literacy & Artistic works, designs and symbols
4. **Legal Information**: Any data related to legal procedures, contracts or regulatory compliance 
5. **Financial Information**: Data related to organizations financial transactions, suck as sales records, invoices, tax documents and bank statements
6. **Human & Non-human readable data**
##### Data Sovereignty
Information is subject to laws and governance structures within the nation where it is collected. General Data Protection Regulation (GDPR)

---
##### Lifecycle of the data
Lifecycle of the data should be clearly defined in policies
1. Collect
2. Retain it
3. Dispose

---
##### Securing data
1. **Geographic Restrictions**
2. **Encryption**
3. **Hashing** 
4. **Masking**
5. **Tokenization**
6. **Obfuscation**: Making data unclear or unintelligible
7. **Segmentation**: Dividing the network into separate segments or security controls 
8. **Permission restriction**: Involve defining who has access to specific data and what they do with it

---
##### Data loss prevention (DLP)
Strategy for ensuring sensitive or critical information does not leave an organization. 
Also setup up monitor the data of a system while it's in use, transit or at rest in order to detect any attempts to steal data.
- Endpoint DLP System: Software that monitors the data in use
- Network DLP System: Software or hardware placed at the parameter of the network to detect data in transit
- Storage DLP: Software Inspect the data while it's at rest on the server
- Cloud baaed DDLP system: SAAS part of cloud service and storage needs



> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions) 
{: .prompt-info }