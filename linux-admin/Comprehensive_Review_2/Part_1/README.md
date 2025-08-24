# Part 1

## Objective
- Troubleshoot and repair boot problems and update the system default target. Schedule tasks to run on a repeating schedule as a normal user.

---

## Overview / Directions
- On workstation, ran the /tmp/rhcsa-break1 script. This script causes an issue with the boot process on serverb and then reboots the machine. Troubleshoot the cause and repaired the boot issue. When prompted, used redhat as the password of the root user.
- On workstation, ran the /tmp/rhcsa-break2 script. This script causes the default target to switch from the multi-user target to the graphical target on the serverb machine and then reboots the machine. On serverb, reset the default target to use the multi-user target. Ensured the default target settings persist after reboot without manual intervention. As the student user, used the sudo command for performing privileged commands. Used student as the password, when required.
- On serverb, scheduled a recurring job as the student user that executes the /home/student/backup-home.sh script hourly between 7 PM and 9 PM every day except on Saturday and Sunday. Downloaded the backup script from ht*p://materials.example.com/labs/backup-home.sh. The backup-home.sh script backs up the /home/student directory from serverb to servera in the /home/student/serverb-backup directory. Used the backup-home.sh script to schedule the recurring job as the student user. Ran the command as an executable.
- Reboot the serverb machine and waited for the boot to complete.

---

## Tools / Skills Used
- **Tools:** RHEL
- **Skills:** system recovery; task automation/scheduling; privilege management; CLI 

---

## Proof of Completion
**[Documentation](./../Documentation/Comprehensive_Review_Parts_1_2_4.PNG)**

---

## Key Takeaway
This lab reinforced my ability to **troubleshoot system-level issues, repair boot problems, and configure system targets** in RHEL environments. I also gained hands-on experience **scheduling automated backup jobs** with cron while following **principle-of-least-privilege** practices.

**[Return to System Administrator II Overview](./../README.md)**
