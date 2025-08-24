# Part 2

## Objective
- Manage user and group accounts, set permissions on files and directories, and manage processes.

---

## Overview / Directions
- Identifed and terminated the process that currently uses the most CPU time.
- Created the database group with a GID of 50000.
- Created the dbadmin1 user and configured it with the following requirements:
1. Added the database group as a supplementary group.
2. Set the password to redhat and forced a password change on first login.
3. Allowed the password to change after 10 days since the day of the last password change.
4. Set the password expiration to 30 days since the day of the last password change.
5. Allowed the user to use the sudo command to run any command as the superuser.
6. Configured the default umask as 007 for the dbadmin user.
- Created the /home/dbadmin1/grading/review2 directory with dbadmin1 as the owning user and the database group as the owning group.
- Configured the /home/dbadmin1/grading/review2 directory so that the database group owns any file or sub-directory that is created in this directory, irrespective of which user created the file. Configured the permissions on the directory to allow members of the database group to access the directory and to create contents in it. Ensured all other users should have read and execute permissions on the directory.
- Ensured that users are allowed to delete only files that they own from the /home/dbadmin1/grading/review2 directory.

---

## Tools / Skills Used
- **Tools:** RHEL
- **Skills:** process management; user and group administration; permission/ownership management; privilege management; access control; CLI

---

## Proof of Completion
**[Documentation](./../Documentation/Comprehensive_Review_Part_2.PNG)**

---

## Key Takeaway
This lab demonstrated advanced Linux administration skills by combining **user and group management** with fine-grained **file system permissions**. It reinforced the ability to enforce **security and operational policies, manage processes, and configure controlled access to shared directories**—key competencies for Red Hat system administration.

**[Return to System Administrator I Overview](./../README.md)**
