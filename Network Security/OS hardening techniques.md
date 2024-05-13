# Cybersecurity Incident Report: OS Hardening
> OS hardening.

## Scenario
You are a cybersecurity analyst for yummyrecipesforme.com, a website that sells recipes and cookbooks. A disgruntled baker has decided to publish the website’s best-selling recipes for the public to access for free. 
The baker executed a brute force attack to gain access to the web host. They repeatedly entered several known default passwords for the administrative account until they correctly guessed the right one. After they obtained the login credentials, they were able to access the admin panel and change the website’s source code. They embedded a javascript function in the source code that prompted visitors to download and run a file upon visiting the website. After running the downloaded file, the customers are redirected to a fake version of the website where the seller’s recipes are now available for free.
Several hours after the attack, multiple customers emailed yummyrecipesforme’s helpdesk. They complained that the company’s website had prompted them to download a file to update their browsers. The customers claimed that, after running the file, the address of the website changed and their personal computers began running more slowly. 
In response to this incident, the website owner tries to log in to the admin panel but is unable to, so they reach out to the website hosting provider. You and other cybersecurity analysts are tasked with investigating this security event.
To address the incident, you create a sandbox environment to observe the suspicious website behavior. You run the network protocol analyzer tcpdump, then type in the URL for the website, yummyrecipesforme.com. As soon as the website loads, you are prompted to download an executable file to update your browser. You accept the download and allow the file to run. You then observe that your browser redirects you to a different URL, greatrecipesforme.com, which is designed to look like the original site. However, the recipes your company sells are now posted for free on the new website. The logs show the following process:
1. The browser requests a DNS resolution of the yummyrecipesforme.com URL
2. The DNS replies with the correct IP address
3. The browser initiates an HTTP request for the webpage
4. The browser initiates the download of the malware
5. The browser requests another DNS resolution for greatrecipesforme.com
6. The DNS server responds with the new IP address
7. The browser initiates an HTTP request to the new IP address <br>

A senior analyst confirms that the website was compromised. The analyst checks the source code for the website. They notice that javascript code had been added to prompt website visitors to download an executable file. Analysis of the downloaded file found a script that redirects the visitors’ browsers from yummyrecipesforme.com to greatrecipesforme.com. 
The cybersecurity team reports that the web server was impacted by a brute force attack. The disgruntled baker was able to guess the password easily because the admin password was still set to the default password. Additionally, there were no controls in place to prevent a brute force attack. 
Your job is to document the incident in detail, including identifying the network protocols used to establish the connection between the user and the website.  You should also recommend a security action to take to prevent brute force attacks in the future.

## DNS & HTTP Traffic Log Analysis Guide

### DNS Traffic Log Analysis
1. **Domain Resolution:** Look for DNS queries to resolve domain names. Analyze the frequency and patterns of domain resolutions to identify any unusual or malicious activity.
2. **Response Codes:** Pay attention to DNS response codes such as "NXDOMAIN" (non-existent domain) or "SERVFAIL" (server failure), which may indicate DNS-related issues or potential attacks.
3. **IP Address Mapping:** Map DNS queries to corresponding IP addresses to understand network traffic patterns and potential communication with malicious domains.
4. **Time Stamps:** Note the timing of DNS queries to identify any spikes in activity, which could indicate coordinated attacks or network congestion.

### HTTP Traffic Log Analysis
1. **HTTP Methods:** Identify HTTP methods used in requests (e.g., GET, POST) to understand the nature of client-server interactions and potential security risks.
2. **Status Codes:** Analyze HTTP status codes (e.g., 200 OK, 404 Not Found) to assess server responses and detect anomalies such as failed requests or server errors.
3. **URL Paths:** Examine URL paths and parameters to identify specific resources accessed by clients and potential vulnerabilities targeted by attackers.
4. **User-Agent Strings:** Evaluate user-agent strings to identify different types of clients accessing the server and detect suspicious or unauthorized user agents.
5. **Referrer URLs:** Review referrer URLs to track the origin of HTTP requests and identify potential sources of malicious traffic or unauthorized access attempts.

## How to read DNS & HTTP Traffic log (Modified version, cut short, just for example)

| No | Description |
|---|---|
| 1 | **14:18:32.192571 IP your.machine.52444 > dns.google.domain: 35084+ A? yummyrecipesforme.com. (24)**<br>**Timestamp:** 14:18:32.192571<br>**Source:** Your machine (IP: your.machine, Port: 52444)<br>**Destination:** DNS server (dns.google.domain)<br>**Query Details:** 35084+ A? yummyrecipesforme.com (24)<br>**Explanation:** This query seeks the IP address for the domain yummyrecipesforme.com. |
| 2 | **14:18:32.204388 IP dns.google.domain > your.machine.52444: 35084 1/0/0 A 203.0.113.22 (40)**<br>**Timestamp:** 14:18:32.204388<br>**Source:** DNS server<br>**Destination:** Your machine (IP: your.machine, Port: 52444)<br>**Response Details:** 35084 1/0/0 A 203.0.113.22<br>**Explanation:** The DNS server replies to your machine with the IP address (203.0.113.22) associated with yummyrecipesforme.com. |
| 3 |TCP Flag codes include: <br> Flags [S]  - Connection Start <br> Flags [F]  - Connection Finish <br> Flags [P]  - Data Push <br> Flags [R]  - Connection Reset <br> Flags [.]  - Acknowledgment <br><br>  14:18:36.786501 IP your.machine.36086 > yummyrecipesforme.com.http: ***Flags [S]***, seq 2873951608, win 65495, options [mss 65495,sackOK,TS val 3302576859 ecr 0,nop,wscale 7], length 0 <br>**Explanation:** This packet initiates the TCP connection to the HTTP server of yummyrecipesforme.com with the [S] flag, indicating the start of the connection.

