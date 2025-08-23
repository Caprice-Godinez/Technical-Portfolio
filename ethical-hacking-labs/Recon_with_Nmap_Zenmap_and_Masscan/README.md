# Reconnaissance with Nmap/Zenmap and Masscan

## Objective
Toplology: OpenSUSE, Security Onion, pfSense, OWASP BWA, and Kali

Perform basic network port reconnaissance and scanning with Nmap, Zenmap, and Masscan with Kali Linux.


---

## Overview / Directions
**Nmap**

1. Disabled Docker and viewed the man pages for Nmap.

2. Conducted a general Nmap scan and a TCP connect scan on the OWASP BWA machine. Learned that Nmap scans can be noisy, so I conducted a scan that targets popular ports and a scan that identifies versions of software running on the ports.

3. Ran a default/general Nmap script to test for vulnerabilites on the OWASP BWA machine.

**Zenmap** (GUI version of Nmap)

1. Initiated Zenmap in the same Terminal window, conducted a Quick scan on the OWASP BWA machine/viewed the output, viewed the organized output from the Ports/Hosts tab, and saved the scan as a .xml file.

2. Conducted a full network scan and viewed the additional hosts that were found. Learned that the Scans tab creates a database of all manually saved scans. Exited Zenmap.

 **Masscan**

1. Viewed the man paged for Masscan and reviewed the Nmap-like features.

2. Conducted a simple scan of the LAN netork that only scans for devices with port 80 open, using a TCP SYN scan technique.

---

## Tools / Skills Used
- **Tools:** Kali Linux; Nmap; Zenmap; Masscan
- **Skills:** security auditing; network discovery; CLI; reconnaissance; enumeration 

---

## Proof of Completion
**[Documentation](./Documentation)**

---

## Key Takeaway
This lab strengthened my ability to perform network port **reconnaissance and scanning** using Nmap, Zenmap, and Masscan. By comparing tools and techniques, I learned how to conduct targeted scans, interpret results, and manage scan noise while identifying active services. These experiences enhanced my analytical thinking and methodical approach, skills that transfer directly to real-world **network assessment and security analysis/auditing**.

**[Return to Ethical Hacking Overview](./../README.md)**
