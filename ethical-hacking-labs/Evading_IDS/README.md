# Evading IDS

## Objective
Topology: OpenSUSE, Security Onion, pfSense, OWASP BWA, and Kali

- Test different methods to thwart IDS detection with network monitoring applications, Nmap scans, low MTU scan, decoy scan, and spoofed MAC scan.

---

## Overview / Directions

1. Initialized Security Onion monitoring tools (Squert, Snorby, Sguil) to observe and analyze intrusion detection alerts.

2. Ran a fragmented Nmap scan from Kali Linux and verified detection across multiple IDS interfaces.

3. Conducted a decoy scan with spoofed IPs, confirmed IDS detection of both legitimate and decoy traffic.

4. Tested a spoofed MAC scan and compared how each monitoring tool (Squert, Snorby, Sguil) reported the intrusion.

---

## Tools / Skills Used
- **Tools:** Kali Linux; Squert; Snorby, Sguil; Nmap
- **Skills:** IDS analysis; fragmented scans; decoy scans; MAC spoofing; attacker evasion tactics vs. defender visibility

---

## Proof of Completion
**[Documentation](./Documentation)**

---

## Key Takeaway
This lab strengthened my ability to **think like both attacker and defender** by testing stealthy Nmap techniques and verifying IDS detection, reinforcing skills in **network monitoring, adversary simulation, and incident response visibility**.

**[Return to Ethical Hacking Overview](./../README.md)**
