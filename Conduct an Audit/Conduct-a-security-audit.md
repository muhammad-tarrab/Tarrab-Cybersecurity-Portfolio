# Botium Toys Security Audit & Compliance

## Case Study: Botium Toys

Botium Toys is a small U.S.-based toy manufacturer and retailer with a single physical location that serves as its main office, storefront, and warehouse. Despite its modest physical presence, the company's online operations have expanded significantly, drawing in customers from both the U.S. and abroad. This growth has placed additional pressure on Botium Toys' Information Technology (IT) department to support the burgeoning online market.

The IT department manager has recognized the need for an internal IT audit to address the lack of a comprehensive strategy for business continuity and compliance as the company grows. An internal audit would provide insights into securing the company's infrastructure and identifying and mitigating potential risks, threats, or vulnerabilities to critical assets. The manager also seeks to ensure compliance with regulations governing online payment processing and conducting business in the European Union (EU).

To initiate the audit, the IT manager has begun implementing the National Institute of Standards and Technology Cybersecurity Framework (NIST CSF). This involves defining the scope and goals of the audit, cataloging the assets currently managed by the IT department, and conducting a risk assessment. The primary objective of the audit is to offer a comprehensive overview of potential risks and penalties the company may face due to its existing security practices.

Your task is to evaluate the IT manager's scope, goals, and risk assessment report. You will then conduct an internal audit by completing a controls and compliance checklist.

## Scenario 
Scope, goals, and risk assessment report


### Scope 

The scope is defined as the entire security program at Botium Toys. This means all assets need to be assessed alongside internal processes and procedures related to the implementation of controls and compliance best practices.


### Goals
Assess existing assets and complete the controls and compliance checklist to determine which controls and compliance best practices that need to be implemented to improve Botium Toys’ security posture.


### Current assets
Assets managed by the IT Department include: 
* On-premises equipment for in-office business needs
* Employee equipment: end-user devices (desktops/laptops, smartphones), remote workstations, headsets, cables, keyboards, mice, docking stations, surveillance cameras, etc.
* Storefront products available for retail sale on site and online; stored in the company’s adjoining warehouse
* Management of systems, software, and services: accounting, telecommunication, database, security, ecommerce, and inventory management
* Internet access
* Internal network
* Data retention and storage
* Legacy system maintenance: end-of-life systems that require human monitoring 

### Risk assessment

#### Risk description
Currently, there is inadequate management of assets. Additionally, Botium Toys does not have all of the proper controls in place and may not be fully compliant with U.S. and international regulations and standards. 

#### Control best practices
The first of the five functions of the NIST CSF is Identify. Botium Toys will need to dedicate resources to identify assets so they can appropriately manage them. Additionally, they will need to classify existing assets and determine the impact of the loss of existing assets, including systems, on business continuity.

#### Risk score
On a scale of 1 to 10, the risk score is 8, which is fairly high. This is due to a lack of controls and adherence to compliance best practices.

#### Additional comments
The potential impact from the loss of an asset is rated as medium, because the IT department does not know which assets would be at risk. The risk to assets or fines from governing bodies is high because Botium Toys does not have all of the necessary controls in place and is not fully adhering to best practices related to compliance regulations that keep critical data private/secure. Review the following bullet points for specific details:
#### Additional Info 

In Cybersecurity, control types can be classified in three ways: 
1. Administrative/Managerial controls
2. Technical controls
3. Physical/Operational controls

Control types (providing defense and protecting assets) include, but are not limited to:
1. Preventative (preventing an incident from occurring in the first place)
2. Corrective (restoring an asset after an incident)
3. Detective (Determining whether an incident has occurred or is in progress)
4. Deterrent (Discouraging attacks)

## Controls Assessment Checklist

Does Botium Toys currenly have this control in place? 

| Yes / No / ? | Control | Explanation |
| :-------        |    :---:   | :---     |
| No | Least Privilige | The employees have access to customer data. This has to be changed to reduce the risk of breach. |
| No | Disaster Recovery Plan | At the moment, there is no plan for handling disaster. Implementing this ensures the business continuity. |
| Yes | Firewall | The organization has a firewall to block traffic based on an appropriately defined set of security rules. |
| ? | Password policies | Password policy exists, yet the requirements are considered weak and put the identity management access at risk. |
| Yes | Antivirus | The antivirus software is active and regulary monitored by IT team. |
| No | Backups | This is as same as disaster recovery plan. They are not prepared in the case of breach. They have to implement the backup plan, such as incremental, full, or partial. |
| No | Encryption | This would protect confidentiality of data. |
| No | IDS | This would help IT team to identiy possible intrusions by the threat actors. | 
| Yes | Storefront| Although IT team is not responsible for the management at the storefront, however the organization should have sufficient locks.|
| Yes | CCTV | It is working and functioning. |
| Yes | Fire detection | The organization has these. However, the team should maintain it and establish a plan on how to use it. |

## Compliance Checklist
Does Botium Toys currenly adhrere to this compliance best practice? 

* Payment Card Industry Data Security Standard (PCI DSS)

| Yes/ No / ? | Best Practice | Explanation |
| :---        |    :---:   | :---     |
| No | Authorized users can access to customer's credit card. | At the moment, all employees have access to it which is a bad practice in the business.  |
| No | Credit card is stored in a secure environment. | It is not encrypted and violates the law and regulations. |
| No | Encryption is secured. | No, the encryption has not taken place yet. | 

* GDPR
  
| Yes/ No / ? | Best Practice | Explanation |
| :---        |    :---:   | :---     |
| No | EU customers are kept secured. | The organization does not apply GDPR practice. Thus, it puts them at risk of being fined by the EU government. |
| Yes | Privacy policies are maintained properly.| According to the scenario, it has been enforced by the IT Team members and other staff. |

* System and Organizations Controls 

| Yes/ No / ? | Best Practice | Explanation |
| :---        |    :---:   | :---     |
| No | User access policies are established | Employees have access to internally stored data which means the access policy has not been applied. |
| Yes | Data integrity is consistent, complete, accurate | Data integrity is in place. | 
| No | Data is available to authorized users | Currently, all the employees can access all the data. |

## Recommendations (optional)

After researching Botium Toys's security posture, the analysts agreed that the security practice is far from the expectation. It lacks of protection of confidentialiy of sensitive information. The following are:
1. Least privilege
2. Disaster recovery plan
3. Password policies
4. Encryption
5. Password management system

By implementing and updating these policies, and actively monitoring and assessing assets, Botium Toys can improve its security practice, reduce risks, and maintain compliance with regulatory requirements.
