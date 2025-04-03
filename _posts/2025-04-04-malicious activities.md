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


#### Privilege Escalation Attacks


#### Replay Attacks


#### Session/Cookie/Session Key Hijacking or Sidejacking


#### Malicious Code Injection Attacks


--- 
### Indicator of Compromise (IOC)





> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions) 
{: .prompt-info }