## Traffic Log:

| Description |
|---|
| **14:18:32.192571 IP your.machine.52444 > dns.google.domain: 35084+ A? yummyrecipesforme.com. (24)**  |
| **14:18:32.204388 IP dns.google.domain > your.machine.52444: 35084 1/0/0 A203.0.113.22 (40)**  |
| **14:18:36.786501 IP your.machine.36086 > yummyrecipesforme.com.http: Flags [S], seq 2873951608, win 65495, options [mss 65495,sackOK,TS val 3302576859 ecr 0,nop,wscale 7], length 0** |
| **14:18:36.786517 IP yummyrecipesforme.com.http > your.machine.36086: Flags [S.], seq 3984334959, ack 2873951609, win 65483, options [mss 65495,sackOK,TS val 3302576859 ecr 3302576859,nop,wscale 7], length 0** |
| **14:18:36.786529 IP your.machine.36086 > yummyrecipesforme.com.http: Flags[.], ack 1, win 512, options [nop,nop,TS val 3302576859 ecr 3302576859], length 0** |
| **14:18:36.786589 IP your.machine.36086 > yummyrecipesforme.com.http: Flags [P.], seq 1:74, ack 1, win 512, options [nop,nop,TS val 3302576859 ecr3302576859], length 73: HTTP: GET / HTTP/1.1** |
| **14:18:36.786595 IP yummyrecipesforme.com.http > your.machine.36086: Flags[.], ack 74, win 512, options [nop,nop,TS val 3302576859 ecr 3302576859], length 0** | 

| Description |
|---|
| ***14:20:32.192571 IP your.machine.52444 > dns.google.domain: 21899+ A?greatrecipesforme.com. (24)*** |
| ***14:20:32.204388 IP dns.google.domain > your.machine.52444: 21899 1/0/0 A192.0.2.17 (40)*** |
| ***14:25:29.576493 IP your.machine.56378 > greatrecipesforme.com.http: Flags[S], seq 1020702883, win 65495, options [mss 65495,sackOK,TS val 3302989649 ecr 0,nop,wscale 7], length 0*** |
| ***14:25:29.576510 IP greatrecipesforme.com.http > your.machine.56378: Flags[S.], seq 1993648018, ack 1020702884, win 65483, options [mss 65495,sackOK,TSval 3302989649 ecr 3302989649,nop,wscale 7], length 0*** |
| ***14:25:29.576524 IP your.machine.56378 > greatrecipesforme.com.http: Flags[.], ack 1, win 512, options [nop,nop,TS val 3302989649 ecr 3302989649], length 0*** |
| ***14:25:29.576590 IP your.machine.56378 > greatrecipesforme.com.http: Flags[P.], seq 1:74, ack 1, win 512, options [nop,nop,TS val 3302989649 ecr3302989649], length 73: HTTP: GET / HTTP/1.1*** |
| ***14:25:29.576597 IP greatrecipesforme.com.http > your.machine.56378: Flags[.], ack 74, win 512, options [nop,nop,TS val 3302989649 ecr 3302989649], length 0*** | <br>
...<a lot of traffic on the port 80>... 


## Respond: 

### Section 1: Identify the network protocol involved in the incident

The incident is centered around the HTTP protocol, which typically operates on port 80. Anomalies were detected in both DNS (Port 53) and HTTP traffic logs during TCPdump analysis. The transmission of the malicious file signifies an attack at the application layer, underscoring the criticality of securing the HTTP protocol in this scenario.

### Incident Description and Investigation

Several customers reported encountering a suspicious prompt upon visiting the website, compelling them to download and execute a file under the guise of browser updates, resulting in account lockouts. In response, the security team initiated an investigation using a sandbox environment and network traffic analysis tools such as tcpdump. The analysis revealed that the browser initially requested the IP address for the legitimate website, followed by a prompt to download the malicious file. Subsequent network traffic indicated a resolution of a new IP for a seemingly altered website. Further analysis unveiled a compromise in the website's code, facilitating the injection of code prompting users to download the malicious file. The compromise of the administrator account led to the locking out of all user accounts, suggestive of a potential brute force attack. The proliferation of the malicious file exacerbated the situation by infecting other computers.

### Section 3: Recommend one remediation for brute force attacks

Define Thresholds and Time Frame
- Determine the number of consecutive failed login attempts that will trigger an account lockout.
- Define the time window within which these failed attempts will be counted.

Specify Lockout Duration
- Establish the duration for which an account will remain locked after reaching the defined threshold of failed login attempts.

Implement Account Lockout Mechanism
- Configure the system to automatically lock user accounts that exceed the specified threshold of failed login attempts within the defined time frame.

Set Up Notification Mechanisms
- Implement notification mechanisms to alert administrators and users when an account is locked due to excessive failed login attempts.

Educate Users
- Provide comprehensive user education on the importance of strong, unique passwords, two-factor authentication (2FA), and adherence to security best practices to minimize the risk of successful brute force attacks.

Test and Refine
- Conduct thorough testing of the account lockout policy to ensure its effectiveness.
- Refine the policy based on testing results and feedback from users and administrators.

Monitor and Maintain
- Regularly monitor account lockout events and adjust policy parameters as needed to adapt to evolving threats.
- Maintain ongoing user education initiatives to reinforce security awareness and promote compliance with the account lockout policy.
