# Part 3

## Objective
- Configure, secure, and use the SSH service to access a remote machine, and manage packages.

---

## Overview / Directions
- Generated SSH keys for the student user. Did not protect the private key with a passphrase. Saved the private and public keys as the /home/student/.ssh/review3_key and /home/student/.ssh/review3_key.pub files respectively.
- Configured the student user on servera to accept logins that are authenticated by the review3_key SSH key pair. Ensured the student user on serverb should not be able to log in to servera by using SSH without entering a password.
- On serverb, configured the sshd service to prevent the root user from logging in.
- On serverb, configured the sshd service to prevent users from using their passwords to log in. Verified users should still be able to authenticate logins by using an SSH key pair.
- Installed the zsh package on the serverb machine.
- Set the time zone of serverb to Asia/Kolkata.

---

## Tools / Skills Used
- **Tools:** RHEL
- **Skills:** CLI; SSH key generation; service management; package management; time zone configuration; secure SSH server configuration; key-based authentication configuration

---

## Proof of Completion
**[Documentation](./../Documentation/Comprehensive_Review_Part_3.PNG)**

---

## Key Takeaway
This lab reinforced **secure remote access practices** in Linux, emphasizing **SSH key-based authentication and hardened server configurations**. It also highlighted essential system administration tasks, including **package installation and time zone management**, critical for maintaining secure and properly configured Linux environments.

**[Return to System Administrator I Overview](./../README.md)**
