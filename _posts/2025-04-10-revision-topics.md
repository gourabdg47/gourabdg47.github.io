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
render_with_liquid: true
pin: "true"
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














---

> 💡 **Join the discussion**:  
> For questions or collaboration opportunities, visit our [ZeroDayMindset Discussion Board](https://github.com/orgs/X3N0-G0D/discussions)
{: .prompt-info }