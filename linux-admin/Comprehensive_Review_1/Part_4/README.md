# Part 4

## Objective
- Configure and test network connectivity.

---

## Overview / Directions
- On serverb, determined the name of the Ethernet interface and its active connection profile.
- On serverb, created and activated a static connection profile for the available Ethernet interface. The static profile statically sets network settings and does not use DHCP. Configured the static profile to use the network settings in the following table:
1. IPv4 address > 172.25.250.111
2. netmask > 255.255.255.0
3. gateway > 172.25.250.254
4. DNS server > 172.25.250.254
- Set the serverb hostname to server-review4.lab4.example.com.
- On serverb, set client-review4 as the canonical hostname for the servera 172.25.250.10 IPv4 address.
- Configured the static connection profile with an additional IPv4 address of 172.25.250.211 with a netmask of 255.255.255.0. Did not remove the existing IPv4 address. Ensured that serverb responds to all addresses when the static connection is active.
- On serverb, restored the original network settings by activating the original network connection profile.

---

## Tools / Skills Used
- **Tools:** RHEL
- **Skills:** CLI; adding multiple IP addresses to a single interface; setting/verifying hostnames; managing/restoring network profiles; static network connection profile configuration; network interface/active connection identification

---

## Proof of Completion
**[Documentation](./../Documentation/Comprehensive_Review_Part_3.PNG)**

---

## Key Takeaway
This lab reinforced hands-on skills in Linux **network administration, including static IP configuration, multi-address interface management, and hostname resolution**. It emphasized the importance of precise **network setup and profile management** for maintaining **consistent connectivity and proper network identification in server environments**.

**[Return to System Administrator I Overview](./../README.md)**

