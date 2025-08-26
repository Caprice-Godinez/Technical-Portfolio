# Part 4

## Objective
- Create rootless detached containers. Configure port mapping and persistent storage. Configure systemd for a container to manage it with systemctl commands.

---

## Overview / Directions
- On serverb, configured the podmgr user with redhat as the password and set up the appropriate tools for the podmgr user to manage the containers for this lab. Configured the registry.lab.example.com as the remote registry. Used admin as the user and redhat321 as the password to authenticate. Used the /tmp/review4/registry.conf file to configure the registry.
- The /tmp/review4/container-dev directory contains two directories with development files for the containers in this lab. Copied the two directories under the /tmp/review4/container-dev directory to the podmgr home directory. Configured the /home/podmgr/storage/database subdirectory so that I can use it as persistent storage for a
container.
- Created the production DNS-enabled container network. Used the 10.81.0.0/16 subnet and 10.81.0.1 as the gateway. Used this container network for the containers that I create in this lab.
- Created the db-app01 detached container based on the registry.lab.example.com/rhel8/mariadb-103 container image with the lowest tag number in the production network. Used the /home/podmgr/storage/database directory as persistent storage for the /var/lib/mysql/data directory of the db-app01 container. Mapped the 13306 port on the local machine to the 3306 port in the container. Used the values of the following table to set the environment variables to create the containerized database:

1. MYSQL_USER > developer

  2. MYSQL_PASSWORD > redhat
  
  3. MYSQL_DATABASE > inventory

  4. MYSQL_ROOT_PASSWORD > redhat
- Created a systemd service file to manage the db-app01 container. Configured the systemd service so that when I start the service, the systemd daemon keeps the original container. Started and enabled the container as a systemd service. Configured the db-app01 container to start at system boot.
- Copied the /home/podmgr/db-dev/inventory.sql script into the /tmp directory of the db-app01 container and executed it inside the container.
- Used the container file in the /home/podmgr/http-dev directory to create the http-app01 detached container in the production network. Ensured the container image name must be http-client with the 9.0 tag. Mapped the 8080 port on the local machine to the 8080 port in the container.
- Used the curl command to query the content of the http-app01 container. Verified that the output of the command shows the container name of the client and that the status of the database is up.
- On serverb, configured the podmgr user with redhat as the password and set up the appropriate tools for the podmgr user to manage the containers for this lab. Configured the registry.lab.example.com as the remote registry. Used admin as the user and redhat321 as the password to authenticate. Used the /tmp/review4/registry.conf file to configure the registry.


---

## Tools / Skills Used
- **Tools:** RHEL
- **Skills:** persistent storage for containerized applications; rootless detached container creation/management; host/containerized service port mapping; environment variable management; systemd integration; DNS-enabled container networks; scripts/database initialization; secure remote container registries; CLI

---

## Proof of Completion
**[Documentation](./../Documentation/Comprehensive_Review_Parts_1_2_4.PNG)**

---

## Key Takeaway
This lab strengthened my ability to deploy and manage containerized applications in a production-style environment. I gained experience in **integrating containers with persistent storage, network configurations, and systemd**, ensuring services start automatically and run securely. It highlighted **best practices** for **orchestrating multiple containers, validating service availability, and maintaining container state across reboots**.

**[Return to System Administrator II Overview](./../README.md)**

