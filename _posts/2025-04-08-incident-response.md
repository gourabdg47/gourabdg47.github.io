---
title: Incident Response
author: gourabdg47
date: 2025-04-08 13:38
categories:
  - Information
  - Security +
tags:
  - reading
  - certification
render_with_liquid: true
---
I am following [Jason Dion's Security+ course on Udemy](https://www.udemy.com/course/securityplus/learn/lecture/40324620#overview) to prepare for the CompTIA Security+ certification.

# **Incident Response**
Outlines a structured approach to  **<span style="color:rgb(0, 176, 80)">Manage</span>** and **<span style="color:rgb(0, 176, 80)">Mitigate</span>** security incidents effectively
##### Goals:
1. **Minimize Impact**
2. **Reduce response Time**
3. **Hasten (Fast)  Recovery**
	- *Incident Detection & Classification*
	- *Evidence Preservation*
	- *Communication & Reporting*
	- *Lessons Learned* 

#### Incident response process
__Incident__: Act of violating an explicit or implied security policy
###### Seven (7) Phase Model
1. **Preparation**: Policies & Procedures are written. Getting ready for future incidents
2. **Detection**: If a security incident has occurred and assessing the potential incident severity. The incident is categorized and triaged 
3. **Analysis**: The incident is thoroughly examined & evaluated. Understand the scope & impact of the incident, evaluate the nature & potential consequences. 
4. **Containment**: Limit the scope and magnitude of the incident by securing the data and minimize the impact on business operations.
5. **Eradication**: Focused on removing the malicious activity from a given system or network.
6. **Recovery**: Focused on restoring the effective system and services to there normal secure state.
	- *Restoring from known good backup*
	- *Installing security patches*
	- *Implementing configuration updates* 
7. **Post-incident activity / Lessons Learned**: Analysis the incident and the response to identify whether the procedures and systems that we had worked properly or anything else we can do better next time. 
		**Actions**: 
		*1. Root cause analysis*: Identify the source of the incident and how to prevent it in future
			**- Define/Scope the incident** 
			**- Determine the casual relationships that led to the incident** 
			**- Identify an effective solution**
			**- Implement & track the solutions**
		*2. Lessons learned process*: What went right, what went wrong & what can we do better next time.
		*3. After-action report*: Formalized report that collects information about what happened. Should have the '**Root cause analysis** & **Recommendation for improvements**'

---
#### Threat Hunting
Method for finding hidden threats not caught by regular security monitoring. This is  the act of being proactive in your defense as opposed to being reactive like you are with incident response. We are looking for threats within our network instead of waiting for them to attack us.
1. **Establish a Hypothesis**: Predicting high-impact, likely events through threat modeling and which events have the highest likelihood if there where to occur. 
	- *Who might want to harm us ?*
	- *Who might want to break into our networks ?*
	- *How might they be able to do that ?*
2. **Profiling Threat Actors and Activities**: Creating scenarios that shows how a perspective attacker might attempt an intrusion and what there objectives might be 
	- *What TTPs (**Tactics, Techniques & Procedures**) might they use ?*
	- Who wants to harm us ?
	- *Are they insider threat, a hacktivist, a criminal organization or a nation-state APT ?*

---

> 💡 **Join the discussion**:  
> For questions or collaboration opportunities, visit our [ZeroDayMindset Discussion Board](https://github.com/orgs/X3N0-G0D/discussions)
{: .prompt-info }