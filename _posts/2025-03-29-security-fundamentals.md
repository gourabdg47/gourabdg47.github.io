---
title: Security Fundamentals
author: gourabdg47
date: 2025-03-29T19:33:00
categories:
  - Information
  - Security +
tags:
  - writing
  - reading
render_with_liquid: true
---
I am following [Udemy Jason Dion](https://www.udemy.com/course/securityplus/learn/lecture/40324620#overview)'s course for Security +

## Fundamentals of Security

- Three pillars of security : CIA (Confidentiality, Integrity & Availability)
	- Confidentiality : Information only accessed to those with the appropriate authorization.
		- Encryption
		- Access Controls
		- Data Masking
		- Physical Security Measures
		- Training & Awareness
	- Integrity : Data remains accurate and unaltered unless modification is required
		- Hashing
		- Digital Signatures
		- Checksums
		- Access Controls
		- Regular Audits
	- Availability : Ensure information and resources are accessible and functional when needed by authorized users 
		- Redundancy : Duplication of critical components or functions of a system with the intention of enhancing its reliability
			1. Server Redundancy
			2. Data Redundancy
			3. Network Redundancy
			4. Power Redundancy
- Non-Repudiation : Guaranteeing that a specific action or event has taken place and can not be denied by the other party involved
- AAA of Security : 
	- Authentication : Process of verifying the identity of a user or system
	- Authorization : Define what action or resources a user can access (maintain system integrity). Rules & Policies 
	- Accounting : Act of tracking user activity and resource usage mainly for audit and billing purpose
		- Transparency 
		- Security 
		- Accountability 
		
		* Accounting System : Audit trail, Regulatory Compliance, Forensic Analysis, Resource Optimization, User Accountability 
		* Tech can be used : 
			1. Syslog servers
			2. Network analysis tools
			3. SIEMs
- Security Controls : Measures put in place to protect confidentiality, integrity & availability of information system and data
	- Security Categories : 
		1. Technical
		2. Managerial
		3. Operational
		4. Physical
	- Security Types : 
		1. Preventive 
		2. Detective
		3. Compensating
		4. Deterrent
		5. Corrective
		6. Directive
## Security Controls Matrix

|Control Type|Preventive|Detective|Corrective|Deterrent|Compensating|Directive|
|---|---|---|---|---|---|---|
|**Technical**|• Firewall rules<br>• Encryption<br>• Antivirus|• IDS/IPS<br>• Log monitoring<br>• SIEM|• Patch management<br>• Automated remediation|• Warning messages<br>• System alerts|• Virtual patching<br>• Redundant systems|• Secure configuration guidelines|
|**Managerial**|• Security policies<br>• Risk assessments<br>• Training programs|• Compliance reviews<br>• Audit procedures|• Incident response plans<br>• Corrective action policies|• Disciplinary actions<br>• Sanctions|• Exception management<br>• Risk acceptance procedures|• Written policies<br>• Documented procedures|
|**Operational**|• Standard operating procedures<br>• Security awareness|• Incident reporting<br>• Manual inspections|• Troubleshooting<br>• Manual interventions|• Supervisory presence<br>• Access logging|• Temporary workaround procedures|• Guidance on secure practices<br>• Best practices documentation|
|**Physical**|• Locks<br>• Biometric readers<br>• Physical barriers|• CCTV<br>• Motion sensors<br>• Alarms|• Fire suppression systems<br>• Repair of access points|• Signage<br>• Security lighting<br>• Visible security guards|• Extra locks<br>• Reinforced doors|• Instructional signage<br>• Emergency exit guidelines|

- Zero Trust : Security model that operates on the principal that no one, whether inside, or outside the organization, should be trusted by default 
	- Control plane
	- Data plane
* Non-repudiation : Undeniable proof in the world in digital transactions (Digital Signatures)
	* Confirming the authenticity of digital transactions 
	* Ensuring Integrity
	* Providing Accountability


> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions) 
{: .prompt-info }