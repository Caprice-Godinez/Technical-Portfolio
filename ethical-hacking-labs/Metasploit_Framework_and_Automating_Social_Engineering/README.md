#  Metasploit Framework and Armitage / Automating Social Engineering

## Objective
Topology: OWASP BWA, pfSense, Kali

- Utilize the Metasploit penetration testing framework and execute attacks in Armitage.
- Test a Social Engineering Toolkit (SET) to perform reconnaissance against a target. 

---

## Overview / Directions
**Metasploit/Armitage**

1. Metasploit Framework: Initialized the database, explored console commands, and reviewed available exploits/payloads. Practiced using Netcat inside Metasploit for service interaction.

2. WMAP Vulnerability Scanning: Loaded the WMAP module, added OWASP Mutillidae as a target, and ran scans to identify web application vulnerabilities.

3. Exploitation & Payloads: Configured and executed a TikiWiki CMS remote code execution exploit with a reverse PHP payload, establishing a shell session on the target.

4. Armitage (GUI for Metasploit): Used Nmap scanning to enumerate hosts, configured attacks via the graphical interface, and re-executed the TikiWiki exploit to gain shell access.

**SET**

1. Social Engineering Toolkit (SET): Launched SET on Kali Linux and configured a credential harvester attack using a cloned Google login page.

2. Configuration: Modified SET parameters (set.config) to define redirect settings and harvesting URLs.

3. Execution & Testing: From a victim machine (OpenSUSE), accessed the fake login page, entered test credentials, and confirmed successful capture of username and password.

4. Reporting: Generated and reviewed the SET report, verifying stored credential data.

---

## Tools / Skills Used
- **Tools:** Armitage; Kali Linux; SET; Nmap
- **Skills:** Metasploit; social engineering; phishing; automation; analytical thinking

---

## Proof of Completion
**[Documentation](./Documentation)**

---

## Key Takeaway
Gained hands-on experience with both **network/system exploitation (Metasploit)** and **social engineering attacks (SET)**, highlighting how technical vulnerabilities and human factors intersect in real-world security threats.

**[Return to Ethical Hacking Overview](./../README.md)**
