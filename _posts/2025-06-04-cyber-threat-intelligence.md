---
title: Cyber Threat Intelligence
author: gourabdg47
date: 25-06-04 02:00:00 +0500
categories:
  - Information
  - Cybersecurity
tags:
  - reading
  - cybersecurity
render_with_liquid: false
---

## Cyber Threat Intelligence

Cyber Threat Intelligence (CTI) can be defined as evidence-based knowledge about adversaries, including their indicators, tactics, motivations, and actionable advice against them. These can be utilized to protect critical assets and inform cyber security teams and management business decisions.

It would be typical to use the terms “data”, “information”, and “intelligence” interchangeably. However, let us distinguish between them to understand better how CTI comes into play.!

**Data:** Discrete indicators associated with an adversary, such as IP addresses, URLs or hashes.
**Information:** A combination of multiple data points that answer questions such as “How many times have employees accessed tryhackme.com within the month?”
**Intelligence:** The correlation of data and information to extract patterns of actions based on contextual analysis.

The primary goal of CTI is to understand the relationship between your operational environment and your adversary and how to defend your environment against any attacks. You would seek this goal by developing your cyber threat context by trying to answer the following questions:  

- Who’s attacking you?
- What are their motivations?
- What are their capabilities?
- What artefacts and indicators of compromise (IOCs) should you look out for?

With these questions, threat intelligence would be gathered from different sources under the following categories:

- **Internal:**
    
    - Corporate security events such as vulnerability assessments and incident response reports.
    - Cyber awareness training reports.
    - System logs and events.
    
- **Community:**
    - Open web forums.
    - Dark web communities for cybercriminals.
    
- **External**
    - Threat intel feeds (Commercial & Open-source)
    - Online marketplaces.
    - Public sources include government data, publications, social media, financial and industrial assessments.

### Threat Intelligence Classifications!
Threat Intel is geared towards understanding the relationship between your operational environment and your adversary. With this in mind, we can break down threat intel into the following classifications:

- **Strategic Intel:** High-level intel that looks into the organization’s threat landscape and maps out the risk areas based on trends, patterns and emerging threats that may impact business decisions.
    
- **Technical Intel:** Looks into evidence and artefacts of attack used by an adversary. Incident Response teams can use this intel to create a baseline attack surface to analyze and develop defense mechanisms.
    
- **Tactical Intel:** Assesses adversaries’ tactics, techniques, and procedures (TTPs). This intel can strengthen security controls and address vulnerabilities through real-time investigations.
    
- **Operational Intel:** Looks into an adversary’s specific motives and intent to perform an attack. Security teams may use this intel to understand the critical assets available in the organization (people, processes and technologies) that may be targeted.

### CTI Lifecycle

Threat intel is obtained from a data-churning process that transforms raw data into contextualised and action-oriented insights geared towards triaging security incidents. The transformational process follows a six-phase cycle:  

##### Direction

Every threat intel program requires to have objectives and goals defined, involving identifying the following parameters:

- Information assets and business processes that require defending.
- Potential impact to be experienced on losing the assets or through process interruptions.
- Sources of data and intel to be used towards protection.
- Tools and resources that are required to defend the assets.

This phase also allows security analysts to pose questions related to investigating incidents.
##### Collection

Once objectives have been defined, security analysts will gather the required data to address them. Analysts will do this by using commercial, private and open-source resources available. Due to the volume of data analysts usually face, it is recommended to automate this phase to provide time for triaging incidents.

##### Processing

Raw logs, vulnerability information, malware and network traffic usually come in different formats and may be disconnected when used to investigate an incident. This phase ensures that the data is extracted, sorted, organised, correlated with appropriate tags and presented visually in a usable and understandable format to the analysts. SIEMs are valuable tools for achieving this and allow quick parsing of data.

##### Analysis

Once the information aggregation is complete, security analysts must derive insights. Decisions to be made may involve:

- Investigating a potential threat through uncovering indicators and attack patterns.
- Defining an action plan to avert an attack and defend the infrastructure.
- Strengthening security controls or justifying investment for additional resources.

##### Dissemination

Different organizational stakeholders will consume the intelligence in varying languages and formats. For example, C-suite members will require a concise report covering trends in adversary activities, financial implications and strategic recommendations. At the same time, analysts will more likely inform the technical team about the threat IOCs, adversary TTPs and tactical action plans.

##### Feedback

The final phase covers the most crucial part, as analysts rely on the responses provided by stakeholders to improve the threat intelligence process and implementation of security controls. Feedback should be regular interaction between teams to keep the lifecycle working.


