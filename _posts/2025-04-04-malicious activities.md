---
title: Malicious Activities
author: gourabdg47
date: 2025-04-04 12:47
categories:
  - Information
  - Security +
tags:
  - reading
  - certification
render_with_liquid: true
---
I am following [Udemy Jason Dion](https://www.udemy.com/course/securityplus/learn/lecture/40324620#overview)'s course for Security +

## Malicious Activities
Understanding cyber threats is the first step towards prevention and mitigation

#### Distributed Denial of Service Attacks (DDOS) 
An attack that attempts to make a computer or computer server's resource unavailable
###### DOS Types: 
1. **Flood Attack**: Type of DDOS which attempts to send more packets to a single server or host
	- **Ping Flood**: A server is sent with too many pings (ICMP Echo). _Preventions_: Timeout (Block) all echo requests
	- **SYN Flood**: An attacker with initiate multiple TCP sessions but never complete the three-way handshake. _Preventions_: Flood Guard, Timeout half open requests, Intrusion Prevention
2. **Permanent Denial of Service (PDOS)**: An attack which exploits a security flaw by reflashing a firmware, permanently breaking the networking device
3. **Fork Bomb**: A large number of processes are created to use up a computer's available processing power. This is not a **WORM** because this can not infect programs

##### Surviving DDOS Attacks Techniques:
1. **Blackhole/Sinkhole**: 
2. **Intrusion Prevention System**
3. **Elastic Cloud Infrastructure** (*Most Effective*): Some Providers - Cloudflare, Akamai

#### Domain Name Server (DNS) Attacks
##### Type of attacks:
1. **DNS Cache Poisoning or DNS Spoofing**: Involves corrupting the DNS cache data of a DNS resolver with false information. _Preventions_: Use **DNSSEC** to add digital signature to the organization's DNS data, Secure network configurations and firewalls to protect DNS server
2. **DNS Amplification**: The attacker overloads a target system with DNS response traffic by exploiting the DNS resolution process. _Preventions_: Add rate limit to DNS response traffic
3. **DNS Tunneling**: Uses DNS protocol over port 53 to encase non-DNS traffic, trying to evade firewall rules for C2 or data exfiltration. _Preventions_: Regular log monitoring
4. **Domain Hijacking** : Altering the original domain name's registration without the original registrant's consent. _Preventions_: Use domain registry lock
5. **DNS Zone Transfer**: The attacker mimics an authorized system to request and obtain the entire DNS zone data for a domain. 

#### Directory Traversal Attacks/Path Traversal
This is a type of injection attack that allows access to commands, files and directories, either connected to web document root directory or not.
- **File Inclusion**: Is a vulnerability which allows an attacker to either download files from an arbitrary location or upload executable or script to open a backdoor
	- **Remote**: Execute a script to inject a remote file
	- **Local**: Execute or add a file that already exist

#### Execution and Escalation Attack

##### Types of Escalation Attacks:
1. **Arbitrary Code Execution**: A vulnerability that allows the attacker to execute a code or run a module to exploit an vulnerability.
2. **Remote Code Execution**: Allows attacker to transmit code from remote host.
3. **Privilege Escalation**: When user accesses or modifies specific resources that they where not entitled to normally access.
	- **Vertical Privilege Escalation**: From normal level user to high level user.
	- **Horizontal Privilege Escalation**: From one user to another user of generally the same level.
4. **Rootkit**: A malware that modifies system files, often at the kernel level, to conceal it's presence.
	- **Kernel mode:** At Ring 0 (Most privileged), this has complete control of the system
	- **User mode:** Might have administrator level privileges, they have to be inside the registry (like *Task Scheduler*)

#### Replay Attacks
This is a type of network-based attack that involves maliciously repeating or delaying valid data transmissions. Here the attacker intercepts the data, analysis it then decides weather to retransmit it later. _prevention_: Use authentication tokens for unique authentication identification or MFA

#### Session/Cookie/Session Key Hijacking or Sidejacking
**Session Management**: A fundamental security component that enables web applications to identify users.
__Cookies__: Allows web applications to retain information about the user.
	1. **Session Cookies**: Gets deleted when browser is closed
	**2. Persistent Cookies**: Stays around for a while, gets deleted by the user manually (clear cookie) or after a given expiration date\

**Session Hijacking**: A type of spoofing attack where the host is disconnected and replaced by the attacker
**Session Prediction**: An attacker attempts to predict the session token to hijack that session.
**Cookie Poisoning**: Modifying the contents of a cookie to be sent to client's browser and exploit the vulnerabilities in an application.

#### On-path Attack
An attacker puts the workstation logically between two hosts during the communication.
	**1. ARP Poisoning** 
	**2. DNS Poisoning**
	**3. Introducing a rouge Wireless Access Point (WAP)**
	**4. Introducing a rouge hover/switch**

**Replay**: Occurs when an attacker captures a valid data which is then repeated immediately or delayed and then repeated.
**Relay**: Occurs when an attacker insert themself in between two hosts and become part of the conversation.
_Prevention_: Using encrypted communications like TLS 1.3
**SSL Striping**: Tricking the encrypted application with an HTTP instead of HTTPs connection.


--- 
### Indicator of Compromise (IOC)
Data pieces that detect potential malicious activity on a network or system. This a digital evidence that a security breach has occurred. 
###### Indications
1. Account lockouts
2. Blocked content
3. Resource consumption
4. Out-of-cycle logging
5. Missing logs
6. Concurrent session usages
7. Impossible travel
8. Resource inaccessibility
9. Article or documents on security breach




> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions/1) 
{: .prompt-info }