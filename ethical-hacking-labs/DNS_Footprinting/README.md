# DNS Footprinting

## Objective
Topology: OpenSuse, pfSense, and Kali

- Footprinting with nslookup
- Compare/contrast nslookup with dig

---

## Overview / Directions
**Kali Linux**
1. Explored the man pages for nslookup, initiated nslookup interactive mode, and viewed the default listed server (pfSense firewall).

2. Changed the default server to the DNS server, conducted domain lookup, explored common DNS record types/configured domain to nameserver, and verified configured domain (if doing this with a public domain, the server would typically return the nameserver different than the server you are using for lookups, unless that DNS server is hosting that domain).

3. Viewed the 'a' record for the OpenSuse host and mx, any, and axfr records for the domain. Learned that the DNS server is configured to not respond to all request types (mx), 'any' does not return everything from a zone on newer DNS servers/does not list all hosts or 'a' records, and tested access to axfr (transfer) records to see everything on the domain (typically configured to deny access).

**OpenSuse** (preconfigured/allowed to pull transfer records)

1. Launched console terminal, initiated nslookup, accessed axfr (transfer) records, viewed every record on the domain (a, soa, cname, mx, and ns), and exited the nslookup utility. 

2. Utilized dig to input the nslookup equivalent of a nameserver.

---

## Tools / Skills Used
- **Tools:** Kali Linux; OpenSUSE; pfSense; nslookup; dig
- **Skills:** nslookup; dig; CLI; DNS querying; DNS server configuration

---

## Proof of Completion
**[Documentation](./Documents)**

---

## Key Takeaway
This lab reinforced my ability to **analyze and interpret DNS responses** while understanding the limitations and behavior of different servers. By systematically exploring record types and testing zone transfers, I strengthened my **attention to detail and methodical problem-solving** skills. These skills transfer to real-world scenarios where careful reconnaissance and tool selection are essential in **ethical hacking and security assessments**.

**[Return to Ethical Hacking Overview](./../README.md)**
