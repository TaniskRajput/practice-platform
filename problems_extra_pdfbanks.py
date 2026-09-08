"""
Quizzes 23-26 parsed from KN Academy PDF question banks
(extracted/downloaded/*.pdf -> extracted/downloaded/mcq-banks.json).
Merged into problems.PROBLEMS by problems.py wiring.
"""

PDF_BANK_QUIZ_PROBLEMS = [


    # ------------------------------------------------------------------ #
    # 23. Cloud MCQ (Complete)
    # ------------------------------------------------------------------ #
    {
        "id": 23,
        "slug": "cloud-mcq",
        "title": "Cloud MCQ (Complete)",
        "difficulty": "Medium",
        "topics": "Cloud · Security · Services".split(" · "),
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p>100 cloud computing MCQs from the <b>Cloud MCQ</b> PDF — service models, deployment models, security and the shared responsibility model.</p>
<p>Select an option for every question, then press <b>Submit</b>. Correct answers
turn green; wrong picks show the right one.</p>
<p style="color:var(--text-dim)">Source PDF is in the <b>PDF Resources</b> section.</p>
""",
        "hint": "Source: KN Academy Cloud MCQ PDF. Submit to see the full answer key; re-attempt any time.",
        "boilerplate": {},
        "samples": [],
        "questions": [
        {
                "q": "<b>1.</b> What is the primary security advantage of using a public cloud provider?",
                "options": ["Reduced cost", "Increased physical security and expertise", "Complete control over data", "Simplified compliance"],
                "answer": 1
        },
        {
                "q": "<b>2.</b> The \"Shared Responsibility Model\" in cloud security means:",
                "options": ["The provider and customer share the cost of security breaches.", "Security is always the primary responsibility of the provider.", "Security responsibilities are divided between the provider and the customer.", "The customer is responsible for all security aspects."],
                "answer": 2
        },
        {
                "q": "<b>3.</b> Which cloud service model gives the customer the MOST control over security configurations?",
                "options": ["Software as a Service (SaaS)", "Platform as a Service (PaaS)", "Infrastructure as a Service (IaaS)", "Security as a Service (SECaaS)"],
                "answer": 2
        },
        {
                "q": "<b>4.</b> Which of the following is a key benefit of cloud computing?",
                "options": ["Guaranteed 100% uptime", "Elimination of all security risks", "Rapid elasticity and scalability", "Reduced need for internet connectivity"],
                "answer": 2
        },
        {
                "q": "<b>5.</b> What does the term \"Multi-tenancy\" mean in cloud computing?",
                "options": ["A single application serving multiple customers", "Multiple customers using separate, isolated resources", "Multiple customers sharing the same physical resources", "A customer using services from multiple providers"],
                "answer": 2
        },
        {
                "q": "<b>6.</b> Which type of cloud deployment model offers the highest level of control and security?",
                "options": ["Public Cloud", "Hybrid Cloud", "Community Cloud", "Private Cloud"],
                "answer": 3
        },
        {
                "q": "<b>7.</b> What is the purpose of data encryption \"at rest\"?",
                "options": ["To protect data while it is being transmitted over a network", "To protect data while it is stored on a disk or database", "To prevent data from being deleted", "To compress data to save space"],
                "answer": 1
        },
        {
                "q": "<b>8.</b> Which tool is commonly used to define and enforce security policies across cloud resources?",
                "options": ["Cloud Access Security Broker (CASB)", "Intrusion Detection System (IDS)", "Virtual Private Network (VPN)", "Web Application Firewall (WAF)"],
                "answer": 0
        },
        {
                "q": "<b>9.</b> A DDoS (Distributed Denial of Service) attack primarily aims to:",
                "options": ["Steal sensitive customer data", "Encrypt files for ransom", "Overwhelm a system with traffic to make it unavailable", "Gain administrative access to servers"],
                "answer": 2
        },
        {
                "q": "<b>10.</b> Identity and Access Management (IAM) is crucial in the cloud for:",
                "options": ["Ensuring high-speed data transfer", "Managing user identities and controlling their access to resources", "Encrypting all database contents", "Providing automatic backups"],
                "answer": 1
        },
        {
                "q": "<b>11.</b> What is a \"security group\" in Amazon Web Services (AWS)?",
                "options": ["A team of security engineers", "A virtual firewall for EC2 instances to control inbound and outbound traffic", "A method for grouping security alerts", "A encrypted storage volume"],
                "answer": 1
        },
        {
                "q": "<b>12.</b> The principle of \"Least Privilege\" means:",
                "options": ["Users should have their accounts permanently privileged.", "Users should be granted the minimum levels of access necessary to perform their duties.", "Privileged accounts should be used for all tasks.", "All users should have administrative access."],
                "answer": 1
        },
        {
                "q": "<b>13.</b> Which compliance standard is specifically designed for the payment card industry?",
                "options": ["HIPAA", "GDPR", "PCI DSS", "SOX"],
                "answer": 2
        },
        {
                "q": "<b>14.</b> What is a major security concern with serverless computing (e.g., AWS Lambda)?",
                "options": ["Physical server security", "Managing the operating system", "Insecure third-party dependencies and event data injection", "Configuring virtual networks"],
                "answer": 2
        },
        {
                "q": "<b>15.</b> Penetration Testing in the cloud:",
                "options": ["Is never allowed by cloud providers.", "Can usually be performed without provider approval on any service.", "Often requires explicit permission from the cloud provider.", "Is the sole responsibility of the provider."],
                "answer": 2
        },
        {
                "q": "<b>16.</b> Which service provides a secure, private connection between an on-premises network and a VPC in the cloud?",
                "options": ["Content Delivery Network (CDN)", "Virtual Private Network (VPN)", "Domain Name System (DNS)", "Load Balancer"],
                "answer": 1
        },
        {
                "q": "<b>17.</b> What is the main goal of data masking or tokenization?",
                "options": ["To improve database performance", "To reduce storage costs", "To de-identify sensitive data in non-production environments", "To encrypt data for transmission"],
                "answer": 2
        },
        {
                "q": "<b>18.</b> A vulnerability that allows a user to access resources from another tenant in a cloud environment is a:",
                "options": ["Data Breach", "Isolation Failure", "DDoS Attack", "Insider Threat"],
                "answer": 1
        },
        {
                "q": "<b>19.</b> What does a Web Application Firewall (WAF) protect against?",
                "options": ["Phishing emails", "Common web exploits like SQL injection and cross-site scripting (XSS)", "Insider data theft", "Physical intrusion"],
                "answer": 1
        },
        {
                "q": "<b>20.</b> Which of these is a characteristic of a well-designed cloud disaster recovery (DR) plan?",
                "options": ["It relies on manual processes for consistency.", "Its Recovery Time Objective (RTO) is as long as possible.", "It is tested regularly.", "It stores backups only in the same region as the primary data."],
                "answer": 2
        },
        {
                "q": "<b>21.</b> The EU's General Data Protection Regulation (GDPR) is primarily concerned with:",
                "options": ["Regulating financial markets", "Protecting the personal data and privacy of EU citizens", "Standardizing encryption algorithms", "Controlling cloud provider pricing"],
                "answer": 1
        },
        {
                "q": "<b>22.</b> What is the main purpose of a Cloud Security Posture Management (CSPM) tool?",
                "options": ["To encrypt all data at rest", "To automatically detect and remediate misconfigurations", "To provide anti-virus for virtual machines", "To manage user identities"],
                "answer": 1
        },
        {
                "q": "<b>23.</b> Which of the following is an example of an \"insider threat\"?",
                "options": ["A hacker from a foreign country", "A disgruntled employee with authorized access", "A natural disaster", "A hardware failure"],
                "answer": 1
        },
        {
                "q": "<b>24.</b> What does \"Data Residency\" refer to?",
                "options": ["The speed at which data can be accessed", "The physical geographic location where data is stored", "The cost of storing data", "The process of archiving old data"],
                "answer": 1
        },
        {
                "q": "<b>25.</b> MFA (Multi-Factor Authentication) enhances security by requiring:",
                "options": ["Multiple passwords", "Two or more verification factors (e.g., password + code from phone)", "Biometric verification only", "Automatic logouts after inactivity"],
                "answer": 1
        },
        {
                "q": "<b>26.</b> Which cloud deployment model combines on-premises infrastructure with public cloud services?",
                "options": ["Public Cloud", "Private Cloud", "Hybrid Cloud", "Multi-Cloud"],
                "answer": 2
        },
        {
                "q": "<b>27.</b> What is the primary risk of using shadow IT?",
                "options": ["Increased cost", "It bypasses organizational security policies and controls", "It slows down innovation", "It requires more IT staff"],
                "answer": 1
        },
        {
                "q": "<b>28.</b> An API (Application Programming Interface) gateway in a cloud environment can enhance security by:",
                "options": ["Providing physical security for servers", "Acting as a single entry point to manage, authenticate, and throttle API traffic", "Encrypting all data at rest automatically", "Replacing the need for a firewall"],
                "answer": 1
        },
        {
                "q": "<b>29.</b> What is the main purpose of a Business Continuity Plan (BCP)?",
                "options": ["To ensure only authorized users have access", "To maintain essential functions during and after a disaster", "To encrypt all customer data", "To reduce cloud spending"],
                "answer": 1
        },
        {
                "q": "<b>30.</b> Which storage class in cloud storage (e.g., Amazon S3) is designed for long-term archival with the lowest cost?",
                "options": ["Standard", "Infrequent Access", "Glacier/Deep Archive", "One Zone-Infrequent Access"],
                "answer": 2
        },
        {
                "q": "<b>31.</b> Container security best practices include:",
                "options": ["Always running containers as the root user", "Using only the latest image tags without scanning", "Scanning images for vulnerabilities and running with least privilege", "Storing secrets and API keys within the container image"],
                "answer": 2
        },
        {
                "q": "<b>32.</b> What does a Content Delivery Network (CDN) primarily improve?",
                "options": ["Data encryption strength", "Performance and availability by caching content at edge locations", "Physical security of data centers", "User access control policies"],
                "answer": 1
        },
        {
                "q": "<b>33.</b> The term \"Zero Trust\" security model is based on the concept of:",
                "options": ["\"Trust no one, verify everything\"", "\"Trust but verify\"", "\"Implicit trust within the corporate network\"", "\"Complete trust in the cloud provider\""],
                "answer": 0
        },
        {
                "q": "<b>34.</b> Which type of encryption key is managed by the cloud provider?",
                "options": ["Customer-Managed Key (CMK)", "Provider-Managed Key (PMK)", "Bring Your Own Key (BYOK)", "Hardware Security Module (HSM)"],
                "answer": 1
        },
        {
                "q": "<b>35.</b> What is the primary function of an Intrusion Detection System (IDS)?",
                "options": ["To block malicious traffic automatically", "To monitor network traffic and generate alerts for suspicious activity", "To encrypt all data packets", "To authenticate users"],
                "answer": 1
        },
        {
                "q": "<b>36.</b> A security misconfiguration is most likely to lead to:",
                "options": ["Improved performance", "A data breach", "Lower costs", "Faster deployment"],
                "answer": 1
        },
        {
                "q": "<b>37.</b> What is the purpose of a Service Level Agreement (SLA) in cloud computing?",
                "options": ["To define the price of services", "To legally define the service standards, including uptime and support responsiveness", "To specify the technical architecture", "To list all employees of the provider"],
                "answer": 1
        },
        {
                "q": "<b>38.</b> Which strategy involves using multiple cloud providers to avoid vendor lock-in and increase resilience?",
                "options": ["Hybrid Cloud", "Private Cloud", "Multi-Cloud", "Community Cloud"],
                "answer": 2
        },
        {
                "q": "<b>39.</b> What is a \"cold\" disaster recovery site?",
                "options": ["A site with running servers that can take over immediately", "A site with power and cooling but no pre-configured hardware", "A cloud-based recovery site", "A site located in a cold climate for natural cooling"],
                "answer": 1
        },
        {
                "q": "<b>40.</b> Which regulation governs the protection of health information in the United States?",
                "options": ["GDPR", "PCI DSS", "HIPAA", "FISMA"],
                "answer": 2
        },
        {
                "q": "<b>41.</b> The \"CIA Triad\" in security stands for:",
                "options": ["Central Intelligence Agency", "Confidentiality, Integrity, Availability", "Cloud Infrastructure Access", "Critical Incident Analysis"],
                "answer": 1
        },
        {
                "q": "<b>42.</b> What is the main security risk of using public container images from registries like Docker Hub?",
                "options": ["They are always more expensive.", "They may contain malicious code or vulnerabilities.", "They cannot be scaled.", "They are always slower."],
                "answer": 1
        },
        {
                "q": "<b>43.</b> What does \"VPC\" stand for in cloud networking?",
                "options": ["Virtual Public Connection", "Verified Private Cloud", "Virtual Private Cloud", "Virtual Packet Circuit"],
                "answer": 2
        },
        {
                "q": "<b>44.</b> Which of these is a database security best practice?",
                "options": ["Use default database passwords for simplicity.", "Enable public access to the database for easy connectivity.", "Use parameterized queries to prevent SQL injection.", "Store database logs in the same instance as the database."],
                "answer": 2
        },
        {
                "q": "<b>45.</b> A security audit is performed primarily to:",
                "options": ["Improve system performance", "Reduce storage costs", "Verify compliance with security policies and regulations", "Develop new software features"],
                "answer": 2
        },
        {
                "q": "<b>46.</b> What is the key difference between a vulnerability and an exploit?",
                "options": ["A vulnerability is a weakness; an exploit is code that attacks it.", "They are the same thing.", "An exploit is a weakness; a vulnerability is an attack.", "A vulnerability is always more dangerous."],
                "answer": 0
        },
        {
                "q": "<b>47.</b> Which service provides secrets management (e.g., for API keys, passwords) in AWS?",
                "options": ["AWS Secrets Manager", "AWS IAM", "AWS KMS", "AWS CloudTrail"],
                "answer": 0
        },
        {
                "q": "<b>48.</b> What is the primary purpose of log management and monitoring?",
                "options": ["To use more storage space", "To enable forensic analysis and detect anomalies in real-time", "To slow down applications", "To comply with data residency laws"],
                "answer": 1
        },
        {
                "q": "<b>49.</b> What does \"Immutable Infrastructure\" refer to?",
                "options": ["Infrastructure that cannot be changed", "Servers that are never patched or updated", "An approach where servers are never modified after deployment; instead, they are replaced with", "Infrastructure located in a single data center"],
                "answer": 2
        },
        {
                "q": "<b>50.</b> Which cloud-native tool in AWS provides a history of API calls and resource changes for auditing?",
                "options": ["AWS CloudWatch", "AWS Config", "AWS CloudTrail", "AWS Shield"],
                "answer": 1
        },
        {
                "q": "<b>51.</b> What is the primary purpose of a \"Bastion Host\" (or Jump Box) in cloud architecture?",
                "options": ["To serve public web content", "To provide a single, secured entry point for administrative access to a private network", "To act as a primary database server", "To perform automated backups"],
                "answer": 1
        },
        {
                "q": "<b>52.</b> Which AWS service provides protection against DDoS attacks?",
                "options": ["AWS GuardDuty", "AWS Shield", "AWS WAF", "AWS KMS"],
                "answer": 1
        },
        {
                "q": "<b>53.</b> The practice of \"Server Hardening\" involves:",
                "options": ["Making servers physically difficult to move", "Reducing server performance to save energy", "Reducing the attack surface by minimizing vulnerabilities", "Using only the most expensive server types"],
                "answer": 2
        },
        {
                "q": "<b>54.</b> What is a \"Canary\" in the context of security?",
                "options": ["A type of encryption algorithm", "A decoy system or piece of data designed to lure attackers and alert defenders", "A bird used to detect poisonous gases in data centers", "A high-speed network connection"],
                "answer": 1
        },
        {
                "q": "<b>55.</b> Which of the following is a key principle of DevSecOps?",
                "options": ["Security is the sole responsibility of a separate team.", "Security testing is performed only after development is complete.", "Security is integrated into every phase of the software development lifecycle.", "Development speed is prioritized over security."],
                "answer": 2
        },
        {
                "q": "<b>56.</b> What does \"Data Exfiltration\" mean?",
                "options": ["The process of backing up data", "The unauthorized transfer of data from a system", "The encryption of data", "The process of importing data into a cloud environment"],
                "answer": 1
        },
        {
                "q": "<b>57.</b> Which Microsoft Azure service provides a single dashboard for managing security posture and threat protection?",
                "options": ["Azure Security Center", "Azure Active Directory", "Azure Sentinel", "Azure Policy"],
                "answer": 0
        },
        {
                "q": "<b>58.</b> What is the main security benefit of using \"Microsegmentation\"?",
                "options": ["To improve network speed", "To create security policies down to the workload level, limiting lateral movement", "To reduce the cost of firewalls", "To simplify network architecture"],
                "answer": 1
        },
        {
                "q": "<b>59.</b> In the context of incident response, what does \"Containment\" involve?",
                "options": ["Identifying the root cause of the incident", "Isolating the affected systems to prevent further damage", "Notifying customers and regulators", "Restoring systems from backup"],
                "answer": 1
        },
        {
                "q": "<b>60.</b> Which type of security testing involves analyzing an application's source code for vulnerabilities?",
                "options": ["Penetration Testing", "Static Application Security Testing (SAST)", "Dynamic Application Security Testing (DAST)", "Vulnerability Scanning"],
                "answer": 1
        },
        {
                "q": "<b>61.</b> What is the primary function of a Hardware Security Module (HSM)?",
                "options": ["To provide physical cooling for servers", "To securely generate, store, and manage cryptographic keys", "To act as a high-speed router", "To host virtual machines"],
                "answer": 1
        },
        {
                "q": "<b>62.</b> The \"Right to be Forgotten\" is a key principle of which regulation?",
                "options": ["PCI DSS", "HIPAA", "GDPR", "SOX"],
                "answer": 2
        },
        {
                "q": "<b>63.</b> What is a \"Threat Model\"?",
                "options": ["A list of all past security incidents", "A proactive process to identify potential threats and vulnerabilities", "A type of virus", "A profile of a cybercriminal"],
                "answer": 1
        },
        {
                "q": "<b>64.</b> Which Google Cloud Platform (GCP) service is used for secrets management?",
                "options": ["Cloud KMS", "Cloud IAM", "Secret Manager", "Security Command Center"],
                "answer": 2
        },
        {
                "q": "<b>65.</b> A \"Supply Chain Attack\" targets:",
                "options": ["A company's logistics and shipping software", "The software development tools or third-party dependencies used to build an application", "The power supply to a data center", "The network cables connecting servers"],
                "answer": 1
        },
        {
                "q": "<b>66.</b> What does a high \"Recovery Time Objective (RTO)\" indicate?",
                "options": ["The system can be recovered very quickly.", "The organization can tolerate a long downtime.", "Data loss will be minimal.", "The disaster recovery plan is excellent."],
                "answer": 1
        },
        {
                "q": "<b>67.</b> Which concept involves granting temporary, elevated permissions to a user to perform a specific task?",
                "options": ["Permanent Privilege", "Just-In-Time (JIT) Access", "Role-Based Access Control (RBAC)", "Multi-Factor Authentication (MFA)"],
                "answer": 1
        },
        {
                "q": "<b>68.</b> What is the main risk associated with \"Orphaned Resources\" in the cloud?",
                "options": ["They improve cost efficiency.", "They can be forgotten but still running, incurring costs and posing security risks.", "They automatically scale down.", "They are automatically secured by the provider."],
                "answer": 1
        },
        {
                "q": "<b>69.</b> Which service is used for auditing and tracking user activity and API usage in AWS?",
                "options": ["AWS CloudTrail", "AWS Config", "AWS CloudWatch", "AWS X-Ray"],
                "answer": 0
        },
        {
                "q": "<b>70.</b> \"Defense in Depth\" is a strategy that employs:",
                "options": ["A single, strong perimeter firewall", "Multiple layers of security controls", "Hiding the location of the servers", "Using only proprietary software"],
                "answer": 1
        },
        {
                "q": "<b>71.</b> What is the primary use case for a \"Cold\" storage class in cloud storage?",
                "options": ["Hosting live website content", "Storing data that is frequently accessed and modified", "Long-term archival of data that is rarely accessed", "Caching session data for web applications"],
                "answer": 2
        },
        {
                "q": "<b>72.</b> Which tool would you use to assess your AWS environment against best practices for security and compliance?",
                "options": ["AWS Trusted Advisor", "AWS Pricing Calculator", "AWS Migration Hub", "AWS Snowball"],
                "answer": 0
        },
        {
                "q": "<b>73.</b> A \"Man-in-the-Middle\" (MitM) attack succeeds by:",
                "options": ["Overwhelming a server with requests", "Secretly relaying and possibly altering the communication between two parties", "Guessing a user's password", "Infecting a system with ransomware"],
                "answer": 1
        },
        {
                "q": "<b>74.</b> What is the key characteristic of a \"Non-repudiation\" security service?",
                "options": ["Data is kept secret from unauthorized users.", "Data is not altered in transit.", "The sender of a message cannot later deny having sent it.", "Systems are available 24/7."],
                "answer": 2
        },
        {
                "q": "<b>75.</b> Which cloud deployment model is shared by several organizations with common concerns (e.g., mission, security needs)?",
                "options": ["Public Cloud", "Private Cloud", "Hybrid Cloud", "Community Cloud"],
                "answer": 3
        },
        {
                "q": "<b>76.</b> What does \"Tokenization\" achieve for sensitive data like credit card numbers?",
                "options": ["It encrypts the data with a reversible algorithm.", "It replaces the sensitive data with a non-sensitive equivalent (a \"token\") that has no exploitable", "It compresses the data to save space.", "It permanently deletes the data."],
                "answer": 1
        },
        {
                "q": "<b>77.</b> Which component is essential for establishing a secure connection to a cloud VPC from a single computer?",
                "options": ["A Content Delivery Network (CDN)", "A Client VPN", "A Load Balancer", "A Bastion Host"],
                "answer": 1
        },
        {
                "q": "<b>78.</b> The \"OWASP Top 10\" is a list of the most critical:",
                "options": ["Cloud providers", "Web application security risks", "Encryption algorithms", "Compliance standards"],
                "answer": 1
        },
        {
                "q": "<b>79.</b> What is the primary purpose of a \"Synchronization\" attack against cloud data?",
                "options": ["To ensure data is consistent across devices", "To overwhelm a system by forcing it to resync data repeatedly", "To improve data availability", "To encrypt data for backup"],
                "answer": 1
        },
        {
                "q": "<b>80.</b> Which practice involves comparing current cloud configurations against a known secure baseline?",
                "options": ["Penetration Testing", "Benchmarking", "Vulnerability Scanning", "Secret Management"],
                "answer": 1
        },
        {
                "q": "<b>81.</b> A \"Worm\" is a type of malware that is characterized by:",
                "options": ["Locking files and demanding a ransom", "Spying on user keystrokes", "Self-replicating and spreading to other systems without user intervention", "Displaying unwanted advertisements"],
                "answer": 2
        },
        {
                "q": "<b>82.</b> What is the main security concern with \"Server-Side Request Forgery\" (SSRF)?",
                "options": ["Forging a user's identity", "Tricking a server into making requests to internal resources that it should not have access to", "Stealing a user's session cookie", "Injecting malicious SQL code"],
                "answer": 1
        },
        {
                "q": "<b>83.</b> Which Azure service is a cloud-native SIEM (Security Information and Event Management) system?",
                "options": ["Azure Security Center", "Azure Sentinel", "Azure Monitor", "Azure Active Directory"],
                "answer": 1
        },
        {
                "q": "<b>84.</b> The concept of \"Data Sovereignty\" is closely related to:",
                "options": ["Data portability", "Data residing in a country subject to its laws and governance structures", "Data encryption", "Data processing speed"],
                "answer": 1
        },
        {
                "q": "<b>85.</b> What is a \"VPC Flow Log\" in AWS used for?",
                "options": ["To encrypt traffic within a VPC", "To capture information about the IP traffic going to and from network interfaces", "To automatically scale network bandwidth", "To create a VPN connection"],
                "answer": 1
        },
        {
                "q": "<b>86.</b> Which of these is a key benefit of using \"Infrastructure as Code\" (IaC) for security?",
                "options": ["It eliminates the need for security policies.", "It allows security and compliance rules to be defined, version-controlled, and consistently applied.", "It makes infrastructure changes slower and more deliberate.", "It requires manual configuration for each deployment."],
                "answer": 1
        },
        {
                "q": "<b>87.</b> A \"Blue/Green Deployment\" strategy enhances security and availability by:",
                "options": ["Using two different cloud providers simultaneously", "Running two identical production environments and switching traffic at once", "Deploying code only on weekends", "Using only blue and green servers for branding"],
                "answer": 1
        },
        {
                "q": "<b>88.</b> What is the primary purpose of a \"Honeypot\"?",
                "options": ["To store sweet data", "To attract and analyze attacker behavior in a controlled environment", "To improve application performance", "To serve as a primary production server"],
                "answer": 1
        },
        {
                "q": "<b>89.</b> Which type of access control model uses labels like \"Confidential\" and \"Top Secret\"?",
                "options": ["Role-Based Access Control (RBAC)", "Mandatory Access Control (MAC)", "Discretionary Access Control (DAC)", "Attribute-Based Access Control (ABAC)"],
                "answer": 1
        },
        {
                "q": "<b>90.</b> What does the \"Principle of Fail-Secure\" state?",
                "options": ["Systems should fail open to maintain availability.", "Systems should fail in a way that protects security, even if it impacts availability.", "All failures should be logged but ignored.", "Failure is not an option."],
                "answer": 1
        },
        {
                "q": "<b>91.</b> A \"Race Condition\" vulnerability can be exploited by:",
                "options": ["Sending a very large amount of data", "Submitting requests at exactly the same time to exploit the time gap between check and use", "Phishing a user", "Brute-forcing a password"],
                "answer": 1
        },
        {
                "q": "<b>92.</b> Which GCP service provides built-in DDoS protection and a global load balancer?",
                "options": ["Cloud CDN", "Cloud Armor", "Cloud NAT", "Cloud DNS"],
                "answer": 1
        },
        {
                "q": "<b>93.</b> What is \"Vendor Lock-in\" in the context of cloud computing?",
                "options": ["The physical locking of server racks", "The difficulty in moving from one cloud provider to another due to proprietary technologies", "A security feature that locks accounts", "A type of encryption provided by the vendor"],
                "answer": 1
        },
        {
                "q": "<b>94.</b> The \"S3\" in Amazon S3 stands for:",
                "options": ["Secure Storage Service", "Simple Storage Service", "System Storage Server", "Standard Storage System"],
                "answer": 1
        },
        {
                "q": "<b>95.</b> Which security control is most effective against phishing attacks?",
                "options": ["Strong firewalls", "User security awareness training", "Intrusion Detection Systems (IDS)", "Using the latest antivirus software"],
                "answer": 1
        },
        {
                "q": "<b>96.</b> What is the main purpose of a \"Service Control Policy\" (SCP) in AWS Organizations?",
                "options": ["To control traffic between instances", "To define permission boundaries for what actions members accounts can do", "To encrypt data at rest", "To manage user passwords"],
                "answer": 1
        },
        {
                "q": "<b>97.</b> A \"Golden Image\" is a:",
                "options": ["A specially colored server chassis", "A pre-configured, hardened, and approved virtual machine template used to launch new instances", "A backup of all data", "A certificate for SSL/TLS"],
                "answer": 1
        },
        {
                "q": "<b>98.</b> What does a \"Secrets Manager\" service help to prevent?",
                "options": ["Hardcoding API keys and passwords into application code", "Users from sharing passwords", "DDoS attacks", "Data loss due to hardware failure"],
                "answer": 0
        },
        {
                "q": "<b>99.</b> Which metric measures the maximum tolerable amount of data loss after an incident?",
                "options": ["Recovery Time Objective (RTO)", "Recovery Point Objective (RPO)", "Mean Time To Recovery (MTTR)", "Service Level Agreement (SLA)"],
                "answer": 1
        },
        {
                "q": "<b>100.</b> The \"Shared Responsibility Model\" for IaaS states that the customer is responsible for:",
                "options": ["Physical security of the data centers", "Securing the hypervisor", "Securing the guest operating system and applications", "Controlling the network infrastructure"],
                "answer": 2
        },
        ],
    },

    # ------------------------------------------------------------------ #
    # 24. Network Security MCQ
    # ------------------------------------------------------------------ #
    {
        "id": 24,
        "slug": "network-security-mcq",
        "title": "Network Security MCQ",
        "difficulty": "Medium",
        "topics": "Security · Protocols · Attacks".split(" · "),
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p>100 network-security MCQs from the <b>Network Security</b> PDF — firewalls, VPNs, cryptography, malware and protocols.</p>
<p>Select an option for every question, then press <b>Submit</b>. Correct answers
turn green; wrong picks show the right one.</p>
<p style="color:var(--text-dim)">Source PDF is in the <b>PDF Resources</b> section.</p>
""",
        "hint": "Source: KN Academy Network Security PDF. Submit to see the full answer key; re-attempt any time.",
        "boilerplate": {},
        "samples": [],
        "questions": [
        {
                "q": "<b>1.</b> What is the primary purpose of a firewall?",
                "options": ["Virus detection", "Network traffic filtering", "Password encryption", "Data backup"],
                "answer": 1
        },
        {
                "q": "<b>2.</b> Which port does HTTPS typically use?",
                "options": ["80", "443", "21", "25"],
                "answer": 1
        },
        {
                "q": "<b>3.</b> What does VPN stand for?",
                "options": ["Virtual Private Network", "Verified Protocol Network", "Virtual Public Network", "Verified Private Node"],
                "answer": 0
        },
        {
                "q": "<b>4.</b> Which protocol is used for secure file transfer?",
                "options": ["FTP", "SFTP", "HTTP", "Telnet"],
                "answer": 1
        },
        {
                "q": "<b>5.</b> What is the main vulnerability in WEP?",
                "options": ["Weak encryption keys", "No authentication", "RC4 stream cipher weakness", "Limited key length"],
                "answer": 2
        },
        {
                "q": "<b>6.</b> What type of malware replicates itself?",
                "options": ["Trojan", "Worm", "Ransomware", "Spyware"],
                "answer": 1
        },
        {
                "q": "<b>7.</b> What is phishing?",
                "options": ["Hardware theft", "Social engineering via email", "Network scanning", "Password cracking"],
                "answer": 1
        },
        {
                "q": "<b>8.</b> What does DDoS stand for?",
                "options": ["Distributed Denial of Service", "Direct Data Overflow System", "Digital Domain Security", "Data Destruction Operation"],
                "answer": 0
        },
        {
                "q": "<b>9.</b> What is a zero-day vulnerability?",
                "options": ["Unknown bug with no patch", "Expired security certificate", "Weak password policy", "Unencrypted data transfer"],
                "answer": 0
        },
        {
                "q": "<b>10.</b> What is ransomware?",
                "options": ["Malware that encrypts files for ransom", "Virus that steals data", "Worm that spreads rapidly", "Trojan that creates backdoors"],
                "answer": 0
        },
        {
                "q": "<b>11.</b> Which is symmetric encryption?",
                "options": ["RSA", "AES", "ECC", "Diffie-Hellman"],
                "answer": 1
        },
        {
                "q": "<b>12.</b> What does SSL/TLS provide?",
                "options": ["End-to-end encryption", "Network segmentation", "Physical security", "Data backup"],
                "answer": 0
        },
        {
                "q": "<b>13.</b> What is hashing used for?",
                "options": ["Data encryption", "Data integrity verification", "User authentication", "Network routing"],
                "answer": 1
        },
        {
                "q": "<b>14.</b> Which is the strongest encryption?",
                "options": ["DES", "3DES", "AES-256", "RC4"],
                "answer": 2
        },
        {
                "q": "<b>15.</b> What is public key cryptography?",
                "options": ["Same key for encryption/decryption", "Different keys for encryption/decryption", "No keys used", "Shared secret keys"],
                "answer": 1
        },
        {
                "q": "<b>16.</b> What is multi-factor authentication?",
                "options": ["Using multiple passwords", "Verification from multiple sources", "Multiple security questions", "Several encryption layers"],
                "answer": 1
        },
        {
                "q": "<b>17.</b> What is the principle of least privilege?",
                "options": ["Users get maximum access", "Users get minimum necessary access", "All users have equal access", "No access restrictions"],
                "answer": 1
        },
        {
                "q": "<b>18.</b> What is RBAC?",
                "options": ["Role-Based Access Control", "Rule-Based Authentication Control", "Random Binary Access Code", "Remote Backup and Control"],
                "answer": 0
        },
        {
                "q": "<b>19.</b> What is biometric authentication?",
                "options": ["Using physical characteristics", "Using complex passwords", "Using security tokens", "Using encryption keys"],
                "answer": 0
        },
        {
                "q": "<b>20.</b> What is single sign-on (SSO)?",
                "options": ["One password for all systems", "Multiple authentications for one system", "No authentication required", "Automatic login without credentials"],
                "answer": 0
        },
        {
                "q": "<b>21.</b> What is SQL injection?",
                "options": ["Database attack through malicious queries", "Password cracking technique", "Network eavesdropping", "File encryption attack"],
                "answer": 0
        },
        {
                "q": "<b>22.</b> What is XSS?",
                "options": ["Cross-Site Scripting", "Extended Security System", "External Server Scanning", "Encrypted Session Service"],
                "answer": 0
        },
        {
                "q": "<b>23.</b> What is a CSRF attack?",
                "options": ["Cross-Site Request Forgery", "Certificate Security Request Failure", "Cryptographic System Random Fault", "Client-Side Resource Filtering"],
                "answer": 0
        },
        {
                "q": "<b>24.</b> What is clickjacking?",
                "options": ["Tricking users to click hidden elements", "Stealing click history", "Monitoring mouse movements", "Blocking legitimate clicks"],
                "answer": 0
        },
        {
                "q": "<b>25.</b> What are web application firewalls (WAF)?",
                "options": ["Protect web apps from attacks", "Block all internet traffic", "Encrypt web server data", "Monitor user browsing habits"],
                "answer": 0
        },
        {
                "q": "<b>26.</b> What is the first step in incident response?",
                "options": ["Preparation", "Detection", "Containment", "Eradication"],
                "answer": 0
        },
        {
                "q": "<b>27.</b> What is a SIEM system?",
                "options": ["Security Information and Event Management", "System Integrity and Encryption Module", "Secure Internet Email Management", "Server Incident and Error Monitoring"],
                "answer": 0
        },
        {
                "q": "<b>28.</b> What is digital forensics?",
                "options": ["Collecting and analyzing digital evidence", "Creating digital art", "Designing digital circuits", "Programming digital systems"],
                "answer": 0
        },
        {
                "q": "<b>29.</b> What is an incident response plan?",
                "options": ["Documented procedures for handling security breaches", "Insurance policy for cyber attacks", "Employee training schedule", "Software update procedure"],
                "answer": 0
        },
        {
                "q": "<b>30.</b> What is chain of custody?",
                "options": ["Documentation of evidence handling", "Password change procedure", "Network access hierarchy", "Software development lifecycle"],
                "answer": 0
        },
        {
                "q": "<b>31.</b> What is mobile device management (MDM)?",
                "options": ["Securing and controlling mobile devices", "Developing mobile applications", "Manufacturing mobile hardware", "Testing mobile networks"],
                "answer": 0
        },
        {
                "q": "<b>32.</b> What is jailbreaking?",
                "options": ["Removing iOS restrictions", "Breaking into Android phones", "Repairing mobile devices", "Securing mobile networks"],
                "answer": 0
        },
        {
                "q": "<b>33.</b> What is rooting?",
                "options": ["Gaining admin access on Android", "Securing Android devices", "Factory resetting phones", "Installing official updates"],
                "answer": 0
        },
        {
                "q": "<b>34.</b> What is the main IoT security concern?",
                "options": ["Weak authentication", "Large storage capacity", "High processing power", "Color displays"],
                "answer": 0
        },
        {
                "q": "<b>35.</b> What is BYOD?",
                "options": ["Bring Your Own Device", "Backup Your Online Data", "Bring Your Own Drive", "Backup Your Office Documents"],
                "answer": 0
        },
        {
                "q": "<b>36.</b> What is the shared responsibility model?",
                "options": ["Cloud provider and customer share security duties", "Multiple teams share one responsibility", "All employees have same security role", "Security is nobody's specific responsibility"],
                "answer": 0
        },
        {
                "q": "<b>37.</b> What is CASB?",
                "options": ["Cloud Access Security Broker", "Certificate Authority Security Base", "Cyber Attack Simulation Bot", "Cloud Authentication Security Bridge"],
                "answer": 0
        },
        {
                "q": "<b>38.</b> What is data encryption at rest?",
                "options": ["Encrypting stored data", "Encrypting data in transit", "Encrypting data being processed", "Encrypting backup tapes"],
                "answer": 0
        },
        {
                "q": "<b>39.</b> What is cloud storage bucket?",
                "options": ["Container for cloud data storage", "Virtual machine instance", "Network security group", "User authentication service"],
                "answer": 0
        },
        {
                "q": "<b>40.</b> What is the main risk of public cloud?",
                "options": ["Data exposure through misconfiguration", "Physical theft of servers", "Power outages", "Hardware failures"],
                "answer": 0
        },
        {
                "q": "<b>41.</b> What is pretexting?",
                "options": ["Creating false scenarios to obtain information", "Sending mass emails", "Breaking encryption", "Scanning networks"],
                "answer": 0
        },
        {
                "q": "<b>42.</b> What is tailgating?",
                "options": ["Unauthorized physical entry following authorized person", "Hacking wireless networks", "Tracking online activities", "Stealing mobile devices"],
                "answer": 0
        },
        {
                "q": "<b>43.</b> What is vishing?",
                "options": ["Voice phishing", "Video phishing", "Virtual phishing", "Verified phishing"],
                "answer": 0
        },
        {
                "q": "<b>44.</b> What is smishing?",
                "options": ["SMS phishing", "Social media phishing", "Server message phishing", "Secure message phishing"],
                "answer": 0
        },
        {
                "q": "<b>45.</b> What is quid pro quo attack?",
                "options": ["Offering something in exchange for information", "Demanding ransom for data", "Threatening legal action", "Pretending to be technical support"],
                "answer": 0
        },
        {
                "q": "<b>46.</b> What is GDPR?",
                "options": ["General Data Protection Regulation", "Global Digital Privacy Rights", "Government Data Protection Rules", "General Digital Policy Regulation"],
                "answer": 0
        },
        {
                "q": "<b>47.</b> What is HIPAA?",
                "options": ["Health Insurance Portability and Accountability Act", "High Internet Protocol Authentication Act", "Hardware Integrity Protection and Access Act", "Homeland Security Information Protection Act"],
                "answer": 0
        },
        {
                "q": "<b>48.</b> What is PCI DSS?",
                "options": ["Payment Card Industry Data Security Standard", "Personal Computer Integrity Data Security System", "Protected Card Information Digital Security Standard", "Public Certificate Infrastructure Data Security Standard"],
                "answer": 0
        },
        {
                "q": "<b>49.</b> What is SOX?",
                "options": ["Sarbanes-Oxley Act", "Security Operations Excellence", "System Operations and Execution", "Secure Online Exchange"],
                "answer": 0
        },
        {
                "q": "<b>50.</b> What is FISMA?",
                "options": ["Federal Information Security Management Act", "Financial Institution Security Management Act", "Federal Internet Security Monitoring Agency", "Financial Information System Management Act"],
                "answer": 0
        },
        {
                "q": "<b>51.</b> What is mantrap?",
                "options": ["Physical access control with two doors", "Network intrusion detection", "Malware containment system", "Data encryption method"],
                "answer": 0
        },
        {
                "q": "<b>52.</b> What is RFID cloning?",
                "options": ["Copying access card data", "Duplicating computer files", "Replicating network signals", "Copying biometric data"],
                "answer": 0
        },
        {
                "q": "<b>53.</b> What is the purpose of security cameras?",
                "options": ["Visual monitoring and deterrence", "Temperature monitoring", "Network speed testing", "Data backup storage"],
                "answer": 0
        },
        {
                "q": "<b>54.</b> What is tailgating detection?",
                "options": ["Identifying unauthorized entry attempts", "Monitoring network traffic", "Detecting malware signatures", "Finding weak passwords"],
                "answer": 0
        },
        {
                "q": "<b>55.</b> What is biometric access control?",
                "options": ["Using physical characteristics for entry", "Using complex passwords", "Using security guards", "Using metal detectors"],
                "answer": 0
        },
        {
                "q": "<b>56.</b> What is WPA3?",
                "options": ["Latest Wi-Fi security protocol", "Wireless power adapter", "Wired network standard", "Web application framework"],
                "answer": 0
        },
        {
                "q": "<b>57.</b> What is evil twin attack?",
                "options": ["Rogue Wi-Fi access point", "Duplicate computer system", "Cloned mobile device", "Fake security certificate"],
                "answer": 0
        },
        {
                "q": "<b>58.</b> What is war driving?",
                "options": ["Searching for wireless networks", "Hacking moving vehicles", "Attacking automotive systems", "Securing transportation networks"],
                "answer": 0
        },
        {
                "q": "<b>59.</b> What is Bluetooth pairing security risk?",
                "options": ["Unauthorized device connection", "Signal interference", "Battery drainage", "Data speed reduction"],
                "answer": 0
        },
        {
                "q": "<b>60.</b> What is NFC security concern?",
                "options": ["Short-range data interception", "Long-distance tracking", "Battery exploitation", "Hardware damage"],
                "answer": 0
        },
        {
                "q": "<b>61.</b> What is penetration testing?",
                "options": ["Authorized simulated cyber attacks", "Network performance testing", "Software quality assurance", "Hardware stress testing"],
                "answer": 0
        },
        {
                "q": "<b>62.</b> What is vulnerability scanning?",
                "options": ["Automated detection of security weaknesses", "Manual code review", "Network speed testing", "Hardware inspection"],
                "answer": 0
        },
        {
                "q": "<b>63.</b> What is CVE?",
                "options": ["Common Vulnerabilities and Exposures", "Critical Vulnerability Evaluation", "Certified Vulnerability Expert", "Common Virus Encyclopedia"],
                "answer": 0
        },
        {
                "q": "<b>64.</b> What is patch management?",
                "options": ["Installing software updates", "Managing network cables", "Patching physical holes", "Fixing hardware defects"],
                "answer": 0
        },
        {
                "q": "<b>65.</b> What is security hardening?",
                "options": ["Reducing system attack surface", "Increasing system performance", "Adding more user features", "Expanding network capacity"],
                "answer": 0
        },
        {
                "q": "<b>66.</b> What is data classification?",
                "options": ["Categorizing data by sensitivity", "Organizing data alphabetically", "Sorting data by size", "Arranging data chronologically"],
                "answer": 0
        },
        {
                "q": "<b>67.</b> What is data loss prevention (DLP)?",
                "options": ["Preventing unauthorized data exposure", "Recovering lost data", "Creating data backups", "Encrypting all data"],
                "answer": 0
        },
        {
                "q": "<b>68.</b> What is data masking?",
                "options": ["Hiding sensitive data in copies", "Encrypting production data", "Deleting old data", "Compressing large files"],
                "answer": 0
        },
        {
                "q": "<b>69.</b> What is data retention policy?",
                "options": ["Rules for how long to keep data", "Methods for data backup", "Procedures for data entry", "Guidelines for data sharing"],
                "answer": 0
        },
        {
                "q": "<b>70.</b> What is data sovereignty?",
                "options": ["Data subject to laws of country where stored", "Data ownership rights", "Data quality standards", "Data access controls"],
                "answer": 0
        },
        {
                "q": "<b>71.</b> What is defense in depth?",
                "options": ["Multiple layers of security controls", "Single strong security barrier", "Redundant backup systems", "Multiple internet connections"],
                "answer": 0
        },
        {
                "q": "<b>72.</b> What is zero trust architecture?",
                "options": ["Verify explicitly, never trust implicitly", "Trust internal networks automatically", "Block all external access", "Allow all encrypted traffic"],
                "answer": 0
        },
        {
                "q": "<b>73.</b> What is microsegmentation?",
                "options": ["Dividing network into small secure zones", "Splitting large files", "Distributing processing load", "Separating user groups"],
                "answer": 0
        },
        {
                "q": "<b>74.</b> What is SOAR?",
                "options": ["Security Orchestration, Automation and Response", "System Operations and Recovery", "Security Operations and Analysis Reporting", "Secure Online Authentication and Routing"],
                "answer": 0
        },
        {
                "q": "<b>75.</b> What is SASE?",
                "options": ["Secure Access Service Edge", "Security Assessment and System Evaluation", "System Authentication and Security Encryption", "Secure Application Service Environment"],
                "answer": 0
        },
        {
                "q": "<b>76.</b> What is SPF?",
                "options": ["Sender Policy Framework", "Secure Password Filter", "Spam Prevention Filter", "System Protection Firewall"],
                "answer": 0
        },
        {
                "q": "<b>77.</b> What is DKIM?",
                "options": ["DomainKeys Identified Mail", "Digital Key Identity Management", "Data Key Infrastructure Method", "Domain Knowledge and Information Management"],
                "answer": 0
        },
        {
                "q": "<b>78.</b> What is DMARC?",
                "options": ["Domain-based Message Authentication, Reporting &amp; Conformance", "Digital Message Authentication and Routing Control", "Data Malware Analysis and Response Center", "Domain Management and Access Rights Control"],
                "answer": 0
        },
        {
                "q": "<b>79.</b> What is email encryption?",
                "options": ["Protecting email content from reading", "Compressing email attachments", "Verifying email senders", "Blocking spam emails"],
                "answer": 0
        },
        {
                "q": "<b>80.</b> What is email filtering?",
                "options": ["Blocking malicious/suspicious emails", "Organizing emails by date", "Sorting emails by sender", "Archiving old emails"],
                "answer": 0
        },
        {
                "q": "<b>81.</b> What is SOC?",
                "options": ["Security Operations Center", "System Operations Control", "Security Oversight Committee", "System Optimization Center"],
                "answer": 0
        },
        {
                "q": "<b>82.</b> What is threat intelligence?",
                "options": ["Information about cyber threats", "Data about system performance", "Reports on user behavior", "Analysis of network speed"],
                "answer": 0
        },
        {
                "q": "<b>83.</b> What is IOC?",
                "options": ["Indicator of Compromise", "Internet Operations Center", "Incident Operations Command", "International Organization for Cybersecurity"],
                "answer": 0
        },
        {
                "q": "<b>84.</b> What is security monitoring?",
                "options": ["Continuous observation for threats", "Periodic security audits", "Annual risk assessments", "Quarterly vulnerability scans"],
                "answer": 0
        },
        {
                "q": "<b>85.</b> What is UEBA?",
                "options": ["User and Entity Behavior Analytics", "Unified Endpoint Backup and Archiving", "Universal Encryption and Biometric Authentication", "User Email Behavior Analysis"],
                "answer": 0
        },
        {
                "q": "<b>86.</b> What is SAST?",
                "options": ["Static Application Security Testing", "System Application Stress Testing", "Secure Access Service Technology", "Security Assessment and Scanning Tool"],
                "answer": 0
        },
        {
                "q": "<b>87.</b> What is DAST?",
                "options": ["Dynamic Application Security Testing", "Data Access Security Technology", "Digital Authentication System Testing", "Database Administration Security Tool"],
                "answer": 0
        },
        {
                "q": "<b>88.</b> What is IAST?",
                "options": ["Interactive Application Security Testing", "Internet Application Stress Testing", "Integrated Authentication Security Technology", "International Application Security Standard"],
                "answer": 0
        },
        {
                "q": "<b>89.</b> What is secure SDLC?",
                "options": ["Integrating security throughout development lifecycle", "Adding security at end of development", "Testing security after deployment", "Outsourcing security testing"],
                "answer": 0
        },
        {
                "q": "<b>90.</b> What is OWASP?",
                "options": ["Open Web Application Security Project", "Organization for Web Application Standards and Protocols", "Official Web Authentication Security Process", "Online Web Application Scanning Program"],
                "answer": 0
        },
        {
                "q": "<b>91.</b> What is IAM?",
                "options": ["Identity and Access Management", "Internet Access Monitoring", "Internal Authentication Method", "International Access Management"],
                "answer": 0
        },
        {
                "q": "<b>92.</b> What is PAM?",
                "options": ["Privileged Access Management", "Personal Authentication Method", "Public Access Monitoring", "Protected Account Management"],
                "answer": 0
        },
        {
                "q": "<b>93.</b> What is federated identity?",
                "options": ["Single identity across multiple systems", "Multiple identities for one user", "Anonymous access to systems", "Temporary access credentials"],
                "answer": 0
        },
        {
                "q": "<b>94.</b> What is directory services?",
                "options": ["Centralized user information database", "File organization system", "Network routing tables", "Security policy repository"],
                "answer": 0
        },
        {
                "q": "<b>95.</b> What is JIT access?",
                "options": ["Just-In-Time privileged access", "Joint International Telecommunications", "Journaled Incident Tracking", "Java Integration Technology"],
                "answer": 0
        },
        {
                "q": "<b>96.</b> What is RTO?",
                "options": ["Recovery Time Objective", "Real-Time Operations", "Risk Treatment Option", "Response Time Objective"],
                "answer": 0
        },
        {
                "q": "<b>97.</b> What is RPO?",
                "options": ["Recovery Point Objective", "Risk Priority Order", "Response Procedure Outline", "Recovery Process Objective"],
                "answer": 0
        },
        {
                "q": "<b>98.</b> What is BCDR?",
                "options": ["Business Continuity and Disaster Recovery", "Backup and Cyber Defense Response", "Business Cybersecurity and Data Recovery", "Backup Continuity and Disaster Response"],
                "answer": 0
        },
        {
                "q": "<b>99.</b> What is 3-2-1 backup rule?",
                "options": ["3 copies, 2 media types, 1 offsite", "3 locations, 2 backups, 1 administrator", "3 days retention, 2 verification tests, 1 encryption key", "3 backup methods, 2 storage types, 1 recovery plan"],
                "answer": 0
        },
        {
                "q": "<b>100.</b> What is differential backup?",
                "options": ["Backs up changes since last full backup", "Backs up all data every time", "Backs up changes since last backup of any type", "Backs up only system files"],
                "answer": 0
        },
        ],
    },

    # ------------------------------------------------------------------ #
    # 25. Microsoft Office MCQ
    # ------------------------------------------------------------------ #
    {
        "id": 25,
        "slug": "ms-office-mcq",
        "title": "Microsoft Office MCQ",
        "difficulty": "Medium",
        "topics": "Word · Excel · PowerPoint · Outlook".split(" · "),
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p>151 Microsoft Office MCQs from the <b>Microsoft Office MCQ</b> PDF — Word, Excel, PowerPoint and Outlook features and shortcuts.</p>
<p>Select an option for every question, then press <b>Submit</b>. Correct answers
turn green; wrong picks show the right one.</p>
<p style="color:var(--text-dim)">Source PDF is in the <b>PDF Resources</b> section.</p>
""",
        "hint": "Source: KN Academy Microsoft Office MCQ PDF. Submit to see the full answer key; re-attempt any time.",
        "boilerplate": {},
        "samples": [],
        "questions": [
        {
                "q": "<b>1.</b> What is the default file extension of a Word document?",
                "options": [".txt", ".docx", ".pdf", ".xlsx"],
                "answer": 1
        },
        {
                "q": "<b>2.</b> Which shortcut key is used to save a document in Word?",
                "options": ["Ctrl + S", "Ctrl + N", "Ctrl + O", "Ctrl + P"],
                "answer": 0
        },
        {
                "q": "<b>3.</b> What is the purpose of the \"Track Changes\" feature in Word?",
                "options": ["To highlight spelling errors", "To track edits made to a document", "To change the font style", "To insert a table"],
                "answer": 1
        },
        {
                "q": "<b>4.</b> Which ribbon tab contains the \"Header &amp; Footer\" option?",
                "options": ["Home", "Insert", "Page Layout", "View"],
                "answer": 1
        },
        {
                "q": "<b>5.</b> What is the purpose of the \"Mail Merge\" feature in Word?",
                "options": ["To send emails", "To create multiple documents from a template", "To merge two documents into one", "To format text"],
                "answer": 1
        },
        {
                "q": "<b>6.</b> Which feature is used to create a numbered list in Word?",
                "options": ["Bullets", "Numbering", "Multilevel List", "All of the above"],
                "answer": 1
        },
        {
                "q": "<b>7.</b> What is the purpose of the \"Thesaurus\" feature in Word?",
                "options": ["To check grammar", "To find synonyms", "To count words", "To insert images"],
                "answer": 1
        },
        {
                "q": "<b>8.</b> Which shortcut key is used to undo the last action in Word?",
                "options": ["Ctrl + Z", "Ctrl + Y", "Ctrl + X", "Ctrl + C"],
                "answer": 0
        },
        {
                "q": "<b>9.</b> What is the purpose of the \"Styles\" feature in Word?",
                "options": ["To apply consistent formatting", "To insert tables", "To check spelling", "To create charts"],
                "answer": 0
        },
        {
                "q": "<b>10.</b> Which feature is used to split a document into sections?",
                "options": ["Page Break", "Section Break", "Column Break", "All of the above"],
                "answer": 1
        },
        {
                "q": "<b>11.</b> What is the purpose of the \"Find and Replace\" feature in Word?",
                "options": ["To search for text and replace it with another text", "To insert images", "To format text", "To create tables"],
                "answer": 0
        },
        {
                "q": "<b>12.</b> Which ribbon tab contains the \"Table\" option?",
                "options": ["Home", "Insert", "Page Layout", "View"],
                "answer": 1
        },
        {
                "q": "<b>13.</b> What is the purpose of the \"Watermark\" feature in Word?",
                "options": ["To add a background image or text", "To insert a table", "To format text", "To check spelling"],
                "answer": 0
        },
        {
                "q": "<b>14.</b> Which shortcut key is used to print a document in Word?",
                "options": ["Ctrl + P", "Ctrl + S", "Ctrl + N", "Ctrl + O"],
                "answer": 0
        },
        {
                "q": "<b>15.</b> What is the purpose of the \"Table of Contents\" feature in Word?",
                "options": ["To list the headings and subheadings in a document", "To insert a table", "To format text", "To check spelling"],
                "answer": 0
        },
        {
                "q": "<b>16.</b> Which feature is used to align text to both the left and right margins?",
                "options": ["Left Align", "Center Align", "Right Align", "Justify"],
                "answer": 3
        },
        {
                "q": "<b>17.</b> What is the purpose of the \"Word Count\" feature in Word?",
                "options": ["To count the number of words in a document", "To check spelling", "To format text", "To insert images"],
                "answer": 0
        },
        {
                "q": "<b>18.</b> Which ribbon tab contains the \"Page Borders\" option?",
                "options": ["Home", "Insert", "Page Layout", "View"],
                "answer": 2
        },
        {
                "q": "<b>19.</b> What is the purpose of the \"Drop Cap\" feature in Word?",
                "options": ["To create a large capital letter at the beginning of a paragraph", "To insert a table", "To format text", "To check spelling"],
                "answer": 0
        },
        {
                "q": "<b>20.</b> Which shortcut key is used to copy text in Word?",
                "options": ["Ctrl + C", "Ctrl + X", "Ctrl + V", "Ctrl + Z"],
                "answer": 0
        },
        {
                "q": "<b>21.</b> What is the purpose of the \"Columns\" feature in Word?",
                "options": ["To divide text into multiple columns", "To insert a table", "To format text", "To check spelling"],
                "answer": 0
        },
        {
                "q": "<b>22.</b> Which ribbon tab contains the \"SmartArt\" option?",
                "options": ["Home", "Insert", "Page Layout", "View"],
                "answer": 1
        },
        {
                "q": "<b>23.</b> What is the purpose of the \"Footnotes\" feature in Word?",
                "options": ["To add notes at the bottom of a page", "To insert a table", "To format text", "To check spelling"],
                "answer": 0
        },
        {
                "q": "<b>24.</b> Which shortcut key is used to paste text in Word?",
                "options": ["Ctrl + V", "Ctrl + X", "Ctrl + C", "Ctrl + Z"],
                "answer": 0
        },
        {
                "q": "<b>25.</b> What is the purpose of the \"Hyperlink\" feature in Word?",
                "options": ["To link to a webpage or another document", "To insert a table", "To format text", "To check spelling"],
                "answer": 0
        },
        {
                "q": "<b>26.</b> Which feature is used to create a bulleted list in Word?",
                "options": ["Bullets", "Numbering", "Multilevel List", "All of the above"],
                "answer": 0
        },
        {
                "q": "<b>27.</b> What is the purpose of the \"Spelling &amp; Grammar\" feature in Word?",
                "options": ["To check spelling and grammar errors", "To insert images", "To format text", "To create tables"],
                "answer": 0
        },
        {
                "q": "<b>28.</b> Which ribbon tab contains the \"Page Color\" option?",
                "options": ["Home", "Insert", "Page Layout", "View"],
                "answer": 2
        },
        {
                "q": "<b>29.</b> What is the purpose of the \"Cover Page\" feature in Word?",
                "options": ["To add a pre-designed cover page to a document", "To insert a table", "To format text", "To check spelling"],
                "answer": 0
        },
        {
                "q": "<b>30.</b> Which shortcut key is used to select all text in Word?",
                "options": ["Ctrl + A", "Ctrl + S", "Ctrl + N", "Ctrl + O"],
                "answer": 0
        },
        {
                "q": "<b>31.</b> What is the purpose of the \"Page Break\" feature in Word?",
                "options": ["To start a new page", "To insert a table", "To format text", "To check spelling"],
                "answer": 0
        },
        {
                "q": "<b>32.</b> Which ribbon tab contains the \"Shapes\" option?",
                "options": ["Home", "Insert", "Page Layout", "View"],
                "answer": 1
        },
        {
                "q": "<b>33.</b> What is the purpose of the \"Text Box\" feature in Word?",
                "options": ["To insert a box for text", "To insert a table", "To format text", "To check spelling"],
                "answer": 0
        },
        {
                "q": "<b>34.</b> Which shortcut key is used to bold text in Word?",
                "options": ["Ctrl + B", "Ctrl + I", "Ctrl + U", "Ctrl + S"],
                "answer": 0
        },
        {
                "q": "<b>35.</b> What is the purpose of the \"Page Margins\" feature in Word?",
                "options": ["To set the margins of a page", "To insert a table", "To format text", "To check spelling"],
                "answer": 0
        },
        {
                "q": "<b>36.</b> Which ribbon tab contains the \"WordArt\" option?",
                "options": ["Home", "Insert", "Page Layout", "View"],
                "answer": 1
        },
        {
                "q": "<b>37.</b> What is the purpose of the \"Table of Authorities\" feature in Word?",
                "options": ["To create a list of references in a legal document", "To insert a table", "To format text", "To check spelling"],
                "answer": 0
        },
        {
                "q": "<b>38.</b> Which shortcut key is used to italicize text in Word?",
                "options": ["Ctrl + I", "Ctrl + B", "Ctrl + U", "Ctrl + S"],
                "answer": 0
        },
        {
                "q": "<b>39.</b> What is the purpose of the \"Page Orientation\" feature in Word?",
                "options": ["To set the page to portrait or landscape", "To insert a table", "To format text", "To check spelling"],
                "answer": 0
        },
        {
                "q": "<b>40.</b> Which ribbon tab contains the \"Equation\" option?",
                "options": ["Home", "Insert", "Page Layout", "View"],
                "answer": 1
        },
        {
                "q": "<b>41.</b> What is the purpose of the \"Index\" feature in Word?",
                "options": ["To create an index of terms in a document", "To insert a table", "To format text", "To check spelling"],
                "answer": 0
        },
        {
                "q": "<b>42.</b> Which shortcut key is used to underline text in Word?",
                "options": ["Ctrl + U", "Ctrl + B", "Ctrl + I", "Ctrl + S"],
                "answer": 0
        },
        {
                "q": "<b>43.</b> What is the purpose of the \"Page Size\" feature in Word?",
                "options": ["To set the size of the page", "To insert a table", "To format text", "To check spelling"],
                "answer": 0
        },
        {
                "q": "<b>44.</b> Which ribbon tab contains the \"Symbol\" option?",
                "options": ["Home", "Insert", "Page Layout", "View"],
                "answer": 1
        },
        {
                "q": "<b>45.</b> What is the purpose of the \"Bibliography\" feature in Word?",
                "options": ["To create a list of references in a document", "To insert a table", "To format text", "To check spelling"],
                "answer": 0
        },
        {
                "q": "<b>46.</b> Which shortcut key is used to open a new document in Word?",
                "options": ["Ctrl + N", "Ctrl + S", "Ctrl + O", "Ctrl + P"],
                "answer": 0
        },
        {
                "q": "<b>47.</b> What is the purpose of the \"Page Numbers\" feature in Word?",
                "options": ["To add page numbers to a document", "To insert a table", "To format text", "To check spelling"],
                "answer": 0
        },
        {
                "q": "<b>48.</b> Which ribbon tab contains the \"Chart\" option?",
                "options": ["Home", "Insert", "Page Layout", "View"],
                "answer": 1
        },
        {
                "q": "<b>49.</b> What is the purpose of the \"Caption\" feature in Word?",
                "options": ["To add captions to images or tables", "To insert a table", "To format text", "To check spelling"],
                "answer": 0
        },
        {
                "q": "<b>50.</b> Which shortcut key is used to open an existing document in Word?",
                "options": ["Ctrl + O", "Ctrl + S", "Ctrl + N", "Ctrl + P"],
                "answer": 0
        },
        {
                "q": "<b>51.</b> What is the default file extension for an Excel workbook?",
                "options": [".xls", ".csv", ".xlsx", ".docx"],
                "answer": 2
        },
        {
                "q": "<b>52.</b> What is the default file extension of a PowerPoint presentation in Office 365?",
                "options": [".ppt", ".pptx", ".ppx", ".ptx"],
                "answer": 1
        },
        {
                "q": "<b>53.</b> Which of the following is NOT a PowerPoint view?",
                "options": ["Slide Sorter", "Notes Page", "Design View", "Slide Show"],
                "answer": 2
        },
        {
                "q": "<b>54.</b> Which key is used to start the slideshow from the beginning?",
                "options": ["F2", "F5", "F7", "Esc"],
                "answer": 1
        },
        {
                "q": "<b>55.</b> Which feature is used to apply consistent formatting across slides?",
                "options": ["Slide Master", "Slide Sorter", "Animations", "SmartArt"],
                "answer": 0
        },
        {
                "q": "<b>56.</b> What is the function of the \"Slide Sorter\" view?",
                "options": ["To edit slide content", "To rearrange slides", "To insert animations", "To add speaker notes"],
                "answer": 1
        },
        {
                "q": "<b>57.</b> Which tab in PowerPoint is used to change the theme of a presentation?",
                "options": ["Home", "Insert", "Design", "View"],
                "answer": 2
        },
        {
                "q": "<b>58.</b> What is the purpose of Slide Layouts?",
                "options": ["To rearrange slides", "To control the design of a slide", "To change slide backgrounds", "To animate slides"],
                "answer": 1
        },
        {
                "q": "<b>59.</b> How can you add a new slide to a presentation?",
                "options": ["Press Ctrl + N", "Go to Insert &gt; New Slide", "Go to Design &gt; New Slide", "Press Ctrl + X"],
                "answer": 1
        },
        {
                "q": "<b>60.</b> Which feature allows you to reuse slides from another presentation?",
                "options": ["Duplicate Slide", "Reuse Slides", "Slide Transition", "Merge Slides"],
                "answer": 1
        },
        {
                "q": "<b>61.</b> Which of the following is NOT a slide layout option?",
                "options": ["Title Slide", "Two Content", "Blank", "Watermark"],
                "answer": 3
        },
        {
                "q": "<b>62.</b> Which tab contains the \"Transitions\" feature?",
                "options": ["Home", "Insert", "Animations", "Transitions"],
                "answer": 3
        },
        {
                "q": "<b>63.</b> What is the difference between animations and transitions in PowerPoint?",
                "options": ["Animations apply to entire slides, transitions apply to objects", "Animations apply to objects, transitions apply between slides", "Both are the same", "Transitions apply to text only"],
                "answer": 1
        },
        {
                "q": "<b>64.</b> Which effect is NOT a type of animation in PowerPoint?",
                "options": ["Entrance", "Emphasis", "Exit", "Transition"],
                "answer": 3
        },
        {
                "q": "<b>65.</b> Which shortcut key is used to apply animation in PowerPoint?",
                "options": ["Shift + A", "Alt + A", "Ctrl + A", "No shortcut available"],
                "answer": 1
        },
        {
                "q": "<b>66.</b> Which of the following is NOT a transition effect?",
                "options": ["Fade", "Wipe", "Morph", "Reverse"],
                "answer": 3
        },
        {
                "q": "<b>67.</b> Which feature is used to insert a video in PowerPoint?",
                "options": ["Insert &gt; Video", "Design &gt; Video", "Animation &gt; Video", "File &gt; Import Video"],
                "answer": 0
        },
        {
                "q": "<b>68.</b> Which format is supported for inserting videos in PowerPoint?",
                "options": [".mp4", ".mov", ".avi", "All of the above"],
                "answer": 3
        },
        {
                "q": "<b>69.</b> What is SmartArt used for?",
                "options": ["Creating tables", "Creating diagrams", "Creating animations", "Formatting slides"],
                "answer": 1
        },
        {
                "q": "<b>70.</b> Which tab contains the option to insert a chart in PowerPoint?",
                "options": ["Insert", "Design", "Animations", "View"],
                "answer": 0
        },
        {
                "q": "<b>71.</b> How can you add a hyperlink to text in PowerPoint?",
                "options": ["Insert &gt; Hyperlink", "Design &gt; Link", "Animations &gt; Hyperlink", "View &gt; Insert Link"],
                "answer": 0
        },
        {
                "q": "<b>72.</b> Which feature allows PowerPoint to generate slides automatically from an outline?",
                "options": ["AutoFormat", "Slide Layouts", "Outline View", "Smart Slide Generator"],
                "answer": 2
        },
        {
                "q": "<b>73.</b> What is the purpose of \"Presenter View\" in PowerPoint?",
                "options": ["To present slides with extra controls for the presenter", "To create slides", "To edit slides", "To add animations"],
                "answer": 0
        },
        {
                "q": "<b>74.</b> How can you print handouts in PowerPoint?",
                "options": ["File &gt; Print &gt; Handouts", "Design &gt; Print", "View &gt; Print", "Slide Show &gt; Print"],
                "answer": 0
        },
        {
                "q": "<b>75.</b> Which PowerPoint feature allows multiple people to work on the same presentation online?",
                "options": ["PowerPoint Sync", "PowerPoint Co-Authoring", "PowerPoint Cloud", "PowerPoint Merge"],
                "answer": 1
        },
        {
                "q": "<b>76.</b> Which feature automatically adjusts text size to fit within a text box?",
                "options": ["AutoFit", "Smart Text", "Word Wrap", "Text Shrink"],
                "answer": 0
        },
        {
                "q": "<b>77.</b> Which PowerPoint feature allows you to time your presentation slides automatically?",
                "options": ["AutoPlay", "Rehearse Timings", "Slide Sorter", "Animation Pane"],
                "answer": 1
        },
        {
                "q": "<b>78.</b> Which shortcut key is used to insert a new slide in PowerPoint?",
                "options": ["Ctrl + N", "Ctrl + M", "Ctrl + S", "Ctrl + P"],
                "answer": 1
        },
        {
                "q": "<b>79.</b> Which file format is used to save a PowerPoint presentation as a video?",
                "options": [".ppt", ".mp4", ".pdf", ".xlsx"],
                "answer": 1
        },
        {
                "q": "<b>80.</b> Which PowerPoint feature allows you to apply a consistent look across multiple slides?",
                "options": ["Slide Layout", "Slide Master", "Animation Pane", "Format Painter"],
                "answer": 1
        },
        {
                "q": "<b>81.</b> Which option allows you to display PowerPoint slides in a continuous loop?",
                "options": ["Slide Show &gt; Set Up Slide Show", "View &gt; Slide Master", "Transitions &gt; Loop", "File &gt; Options"],
                "answer": 0
        },
        {
                "q": "<b>82.</b> Which PowerPoint feature allows you to apply artistic effects to images?",
                "options": ["Picture Effects", "SmartArt", "Slide Master", "Table Tools"],
                "answer": 0
        },
        {
                "q": "<b>83.</b> Which feature allows you to copy formatting from one object to another?",
                "options": ["Format Painter", "Slide Master", "Design Mode", "Shape Effects"],
                "answer": 0
        },
        {
                "q": "<b>84.</b> How can you group multiple objects together in PowerPoint?",
                "options": ["Select objects &gt; Right-click &gt; Group", "Select objects &gt; Press Ctrl + G", "Both A and B", "PowerPoint does not support grouping"],
                "answer": 2
        },
        {
                "q": "<b>85.</b> Which tool is used to adjust the alignment of text within a text box?",
                "options": ["Paragraph Alignment", "WordArt", "Animation Pane", "Slide Layout"],
                "answer": 0
        },
        {
                "q": "<b>86.</b> Which tab allows you to change the slide background?",
                "options": ["Home", "Design", "Insert", "View"],
                "answer": 1
        },
        {
                "q": "<b>87.</b> Which PowerPoint feature allows you to navigate to another slide, document, or webpage?",
                "options": ["Hyperlink", "SmartArt", "Slide Transition", "None of the above"],
                "answer": 0
        },
        {
                "q": "<b>88.</b> Which tab contains the option to add an audio file to a slide?",
                "options": ["Insert", "Design", "View", "Transitions"],
                "answer": 0
        },
        {
                "q": "<b>89.</b> Which PowerPoint feature allows you to insert an action button to navigate slides?",
                "options": ["Slide Sorter", "Action Buttons", "Animations", "Rehearse Timings"],
                "answer": 1
        },
        {
                "q": "<b>90.</b> Which file format is used to save a PowerPoint presentation as a PDF?",
                "options": [".pptx", ".pdf", ".mp4", ".txt"],
                "answer": 1
        },
        {
                "q": "<b>91.</b> Which option helps to trim a video within PowerPoint?",
                "options": ["Playback tab &gt; Trim Video", "Insert tab &gt; Video", "Design tab &gt; Format", "None of the above"],
                "answer": 0
        },
        {
                "q": "<b>92.</b> Which PowerPoint feature allows multiple users to edit a presentation at the same time?",
                "options": ["Slide Master", "Co-Authoring", "Slide Sorter", "Presenter View"],
                "answer": 1
        },
        {
                "q": "<b>93.</b> Which cloud service is integrated with PowerPoint for online collaboration?",
                "options": ["Dropbox", "Google Drive", "OneDrive", "iCloud"],
                "answer": 2
        },
        {
                "q": "<b>94.</b> Which option allows you to protect a presentation with a password?",
                "options": ["File &gt; Save As &gt; Encrypt", "File &gt; Info &gt; Protect Presentation", "View &gt; Security Settings", "None of the above"],
                "answer": 1
        },
        {
                "q": "<b>95.</b> Which PowerPoint feature allows you to broadcast a presentation online?",
                "options": ["Slide Show Broadcast", "Web Viewer", "PowerPoint Live", "Presenter Mode"],
                "answer": 2
        },
        {
                "q": "<b>96.</b> How can you track changes in a shared PowerPoint file?",
                "options": ["Review tab &gt; Track Changes", "View tab &gt; Change Tracker", "File tab &gt; History", "PowerPoint does not support tracking changes"],
                "answer": 2
        },
        {
                "q": "<b>97.</b> Which shortcut key is used to close PowerPoint?",
                "options": ["Alt + F4", "Ctrl + Q", "Ctrl + W", "Shift + Esc"],
                "answer": 0
        },
        {
                "q": "<b>98.</b> Which PowerPoint feature allows you to record narration for your slides?",
                "options": ["Slide Notes", "Record Slide Show", "Presenter View", "Audio Overlay"],
                "answer": 1
        },
        {
                "q": "<b>99.</b> Which command is used to export a PowerPoint as an image?",
                "options": ["File &gt; Export &gt; Save as Pictures", "Insert &gt; Screenshot", "File &gt; Save As &gt; PNG", "Both A and C"],
                "answer": 3
        },
        {
                "q": "<b>100.</b> Which view is best for organizing slides and rearranging their order?",
                "options": ["Normal View", "Slide Sorter View", "Presenter View", "Outline View"],
                "answer": 1
        },
        {
                "q": "<b>101.</b> Which feature is used to rehearse a presentation with automatic timing?",
                "options": ["Slide Show &gt; Rehearse Timings", "Animation &gt; Timings", "Slide Show &gt; Presenter View", "Transitions &gt; AutoPlay"],
                "answer": 0
        },
        {
                "q": "<b>102.</b> What is the primary function of Microsoft Outlook?",
                "options": ["Web browsing", "Email communication", "Video editing", "File compression"],
                "answer": 1
        },
        {
                "q": "<b>103.</b> Which protocol is used by Outlook to send emails?",
                "options": ["POP3", "IMAP", "SMTP", "FTP"],
                "answer": 2
        },
        {
                "q": "<b>104.</b> Which protocol allows Outlook to retrieve emails from a mail server?",
                "options": ["SMTP", "IMAP", "POP3", "Both b and c"],
                "answer": 3
        },
        {
                "q": "<b>105.</b> What is the default file format for Outlook data files?",
                "options": [".pst", ".xls", ".docx", ".pdf"],
                "answer": 0
        },
        {
                "q": "<b>106.</b> Which Outlook feature allows you to schedule meetings and appointments?",
                "options": ["Tasks", "Calendar", "Contacts", "Notes"],
                "answer": 1
        },
        {
                "q": "<b>107.</b> Which feature helps in organizing emails automatically in Outlook?",
                "options": ["Rules", "Junk Mail", "Folders", "Search Bar"],
                "answer": 0
        },
        {
                "q": "<b>108.</b> Which Outlook feature is used to recall an email after sending?",
                "options": ["Undo Send", "Message Recall", "Drafts", "Archive"],
                "answer": 1
        },
        {
                "q": "<b>109.</b> Which Outlook folder stores unsent emails?",
                "options": ["Drafts", "Sent Items", "Junk Email", "Outbox"],
                "answer": 3
        },
        {
                "q": "<b>110.</b> Which folder stores deleted emails before they are permanently removed?",
                "options": ["Inbox", "Junk Mail", "Trash/Deleted Items", "Sent Items"],
                "answer": 2
        },
        {
                "q": "<b>111.</b> Which feature helps to send the same email to multiple recipients without them seeing each other’s email addresses?",
                "options": ["CC (Carbon Copy)", "BCC (Blind Carbon Copy)", "Reply All", "Forward"],
                "answer": 1
        },
        {
                "q": "<b>112.</b> Which Outlook feature allows you to create reminders for important tasks?",
                "options": ["Notes", "Calendar Alerts", "Mail Filters", "Rules"],
                "answer": 1
        },
        {
                "q": "<b>113.</b> Which scheduling feature in Outlook lets you check attendees’ availability?",
                "options": ["Meeting Planner", "Scheduling Assistant", "Task Manager", "Shared Calendar"],
                "answer": 1
        },
        {
                "q": "<b>114.</b> What does the \"Tentative\" status indicate in Outlook Calendar?",
                "options": ["The meeting is confirmed", "The recipient might attend", "The meeting is canceled", "The recipient declined the invitation"],
                "answer": 1
        },
        {
                "q": "<b>115.</b> Which Outlook feature allows others to see your schedule?",
                "options": ["Shared Calendar", "Outlook Tasks", "Email Rules", "Quick Steps"],
                "answer": 0
        },
        {
                "q": "<b>116.</b> Which Outlook feature allows you to add public holidays automatically?",
                "options": ["Calendar Tools", "Import Calendar", "Add Holidays", "Recurring Events"],
                "answer": 2
        },
        {
                "q": "<b>117.</b> Which tab in Outlook is used to create a new contact?",
                "options": ["File", "Home", "Contacts", "People"],
                "answer": 3
        },
        {
                "q": "<b>118.</b> Which feature allows you to store multiple email addresses for a contact?",
                "options": ["Address Book", "Contact Groups", "Distribution List", "People Pane"],
                "answer": 0
        },
        {
                "q": "<b>119.</b> Which option is used to send an email to a predefined group of people?",
                "options": ["Contact Group", "CC", "BCC", "Rules"],
                "answer": 0
        },
        {
                "q": "<b>120.</b> Where can you store additional notes about a contact?",
                "options": ["Notes Section", "Calendar", "Tasks", "Journal"],
                "answer": 0
        },
        {
                "q": "<b>121.</b> Which feature in Outlook helps in merging duplicate contacts?",
                "options": ["Find and Merge Contacts", "Address Book Cleaner", "People Pane", "Contact Group"],
                "answer": 0
        },
        {
                "q": "<b>122.</b> Which Outlook feature allows you to delay the delivery of an email?",
                "options": ["Delay Send", "Schedule Email", "Outbox Hold", "Postpone Send"],
                "answer": 0
        },
        {
                "q": "<b>123.</b> Which shortcut key is used to send an email in Outlook?",
                "options": ["Ctrl + S", "Alt + Enter", "Ctrl + Enter", "Shift + Enter"],
                "answer": 2
        },
        {
                "q": "<b>124.</b> Which Outlook feature helps in managing spam or unwanted emails?",
                "options": ["Junk Mail Filter", "Email Archiving", "Contact List", "Auto Reply"],
                "answer": 0
        },
        {
                "q": "<b>125.</b> Which Outlook feature automatically organizes emails based on priority?",
                "options": ["Focused Inbox", "Quick Steps", "Clutter", "AutoArchive"],
                "answer": 0
        },
        {
                "q": "<b>126.</b> Which file format is used to export Outlook emails?",
                "options": [".ost", ".csv", ".pdf", ".xml"],
                "answer": 1
        },
        {
                "q": "<b>127.</b> Which Microsoft cloud service is integrated with Outlook?",
                "options": ["OneDrive", "SharePoint", "Teams", "All of the above"],
                "answer": 3
        },
        {
                "q": "<b>128.</b> Which feature encrypts Outlook emails for security?",
                "options": ["Secure Mail", "Digital Signature", "Encrypted Mail", "Both b and c"],
                "answer": 3
        },
        {
                "q": "<b>129.</b> Which tool allows you to back up and restore Outlook emails?",
                "options": ["Import/Export Wizard", "Archive Manager", "Backup Manager", "None of the above"],
                "answer": 0
        },
        {
                "q": "<b>130.</b> Which shortcut key is used to reply to all recipients in an email?",
                "options": ["Ctrl + R", "Ctrl + Shift + R", "Ctrl + F", "Alt + R"],
                "answer": 1
        },
        {
                "q": "<b>131.</b> Which Outlook feature automatically replies to emails when you are unavailable?",
                "options": ["Auto Forward", "Out of Office Reply", "Smart Reply", "Email Redirect"],
                "answer": 1
        },
        {
                "q": "<b>132.</b> Which Outlook feature allows you to categorize emails by color for better organization?",
                "options": ["Quick Steps", "Conditional Formatting", "Color Categories", "Focused Inbox"],
                "answer": 2
        },
        {
                "q": "<b>133.</b> Which tool in Outlook allows you to search for specific emails quickly?",
                "options": ["Email Filters", "Search Bar", "Advanced Find", "Both b and c"],
                "answer": 3
        },
        {
                "q": "<b>134.</b> What happens when you \"Flag\" an email in Outlook?",
                "options": ["It is marked as spam", "It is deleted automatically", "It is marked for follow-up", "It moves to the Archive folder"],
                "answer": 2
        },
        {
                "q": "<b>135.</b> Which Outlook feature helps reduce the size of your mailbox by moving older emails to another location?",
                "options": ["Junk Mail Filter", "AutoArchive", "Email Rules", "Focused Inbox"],
                "answer": 1
        },
        {
                "q": "<b>136.</b> Which feature allows you to view all unread emails quickly in Outlook?",
                "options": ["Search Folder", "Junk Mail Folder", "Drafts", "Outbox"],
                "answer": 0
        },
        {
                "q": "<b>137.</b> Which Outlook feature allows you to attach large files using cloud storage?",
                "options": ["File Explorer", "OneDrive Integration", "Mail Merge", "Attachment Resizer"],
                "answer": 1
        },
        {
                "q": "<b>138.</b> What is the maximum attachment size for an Outlook email (without cloud storage)?",
                "options": ["10 MB", "20 MB", "25 MB", "50 MB"],
                "answer": 2
        },
        {
                "q": "<b>139.</b> Which feature in Outlook allows you to preview attachments without opening them?",
                "options": ["File Explorer", "Attachment Preview", "Quick View", "Inline Viewer"],
                "answer": 1
        },
        {
                "q": "<b>140.</b> Which action should you take to attach a file from your computer to an email?",
                "options": ["Drag and drop the file", "Click on \"Insert\" → \"Attach File\"", "Copy-paste the file into the email body", "All of the above"],
                "answer": 3
        },
        {
                "q": "<b>141.</b> Which file formats are blocked by Outlook for security reasons?",
                "options": [".exe", ".bat", ".vbs", "All of the above"],
                "answer": 3
        },
        {
                "q": "<b>142.</b> What does a \"Read Receipt\" in Outlook do?",
                "options": ["Confirms that an email has been read", "Confirms that an email has been delivered", "Both a and b", "None of the above"],
                "answer": 0
        },
        {
                "q": "<b>143.</b> Which feature in Outlook allows you to know when an email is delivered to the recipient’s mailbox?",
                "options": ["Delivery Report", "Read Receipt", "Tracking Options", "Follow-up Flags"],
                "answer": 0
        },
        {
                "q": "<b>144.</b> Which Outlook feature allows you to track responses from multiple recipients?",
                "options": ["Polls", "Voting Buttons", "Quick Steps", "Contact Groups"],
                "answer": 1
        },
        {
                "q": "<b>145.</b> How can you check if an email you sent has been opened in Outlook?",
                "options": ["Request a Read Receipt", "Request a Delivery Receipt", "Check Sent Items", "Use Tracking Options"],
                "answer": 0
        },
        {
                "q": "<b>146.</b> Which email setting ensures that you receive confirmation when an email is successfully delivered?",
                "options": ["Read Receipt", "Delivery Receipt", "Auto Forward", "Encryption"],
                "answer": 1
        },
        {
                "q": "<b>147.</b> Which feature in Outlook allows you to create email templates for repetitive messages?",
                "options": ["Mail Merge", "Quick Parts", "AutoArchive", "Email Forwarding"],
                "answer": 1
        },
        {
                "q": "<b>148.</b> Which Outlook feature allows you to create automated actions like moving emails to a folder?",
                "options": ["Quick Steps", "Rules", "Filters", "Smart Mailbox"],
                "answer": 1
        },
        {
                "q": "<b>149.</b> Which feature allows you to schedule an email to be sent at a later time?",
                "options": ["Delay Delivery", "Send Later", "Postpone Mail", "Hold for Approval"],
                "answer": 0
        },
        {
                "q": "<b>150.</b> What is the purpose of the \"Focused Inbox\" feature in Outlook?",
                "options": ["To separate important emails from others", "To organize emails based on categories", "To block spam emails", "To create automatic replies"],
                "answer": 0
        },
        {
                "q": "<b>151.</b> Which Outlook feature allows you to create a shortcut for frequently used actions?",
                "options": ["Quick Steps", "Shortcuts Menu", "Macro Manager", "Email Templates"],
                "answer": 0
        },
        ],
    },

    # ------------------------------------------------------------------ #
    # 26. Computer Networks MCQ (Complete)
    # ------------------------------------------------------------------ #
    {
        "id": 26,
        "slug": "cn-mcq-complete",
        "title": "Computer Networks MCQ (Complete)",
        "difficulty": "Medium",
        "topics": "Networking · OSI · TCP/IP".split(" · "),
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p>349 computer-networks MCQs from the <b>CN MCQ Complete</b> PDF — OSI/TCP-IP layers, physical & data-link layer, transport, and advanced topics.</p>
<p>Select an option for every question, then press <b>Submit</b>. Correct answers
turn green; wrong picks show the right one.</p>
<p style="color:var(--text-dim)">Source PDF is in the <b>PDF Resources</b> section.</p>
""",
        "hint": "Source: KN Academy CN MCQ Complete PDF. Submit to see the full answer key; re-attempt any time.",
        "boilerplate": {},
        "samples": [],
        "questions": [
        {
                "q": "<b>1.</b> What is a computer network?",
                "options": ["A single computer system", "Interconnected computing devices for resource sharing", "A type of software", "An internet browser"],
                "answer": 1
        },
        {
                "q": "<b>2.</b> What is the primary purpose of a network?",
                "options": ["To play games", "To share resources and information", "To increase computer speed", "To block viruses"],
                "answer": 1
        },
        {
                "q": "<b>3.</b> What is bandwidth?",
                "options": ["The width of a network cable", "The maximum data transfer rate of a network", "The number of computers on a network", "The strength of a wireless signal"],
                "answer": 1
        },
        {
                "q": "<b>4.</b> What is latency?",
                "options": ["Data transfer speed", "Time delay in data transmission", "Network cable length", "Number of network users"],
                "answer": 1
        },
        {
                "q": "<b>5.</b> What is a node in a network?",
                "options": ["A network cable", "Any device connected to a network", "A software program", "A type of virus"],
                "answer": 1
        },
        {
                "q": "<b>6.</b> What is a protocol?",
                "options": ["A network cable", "Rules governing data communication", "A type of computer virus", "Network hardware"],
                "answer": 1
        },
        {
                "q": "<b>7.</b> What is data packet?",
                "options": ["A large file", "A small unit of data transmitted over a network", "A type of computer", "Network security software"],
                "answer": 1
        },
        {
                "q": "<b>8.</b> What is a router?",
                "options": ["A device that connects different networks", "A device that connects computers in same network", "A type of cable", "Internet browser"],
                "answer": 0
        },
        {
                "q": "<b>9.</b> What is a switch?",
                "options": ["Device that connects different networks", "Device that connects devices within a network", "A type of software", "Wireless access point"],
                "answer": 1
        },
        {
                "q": "<b>10.</b> What is a hub?",
                "options": ["A basic network device that broadcasts data to all ports", "A device that routes data between networks", "A wireless access point", "A network security device"],
                "answer": 0
        },
        {
                "q": "<b>11.</b> What is a LAN?",
                "options": ["A worldwide network", "A network covering a small geographical area", "A wireless network", "A mobile network"],
                "answer": 1
        },
        {
                "q": "<b>12.</b> What is a WAN?",
                "options": ["A small office network", "A network spanning a large geographical area", "A wireless network", "A home network"],
                "answer": 1
        },
        {
                "q": "<b>13.</b> What is a MAN?",
                "options": ["A home network", "A network covering a metropolitan area", "A global network", "A wireless network"],
                "answer": 1
        },
        {
                "q": "<b>14.</b> What is a PAN?",
                "options": ["A global network", "A personal area network for individual use", "An office network", "A city-wide network"],
                "answer": 1
        },
        {
                "q": "<b>15.</b> What is a WLAN?",
                "options": ["A wired network", "A wireless local area network", "A wide area network", "A metropolitan network"],
                "answer": 1
        },
        {
                "q": "<b>16.</b> What is VPN?",
                "options": ["A local network", "A secure private network over public infrastructure", "A wireless network", "A home network"],
                "answer": 1
        },
        {
                "q": "<b>17.</b> What is client-server network?",
                "options": ["All computers are equal", "Centralized servers provide services to client computers", "No central control", "Only wireless connections"],
                "answer": 1
        },
        {
                "q": "<b>18.</b> What is peer-to-peer network?",
                "options": ["All computers act as both clients and servers", "Only one central server", "No file sharing possible", "Requires dedicated hardware"],
                "answer": 0
        },
        {
                "q": "<b>19.</b> What is intranet?",
                "options": ["The global internet", "Private network using internet technologies", "A wireless network", "A mobile network"],
                "answer": 1
        },
        {
                "q": "<b>20.</b> What is extranet?",
                "options": ["Public internet", "Private network extended to authorized external users", "Wireless network", "Home network"],
                "answer": 1
        },
        {
                "q": "<b>21.</b> How many layers does the OSI model have?",
                "options": ["5", "7", "4", "9"],
                "answer": 1
        },
        {
                "q": "<b>22.</b> Which OSI layer handles physical transmission?",
                "options": ["Network Layer", "Physical Layer", "Data Link Layer", "Transport Layer"],
                "answer": 1
        },
        {
                "q": "<b>23.</b> Which layer is responsible for routing?",
                "options": ["Physical Layer", "Network Layer", "Transport Layer", "Application Layer"],
                "answer": 1
        },
        {
                "q": "<b>24.</b> Which layer provides end-to-end delivery?",
                "options": ["Network Layer", "Transport Layer", "Data Link Layer", "Session Layer"],
                "answer": 1
        },
        {
                "q": "<b>25.</b> Which layer handles error detection in frames?",
                "options": ["Physical Layer", "Data Link Layer", "Network Layer", "Transport Layer"],
                "answer": 1
        },
        {
                "q": "<b>26.</b> Which layer establishes, maintains, and terminates sessions?",
                "options": ["Transport Layer", "Session Layer", "Presentation Layer", "Application Layer"],
                "answer": 1
        },
        {
                "q": "<b>27.</b> Which layer handles data encryption and compression?",
                "options": ["Session Layer", "Presentation Layer", "Application Layer", "Transport Layer"],
                "answer": 1
        },
        {
                "q": "<b>28.</b> Which layer provides network services to applications?",
                "options": ["Presentation Layer", "Application Layer", "Session Layer", "Transport Layer"],
                "answer": 1
        },
        {
                "q": "<b>29.</b> What is the correct order of OSI layers from bottom to top?",
                "options": ["Application, Presentation, Session, Transport, Network, Data Link, Physical", "Physical, Data Link, Network, Transport, Session, Presentation, Application", "Physical, Network, Data Link, Transport, Session, Presentation, Application", "Application, Transport, Network, Data Link, Physical, Session, Presentation"],
                "answer": 1
        },
        {
                "q": "<b>30.</b> Which OSI layer uses MAC addresses?",
                "options": ["Network Layer", "Data Link Layer", "Physical Layer", "Transport Layer"],
                "answer": 1
        },
        {
                "q": "<b>31.</b> How many layers does the TCP/IP model have?",
                "options": ["7", "4", "5", "6"],
                "answer": 1
        },
        {
                "q": "<b>32.</b> Which TCP/IP layer corresponds to OSI's Transport layer?",
                "options": ["Network Access", "Internet", "Transport", "Application"],
                "answer": 2
        },
        {
                "q": "<b>33.</b> Which TCP/IP layer handles IP addressing?",
                "options": ["Network Access", "Internet", "Transport", "Application"],
                "answer": 1
        },
        {
                "q": "<b>34.</b> What does TCP stand for?",
                "options": ["Transmission Control Protocol", "Total Communication Protocol", "Transmission Communication Process", "Technical Control Protocol"],
                "answer": 0
        },
        {
                "q": "<b>35.</b> What does IP stand for?",
                "options": ["International Protocol", "Internet Protocol", "Internet Program", "Internal Protocol"],
                "answer": 1
        },
        {
                "q": "<b>36.</b> Which protocol is connection-oriented?",
                "options": ["UDP", "TCP", "IP", "HTTP"],
                "answer": 1
        },
        {
                "q": "<b>37.</b> Which protocol is connectionless?",
                "options": ["TCP", "UDP", "FTP", "HTTP"],
                "answer": 1
        },
        {
                "q": "<b>38.</b> Which TCP/IP layer includes HTTP and FTP?",
                "options": ["Transport", "Internet", "Application", "Network Access"],
                "answer": 2
        },
        {
                "q": "<b>39.</b> What is the main function of TCP?",
                "options": ["Routing", "Reliable data delivery", "Physical transmission", "Error detection"],
                "answer": 1
        },
        {
                "q": "<b>40.</b> What is the main advantage of UDP?",
                "options": ["Reliability", "Lower overhead and faster transmission", "Error correction", "Connection management"],
                "answer": 1
        },
        {
                "q": "<b>41.</b> What does HTTP stand for?",
                "options": ["HyperText Transfer Protocol", "High Transfer Text Protocol", "Hyper Transfer Text Process", "High Technical Transfer Protocol"],
                "answer": 0
        },
        {
                "q": "<b>42.</b> What does FTP stand for?",
                "options": ["File Transfer Protocol", "Fast Transfer Process", "File Transmission Program", "Fast Technical Protocol"],
                "answer": 0
        },
        {
                "q": "<b>43.</b> What is DNS used for?",
                "options": ["File transfer", "Converting domain names to IP addresses", "Sending emails", "Web page display"],
                "answer": 1
        },
        {
                "q": "<b>44.</b> What does SMTP stand for?",
                "options": ["Simple Mail Transfer Protocol", "System Mail Transfer Process", "Simple Message Transfer Protocol", "System Message Technical Protocol"],
                "answer": 0
        },
        {
                "q": "<b>45.</b> What is the purpose of DHCP?",
                "options": ["Web browsing", "Automatically assigning IP addresses", "File sharing", "Email delivery"],
                "answer": 1
        },
        {
                "q": "<b>46.</b> What is the main function of ARP?",
                "options": ["Mapping IP addresses to MAC addresses", "Converting domain names", "Transferring files", "Sending emails"],
                "answer": 0
        },
        {
                "q": "<b>47.</b> What port does HTTP use?",
                "options": ["25", "443", "80", "21"],
                "answer": 2
        },
        {
                "q": "<b>48.</b> What port does HTTPS use?",
                "options": ["80", "443", "25", "110"],
                "answer": 1
        },
        {
                "q": "<b>49.</b> What is the purpose of ICMP?",
                "options": ["File transfer", "Network error reporting and diagnostics", "Web browsing", "Email delivery"],
                "answer": 1
        },
        {
                "q": "<b>50.</b> What is the main difference between IPv4 and IPv6?",
                "options": ["IPv6 is slower", "IPv6 has larger address space", "IPv4 is more secure", "IPv6 has fewer features"],
                "answer": 1
        },
        {
                "q": "<b>51.</b> The physical layer is responsible for _______.",
                "options": ["Logical addressing", "Route determination", "Transmission of raw bits over a medium", "Error correction"],
                "answer": 2
        },
        {
                "q": "<b>52.</b> Which device operates at the physical layer?",
                "options": ["Switch", "Router", "Hub", "Bridge"],
                "answer": 2
        },
        {
                "q": "<b>53.</b> The physical layer converts data into _______.",
                "options": ["Frames", "Segments", "Packets", "Signals"],
                "answer": 3
        },
        {
                "q": "<b>54.</b> The main function of the physical layer is to define _______.",
                "options": ["Transmission medium", "Protocols", "Routing algorithms", "MAC addressing"],
                "answer": 0
        },
        {
                "q": "<b>55.</b> Which of the following is not a physical layer medium?",
                "options": ["Fiber optic cable", "Coaxial cable", "Wireless radio", "IP address"],
                "answer": 3
        },
        {
                "q": "<b>56.</b> The data rate of a channel is measured in _______.",
                "options": ["Bytes per second", "Bits per second", "Hertz", "Baud"],
                "answer": 1
        },
        {
                "q": "<b>57.</b> Baud rate refers to _______.",
                "options": ["Number of bits per second", "Number of signal changes per second", "Number of frames per second", "Number of bytes per second"],
                "answer": 1
        },
        {
                "q": "<b>58.</b> Which layer converts digital bits into electrical, radio, or optical signals?",
                "options": ["Network", "Data Link", "Physical", "Application"],
                "answer": 2
        },
        {
                "q": "<b>59.</b> What is the unit of signal frequency?",
                "options": ["Joule", "Bit", "Hertz", "Volt"],
                "answer": 2
        },
        {
                "q": "<b>60.</b> The physical layer defines the _______ between devices.",
                "options": ["Software interface", "Hardware interface", "Logical link", "Network topology"],
                "answer": 1
        },
        {
                "q": "<b>61.</b> Twisted pair cables reduce _______.",
                "options": ["Attenuation", "Crosstalk", "Reflection", "Delay"],
                "answer": 1
        },
        {
                "q": "<b>62.</b> Attenuation means _______.",
                "options": ["Increase in signal power", "Loss of signal strength", "Signal reflection", "Data delay"],
                "answer": 1
        },
        {
                "q": "<b>63.</b> Which of these is a guided transmission medium?",
                "options": ["Infrared", "Satellite", "Fiber optic", "Bluetooth"],
                "answer": 2
        },
        {
                "q": "<b>64.</b> The physical layer standard for Ethernet is defined by _______.",
                "options": ["IEEE 802.3", "IEEE 802.11", "IEEE 802.5", "IEEE 802.15"],
                "answer": 0
        },
        {
                "q": "<b>65.</b> Which encoding scheme uses transitions to represent binary data?",
                "options": ["NRZ", "Manchester", "4B/5B", "AMI"],
                "answer": 1
        },
        {
                "q": "<b>66.</b> What does a repeater do?",
                "options": ["Amplifies the data", "Regenerates the signal", "Converts analog to digital", "Routes packets"],
                "answer": 1
        },
        {
                "q": "<b>67.</b> Which type of signal represents discrete values?",
                "options": ["Analog", "Digital", "Continuous", "Sinusoidal"],
                "answer": 1
        },
        {
                "q": "<b>68.</b> The Nyquist theorem is used to find _______.",
                "options": ["Maximum data rate for noiseless channels", "Minimum bandwidth", "Signal-to-noise ratio", "Modulation index"],
                "answer": 0
        },
        {
                "q": "<b>69.</b> Shannon capacity theorem defines _______.",
                "options": ["Max data rate with noise", "Voltage levels", "Modulation type", "Signal shape"],
                "answer": 0
        },
        {
                "q": "<b>70.</b> In coaxial cables, the core conductor is surrounded by _______.",
                "options": ["Plastic sheath", "Insulator and shield", "Copper mesh only", "Glass fiber"],
                "answer": 1
        },
        {
                "q": "<b>71.</b> Bit rate and baud rate are equal when _______.",
                "options": ["One bit per signal", "Multiple bits per symbol", "Binary encoding", "NRZ encoding"],
                "answer": 0
        },
        {
                "q": "<b>72.</b> Propagation delay depends on _______.",
                "options": ["Distance and signal speed", "Bandwidth", "Transmission rate", "Medium type only"],
                "answer": 0
        },
        {
                "q": "<b>73.</b> The physical layer deals with _______ topology.",
                "options": ["Logical", "Physical", "Hybrid", "Network"],
                "answer": 1
        },
        {
                "q": "<b>74.</b> What is the main purpose of modulation?",
                "options": ["Multiplexing", "Signal transformation for transmission", "Error correction", "Encryption"],
                "answer": 1
        },
        {
                "q": "<b>75.</b> Amplitude Shift Keying varies the _______ of the carrier.",
                "options": ["Frequency", "Amplitude", "Phase", "Time"],
                "answer": 1
        },
        {
                "q": "<b>76.</b> Frequency Division Multiplexing divides channels by _______.",
                "options": ["Time", "Frequency", "Code", "Space"],
                "answer": 1
        },
        {
                "q": "<b>77.</b> Time Division Multiplexing divides channels by _______.",
                "options": ["Time slots", "Frequency bands", "Voltage levels", "Signal phase"],
                "answer": 0
        },
        {
                "q": "<b>78.</b> Optical fiber works on the principle of _______.",
                "options": ["Diffraction", "Reflection", "Refraction", "Total internal reflection"],
                "answer": 3
        },
        {
                "q": "<b>79.</b> The most common fiber optic core material is _______.",
                "options": ["Copper", "Plastic", "Glass", "Carbon"],
                "answer": 2
        },
        {
                "q": "<b>80.</b> The signal-to-noise ratio is measured in _______.",
                "options": ["Decibels", "Hertz", "Volts", "Bits"],
                "answer": 0
        },
        {
                "q": "<b>81.</b> Attenuation is usually measured in _______.",
                "options": ["Volts", "dB/km", "Hz", "Bytes"],
                "answer": 1
        },
        {
                "q": "<b>82.</b> Parabolic antennas are used for _______.",
                "options": ["Long-distance point-to-point links", "LANs", "Bluetooth", "Coaxial networks"],
                "answer": 0
        },
        {
                "q": "<b>83.</b> Which of these is not a multiplexing method?",
                "options": ["FDM", "TDM", "CDM", "PDM"],
                "answer": 3
        },
        {
                "q": "<b>84.</b> Which layer ensures bit synchronization?",
                "options": ["Data link", "Network", "Physical", "Transport"],
                "answer": 2
        },
        {
                "q": "<b>85.</b> Crosstalk occurs due to _______.",
                "options": ["Overlapping signals in adjacent wires", "High signal frequency", "Noise reflection", "Attenuation"],
                "answer": 0
        },
        {
                "q": "<b>86.</b> Baseband transmission means _______.",
                "options": ["Analog signals only", "Single signal occupies full bandwidth", "Multiple signals share bandwidth", "Frequency modulation"],
                "answer": 1
        },
        {
                "q": "<b>87.</b> Broadband transmission uses _______.",
                "options": ["Digital baseband", "Multiple frequencies", "Analog-only", "Single frequency"],
                "answer": 1
        },
        {
                "q": "<b>88.</b> The physical layer of the OSI model corresponds to layer _______ in TCP/IP.",
                "options": ["Application", "Network Access", "Transport", "Internet"],
                "answer": 1
        },
        {
                "q": "<b>89.</b> Unshielded Twisted Pair (UTP) is commonly used in _______.",
                "options": ["Fiber networks", "LAN cabling", "Satellite links", "Coaxial networks"],
                "answer": 1
        },
        {
                "q": "<b>90.</b> Which transmission is bidirectional but not simultaneous?",
                "options": ["Simplex", "Half duplex", "Full duplex", "Unidirectional"],
                "answer": 1
        },
        {
                "q": "<b>91.</b> Full duplex means _______.",
                "options": ["One-way communication", "Two-way simultaneous communication", "Time-shared communication", "Broadcast mode"],
                "answer": 1
        },
        {
                "q": "<b>92.</b> Which property defines resistance to interference?",
                "options": ["Noise immunity", "Bandwidth", "Latency", "Modulation"],
                "answer": 0
        },
        {
                "q": "<b>93.</b> Bit synchronization is achieved by _______.",
                "options": ["Clock signals", "Parity bits", "Error detection", "Modulation"],
                "answer": 0
        },
        {
                "q": "<b>94.</b> Digital-to-analog conversion includes _______.",
                "options": ["ASK, FSK, PSK", "PCM", "AM", "DM"],
                "answer": 0
        },
        {
                "q": "<b>95.</b> The bandwidth of a signal is the range between _______.",
                "options": ["Max and min amplitude", "Max and min frequency", "Time slots", "Voltage levels"],
                "answer": 1
        },
        {
                "q": "<b>96.</b> Which transmission media offers highest bandwidth?",
                "options": ["UTP", "Coaxial", "Fiber optic", "Microwave"],
                "answer": 2
        },
        {
                "q": "<b>97.</b> PCM stands for _______.",
                "options": ["Pulse Code Modulation", "Phase Code Multiplexing", "Path Control Method", "Pulse Communication Mode"],
                "answer": 0
        },
        {
                "q": "<b>98.</b> Which device regenerates signals without changing data?",
                "options": ["Switch", "Bridge", "Repeater", "Gateway"],
                "answer": 2
        },
        {
                "q": "<b>99.</b> Bit duration is the reciprocal of _______.",
                "options": ["Bandwidth", "Bit rate", "Baud rate", "Frequency"],
                "answer": 1
        },
        {
                "q": "<b>100.</b> The physical layer in OSI is layer number _______.",
                "options": ["1", "2", "3", "4"],
                "answer": 0
        },
        {
                "q": "<b>101.</b> What is the main purpose of the Data Link Layer?",
                "options": ["End-to-end delivery", "Node-to-node delivery", "Process-to-process delivery", "Application data formatting"],
                "answer": 1
        },
        {
                "q": "<b>102.</b> Which sublayer interfaces with the Physical Layer?",
                "options": ["LLC", "MAC", "Network", "Transport"],
                "answer": 1
        },
        {
                "q": "<b>103.</b> Which sublayer interfaces with the Network Layer?",
                "options": ["LLC", "MAC", "Physical", "Session"],
                "answer": 0
        },
        {
                "q": "<b>104.</b> What is the primary function of MAC sublayer?",
                "options": ["Routing", "Media access control", "Error correction", "Packet sequencing"],
                "answer": 1
        },
        {
                "q": "<b>105.</b> What is a MAC address?",
                "options": ["Logical address", "Physical hardware address", "IP address", "Port address"],
                "answer": 1
        },
        {
                "q": "<b>106.</b> How many bytes is a MAC address?",
                "options": ["4 bytes", "6 bytes", "8 bytes", "32 bytes"],
                "answer": 1
        },
        {
                "q": "<b>107.</b> What is the purpose of framing?",
                "options": ["Error correction", "Delimiting data boundaries", "Routing packets", "Address resolution"],
                "answer": 1
        },
        {
                "q": "<b>108.</b> Which error detection method uses polynomial division?",
                "options": ["Parity check", "Checksum", "CRC", "Hamming code"],
                "answer": 2
        },
        {
                "q": "<b>109.</b> What does CRC stand for?",
                "options": ["Cyclic Redundancy Check", "Computer Redundancy Code", "Cyclic Redundancy Code", "Computer Redundancy Check"],
                "answer": 0
        },
        {
                "q": "<b>110.</b> Which protocol uses sliding window protocol?",
                "options": ["IP", "HDLC", "HTTP", "SMTP"],
                "answer": 1
        },
        {
                "q": "<b>111.</b> What is the purpose of flow control?",
                "options": ["Error detection", "Preventing receiver overload", "Routing packets", "Address resolution"],
                "answer": 1
        },
        {
                "q": "<b>112.</b> Which flow control method uses window size?",
                "options": ["Stop-and-wait", "Sliding window", "Parity check", "CRC"],
                "answer": 1
        },
        {
                "q": "<b>113.</b> In Stop-and-Wait ARQ, how many frames can be sent before ACK?",
                "options": ["Multiple frames", "One frame", "Zero frames", "Unlimited frames"],
                "answer": 1
        },
        {
                "q": "<b>114.</b> What does ARQ stand for?",
                "options": ["Automatic Repeat Request", "Automatic Response Query", "Address Resolution Query", "Automatic Routing Quality"],
                "answer": 0
        },
        {
                "q": "<b>115.</b> Which media access method is used in Ethernet?",
                "options": ["Token passing", "CSMA/CD", "Polling", "TDMA"],
                "answer": 1
        },
        {
                "q": "<b>116.</b> What does CSMA/CD stand for?",
                "options": ["Carrier Sense Multiple Access with Collision Detection", "Computer System Media Access with Collision Detection", "Carrier System Multiple Access with Collision Detection", "Computer Sense Media Access with Collision Detection"],
                "answer": 0
        },
        {
                "q": "<b>117.</b> What happens when collision occurs in CSMA/CD?",
                "options": ["Continue transmission", "Send jam signal and retry", "Stop network", "Ignore collision"],
                "answer": 1
        },
        {
                "q": "<b>118.</b> Which protocol is used for point-to-point links?",
                "options": ["Ethernet", "PPP", "Token Ring", "CSMA/CD"],
                "answer": 1
        },
        {
                "q": "<b>119.</b> What does PPP stand for?",
                "options": ["Point-to-Point Protocol", "Packet-to-Packet Protocol", "Port-to-Port Protocol", "Process-to-Process Protocol"],
                "answer": 0
        },
        {
                "q": "<b>120.</b> Which device operates at Data Link Layer?",
                "options": ["Router", "Switch", "Hub", "Repeater"],
                "answer": 1
        },
        {
                "q": "<b>121.</b> What is the purpose of a bridge?",
                "options": ["Route between networks", "Connect two network segments", "Amplify signals", "Convert protocols"],
                "answer": 1
        },
        {
                "q": "<b>122.</b> Which addressing is used at Data Link Layer?",
                "options": ["IP address", "MAC address", "Port address", "Logical address"],
                "answer": 1
        },
        {
                "q": "<b>123.</b> What is the maximum Ethernet frame size?",
                "options": ["512 bytes", "1024 bytes", "1518 bytes", "2048 bytes"],
                "answer": 2
        },
        {
                "q": "<b>124.</b> What is the minimum Ethernet frame size?",
                "options": ["46 bytes", "64 bytes", "128 bytes", "256 bytes"],
                "answer": 1
        },
        {
                "q": "<b>125.</b> Which field in Ethernet frame contains type/length?",
                "options": ["Preamble", "EtherType", "FCS", "Data"],
                "answer": 1
        },
        {
                "q": "<b>126.</b> What is the main function of Network Layer?",
                "options": ["Node-to-node delivery", "Source-to-destination delivery", "Process-to-process delivery", "Application data formatting"],
                "answer": 1
        },
        {
                "q": "<b>127.</b> Which addressing is used at Network Layer?",
                "options": ["MAC address", "IP address", "Port address", "Physical address"],
                "answer": 1
        },
        {
                "q": "<b>128.</b> What is the purpose of routing?",
                "options": ["Error detection", "Determining optimal path", "Flow control", "Frame formatting"],
                "answer": 1
        },
        {
                "q": "<b>129.</b> Which device operates at Network Layer?",
                "options": ["Switch", "Router", "Hub", "Bridge"],
                "answer": 1
        },
        {
                "q": "<b>130.</b> What does IP stand for?",
                "options": ["Internet Protocol", "Internal Protocol", "Internet Program", "Internal Program"],
                "answer": 0
        },
        {
                "q": "<b>131.</b> What is the size of IPv4 address?",
                "options": ["16 bits", "32 bits", "48 bits", "128 bits"],
                "answer": 1
        },
        {
                "q": "<b>132.</b> What is the size of IPv6 address?",
                "options": ["32 bits", "64 bits", "128 bits", "256 bits"],
                "answer": 2
        },
        {
                "q": "<b>133.</b> Which protocol provides error reporting?",
                "options": ["TCP", "ICMP", "UDP", "ARP"],
                "answer": 1
        },
        {
                "q": "<b>134.</b> What does ICMP stand for?",
                "options": ["Internet Control Message Protocol", "Internal Control Message Protocol", "Internet Communication Message Protocol", "Internal Communication Message Protocol"],
                "answer": 0
        },
        {
                "q": "<b>135.</b> Which protocol maps IP to MAC addresses?",
                "options": ["ICMP", "ARP", "RARP", "DHCP"],
                "answer": 1
        },
        {
                "q": "<b>136.</b> What does ARP stand for?",
                "options": ["Address Resolution Protocol", "Address Routing Protocol", "Automatic Resolution Protocol", "Automatic Routing Protocol"],
                "answer": 0
        },
        {
                "q": "<b>137.</b> What is the purpose of subnetting?",
                "options": ["Increase network size", "Divide large networks into smaller subnets", "Combine small networks", "Change IP addresses"],
                "answer": 1
        },
        {
                "q": "<b>138.</b> What is the default subnet mask for Class C?",
                "options": ["255.0.0.0", "255.255.0.0", "255.255.255.0", "255.255.255.255"],
                "answer": 2
        },
        {
                "q": "<b>139.</b> Which routing algorithm uses shortest path?",
                "options": ["Distance vector", "Link state", "Path vector", "Hybrid"],
                "answer": 1
        },
        {
                "q": "<b>140.</b> Which protocol is a distance vector protocol?",
                "options": ["OSPF", "RIP", "BGP", "IS-IS"],
                "answer": 1
        },
        {
                "q": "<b>141.</b> What is the maximum hop count in RIP?",
                "options": ["10", "15", "20", "255"],
                "answer": 1
        },
        {
                "q": "<b>142.</b> Which protocol is used between autonomous systems?",
                "options": ["RIP", "OSPF", "BGP", "EIGRP"],
                "answer": 2
        },
        {
                "q": "<b>143.</b> What does BGP stand for?",
                "options": ["Border Gateway Protocol", "Basic Gateway Protocol", "Border Gateway Process", "Basic Gateway Process"],
                "answer": 0
        },
        {
                "q": "<b>144.</b> What is NAT used for?",
                "options": ["Error detection", "Translating private IP to public IP", "Routing between networks", "Address resolution"],
                "answer": 1
        },
        {
                "q": "<b>145.</b> What does NAT stand for?",
                "options": ["Network Address Translation", "Network Access Translation", "Network Address Transfer", "Network Access Transfer"],
                "answer": 0
        },
        {
                "q": "<b>146.</b> What is the purpose of fragmentation?",
                "options": ["Error correction", "Breaking packets to fit MTU", "Flow control", "Address resolution"],
                "answer": 1
        },
        {
                "q": "<b>147.</b> Which field identifies fragments of same packet?",
                "options": ["TTL", "Identification", "Flags", "Protocol"],
                "answer": 1
        },
        {
                "q": "<b>148.</b> What is TTL used for?",
                "options": ["Error detection", "Preventing infinite looping", "Flow control", "Sequencing"],
                "answer": 1
        },
        {
                "q": "<b>149.</b> What does TTL stand for?",
                "options": ["Time to Live", "Time to Leave", "Transfer Time Limit", "Transmission Time Length"],
                "answer": 0
        },
        {
                "q": "<b>150.</b> Which protocol provides logical addressing?",
                "options": ["TCP", "IP", "ARP", "ICMP"],
                "answer": 1
        },
        {
                "q": "<b>151.</b> Data Transmission Time Q: A 1 MB file is transmitted over a 10 Mbps link. What is the transmission time? Options:",
                "options": ["0.8 s", "0.64 s", "0.1 s", "1 s"],
                "answer": 0
        },
        {
                "q": "<b>152.</b> Propagation Delay Q: A signal travels through a 2000 km fiber optic cable at 2 × 10^8 m/s. What is the propagation delay? Options:",
                "options": ["10 ms", "5 ms", "20 ms", "2 ms"],
                "answer": 0
        },
        {
                "q": "<b>153.</b> Bandwidth-Delay Product Q: A 1 Gbps link has a round-trip delay of 50 ms. What is the bandwidth-delay product? Options:",
                "options": ["50 Mb", "100 Mb", "25 Mb", "1 Mb"],
                "answer": 0
        },
        {
                "q": "<b>154.</b> Maximum IP Addresses Q: How many hosts can be assigned in a subnet with mask 255.255.255.240? Options:",
                "options": ["14", "16", "30", "254"],
                "answer": 0
        },
        {
                "q": "<b>155.</b> Effective Throughput Q: A 100 Mbps link has 20% overhead. What is the effective throughput? Options:",
                "options": ["80 Mbps", "90 Mbps", "70 Mbps", "100 Mbps"],
                "answer": 0
        },
        {
                "q": "<b>156.</b> Channel Capacity (Shannon) Q: A channel has bandwidth 3 kHz and SNR = 15. Find channel capacity. Options:",
                "options": ["15 kbps", "12 kbps", "18 kbps", "10 kbps"],
                "answer": 1
        },
        {
                "q": "<b>157.</b> Delay × Bandwidth Product Q: 10 Mbps link with 100 ms delay. Bandwidth-delay product? Options:",
                "options": ["1 Mb", "10 Mb", "100 Mb", "0.1 Mb"],
                "answer": 0
        },
        {
                "q": "<b>158.</b> Utilization in Stop-and-Wait Q: A 1 Mbps link with 100 ms one-way delay uses Stop-and-Wait. Frame size = 10 kb. Utilization? Options:",
                "options": ["0.5", "0.66", "0.8", "0.05"],
                "answer": 3
        },
        {
                "q": "<b>159.</b> Subnetting Q: Number of subnets created if /24 network uses /26 mask? Options:",
                "options": ["4", "8", "2", "16"],
                "answer": 0
        },
        {
                "q": "<b>160.</b> Number of Hosts Q: /22 subnet mask → number of hosts per subnet? Options:",
                "options": ["1022", "1024", "512", "2048"],
                "answer": 0
        },
        {
                "q": "<b>161.</b> Transmission Delay Q: 5 MB file over 50 Mbps link. Transmission delay? Options:",
                "options": ["0.8 s", "0.5 s", "0.64 s", "1 s"],
                "answer": 0
        },
        {
                "q": "<b>162.</b> Efficiency in Sliding Window Q: Window size = 5, link delay = 20 ms, frame size = 1 kb, bandwidth = 10 kb/ms. Efficiency? Options:",
                "options": ["0.5", "0.8", "1", "0.9"],
                "answer": 1
        },
        {
                "q": "<b>163.</b> IPv4 Address Range Q: Network 192.168.5.0/26. Last usable IP? Options:",
                "options": ["192.168.5.62", "192.168.5.63", "192.168.5.64", "192.168.5.61"],
                "answer": 0
        },
        {
                "q": "<b>164.</b> CRC Calculation Q: Frame = 1101011011, Generator = 1011. Number of CRC bits? Options:",
                "options": ["3", "4", "5", "2"],
                "answer": 0
        },
        {
                "q": "<b>165.</b> Propagation Speed Q: Signal takes 0.2 ms over 40 km cable. Speed? Options:",
                "options": ["2 × 10^8 m/s", "1 × 10^8 m/s", "4 × 10^8 m/s", "3 × 10^8 m/s"],
                "answer": 0
        },
        {
                "q": "<b>166.</b> Channel Bandwidth Q: Max data rate for noiseless 3 kHz channel with 8 signal levels? Options:",
                "options": ["12 kbps", "9 kbps", "24 kbps", "18 kbps"],
                "answer": 3
        },
        {
                "q": "<b>167.</b> Queuing Delay Q: Average queue length = 10 packets, service rate = 1000 packets/s. Delay? Options:",
                "options": ["0.01 s", "0.1 s", "0.05 s", "0.1 ms"],
                "answer": 0
        },
        {
                "q": "<b>168.</b> Maximum TCP Window Q: 100 Mbps link, RTT = 50 ms. Maximum TCP window size? Options:",
                "options": ["0.5 Mb", "5 Mb", "1 Mb", "2 Mb"],
                "answer": 1
        },
        {
                "q": "<b>169.</b> Number of Subnets Q: /16 network divided into /18 subnets → Number of subnets? Options:",
                "options": ["4", "8", "16", "64"],
                "answer": 0
        },
        {
                "q": "<b>170.</b> Transmission Time with Overhead Q: 1000-byte packet over 1 Mbps link. 20% header overhead. Transmission time? Options:",
                "options": ["8.2 ms", "10 ms", "9.6 ms", "12 ms"],
                "answer": 2
        },
        {
                "q": "<b>171.</b> A 1 MB file is sent over a 10 Mbps link. Transmission time?",
                "options": ["0.8 s", "0.64 s", "1 s", "0.5 s"],
                "answer": 0
        },
        {
                "q": "<b>172.</b> Propagation delay for 2000 km at 2 × 10^8 m/s?",
                "options": ["10 ms", "5 ms", "20 ms", "2 ms"],
                "answer": 0
        },
        {
                "q": "<b>173.</b> 5 MB file on 50 Mbps link, transmission time?",
                "options": ["0.8 s", "0.5 s", "0.64 s", "1 s"],
                "answer": 0
        },
        {
                "q": "<b>174.</b> 10 Mbps link, 100 ms delay, bandwidth-delay product?",
                "options": ["1 Mb", "10 Mb", "100 Mb", "0.1 Mb"],
                "answer": 0
        },
        {
                "q": "<b>175.</b> Transmission time for 1000-byte packet over 1 Mbps link?",
                "options": ["8 ms", "10 ms", "12 ms", "9.6 ms"],
                "answer": 0
        },
        {
                "q": "<b>176.</b> Propagation speed 2 × 10^8 m/s, distance 40 km. Delay?",
                "options": ["0.2 ms", "0.1 ms", "0.4 ms", "0.5 ms"],
                "answer": 0
        },
        {
                "q": "<b>177.</b> 50 kb file, 10 kb/ms link. Transmission time?",
                "options": ["5 ms", "10 ms", "2 ms", "20 ms"],
                "answer": 0
        },
        {
                "q": "<b>178.</b> Link 1 Mbps, frame size 5000 bits. Transmission time?",
                "options": ["5 ms", "4 ms", "10 ms", "0.5 ms"],
                "answer": 0
        },
        {
                "q": "<b>179.</b> Round-trip delay 100 ms, TCP uses 10 kb frame, 1 Mbps link. Utilization (Stop-and-Wait)?",
                "options": ["0.05", "0.5", "0.8", "1"],
                "answer": 0
        },
        {
                "q": "<b>180.</b> Link 100 Mbps, RTT 50 ms. Maximum TCP window size?",
                "options": ["5 Mb", "2 Mb", "1 Mb", "10 Mb"],
                "answer": 0
        },
        {
                "q": "<b>181.</b> 1 Gbps link, 50 ms delay. BDP?",
                "options": ["50 Mb", "100 Mb", "25 Mb", "1 Mb"],
                "answer": 0
        },
        {
                "q": "<b>182.</b> 100 Mbps link, 20% overhead. Effective throughput?",
                "options": ["80 Mbps", "90 Mbps", "70 Mbps", "100 Mbps"],
                "answer": 0
        },
        {
                "q": "<b>183.</b> Channel bandwidth 3 kHz, SNR = 15. Shannon capacity?",
                "options": ["12 kbps", "15 kbps", "18 kbps", "10 kbps"],
                "answer": 0
        },
        {
                "q": "<b>184.</b> 10 Mbps link, 100 ms delay. BDP?",
                "options": ["1 Mb", "10 Mb", "100 Mb", "0.1 Mb"],
                "answer": 0
        },
        {
                "q": "<b>185.</b> Sliding window size = 5, propagation 20 ms, frame 1 kb, bandwidth 10 kb/ms. Efficiency?",
                "options": ["0.5", "0.8", "1", "0.9"],
                "answer": 1
        },
        {
                "q": "<b>186.</b> UDP transmission 1 MB file, 10 Mbps link. Time?",
                "options": ["0.8 s", "1 s", "0.64 s", "0.5 s"],
                "answer": 0
        },
        {
                "q": "<b>187.</b> 1 Mbps link, 1000-byte frame, propagation 50 ms. Stop-and-Wait utilization?",
                "options": ["0.05", "0.1", "0.2", "0.5"],
                "answer": 0
        },
        {
                "q": "<b>188.</b> Window size 10 frames, link 1 Mbps, 10 ms frame time. Efficiency?",
                "options": ["0.5", "0.8", "1", "0.9"],
                "answer": 2
        },
        {
                "q": "<b>189.</b> 50 Mbps, 20 ms delay, BDP?",
                "options": ["1 Mb", "0.5 Mb", "2 Mb", "5 Mb"],
                "answer": 0
        },
        {
                "q": "<b>190.</b> /28 subnet, number of hosts?",
                "options": ["14", "16", "30", "32"],
                "answer": 0
        },
        {
                "q": "<b>191.</b> /22 subnet, number of hosts?",
                "options": ["1022", "1024", "512", "2048"],
                "answer": 0
        },
        {
                "q": "<b>192.</b> /24 network divided into /26 subnets → Number of subnets?",
                "options": ["4", "2", "8", "16"],
                "answer": 0
        },
        {
                "q": "<b>193.</b> /16 divided into /18 → subnets?",
                "options": ["4", "8", "16", "64"],
                "answer": 0
        },
        {
                "q": "<b>194.</b> IP 192.168.1.0/26, last usable IP?",
                "options": ["192.168.1.62", "192.168.1.63", "192.168.1.64", "192.168.1.61"],
                "answer": 0
        },
        {
                "q": "<b>195.</b> /28 subnet mask, number of subnets in /24 network?",
                "options": ["16", "4", "8", "2"],
                "answer": 0
        },
        {
                "q": "<b>196.</b> /30 subnet, usable hosts?",
                "options": ["2", "4", "6", "8"],
                "answer": 0
        },
        {
                "q": "<b>197.</b> /27 subnet mask → number of hosts?",
                "options": ["30", "32", "62", "64"],
                "answer": 0
        },
        {
                "q": "<b>198.</b> Subnet mask 255.255.255.240 → hosts?",
                "options": ["14", "16", "30", "254"],
                "answer": 0
        },
        {
                "q": "<b>199.</b> /25 subnet, usable hosts?",
                "options": ["126", "128", "254", "256"],
                "answer": 0
        },
        {
                "q": "<b>200.</b> Stop-and-Wait, frame size = 1000 bits, link = 1 Mbps, propagation = 50 ms. Efficiency?",
                "options": ["0.05", "0.1", "0.2", "0.5"],
                "answer": 0
        },
        {
                "q": "<b>201.</b> Go-Back-N, window size = 5, link = 1 Mbps, frame = 1 kb, RTT = 10 ms. Utilization?",
                "options": ["0.2", "0.5", "0.33", "1"],
                "answer": 1
        },
        {
                "q": "<b>202.</b> Selective Repeat, window size = 4, Tx = 2 ms, RTT = 20 ms. Efficiency?",
                "options": ["0.4", "0.5", "0.66", "0.8"],
                "answer": 0
        },
        {
                "q": "<b>203.</b> Frame size = 8000 bits, link = 2 Mbps, transmission time?",
                "options": ["4 ms", "5 ms", "3 ms", "2 ms"],
                "answer": 0
        },
        {
                "q": "<b>204.</b> RTT = 100 ms, frame Tx = 10 ms, window = 5. Efficiency of sliding window?",
                "options": ["0.33", "0.5", "0.66", "1"],
                "answer": 1
        },
        {
                "q": "<b>205.</b> Stop-and-Wait, 5 kb frame, 2 Mbps link, 20 ms RTT. Efficiency?",
                "options": ["0.2", "0.25", "0.5", "0.4"],
                "answer": 0
        },
        {
                "q": "<b>206.</b> Window size 8, transmission = 1 ms, RTT = 10 ms. Maximum utilization?",
                "options": ["0.5", "0.66", "0.8", "1"],
                "answer": 2
        },
        {
                "q": "<b>207.</b> Link 10 Mbps, frame 10 kb, Tx time?",
                "options": ["1 ms", "2 ms", "10 ms", "5 ms"],
                "answer": 0
        },
        {
                "q": "<b>208.</b> Stop-and-Wait, Tx = 2 ms, RTT = 20 ms, efficiency?",
                "options": ["0.1", "0.2", "0.5", "0.9"],
                "answer": 0
        },
        {
                "q": "<b>209.</b> Sliding window, Tx = 5 ms, RTT = 50 ms, window = 5. Efficiency?",
                "options": ["0.25", "0.33", "0.5", "0.66"],
                "answer": 2
        },
        {
                "q": "<b>210.</b> CRC bits for generator 1011?",
                "options": ["3", "4", "5", "2"],
                "answer": 0
        },
        {
                "q": "<b>211.</b> Channel 3 kHz, SNR = 15, Shannon capacity?",
                "options": ["12 kbps", "10 kbps", "15 kbps", "18 kbps"],
                "answer": 0
        },
        {
                "q": "<b>212.</b> Propagation speed 2 × 10^8 m/s, distance 1000 km, delay?",
                "options": ["5 ms", "10 ms", "2 ms", "20 ms"],
                "answer": 0
        },
        {
                "q": "<b>213.</b> TCP maximum window = 65,535 bytes, link 1 Mbps, RTT 100 ms. Max utilization?",
                "options": ["0.5", "0.52", "0.52", "1"],
                "answer": 3
        },
        {
                "q": "<b>214.</b> Transmission time 1000-byte packet, 10 Mbps link?",
                "options": ["0.8 ms", "0.8 s", "0.64 s", "1 s"],
                "answer": 0
        },
        {
                "q": "<b>215.</b> 100 kb file, 10 Mbps, delay 50 ms. BDP?",
                "options": ["0.5 Mb", "0.25 Mb", "1 Mb", "0.05 Mb"],
                "answer": 0
        },
        {
                "q": "<b>216.</b> Window size 10 frames, 1 ms/frame, RTT 20 ms. Efficiency Go-Back-N?",
                "options": ["0.33", "0.5", "0.66", "0.75"],
                "answer": 1
        },
        {
                "q": "<b>217.</b> UDP, 5 MB file, 10 Mbps link, time?",
                "options": ["4 s", "5 s", "0.8 s", "1 s"],
                "answer": 0
        },
        {
                "q": "<b>218.</b> 10 Mbps, frame 5000 bits, Tx time?",
                "options": ["0.5 ms", "1 ms", "0.8 ms", "2 ms"],
                "answer": 0
        },
        {
                "q": "<b>219.</b> Propagation 2 × 10^8 m/s, distance 600 km. Delay?",
                "options": ["2 ms", "3 ms", "6 ms", "0.6 ms"],
                "answer": 1
        },
        {
                "q": "<b>220.</b> Which transport layer protocol is connection-oriented?",
                "options": ["UDP", "TCP", "IP", "ICMP"],
                "answer": 1
        },
        {
                "q": "<b>221.</b> UDP is suitable for:",
                "options": ["Reliable data transfer", "Real-time applications", "File transfer", "Web browsing"],
                "answer": 1
        },
        {
                "q": "<b>222.</b> TCP uses:",
                "options": ["Stop-and-wait", "Sliding window", "CSMA/CD", "ARP"],
                "answer": 1
        },
        {
                "q": "<b>223.</b> Maximum segment size (MSS) is associated with:",
                "options": ["UDP", "TCP", "IP", "ICMP"],
                "answer": 1
        },
        {
                "q": "<b>224.</b> Which port does HTTP use by default?",
                "options": ["21", "22", "80", "25"],
                "answer": 2
        },
        {
                "q": "<b>225.</b> UDP provides:",
                "options": ["Flow control", "Error control", "Both A and B", "None"],
                "answer": 3
        },
        {
                "q": "<b>226.</b> TCP header contains:",
                "options": ["Source and destination port", "Sequence number", "Acknowledgment number", "All of the above"],
                "answer": 3
        },
        {
                "q": "<b>227.</b> Which is faster for data transfer?",
                "options": ["TCP", "UDP", "FTP", "SMTP"],
                "answer": 1
        },
        {
                "q": "<b>228.</b> TCP guarantees:",
                "options": ["Ordered delivery", "Reliable delivery", "Both A and B", "None"],
                "answer": 2
        },
        {
                "q": "<b>229.</b> UDP is used in:",
                "options": ["Video streaming", "Email transfer", "File transfer", "Web browsing"],
                "answer": 0
        },
        {
                "q": "<b>230.</b> Port number range in TCP/UDP is:",
                "options": ["0–255", "0–65535", "0–1023", "1024–49151"],
                "answer": 1
        },
        {
                "q": "<b>231.</b> TCP checksum is used for:",
                "options": ["Error detection", "Flow control", "Congestion control", "Routing"],
                "answer": 0
        },
        {
                "q": "<b>232.</b> Which transport protocol is best for DNS queries?",
                "options": ["TCP", "UDP", "IP", "HTTP"],
                "answer": 1
        },
        {
                "q": "<b>233.</b> Sliding window is used for:",
                "options": ["Flow control", "Congestion control", "Routing", "Addressing"],
                "answer": 0
        },
        {
                "q": "<b>234.</b> TCP three-way handshake involves:",
                "options": ["SYN, SYN-ACK, ACK", "ACK, SYN, SYN-ACK", "FIN, ACK, SYN", "SYN, ACK, FIN"],
                "answer": 0
        },
        {
                "q": "<b>235.</b> Which field in TCP identifies the session?",
                "options": ["Sequence number", "Port number", "IP address", "Checksum"],
                "answer": 1
        },
        {
                "q": "<b>236.</b> Which protocol is connectionless?",
                "options": ["TCP", "UDP", "FTP", "Telnet"],
                "answer": 1
        },
        {
                "q": "<b>237.</b> Flow control prevents:",
                "options": ["Congestion in network", "Overflow of receiver buffer", "Packet loss", "Routing loops"],
                "answer": 1
        },
        {
                "q": "<b>238.</b> Which protocol supports multicast?",
                "options": ["TCP", "UDP", "SMTP", "HTTP"],
                "answer": 1
        },
        {
                "q": "<b>239.</b> TCP uses sequence numbers to:",
                "options": ["Identify port", "Order packets", "Detect errors", "Determine congestion"],
                "answer": 1
        },
        {
                "q": "<b>240.</b> Time to live (TTL) is used in:",
                "options": ["TCP header", "UDP header", "IP header", "Session layer"],
                "answer": 2
        },
        {
                "q": "<b>241.</b> Maximum window size in TCP:",
                "options": ["65,535 bytes", "64 KB", "32 KB", "16 KB"],
                "answer": 0
        },
        {
                "q": "<b>242.</b> Acknowledgment in TCP can be:",
                "options": ["Cumulative", "Selective", "Both A and B", "None"],
                "answer": 2
        },
        {
                "q": "<b>243.</b> Which is true about UDP?",
                "options": ["Reliable", "Ordered", "Lightweight", "Connection-oriented"],
                "answer": 2
        },
        {
                "q": "<b>244.</b> TCP segments include:",
                "options": ["Data and header", "Only data", "Only header", "Routing info"],
                "answer": 0
        },
        {
                "q": "<b>245.</b> Session layer is responsible for:",
                "options": ["Routing", "Managing sessions", "Error detection", "Flow control"],
                "answer": 1
        },
        {
                "q": "<b>246.</b> Which layer establishes, manages, and terminates sessions?",
                "options": ["Transport", "Session", "Network", "Data Link"],
                "answer": 1
        },
        {
                "q": "<b>247.</b> Session checkpointing is used for:",
                "options": ["Flow control", "Recovery from failure", "Congestion control", "Packet sequencing"],
                "answer": 1
        },
        {
                "q": "<b>248.</b> RPC (Remote Procedure Call) works at:",
                "options": ["Transport layer", "Session layer", "Application layer", "Network layer"],
                "answer": 1
        },
        {
                "q": "<b>249.</b> Which protocol is used for session establishment in Windows?",
                "options": ["NetBIOS", "HTTP", "FTP", "SMTP"],
                "answer": 0
        },
        {
                "q": "<b>250.</b> Session layer provides:",
                "options": ["Dialog control", "Token management", "Synchronization", "All of the above"],
                "answer": 3
        },
        {
                "q": "<b>251.</b> Half-duplex session:",
                "options": ["Only one side communicates at a time", "Both communicate simultaneously", "No communication", "None"],
                "answer": 0
        },
        {
                "q": "<b>252.</b> Full-duplex session:",
                "options": ["Both sides communicate simultaneously", "Only one side communicates", "Only data link layer", "None"],
                "answer": 0
        },
        {
                "q": "<b>253.</b> Session layer is Layer number:",
                "options": ["3", "4", "5", "6"],
                "answer": 2
        },
        {
                "q": "<b>254.</b> Which is not a session layer function?",
                "options": ["Establish session", "Flow control", "Dialog management", "Terminate session"],
                "answer": 1
        },
        {
                "q": "<b>255.</b> Token management prevents:",
                "options": ["Deadlock", "Congestion", "Packet loss", "Error detection"],
                "answer": 0
        },
        {
                "q": "<b>256.</b> Which session type is used in video conferencing?",
                "options": ["Half-duplex", "Full-duplex", "Simplex", "None"],
                "answer": 1
        },
        {
                "q": "<b>257.</b> Synchronization in session layer ensures:",
                "options": ["Data ordering", "Routing efficiency", "Error detection", "Address assignment"],
                "answer": 0
        },
        {
                "q": "<b>258.</b> Session layer is responsible for:",
                "options": ["Authentication", "Encryption", "Authorization", "All of the above"],
                "answer": 3
        },
        {
                "q": "<b>259.</b> Session layer works closely with:",
                "options": ["Transport and Application layer", "Network and Data link layer", "Physical layer only", "None"],
                "answer": 0
        },
        {
                "q": "<b>260.</b> Which protocol provides session services over TCP/IP?",
                "options": ["NetBIOS", "NFS", "RPC", "All of the above"],
                "answer": 3
        },
        {
                "q": "<b>261.</b> Dialog control can be:",
                "options": ["Simplex", "Half-duplex", "Full-duplex", "All of the above"],
                "answer": 3
        },
        {
                "q": "<b>262.</b> Session termination is:",
                "options": ["Optional", "Mandatory", "Not required", "Only for UDP"],
                "answer": 1
        },
        {
                "q": "<b>263.</b> Remote procedure call ensures:",
                "options": ["Client-server communication", "Network routing", "Congestion control", "Packet ordering"],
                "answer": 0
        },
        {
                "q": "<b>264.</b> Which of the following is a session protocol?",
                "options": ["PPTP", "TCP", "UDP", "IP"],
                "answer": 0
        },
        {
                "q": "<b>265.</b> Session layer provides:",
                "options": ["Checkpointing", "Recovery", "Synchronization", "All of the above"],
                "answer": 3
        },
        {
                "q": "<b>266.</b> Dialog control helps in:",
                "options": ["Managing communication direction", "Error detection", "Routing", "None"],
                "answer": 0
        },
        {
                "q": "<b>267.</b> Token management is mainly used in:",
                "options": ["Multi-user environment", "Single user environment", "Routing", "Packet switching"],
                "answer": 0
        },
        {
                "q": "<b>268.</b> Session establishment includes:",
                "options": ["Authentication", "Authorization", "Both A and B", "None"],
                "answer": 2
        },
        {
                "q": "<b>269.</b> Primary function of session layer:",
                "options": ["Data delivery", "Error detection", "Session management", "Routing"],
                "answer": 2
        },
        {
                "q": "<b>270.</b> Which layer provides network services directly to the user?",
                "options": ["Transport", "Application", "Session", "Network"],
                "answer": 1
        },
        {
                "q": "<b>271.</b> HTTP stands for:",
                "options": ["Hypertext Transfer Protocol", "Hypertext Transmission Protocol", "Hyper Transfer Text Protocol", "Hyper Transmission Text Protocol"],
                "answer": 0
        },
        {
                "q": "<b>272.</b> Which port does HTTP use by default?",
                "options": ["20", "21", "80", "443"],
                "answer": 2
        },
        {
                "q": "<b>273.</b> HTTPS uses:",
                "options": ["TCP 443", "UDP 443", "TCP 80", "UDP 80"],
                "answer": 0
        },
        {
                "q": "<b>274.</b> FTP works on which ports?",
                "options": ["20 and 21", "21 and 22", "23 and 25", "80 and 443"],
                "answer": 0
        },
        {
                "q": "<b>275.</b> Which protocol is used for sending emails?",
                "options": ["HTTP", "SMTP", "FTP", "DNS"],
                "answer": 1
        },
        {
                "q": "<b>276.</b> POP3 protocol is used for:",
                "options": ["Sending emails", "Receiving emails", "File transfer", "Remote login"],
                "answer": 1
        },
        {
                "q": "<b>277.</b> IMAP differs from POP3 because:",
                "options": ["It stores emails on server", "It deletes emails after download", "It uses TCP 21", "It is connectionless"],
                "answer": 0
        },
        {
                "q": "<b>278.</b> DNS is used for:",
                "options": ["Translating IP addresses to domain names", "Email transfer", "File transfer", "Remote login"],
                "answer": 0
        },
        {
                "q": "<b>279.</b> Telnet protocol is used for:",
                "options": ["Remote login", "Email transfer", "File transfer", "Web browsing"],
                "answer": 0
        },
        {
                "q": "<b>280.</b> TFTP uses which transport protocol?",
                "options": ["TCP", "UDP", "ICMP", "HTTP"],
                "answer": 1
        },
        {
                "q": "<b>281.</b> FTP provides:",
                "options": ["Reliable data transfer", "Encryption by default", "Connectionless service", "Only uploading files"],
                "answer": 0
        },
        {
                "q": "<b>282.</b> Which command downloads a file using FTP?",
                "options": ["GET", "POST", "PUT", "SEND"],
                "answer": 0
        },
        {
                "q": "<b>283.</b> Which command uploads a file using FTP?",
                "options": ["GET", "PUT", "POST", "SEND"],
                "answer": 1
        },
        {
                "q": "<b>284.</b> SSH provides:",
                "options": ["Encrypted remote login", "File transfer only", "Web browsing", "Email services"],
                "answer": 0
        },
        {
                "q": "<b>285.</b> Which port does SSH use by default?",
                "options": ["22", "21", "23", "25"],
                "answer": 0
        },
        {
                "q": "<b>286.</b> SFTP differs from FTP in:",
                "options": ["Encryption", "Port number", "Transport protocol", "All of the above"],
                "answer": 3
        },
        {
                "q": "<b>287.</b> SMTP uses which port by default?",
                "options": ["20", "21", "25", "110"],
                "answer": 2
        },
        {
                "q": "<b>288.</b> POP3 uses which port by default?",
                "options": ["21", "25", "110", "443"],
                "answer": 2
        },
        {
                "q": "<b>289.</b> IMAP uses which port by default?",
                "options": ["143", "110", "25", "80"],
                "answer": 0
        },
        {
                "q": "<b>290.</b> HTTP is stateless, which means:",
                "options": ["Server remembers client info", "Server does not remember client info", "Client stores session info", "None of the above"],
                "answer": 1
        },
        {
                "q": "<b>291.</b> HTTPS adds which layer over HTTP?",
                "options": ["TCP", "SSL/TLS", "UDP", "IP"],
                "answer": 1
        },
        {
                "q": "<b>292.</b> Which MIME type represents text data?",
                "options": ["text/html", "image/jpeg", "application/pdf", "audio/mp3"],
                "answer": 0
        },
        {
                "q": "<b>293.</b> Which MIME type represents images?",
                "options": ["text/html", "image/jpeg", "application/pdf", "audio/mp3"],
                "answer": 1
        },
        {
                "q": "<b>294.</b> DNS uses which port for queries?",
                "options": ["53", "80", "443", "21"],
                "answer": 0
        },
        {
                "q": "<b>295.</b> URL consists of:",
                "options": ["Protocol, domain, path", "IP address only", "Port only", "Hostname only"],
                "answer": 0
        },
        {
                "q": "<b>296.</b> HTTP response code 404 indicates:",
                "options": ["OK", "Not Found", "Redirect", "Server error"],
                "answer": 1
        },
        {
                "q": "<b>297.</b> HTTP response code 200 indicates:",
                "options": ["OK", "Not Found", "Redirect", "Server error"],
                "answer": 0
        },
        {
                "q": "<b>298.</b> HTTP uses which transport protocol?",
                "options": ["TCP", "UDP", "ICMP", "IP"],
                "answer": 0
        },
        {
                "q": "<b>299.</b> HTTPS uses which transport protocol?",
                "options": ["TCP", "UDP", "ICMP", "IP"],
                "answer": 0
        },
        {
                "q": "<b>300.</b> DHCP is used for:",
                "options": ["Dynamic IP allocation", "DNS resolution", "Remote login", "File transfer"],
                "answer": 0
        },
        {
                "q": "<b>301.</b> Dynamic IP addresses are assigned by:",
                "options": ["Router", "DHCP server", "DNS server", "FTP server"],
                "answer": 1
        },
        {
                "q": "<b>302.</b> LDAP is used for:",
                "options": ["Directory services", "Email transfer", "File transfer", "Web browsing"],
                "answer": 0
        },
        {
                "q": "<b>303.</b> Which protocol is used for VoIP?",
                "options": ["SIP", "SMTP", "FTP", "HTTP"],
                "answer": 0
        },
        {
                "q": "<b>304.</b> Which port does SIP use by default?",
                "options": ["5060", "80", "443", "25"],
                "answer": 0
        },
        {
                "q": "<b>305.</b> NTP is used for:",
                "options": ["Synchronizing clocks", "Email transfer", "File sharing", "Remote login"],
                "answer": 0
        },
        {
                "q": "<b>306.</b> Port number for NTP:",
                "options": ["23", "123", "80", "25"],
                "answer": 1
        },
        {
                "q": "<b>307.</b> DNS uses which transport protocol?",
                "options": ["UDP (queries), TCP (zone transfer)", "TCP only", "UDP only", "ICMP"],
                "answer": 0
        },
        {
                "q": "<b>308.</b> Telnet transmits data:",
                "options": ["Encrypted", "Plain text", "Compressed", "Binary"],
                "answer": 1
        },
        {
                "q": "<b>309.</b> HTTPS encrypts data using:",
                "options": ["SSL/TLS", "TCP", "IP", "UDP"],
                "answer": 0
        },
        {
                "q": "<b>310.</b> Which application layer protocol is used for video streaming?",
                "options": ["RTP", "SMTP", "FTP", "DNS"],
                "answer": 0
        },
        {
                "q": "<b>311.</b> RTP provides:",
                "options": ["Real-time data transfer", "File transfer", "Email delivery", "DNS resolution"],
                "answer": 0
        },
        {
                "q": "<b>312.</b> SNMP is used for:",
                "options": ["Network management", "File transfer", "Web browsing", "Email"],
                "answer": 0
        },
        {
                "q": "<b>313.</b> Port number for SNMP:",
                "options": ["161", "80", "443", "25"],
                "answer": 0
        },
        {
                "q": "<b>314.</b> HTTP POST method is used to:",
                "options": ["Submit data to server", "Retrieve data", "Delete data", "Update server"],
                "answer": 0
        },
        {
                "q": "<b>315.</b> HTTP GET method is used to:",
                "options": ["Retrieve data", "Submit data", "Delete data", "Authenticate"],
                "answer": 0
        },
        {
                "q": "<b>316.</b> Which protocol allows clients to download files without authentication?",
                "options": ["TFTP", "FTP", "HTTP", "SMTP"],
                "answer": 0
        },
        {
                "q": "<b>317.</b> Application layer protocols provide:",
                "options": ["End-user services", "Reliable delivery", "Routing", "Flow control"],
                "answer": 0
        },
        {
                "q": "<b>318.</b> Which application layer protocol supports email retrieval while keeping emails on server?",
                "options": ["IMAP", "POP3", "SMTP", "FTP"],
                "answer": 0
        },
        {
                "q": "<b>319.</b> Application layer interacts directly with:",
                "options": ["User applications", "Transport layer", "Network layer", "Data link layer"],
                "answer": 0
        },
        {
                "q": "<b>320.</b> IPv6 address length is:",
                "options": ["32 bits", "64 bits", "128 bits", "256 bits"],
                "answer": 2
        },
        {
                "q": "<b>321.</b> IPv6 header does NOT include:",
                "options": ["Checksum", "Source IP", "Next header", "Hop limit"],
                "answer": 0
        },
        {
                "q": "<b>322.</b> IPv6 address type 2001:db8::/32 is:",
                "options": ["Link-local", "Global unicast", "Multicast", "Anycast"],
                "answer": 1
        },
        {
                "q": "<b>323.</b> OSPFv3 supports which IP version?",
                "options": ["IPv4", "IPv6", "Both", "None"],
                "answer": 1
        },
        {
                "q": "<b>324.</b> EIGRP for IPv6 uses:",
                "options": ["Protocol number 88", "Next header field", "Multicast FF02::A", "TCP"],
                "answer": 2
        },
        {
                "q": "<b>325.</b> MPLS stands for:",
                "options": ["Multi-Protocol Label Switching", "Multi-Path Link Switching", "Multi-Protocol Link Sharing", "Multi-Path Label System"],
                "answer": 0
        },
        {
                "q": "<b>326.</b> MPLS label is added after:",
                "options": ["IP header", "TCP header", "Ethernet trailer", "Payload"],
                "answer": 0
        },
        {
                "q": "<b>327.</b> Link-state routing algorithm example:",
                "options": ["RIP", "OSPF", "BGP", "EIGRP"],
                "answer": 1
        },
        {
                "q": "<b>328.</b> Distance-vector routing example:",
                "options": ["OSPF", "RIP", "BGP", "IS-IS"],
                "answer": 1
        },
        {
                "q": "<b>329.</b> BGP is primarily used in:",
                "options": ["LAN", "WAN", "Wireless networks", "Personal networks"],
                "answer": 1
        },
        {
                "q": "<b>330.</b> QoS ensures:",
                "options": ["Packet delivery order", "Bandwidth and latency guarantees", "Encryption", "Routing updates"],
                "answer": 1
        },
        {
                "q": "<b>331.</b> DiffServ uses:",
                "options": ["6-bit DSCP", "8-bit TTL", "16-bit port number", "32-bit sequence number"],
                "answer": 0
        },
        {
                "q": "<b>332.</b> IEEE 802.11 uses:",
                "options": ["CSMA/CD", "CSMA/CA", "TDMA", "FDMA"],
                "answer": 1
        },
        {
                "q": "<b>333.</b> WPA2 improves over WEP by:",
                "options": ["Using RC4", "Using AES encryption", "Using 40-bit key", "Removing encryption"],
                "answer": 1
        },
        {
                "q": "<b>334.</b> VPN ensures:",
                "options": ["Encrypted data transfer", "Faster routing", "Longer IP addresses", "Larger MTU"],
                "answer": 0
        },
        {
                "q": "<b>335.</b> IPSec operates at:",
                "options": ["Network layer", "Data link layer", "Transport layer", "Application layer"],
                "answer": 0
        },
        {
                "q": "<b>336.</b> SSL VPN works at:",
                "options": ["Transport layer", "Network layer", "Application layer", "Data link layer"],
                "answer": 2
        },
        {
                "q": "<b>337.</b> WLAN frequency 5 GHz allows:",
                "options": ["Longer range", "Higher data rate", "Lower bandwidth", "Lower throughput"],
                "answer": 1
        },
        {
                "q": "<b>338.</b> CSMA/CA avoids collisions by:",
                "options": ["Listening before sending", "Acknowledging received packets", "Using labels", "Multiplexing channels"],
                "answer": 0
        },
        {
                "q": "<b>339.</b> Network Address Translation (NAT) converts:",
                "options": ["Private IP to public IP", "MAC to IP", "IPv4 to IPv6", "Hostname to IP"],
                "answer": 0
        },
        {
                "q": "<b>340.</b> SDN separates:",
                "options": ["Control plane and data plane", "IP and MAC", "Transport and network layer", "TCP and UDP"],
                "answer": 0
        },
        {
                "q": "<b>341.</b> OpenFlow protocol is used in:",
                "options": ["SDN", "MPLS", "BGP", "RIP"],
                "answer": 0
        },
        {
                "q": "<b>342.</b> IoT device typically uses:",
                "options": ["CoAP protocol", "FTP", "HTTP only", "SMTP"],
                "answer": 0
        },
        {
                "q": "<b>343.</b> MQTT protocol in IoT is:",
                "options": ["Publish-subscribe", "Request-response", "Distance-vector", "Link-state"],
                "answer": 0
        },
        {
                "q": "<b>344.</b> TLS ensures:",
                "options": ["Encryption, integrity, authentication", "Only encryption", "Only authentication", "Only routing"],
                "answer": 0
        },
        {
                "q": "<b>345.</b> DNSSEC protects against:",
                "options": ["Cache poisoning", "DDoS", "Routing loops", "Collisions"],
                "answer": 0
        },
        {
                "q": "<b>346.</b> MPLS improves:",
                "options": ["Routing speed", "Encryption", "Wireless range", "DNS resolution"],
                "answer": 0
        },
        {
                "q": "<b>347.</b> SD-WAN is used to:",
                "options": ["Optimize WAN traffic", "Encrypt LAN", "Reduce IPv6 addresses", "Increase MAC addresses"],
                "answer": 0
        },
        {
                "q": "<b>348.</b> IPv6 anycast allows:",
                "options": ["Packet to nearest of multiple destinations", "Packet to all nodes", "Packet to single node only", "Packet to default gateway"],
                "answer": 0
        },
        {
                "q": "<b>349.</b> Zero-trust security assumes:",
                "options": ["No device is trusted by default", "LAN is fully trusted", "WAN is untrusted", "Only wireless is untrusted"],
                "answer": 0
        },
        ],
    },
]