### Threat Intelligence Frameworks
- The [ATT&CK framework](https://tryhackme.com/room/mitre) is a knowledge base of adversary behavior, focusing on the indicators and tactics. Security analysts can use the information to be thorough while investigating and tracking adversarial behavior.
- [The Trusted Automated eXchange of Indicator Information (TAXII)](https://oasis-open.github.io/cti-documentation/taxii/intro) defines protocols for securely exchanging threat intel to have near real-time detection, prevention and mitigation of threats. The protocol supports two sharing models:
	- Collection: Threat intel is collected and hosted by a producer upon request by users using a request-response model.
	- Channel: Threat intel is pushed to users from a central server through a publish-subscribe model.
- [Structured Threat Information Expression (STIX)](https://oasis-open.github.io/cti-documentation/stix/intro) is a language developed for the "specification, capture, characterization and communication of standardized cyber threat information". It provides defined relationships between sets of threat info such as observables, indicators, adversary TTPs, attack campaigns, and more.
- Developed by Lockheed Martin, the Cyber Kill Chain breaks down adversary actions into steps. This breakdown helps analysts and defenders identify which stage-specific activities occurred when investigating an attack. The phases defined are shown in the image below.
	1. **Reconnaissance** : Obtain information about the victim and the tactics used for the attack.
	2. **Weaponization** : Malware is engineered based on the needs and intentions of the attack.
	3. **Delivery** : Covers how the malware would be delivered to the victim's system.
	4. **Exploitation** : Breach the victim's system vulnerabilities to execute code and create scheduled jobs to establish persistence.
	5. **Installation** : Install malware and other tools to gain access to the victim's system.
	6. **Command & Control** : Remotely control the compromised system, deliver additional malware, move across valuable assets and elevate privileges.
	7. **Actions on Objectives** : Fulfil the intended goals for the attack: financial gain, corporate espionage, and data exfiltration.
- The **diamond model** looks at intrusion analysis and tracking attack groups over time. It focuses on four key areas, each representing a different point on the diamond. These are:
	1. **Adversary** : The focus here is on the threat actor behind an attack and allows analysts to identify the motive behind the attack.
	2. **Victim** : The opposite end of adversary looks at an individual, group or organization affected by an attack.
	3. **Infrastructure** : The adversaries' tools, systems, and software to conduct their attack are the main focus. Additionally, the victim's systems would be crucial to providing information about the compromise.
	4. **Capabilities** : The focus here is on the adversary's approach to reaching its goal. This looks at the means of exploitation and the TTPs implemented across the attack timeline


### Threat Intelligence Tools
1. [**Urlscan.io**](https://urlscan.io/) is a free service developed to assist in scanning and analyzing websites. It is used to automate the process of browsing and crawling through websites to record activities and interactions.
2. [Abuse.ch](https://abuse.ch/) is a research project hosted by the Institute for Cybersecurity and Engineering at the Bern University of Applied Sciences in Switzerland. It was developed to identify and track malware and botnets through several operational platforms developed under the project. These platforms are:
	- **Malware Bazaar:**  A resource for sharing malware samples.
	- **Feodo Tracker:**  A resource used to track botnet command and control (C2) infrastructure linked with Emotet, Dridex and TrickBot.
	- **SSL Blacklist:**  A resource for collecting and providing a blocklist for malicious SSL certificates and JA3/JA3s fingerprints.
	- **URL Haus:**  A resource for sharing malware distribution sites.
	- **Threat Fox:**  A resource for sharing indicators of compromise (IOCs).
3. [PhishTool](https://www.phishtool.com/) seeks to elevate the perception of phishing as a severe form of attack and provide a responsive means of email security. Through email analysis, security analysts can uncover email IOCs, prevent breaches and provide forensic reports that could be used in phishing containment and training engagements.
4. [Talos Intelligence](https://talosintelligence.com/). IT and Cybersecurity companies collect massive amounts of information that could be used for threat analysis and intelligence. Being one of those companies, Cisco assembled a large team of security practitioners called Cisco Talos to provide actionable intelligence, visibility on indicators, and protection against emerging threats through data collected from their products.

### Threat intelligence platform
- [OpenCTI](https://github.com/OpenCTI-Platform/opencti) is another open-sourced platform designed to provide organizations with the means to manage CTI through the storage, analysis, visualization and presentation of threat campaigns, malware and IOCs.
- [TheHive](https://thehive-project.org/) -  [GitHub Repo](https://github.com/TheHive-Project/TheHive). Project is a scalable, open-source and freely available Security Incident Response Platform, designed to assist security analysts and practitioners working in SOCs, CSIRTs and CERTs to track, investigate and act upon identified security incidents in a swift and collaborative manner.
- [MISP (Malware Information Sharing Platform)](https://www.misp-project.org/) is an open-source threat information platform that facilitates the collection, storage and distribution of threat intelligence and Indicators of Compromise (IOCs) related to malware, cyber attacks, financial fraud or any intelligence within a community of trusted members.
- [YARA GitHub repo here](https://github.com/virustotal/yara)  _The pattern matching Swiss knife for malware researchers (and everyone else)_ 



> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions/1) 
{: .prompt-info }
