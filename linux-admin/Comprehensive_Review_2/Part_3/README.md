# Part 3

## Objective
- Configure SSH key-based authentication, change firewall settings, adjust the SELinux mode and an SELinux Boolean, and troubleshoot SELinux issues.

---

## Overview / Directions
- On serverb, generated an SSH key pair for the student user. Did not protect the private key with a passphrase.
- Configured the student user on servera to accept login authentication with the SSH key pair that I generated on the serverb machine. Ensured the student user on serverb must be able to log in to servera via SSH without entering a password.
- On servera, checkd the /user-homes/production5 directory permissions. Then, configured SELinux to run in the permissive mode by default.
- On serverb, verified that the /localhome directory does not exist. Then, configured the production5 user's home directory to mount the /user-homes/production5 network file system. The servera.lab.example.com machine exports the file system as the servera.lab.example.com:/user-homes/production5 NFS share. Used the autofs service to mount the network share. Verified that the autofs service creates the /localhome/production5 directory with the same permissions as on servera.
- On serverb, adjusted the appropriate SELinux Boolean so that the production5 user may use the NFS-mounted home directory after authenticating with an SSH key. If required, used redhat as the password of the production5 user.
- On serverb, adjusted the firewall settings to reject all connection requests from the servera machine. Used the servera IPv4 address (172.25.250.10) to configure the firewall rule.
- On serverb, investigated and fixed the issue with the failing Apache web service, which listens on port 30080/TCP for connections. Adjusted the firewall settings appropriately so that the port 30080/TCP is open for incoming connections.

---

## Tools / Skills Used
- **Tools:** RHEL
- **Skills:** SSH key-based authentication; firewall management; SElinux administration; NFS configuration; web service troubleshooting; directory management; CLI

---

## Proof of Completion
**[Documentation](./../Documentation/Comprehensive_Review_Part_3.JPG)**

---

## Key Takeaway
This lab strengthened my ability to manage **secure remote access, firewall rules, and SELinux policies while troubleshooting** real-world service issues. It demonstrated how to **balance security and functionality**—configuring SELinux and firewalls without breaking legitimate workflows, ensuring services like SSH, NFS, and Apache remain both secure and operational.

**[Return to System Administrator II Overview](./../README.md)**
