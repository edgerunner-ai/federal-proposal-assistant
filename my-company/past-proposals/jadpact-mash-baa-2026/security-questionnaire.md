# Appendix 2 — Security Program Questionnaire
**AFRL S&T Protection | EdgeRunner AI, Inc.**
**Date Submitted:** March 14, 2026
**Completed by:** Sean Bailey, Head of Prototype Engineering
**CAGE:** 9Z176

> This is EdgeRunner's only on-file example of an AFRL Security Program Questionnaire.
> Reuse these answers directly for future AFRL BAA submissions — they are written to NIST SP 800-171
> and cover all standard 13 questions. Update personnel names and any specific system references as needed.

---

**Objective:** This questionnaire is used to review the security program and practices of institutions receiving research funding. Completed by collaborators; reviewed by S&T Protection Lead.

---

**1. What are your physical security plans?**

EdgeRunner AI personnel utilize company-issued laptops and development devices that are secured with full disk encryption and endpoint protection. Devices are maintained in controlled home office environments with restricted physical access. Personnel are responsible for safeguarding devices when not in use, including storage in secured locations. Physical media containing project information is prohibited unless encrypted and authorized in accordance with NIST SP 800-171 media protection controls.

---

**2. What information security processes are in place?**

EdgeRunner maintains an information security program aligned with NIST SP 800-171 controls for protection of Controlled Unclassified Information (CUI). Core protections include:

- Identity and Access Management (IAM) enforcing least privilege access
- Single Sign-On (SSO) with Multi-Factor Authentication (MFA)
- Encryption of data at rest and in transit
- Endpoint protection and device management
- Centralized logging and audit monitoring
- Role-Based Access Control (RBAC) for all systems supporting development and operations

These controls ensure only authorized personnel can access information related to this effort.

---

**3. Where will information for this effort be stored?**

Information supporting this effort will be stored on secured edge devices during inference runtime and within controlled cloud infrastructure used for model training and development.

Cloud storage environments utilize:
- Encryption at rest (AES-256 or equivalent)
- Encryption in transit (TLS 1.2 or higher)
- Role-based access control
- Audit logging

All storage environments are configured to protect Controlled Unclassified Information in accordance with NIST SP 800-171 security requirements.

---

**4. What procedures are in place for transmission/transportation of information for this effort?**

All data transmission utilizes TLS 1.2 or higher encryption. Access to systems transmitting project data requires authenticated user sessions protected by Multi-Factor Authentication (MFA).

Where applicable, system access uses SSH key authentication and restricted network ports. Network ingress and egress is monitored and limited to authorized endpoints.

---

**5. What procedures are in place for disposal and destruction of information for this effort?**

Data destruction follows NIST SP 800-88 media sanitization guidance:

- Cloud data is securely deleted using provider decommissioning procedures
- Edge devices and local storage are sanitized using secure wipe utilities prior to reassignment or disposal
- Any physical media containing project information is destroyed or sanitized using approved secure methods

These procedures ensure information cannot be recovered once disposal is complete.

---

**6. What procedures are in place for reproduction of information for this effort?**

Reproduction or duplication of project information is restricted to authorized systems and personnel supporting the effort. Data replication may occur within secured storage environments that enforce encryption, access controls, and audit logging.

Information may only be shared externally with authorized government personnel or approved collaborators under controlled access conditions.

---

**7. What safeguards are in place for personnel who can access information for this effort?**

Access to project information is governed by Role-Based Access Control (RBAC) enforced through Single Sign-On and Multi-Factor Authentication. Additional personnel safeguards include:

- Employment screening and vetting procedures
- Security awareness training for personnel handling sensitive information
- Access provisioning limited to personnel directly supporting the project
- Periodic review of access privileges

These measures ensure only authorized personnel can access project data.

---

**8. What is the plan for safeguarding GFE/GFI?**

Government Furnished Equipment (GFE) and Government Furnished Information (GFI) will be stored and accessed only on authorized devices and systems. Safeguards include:

- Encryption of data at rest and in transit
- Role-based access controls with MFA authentication
- Audit logging of access and data transfers
- Physical protection of devices when not in use

Access to GFE/GFI is limited strictly to personnel supporting the effort.

---

**9. What procedures are in place for cybersecurity or network protection?**

Systems supporting this effort implement layered cybersecurity protections including:

- Firewall protection and restricted network ports
- SSH key authentication for system access
- Endpoint protection and system hardening
- Network monitoring and logging
- Controlled ingress and egress access

These controls are implemented consistent with NIST SP 800-171 cybersecurity requirements.

---

**10. What operations security processes are in place to prevent adversaries' access to information for this effort?**

Operational security is maintained through:

- Least privilege access controls
- Multi-Factor Authentication for all system access
- Compartmentalization of project information
- Limited network exposure for edge devices and development environments
- Continuous logging and monitoring of system activity

These measures reduce the attack surface and protect sensitive information from unauthorized access.

---

**11. What processes are in place to deter, detect, and mitigate actions of insider threat?**

EdgeRunner mitigates insider threats through:

- Least privilege access enforcement
- Monitoring and logging of data access and transfer events
- Periodic access reviews to ensure appropriate permissions
- Restrictions on external data sharing

Suspicious activity is investigated through internal security procedures.

---

**12. What procedures are in place to handle if information for this effort is compromised?**

EdgeRunner maintains an incident response process to address potential security events. In the event of a suspected compromise, the company will:

1. Contain and isolate affected systems
2. Review audit logs to identify the scope of exposure
3. Notify appropriate project stakeholders and government sponsors as required
4. Implement remediation measures to prevent recurrence

Incident response procedures are designed to quickly identify, contain, and mitigate security risks.

---

**13. Are you willing to provide AFRL S&T Protection training to all personnel with access annually?**

Yes. EdgeRunner is willing to provide AFRL S&T Protection training annually to all personnel with access to project information.
