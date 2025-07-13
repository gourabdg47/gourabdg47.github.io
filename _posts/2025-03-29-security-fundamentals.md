---
title: Security Fundamentals
author: gourabdg47
date: 2025-03-29T19:33:00
categories:
  - Information
  - Security +
tags:
  - reading
  - certification
render_with_liquid: true
---
I am following [Udemy Jason Dion](https://www.udemy.com/course/securityplus/learn/lecture/40324620#overview)'s course for Security +

## Fundamentals of Security

- Three pillars of security : CIA (Confidentiality, Integrity & Availability)
	- **Confidentiality :** Information only accessed to those with the appropriate authorization.
		- Encryption
		- Access Controls
		- Data Masking
		- Physical Security Measures
		- Training & Awareness
	- **Integrity :** Data remains accurate and unaltered unless modification is required
		- Hashing
		- Digital Signatures
		- Checksums
		- Access Controls
		- Regular Audits
	- **Availability :** Ensure information and resources are accessible and functional when needed by authorized users 
		- Redundancy : Duplication of critical components or functions of a system with the intention of enhancing its reliability
			1. Server Redundancy
			2. Data Redundancy
			3. Network Redundancy
			4. Power Redundancy
- Non-Repudiation : Guaranteeing that a specific action or event has taken place and can not be denied by the other party involved
- AAA of Security : 
	- **Authentication :** Process of verifying the identity of a user or system
	- **Authorization :** Define what action or resources a user can access (maintain system integrity). Rules & Policies 
	- **Accounting :** Act of tracking user activity and resource usage mainly for audit and billing purpose
		- Transparency 
		- Security 
		- Accountability 
		
		* Accounting System : Audit trail, Regulatory Compliance, Forensic Analysis, Resource Optimization, User Accountability 
		* Tech can be used : 
			1. Syslog servers
			2. Network analysis tools
			3. SIEMs
- **Security Controls :** Measures put in place to protect confidentiality, integrity & availability of information system and data
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

| Control Type    | Preventive                                                       | Detective                                    | Corrective                                                | Deterrent                                                     | Compensating                                           | Directive                                                        |
| --------------- | ---------------------------------------------------------------- | -------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------- |
| **Technical**   | • Firewall rules<br>• Encryption<br>• Antivirus                  | • IDS/IPS<br>• Log monitoring<br>• SIEM      | • Patch management<br>• Automated remediation             | • Warning messages<br>• System alerts                         | • Virtual patching<br>• Redundant systems              | • Secure configuration guidelines                                |
| **Managerial**  | • Security policies<br>• Risk assessments<br>• Training programs | • Compliance reviews<br>• Audit procedures   | • Incident response plans<br>• Corrective action policies | • Disciplinary actions<br>• Sanctions                         | • Exception management<br>• Risk acceptance procedures | • Written policies<br>• Documented procedures                    |
| **Operational** | • Standard operating procedures<br>• Security awareness          | • Incident reporting<br>• Manual inspections | • Troubleshooting<br>• Manual interventions               | • Supervisory presence<br>• Access logging                    | • Temporary workaround procedures                      | • Guidance on secure practices<br>• Best practices documentation |
| **Physical**    | • Locks<br>• Biometric readers<br>• Physical barriers            | • CCTV<br>• Motion sensors<br>• Alarms       | • Fire suppression systems<br>• Repair of access points   | • Signage<br>• Security lighting<br>• Visible security guards | • Extra locks<br>• Reinforced doors                    | • Instructional signage<br>• Emergency exit guidelines           |

- **Zero Trust :** Zero Trust is not just another security buzzword—it's a paradigm shift that challenges the traditional "trust but verify" mindset. Instead of assuming that anyone inside your network is inherently trustworthy, Zero Trust flips the script: **never trust, always verify**. This means that whether a user or device is inside or outside your organization’s network, every access attempt must be authenticated, authorized, and continuously monitored.
	### *The Two Essential Planes of Zero Trust*
	Zero Trust architecture can be divided into two primary components:
	
	1. **Control Plane**
	
		Think of the control plane as the brain of your security system. It’s where all the magic happens—from defining policies to making real-time decisions on who gets access. Here’s what it does:
		
		- **Policy Management:** The control plane establishes and manages the security policies that dictate who or what is allowed to access your resources. It takes into account contextual data like user roles, device security posture, location, and time of access.
		    
		- **Identity Verification:** Every access request goes through rigorous identity checks. The control plane integrates with authentication systems (like multi-factor authentication or SSO) to confirm that users are who they claim to be.
		    
		- **Centralized Decision-Making:** When a request comes in, the control plane quickly evaluates it against the established policies. It decides whether the request should be permitted, flagged for additional scrutiny, or denied outright.
		    
		- **Dynamic Adaptation:** The control plane isn’t static. It continuously learns from ongoing traffic and can adapt policies in real time to mitigate emerging threats or respond to unusual behavior.
	    
	
	 2. **Data Plane**
	
		If the control plane is the brain, then the data plane is the nervous system that actually carries  out the actions. It’s responsible for:
		
		- **Traffic Management:** The data plane handles the flow of information. It routes data packets between users and resources, ensuring that only authenticated and authorized requests get through.
		    
		- **Policy Enforcement:** Once the control plane makes a decision, the data plane enforces it. For example, if access is denied, the data plane stops the data packets from reaching their destination.
		    
		- **Real-Time Monitoring:** It continuously monitors data flow for any signs of abnormal activity. This immediate, on-the-fly analysis is crucial for detecting breaches or potential threats as they happen.
		    
		- **Scalability:** The data plane is designed to manage large volumes of traffic efficiently, making sure that security measures don’t bottleneck your network performance.
	
* Non-repudiation : Undeniable proof in the world in digital transactions (Digital Signatures)
	* Confirming the authenticity of digital transactions 
	* Ensuring Integrity
	* Providing Accountability
	
* **Gap Analysis** : The process of evaluating the difference between an organization's current performance and its desired performance. This systematic approach helps organizations identify shortcomings in processes, systems, skills, or resources that prevent them from achieving optimal results.
## Steps of the Analysis

1. **Define the Scope**
    - Clearly identify objectives and goals
    - Establish performance metrics and benchmarks
    - Determine which aspects of the organization to evaluate
2. **Gather Data on the Current State**
    - Collect relevant metrics and performance indicators
    - Interview stakeholders and team members
    - Review existing documentation and reports
    - Observe current processes in action
3. **Analyze the Data to Identify Gaps**
    - Compare current performance against desired outcomes
    - Quantify discrepancies where possible
    - Prioritize gaps based on impact and strategic importance
    - Identify root causes of performance shortfalls
4. **Develop a Plan to Bridge the Gap**
    - Create specific, actionable strategies to address each gap
    - Assign responsibilities and allocate resources
    - Establish realistic timelines for implementation
    - Define success metrics to measure progress

## Types of Gap Analysis

### Technical Gap Analysis

Focuses on evaluating technological capabilities, systems, infrastructure, and technical skills within an organization. This analysis identifies where technical capabilities fall short of requirements or industry standards.

### Business Gap Analysis

Examines broader organizational elements including business processes, market positioning, customer service, and operational efficiency. This analysis helps align business operations with strategic objectives.

## POA&M (Plan of Action & Milestones)

A POA&M is a structured document that outlines specific measures to address each identified vulnerability or gap. Key components include:

- Detailed description of each gap or vulnerability
- Specific remediation tasks and action items
- Resource allocation (budget, personnel, tools)
- Clearly defined timelines for completion
- Assignment of responsibility for each task
- Methods for tracking progress and measuring success
- Regular review and update processes

The POA&M serves as both a roadmap for implementation and an accountability tool to ensure that remediation efforts stay on track and achieve their intended outcomes.


> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions/1) 
{: .prompt-info }