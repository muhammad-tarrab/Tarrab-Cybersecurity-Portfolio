# Security Risk Assessment Report: Network Hardening

## Scenario 

You are a security analyst working for a social media organization. The organization recently experienced a major data breach, compromising the safety of their customers’ personal information, such as names and addresses. Your organization wants to implement strong network hardening practices to prevent future attacks and breaches. 

After inspecting the organization’s network, you discover four major vulnerabilities:
1. The organization’s employees share passwords.
2. The admin password for the database is set to the default.
3. The firewalls lack rules to filter traffic coming in and out of the network.
4. Multifactor authentication (MFA) is not used. 

If no action is taken to address these vulnerabilities, the organization is at risk of experiencing another data breach or other attacks in the future. 

In this activity, you will write a security risk assessment to analyze the incident and explain what methods can be used to further secure the network.

## Selecting Hardening Tools and Methods & Explain your recommendations

To address the identified vulnerabilities and enhance network security, the following hardening tools and methods can be implemented:

1. **Password Management Software:**
   - Implementing a password management solution allows the organization to enforce strong, unique passwords for each user account while eliminating the practice of sharing passwords among employees. This ensures that sensitive accounts remain protected against unauthorized access. Additionally, the password management software can facilitate periodic password rotation to further enhance security.

2. **Database Hardening Techniques:**
   - Utilize database hardening techniques to secure the admin password for the database. This includes changing the default admin password to a strong, unique passphrase and implementing access controls to restrict unauthorized access to sensitive database resources. Additionally, enabling encryption for data at rest and in transit adds an extra layer of protection against data breaches.

3. **Firewall Configuration and Rule Management:**
   - Configure the organization's firewalls to implement strict inbound and outbound traffic filtering rules. This involves defining and enforcing firewall rules based on the principle of least privilege, allowing only necessary network traffic to pass through while blocking or denying unauthorized access attempts. Regularly reviewing and updating firewall rules ensures that the network remains protected against evolving threats.

4. **Multifactor Authentication (MFA) Implementation:**
   - Deploy multifactor authentication (MFA) across the organization's systems and applications to strengthen authentication mechanisms and prevent unauthorized access to sensitive resources. MFA requires users to provide additional verification factors, such as biometric data or one-time passcodes, in addition to their passwords, significantly reducing the risk of credential-based attacks like password guessing or phishing.

By implementing these hardening tools and methods, the organization can significantly improve its network security posture, mitigate the identified vulnerabilities, and reduce the risk of experiencing future data breaches or attacks. Regular monitoring, testing, and updates should be performed to ensure the effectiveness and continued resilience of the security measures implemented.
