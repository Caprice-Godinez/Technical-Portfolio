# Part 2

## Objective
- Create a logical volume, mount a network file system, and create a swap partition that is automatically activated at boot. Configure directories to store temporary files.

---

## Overview / Directions
- On serverb, configured a new 1 GiB vol_home logical volume in a new 2 GiB extra_storage volume group. Used the unpartitioned /dev/vdb disk to create the partition.
- Formatted the vol_home logical volume with the XFS file-system type, and persistently mounted it on the /user-homes directory.
- On serverb, persistently mounted the /share network file system that servera exports on the /local-share directory. The servera machine exports the servera.lab.example.com:/share path.
- On serverb, created a 512 MiB swap partition on the /dev/vdc disk. Persistently mounted the swap partition.
- Created the production user group. Created the production1, production2, production3, and production4 users with the production group as their supplementary group.
- On serverb, configured the /run/volatile directory to store temporary files. If the files in this directory are not accessed for more than 30 seconds, then the system automatically deletes them. Set 0700 as the octal permissions for the directory. Used the /etc/tmpfiles.d/volatile.conf file to configure the time-based deletion of the files in the /run/volatile directory.

---

## Tools / Skills Used
- **Tools:** RHEL
- **Skills:** user and group administration; automation; NFS client configuration; filesystem formatting; logical volume management; CLI; boot persistence; swap partition creation

---

## Proof of Completion
**[Documentation](./../Documentation/Comprehensive_Review_Parts_1_2_4.PNG)**

---

## Key Takeaway
This lab reinforced advanced Linux system administration by combining **storage management, network file system integration, and automated system cleanup**. It demonstrated how to manage resources that persist across reboots while enforcing time-based cleanup policies, a crucial skill for maintaining reliable and secure multi-user systems.

**[Return to System Administrator II Overview](./../README.md)**
