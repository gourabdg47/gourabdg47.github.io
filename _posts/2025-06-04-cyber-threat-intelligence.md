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


### Threat Intelligence Tools
1. [**Urlscan.io**](https://urlscan.io/) is a free service developed to assist in scanning and analysing websites. It is used to automate the process of browsing and crawling through websites to record activities and interactions.
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



> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions) 
{: .prompt-info }
