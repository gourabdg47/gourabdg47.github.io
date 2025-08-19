---
title: Operation Shatterbox
author: gourabdg47
date: 2025-08-19 02:53:00
categories:
  - Project
  - CTF
tags:
  - writing
  - project
  - cybersecurity
render_with_liquid: true
---


# Metasploitable3 CTF: Operation Shatterbox

MISSION BRIEFING:

Welcome, operative. Your target is "Shatterbox," a server known to house critical vulnerabilities. Your mission is to infiltrate the system, escalate your privileges, and achieve total system compromise. Each completed objective is a captured flag. Track your progress below. Good luck.

## Mission 1: Initial Infiltration & Foothold

_Your first objective is to breach the outer defenses and establish a presence on the target system. Every service is a potential doorway._

- [ ] **Reconnaissance:** Map the target's digital footprint. Perform a full TCP and UDP port scan to identify all open ports and running services.
    
- [ ] **FTP Breach:** The ProFTPD service on port 21 is an old gatekeeper. Find its weakness and use a Metasploit module to gain a shell.
    
- [ ] **IRC Backdoor:** The UnrealIRCd service has a hidden backdoor. Discover and exploit it to gain a command shell.
    
- [ ] **Tomcat Takeover:** The Apache Tomcat Manager on port 8180 uses weak, default credentials. Find them, log in, and deploy a malicious WAR file to get a shell.
    
- [ ] **Jenkins CI/CD Exploit:** The Jenkins service is configured to trust anyone. Use its unauthenticated script console to execute code and get a reverse shell.
    
- [ ] **ElasticSearch RCE:** The ElasticSearch instance is outdated. Use the known Remote Code Execution (RCE) vulnerability (CVE-2014-3120) to gain a shell.
    
- [ ] **SNMP Enumeration:** The SNMP service is leaking sensitive information. Use a tool like `snmp-check` to extract everything you can, including user accounts and running processes.
    
- [ ] **SSH Brute-Force:** The `vagrant` user has a weak password. Use Hydra to crack the SSH login and gain user-level access.
    

## Mission 2: Web Exploitation & Lateral Movement

_Now that you're inside, the web applications are your new playground. Exploit them to deepen your access and uncover the secrets they hold._

- [ ] **SQL Injection:** The `payroll_app` is vulnerable to SQL injection. Use `sqlmap` to bypass authentication and dump the entire database.
    
- [ ] **Drupageddon:** The Drupal CMS is ancient and vulnerable. Unleash the "Drupageddon" (CVE-2014-3704) exploit to seize control.
    
- [ ] **Hash Cracking:** You've dumped the Drupal database. Now, extract the user password hashes and crack them with John the Ripper or Hashcat to impersonate users.
    
- [ ] **WordPress Enumeration:** The WordPress blog is a trove of information. Use `wpscan` to find vulnerable plugins, themes, and user accounts.
    
- [ ] **WordPress Plugin Pwnage:** One of the plugins you found is vulnerable. Find the public exploit and use it to get another shell on the system.
    
- [ ] **SMB File Drop:** An SMB share is misconfigured. Use credentials you've found to log in with `smbclient` and upload a webshell to the web server's root directory.
    
- [ ] **Manual FTP Exploitation:** Metasploit is too loud. Manually exploit the `mod_copy` vulnerability in ProFTPD using only `netcat` or `telnet` to prove your skill.
    
- [ ] **JMX Exploitation:** A Java Management Extensions (JMX) service is exposed. Use the corresponding Metasploit module to exploit it for a shell.
    

## Mission 3: Privilege Escalation & Dominance

_User-level access is not enough. Your final objective is to become root, the master of the machine. Find a path to ultimate power._

- [ ] **Docker Breakout:** A compromised user is in the `docker` group. Use this privilege to spawn a container and mount the host's root filesystem, giving you root access.
    
- [ ] **Automated PE Scan:** You have a user shell. Deploy a script like `LinPEAS` or `WinPEAS` to automatically discover privilege escalation vectors.
    
- [ ] **Kernel Exploit:** The system's kernel is old and vulnerable. Identify the version, find a matching local privilege escalation exploit, and run it to become root.
    
- [ ] **Firewall Pivot:** Critical services like RDP (3389) are firewalled. From an existing shell, use SSH tunneling to bypass the firewall and access a blocked internal service.
    
- [ ] **Chain Attack:** Combine your skills. Exploit a web app for a user shell, then use a local misconfiguration or kernel exploit to escalate to root in a single, fluid attack chain.
    
- [ ] **DNS Exfiltration:** The firewall is watching HTTP traffic. Exfiltrate the `/etc/shadow` file from the target to your machine using only DNS queries.
    
- [ ] **Java Deserialization (Manual):** A custom Java service is vulnerable to deserialization. Manually craft a payload with a tool like `ysoserial` to get RCE.
    

## Elite Tier: The Ghost Protocol

_True masters leave no trace and own the board. These are the final, ultimate challenges._

- [ ] **Establish Persistence:** The system will be rebooted. Ensure your access survives by creating a persistent backdoor (e.g., cron job, systemd service).
    
- [ ] **Cover Your Tracks:** You are a ghost. From your root shell, selectively erase your login and command history from the system logs (`/var/log/auth.log`, `.bash_history`).




> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions/1) 
{: .prompt-info }
