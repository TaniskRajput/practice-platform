"""
Practice Sets — a separate, curated MCQ section distinct from the raw PDF
question banks.

Unlike the PDF-derived quizzes (which are transcriptions of real papers and
inherit whatever repetition and definition-recall style the source had),
these are original, scenario/situational questions: each poses a short
workplace situation and asks what you'd actually do, rather than "what does
X stand for". Every set is exactly 20 questions and no single concept is
tested twice within the same set.

Each question carries its topic and explanation inline (no separate
quiz_explanations.py entry needed) — app.py's grade_quiz() checks
q.get("topic")/q.get("explanation") before falling back to that file.
"""

PRACTICE_SET_TAG = "Practice Set"


def _q(topic, stem, options, answer, explanation):
    return {
        "topic": topic,
        "q": stem,
        "options": options,
        "answer": answer,
        "explanation": explanation,
    }


# ==================================================================== #
# 1. Cloud Fundamentals & Service Models
# ==================================================================== #
CLOUD_FUNDAMENTALS_QUESTIONS = [
    _q(
        "Service models",
        "Your team wants to deploy a web app without managing servers, OS patching, or runtime "
        "installs — you just want to upload code and have it run. Which service model fits?",
        ["IaaS", "PaaS", "SaaS", "On-premises"],
        1,
        "PaaS (Platform as a Service) hands you a ready-to-deploy runtime — you push code, the "
        "platform handles the OS, patching, and scaling underneath. IaaS would still leave you "
        "managing the VM and OS yourself; SaaS is a finished application you'd consume, not build on.",
    ),
    _q(
        "Elasticity",
        "An e-commerce site gets 10x normal traffic during a flash sale, then drops back to "
        "normal a few hours later. Which cloud property lets the infrastructure grow and shrink "
        "automatically to match, without manual intervention?",
        ["Elasticity (auto-scaling)", "High availability", "Fault tolerance", "Vendor lock-in"],
        0,
        "Elasticity is specifically about automatically adding/removing capacity in response to "
        "real-time demand. High availability and fault tolerance are about staying up during "
        "failures — a related but different property.",
    ),
    _q(
        "Deployment models",
        "A hospital must keep patient records on infrastructure it fully controls for regulatory "
        "reasons, but wants to burst non-sensitive analytics workloads to a public cloud for "
        "extra compute during quarterly reporting. Which deployment model is this?",
        ["Public cloud", "Private cloud", "Hybrid cloud", "Community cloud"],
        2,
        "Hybrid cloud combines private infrastructure (for the regulated data) with public cloud "
        "(for the burst workload), connected together. Community cloud is shared among "
        "organizations with similar requirements, not private+public combined.",
    ),
    _q(
        "Vendor lock-in",
        "A company built its entire backend around one provider's proprietary database and "
        "serverless functions. They now want to switch providers but find it would take a "
        "year-long rewrite. What is this risk called?",
        ["Data residency", "Vendor lock-in", "Shared responsibility", "Elasticity"],
        1,
        "Vendor lock-in happens when you depend so heavily on one provider's proprietary "
        "services and APIs that migrating away becomes prohibitively expensive. Using open "
        "standards and containers is the usual mitigation.",
    ),
    _q(
        "Storage types",
        "You need to store millions of user-uploaded profile photos, accessed by URL, with no "
        "fixed size limit and automatic scaling as more photos are added. Which storage type "
        "fits best?",
        ["Block storage", "Object storage", "File storage (NFS)", "In-memory cache"],
        1,
        "Object storage (like S3) is a flat key-value store built exactly for this — unlimited "
        "scale, HTTP-addressable objects, no filesystem hierarchy to manage. Block storage is "
        "for a single attached disk (like a database volume), not for millions of independent files.",
    ),
    _q(
        "Cost models",
        "Your workload runs 24/7 at a predictable, steady load for the next 3 years. Finance "
        "wants the lowest possible cost and doesn't mind committing upfront. What should you buy?",
        ["On-demand instances", "Reserved instances", "Spot instances", "Serverless functions"],
        1,
        "Reserved instances trade a term commitment (1-3 years) for a steep discount versus "
        "on-demand pricing — ideal for steady, predictable workloads. Spot instances are cheaper "
        "still but can be reclaimed anytime, wrong fit for something that must run continuously.",
    ),
    _q(
        "CDN",
        "Your website's users are in India, but your only server is in the US, and static images "
        "load slowly for them. What should you add to fix this without moving your server?",
        ["A bigger EC2 instance", "A Content Delivery Network (CDN)", "A VPN", "A hypervisor"],
        1,
        "A CDN caches static content (images, JS, CSS) on edge servers close to users worldwide, "
        "so a request from India is served from a nearby edge node instead of round-tripping to "
        "the US origin server.",
    ),
    _q(
        "Scaling strategy",
        "A database server is running out of capacity. Instead of adding more servers, you "
        "upgrade it to a machine with more CPU and RAM. What kind of scaling is this?",
        ["Horizontal scaling", "Vertical scaling", "Auto-scaling", "Load balancing"],
        1,
        "Vertical scaling ('scaling up') means making one machine bigger. Horizontal scaling "
        "('scaling out') means adding more machines instead — usually preferred for very large "
        "scale since a single machine has an upper physical limit.",
    ),
    _q(
        "Load balancing",
        "You have 5 identical web servers behind a single public endpoint, and traffic needs to "
        "be spread evenly across them so no one server is overwhelmed. What component does this?",
        ["A load balancer", "A firewall", "A CDN", "A VPN gateway"],
        0,
        "A load balancer sits in front of a pool of servers and distributes incoming requests "
        "across them (round-robin or by load), and can also stop sending traffic to an unhealthy "
        "instance automatically.",
    ),
    _q(
        "Availability Zones",
        "You want your application to survive an entire data center going offline (power outage, "
        "fire, etc.), not just a single server failing. What should you deploy across?",
        ["Multiple servers in one rack", "Multiple Availability Zones", "Multiple containers on one host", "Multiple browser tabs"],
        1,
        "An Availability Zone is an isolated data center within a region; deploying across "
        "multiple AZs means one facility's total failure doesn't take your application down, "
        "since the others keep serving traffic.",
    ),
    _q(
        "Serverless",
        "You need to resize an image every time one is uploaded, but this happens randomly and "
        "rarely — sometimes 100 times a day, sometimes zero. You don't want to pay for an idle "
        "server waiting for uploads. What fits best?",
        ["A dedicated always-on VM", "A serverless function (FaaS)", "A private data center", "A load balancer"],
        1,
        "Serverless/FaaS (like Lambda) runs your code only when triggered (here, on each upload) "
        "and you pay per execution — nothing runs, nothing is billed, when there's no event.",
    ),
    _q(
        "Storage tiers",
        "Your company must legally retain financial records for 10 years but will almost never "
        "read them back. What storage tier minimizes cost for this?",
        ["Standard/hot storage", "Cold/archive storage", "In-memory cache", "Block storage"],
        1,
        "Archive/cold storage tiers (like Glacier) are priced for exactly this: data you rarely "
        "touch, in exchange for the cheapest per-GB cost and slower retrieval when you do need it.",
    ),
    _q(
        "Data residency",
        "A German customer's data must, by local law, remain stored within the EU. Which cloud "
        "decision directly satisfies this requirement?",
        ["Choosing the EU region for that customer's data", "Encrypting the data", "Using a CDN", "Enabling auto-scaling"],
        0,
        "Data residency requirements are satisfied by physically choosing a region within the "
        "required jurisdiction to store the data — encryption or CDNs don't change WHERE the "
        "data legally sits.",
    ),
    _q(
        "High availability vs DR",
        "Your app runs across 3 AZs so a single AZ outage causes zero downtime — but you also "
        "keep a separate backup copy of the whole system in another region in case the entire "
        "primary region goes down. The second part (separate region backup) is an example of:",
        ["High availability", "Disaster recovery", "Elasticity", "Vendor lock-in"],
        1,
        "High availability handles routine, smaller-scale failures (one AZ) with near-zero "
        "downtime. Disaster recovery is the plan for a catastrophic, larger-scale event (a whole "
        "region down) — it's a separate concern with its own RTO/RPO targets.",
    ),
    _q(
        "Managed services",
        "Your DBA team is spending most of its time on routine patching, backups, and failover "
        "configuration instead of query optimization. What would free them up?",
        ["Migrating to a managed database service", "Adding more RAM", "Enabling a CDN", "Switching to object storage"],
        0,
        "A managed database service (like RDS) takes over patching, backups, and failover "
        "automatically, so the DBA team can focus on schema design and query tuning instead of "
        "operational upkeep.",
    ),
    _q(
        "Lifecycle policies",
        "Log files are frequently accessed for the first 30 days, rarely after that, and never "
        "after a year — but must be kept for 7 years for compliance. What avoids you manually "
        "moving them between storage tiers?",
        ["A lifecycle policy", "A load balancer", "A VPN", "An IAM role"],
        0,
        "A storage lifecycle policy automatically transitions objects between tiers (hot → "
        "infrequent access → archive) based on age, and can also auto-delete after the retention "
        "period — no manual intervention needed.",
    ),
    _q(
        "Multi-cloud",
        "After a major outage at their single cloud provider took their entire business offline "
        "for 6 hours, a company decides to split critical workloads across two different cloud "
        "providers. What strategy is this?",
        ["Hybrid cloud", "Multi-cloud", "Vertical scaling", "Serverless computing"],
        1,
        "Multi-cloud specifically means using two or more different PUBLIC cloud providers "
        "(as opposed to hybrid, which mixes private infrastructure with one public cloud) — "
        "usually done to avoid a single provider being a single point of failure.",
    ),
    _q(
        "Billing model",
        "A startup likes cloud computing because they pay only for what they use, hour by hour, "
        "with no large upfront hardware purchase. What billing concept does this describe?",
        ["Capital expenditure (CapEx)", "Pay-as-you-go (OpEx)", "Reserved pricing", "Flat annual licensing"],
        1,
        "Pay-as-you-go shifts spending from CapEx (buying hardware upfront) to OpEx (paying "
        "incrementally for usage) — a major reason startups favor cloud over building their own "
        "data centers.",
    ),
    _q(
        "API rate limiting",
        "Your public API is being hit so hard by a few clients that it's slowing down for "
        "everyone else. What should sit in front of the API to cap how many requests each client "
        "can make per minute?",
        ["An API gateway with throttling", "A CDN", "Cold storage", "A hypervisor"],
        0,
        "An API gateway centralizes authentication, logging, and throttling/rate-limiting for "
        "API traffic, so one noisy client can be capped without affecting others or requiring "
        "every backend service to implement its own limiting.",
    ),
    _q(
        "Cloud bursting",
        "A retailer normally runs its inventory system entirely on-premises, but during Black "
        "Friday it temporarily overflows extra load onto a public cloud provider before scaling "
        "back down afterward. What is this pattern called?",
        ["Cloud bursting", "Vendor lock-in", "Data sovereignty", "Vertical scaling"],
        0,
        "Cloud bursting is exactly this pattern: a primarily on-prem (or private cloud) "
        "workload temporarily 'bursts' extra capacity into the public cloud only during demand "
        "spikes, then retreats back.",
    ),
]


# ==================================================================== #
# 2. Cloud Security & Shared Responsibility
# ==================================================================== #
CLOUD_SECURITY_QUESTIONS = [
    _q(
        "Shared responsibility (IaaS)",
        "You've provisioned a virtual machine on IaaS. A breach occurs because you never applied "
        "the latest OS security patch. Whose responsibility was that patch, under the shared "
        "responsibility model?",
        ["The cloud provider's", "Yours (the customer's)", "Neither — it's automatic", "The hypervisor vendor's"],
        1,
        "On IaaS, the provider secures the physical infrastructure and hypervisor; everything "
        "from the guest OS upward — patching, users, application, data — is the customer's job. "
        "This is the single most commonly tested shared-responsibility scenario.",
    ),
    _q(
        "Shared responsibility (SaaS)",
        "You use a SaaS email platform. A phishing email gets through because YOUR company "
        "disabled the provider's optional advanced threat filtering to save cost. Who bears "
        "responsibility for that gap?",
        ["The provider — SaaS means they secure everything", "You — you control your own configuration choices", "Nobody, SaaS has no shared responsibility", "The email sender"],
        1,
        "Even in SaaS, where the provider manages the most, the customer still owns their own "
        "configuration choices, user access, and data — 'shared responsibility' never disappears "
        "entirely, it just shifts more toward the provider as you move IaaS → PaaS → SaaS.",
    ),
    _q(
        "Least privilege",
        "A junior developer only needs to read from one specific database table for their task, "
        "but is granted full admin access to the entire cloud account 'to be safe.' What "
        "principle is being violated?",
        ["Least privilege", "Defense in depth", "Zero trust", "Non-repudiation"],
        0,
        "Least privilege means granting only the minimum access needed for the task at hand. "
        "Over-provisioning access (like full admin for a read-only task) massively increases the "
        "damage if that developer's account is ever compromised.",
    ),
    _q(
        "MFA",
        "An attacker obtains a cloud admin's password through a data breach on an unrelated "
        "site (password reuse). What single control would have stopped them from logging in "
        "with just that password?",
        ["A stronger firewall rule", "Multi-factor authentication (MFA)", "A CDN", "Object storage encryption"],
        1,
        "MFA requires a second factor (a code from a phone, a hardware token) beyond the "
        "password alone, so a leaked/reused password by itself isn't enough to log in.",
    ),
    _q(
        "Encryption",
        "Your company needs to protect customer data sitting in cloud storage from anyone who "
        "might gain physical or unauthorized access to the storage disks themselves. Which "
        "control directly addresses this?",
        ["Encryption at rest", "Encryption in transit", "A CDN", "Auto-scaling"],
        0,
        "Encryption AT REST protects stored data — even if someone accessed the raw disk, they'd "
        "only see ciphertext without the key. Encryption in transit protects data while it's "
        "moving across a network, which is a different threat.",
    ),
    _q(
        "Key management",
        "A financial services company wants to control and rotate its own encryption keys "
        "rather than letting the cloud provider fully manage them, for extra assurance. What "
        "should they use?",
        ["Provider-managed keys", "Customer-managed keys (via KMS)", "No encryption", "A CDN"],
        1,
        "Customer-managed keys give the customer control over key creation, rotation policy, "
        "and revocation, while provider-managed keys are simpler but hand that control entirely "
        "to the platform.",
    ),
    _q(
        "Security groups",
        "You launch a new database server in your cloud VPC and want to make sure only your "
        "application servers (not the whole internet) can connect to its database port. What "
        "should you configure?",
        ["A CDN rule", "A security group restricting inbound traffic to the app servers", "A storage lifecycle policy", "A reserved instance"],
        1,
        "A security group acts as a virtual, stateful firewall on the instance's network "
        "interface — you'd restrict inbound access on the DB port to only the source IPs/security "
        "group of your application tier, not 0.0.0.0/0 (the whole internet).",
    ),
    _q(
        "Misconfiguration",
        "A researcher finds your company's customer database backup sitting in a storage bucket "
        "that anyone on the internet can read, with no authentication required. What category of "
        "failure is this, most precisely?",
        ["A zero-day vulnerability", "A misconfiguration", "A DDoS attack", "A supply chain attack"],
        1,
        "This is a classic cloud misconfiguration (public storage bucket) — the leading cause of "
        "real-world cloud data breaches, and entirely preventable, unlike a zero-day which "
        "requires an unpatched software flaw.",
    ),
    _q(
        "CSPM",
        "Your security team wants a tool that continuously scans all cloud accounts for risky "
        "settings (like the public bucket above) and either alerts or auto-remediates them. What "
        "category of tool is this?",
        ["CSPM (Cloud Security Posture Management)", "CDN", "Load balancer", "Hypervisor"],
        0,
        "CSPM tools continuously monitor cloud configurations against best-practice baselines "
        "and flag or fix drift — exactly the ongoing misconfiguration-detection need described here.",
    ),
    _q(
        "CASB",
        "Employees are signing up for unapproved SaaS apps with their corporate email without "
        "IT's knowledge, and sensitive files are ending up there. What tool gives IT visibility "
        "and control over this kind of unsanctioned SaaS usage?",
        ["A CASB (Cloud Access Security Broker)", "A hypervisor", "An object storage lifecycle policy", "A reserved instance"],
        0,
        "A CASB sits between users and cloud services to give visibility into (and control over) "
        "SaaS usage across the organization — including the 'shadow IT' apps employees adopt "
        "without going through official channels.",
    ),
    _q(
        "Zero Trust",
        "Since shifting to remote work, your company no longer assumes a device is safe just "
        "because it's on the corporate VPN — every request is authenticated and authorized "
        "regardless of network location. What security model is this?",
        ["Perimeter security", "Zero Trust", "Defense in depth (only)", "Air-gapping"],
        1,
        "Zero Trust's core idea is 'never trust, always verify' — no request is implicitly "
        "trusted just because of where it came from (like being on the VPN); every request is "
        "checked on its own merits.",
    ),
    _q(
        "RBAC",
        "A cloud account has 50 employees across 5 job functions. Instead of configuring "
        "permissions individually for each of the 50 people, the admin creates 5 permission sets "
        "and assigns each person to the matching one. What access control model is this?",
        ["Discretionary Access Control (DAC)", "Role-Based Access Control (RBAC)", "Mandatory Access Control (MAC)", "No access control"],
        1,
        "RBAC ties permissions to ROLES (job functions) rather than individuals, so managing "
        "access for a large team scales — you assign the role, not 50 separate permission sets.",
    ),
    _q(
        "Audit logging",
        "After a suspicious change to a production database's permissions, your team needs to "
        "find out exactly who made the change, from where, and when. What should already have "
        "been enabled to make this possible?",
        ["A CDN", "Audit/API call logging", "Auto-scaling", "A storage lifecycle policy"],
        1,
        "Audit logging (like CloudTrail-style API call logs) records who did what, from where, "
        "and when — without it enabled beforehand, this kind of forensic question often can't be "
        "answered after the fact.",
    ),
    _q(
        "Secrets management",
        "A developer accidentally commits an API key directly inside a Python file that gets "
        "pushed to a public GitHub repo. What should have been used instead to avoid this "
        "exposure?",
        ["A secrets manager, referenced at runtime", "A bigger EC2 instance", "A CDN", "Object storage"],
        0,
        "Secrets managers store credentials outside the codebase and hand them to the "
        "application at runtime with audited, revocable access — so a leaked source repo never "
        "exposes the actual key.",
    ),
    _q(
        "DLP",
        "Your company wants to automatically block any attempt by an employee to upload a file "
        "containing credit card numbers to a personal cloud storage account. What technology "
        "does this?",
        ["Data Loss Prevention (DLP)", "A load balancer", "A hypervisor", "Auto-scaling"],
        0,
        "DLP tools inspect data in motion (and at rest) for sensitive patterns like card numbers "
        "or PII, and can block, quarantine, or alert on policy violations like this exfiltration "
        "attempt.",
    ),
    _q(
        "Compliance retention",
        "A regulation requires your company to retain access logs for at least 3 years for audit "
        "purposes. Where does this requirement most directly get enforced in your cloud setup?",
        ["In the load balancer configuration", "In a log retention/lifecycle policy", "In the CDN cache settings", "In the hypervisor"],
        1,
        "A log retention policy (a form of lifecycle policy applied to logs) is what enforces "
        "'keep this data for exactly X years, then handle appropriately' — matching a compliance "
        "requirement to an actual technical control.",
    ),
    _q(
        "Immutable infrastructure",
        "Instead of logging into servers to apply patches and fix drift over time, your platform "
        "team builds a new hardened image for every release and replaces old servers entirely. "
        "Why is this considered more secure?",
        ["It's cheaper", "It prevents configuration drift and undocumented changes from accumulating", "It requires no encryption", "It disables logging"],
        1,
        "Immutable infrastructure means every server starts from a known-good, hardened image "
        "and is never modified in place — so there's no risk of drift where ad-hoc manual "
        "changes accumulate into an undocumented, insecure state over time.",
    ),
    _q(
        "JIT access",
        "An admin needs elevated permissions for a 2-hour maintenance window, after which those "
        "permissions should automatically expire rather than remaining active indefinitely. What "
        "access pattern is this?",
        ["Just-In-Time (JIT) privileged access", "Least privilege (alone)", "RBAC (alone)", "MFA"],
        0,
        "JIT access grants elevated rights only for the specific window needed and automatically "
        "revokes them afterward — reducing the amount of time a standing, always-privileged "
        "account exists for an attacker to steal.",
    ),
    _q(
        "Incident response",
        "Your team detects that a cloud server has been compromised and is actively "
        "communicating with an external attacker. What should be the FIRST action?",
        ["Isolate/contain the affected server from the network", "Immediately delete all logs", "Wait and monitor for a week", "Restart the whole cloud account"],
        0,
        "Containment comes first in incident response — isolate the compromised system to stop "
        "further damage or lateral movement, before moving on to investigation (never delete "
        "logs) and eradication/recovery.",
    ),
    _q(
        "Ransomware defense",
        "After a ransomware attack encrypts production data, the company discovers their backups "
        "were also encrypted because they were mounted as a regular writable network drive. What "
        "backup design would have prevented this?",
        ["Storing backups on the same server as production", "Immutable/offline (air-gapped) backups", "Skipping backups entirely", "A CDN"],
        1,
        "Immutable or offline backups can't be altered or encrypted by ransomware that has "
        "compromised the production environment, because they're either write-once or "
        "physically/logically disconnected — the classic gap in this scenario was backups being "
        "reachable and writable from the infected network.",
    ),
]


# ==================================================================== #
# 3. Network Security — Attacks & Defenses
# ==================================================================== #
NETWORK_SECURITY_QUESTIONS = [
    _q(
        "Phishing",
        "You receive an email that looks like it's from your bank, urging you to click a link "
        "and 're-verify your account' immediately or it will be suspended. What is this an "
        "example of?",
        ["A DDoS attack", "Phishing", "A brute-force attack", "A zero-day exploit"],
        1,
        "Phishing uses a fake but convincing message (often urgent) to trick you into clicking a "
        "malicious link or handing over credentials. The urgency ('act now or else') is a classic "
        "social-engineering pressure tactic.",
    ),
    _q(
        "DDoS",
        "A company's website suddenly becomes unreachable after receiving a massive flood of "
        "traffic from thousands of different IP addresses simultaneously. What attack is this?",
        ["SQL injection", "DDoS (Distributed Denial of Service)", "Man-in-the-middle", "Phishing"],
        1,
        "DDoS floods a target from many distributed sources at once, overwhelming its capacity "
        "so legitimate users can't get through. The 'distributed' (many sources) part "
        "distinguishes it from a simple single-source DoS.",
    ),
    _q(
        "MITM",
        "An employee connects to free public airport WiFi and logs into the company portal over "
        "plain HTTP. An attacker on the same network intercepts and reads the credentials in "
        "transit. What attack allowed this?",
        ["Ransomware", "Man-in-the-Middle (MITM)", "SQL injection", "Insider threat"],
        1,
        "MITM means an attacker positions themselves between two communicating parties and "
        "eavesdrops or alters the traffic — exactly what unencrypted HTTP on a shared public "
        "network exposes. HTTPS (encrypted in transit) is the fix.",
    ),
    _q(
        "SQL injection",
        "A login form takes a username and password and inserts them directly into a SQL query "
        "without sanitization. An attacker enters a specially crafted username that lets them "
        "bypass the login entirely. What vulnerability is this?",
        ["Cross-Site Scripting (XSS)", "SQL injection", "DDoS", "MITM"],
        1,
        "SQL injection happens when untrusted input is concatenated directly into a SQL query, "
        "letting the attacker inject their own SQL logic. Parameterized queries (prepared "
        "statements) are the standard fix.",
    ),
    _q(
        "XSS",
        "A website lets users post comments, and one attacker posts a comment containing a "
        "`<script>` tag that runs in every other visitor's browser who views that page, stealing "
        "their session cookies. What vulnerability is this?",
        ["Cross-Site Scripting (XSS)", "SQL injection", "DDoS", "Ransomware"],
        0,
        "XSS injects malicious script into a page that then runs in OTHER users' browsers when "
        "they view it — the giveaway here is script executing client-side in visitors' browsers, "
        "not the database being manipulated.",
    ),
    _q(
        "Ransomware",
        "Employees suddenly can't open any files on the shared drive — everything now has a "
        "strange extension, and a text file demands payment in cryptocurrency to restore access. "
        "What is happening?",
        ["A DDoS attack", "Ransomware", "A phishing attempt (in progress)", "A firewall misconfiguration"],
        1,
        "Ransomware encrypts victim files and demands payment for the decryption key. The best "
        "recovery is restoring from clean, offline backups — paying doesn't guarantee you get "
        "usable data back.",
    ),
    _q(
        "IDS vs IPS",
        "Your security team wants a system that not only detects a malicious packet but "
        "automatically blocks it inline before it reaches its target, rather than just raising "
        "an alert. What should they deploy?",
        ["An IDS (Intrusion Detection System)", "An IPS (Intrusion Prevention System)", "A CDN", "A DNS server"],
        1,
        "An IDS only detects and alerts — it doesn't block. An IPS sits inline and actively "
        "blocks malicious traffic in real time, which is what 'automatically blocks it before it "
        "reaches its target' describes.",
    ),
    _q(
        "WAF",
        "Your public-facing web application keeps getting hit with SQL injection and XSS attempts "
        "through its HTTP requests. What security appliance is specifically designed to filter "
        "these at the application layer?",
        ["A Web Application Firewall (WAF)", "A regular network firewall", "A VPN", "A hypervisor"],
        0,
        "A WAF inspects HTTP/HTTPS traffic at layer 7 and blocks known web application attack "
        "patterns like SQLi and XSS — a regular network firewall only filters by IP/port, not "
        "by request content.",
    ),
    _q(
        "Brute force",
        "An attacker is repeatedly trying thousands of password combinations against a login "
        "endpoint in rapid succession. What control would most directly stop this?",
        ["Account lockout / rate limiting after failed attempts", "A CDN", "Encryption at rest", "A load balancer"],
        0,
        "Rate limiting or temporarily locking an account after repeated failed attempts directly "
        "blocks brute-force guessing at scale, by making rapid-fire attempts impractical.",
    ),
    _q(
        "Symmetric vs asymmetric",
        "Two parties who have never met before need to securely agree on a shared secret key "
        "over an insecure public channel, without ever having exchanged a key in person. What "
        "type of cryptography makes this possible?",
        ["Symmetric encryption", "Asymmetric (public-key) encryption", "Hashing", "No cryptography can do this"],
        1,
        "Asymmetric cryptography uses a public/private key pair, so two strangers can establish "
        "a shared secret over an insecure channel (e.g. via Diffie-Hellman) without ever having "
        "met to exchange keys beforehand — something symmetric encryption alone can't do.",
    ),
    _q(
        "Digital signatures",
        "You download a software update and want to verify it genuinely came from the vendor and "
        "wasn't tampered with in transit. What should you check?",
        ["The file's digital signature", "The file's size only", "The download speed", "The file extension"],
        0,
        "A digital signature, created with the vendor's private key, lets you verify (with their "
        "public key) both authenticity (it really came from them) and integrity (it wasn't "
        "altered) — file size or extension prove neither.",
    ),
    _q(
        "PKI / certificates",
        "Your browser shows a warning that a website's SSL certificate is invalid or "
        "self-signed, unrelated to any trusted authority. What risk does this warning represent?",
        ["The site might be slow", "You might be connecting to an imposter site (MITM risk)", "The site uses too much bandwidth", "The site is using UDP"],
        1,
        "A certificate is how a browser verifies it's really talking to the claimed site, "
        "issued by a trusted Certificate Authority. An invalid/untrusted certificate means that "
        "verification failed — a red flag for a MITM or spoofed site.",
    ),
    _q(
        "VPN",
        "Two company offices in different cities need their internal networks to communicate as "
        "if they were on the same LAN, securely, over the public internet. What should connect "
        "them?",
        ["A site-to-site VPN", "A CDN", "A WAF", "Plain HTTP"],
        0,
        "A site-to-site VPN builds an encrypted tunnel between two networks (not just one user), "
        "letting devices on both sides communicate securely as though on one private network.",
    ),
    _q(
        "Insider threat",
        "A recently terminated employee, whose account access wasn't immediately revoked, logs "
        "back in and deletes critical files out of spite. What category of threat is this?",
        ["A DDoS attack", "An insider threat", "A zero-day exploit", "A supply chain attack"],
        1,
        "An insider threat comes from someone with legitimate (or recently legitimate) access — "
        "here, the failure was not revoking access immediately upon termination, a basic offboarding "
        "control gap.",
    ),
    _q(
        "Vulnerability scan vs pentest",
        "Your team runs an automated tool weekly that checks all servers against a database of "
        "known vulnerabilities and produces a report. Separately, once a year, a hired team "
        "actively tries to break in like a real attacker would. The weekly automated check is:",
        ["Penetration testing", "Vulnerability scanning", "Social engineering", "Incident response"],
        1,
        "Vulnerability scanning is automated and checks against known-issue databases — broad "
        "but shallow. Penetration testing is the manual, authorized attempt to actually exploit "
        "weaknesses — the once-a-year hired-team activity in this scenario.",
    ),
    _q(
        "Patch management",
        "A company is breached through a vulnerability that was publicly disclosed and patched "
        "by the vendor eight months earlier, but the fix was never applied to the affected "
        "server. What failure does this represent?",
        ["A zero-day exploit", "Poor patch management", "A DDoS attack", "Data residency violation"],
        1,
        "A zero-day means no patch existed yet. Here a patch existed for 8 months and simply "
        "wasn't applied — that's a patch management failure, and statistically the more common "
        "cause of real breaches than true zero-days.",
    ),
    _q(
        "MFA methods",
        "Security researchers point out that SMS-based one-time codes can be intercepted via "
        "SIM-swapping attacks. What alternative MFA method is considered stronger?",
        ["Using a longer password instead", "An authenticator app or hardware security key", "Disabling MFA entirely", "Emailing the code instead"],
        1,
        "Authenticator apps (TOTP) and hardware keys (like FIDO2/U2F) don't rely on the mobile "
        "network, so they're immune to SIM-swap interception — a well-known weakness of SMS-based "
        "MFA specifically.",
    ),
    _q(
        "Pretexting",
        "Someone calls the IT helpdesk claiming to be a senior executive who is 'locked out and "
        "in an urgent meeting,' pressuring the technician to reset a password without normal "
        "identity verification. What social engineering technique is this?",
        ["Phishing", "Pretexting", "Tailgating", "Baiting"],
        1,
        "Pretexting is inventing a believable false scenario and identity to manipulate someone "
        "into an action (like a password reset) they normally wouldn't do without proper "
        "verification — the fabricated urgency and authority claim are the giveaways.",
    ),
    _q(
        "Physical security",
        "An unauthorized person walks into a secure server room right behind an employee who "
        "badges in, without presenting their own credentials. What is this called, and what "
        "physical control best prevents it?",
        ["Phishing; prevented by a firewall", "Tailgating; prevented by a mantrap (interlocking doors)", "SQL injection; prevented by a WAF", "DDoS; prevented by rate limiting"],
        1,
        "Tailgating is following an authorized person through a secured door without your own "
        "credentials. A mantrap (a small space with two interlocking doors, only one open at a "
        "time) directly prevents this by only ever letting one verified person through at a time.",
    ),
    _q(
        "Security awareness",
        "Despite having firewalls, antivirus, and email filtering in place, employees still "
        "regularly click on convincing phishing links. What additional control most directly "
        "addresses this remaining gap?",
        ["A bigger firewall", "Ongoing security awareness training", "More antivirus licenses", "A faster network"],
        1,
        "Phishing targets human judgment, not a technical vulnerability — no firewall or "
        "antivirus can fully stop a person from choosing to click. Regular awareness training "
        "(and simulated phishing tests) is what actually closes this human-factor gap.",
    ),
]


# ==================================================================== #
# 4. Networking Fundamentals — OSI, Protocols & Ports
# ==================================================================== #
NETWORKING_FUNDAMENTALS_QUESTIONS = [
    _q(
        "OSI layer 3 (routing)",
        "A router needs to decide which path a packet should take to reach a destination on a "
        "completely different network. Which OSI layer is responsible for this?",
        ["Physical layer", "Data Link layer", "Network layer", "Transport layer"],
        2,
        "The Network layer (layer 3) handles logical addressing (IP) and routing between "
        "different networks. Routers are layer-3 devices for exactly this reason.",
    ),
    _q(
        "OSI layer 2 (switching)",
        "A switch needs to decide which specific port to forward a frame out of, based on the "
        "destination's hardware address. Which OSI layer handles this?",
        ["Physical layer", "Data Link layer", "Network layer", "Session layer"],
        1,
        "The Data Link layer (layer 2) handles MAC addressing and frame delivery within a local "
        "network segment — which is exactly what a switch uses to decide which port to forward "
        "a frame to.",
    ),
    _q(
        "TCP vs UDP",
        "You're building a live video call feature where a few dropped frames are acceptable but "
        "any added delay from retransmission would make the call unusable. Which transport "
        "protocol fits?",
        ["TCP", "UDP", "FTP", "SMTP"],
        1,
        "UDP is connectionless with no retransmission or ordering guarantees, trading reliability "
        "for low latency — ideal for real-time media where a late-arriving retransmitted frame is "
        "worse than just dropping it.",
    ),
    _q(
        "DNS",
        "You type 'example.com' into your browser, and before it can connect to anything, your "
        "computer needs to find out what IP address that name maps to. What service handles this?",
        ["DHCP", "DNS", "SMTP", "ARP"],
        1,
        "DNS translates human-readable domain names into IP addresses — without this lookup, "
        "your browser has no address to actually connect to.",
    ),
    _q(
        "DHCP",
        "A new laptop joins the office WiFi and automatically receives an IP address, subnet "
        "mask, default gateway, and DNS server — with no manual configuration by the user. What "
        "protocol made this automatic?",
        ["DHCP", "DNS", "HTTP", "ARP"],
        0,
        "DHCP automatically assigns IP configuration to devices joining a network, which is why "
        "a new laptop 'just works' on WiFi without anyone typing in an IP address by hand.",
    ),
    _q(
        "SSH",
        "A system administrator needs to securely log into and run commands on a remote Linux "
        "server over the internet, with the session fully encrypted. Which protocol and port "
        "should they use?",
        ["Telnet, port 23", "SSH, port 22", "HTTP, port 80", "FTP, port 21"],
        1,
        "SSH provides encrypted remote login on port 22. Telnet does the same job but in "
        "plaintext (port 23) — a security downgrade that SSH replaced for exactly this reason.",
    ),
    _q(
        "HTTPS",
        "A customer is entering their credit card details on an online checkout page. What port "
        "should the site be using to ensure this traffic is encrypted?",
        ["Port 80 (HTTP)", "Port 443 (HTTPS)", "Port 21 (FTP)", "Port 25 (SMTP)"],
        1,
        "Port 443 is HTTPS — HTTP wrapped in TLS encryption. Port 80 (plain HTTP) would send the "
        "card details unencrypted, which is unacceptable for a payment page.",
    ),
    _q(
        "SMTP",
        "An application needs to send an automated 'order confirmed' email to a customer. What "
        "protocol is used to actually transmit that email to the recipient's mail server?",
        ["POP3", "IMAP", "SMTP", "FTP"],
        2,
        "SMTP is used to SEND mail between servers. POP3 and IMAP are both about a client "
        "RETRIEVING mail that's already arrived — the direction of travel is the key distinction.",
    ),
    _q(
        "Subnetting",
        "Your network uses the subnet mask 255.255.255.240 for a small segment. How many usable "
        "host addresses does this subnet provide?",
        ["16", "14", "30", "62"],
        1,
        "255.255.255.240 is a /28, leaving 4 host bits: 2⁴ = 16 total addresses, minus 1 for the "
        "network address and 1 for the broadcast address = 14 usable hosts.",
    ),
    _q(
        "VPN vs leased line",
        "A company wants to connect two branch offices so their internal networks can "
        "communicate, but a dedicated leased line is too expensive for their budget. What's the "
        "lower-cost alternative that still gives them a secure connection over the internet?",
        ["A site-to-site VPN", "A public WiFi hotspot", "A CDN", "Plain unencrypted internet routing"],
        0,
        "A site-to-site VPN gives you an encrypted tunnel over the existing public internet — "
        "far cheaper than a dedicated leased line, while still keeping the traffic between "
        "offices private.",
    ),
    _q(
        "NAT",
        "An office has 50 employee devices but the ISP has only assigned the company a single "
        "public IP address. How can all 50 devices still reach the internet simultaneously?",
        ["DNS", "NAT (Network Address Translation)", "DHCP", "SSH"],
        1,
        "NAT translates many private internal IP addresses to one shared public IP (typically "
        "using different port numbers to track each device's connections), letting many devices "
        "share a single public address.",
    ),
    _q(
        "Network devices",
        "Your office network is getting slow because every device's traffic is broadcast to "
        "every other device (like an old hub setup). What device should replace the hub to send "
        "traffic only to its intended destination port?",
        ["Another hub", "A switch", "A modem", "A repeater"],
        1,
        "A switch learns which MAC address is on which port and forwards frames only to the "
        "relevant port, instead of broadcasting to everyone like a hub does — directly fixing "
        "this kind of congestion.",
    ),
    _q(
        "Bandwidth vs latency",
        "A user has a 500 Mbps internet connection (confirmed by a speed test) but still "
        "experiences a noticeable delay/lag during video calls to a server on another continent. "
        "What is actually causing the lag?",
        ["Insufficient bandwidth", "High latency (propagation delay)", "A DNS misconfiguration", "A weak WiFi password"],
        1,
        "Bandwidth (capacity) and latency (delay) are different things — a fast connection can "
        "still have high latency due to physical distance and the speed of signal propagation, "
        "which a bandwidth speed test doesn't measure.",
    ),
    _q(
        "ICMP",
        "A network engineer wants to test whether a remote server is reachable and measure the "
        "round-trip time to it, using the 'ping' command. What protocol does ping rely on?",
        ["TCP", "UDP", "ICMP", "ARP"],
        2,
        "Ping uses ICMP echo request/reply messages specifically designed for network "
        "diagnostics like reachability testing and round-trip time measurement — it isn't a "
        "TCP or UDP-based tool.",
    ),
    _q(
        "VLANs",
        "A company wants guest WiFi visitors to be able to access the internet but be completely "
        "isolated from the internal corporate network on the same physical switches. What "
        "technology achieves this logical separation?",
        ["A VLAN (Virtual LAN)", "A longer subnet mask", "NAT", "A CDN"],
        0,
        "A VLAN logically segments a physical network into separate broadcast domains, so guest "
        "and corporate traffic can share the same physical switches while remaining completely "
        "isolated from each other at layer 2.",
    ),
    _q(
        "Wireless security",
        "Your office is still using an older wireless security protocol from years ago. A "
        "security audit recommends upgrading to the current standard for the strongest available "
        "protection. Which should you upgrade to?",
        ["WEP", "WPA", "WPA3", "No encryption (open network)"],
        2,
        "WPA3 is the current Wi-Fi security standard, offering stronger encryption and "
        "resistance to offline password-guessing attacks compared to the older, now-broken WEP "
        "and the superseded WPA.",
    ),
    _q(
        "Network segmentation",
        "A retailer must isolate the systems that process credit card payments from the rest of "
        "the corporate network, as required by PCI DSS compliance. What networking practice "
        "achieves this?",
        ["Network segmentation", "Increasing bandwidth", "Using a CDN", "Disabling DHCP"],
        0,
        "Segmentation isolates sensitive systems into their own network zone with controlled "
        "access between zones — exactly what compliance frameworks like PCI DSS require for "
        "systems handling cardholder data.",
    ),
    _q(
        "Bandwidth-delay product",
        "A satellite internet link has decent bandwidth on paper, but file transfers over it are "
        "much slower than expected because the sender keeps waiting for acknowledgments across "
        "the very high round-trip delay before sending more data. What networking concept "
        "explains why a bigger TCP window would help here?",
        ["The bandwidth-delay product", "NAT", "DNS caching", "VLAN tagging"],
        0,
        "The bandwidth-delay product tells you how much data can be 'in flight' unacknowledged "
        "at once; over a high-delay link, a small TCP window means the sender constantly stalls "
        "waiting for ACKs instead of keeping the pipe full — a larger window fixes exactly this.",
    ),
    _q(
        "IPv4 exhaustion",
        "The organization's ISP explains that the pool of available public IPv4 addresses is "
        "nearly exhausted globally. What longer-term addressing solution is designed to solve "
        "this at the protocol level (rather than just conserving IPv4 via NAT)?",
        ["NAT", "IPv6", "DHCP", "VLANs"],
        1,
        "IPv6 uses 128-bit addresses (an effectively unlimited space) specifically to solve IPv4 "
        "exhaustion at the protocol level. NAT is a workaround that conserves IPv4 addresses but "
        "doesn't solve the underlying scarcity.",
    ),
    _q(
        "Duplex modes",
        "During a video call, both participants can speak and be heard by the other "
        "simultaneously, without needing to take turns. What transmission mode describes this?",
        ["Simplex", "Half duplex", "Full duplex", "Broadcast only"],
        2,
        "Full duplex allows simultaneous two-way communication, like a phone call. Half duplex "
        "(like a walkie-talkie) only allows one direction at a time; simplex is one-way only.",
    ),
]


# ==================================================================== #
# 5. DevOps & Containers
# ==================================================================== #
DEVOPS_CONTAINERS_QUESTIONS = [
    _q(
        "CI",
        "A team of 10 developers used to only merge code once a month, causing massive, painful "
        "merge conflicts. They switch to merging small changes into the main branch every day, "
        "with an automated build and test run on every merge. What practice is this?",
        ["Continuous Deployment", "Continuous Integration (CI)", "Blue-green deployment", "Infrastructure as Code"],
        1,
        "Continuous Integration is exactly this: merging code changes frequently (not "
        "monthly), each time triggering an automated build/test, so integration problems surface "
        "early and in small pieces instead of one giant conflict.",
    ),
    _q(
        "CD: delivery vs deployment",
        "Every change that passes the automated pipeline is automatically pushed straight to "
        "production, with no human clicking 'approve' at any point. What is this specific "
        "practice called?",
        ["Continuous Integration", "Continuous Delivery", "Continuous Deployment", "Manual deployment"],
        2,
        "Continuous Deployment goes all the way to production automatically. Continuous "
        "Delivery stops one step short — the build is always release-ready, but a human still "
        "approves the actual push to production.",
    ),
    _q(
        "Branching strategy",
        "Multiple developers keep breaking the shared main branch by pushing incomplete work "
        "directly to it. What practice would let them work independently and only merge once "
        "their own work is tested and ready?",
        ["Deleting version control", "Feature branches with pull requests", "Disabling automated tests", "Working only on Fridays"],
        1,
        "Feature branches let each developer work in isolation and only merge into main via a "
        "reviewed pull request once their change is complete and tested — directly preventing "
        "half-finished work from breaking the shared branch.",
    ),
    _q(
        "Containers vs VMs",
        "A team needs to run 20 lightweight, isolated application instances on a single physical "
        "server with minimal overhead and fast startup times, and doesn't need each instance to "
        "have its own full OS kernel. What technology fits best?",
        ["Full virtual machines, one per instance", "Containers (e.g. Docker)", "Bare metal servers", "A single monolithic process"],
        1,
        "Containers share the host OS kernel and package just the app plus its dependencies, "
        "giving much lower overhead and faster startup than full VMs (which each need their own "
        "guest OS) — ideal for many lightweight, isolated instances on one host.",
    ),
    _q(
        "Docker images",
        "A developer says 'it works on my machine' but the same code fails when deployed to the "
        "test server, due to a subtly different library version installed there. What practice "
        "would eliminate this class of problem?",
        ["Packaging the app and its exact dependencies into a container image", "Writing more comments in the code", "Increasing server RAM", "Disabling the firewall"],
        0,
        "A container image bundles the application together with its exact dependency versions, "
        "so the same image runs identically everywhere — directly eliminating 'works on my "
        "machine' environment-drift problems.",
    ),
    _q(
        "Kubernetes (concept)",
        "A company has 200 containers running across a fleet of servers, and manually starting, "
        "restarting, and load-balancing each one individually has become unmanageable. What kind "
        "of tool is designed to automate this at scale?",
        ["A container orchestrator (e.g. Kubernetes)", "A single Dockerfile", "A CDN", "A code editor"],
        0,
        "Container orchestrators automate deploying, scaling, restarting, and load-balancing "
        "large numbers of containers across a cluster of machines — exactly the 'unmanageable at "
        "200 containers by hand' problem described.",
    ),
    _q(
        "Infrastructure as Code",
        "A team used to click through a cloud console by hand to set up each new environment, "
        "leading to inconsistent, undocumented setups that were hard to reproduce. What practice "
        "solves this by describing infrastructure in version-controlled config files instead?",
        ["Infrastructure as Code (IaC)", "Continuous Integration", "Blue-green deployment", "A load balancer"],
        0,
        "IaC (e.g. Terraform-style tooling) defines infrastructure in version-controlled files "
        "that can be reviewed, repeated, and audited — directly replacing inconsistent, "
        "undocumented manual console clicking.",
    ),
    _q(
        "Blue-green deployment",
        "A company wants to release a new version of their app with zero downtime, and be able "
        "to instantly switch back to the old version if something goes wrong, by just redirecting "
        "traffic. What deployment strategy does this?",
        ["Blue-green deployment", "A single in-place upgrade", "Manual server restart", "Continuous Integration"],
        0,
        "Blue-green keeps two identical environments (old='blue', new='green') and switches "
        "traffic between them instantly — giving zero-downtime releases and an equally instant "
        "rollback by just switching traffic back.",
    ),
    _q(
        "Canary release",
        "Instead of releasing a new version to all users at once, a team first routes just 5% of "
        "traffic to it, watches for errors, and only then gradually increases that percentage. "
        "What is this release strategy called?",
        ["A canary release", "A big-bang release", "Continuous Integration", "Vertical scaling"],
        0,
        "A canary release gradually rolls a new version out to a small subset of real traffic "
        "first, so problems are caught while affecting only a few users, before a full rollout.",
    ),
    _q(
        "Rollback",
        "A new deployment causes a critical bug in production. The on-call engineer needs to "
        "restore service immediately by reverting to the last known-good version rather than "
        "trying to debug live. What is this action called?",
        ["A rollback", "A canary release", "A feature flag toggle", "Horizontal scaling"],
        0,
        "A rollback reverts to a previously working version to restore service quickly — the "
        "priority in an active incident is restoring service first, with root-cause debugging "
        "done afterward in a safe environment.",
    ),
    _q(
        "Monitoring / observability",
        "A service's response times have been slowly degrading over the past week, but nobody "
        "noticed until customers started complaining. What practice would have surfaced this "
        "proactively?",
        ["Monitoring and alerting on key metrics", "More frequent code comments", "A bigger Git repository", "Manual daily server reboots"],
        0,
        "Monitoring (tracking metrics like latency over time) with alerting on thresholds "
        "surfaces gradual degradation automatically, rather than waiting for customers to notice "
        "and complain first.",
    ),
    _q(
        "Centralized logging",
        "An issue spans five different microservices, and the team needs to trace a single "
        "request's path and errors across all five logs at once, instead of SSH-ing into each "
        "server individually. What practice solves this?",
        ["Centralized log aggregation", "Deleting old logs", "Disabling logging to save space", "Using more servers"],
        0,
        "Centralized logging aggregates logs from all services into one searchable place, "
        "letting you trace one request's journey across many services at once — without that, "
        "correlating five separate logs manually is painfully slow.",
    ),
    _q(
        "Health checks",
        "A load balancer keeps sending traffic to a server instance that has silently crashed "
        "internally (though its network port still technically accepts connections), causing "
        "errors for users routed there. What mechanism should the load balancer use to detect "
        "and avoid this?",
        ["Health checks / readiness probes", "A bigger instance size", "More bandwidth", "A longer subnet mask"],
        0,
        "Health checks actively probe an instance's actual application health (not just whether "
        "the port is open) and let the load balancer stop routing traffic to an instance that "
        "fails them.",
    ),
    _q(
        "Configuration management",
        "A company has 100 servers that have gradually drifted to slightly different "
        "configurations over time due to manual changes, causing 'works on some servers but not "
        "others' bugs. What kind of tool enforces a consistent, declared configuration across "
        "all of them?",
        ["A configuration management tool (e.g. Ansible-style)", "A single Dockerfile", "A CDN", "A load balancer"],
        0,
        "Configuration management tools declare the desired state of a server's configuration "
        "and enforce it across the whole fleet, correcting drift automatically rather than "
        "letting manual one-off changes accumulate inconsistently.",
    ),
    _q(
        "Microservices vs monolith",
        "A large monolithic application has become so tightly coupled that even a tiny change "
        "requires redeploying and retesting the entire system, slowing releases to a crawl. What "
        "architectural approach addresses this by splitting it into independently deployable "
        "services?",
        ["Microservices architecture", "A bigger monolith", "Vertical scaling only", "Disabling version control"],
        0,
        "Microservices split a system into smaller, independently deployable services, so a "
        "change to one doesn't require redeploying and retesting the whole application — "
        "directly trading monolithic coupling for independent release cycles.",
    ),
    _q(
        "API versioning",
        "A company needs to make breaking changes to its public API's response format, but many "
        "existing client apps still depend on the old format and can't be updated immediately. "
        "What practice lets both coexist safely during the transition?",
        ["API versioning (e.g. /v1/ and /v2/)", "Deleting the old API immediately", "Ignoring the breaking change", "Disabling the API entirely"],
        0,
        "Versioning the API (keeping /v1/ live alongside a new /v2/) lets old clients keep "
        "working unmodified while new clients adopt the updated version, avoiding a hard cutover "
        "that breaks everyone at once.",
    ),
    _q(
        "CI/CD secrets",
        "A build pipeline's logs are accidentally left publicly viewable, and someone notices "
        "that a database password was printed in plain text during one of the build steps. What "
        "practice would have prevented this exposure?",
        ["Masking/injecting secrets securely rather than printing them in logs", "Making the pipeline run faster", "Adding more build servers", "Disabling automated testing"],
        0,
        "CI/CD platforms support injecting secrets as protected environment variables that get "
        "automatically masked in logs — a secret should never appear in plaintext in build "
        "output, which is exactly the leak here.",
    ),
    _q(
        "Feature flags",
        "A team wants to ship a new feature's code to production now, but keep it turned off "
        "for all users until marketing is ready to launch it next month, without doing another "
        "deployment at launch time. What technique enables this?",
        ["A feature flag/toggle", "A rollback", "A canary release", "Vertical scaling"],
        0,
        "Feature flags let you deploy code with a feature dormant behind a toggle, then turn it "
        "on later for some or all users with a config change — no redeploy needed at actual "
        "launch time.",
    ),
    _q(
        "Artifact registries",
        "Your build pipeline produces a container image for every commit, and deployments need "
        "to pull a specific, exact version of that image — not just 'the latest build'. Where "
        "should those versioned images be stored and pulled from?",
        ["A container/artifact registry with tagged versions", "Each developer's laptop", "A shared email inbox", "The production database"],
        0,
        "An artifact/container registry stores built images with immutable version tags, so a "
        "deployment can pull exactly the version it was tested against — relying on 'latest' is "
        "precisely how you end up deploying something different from what you tested.",
    ),
    _q(
        "Postmortems",
        "After a major outage is resolved, the team holds a meeting to document what happened "
        "and why, focused on fixing the process rather than blaming the engineer who pushed the "
        "change. What DevOps practice is this?",
        ["A blameless postmortem", "A performance review", "A code freeze", "A rollback"],
        0,
        "A blameless postmortem examines the systemic and process causes of an incident (not "
        "individual blame), so the team improves the actual conditions that allowed the failure, "
        "and people feel safe reporting issues honestly in the future.",
    ),
]


# ==================================================================== #
# 6. Cloud Fundamentals & Service Models — Set 2
# ==================================================================== #
CLOUD_FUNDAMENTALS_QUESTIONS_2 = [
    _q(
        "Region selection",
        "Your main user base is in Southeast Asia, but your only deployment is in a US region, "
        "and users report slow page loads even though the app itself is lightweight. What's the "
        "most direct fix?",
        ["Add more CPU to the US servers", "Deploy into a region closer to Southeast Asia", "Enable auto-scaling", "Switch to block storage"],
        1,
        "Physical distance directly adds propagation delay. Deploying into (or adding) a region "
        "geographically closer to your users cuts that round-trip time — no amount of extra CPU "
        "in the wrong location fixes a distance problem.",
    ),
    _q(
        "Auto-scaling policy",
        "You want new server instances to launch automatically whenever average CPU usage across "
        "the fleet exceeds 70%, and to terminate extras once it drops back down. What should you "
        "configure?",
        ["A manual scaling schedule", "A target-tracking auto-scaling policy", "A static fleet size", "A CDN rule"],
        1,
        "A target-tracking scaling policy continuously watches a metric (like CPU%) and adds or "
        "removes instances to keep it near your target — exactly the reactive, threshold-based "
        "behavior described, unlike a fixed schedule which doesn't respond to real load.",
    ),
    _q(
        "Snapshots & backup",
        "Before applying a risky configuration change to a production database's underlying "
        "disk, you want a point-in-time copy you can restore from if something goes wrong. What "
        "should you take first?",
        ["A volume snapshot", "A new VPC", "A load balancer", "A CDN cache purge"],
        0,
        "A snapshot captures the exact state of a disk/volume at a point in time, giving you a "
        "restore point before a risky change — the standard safety net before any change that "
        "might corrupt or lose data.",
    ),
    _q(
        "Read replicas",
        "Your application's database is struggling because reporting queries (heavy SELECTs) "
        "are competing with normal transactional writes for the same database resources. What "
        "would offload the reporting load without touching the write path?",
        ["Add a read replica for reporting queries", "Increase the write timeout", "Enable a CDN", "Switch to object storage"],
        0,
        "A read replica is a synced copy of the database that serves read-only queries, letting "
        "you point reporting/analytics traffic at it while the primary handles writes "
        "undisturbed.",
    ),
    _q(
        "Message queues",
        "An order-processing service sometimes gets overwhelmed by bursts of incoming orders, "
        "causing it to crash or drop requests. You want incoming orders to be buffered and "
        "processed at a steady rate instead of hitting the service directly. What should sit "
        "between them?",
        ["A message queue", "A hypervisor", "A subnet mask", "A digital signature"],
        0,
        "A message queue decouples producers (incoming orders) from consumers (the processing "
        "service), buffering bursts so the consumer processes at its own sustainable rate "
        "instead of being hit with the full spike directly.",
    ),
    _q(
        "Edge computing",
        "A factory has hundreds of IoT sensors that need to react to abnormal readings within "
        "milliseconds, but sending every reading to a distant cloud region for processing adds "
        "too much delay. What approach processes the data closer to the sensors themselves?",
        ["Edge computing", "A larger cloud region", "A CDN for images", "Vertical scaling only"],
        0,
        "Edge computing pushes processing to devices/servers physically near the data source, "
        "cutting the round-trip to a distant cloud region — critical when a sub-second reaction "
        "time is required.",
    ),
    _q(
        "NoSQL vs relational",
        "You're storing chat messages for a messaging app: extremely high write volume, flexible "
        "and evolving message formats, and you rarely need complex multi-table joins across the "
        "data. Which type of database fits better than a traditional relational database?",
        ["A relational (SQL) database", "A NoSQL database", "A single flat text file", "No database at all"],
        1,
        "NoSQL databases favor high write throughput and flexible/schema-less data over strict "
        "relational structure and complex joins — a good fit when your access pattern doesn't "
        "need multi-table joins and your schema will keep evolving.",
    ),
    _q(
        "Spot instances",
        "A nightly batch job that processes video files can be safely paused and resumed later "
        "if interrupted, and cost is the top priority. What instance purchasing option is best "
        "suited to this workload?",
        ["Reserved instances", "Spot/preemptible instances", "On-demand instances only", "Dedicated hosts"],
        1,
        "Spot instances offer the steepest discount in exchange for the provider being able to "
        "reclaim them with little notice — a great fit for interruptible, resumable batch work, "
        "but wrong for anything that must run continuously without interruption.",
    ),
    _q(
        "Data egress cost",
        "Your monthly cloud bill has a surprisingly large line item for data leaving the cloud "
        "provider's network to the public internet, even though compute costs stayed flat. What "
        "is this charge commonly called?",
        ["Data egress cost", "Reserved instance cost", "A CDN subscription fee", "A vendor lock-in fee"],
        0,
        "Cloud providers typically charge for data egress (data leaving their network to the "
        "internet or another provider) while ingress (data coming in) is usually free — a "
        "commonly underestimated cost driver at scale.",
    ),
    _q(
        "Capacity modes",
        "A new database table will have wildly unpredictable traffic — sometimes near zero, "
        "sometimes a huge spike — and you don't want to manually provision or pay for fixed "
        "capacity you might not use. What capacity model fits?",
        ["Fixed/provisioned capacity only", "On-demand (pay-per-request) capacity", "A single dedicated server", "A CDN"],
        1,
        "On-demand capacity modes bill per actual request/usage rather than a pre-provisioned "
        "fixed amount, which suits wildly unpredictable traffic far better than committing to a "
        "fixed throughput level you'd either overpay for or run out of.",
    ),
    _q(
        "Multi-region active-active",
        "A global application runs full, independent copies of itself in both the US and Europe "
        "simultaneously, with users routed to whichever is closest, and either region can handle "
        "100% of traffic alone if the other fails. What architecture is this?",
        ["Single-region deployment", "Multi-region active-active", "A single Availability Zone", "Vertical scaling"],
        1,
        "Active-active multi-region means multiple regions are all live and serving traffic "
        "simultaneously (not one primary + a passive standby), giving both lower latency via "
        "proximity routing and resilience if any one region fails entirely.",
    ),
    _q(
        "Marketplace images",
        "Instead of installing and configuring a complex piece of software from scratch on a "
        "fresh VM, a team launches a pre-built, vendor-maintained image with it already "
        "installed and configured. What did they use?",
        ["A cloud marketplace image", "A security group", "A load balancer", "A VPN gateway"],
        0,
        "Cloud marketplaces offer pre-built, vendor-maintained images (often paid) for common "
        "software stacks, letting you launch a ready-configured instance instead of installing "
        "everything manually from a bare OS image.",
    ),
    _q(
        "Resource tagging",
        "Finance wants to know exactly how much of the monthly cloud bill each internal team is "
        "responsible for, across hundreds of shared resources. What practice, applied "
        "consistently when resources are created, makes this possible?",
        ["Resource tagging (e.g. team=marketing)", "Using only reserved instances", "Disabling logging", "Using a single shared account with no structure"],
        0,
        "Tagging resources with metadata like team, project, or cost-center lets billing tools "
        "aggregate spend by tag — without consistent tagging from the start, splitting a shared "
        "bill accurately after the fact is very difficult.",
    ),
    _q(
        "Self-healing infrastructure",
        "An instance in a fleet crashes unexpectedly at 3 AM. By the time an engineer checks "
        "their phone an hour later, a replacement instance has already been automatically "
        "launched and is serving traffic normally. What enabled this?",
        ["Manual intervention", "Auto-healing / self-healing infrastructure (health checks + auto-replace)", "A bigger hard drive", "A CDN"],
        1,
        "Self-healing setups combine health checks with automation that detects a failed "
        "instance and launches a replacement without human involvement — turning a 3 AM page "
        "into a non-event instead of an emergency.",
    ),
    _q(
        "TCO",
        "A company is deciding whether to keep running their own physical data center or migrate "
        "to the cloud, factoring in not just server cost but power, cooling, real estate, and "
        "staff to maintain it all. What are they calculating?",
        ["Total Cost of Ownership (TCO)", "Bandwidth-delay product", "Elasticity", "Shared responsibility"],
        0,
        "TCO looks beyond the sticker price of hardware to every associated cost — power, "
        "cooling, facilities, and staff — which is the fair way to compare on-prem against "
        "cloud's all-inclusive pricing.",
    ),
    _q(
        "Identity federation",
        "Employees already log into their laptops and internal tools using the company's "
        "on-premises Active Directory. The company wants them to use those SAME credentials to "
        "access cloud resources, without creating a second separate cloud-only account for "
        "everyone. What enables this?",
        ["Identity federation / SSO with the on-prem directory", "A CDN", "A load balancer", "Object storage"],
        0,
        "Identity federation connects an existing identity provider (like on-prem AD) to cloud "
        "services, so users authenticate once with their existing credentials rather than "
        "juggling a separate cloud-only identity.",
    ),
    _q(
        "SLA",
        "A cloud provider's contract guarantees 99.9% uptime per month. Roughly how much downtime "
        "does that still allow in a 30-day month?",
        ["About 43 minutes", "About 3 days", "Zero downtime, ever", "About 12 hours"],
        0,
        "99.9% ('three nines') allows about 0.1% downtime — roughly 43 minutes per 30-day month. "
        "Each additional 'nine' of SLA cuts allowed downtime by roughly 10x, which is why 99.99% "
        "vs 99.9% is a meaningfully bigger commitment.",
    ),
    _q(
        "Right-sizing",
        "A cost review finds that a fleet of large instances is consistently running at only "
        "8-10% CPU utilization, month after month. What optimization directly addresses this "
        "waste?",
        ["Right-sizing to smaller instances that match actual usage", "Adding a CDN", "Enabling encryption", "Switching to object storage"],
        0,
        "Right-sizing matches instance capacity to actual observed usage — consistently low "
        "utilization like 8-10% is a strong signal you're paying for far more capacity than the "
        "workload needs.",
    ),
    _q(
        "Cost governance",
        "After being surprised by an unexpectedly large monthly bill caused by a forgotten "
        "test environment left running, a team wants to be notified automatically the moment "
        "spending crosses a set threshold going forward. What should they set up?",
        ["A budget alert", "A security group", "A DNS record", "A VLAN"],
        0,
        "Budget alerts notify you automatically when spending crosses a defined threshold, "
        "catching runaway or forgotten resources early rather than discovering them a month "
        "later on the bill.",
    ),
    _q(
        "In-memory caching",
        "A product page's database query for 'top 10 bestsellers' is run thousands of times a "
        "minute, but the underlying data only actually changes once an hour. What would reduce "
        "database load without changing the data's freshness requirements?",
        ["An in-memory cache (e.g. Redis) in front of the query", "A bigger database instance only", "More database read replicas only", "Disabling the query entirely"],
        0,
        "An in-memory cache stores the result of an expensive, rarely-changing query so "
        "subsequent requests are served from fast memory instead of hitting the database again "
        "— ideal when data changes far less often than it's read.",
    ),
]

# ==================================================================== #
# 7. Cloud Security & Shared Responsibility — Set 2
# ==================================================================== #
CLOUD_SECURITY_QUESTIONS_2 = [
    _q(
        "Shared responsibility (PaaS)",
        "You deploy your application code to a PaaS platform. A vulnerability in the underlying "
        "runtime/container orchestration layer is found — whose job is it to patch that layer?",
        ["The customer's — PaaS still means you patch everything", "The provider's — they manage the platform/runtime layer", "Nobody's, PaaS has no shared responsibility", "It depends on the day of the week"],
        1,
        "PaaS sits between IaaS and SaaS: the provider manages the runtime, orchestration, and "
        "underlying platform, while the customer is responsible for their application code and "
        "data — patching the platform layer itself is the provider's job here.",
    ),
    _q(
        "Security groups vs NACLs",
        "You need a rule that evaluates traffic statelessly at the subnet boundary (return "
        "traffic must be explicitly allowed too), as an extra layer alongside your "
        "instance-level firewall rules. What are you configuring?",
        ["A Security Group", "A Network ACL", "A CDN rule", "A DNS record"],
        1,
        "Network ACLs are stateless and operate at the subnet level — unlike security groups "
        "(stateful, instance-level), a NACL requires explicit rules for both inbound AND the "
        "matching outbound return traffic.",
    ),
    _q(
        "Cloud WAF",
        "Your login page is being hit by an automated bot trying thousands of stolen "
        "username/password combinations per minute (credential stuffing). What cloud-native "
        "control is designed to detect and block this pattern at the edge?",
        ["A cloud WAF with bot/rate-based rules", "A bigger database", "A VPC peering connection", "A storage lifecycle policy"],
        0,
        "A cloud WAF can apply rate-based and bot-detection rules right at the edge, blocking "
        "credential-stuffing patterns before they ever reach your application servers.",
    ),
    _q(
        "Default encryption",
        "A cloud storage service now encrypts every new object automatically the moment it's "
        "uploaded, with no action required from the customer. What security principle does this "
        "reflect?",
        ["Secure by default", "Zero Trust", "Least privilege", "Defense in depth"],
        0,
        "'Secure by default' means the safe configuration is what you get automatically, rather "
        "than requiring the customer to remember to turn security on — a design philosophy "
        "cloud providers have increasingly adopted after years of misconfiguration-driven "
        "breaches.",
    ),
    _q(
        "Container image scanning",
        "Before a container image is allowed to be deployed, your pipeline automatically checks "
        "it against a database of known vulnerable packages and blocks the deployment if any "
        "critical ones are found. What practice is this?",
        ["Container image vulnerability scanning", "Load balancing", "DNS resolution", "Cost tagging"],
        0,
        "Scanning container images for known-vulnerable packages before deployment catches "
        "issues (like an outdated base image with a critical CVE) before they ever reach "
        "production, rather than discovering them after the fact.",
    ),
    _q(
        "Cloud pentesting rules",
        "A security firm wants to pentest a client's cloud environment, but discovers that "
        "certain shared, multi-tenant services are explicitly excluded from testing by the "
        "cloud provider's policy. Why would a provider restrict this?",
        ["To hide vulnerabilities", "Because testing shared multi-tenant infrastructure could affect other customers", "Because pentesting is illegal everywhere", "Providers never restrict pentesting"],
        1,
        "Cloud providers publish rules of engagement partly because some shared services "
        "underlie many customers at once — an aggressive test could degrade or disrupt other "
        "tenants who never consented to being part of the test.",
    ),
    _q(
        "Data classification",
        "Before deciding how strictly to encrypt, restrict, and monitor a given dataset, a "
        "company first labels it as Public, Internal, Confidential, or Restricted. What is this "
        "labeling process called, and why does it matter?",
        ["Data classification — it lets controls scale to the data's actual sensitivity", "Data residency — it decides which country stores the data", "Tokenization — it replaces the data with a fake value", "Encryption — it's the same thing as encrypting"],
        0,
        "Data classification tags data by sensitivity so that security controls (encryption "
        "strength, access restrictions, monitoring) can be applied proportionally, instead of "
        "either under-protecting sensitive data or over-engineering controls for trivial data.",
    ),
    _q(
        "Multi-account strategy",
        "A company puts its production, staging, and development workloads into three "
        "completely separate cloud accounts instead of one shared account, so a mistake or "
        "breach in dev can't touch production. What strategy is this?",
        ["A multi-account / landing zone strategy", "A single VPC", "A CDN", "A security group"],
        0,
        "A multi-account (landing zone) strategy uses account boundaries as a hard isolation "
        "layer between environments, so a compromised or misconfigured dev account structurally "
        "cannot reach production resources in a separate account.",
    ),
    _q(
        "Cross-account roles",
        "A contractor needs temporary access to a specific set of resources in your cloud "
        "account for a two-week project. Instead of creating a permanent user with a shared "
        "access key, what's the more secure way to grant this?",
        ["Share your own root credentials", "Have them assume a scoped, temporary cross-account role", "Email them a permanent API key", "Give them the same access as all employees"],
        1,
        "Cross-account role assumption grants temporary, scoped credentials for exactly the "
        "access needed, auditable and easy to revoke — far safer than a permanent shared key "
        "that lingers long after the two-week project ends.",
    ),
    _q(
        "Cloud DDoS protection",
        "A cloud provider offers a managed service that automatically absorbs and mitigates "
        "large-scale volumetric traffic floods aimed at your public-facing resources. What "
        "service category is this?",
        ["A cloud-native DDoS protection service", "A CDN cache", "A VPN gateway", "An IAM policy"],
        0,
        "Managed DDoS protection services (like AWS Shield or Azure DDoS Protection) sit in "
        "front of your public endpoints and absorb/mitigate volumetric attacks using the "
        "provider's much larger network capacity.",
    ),
    _q(
        "API key rotation",
        "An API key used by an integration has been active, unchanged, for three years. "
        "Security policy now requires all such keys to be replaced with fresh ones on a regular "
        "schedule. What practice is being enforced?",
        ["API key rotation", "Data classification", "Multi-account isolation", "Auto-scaling"],
        0,
        "Rotating keys on a regular schedule limits how long a leaked or forgotten key remains "
        "valid — a 3-year-old never-rotated key is a much larger window of exposure than one "
        "rotated every 90 days.",
    ),
    _q(
        "Over-privileged functions",
        "A serverless function that only needs to read from one specific storage bucket is "
        "instead given full read/write access to every bucket in the account, 'just in case.' "
        "What risk does this create if the function is ever compromised?",
        ["No risk — serverless functions can't be compromised", "A much larger blast radius than necessary", "Faster execution time", "Lower cost"],
        1,
        "If a function with unnecessarily broad permissions is compromised (via a code "
        "vulnerability or a poisoned dependency), the attacker inherits ALL of that "
        "over-provisioned access — least privilege exists specifically to shrink this blast "
        "radius.",
    ),
    _q(
        "Container escape",
        "A security researcher discovers a flaw that lets a process inside a container break out "
        "and access the underlying host machine's resources directly. What is this risk called?",
        ["A container escape", "A DDoS attack", "A phishing attack", "Data residency violation"],
        0,
        "Container escape means the isolation between a container and its host kernel has been "
        "broken, letting malicious code inside the container reach the host — a particularly "
        "severe risk since a host often runs many other containers too.",
    ),
    _q(
        "Compliance attestation",
        "Before signing a contract with a new cloud vendor, your company's security team asks "
        "for independent proof that the vendor's controls meet a recognized security standard, "
        "rather than just taking the vendor's word for it. What might they request?",
        ["A SOC 2 report (or similar compliance attestation)", "A discount code", "A CDN subscription", "A load balancer"],
        0,
        "A SOC 2 (or ISO 27001, etc.) attestation is an independent auditor's verification that "
        "a vendor's controls actually meet a recognized standard — giving assurance beyond just "
        "trusting the vendor's own marketing claims.",
    ),
    _q(
        "Key rotation",
        "An encryption key that protects a large volume of sensitive data has been in use "
        "unchanged for five years. What practice reduces the risk of that single key ever being "
        "fully compromised?",
        ["Key rotation on a defined schedule", "Never touching the key again", "Sharing the key with more people", "Disabling encryption"],
        0,
        "Rotating encryption keys periodically limits how much data any single compromised key "
        "exposure would affect, and is a standard requirement in most compliance frameworks for "
        "long-lived encrypted data.",
    ),
    _q(
        "Object versioning",
        "An employee accidentally overwrites a critical configuration file in cloud storage with "
        "the wrong version, and there's no way to get the original back. What feature, if "
        "enabled beforehand, would have let you restore the previous version?",
        ["Object/bucket versioning", "A security group", "A VPN", "A load balancer"],
        0,
        "Versioning keeps every previous version of an object when it's overwritten or deleted, "
        "so an accidental (or malicious) overwrite can simply be rolled back — without it "
        "enabled in advance, the old version is gone.",
    ),
    _q(
        "CIS benchmarks",
        "A tool checks your cloud account's configuration against an industry-standard checklist "
        "of security best practices (like 'root account should have MFA enabled') and scores "
        "your compliance. What kind of standard is it likely checking against?",
        ["A CIS Benchmark", "A DNS zone file", "A VPC peering table", "A load balancer config"],
        0,
        "CIS Benchmarks are widely-adopted, vendor-specific checklists of security best "
        "practices; many CSPM tools score your environment specifically against these published "
        "standards.",
    ),
    _q(
        "SSO single point of failure",
        "A company federates login for dozens of cloud applications through a single identity "
        "provider (SSO). One morning, that identity provider suffers an outage. What is the "
        "consequence of centralizing authentication this way?",
        ["No impact — each app still works independently", "Every federated application becomes inaccessible at once", "Only the identity provider's own website goes down", "Security actually improves during the outage"],
        1,
        "Centralizing authentication through SSO is a security and convenience win, but it also "
        "concentrates risk — if the identity provider itself goes down, every application "
        "relying on it for login becomes unreachable simultaneously.",
    ),
    _q(
        "Log tampering",
        "During a forensic investigation, the security team discovers that an attacker deleted "
        "the cloud audit logs covering the time window of the breach, making it hard to "
        "reconstruct what happened. What control, configured in advance, would have prevented "
        "this?",
        ["Immutable / write-once log storage that even admins can't delete", "A faster CDN", "A bigger load balancer", "More storage tiers"],
        0,
        "Write-once, immutable log storage (or shipping logs to a separate, restricted account) "
        "prevents even a compromised admin account from deleting the evidence — a key control "
        "for making sure logs actually survive to be useful during an investigation.",
    ),
    _q(
        "Insecure defaults",
        "A team spins up a new type of cloud resource for the first time, unaware that this "
        "particular service defaults to allowing public internet access unless explicitly "
        "locked down. What category of risk does this represent?",
        ["An insecure default configuration", "A DDoS attack", "A digital signature failure", "A network segmentation success"],
        0,
        "Not every cloud service defaults to 'secure' — some newer or less common services "
        "still ship with permissive defaults, which is why teams should verify a new service's "
        "default posture rather than assuming it's automatically locked down.",
    ),
]

# ==================================================================== #
# 8. Network Security — Attacks & Defenses — Set 2
# ==================================================================== #
NETWORK_SECURITY_QUESTIONS_2 = [
    _q(
        "Smishing",
        "An employee receives a text message claiming to be from a parcel delivery service, "
        "with a link to 'reschedule delivery' that actually leads to a credential-harvesting "
        "site. What is this attack called?",
        ["Vishing", "Smishing", "Whaling", "Baiting"],
        1,
        "Smishing is phishing delivered via SMS text message rather than email — the delivery "
        "channel is what distinguishes it from ordinary phishing or voice-based vishing.",
    ),
    _q(
        "Vishing",
        "An attacker calls an employee directly, impersonating the company's IT support team "
        "over the phone, and talks them into reading out a one-time verification code. What "
        "attack is this?",
        ["Vishing (voice phishing)", "Smishing", "A DDoS attack", "SQL injection"],
        0,
        "Vishing is phishing conducted over a phone call — the live, real-time conversation "
        "often makes it more persuasive than an email, since the attacker can adapt and react "
        "in the moment.",
    ),
    _q(
        "Whaling",
        "Instead of targeting random employees, an attacker crafts a highly personalized, "
        "carefully researched phishing email aimed specifically at the company's CFO. What is "
        "this more targeted form of phishing called?",
        ["Whaling", "Smishing", "Tailgating", "A brute-force attack"],
        0,
        "Whaling targets high-value individuals (executives, 'the big fish') with highly "
        "customized attacks, in contrast to broad, generic phishing blasts sent to thousands of "
        "random recipients.",
    ),
    _q(
        "Business Email Compromise",
        "An accounts payable clerk receives an email that appears to be from the CEO, urgently "
        "instructing an unusual wire transfer to a new vendor account, with none of the normal "
        "approval steps. What type of fraud is this?",
        ["Business Email Compromise (BEC)", "A DDoS attack", "A supply chain attack", "Session hijacking"],
        0,
        "BEC uses a spoofed or compromised executive email account (or a lookalike domain) to "
        "pressure staff into fraudulent wire transfers — the urgency and bypassed approval "
        "process are the classic warning signs.",
    ),
    _q(
        "DNS spoofing",
        "A user types the correct URL for their bank, but their computer's DNS resolver has been "
        "tampered with to return the IP address of an attacker-controlled server instead of the "
        "real bank. What attack is this?",
        ["DNS spoofing / cache poisoning", "ARP spoofing", "Session hijacking", "A buffer overflow"],
        0,
        "DNS spoofing corrupts the name-to-IP mapping so a correctly-typed domain resolves to a "
        "malicious server — the user did everything right, but the underlying resolution "
        "process was compromised.",
    ),
    _q(
        "ARP spoofing",
        "An attacker on the same local network sends forged messages associating their own MAC "
        "address with the IP address of the default gateway, causing other devices' traffic to "
        "route through the attacker's machine. What attack is this?",
        ["ARP spoofing", "DNS spoofing", "A DDoS attack", "SQL injection"],
        0,
        "ARP spoofing forges the IP-to-MAC mapping on a local segment, letting an attacker "
        "position themselves as a man-in-the-middle for local traffic — a LAN-specific technique, "
        "unlike DNS spoofing which corrupts name resolution instead.",
    ),
    _q(
        "Session hijacking",
        "An attacker who intercepted a user's session cookie over an unencrypted connection uses "
        "that cookie to impersonate the logged-in user, without ever needing their password. "
        "What attack is this?",
        ["Session hijacking", "A brute-force attack", "A zero-day exploit", "A supply chain attack"],
        0,
        "Session hijacking steals an already-authenticated session token/cookie to impersonate "
        "the user directly — the password itself is never needed, which is why protecting "
        "session tokens (HTTPS, secure cookie flags) matters as much as protecting passwords.",
    ),
    _q(
        "Command injection",
        "A web form lets users check if a hostname is reachable, and passes the input directly "
        "into a system shell command. An attacker enters a hostname followed by `; rm -rf /` to "
        "run their own command afterward. What vulnerability is this?",
        ["Command injection", "Cross-Site Scripting (XSS)", "DNS spoofing", "A DDoS attack"],
        0,
        "Command injection happens when untrusted input is passed unsanitized into a system "
        "shell call, letting an attacker append their own OS commands — the fix is avoiding "
        "shell calls with user input entirely, or strictly validating/escaping it.",
    ),
    _q(
        "Directory traversal",
        "A file-download feature takes a filename from the URL and an attacker changes it to "
        "`../../../../etc/passwd` to try to read a file outside the intended folder. What "
        "vulnerability is being exploited?",
        ["Directory traversal", "SQL injection", "A DDoS attack", "ARP spoofing"],
        0,
        "Directory traversal exploits insufficient path validation to escape the intended "
        "directory using '../' sequences and reach arbitrary files elsewhere on the "
        "filesystem — the fix is validating and normalizing paths server-side.",
    ),
    _q(
        "Buffer overflow",
        "A program allocates a fixed-size memory buffer for user input but never checks the "
        "input's actual length, letting an attacker's oversized input overwrite adjacent memory "
        "and potentially execute injected code. What is this classic vulnerability called?",
        ["A buffer overflow", "A DDoS attack", "Session hijacking", "DNS spoofing"],
        0,
        "A buffer overflow occurs when data written exceeds the allocated buffer's bounds, "
        "corrupting adjacent memory — a foundational class of memory-safety vulnerability behind "
        "many historic exploits, mitigated by bounds checking and memory-safe languages.",
    ),
    _q(
        "Zero-day",
        "A vulnerability is actively being exploited in the wild, but the software vendor has no "
        "patch or fix available yet because they only just learned about it. What is this "
        "situation called?",
        ["A zero-day vulnerability/exploit", "A patch management failure", "A misconfiguration", "An insider threat"],
        0,
        "A zero-day means the vendor has had zero days to produce a fix — distinct from a patch "
        "management failure, where a fix already exists but simply wasn't applied yet.",
    ),
    _q(
        "Botnets",
        "Thousands of compromised home routers and IoT devices, unbeknownst to their owners, are "
        "being remotely controlled by an attacker to simultaneously flood a target with traffic. "
        "What is this network of compromised devices called?",
        ["A botnet", "A VPN", "A CDN", "A honeypot"],
        0,
        "A botnet is a network of compromised, remotely-controlled devices, commonly used to "
        "launch large-scale DDoS attacks or distributed spam/credential-stuffing campaigns at a "
        "scale a single machine couldn't achieve.",
    ),
    _q(
        "Keyloggers",
        "Malware silently installed on a user's laptop records every keystroke they type, "
        "including passwords, and periodically sends the captured data to an attacker. What "
        "type of malware is this?",
        ["A keylogger", "Ransomware", "A worm", "A DDoS tool"],
        0,
        "A keylogger captures keystrokes to steal credentials and other typed sensitive "
        "information — unlike ransomware (which encrypts and demands payment), it's designed to "
        "stay hidden and keep collecting data over time.",
    ),
    _q(
        "Rootkits",
        "Security software fails to detect an infection because the malware has modified the "
        "operating system itself to hide its own files, processes, and network connections from "
        "normal detection tools. What type of malware achieves this deep concealment?",
        ["A rootkit", "A worm", "Ransomware", "Spyware (only)"],
        0,
        "A rootkit operates at a deep system level (sometimes kernel-level) specifically to hide "
        "its own presence from the OS and security tools, which is why rootkit infections often "
        "require booting from external, trusted media to properly detect and remove.",
    ),
    _q(
        "Supply chain attacks",
        "Instead of attacking a company directly, an attacker compromises a widely-used "
        "third-party software library, so that every application which later updates to the "
        "poisoned version unknowingly includes the attacker's malicious code. What is this "
        "attack pattern called?",
        ["A supply chain attack", "A DDoS attack", "Session hijacking", "Tailgating"],
        0,
        "Supply chain attacks compromise something upstream that many victims trust and pull in "
        "automatically (a library, a build tool, a vendor update), letting one compromise "
        "cascade into every downstream consumer — notoriously hard to detect since the code "
        "arrives through a normally-trusted channel.",
    ),
    _q(
        "Watering hole attacks",
        "Attackers identify a niche industry forum that employees of their target organization "
        "frequently visit, and compromise that forum to serve malware only to visitors from the "
        "target's IP range. What is this attack called?",
        ["A watering hole attack", "A whaling attack", "A brute-force attack", "ARP spoofing"],
        0,
        "A watering hole attack compromises a site the target audience is known to frequent "
        "(like predators waiting at a watering hole), rather than attacking the target directly "
        "— useful when the target itself is too well-defended to hit head-on.",
    ),
    _q(
        "Baiting",
        "An attacker leaves several USB drives labeled 'Confidential Salary Data' scattered in a "
        "company's parking lot, hoping a curious employee will plug one into a work computer. "
        "What social engineering technique is this?",
        ["Baiting", "Pretexting", "Vishing", "Tailgating"],
        0,
        "Baiting dangles something enticing (a labeled USB drive, a free download) to lure the "
        "victim into taking the compromising action themselves — the curiosity/greed hook is "
        "what distinguishes it from pretexting's fabricated-identity approach.",
    ),
    _q(
        "Shoulder surfing",
        "In a crowded coffee shop, someone at the next table quietly watches over your shoulder "
        "as you type your laptop password, then memorizes it. What is this low-tech but "
        "effective technique called?",
        ["Shoulder surfing", "Tailgating", "Baiting", "Phishing"],
        0,
        "Shoulder surfing is simply directly observing someone entering sensitive information "
        "— defended against with privacy screens and basic situational awareness in public "
        "spaces, no technical control involved.",
    ),
    _q(
        "Clean desk / dumpster diving",
        "An attacker rummages through a company's outdoor trash bins after hours and finds "
        "printed documents with employee names, internal project codenames, and a sticky note "
        "with a password on it. What organizational policy would have prevented this exposure?",
        ["A clean desk policy and secure document shredding", "A firewall", "A VPN", "Multi-factor authentication"],
        0,
        "A clean desk policy (nothing sensitive left out) combined with shredding/secure "
        "disposal of printed sensitive material closes off this entirely physical, low-tech "
        "attack vector — no firewall or VPN protects paper in a trash bin.",
    ),
    _q(
        "Honeypots",
        "A security team deliberately sets up a fake, intentionally vulnerable-looking server "
        "isolated from real production systems, specifically to attract attackers and study "
        "their techniques. What is this decoy system called?",
        ["A honeypot", "A firewall", "A VPN", "A load balancer"],
        0,
        "A honeypot is a deliberately exposed decoy designed to lure attackers away from real "
        "assets and let defenders observe their tools and techniques safely, since any "
        "interaction with it is inherently suspicious — no legitimate user has a reason to touch "
        "it.",
    ),
]

# ==================================================================== #
# 9. Networking Fundamentals — OSI, Protocols & Ports — Set 2
# ==================================================================== #
NETWORKING_FUNDAMENTALS_QUESTIONS_2 = [
    _q(
        "OSI layer 4 (transport)",
        "An application needs to make sure a large file arrives completely and in the correct "
        "order, splitting it into numbered segments and reassembling them at the destination. "
        "Which OSI layer is responsible for this segmentation and reassembly?",
        ["Network layer", "Transport layer", "Data Link layer", "Physical layer"],
        1,
        "The Transport layer (layer 4) handles segmentation, sequencing, and (with TCP) "
        "reliable, ordered delivery — the Network layer below it only handles addressing and "
        "routing of individual packets, not the ordering guarantee.",
    ),
    _q(
        "OSI layer 7 (application)",
        "A web browser constructs an HTTP GET request to fetch a webpage. Which OSI layer does "
        "HTTP itself operate at?",
        ["Application layer", "Presentation layer", "Session layer", "Transport layer"],
        0,
        "HTTP is an Application layer (layer 7) protocol — it's the layer that directly serves "
        "the end-user's request, sitting on top of the lower layers that handle the actual "
        "delivery mechanics.",
    ),
    _q(
        "SFTP vs FTP",
        "A company needs to transfer sensitive financial files to a partner's server regularly, "
        "and management insists the transfer must be encrypted in transit. Which protocol should "
        "they use instead of a plain option?",
        ["FTP", "SFTP", "Telnet", "SMTP"],
        1,
        "SFTP (SSH File Transfer Protocol) encrypts the entire session, including credentials "
        "and file contents, over SSH. Plain FTP transmits everything, including the login, in "
        "cleartext.",
    ),
    _q(
        "POP3 vs IMAP",
        "A user checks their email from both their phone and their laptop, and expects read "
        "status and folder organization to stay in sync across both devices. Which mail "
        "retrieval protocol supports this, unlike its older alternative which just downloads and "
        "deletes from the server?",
        ["POP3", "IMAP", "SMTP", "FTP"],
        1,
        "IMAP keeps mail on the server and synchronizes state (read/unread, folders, flags) "
        "across every device that connects. POP3 traditionally downloads messages to one device "
        "and removes them from the server, which breaks multi-device sync.",
    ),
    _q(
        "Default gateway",
        "A laptop on a local network needs to send a request to a server on the internet, "
        "outside its own local subnet. What does the laptop send that traffic to first?",
        ["Its default gateway", "Its own MAC address", "A DNS server directly, always", "The destination server directly, always"],
        0,
        "The default gateway (usually a router) is the exit point for any traffic destined "
        "outside the local subnet — a device only talks directly to hosts on its own subnet; "
        "everything else routes through the gateway first.",
    ),
    _q(
        "MAC vs IP purpose",
        "A network engineer needs to explain why a device has both a MAC address and an IP "
        "address rather than just one. What's the key distinction?",
        ["They're identical, just different formats", "MAC identifies the device on the local segment (layer 2); IP identifies it globally for routing (layer 3)", "MAC is used for encryption; IP is used for authentication", "IP never changes; MAC changes every session"],
        1,
        "MAC addresses are physical, layer-2 identifiers meaningful only on the local segment, "
        "while IP addresses are logical, layer-3 identifiers used to route traffic across "
        "different networks — a device typically needs both to communicate locally and "
        "globally.",
    ),
    _q(
        "Wired vs wireless",
        "A hospital's operating room requires an absolutely rock-solid, interference-free "
        "network connection for critical real-time monitoring equipment, where even brief signal "
        "drops are unacceptable. Which connection type should be used?",
        ["WiFi", "A wired Ethernet connection", "Bluetooth", "Cellular/mobile data"],
        1,
        "Wired Ethernet is immune to the interference, signal degradation, and contention issues "
        "that wireless is subject to, making it the safer choice when absolute reliability is "
        "non-negotiable, as in critical medical equipment.",
    ),
    _q(
        "Network topologies",
        "In a star topology, every device connects to one central switch. If that central switch "
        "fails, what happens to the whole network?",
        ["Nothing — a star topology has no single point of failure", "The entire network goes down, since every device depended on that one switch", "Only two devices lose connectivity", "The network automatically reroutes through the internet"],
        1,
        "A star topology's central device is a single point of failure — every connection "
        "depends on it, so its failure takes down the whole network, unlike a mesh topology "
        "where multiple paths exist between devices.",
    ),
    _q(
        "Fiber vs copper",
        "A company needs to run a network cable between two buildings 2 km apart, requiring high "
        "bandwidth and immunity to electromagnetic interference from nearby power lines. Which "
        "cable type is appropriate?",
        ["Copper (UTP)", "Fiber optic", "Coaxial", "No cable can span that distance"],
        1,
        "Fiber optic carries signals as light rather than electricity, giving it immunity to "
        "electromagnetic interference and much longer effective range at high bandwidth than "
        "copper, which degrades significantly over both distance and interference.",
    ),
    _q(
        "Static vs dynamic IP",
        "A company's public-facing mail server needs an IP address that never changes, since "
        "external systems and DNS records depend on reaching it at a consistent, known address. "
        "What should be configured instead of relying on DHCP?",
        ["A static IP address", "A dynamic IP address via DHCP", "No IP address at all", "A random IP each reboot"],
        0,
        "A static IP is manually assigned and never changes, which matters for servers that "
        "external parties (like DNS records) need to reliably find at the same address — DHCP's "
        "dynamic reassignment would break that dependency.",
    ),
    _q(
        "Port forwarding",
        "A home user wants to run a game server on their PC and let friends outside their home "
        "network connect to it, but the PC only has a private IP address behind their router. "
        "What should be configured on the router?",
        ["Port forwarding", "A VLAN", "A default gateway change", "DNS caching"],
        0,
        "Port forwarding configures the router to forward incoming traffic on a specific port to "
        "a specific internal device, letting external users reach a service on a private-IP "
        "device behind NAT.",
    ),
    _q(
        "Round-trip time",
        "A network monitoring tool reports that the time between sending a request and "
        "receiving its response has climbed from 20ms to 300ms over the past hour, even though "
        "no packets are being dropped. What metric is being measured here?",
        ["Round-Trip Time (RTT)", "Packet loss rate", "Bandwidth", "MAC address table size"],
        0,
        "RTT measures the total time for a signal to travel to a destination and the response "
        "to come back — rising RTT with no packet loss points to growing congestion or distance "
        "delay, not data being dropped.",
    ),
    _q(
        "QoS",
        "An office network carries both VoIP phone calls and large file downloads "
        "simultaneously, and calls start breaking up whenever a big download is running. What "
        "networking feature lets you prioritize voice traffic over bulk downloads?",
        ["Quality of Service (QoS)", "NAT", "A VLAN", "DHCP"],
        0,
        "QoS lets you classify and prioritize traffic types, ensuring latency-sensitive traffic "
        "like VoIP gets priority over less time-sensitive bulk downloads competing for the same "
        "bandwidth.",
    ),
    _q(
        "Jitter",
        "During a video call, audio isn't necessarily delayed overall, but packets are arriving "
        "at wildly inconsistent intervals, causing choppy, uneven playback. What specific network "
        "characteristic is causing this, distinct from plain latency?",
        ["Jitter (variation in packet delay)", "Bandwidth", "A duplex mismatch", "DNS caching"],
        0,
        "Jitter is the VARIATION in delay between packets, not the delay itself — even with "
        "reasonable average latency, high jitter causes uneven arrival timing that a real-time "
        "call's playback buffer struggles to smooth out.",
    ),
    _q(
        "Forward proxy caching",
        "A corporate network deploys a proxy server that caches frequently-requested external "
        "web content, so the next employee requesting the same page gets it from the local cache "
        "instead of re-fetching it from the internet. What is this local caching layer often "
        "called?",
        ["A forward proxy cache", "A CDN edge node run by the content owner", "A VPN concentrator", "A load balancer"],
        0,
        "A forward proxy sits between internal users and the internet and can cache frequently "
        "requested content locally — conceptually similar to a CDN's caching, but deployed by "
        "the CONSUMING organization for its own outbound traffic, not by the content owner.",
    ),
    _q(
        "Load balancing algorithms",
        "A load balancer needs to send new connections to whichever backend server currently has "
        "the fewest active connections, rather than blindly cycling through servers in order. "
        "What algorithm is this?",
        ["Round robin", "Least connections", "Random selection", "First available only"],
        1,
        "Least connections actively tracks each backend's current load and routes new "
        "connections to the least-busy one — round robin, by contrast, cycles through servers "
        "in a fixed order regardless of how busy each currently is.",
    ),
    _q(
        "Transmission types",
        "A router needs to send a single video stream to exactly the group of devices that have "
        "subscribed to it, without sending it to every device on the network and without sending "
        "a separate copy to each subscriber individually. What transmission type does this?",
        ["Unicast", "Broadcast", "Multicast", "Anycast only"],
        2,
        "Multicast sends one stream to a defined group of subscribers efficiently — unicast "
        "would need a separate copy per recipient, and broadcast would blast it to every device "
        "on the network whether they wanted it or not.",
    ),
    _q(
        "NTP",
        "A distributed system's servers need their internal clocks to be tightly synchronized, "
        "since even small time differences cause certificate validation and log correlation "
        "problems. What protocol keeps devices' clocks in sync?",
        ["NTP (Network Time Protocol)", "DHCP", "ARP", "ICMP"],
        0,
        "NTP synchronizes device clocks against reference time sources — critical for anything "
        "relying on consistent, accurate timestamps across systems, like TLS certificate "
        "validation, Kerberos authentication, and correlating logs from multiple servers.",
    ),
    _q(
        "MTU and fragmentation",
        "A packet larger than a network link's maximum allowed frame size needs to be split into "
        "smaller pieces before it can be transmitted across that link. What is this splitting "
        "process, and what does it split against?",
        ["Fragmentation, against the link's MTU (Maximum Transmission Unit)", "Encryption, against the link's bandwidth", "Routing, against the subnet mask", "NAT, against the port range"],
        0,
        "The MTU defines the largest frame a link can carry; a packet exceeding it must be "
        "fragmented into smaller pieces (and reassembled at the destination) — a common source "
        "of subtle performance issues when MTU sizes mismatch across a path.",
    ),
    _q(
        "Traceroute",
        "A user reports slow access to a website, and the engineer wants to see every router hop "
        "the traffic passes through on the way there, to identify exactly where the delay is "
        "introduced. What tool shows this hop-by-hop path?",
        ["Ping", "Traceroute", "DNS lookup", "ARP"],
        1,
        "Traceroute reveals the sequence of routers (hops) a packet passes through and the delay "
        "at each one, pinpointing where along the path a slowdown occurs — ping only tells you "
        "overall reachability and round-trip time, not the path.",
    ),
]

# ==================================================================== #
# 10. DevOps & Containers — Set 2
# ==================================================================== #
DEVOPS_CONTAINERS_QUESTIONS_2 = [
    _q(
        "Dockerfile layer caching",
        "A team notices their container builds take 10 minutes every time, even for a one-line "
        "code change, because dependency installation reruns from scratch on every build. "
        "Reordering the Dockerfile so dependencies are installed in an earlier, rarely-changing "
        "layer would fix this by taking advantage of what?",
        ["Docker layer caching", "A bigger CI server", "Blue-green deployment", "A feature flag"],
        0,
        "Docker builds each instruction as a cached layer; if an earlier layer (like dependency "
        "installation) hasn't changed, Docker reuses its cache instead of rerunning it — "
        "ordering rarely-changing steps before frequently-changing ones (like copying source "
        "code) maximizes cache hits and build speed.",
    ),
    _q(
        "Auto-restart on crash",
        "A container orchestrator notices that a container's process has crashed and "
        "automatically starts a new instance of it within seconds, without any human "
        "intervention. What capability is this?",
        ["Auto-restart / self-healing at the orchestrator level", "Blue-green deployment", "A canary release", "API versioning"],
        0,
        "Orchestrators like Kubernetes continuously watch container health and automatically "
        "restart failed containers — a baseline resilience feature distinct from the "
        "higher-level 'scale many containers' orchestration concept.",
    ),
    _q(
        "Horizontal Pod Autoscaling",
        "A containerized service automatically increases the NUMBER of running instances "
        "(pods) when CPU usage crosses a threshold, and decreases it again once load drops. "
        "What is this Kubernetes capability called?",
        ["Horizontal Pod Autoscaling (HPA)", "A Dockerfile", "A sidecar container", "Trunk-based development"],
        0,
        "HPA automatically adjusts the number of running pod replicas based on observed metrics "
        "like CPU or custom application metrics — it scales OUT (more pods), as opposed to "
        "vertical scaling which would mean making one pod bigger.",
    ),
    _q(
        "Service mesh",
        "As a company's number of microservices grows into the dozens, they need consistent "
        "traffic encryption, retries, and observability for service-to-service calls, without "
        "modifying every individual service's code to add this logic. What infrastructure layer "
        "addresses this?",
        ["A service mesh", "A single Dockerfile", "A load balancer only", "A feature flag system"],
        0,
        "A service mesh (like Istio or Linkerd) adds a dedicated infrastructure layer — usually "
        "via sidecar proxies — that handles cross-cutting concerns like mTLS, retries, and "
        "traffic observability uniformly, without each service reimplementing that logic.",
    ),
    _q(
        "Twelve-factor apps",
        "A development guideline states that an application's configuration (database URLs, API "
        "keys) should come from environment variables, never be hardcoded into the source code. "
        "What well-known set of principles includes this as a core rule?",
        ["The Twelve-Factor App methodology", "Trunk-based development", "GitOps", "Chaos engineering"],
        0,
        "The Twelve-Factor App methodology (config as environment variables is factor #3) "
        "describes best practices for building portable, scalable cloud-native applications — "
        "hardcoded config breaks the same build from running identically across environments.",
    ),
    _q(
        "Shift-left testing",
        "Instead of only running security and quality checks right before a release, a team "
        "moves those same checks to run automatically on every single commit, much earlier in "
        "the development process. What practice is this?",
        ["Shift-left testing", "Blue-green deployment", "A canary release", "Trunk-based development"],
        0,
        "Shift-left means moving testing/security checks earlier ('to the left' on a typical "
        "left-to-right pipeline timeline) so problems are caught during development, when "
        "they're cheapest to fix, rather than right before release.",
    ),
    _q(
        "Test pyramid",
        "A team has thousands of slow, brittle end-to-end UI tests but very few fast unit tests, "
        "making their test suite take hours and fail unpredictably. What testing principle "
        "explains why this balance is inverted from what's recommended?",
        ["The test pyramid (many fast unit tests, fewer slow E2E tests)", "Chaos engineering", "GitOps", "Feature flags"],
        0,
        "The test pyramid recommends a large base of fast, cheap unit tests, a smaller layer of "
        "integration tests, and few slow, expensive end-to-end tests at the top — this team's "
        "suite is inverted, which is exactly why it's slow and brittle.",
    ),
    _q(
        "Chaos engineering",
        "A team deliberately and randomly terminates production servers during business hours "
        "(in a controlled way) specifically to verify their system actually survives failures "
        "as designed, rather than assuming it does. What practice is this?",
        ["Chaos engineering", "A rollback", "A postmortem", "Trunk-based development"],
        0,
        "Chaos engineering intentionally injects failure into a system to verify its resilience "
        "assumptions hold up in practice — proactively finding weaknesses before a real, "
        "unplanned outage does.",
    ),
    _q(
        "GitOps",
        "A team manages all their infrastructure and deployment configuration as files in a Git "
        "repository, and an automated agent continuously ensures the live environment matches "
        "exactly what's declared in that repo — any manual change to the live environment gets "
        "automatically reverted. What practice is this?",
        ["GitOps", "Trunk-based development", "A blue-green deployment", "A canary release"],
        0,
        "GitOps uses Git as the single source of truth for desired infrastructure/application "
        "state, with automation continuously reconciling reality to match it — manual "
        "'kubectl edit'-style changes get overwritten because Git, not the live cluster, is "
        "authoritative.",
    ),
    _q(
        "Environment parity",
        "A bug only reproduces in production and never in staging, and investigation reveals "
        "staging runs a different OS version and different library versions than production. "
        "What principle, if followed, would have prevented this gap?",
        ["Environment parity (keeping dev/staging/prod as similar as possible)", "Chaos engineering", "A rollback strategy", "Feature flags"],
        0,
        "Environment parity means keeping environments as similar as practically possible "
        "(same OS, same dependency versions), specifically so that 'works in staging' reliably "
        "predicts 'works in production' — divergence between them is a common source of "
        "hard-to-reproduce bugs.",
    ),
    _q(
        "DORA metrics",
        "A company wants an objective, industry-benchmarked way to measure how good their "
        "software delivery process actually is — tracking things like deployment frequency and "
        "change failure rate. What well-known framework provides these metrics?",
        ["DORA metrics", "The OSI model", "The CAP theorem", "RBAC"],
        0,
        "DORA (DevOps Research and Assessment) metrics — deployment frequency, lead time for "
        "changes, change failure rate, and time to restore service — are widely used, "
        "research-backed benchmarks for software delivery performance.",
    ),
    _q(
        "MTTR",
        "After an incident, a team measures how long it took from the moment the system broke to "
        "the moment it was fully restored to normal operation. What reliability metric are they "
        "calculating?",
        ["Mean Time To Recovery (MTTR)", "Mean Time Between Failures (MTBF, a different metric)", "Deployment frequency", "Code coverage"],
        0,
        "MTTR measures how quickly a team detects and recovers from failures — a low MTTR "
        "matters as much as preventing failures altogether, since some incidents are inevitable "
        "no matter how careful you are.",
    ),
    _q(
        "Alert fatigue",
        "An on-call engineer receives so many low-priority, non-actionable alerts every night "
        "that they've started ignoring notifications altogether, including the rare genuinely "
        "critical one. What problem is this?",
        ["Alert fatigue", "A zero-day exploit", "A supply chain attack", "Environment drift"],
        0,
        "Alert fatigue happens when excessive low-value alerts desensitize responders, causing "
        "them to miss or delay reacting to the genuinely critical ones — the fix is tuning "
        "alert thresholds and only paging on truly actionable conditions.",
    ),
    _q(
        "Dependency scanning",
        "A pipeline automatically checks every third-party library your application depends on "
        "against a database of known vulnerabilities before allowing a build to proceed. What "
        "practice is this, sometimes abbreviated SCA?",
        ["Software Composition Analysis (dependency vulnerability scanning)", "Chaos engineering", "Blue-green deployment", "A postmortem"],
        0,
        "SCA (Software Composition Analysis) scans your dependency tree against vulnerability "
        "databases, catching a known-vulnerable library (a common real-world breach vector) "
        "before it ships, rather than discovering it after the fact.",
    ),
    _q(
        "Resource limits",
        "One misbehaving container on a shared host consumes so much memory that it starves "
        "every other container on the same machine, degrading unrelated services. What "
        "configuration, if set in advance, would have contained the impact to just that one "
        "container?",
        ["Per-container resource requests/limits", "A bigger Dockerfile", "More Git branches", "A feature flag"],
        0,
        "Setting explicit CPU/memory limits per container caps how much of the shared host's "
        "resources any single 'noisy neighbor' container can consume, protecting the other "
        "containers sharing that host from being starved.",
    ),
    _q(
        "Sidecar pattern",
        "Instead of building logging/metrics-collection logic directly into every application's "
        "codebase, a team deploys a small helper container alongside each application container "
        "that handles this shared concern uniformly. What container pattern is this?",
        ["The sidecar pattern", "Blue-green deployment", "A monolith", "Trunk-based development"],
        0,
        "The sidecar pattern attaches a helper container to the main application container "
        "(sharing its pod/network) to handle a cross-cutting concern like logging or proxying, "
        "without that logic being duplicated inside every application's own code.",
    ),
    _q(
        "Build once, deploy many",
        "A team builds a single container image after tests pass, then promotes that EXACT same "
        "image through staging and into production — rather than rebuilding from source at each "
        "stage. What principle does this follow, and why does it matter?",
        ["Build once, deploy many — it guarantees what's tested is exactly what ships", "Chaos engineering — it deliberately introduces risk", "Trunk-based development — it's about branching, not builds", "GitOps — it's unrelated to image builds"],
        0,
        "Building once and promoting the identical artifact through every environment "
        "guarantees the exact bits that passed testing are the exact bits that reach "
        "production — rebuilding at each stage risks a subtly different result slipping "
        "through (a different dependency version resolving differently, for instance).",
    ),
    _q(
        "Trunk-based development",
        "Instead of long-lived feature branches that diverge from main for weeks, a team commits "
        "small changes directly to the main branch multiple times a day, often behind feature "
        "flags if incomplete. What development practice is this?",
        ["Trunk-based development", "GitOps", "A blue-green deployment", "Chaos engineering"],
        0,
        "Trunk-based development keeps everyone integrating frequently against a single main "
        "branch, avoiding the painful, large merge conflicts that long-lived feature branches "
        "tend to accumulate — incomplete work stays hidden behind feature flags instead of "
        "living on a separate branch.",
    ),
    _q(
        "Infrastructure drift",
        "An engineer makes a quick manual fix directly on a production server to resolve an "
        "urgent issue, but never updates the Infrastructure as Code definition to match. Weeks "
        "later, a routine IaC deployment silently reverts that fix. What problem occurred?",
        ["Infrastructure drift (reality diverged from the declared IaC state)", "A DDoS attack", "A supply chain attack", "Alert fatigue"],
        0,
        "Infrastructure drift happens when the live environment diverges from what's declared "
        "in code — any manual, undocumented change is at risk of being silently overwritten the "
        "next time the IaC is applied, which is exactly why manual production changes are "
        "discouraged.",
    ),
    _q(
        "Load testing",
        "Before a major product launch expected to bring 50x normal traffic, a team simulates "
        "that load against a staging environment to find bottlenecks in advance, rather than "
        "discovering them live during the actual launch. What practice is this?",
        ["Load testing", "A postmortem", "A rollback", "A feature flag toggle"],
        0,
        "Load testing simulates expected (or worse-than-expected) traffic ahead of a known "
        "high-stakes event, surfacing capacity bottlenecks while there's still time to fix them "
        "— far better than finding out live in front of real users.",
    ),
]


# ==================================================================== #
# 11. Cloud Fundamentals & Service Models — Set 3
# ==================================================================== #
CLOUD_FUNDAMENTALS_QUESTIONS_3 = [
    _q(
        "Migration strategy",
        "A company moves its application to the cloud by copying the exact same VMs and "
        "architecture as-is, with no redesign, just to get out of their physical data center "
        "quickly. What migration strategy is this?",
        ["Refactoring", "Lift-and-shift (rehosting)", "Building serverless from scratch", "Multi-cloud"],
        1,
        "Lift-and-shift (rehosting) moves workloads to the cloud with minimal changes — fast "
        "and low-risk, but it doesn't take advantage of cloud-native features. Refactoring "
        "would mean redesigning the application to actually use those features.",
    ),
    _q(
        "Scheduled scaling",
        "An e-commerce platform knows from past data that traffic spikes every day at 6 PM when "
        "people get home from work. Instead of waiting for a reactive CPU-based trigger, they "
        "want extra capacity already running just before 6 PM every day. What should they set up?",
        ["A target-tracking (reactive) policy only", "A scheduled/predictive scaling policy", "A single fixed-size fleet forever", "A CDN"],
        1,
        "Scheduled scaling adds capacity ahead of a KNOWN, predictable pattern (like a daily "
        "peak), rather than waiting for a reactive metric like CPU to cross a threshold after "
        "the spike has already started hurting performance.",
    ),
    _q(
        "Blast radius",
        "A team realizes that every single one of their microservices — regardless of function "
        "— depends on one shared authentication service, and if that one service goes down, "
        "the entire platform stops working. What should they be worried about?",
        ["Too much blast radius concentrated in one dependency", "Too little elasticity", "Too much data residency compliance", "Too many Availability Zones"],
        0,
        "Blast radius describes how much of a system is affected when one component fails. A "
        "single shared dependency that everything relies on creates an outsized blast radius — "
        "one failure cascades everywhere, which is why critical shared services need extra "
        "redundancy.",
    ),
    _q(
        "Warm standby DR",
        "A company keeps a smaller-scale, always-running copy of their production environment "
        "in a second region, ready to be scaled up quickly if the primary region fails — rather "
        "than running nothing at all, or running a full-scale duplicate. What DR pattern is this?",
        ["Pilot light", "Warm standby", "Active-active", "No DR plan at all"],
        1,
        "Warm standby keeps a scaled-down but functional copy running continuously, which can be "
        "scaled up faster than a 'pilot light' (which keeps only the bare minimum core running) "
        "but costs less than full active-active duplication.",
    ),
    _q(
        "Database sharding",
        "A single database instance can no longer handle the write volume of a rapidly growing "
        "user base, so the company splits the data across multiple database instances by user "
        "ID range, with each instance owning a subset of users. What technique is this?",
        ["Database sharding", "A read replica", "A CDN", "Vertical scaling only"],
        0,
        "Sharding horizontally partitions data across multiple database instances (each owning "
        "a subset), which scales WRITE capacity — a read replica, by contrast, only helps with "
        "read traffic and still funnels all writes through one primary.",
    ),
    _q(
        "Geo-DNS routing",
        "A global application wants users in Japan to be automatically routed to servers in "
        "Tokyo, and users in France to servers in Paris, based on where the request originates. "
        "What kind of routing achieves this?",
        ["Geo-DNS / global load balancing", "NAT", "A VPN", "A single static IP for everyone"],
        0,
        "Geo-DNS (or a global/geo load balancer) resolves requests to the nearest healthy "
        "regional endpoint based on the requester's location, minimizing latency for a "
        "geographically distributed user base.",
    ),
    _q(
        "Reserved instance marketplace",
        "A company purchased a 3-year reserved instance commitment, but 18 months in, they no "
        "longer need that capacity. Some cloud providers let them do what with the unused "
        "portion, instead of just wasting the sunk cost?",
        ["Nothing can be done — it's a total loss", "Sell the remaining term on a reserved instance marketplace", "Convert it to a CDN subscription", "Use it as security group credit"],
        1,
        "Some providers run a marketplace where unused reserved capacity can be resold to other "
        "customers, recovering some value instead of paying for capacity nobody uses for the "
        "remaining term.",
    ),
    _q(
        "Consumption-based licensing",
        "A SaaS analytics tool charges customers based on the number of data rows they actually "
        "process each month, rather than a flat fee regardless of usage. What licensing model "
        "is this?",
        ["Per-seat licensing", "Consumption-based (usage-based) licensing", "Perpetual licensing", "Open-source licensing"],
        1,
        "Consumption-based licensing ties cost directly to actual usage (rows processed, API "
        "calls, compute-seconds), aligning cost with value delivered — a different model from "
        "flat per-seat or one-time perpetual licenses.",
    ),
    _q(
        "Consistency models",
        "After writing new data to a distributed cloud database, a read immediately afterward "
        "from a different region might briefly return the OLD value until the update propagates "
        "everywhere. What consistency model does this describe?",
        ["Strong consistency", "Eventual consistency", "No consistency model at all", "Synchronous replication only"],
        1,
        "Eventual consistency accepts a brief window where different replicas may disagree, in "
        "exchange for higher availability and lower latency — strong consistency guarantees "
        "every read sees the latest write immediately, at the cost of more coordination "
        "overhead.",
    ),
    _q(
        "Webhooks",
        "Instead of your application repeatedly polling a third-party payment provider asking "
        "'is this payment done yet?', the payment provider instead sends an HTTP POST to your "
        "server automatically the moment the payment completes. What mechanism is this?",
        ["Polling", "A webhook", "DNS", "A VPN"],
        1,
        "A webhook is a push-based callback: the provider notifies you the instant an event "
        "happens, avoiding the wasted requests and delay inherent in constantly polling "
        "'has anything changed yet?'",
    ),
    _q(
        "Idempotency",
        "A payment API is designed so that if a client's request times out and it retries the "
        "exact same request, the customer is charged only once, not twice. What property does "
        "this API have?",
        ["Idempotency", "Elasticity", "High availability", "Vendor lock-in"],
        0,
        "An idempotent operation produces the same result no matter how many times it's safely "
        "retried — essential for APIs like payments, where a network retry after a timeout must "
        "never double-charge the customer.",
    ),
    _q(
        "Circuit breaker pattern",
        "One microservice keeps timing out, and every other service that calls it keeps waiting "
        "the full timeout period before failing, slowing the ENTIRE system to a crawl. What "
        "pattern would make callers fail fast instead, once a dependency is known to be "
        "unhealthy?",
        ["A circuit breaker", "A load balancer", "A VPN", "A CDN"],
        0,
        "A circuit breaker 'trips' after repeated failures and starts failing fast immediately "
        "(without waiting for the full timeout) until the dependency recovers — preventing one "
        "slow, failing service from cascading delay through the whole system.",
    ),
    _q(
        "Pub/sub messaging",
        "An 'order placed' event needs to simultaneously trigger inventory update, email "
        "confirmation, and analytics logging — three completely independent services all "
        "reacting to the same single event. What messaging pattern fits, where one message can "
        "have many independent subscribers?",
        ["A point-to-point queue (one consumer per message)", "Publish/subscribe (pub/sub)", "A single direct API call to each service in sequence", "NAT"],
        1,
        "Pub/sub lets one published event be delivered to MULTIPLE independent subscribers at "
        "once. A plain point-to-point queue delivers each message to only ONE consumer — the "
        "wrong shape when three unrelated services all need to react to the same event.",
    ),
    _q(
        "Data warehouse vs data lake",
        "A company wants to store years of raw, unstructured log files, images, and sensor data "
        "cheaply, without deciding the exact schema upfront, to be analyzed later by data "
        "scientists. What kind of storage fits better than a structured, schema-first system?",
        ["A traditional relational data warehouse", "A data lake", "Block storage only", "A CDN"],
        1,
        "A data lake stores raw data in its native format at low cost, with schema applied later "
        "at read/query time — a data warehouse, by contrast, expects structured, pre-modeled "
        "data upfront, which doesn't fit 'figure out the schema later' raw data.",
    ),
    _q(
        "Cold start",
        "A serverless function that hasn't been invoked in a while takes a noticeably longer "
        "time to respond to its first request after being idle, compared to subsequent rapid "
        "requests. What is this delay called?",
        ["A cold start", "Elasticity", "A data egress charge", "A blast radius issue"],
        0,
        "A cold start is the extra latency incurred when a serverless platform has to "
        "initialize a new execution environment for a function that hasn't run recently — "
        "subsequent 'warm' invocations reuse an already-initialized environment and respond "
        "much faster.",
    ),
    _q(
        "FinOps",
        "A company forms a dedicated cross-functional practice — combining finance, engineering, "
        "and operations — specifically focused on continuously optimizing and forecasting cloud "
        "spend. What is this practice commonly called?",
        ["DevOps", "FinOps", "SecOps", "GitOps"],
        1,
        "FinOps is the practice of bringing financial accountability to cloud spend, uniting "
        "engineering (which drives usage), finance (which tracks cost), and business "
        "stakeholders around shared, ongoing cost optimization — distinct from DevOps (delivery "
        "speed) or SecOps (security operations).",
    ),
    _q(
        "RPO",
        "A company decides that in a disaster, they can tolerate losing at most 15 minutes' "
        "worth of data — meaning backups or replication must happen at least that frequently. "
        "What metric are they defining?",
        ["Recovery Time Objective (RTO)", "Recovery Point Objective (RPO)", "Service Level Agreement (SLA)", "Total Cost of Ownership (TCO)"],
        1,
        "RPO is about acceptable DATA LOSS, measured in time — a 15-minute RPO means your last "
        "backup/replication point can be at most 15 minutes old. RTO is the separate metric for "
        "how long you're allowed to be DOWN.",
    ),
    _q(
        "Self-service provisioning",
        "Developers at a company can request and provision their own pre-approved cloud "
        "resources through a catalog, without filing a ticket and waiting days for the "
        "infrastructure team to manually provision it. What capability does this represent?",
        ["A self-service catalog / service catalog", "A CDN", "A security group", "Data residency compliance"],
        0,
        "A self-service catalog offers pre-approved, guardrail-compliant resource templates "
        "developers can provision on demand — removing the bottleneck of a central team "
        "manually fulfilling every infrastructure request.",
    ),
    _q(
        "Sandbox accounts",
        "New engineers are given access to a completely separate cloud account, isolated from "
        "production billing and data, specifically to experiment and learn without any risk to "
        "real systems or unexpected charges on the real bill. What is this account called?",
        ["A production account", "A sandbox account", "A shared root account", "A CDN account"],
        1,
        "A sandbox account gives a safe, isolated space to experiment freely, with its own "
        "billing boundary and no access to production data — mistakes here cost nothing and "
        "risk nothing beyond the sandbox itself.",
    ),
    _q(
        "Cloud exit strategy",
        "Before fully committing to a cloud provider, a company's leadership asks the "
        "architecture team to document how they WOULD migrate away if ever needed, and to avoid "
        "unnecessary dependencies on proprietary features where reasonable. What are they "
        "planning for?",
        ["A cloud exit strategy / data portability plan", "A DDoS response plan", "A patch management schedule", "A security group policy"],
        0,
        "An exit strategy considers data portability and avoiding excessive proprietary lock-in "
        "up front, so leaving a provider later (whether for cost, outage history, or strategic "
        "reasons) remains realistically possible rather than practically impossible.",
    ),
]

# ==================================================================== #
# 12. Cloud Security & Shared Responsibility — Set 3
# ==================================================================== #
CLOUD_SECURITY_QUESTIONS_3 = [
    _q(
        "Confidential computing",
        "A healthcare company needs to process sensitive patient data during computation, not "
        "just protect it at rest or in transit — even the cloud provider's own infrastructure "
        "should not be able to see the data while it's being processed in memory. What "
        "technology addresses this?",
        ["Confidential computing (encryption in use)", "Encryption at rest only", "A CDN", "A load balancer"],
        0,
        "Confidential computing uses hardware-based trusted execution environments to keep data "
        "encrypted even WHILE it's being processed in memory — closing the one gap that "
        "at-rest and in-transit encryption alone don't cover.",
    ),
    _q(
        "ABAC",
        "Instead of assigning permissions by job role alone, a system grants access based on a "
        "combination of attributes — department, data classification level, time of day, and "
        "device type — evaluated together for each request. What access control model is this?",
        ["Role-Based Access Control (RBAC)", "Attribute-Based Access Control (ABAC)", "Mandatory Access Control (MAC)", "No access control"],
        1,
        "ABAC evaluates multiple attributes dynamically (not just a fixed role) to make "
        "fine-grained access decisions — more flexible than RBAC's simpler 'role equals "
        "permission set' model, at the cost of more complex policy design.",
    ),
    _q(
        "Break-glass access",
        "During a severe production outage, an on-call engineer needs emergency admin access "
        "that bypasses the normal multi-step approval process, but every use of this emergency "
        "path is heavily logged and triggers an automatic post-incident review. What is this "
        "procedure called?",
        ["Break-glass access", "Least privilege", "Zero Trust", "Data classification"],
        0,
        "Break-glass procedures provide a deliberately fast emergency path for genuine crises, "
        "accepting the normally-tighter controls are bypassed — balanced by heavy logging and "
        "mandatory review afterward so the emergency path itself can't become a silent backdoor.",
    ),
    _q(
        "Threat modeling",
        "Before writing any code for a new payment feature, the team sits down to systematically "
        "ask 'what could go wrong here, and who would want to attack this?', identifying "
        "potential threats and mitigations at the design stage. What practice is this?",
        ["Threat modeling", "Penetration testing", "A postmortem", "Vulnerability scanning"],
        0,
        "Threat modeling (often using a framework like STRIDE) happens proactively during "
        "DESIGN, before code exists — much cheaper than penetration testing, which finds issues "
        "in something already built.",
    ),
    _q(
        "Bug bounty programs",
        "A company publicly invites independent security researchers to find and responsibly "
        "report vulnerabilities in their systems, paying a reward for each valid finding "
        "reported through proper channels. What program is this?",
        ["A bug bounty program", "A red team engagement", "A CSPM tool", "A SOC"],
        0,
        "Bug bounty programs crowdsource vulnerability discovery to a broad pool of external "
        "researchers, paying per valid finding — complementary to, but distinct from, a formal "
        "internal or contracted red team engagement.",
    ),
    _q(
        "Red/blue/purple teams",
        "One group at a company plays the role of attackers trying to breach systems, while a "
        "separate group defends and tries to detect them — and afterward, both groups meet to "
        "share findings and improve defenses together. What are these three roles/practices "
        "called respectively?",
        ["Red team (attack), Blue team (defense), Purple team (collaboration)", "IDS, IPS, WAF", "IaaS, PaaS, SaaS", "RTO, RPO, SLA"],
        0,
        "Red team simulates attackers, blue team defends and detects, and purple team is the "
        "collaborative debrief/integration of both sides' findings to systematically improve "
        "detection and response.",
    ),
    _q(
        "Data sovereignty",
        "A company stores EU customer data in a US-based cloud region. Legal counsel points out "
        "that this could subject the data to US government access laws that wouldn't apply if "
        "it were stored in the EU, regardless of any technical encryption in place. What concept "
        "is this?",
        ["Data residency (only about physical location)", "Data sovereignty (data subject to the laws of where it's stored)", "Data classification", "Data masking"],
        1,
        "Data sovereignty is about which country's LAWS govern the data based on where it "
        "physically resides — related to residency, but the emphasis here is specifically on "
        "legal jurisdiction and government access powers, not just the technical location "
        "itself.",
    ),
    _q(
        "CWPP",
        "A security team wants a single tool that provides consistent protection (vulnerability "
        "management, runtime protection, compliance) across their mix of VMs, containers, and "
        "serverless functions, rather than separate point tools for each. What category of tool "
        "is this?",
        ["A Cloud Workload Protection Platform (CWPP)", "A CDN", "A VPN concentrator", "A load balancer"],
        0,
        "CWPPs provide unified security across heterogeneous workload types (VMs, containers, "
        "serverless) rather than requiring a different disconnected tool for each — increasingly "
        "important as environments mix all three.",
    ),
    _q(
        "Serverless injection risk",
        "A serverless function processes event data (like a message from a queue) and passes "
        "fields from that event directly into a database query without validation. What "
        "category of risk does this event-driven input path introduce?",
        ["No risk — serverless events are always trusted", "An injection vulnerability via untrusted event data", "A billing overage only", "A cold start delay"],
        1,
        "Event data (queue messages, uploaded file metadata, etc.) is still untrusted input, "
        "even though it doesn't arrive through a traditional HTTP form — failing to validate it "
        "before using it in a query creates the same class of injection risk as any other "
        "unsanitized input.",
    ),
    _q(
        "IaC supply chain risk",
        "A team pulls in a popular, publicly shared Terraform module to provision their cloud "
        "infrastructure, without reviewing what it actually does. The module secretly creates an "
        "additional admin user with a hardcoded password. What risk category is this?",
        ["A supply chain risk in third-party Infrastructure as Code", "A DDoS attack", "A data residency violation", "A cold start issue"],
        0,
        "Untrusted or unreviewed third-party IaC modules can embed malicious actions just like "
        "any other supply chain dependency — 'it's just infrastructure config, not application "
        "code' is a dangerous assumption, since IaC has full power to create backdoors.",
    ),
    _q(
        "Data masking/tokenization",
        "Developers need realistic-looking customer data to test with, but must never see real "
        "customers' actual credit card numbers or SSNs. What technique replaces the real "
        "sensitive values with realistic fakes in the test copy?",
        ["Data masking/tokenization", "Encryption at rest", "RBAC", "A CDN"],
        0,
        "Masking/tokenization substitutes sensitive values with realistic but fake equivalents "
        "in non-production copies, so developers can work with production-like data without "
        "ever handling the real sensitive values.",
    ),
    _q(
        "PAM vaulting",
        "Instead of admins remembering and manually rotating shared root/privileged passwords, "
        "a tool automatically stores, rotates, and hands out privileged credentials on demand, "
        "logging every checkout. What category of tool is this?",
        ["A Privileged Access Management (PAM) vault", "A CDN", "A load balancer", "A VPN"],
        0,
        "PAM tools vault privileged credentials centrally, automate their rotation, and audit "
        "every checkout — removing the risk of shared, static, rarely-rotated admin passwords "
        "floating around in spreadsheets or sticky notes.",
    ),
    _q(
        "Distributed/cloud-native firewalls",
        "Instead of one large firewall guarding the network perimeter, security policy is "
        "enforced individually at each workload, following that workload wherever it moves in "
        "the cloud (rather than depending on network location). What model is this?",
        ["A traditional perimeter firewall model", "A distributed/cloud-native firewall model", "No firewall model at all", "A CDN model"],
        1,
        "Distributed firewalls enforce policy per-workload rather than only at a network "
        "perimeter, which fits cloud environments where workloads move dynamically and a single "
        "network boundary is a poor proxy for trust.",
    ),
    _q(
        "UEBA",
        "A tool learns each employee's normal login times, locations, and data access patterns, "
        "then automatically flags a login from an unusual country at 3 AM as suspicious even "
        "though the correct password and MFA code were used. What technology is this?",
        ["User and Entity Behavior Analytics (UEBA)", "A firewall", "A VPN", "A load balancer"],
        0,
        "UEBA baselines normal behavior per user/entity and flags deviations — catching misuse "
        "of otherwise-valid credentials (a compromised account behaving abnormally) that "
        "password and MFA checks alone wouldn't catch.",
    ),
    _q(
        "Right to audit",
        "A large enterprise customer negotiates a contract clause with their cloud vendor "
        "guaranteeing the customer (or an independent auditor on their behalf) can formally "
        "review the vendor's security controls. What is this contractual clause called?",
        ["A right-to-audit clause", "A shared responsibility model", "An SLA", "A data residency clause"],
        0,
        "A right-to-audit clause gives the customer contractual assurance they (or a designated "
        "auditor) can verify the vendor's actual security practices, rather than relying purely "
        "on the vendor's own claims or a generic compliance certificate.",
    ),
    _q(
        "Shared responsibility matrix",
        "A company documents, line by line, exactly which security controls the cloud provider "
        "owns versus which ones the company itself owns, for every service they use — and "
        "reviews this document during audits. What artifact is this?",
        ["A shared responsibility matrix", "A CSPM dashboard", "An incident response plan", "A DDoS mitigation plan"],
        0,
        "A shared responsibility matrix turns the abstract 'shared responsibility model' concept "
        "into a concrete, per-service, auditable document — essential for proving to auditors "
        "exactly who owns what, rather than relying on general understanding alone.",
    ),
    _q(
        "Key escrow",
        "A company's encryption key management policy requires that a securely-stored backup "
        "copy of every encryption key exists, so that if the primary key holder becomes "
        "unavailable, data can still be recovered rather than becoming permanently "
        "inaccessible. What is this backup arrangement called?",
        ["Key escrow / key recovery", "Key rotation", "Zero Trust", "Data masking"],
        0,
        "Key escrow keeps a secure recovery copy of encryption keys, protecting against "
        "permanent data loss if the primary key or key holder is lost — a different concern from "
        "key ROTATION, which is about periodically replacing keys, not backing them up.",
    ),
    _q(
        "Container runtime security",
        "A tool monitors a container WHILE it's running in production, flagging unexpected "
        "behavior like an unfamiliar process suddenly starting inside it — a compromise that "
        "wouldn't have been visible from just scanning the image before deployment. What "
        "category of security tool is this?",
        ["Container image scanning (pre-deployment only)", "Container runtime security monitoring", "A CDN", "A load balancer"],
        1,
        "Runtime security monitors LIVE container behavior for anomalies, catching compromises "
        "that occur after deployment — pre-deployment image scanning only checks the image "
        "BEFORE it ever runs, so it can't detect something that goes wrong at runtime.",
    ),
    _q(
        "Incident response playbooks",
        "Instead of figuring out response steps from scratch during a live ransomware incident, "
        "the security team follows a pre-written, specific step-by-step procedure for exactly "
        "this type of incident. What is this document called?",
        ["An incident response playbook", "A shared responsibility matrix", "A CIS benchmark", "A budget alert"],
        0,
        "Playbooks are pre-written, incident-type-specific procedures (ransomware, data breach, "
        "DDoS, etc.) prepared in advance, so responders execute a rehearsed plan under pressure "
        "instead of inventing a response in real time during the incident itself.",
    ),
    _q(
        "Vendor risk assessment",
        "Before allowing a new third-party SaaS tool to be connected to internal systems, "
        "security reviews the vendor's own security practices, certifications, and data "
        "handling policies. What process is this?",
        ["A vendor/third-party risk assessment", "A CIS benchmark", "A break-glass procedure", "Data masking"],
        0,
        "Vendor risk assessments evaluate a THIRD PARTY's security posture before granting it "
        "access to your systems or data — your own security controls mean little if a "
        "connected vendor is the weak link that gets breached instead.",
    ),
]

# ==================================================================== #
# 13. Network Security — Attacks & Defenses — Set 3
# ==================================================================== #
NETWORK_SECURITY_QUESTIONS_3 = [
    _q(
        "Evil twin",
        "At a coffee shop, an attacker sets up a WiFi access point broadcasting the exact same "
        "name as the shop's real free WiFi, hoping customers connect to the fake one instead. "
        "What is this attack called?",
        ["An evil twin access point", "ARP spoofing", "DNS spoofing", "A botnet"],
        0,
        "An evil twin is a rogue access point mimicking a legitimate one's name (SSID), tricking "
        "victims into connecting through the attacker instead — everything they send can then "
        "be intercepted.",
    ),
    _q(
        "Wardriving",
        "A security researcher drives through a business district with a laptop and antenna, "
        "mapping every wireless network they detect and noting which ones use weak or no "
        "encryption. What is this activity called?",
        ["Wardriving", "Phishing", "Vishing", "A DDoS attack"],
        0,
        "Wardriving is the practice of searching for and mapping wireless networks (often from "
        "a moving vehicle), historically used both by attackers scouting targets and by "
        "researchers/auditors surveying wireless security posture.",
    ),
    _q(
        "Bluesnarfing",
        "An attacker exploits a Bluetooth vulnerability to access and copy contacts, messages, "
        "and files from a nearby phone without the owner's knowledge or permission. What attack "
        "is this?",
        ["Bluesnarfing", "Wardriving", "A DDoS attack", "SQL injection"],
        0,
        "Bluesnarfing is unauthorized access to data over a Bluetooth connection — a reminder "
        "that short-range wireless protocols carry their own distinct attack surface, separate "
        "from WiFi or cellular.",
    ),
    _q(
        "DNS tunneling",
        "An attacker who has already compromised a machine inside a well-monitored corporate "
        "network encodes stolen data inside DNS queries to slip it past firewalls that don't "
        "closely inspect DNS traffic. What technique is this?",
        ["DNS tunneling", "ARP spoofing", "A brute-force attack", "Session hijacking"],
        0,
        "DNS tunneling smuggles data inside DNS queries/responses, a protocol that's often "
        "allowed through firewalls with minimal inspection — making it an effective, "
        "hard-to-detect exfiltration channel once other paths are blocked.",
    ),
    _q(
        "Typosquatting",
        "An attacker registers the domain 'gmai1.com' (with a '1' instead of an 'l') and sets up "
        "a fake login page there, hoping people who mistype the real domain end up handing over "
        "their credentials. What is this technique called?",
        ["Typosquatting", "Business Email Compromise", "ARP spoofing", "A botnet"],
        0,
        "Typosquatting registers domains that are common typos or lookalikes of legitimate ones, "
        "catching victims who mistype a URL or don't look closely at a link before clicking.",
    ),
    _q(
        "Credential stuffing",
        "An attacker takes a huge list of username/password pairs leaked from a completely "
        "different, unrelated website breach, and tries all of them against YOUR login page, "
        "betting that some users reused the same password. What attack is this?",
        ["Password spraying", "Credential stuffing", "A brute-force attack (against one account)", "Session hijacking"],
        1,
        "Credential stuffing reuses KNOWN, previously-leaked username/password pairs across "
        "other sites, betting on password reuse — different from brute-force, which guesses "
        "unknown passwords for a single targeted account.",
    ),
    _q(
        "Password spraying",
        "Instead of trying many passwords against one account (which triggers a lockout), an "
        "attacker tries just ONE common password (like 'Summer2024!') against THOUSANDS of "
        "different accounts, staying under each account's lockout threshold. What attack is "
        "this?",
        ["Password spraying", "Credential stuffing", "Session hijacking", "A supply chain attack"],
        0,
        "Password spraying flips brute-force around: one common password across many accounts, "
        "specifically to stay under any single account's failed-attempt lockout threshold while "
        "still catching whoever happened to choose that common password.",
    ),
    _q(
        "Man-in-the-browser",
        "Malware installed on a user's own computer secretly modifies transactions inside their "
        "browser in real time — for example, changing the destination account number on a bank "
        "transfer — even though the user is on the genuine, correctly-encrypted bank website. "
        "What attack is this?",
        ["Man-in-the-Middle (network-level)", "Man-in-the-browser (malware inside the browser itself)", "DNS spoofing", "ARP spoofing"],
        1,
        "Man-in-the-browser operates INSIDE the compromised browser itself, so it works even "
        "over a perfectly legitimate, correctly-encrypted HTTPS connection — unlike network-level "
        "MITM, encryption in transit provides no protection against this.",
    ),
    _q(
        "Replay attacks",
        "An attacker captures a legitimate, encrypted authentication message sent earlier and "
        "resends it later to fraudulently gain access, without ever needing to decrypt or "
        "understand its contents. What attack is this?",
        ["A replay attack", "A downgrade attack", "A zero-day exploit", "Cryptojacking"],
        0,
        "A replay attack simply re-sends previously captured, valid data to trick a system into "
        "accepting it again — defended against with techniques like timestamps, nonces, or "
        "sequence numbers that make a resent message detectably stale.",
    ),
    _q(
        "Downgrade attacks",
        "An attacker intercepts the initial handshake of a secure connection and manipulates it "
        "so both sides fall back to using an older, known-weak encryption protocol instead of "
        "the strongest one both actually support. What attack is this?",
        ["A downgrade attack", "A replay attack", "Cryptojacking", "A logic bomb"],
        0,
        "Downgrade attacks force a connection to use a weaker, breakable protocol version even "
        "when both parties support something stronger — modern protocols include specific "
        "protections against this exact manipulation.",
    ),
    _q(
        "Cryptojacking",
        "A company notices their cloud bill has spiked dramatically and server CPU usage is "
        "pegged at 100% around the clock, with no legitimate explanation — investigation reveals "
        "malware is using their servers to mine cryptocurrency for the attacker. What is this "
        "called?",
        ["Cryptojacking", "Ransomware", "A DDoS attack", "A rootkit (specifically)"],
        0,
        "Cryptojacking hijacks victim compute resources to mine cryptocurrency for the "
        "attacker's benefit — unlike ransomware, it often tries to stay hidden and keep running "
        "as long as possible, rather than announcing itself with a ransom demand.",
    ),
    _q(
        "Logic bombs",
        "A disgruntled IT employee plants code in the company's systems set to silently delete "
        "critical files on a specific future date, weeks after their planned resignation. What "
        "is this malicious code called?",
        ["A logic bomb", "A worm", "A keylogger", "A honeypot"],
        0,
        "A logic bomb lies dormant until a specific triggering condition (a date, an event, a "
        "missing 'still employed' check) fires — the delayed, condition-based trigger is what "
        "distinguishes it from malware that acts immediately upon infection.",
    ),
    _q(
        "Fileless malware",
        "Antivirus software scanning the hard drive finds nothing suspicious, because the "
        "malware never writes itself to disk as a file at all — it lives entirely in system "
        "memory and abuses legitimate built-in system tools to operate. What is this type of "
        "malware called?",
        ["Fileless malware", "A rootkit (specifically)", "Ransomware", "A worm"],
        0,
        "Fileless malware avoids traditional file-based antivirus detection by operating purely "
        "in memory and abusing legitimate system tools (like PowerShell) — requiring "
        "behavior-based detection instead of signature-based file scanning.",
    ),
    _q(
        "APT",
        "A sophisticated, well-funded attacker group quietly maintains undetected access inside "
        "a target's network for over a year, carefully avoiding detection while slowly "
        "exfiltrating sensitive data. What category of threat is this?",
        ["An Advanced Persistent Threat (APT)", "A DDoS attack", "A brute-force attack", "Baiting"],
        0,
        "APTs are characterized by sophistication, resourcing, and — most distinctively — "
        "PERSISTENCE: long-term, stealthy presence rather than a quick smash-and-grab, typically "
        "associated with well-resourced actors like nation-states.",
    ),
    _q(
        "SIEM",
        "A security team wants one central system that ingests logs from firewalls, servers, and "
        "applications across the whole company, correlates them, and raises an alert when a "
        "pattern across multiple sources suggests an attack. What kind of system is this?",
        ["A SIEM (Security Information and Event Management)", "A WAF", "A VPN", "A CDN"],
        0,
        "A SIEM centralizes and correlates logs from many sources, spotting patterns that would "
        "be invisible looking at any single log source alone — the backbone of most modern "
        "security monitoring operations.",
    ),
    _q(
        "Threat hunting",
        "Rather than waiting passively for an alert to fire, a security analyst proactively "
        "searches through logs and system behavior for signs of a threat that might already be "
        "present but hasn't triggered any automated detection yet. What practice is this?",
        ["Threat hunting", "Vulnerability scanning", "Patch management", "Penetration testing"],
        0,
        "Threat hunting is a proactive, hypothesis-driven search for threats that have evaded "
        "existing automated detection — a mindset shift from 'wait for the alert' to 'assume "
        "something might already be here and go look for it.'",
    ),
    _q(
        "Air gapping",
        "A nuclear facility's most critical control system has no network connection to the "
        "internet or any other network whatsoever — the only way to transfer data to or from it "
        "is by physically carrying removable media. What security measure is this?",
        ["Air gapping", "A VPN", "Network segmentation (with some connectivity)", "A firewall"],
        0,
        "Air gapping physically isolates a system with NO network connection at all — the "
        "strongest possible isolation, distinct from segmentation (which still allows some "
        "controlled connectivity between zones).",
    ),
    _q(
        "Sandboxing",
        "Before allowing an email attachment to reach a user's inbox, a security tool first "
        "opens and executes it in an isolated, disposable virtual environment to observe what "
        "it actually does. What technique is this?",
        ["Sandboxing", "Air gapping", "Network segmentation", "A honeypot"],
        0,
        "Sandboxing detonates suspicious files in an isolated, throwaway environment to observe "
        "their real behavior before deciding whether they're safe to deliver — catching malware "
        "that might evade simple signature-based scanning.",
    ),
    _q(
        "EDR",
        "A security tool installed on every laptop and server continuously monitors process "
        "behavior, can automatically isolate an infected machine from the network, and gives "
        "responders deep visibility for investigation — going well beyond traditional antivirus "
        "signature matching. What category of tool is this?",
        ["Endpoint Detection and Response (EDR)", "A WAF", "A VPN", "A CDN"],
        0,
        "EDR provides continuous behavioral monitoring, automated containment, and deep "
        "forensic visibility at the endpoint level — a significant step up from traditional "
        "signature-based antivirus, which mainly just blocks known-bad files.",
    ),
    _q(
        "SOC",
        "A dedicated team works in shifts around the clock, watching dashboards, investigating "
        "alerts, and coordinating incident response for the entire organization's security "
        "posture. What is this team/facility called?",
        ["A Security Operations Center (SOC)", "A CSPM tool", "A CDN", "A load balancer"],
        0,
        "A SOC is the centralized team (and often physical/virtual facility) responsible for "
        "continuous security monitoring and incident response — the human and process layer "
        "that acts on what tools like SIEM and EDR surface.",
    ),
]

# ==================================================================== #
# 14. Networking Fundamentals — OSI, Protocols & Ports — Set 3
# ==================================================================== #
NETWORKING_FUNDAMENTALS_QUESTIONS_3 = [
    _q(
        "OSI layer 5 (session)",
        "Two applications need to establish, maintain, and eventually cleanly terminate a "
        "back-and-forth dialogue, including handling checkpoints so a long transfer could "
        "resume after a brief interruption. Which OSI layer handles this dialogue management?",
        ["Transport layer", "Session layer", "Presentation layer", "Network layer"],
        1,
        "The Session layer (layer 5) manages the dialogue itself — establishing, maintaining, "
        "synchronizing, and tearing down a session — distinct from the Transport layer below it, "
        "which handles reliable delivery of the actual data.",
    ),
    _q(
        "OSI layer 6 (presentation)",
        "Before data can be understood by the receiving application, it may need to be "
        "translated between character encodings, compressed, or encrypted/decrypted, so both "
        "ends interpret the same bytes the same way. Which OSI layer handles this translation?",
        ["Application layer", "Session layer", "Presentation layer", "Data Link layer"],
        2,
        "The Presentation layer (layer 6) handles data representation — encoding, compression, "
        "and encryption/decryption — ensuring both ends interpret the transmitted data "
        "consistently, regardless of differences in how each system natively represents it.",
    ),
    _q(
        "TCP handshake",
        "Before any data flows over a new TCP connection, the client and server exchange exactly "
        "three specific messages to synchronize and confirm the connection. What is this "
        "three-step exchange called?",
        ["The three-way handshake (SYN, SYN-ACK, ACK)", "The DHCP DORA process", "The ARP resolution process", "The DNS lookup process"],
        0,
        "TCP's three-way handshake (SYN → SYN-ACK → ACK) establishes and synchronizes sequence "
        "numbers for a reliable connection before any actual application data is sent — this is "
        "specifically a TCP mechanism; UDP has no equivalent handshake at all.",
    ),
    _q(
        "TCP teardown",
        "When a TCP connection is done, both sides exchange specific control messages to "
        "gracefully close the connection, rather than just abruptly stopping. What TCP flag "
        "signals 'I'm finished sending data'?",
        ["SYN", "ACK (alone)", "FIN", "RST (a graceful close, not abrupt)"],
        2,
        "FIN signals a graceful connection termination request. SYN is for opening a connection, "
        "plain ACK just acknowledges receipt, and RST is an abrupt, non-graceful reset rather "
        "than an orderly teardown.",
    ),
    _q(
        "Anycast",
        "Multiple servers around the world are all configured with the exact same IP address, "
        "and network routing automatically sends each user's request to whichever one of them "
        "is topologically nearest. What addressing scheme is this?",
        ["Unicast", "Multicast", "Anycast", "Broadcast"],
        2,
        "Anycast lets many geographically distributed servers share one IP address, with "
        "routing sending each request to the nearest instance — this is how many DNS root "
        "servers and CDNs achieve low latency globally from one advertised address.",
    ),
    _q(
        "CIDR notation",
        "A network administrator sees the notation '192.168.1.0/24' in documentation. What does "
        "the '/24' specifically indicate?",
        ["The network uses 24 total addresses", "The first 24 bits of the address are the network portion", "The network can support 24 devices", "The connection speed is 24 Mbps"],
        1,
        "CIDR notation's '/24' means the first 24 bits identify the network, leaving 8 bits for "
        "host addresses (256 addresses, 254 usable) — a compact way to express both an address "
        "and its associated subnet mask together.",
    ),
    _q(
        "Route summarization",
        "Instead of a core router maintaining separate routing table entries for 16 small, "
        "contiguous subnets that all lead to the same next hop, it's configured with just ONE "
        "combined entry covering all of them. What technique is this?",
        ["Route summarization (supernetting)", "NAT", "DHCP", "VLAN tagging"],
        0,
        "Route summarization (supernetting) combines multiple contiguous network routes into "
        "one larger advertised route, shrinking routing table size and update overhead — "
        "especially valuable on core internet routers handling enormous numbers of routes.",
    ),
    _q(
        "Private IP ranges",
        "A network engineer assigns the address 10.0.5.12 to an internal server, knowing this "
        "address is not directly reachable from the public internet. What category of address "
        "range is this?",
        ["A public IP address", "A private IP address (RFC 1918)", "A loopback address", "A multicast address"],
        1,
        "RFC 1918 reserves specific ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) for "
        "private, non-internet-routable use — these addresses can be reused inside countless "
        "different private networks simultaneously without conflict.",
    ),
    _q(
        "Loopback address",
        "A developer wants to test a web server running on their own machine by pointing their "
        "browser back at that same machine, without any traffic actually leaving the computer. "
        "What address do they use?",
        ["10.0.0.1", "127.0.0.1 (loopback)", "255.255.255.255", "0.0.0.0"],
        1,
        "127.0.0.1 (the loopback address) always refers back to the local machine itself — "
        "traffic sent there never leaves the network stack, making it ideal for testing local "
        "services without any actual network transmission.",
    ),
    _q(
        "APIPA",
        "A laptop that failed to receive a response from a DHCP server automatically assigns "
        "itself an address in the 169.254.x.x range. This is a strong diagnostic clue pointing "
        "to what underlying problem?",
        ["A DNS server issue", "A DHCP failure (the device couldn't reach a DHCP server)", "A successful, normal configuration", "A firewall blocking HTTPS"],
        1,
        "A 169.254.x.x (APIPA) address is a Windows/OS self-assigned fallback used specifically "
        "when DHCP fails — seeing this address is a clear diagnostic signal to go check DHCP "
        "connectivity, not a normal successful configuration.",
    ),
    _q(
        "Split-brain",
        "Two nodes in a cluster both lose contact with each other due to a network issue, and "
        "each independently decides it is now the sole active primary, both accepting writes "
        "simultaneously — leading to conflicting data. What problem is this?",
        ["Split-brain (a network partition)", "A DDoS attack", "Route summarization", "A loopback issue"],
        0,
        "Split-brain occurs when a network partition causes nodes to lose contact and each "
        "assumes sole leadership, leading to divergent, conflicting state — clusters use "
        "quorum-based consensus specifically to prevent this scenario.",
    ),
    _q(
        "Link aggregation",
        "A server needs more network throughput and redundancy than a single network cable can "
        "provide, so multiple physical network connections are combined and treated as one "
        "logical, higher-capacity link. What is this called?",
        ["Link aggregation / bonding", "VLAN tagging", "NAT", "Subnetting"],
        0,
        "Link aggregation (bonding/teaming) combines multiple physical links into one logical "
        "link, increasing both throughput and fault tolerance — if one physical cable fails, "
        "traffic continues over the remaining ones.",
    ),
    _q(
        "SDN",
        "A network architecture separates the decision-making logic (which determines where "
        "traffic should go) from the physical devices that actually forward the traffic, "
        "centralizing that intelligence in software instead. What architecture is this?",
        ["Software-Defined Networking (SDN)", "VLAN tagging", "NAT", "A traditional switch fabric"],
        0,
        "SDN separates the control plane (decision-making) from the data plane (packet "
        "forwarding), centralizing network intelligence in software rather than distributing it "
        "across individually-configured physical devices — enabling more flexible, programmable "
        "network management.",
    ),
    _q(
        "BGP",
        "The internet as a whole is made up of thousands of independently-operated networks "
        "(autonomous systems), and a specific routing protocol is what lets them exchange "
        "reachability information with each other at that massive scale. What protocol is this?",
        ["OSPF", "BGP (Border Gateway Protocol)", "RIP", "DHCP"],
        1,
        "BGP is the exterior routing protocol that holds the global internet together, "
        "exchanging routes BETWEEN autonomous systems — OSPF and RIP are interior protocols used "
        "WITHIN a single organization's network instead.",
    ),
    _q(
        "OSPF",
        "Within a single company's internal network, routers automatically build a complete map "
        "of the network topology and calculate the shortest path to every destination using a "
        "link-state protocol. What protocol is this most likely to be?",
        ["BGP", "OSPF", "SMTP", "HTTP"],
        1,
        "OSPF is a common interior (intra-organization) link-state routing protocol that builds "
        "a full topology map and computes shortest paths — BGP instead operates between separate "
        "organizations across the internet.",
    ),
    _q(
        "PDU encapsulation",
        "As data moves down through the OSI layers for transmission, each layer wraps it with "
        "its own header, and the unit gets a different name at each layer. At the Data Link "
        "layer, what is this unit called?",
        ["A segment", "A packet", "A frame", "A bit"],
        2,
        "The naming changes by layer: segment (Transport), packet (Network), frame (Data Link), "
        "and raw bits (Physical) — each layer's header is added ('encapsulated') around the "
        "layer above's unit as data moves down the stack for transmission.",
    ),
    _q(
        "WAN vs LAN vs MAN",
        "A university connects its own network across buildings on one campus (a LAN), but also "
        "connects to its other campus in a different city over links leased from a "
        "telecommunications provider. What type of network is that second, longer-distance "
        "connection?",
        ["Still a LAN, just bigger", "A WAN (Wide Area Network)", "A PAN (Personal Area Network)", "A VLAN"],
        1,
        "Connecting sites across a large geographic distance, typically over links leased from "
        "a telecom provider, is the defining characteristic of a WAN — a LAN, by contrast, is "
        "confined to a single site or building.",
    ),
    _q(
        "PPP",
        "Two routers are connected by a single dedicated serial link with no other devices "
        "involved, and need a data link protocol designed specifically for this kind of "
        "direct, two-endpoint connection (including built-in authentication). What protocol "
        "fits this exact scenario?",
        ["Ethernet (802.3)", "PPP (Point-to-Point Protocol)", "WiFi (802.11)", "Token Ring"],
        1,
        "PPP is designed specifically for direct, point-to-point links between exactly two "
        "endpoints (like a dedicated serial or dial-up line), including features like "
        "authentication that a shared-medium protocol like Ethernet doesn't need in the same "
        "way.",
    ),
    _q(
        "TTL field",
        "A misconfigured router creates a routing loop, but packets circulating in that loop "
        "don't actually consume network resources forever — they eventually get discarded. What "
        "IP header field ensures this?",
        ["The TTL (Time To Live) field", "The checksum field", "The source IP field", "The protocol field"],
        0,
        "TTL is decremented by every router a packet passes through and the packet is dropped "
        "once it reaches zero, guaranteeing a looping packet is eventually discarded rather than "
        "circulating forever and wasting bandwidth indefinitely.",
    ),
    _q(
        "Mesh topology",
        "A network is designed so that every device has a direct connection to every other "
        "device, meaning even if several connections fail, devices can usually still reach each "
        "other through an alternate path. What topology provides this kind of redundancy?",
        ["A star topology", "A full mesh topology", "A bus topology", "A single point-to-point link"],
        1,
        "A full mesh topology's defining strength is redundancy — with direct connections "
        "between every pair of devices, there's no single point of failure the way a star "
        "topology's central hub represents, though the cabling cost grows quickly as more "
        "devices are added.",
    ),
]

# ==================================================================== #
# 15. DevOps & Containers — Set 3
# ==================================================================== #
DEVOPS_CONTAINERS_QUESTIONS_3 = [
    _q(
        "Kubernetes namespaces",
        "A single Kubernetes cluster is shared by three different teams, and the platform team "
        "wants each team's resources logically isolated from the others — separate names, "
        "separate resource quotas — without giving each team an entirely separate physical "
        "cluster. What Kubernetes feature achieves this?",
        ["Namespaces", "Ingress", "A sidecar container", "A ConfigMap"],
        0,
        "Namespaces partition a single cluster into logically isolated virtual clusters, letting "
        "multiple teams or environments share the same underlying infrastructure with separate "
        "naming and resource boundaries — cheaper than provisioning a fully separate cluster per "
        "team.",
    ),
    _q(
        "Kubernetes Ingress",
        "External users on the internet need a single, consistent entry point to reach the "
        "correct internal service inside a Kubernetes cluster, with routing rules based on the "
        "requested hostname or URL path. What Kubernetes resource manages this?",
        ["A ConfigMap", "Ingress", "A Persistent Volume", "A namespace"],
        1,
        "Ingress manages external HTTP(S) access into a cluster, routing requests to the "
        "correct internal service based on hostname/path rules — the standard way to expose "
        "multiple services behind one external entry point.",
    ),
    _q(
        "ConfigMaps & Secrets",
        "A containerized application needs its database connection string (non-sensitive) and "
        "its database password (sensitive) supplied at runtime, without baking either into the "
        "container image itself. What two Kubernetes-native objects are designed for exactly "
        "this, one for each type of value?",
        ["Namespaces and Ingress", "ConfigMaps (non-sensitive config) and Secrets (sensitive values)", "Persistent Volumes and Services", "Sidecars and DaemonSets"],
        1,
        "ConfigMaps hold non-sensitive configuration and Secrets hold sensitive values (with "
        "additional access controls), both injected into pods at runtime — keeping "
        "configuration and credentials out of the image itself so the same image can run "
        "identically across environments with different config.",
    ),
    _q(
        "Persistent volumes",
        "A containerized database needs its data to survive even if the container itself "
        "crashes and is replaced — normal container storage is wiped when the container dies. "
        "What Kubernetes concept provides storage that outlives any individual container?",
        ["A Persistent Volume", "A ConfigMap", "A sidecar container", "A namespace"],
        0,
        "Persistent Volumes provide storage with a lifecycle independent of any single "
        "container/pod, so stateful workloads like databases retain their data across restarts "
        "and rescheduling — plain container filesystem storage is ephemeral and disappears with "
        "the container.",
    ),
    _q(
        "Rolling updates",
        "A team wants to deploy a new version by gradually replacing old instances with new "
        "ones a few at a time, keeping the service continuously available throughout, without "
        "maintaining two full parallel environments like blue-green requires. What deployment "
        "strategy is this?",
        ["A rolling update", "Blue-green deployment", "A canary release", "A big-bang deployment"],
        0,
        "A rolling update gradually replaces instances in place, batch by batch, keeping the "
        "service available without doubling infrastructure the way blue-green does — the "
        "tradeoff is that rollback is slightly slower since you're reversing the same gradual "
        "process rather than an instant traffic switch.",
    ),
    _q(
        "Pipeline as Code",
        "Instead of configuring a CI/CD pipeline through a web UI that isn't version-controlled "
        "or reviewable, a team defines the entire pipeline's stages and steps in a YAML file "
        "checked into their Git repository alongside the application code. What practice is "
        "this?",
        ["Pipeline as Code", "GitOps (a related but distinct practice)", "Infrastructure as Code (for infra, not pipelines specifically)", "Chaos engineering"],
        0,
        "Pipeline as Code defines the CI/CD pipeline itself in a version-controlled file, "
        "making pipeline changes reviewable, auditable, and reproducible just like application "
        "code — rather than living as unreviewable clicks in a UI.",
    ),
    _q(
        "Runbooks",
        "When a specific, previously-seen type of alert fires (like 'disk usage above 90%'), "
        "the on-call engineer follows a pre-written, step-by-step document explaining exactly "
        "how to diagnose and resolve that specific known issue. What is this document called?",
        ["A runbook", "A postmortem", "A pipeline", "A service mesh"],
        0,
        "A runbook provides pre-written, specific procedures for KNOWN issue types, letting "
        "an on-call engineer (even one unfamiliar with that particular system) follow a tested "
        "resolution path instead of improvising under pressure.",
    ),
    _q(
        "Error budgets",
        "An SRE team defines that their service is allowed 43 minutes of downtime per month "
        "(matching a 99.9% target) as a defined 'budget.' Once that budget is spent, the team "
        "pauses new feature releases to focus entirely on reliability instead. What concept is "
        "this?",
        ["An error budget", "MTTR", "A rollback", "A postmortem"],
        0,
        "An error budget makes the reliability-vs-velocity tradeoff explicit and quantified — "
        "as long as you're within budget, ship features freely; once it's exhausted, reliability "
        "work takes priority until the budget resets.",
    ),
    _q(
        "Toil reduction",
        "An SRE team notices they spend 15 hours a week manually restarting the same stuck "
        "service and manually rotating the same set of logs — repetitive, manual work with no "
        "lasting improvement. What SRE principle specifically targets eliminating this kind of "
        "work through automation?",
        ["Toil reduction", "Chaos engineering", "GitOps", "Trunk-based development"],
        0,
        "Toil is manual, repetitive, automatable work that scales linearly with system size and "
        "provides no enduring value — SRE explicitly prioritizes automating it away, freeing "
        "engineering time for work that actually improves the system.",
    ),
    _q(
        "Platform engineering",
        "Instead of every application team building and maintaining their own CI/CD setup, "
        "monitoring, and infrastructure provisioning from scratch, a dedicated team builds a "
        "self-service internal platform that all teams use, with sane defaults built in. What "
        "practice is this?",
        ["Platform engineering (internal developer platform)", "Chaos engineering", "Trunk-based development", "A service mesh"],
        0,
        "Platform engineering builds shared, self-service internal tooling and paved paths so "
        "individual application teams don't each reinvent infrastructure, CI/CD, and monitoring "
        "setups from scratch — improving consistency and freeing teams to focus on their actual "
        "product.",
    ),
    _q(
        "Policy as Code",
        "A company wants to automatically block any Infrastructure as Code deployment that "
        "would create a publicly-accessible storage bucket, enforced consistently across every "
        "pipeline rather than relying on manual code review to catch it. What practice codifies "
        "and automatically enforces rules like this?",
        ["Policy as Code (e.g. Open Policy Agent)", "GitOps", "A postmortem", "Chaos engineering"],
        0,
        "Policy as Code expresses governance rules (like 'no public buckets') as automatically "
        "enforced, version-controlled policy, catching violations consistently in the pipeline "
        "rather than depending on every reviewer remembering to check for them manually.",
    ),
    _q(
        "Choosing a deployment strategy",
        "A team needs to test a risky new feature with just 5% of real production users before "
        "committing to a full rollout, while being able to instantly pull back if error rates "
        "spike. Which deployment strategy fits best — rolling update, blue-green, or canary?",
        ["A rolling update", "Blue-green deployment", "A canary release", "None of these support partial rollout"],
        2,
        "A canary release is specifically designed for gradual, percentage-based exposure to "
        "real traffic with easy pullback — a rolling update replaces ALL instances "
        "eventually with no traffic-percentage control, and blue-green is an all-or-nothing "
        "traffic switch between two full environments.",
    ),
    _q(
        "Node affinity",
        "A team wants a specific memory-intensive workload's pods to always be scheduled on "
        "nodes with high-memory hardware, and wants replicas of the SAME workload deliberately "
        "spread across different physical nodes for resilience. What Kubernetes scheduling "
        "features control this?",
        ["Namespaces", "Node affinity (and anti-affinity)", "Ingress rules", "ConfigMaps"],
        1,
        "Node affinity lets you require or prefer scheduling on nodes matching certain "
        "characteristics (like high-memory hardware), while anti-affinity spreads replicas of "
        "the same workload apart — both are scheduling controls layered on top of Kubernetes' "
        "default bin-packing behavior.",
    ),
    _q(
        "Multi-stage builds",
        "A team's container image is 1.5 GB because it includes the full compiler toolchain used "
        "to build the application, even though that toolchain is completely unnecessary at "
        "runtime. What Docker technique produces a much smaller final image by separating the "
        "build environment from the runtime image?",
        ["A multi-stage build", "A sidecar pattern", "A ConfigMap", "Node affinity"],
        0,
        "Multi-stage builds use one build stage with the full toolchain to compile the "
        "application, then copy only the compiled output into a minimal final runtime image — "
        "shrinking image size and reducing the attack surface by excluding build-time tools that "
        "were never needed in production.",
    ),
    _q(
        "Semantic versioning",
        "A library's maintainers release version 2.3.1, then later 2.4.0, then eventually 3.0.0 "
        "— and consumers know that jumping from 2.x to 3.0.0 might require code changes, while "
        "2.3.1 to 2.4.0 should be safe. What versioning scheme are they following?",
        ["Random version numbers", "Semantic versioning (MAJOR.MINOR.PATCH)", "Calendar versioning only", "Git commit hashes as versions"],
        1,
        "Semantic versioning communicates the nature of a change through the version number "
        "itself: MAJOR for breaking changes, MINOR for backward-compatible new features, PATCH "
        "for backward-compatible fixes — letting consumers judge upgrade risk at a glance.",
    ),
    _q(
        "Release cadence",
        "One company ships a new production release every 30 minutes as soon as changes pass "
        "the pipeline. Another company bundles up several weeks of changes into one big, "
        "carefully coordinated release. What's the key operational tradeoff between these two "
        "release cadence philosophies?",
        ["There is no meaningful difference between the two", "Frequent small releases isolate problems to a smaller change set; infrequent big releases bundle more risk into one event", "Only the second approach is considered DevOps at all", "Frequent releases are always slower to develop"],
        1,
        "Frequent, small releases make it much easier to pinpoint which specific tiny change "
        "caused a problem (a core DevOps/continuous delivery argument), while infrequent, large "
        "'release train' style releases bundle many changes together, making it harder to "
        "isolate the cause when something breaks.",
    ),
    _q(
        "Distributed tracing",
        "A single user request passes through eight different microservices before returning a "
        "response, and it's slow — but nobody can tell which of the eight services is actually "
        "responsible for the delay just from separate logs. What observability practice "
        "specifically tracks one request's journey across all the services it touches?",
        ["Centralized logging (alone)", "Distributed tracing", "Health checks", "Chaos engineering"],
        1,
        "Distributed tracing follows a single request end-to-end across every service it "
        "touches, timing each hop — exactly what's needed to pinpoint which ONE of eight "
        "services in a chain is the actual bottleneck, which separate, uncorrelated logs can't "
        "easily show.",
    ),
    _q(
        "Database migration versioning",
        "A team's database schema has changed dozens of times over two years, and they need a "
        "reliable way to apply exactly the right sequence of schema changes when setting up a "
        "new environment, in the correct order, without missing or repeating any. What practice "
        "manages this?",
        ["Database migration versioning (e.g. Flyway/Liquibase-style scripts)", "Blue-green deployment", "A service mesh", "Chaos engineering"],
        0,
        "Versioned migration scripts, applied in a tracked, ordered sequence, let any "
        "environment (new or existing) be reliably brought to the exact right schema state — "
        "manually remembering and reapplying two years of ad-hoc schema changes correctly is "
        "essentially impossible.",
    ),
    _q(
        "Incident severity levels",
        "A company classifies a total outage of their main product as 'SEV1' (immediate, "
        "all-hands response), while a minor cosmetic bug affecting a few users is 'SEV4' "
        "(fix whenever convenient). What is the purpose of this classification system?",
        ["To make incidents sound more dramatic for reports", "To ensure response urgency and resources match actual business impact", "To assign blame to specific engineers", "It's purely for compliance paperwork with no operational value"],
        1,
        "Severity levels ensure the response effort matches actual impact — waking up the whole "
        "team at 3 AM for a cosmetic bug wastes everyone's time, while treating a total outage "
        "as low-priority risks real business damage. The classification drives appropriate "
        "urgency and resourcing.",
    ),
    _q(
        "Smoke tests",
        "Immediately after a new deployment finishes, a small, fast set of tests automatically "
        "checks that the most critical functions (login works, homepage loads, checkout "
        "processes a test order) are functioning, before the deployment is declared successful. "
        "What are these quick post-deployment checks called?",
        ["Smoke tests", "Load tests", "Chaos experiments", "Unit tests (run at deploy time)"],
        0,
        "Smoke tests are a fast, minimal set of checks confirming the most critical paths "
        "work immediately after deployment — designed to catch a badly broken release within "
        "seconds/minutes, well before comprehensive load or full regression testing would even "
        "finish running.",
    ),
]



# ==================================================================== #
# 16. Pseudocode Practice — Set 1
# ==================================================================== #
# Set 1 — Basic control-flow tracing: if/else-if chains and boundary
# conditions, while/for loop accumulators, nested loops, compound
# (AND/OR) conditions, boolean flags, digit manipulation, operator
# precedence, and classic "what does this print?" gotchas (leap year,
# FizzBuzz-style counting).
# ==================================================================== #
PSEUDOCODE_PRACTICE_QUESTIONS = [
    _q(
        "If/else-if chains",
        "Trace this pseudocode for <b>shippingCost(20)</b>:"
        "<pre>function shippingCost(Integer weight)\n"
        "    if (weight &lt;= 5)\n"
        "        Print \"Cost 50\"\n"
        "    else if (weight &lt;= 20)\n"
        "        Print \"Cost 120\"\n"
        "    else if (weight &lt;= 50)\n"
        "        Print \"Cost 250\"\n"
        "    else\n"
        "        Print \"Cost 400\"\n"
        "    end if\n"
        "end function</pre>"
        "What is printed?",
        ["Cost 50", "Cost 120", "Cost 250", "Cost 400"],
        1,
        "weight is 20, so the first check (weight &lt;= 5) fails, but the second check "
        "(weight &lt;= 20) is true because the boundary is inclusive — 20 satisfies \"&lt;= 20\". "
        "A common mistake is assuming 20 falls into the next bracket, forgetting that "
        "<= includes the boundary value itself.",
    ),
    _q(
        "Nested if",
        "Trace this pseudocode for <b>check(7)</b>:"
        "<pre>function check(Integer n)\n"
        "    if (n &gt; 0)\n"
        "        if (n mod 2 == 0)\n"
        "            Print \"Positive Even\"\n"
        "        else\n"
        "            Print \"Positive Odd\"\n"
        "        end if\n"
        "    else\n"
        "        Print \"Non-positive\"\n"
        "    end if\n"
        "end function</pre>"
        "What is printed?",
        ["Positive Even", "Positive Odd", "Non-positive", "Nothing is printed"],
        1,
        "7 &gt; 0 so we enter the outer branch, then 7 mod 2 == 1 (not 0) so the inner "
        "else fires, printing \"Positive Odd\". The outer \"Non-positive\" branch is a "
        "distractor that would only trigger for n &lt;= 0.",
    ),
    _q(
        "While loop accumulator",
        "Trace this pseudocode for <b>sumN(5)</b>:"
        "<pre>function sumN(Integer n)\n"
        "    Integer i = 1, total = 0\n"
        "    while (i &lt;= n)\n"
        "        total = total + i\n"
        "        i = i + 1\n"
        "    end while\n"
        "    Print total\n"
        "end function</pre>"
        "What is printed?",
        ["10", "15", "20", "5"],
        1,
        "The loop adds 1+2+3+4+5, giving 15. A frequent slip is stopping one iteration "
        "early (missing i == n because of an off-by-one read of \"i &lt;= n\"), which "
        "would wrongly give 10 (1+2+3+4).",
    ),
    _q(
        "For loop with step",
        "Trace this pseudocode for <b>sumEven(10)</b>:"
        "<pre>function sumEven(Integer n)\n"
        "    Integer total = 0\n"
        "    for i = 2 to n step 2\n"
        "        total = total + i\n"
        "    end for\n"
        "    Print total\n"
        "end function</pre>"
        "What is printed?",
        ["25", "30", "45", "55"],
        1,
        "The loop visits 2, 4, 6, 8, 10 (step 2), summing to 30. Summing 1 through 10 "
        "instead (ignoring the step and the starting value of 2) would incorrectly give 55.",
    ),
    _q(
        "Iterative accumulation",
        "Trace this pseudocode for <b>product(4)</b>:"
        "<pre>function product(Integer n)\n"
        "    Integer i = 1, result = 1\n"
        "    while (i &lt;= n)\n"
        "        result = result * i\n"
        "        i = i + 1\n"
        "    end while\n"
        "    Print result\n"
        "end function</pre>"
        "What is printed?",
        ["6", "12", "24", "120"],
        2,
        "This is an iterative factorial: result multiplies 1*2*3*4 = 24. 120 would be "
        "5! (running one extra iteration), a common off-by-one error when tracing "
        "\"i &lt;= n\" loops.",
    ),
    _q(
        "Nested loop counting",
        "Trace this pseudocode for <b>pattern(4)</b>:"
        "<pre>function pattern(Integer n)\n"
        "    Integer count = 0\n"
        "    for i = 1 to n\n"
        "        for j = 1 to i\n"
        "            count = count + 1\n"
        "        end for\n"
        "    end for\n"
        "    Print count\n"
        "end function</pre>"
        "What is printed?",
        ["8", "10", "12", "16"],
        1,
        "The inner loop runs i times for each outer i, so the total is 1+2+3+4 = 10 "
        "(a triangular number). Multiplying n*n (16) is a common wrong shortcut that "
        "ignores that the inner bound depends on the outer variable i, not n.",
    ),
    _q(
        "Conditional counting in a loop",
        "Trace this pseudocode for <b>countOdd(9)</b>:"
        "<pre>function countOdd(Integer n)\n"
        "    Integer count = 0\n"
        "    for i = 1 to n\n"
        "        if (i mod 2 != 0)\n"
        "            count = count + 1\n"
        "        end if\n"
        "    end for\n"
        "    Print count\n"
        "end function</pre>"
        "What is printed?",
        ["4", "5", "9", "0"],
        1,
        "Odd numbers from 1 to 9 are 1, 3, 5, 7, 9 — five of them. Answering 4 mistakes "
        "the count of even numbers in the same range for the count of odd ones.",
    ),
    _q(
        "Swap without a temp variable",
        "Trace this pseudocode for <b>swapTrick(5, 9)</b>:"
        "<pre>function swapTrick(Integer a, Integer b)\n"
        "    a = a + b\n"
        "    b = a - b\n"
        "    a = a - b\n"
        "    Print a\n"
        "    Print b\n"
        "end function</pre>"
        "What is printed?",
        ["5 then 9", "9 then 5", "14 then 5", "9 then 14"],
        1,
        "This is the classic add/subtract swap trick: a becomes 14 (5+9), then b becomes "
        "14-9=5, then a becomes 14-5=9. So it prints 9 then 5 — the values of a and b have "
        "swapped without ever using a third variable.",
    ),
    _q(
        "Digit manipulation — reverse",
        "Trace this pseudocode for <b>reverseNum(1234)</b>:"
        "<pre>function reverseNum(Integer n)\n"
        "    Integer rev = 0\n"
        "    while (n &gt; 0)\n"
        "        Integer digit = n mod 10\n"
        "        rev = rev * 10 + digit\n"
        "        n = n / 10\n"
        "    end while\n"
        "    Print rev\n"
        "end function</pre>"
        "(Assume integer division.) What is printed?",
        ["1234", "4321", "4320", "1230"],
        1,
        "Each iteration peels off the last digit of n (via mod 10) and appends it to rev, "
        "so 1234 becomes 4321 digit by digit. 4320 would result from mistakenly dropping "
        "the final digit (1) instead of appending it.",
    ),
    _q(
        "Digit manipulation — sum",
        "Trace this pseudocode for <b>sumDigits(4521)</b>:"
        "<pre>function sumDigits(Integer n)\n"
        "    Integer sum = 0\n"
        "    while (n &gt; 0)\n"
        "        sum = sum + (n mod 10)\n"
        "        n = n / 10\n"
        "    end while\n"
        "    Print sum\n"
        "end function</pre>"
        "(Assume integer division.) What is printed?",
        ["10", "12", "13", "4521"],
        1,
        "The loop extracts each digit with mod 10 and adds it: 4+5+2+1 = 12 (digits are "
        "consumed in reverse order — 1, 2, 5, 4 — but addition is commutative so order "
        "doesn't change the total).",
    ),
    _q(
        "Loop with early return",
        "Trace this pseudocode for <b>isPrime(15)</b>:"
        "<pre>function isPrime(Integer n)\n"
        "    if (n &lt; 2)\n"
        "        return false\n"
        "    end if\n"
        "    for i = 2 to n - 1\n"
        "        if (n mod i == 0)\n"
        "            return false\n"
        "        end if\n"
        "    end for\n"
        "    return true\n"
        "end function</pre>"
        "What does isPrime(15) return?",
        ["true", "false", "15", "0"],
        1,
        "When i reaches 3, 15 mod 3 == 0, so the function returns false immediately "
        "without checking the remaining values of i. A trace that forgets the early "
        "return would incorrectly run the loop to completion and answer true.",
    ),
    _q(
        "Compound condition — AND",
        "Trace this pseudocode:"
        "<pre>function loopTrace()\n"
        "    Integer i = 0, j = 10\n"
        "    while (i &lt; 5 and j &gt; 0)\n"
        "        i = i + 1\n"
        "        j = j - 3\n"
        "    end while\n"
        "    Print i\n"
        "    Print j\n"
        "end function</pre>"
        "What is printed?",
        ["4 then -2", "5 then -5", "4 then 1", "3 then 1"],
        0,
        "The loop runs while BOTH conditions hold. After 4 iterations i=4, j=-2; checking "
        "again, i &lt; 5 is true but j &gt; 0 is now false, so the AND fails and the loop "
        "stops with i=4, j=-2. Answering \"5 then -5\" wrongly assumes the loop runs one "
        "more time after j goes negative.",
    ),
    _q(
        "Compound condition — OR",
        "Trace this pseudocode:"
        "<pre>function trace2()\n"
        "    Integer x = 1, count = 0\n"
        "    while (x &lt; 20 or count &lt; 2)\n"
        "        x = x * 2\n"
        "        count = count + 1\n"
        "    end while\n"
        "    Print x\n"
        "    Print count\n"
        "end function</pre>"
        "What is printed?",
        ["16 then 4", "32 then 5", "20 then 5", "32 then 4"],
        1,
        "With OR, the loop keeps running as long as EITHER condition is true, so it only "
        "stops once x reaches 32 (&gt;=20) AND count reaches 5 (&gt;=2) simultaneously. "
        "Stopping at x=16 (\"16 then 4\") wrongly treats this like an AND condition and "
        "quits as soon as x &gt;= 20 alone looks close.",
    ),
    _q(
        "Multi-branch comparison",
        "Trace this pseudocode for <b>findMax(7, 7, 5)</b>:"
        "<pre>function findMax(Integer a, Integer b, Integer c)\n"
        "    if (a &gt;= b and a &gt;= c)\n"
        "        Print a\n"
        "    else if (b &gt;= a and b &gt;= c)\n"
        "        Print b\n"
        "    else\n"
        "        Print c\n"
        "    end if\n"
        "end function</pre>"
        "What is printed?",
        ["7", "5", "Nothing", "It prints both 7 and 7"],
        0,
        "Since a==7 and b==7 are tied, the first condition (a &gt;= b and a &gt;= c) is "
        "still true because &gt;= allows equality, so a (7) is printed. Assuming a tie "
        "means neither branch fires (\"Nothing\") ignores that &gt;= includes the equal case.",
    ),
    _q(
        "Counting iterations to a threshold",
        "Trace this pseudocode for <b>iterations(100)</b>:"
        "<pre>function iterations(Integer n)\n"
        "    Integer count = 0\n"
        "    Integer val = 1\n"
        "    while (val &lt; n)\n"
        "        val = val * 3\n"
        "        count = count + 1\n"
        "    end while\n"
        "    Print count\n"
        "end function</pre>"
        "What is printed?",
        ["3", "4", "5", "6"],
        2,
        "val grows 1 -> 3 -> 9 -> 27 -> 81 -> 243, which takes 5 multiplications before "
        "val (243) is no longer less than 100. Stopping the count at val=81 (still &lt; "
        "100) one step too early would wrongly give 4.",
    ),
    _q(
        "Operator precedence",
        "Trace this pseudocode:"
        "<pre>function calc()\n"
        "    Integer a = 10, b = 3, c = 2\n"
        "    Integer result = a + b * c - a / c\n"
        "    Print result\n"
        "end function</pre>"
        "(Assume integer division.) What is printed?",
        ["11", "13", "8", "20"],
        0,
        "Standard precedence evaluates * and / before + and -: b*c = 6 and a/c = 5, so "
        "result = 10 + 6 - 5 = 11. Evaluating strictly left to right instead (ignoring "
        "precedence) would give a wrong value like 20.",
    ),
    _q(
        "Boolean flag toggling",
        "Trace this pseudocode for <b>toggle(7)</b>:"
        "<pre>function toggle(Integer n)\n"
        "    Boolean flag = true\n"
        "    Integer count = 0\n"
        "    for i = 1 to n\n"
        "        if (flag)\n"
        "            count = count + 1\n"
        "        end if\n"
        "        flag = not flag\n"
        "    end for\n"
        "    Print count\n"
        "end function</pre>"
        "What is printed?",
        ["3", "4", "5", "7"],
        1,
        "flag starts true and flips every iteration, so it's true on iterations 1, 3, 5, "
        "7 — four times out of seven — incrementing count each of those times. Answering "
        "7 would assume count increments on every iteration, ignoring the toggle.",
    ),
    _q(
        "Halving loop",
        "Trace this pseudocode for <b>countHalvings(20)</b>:"
        "<pre>function countHalvings(Integer n)\n"
        "    Integer count = 0\n"
        "    while (n &gt; 1)\n"
        "        n = n / 2\n"
        "        count = count + 1\n"
        "    end while\n"
        "    Print count\n"
        "end function</pre>"
        "(Assume integer division.) What is printed?",
        ["3", "4", "5", "10"],
        1,
        "n goes 20 -> 10 -> 5 -> 2 -> 1, which is 4 halvings before the loop condition "
        "(n &gt; 1) fails. Stopping the count one step early at n=2 would wrongly give 3.",
    ),
    _q(
        "Classic boolean gotcha — leap year",
        "Trace this pseudocode for <b>isLeap(1900)</b>:"
        "<pre>function isLeap(Integer year)\n"
        "    if ((year mod 4 == 0 and year mod 100 != 0) or year mod 400 == 0)\n"
        "        Print \"Leap\"\n"
        "    else\n"
        "        Print \"Not Leap\"\n"
        "    end if\n"
        "end function</pre>"
        "What is printed?",
        ["Leap", "Not Leap", "Error", "1900"],
        1,
        "1900 is divisible by 4 and by 100, so \"year mod 100 != 0\" is false, killing "
        "the first clause; it's also not divisible by 400, so the OR clause fails too — "
        "overall \"Not Leap\". This is the classic century-year exception (1900 is not a "
        "leap year, unlike 2000, which is divisible by 400).",
    ),
    _q(
        "FizzBuzz-style counting",
        "Trace this pseudocode for <b>countMultiples(15)</b>:"
        "<pre>function countMultiples(Integer n)\n"
        "    Integer count = 0\n"
        "    for i = 1 to n\n"
        "        if (i mod 3 == 0 or i mod 5 == 0)\n"
        "            count = count + 1\n"
        "        end if\n"
        "    end for\n"
        "    Print count\n"
        "end function</pre>"
        "What is printed?",
        ["5", "6", "7", "8"],
        2,
        "From 1 to 15, the multiples of 3 or 5 are 3, 5, 6, 9, 10, 12, 15 — seven values "
        "(15 is a multiple of both but is counted only once because of the OR). Counting "
        "multiples of 3 and 5 separately and adding (5 + 3 = 8) double-counts 15.",
    ),
]


# ==================================================================== #
# 17. Pseudocode Practice — Set 2
# ==================================================================== #
# ==================================================================== #
# Set 2 — Arrays & strings: traversal (sum/max/count), linear and binary
# search, swapping/rotating/reversing elements, one pass of bubble and
# selection sort, merging sorted arrays, duplicate detection, and string
# operations (reverse, palindrome, vowel count, character frequency,
# word count).
# ==================================================================== #
PSEUDOCODE_PRACTICE_QUESTIONS_2 = [
    _q(
        "Array traversal — sum",
        "Trace this pseudocode for <b>arraySum(A, 5)</b> with A = [4, 7, 2, 9, 1]:"
        "<pre>function arraySum(Integer A[], Integer n)\n"
        "    Integer sum = 0\n"
        "    for i = 0 to n - 1\n"
        "        sum = sum + A[i]\n"
        "    end for\n"
        "    Print sum\n"
        "end function</pre>"
        "What is printed?",
        ["21", "22", "23", "24"],
        2,
        "Summing every element gives 4+7+2+9+1 = 23. A miscount that skips the last "
        "element (index n-1) would wrongly land on 22.",
    ),
    _q(
        "Array traversal — maximum",
        "Trace this pseudocode for <b>findMax(A, 5)</b> with A = [3, 9, 4, 9, 2]:"
        "<pre>function findMax(Integer A[], Integer n)\n"
        "    Integer max = A[0]\n"
        "    for i = 1 to n - 1\n"
        "        if (A[i] &gt; max)\n"
        "            max = A[i]\n"
        "        end if\n"
        "    end for\n"
        "    Print max\n"
        "end function</pre>"
        "What is printed?",
        ["3", "4", "9", "2"],
        2,
        "max starts at A[0]=3 and updates whenever a larger element is found (at index 1, "
        "value 9); the second occurrence of 9 at index 3 doesn't change anything since it "
        "uses a strict &gt;, not &gt;=. The final max is 9.",
    ),
    _q(
        "Linear search",
        "Trace this pseudocode for <b>linearSearch(A, 5, 4)</b> with A = [6, 2, 9, 4, 8]:"
        "<pre>function linearSearch(Integer A[], Integer n, Integer key)\n"
        "    for i = 0 to n - 1\n"
        "        if (A[i] == key)\n"
        "            return i\n"
        "        end if\n"
        "    end for\n"
        "    return -1\n"
        "end function</pre>"
        "What is returned?",
        ["2", "3", "4", "-1"],
        1,
        "Scanning left to right, A[0]=6, A[1]=2, A[2]=9, A[3]=4 — the key 4 is found at "
        "index 3, so 3 is returned. Returning -1 would be correct only if the key were "
        "absent from the array, which isn't the case here.",
    ),
    _q(
        "Binary search",
        "Trace this pseudocode for <b>binarySearch(A, 7, 25)</b> with "
        "A = [3, 7, 11, 19, 25, 31, 42]:"
        "<pre>function binarySearch(Integer A[], Integer n, Integer key)\n"
        "    Integer low = 0, high = n - 1\n"
        "    while (low &lt;= high)\n"
        "        Integer mid = (low + high) / 2\n"
        "        if (A[mid] == key)\n"
        "            return mid\n"
        "        else if (A[mid] &lt; key)\n"
        "            low = mid + 1\n"
        "        else\n"
        "            high = mid - 1\n"
        "        end if\n"
        "    end while\n"
        "    return -1\n"
        "end function</pre>"
        "(Assume integer division.) What is returned?",
        ["2", "3", "4", "5"],
        2,
        "First mid=3 (A[3]=19 &lt; 25, so low=4); next mid=5 (A[5]=31 &gt; 25, so high=4); "
        "next mid=4 (A[4]=25 == key), returning index 4. Stopping after the first "
        "comparison and guessing the midpoint (index 3) would be wrong since A[3] isn't 25.",
    ),
    _q(
        "Swapping array elements",
        "Trace this pseudocode for <b>swapEnds(A, 5)</b> with A = [10, 20, 30, 40, 50]:"
        "<pre>function swapEnds(Integer A[], Integer n)\n"
        "    Integer temp = A[0]\n"
        "    A[0] = A[n - 1]\n"
        "    A[n - 1] = temp\n"
        "    for i = 0 to n - 1\n"
        "        Print A[i]\n"
        "    end for\n"
        "end function</pre>"
        "What is printed?",
        ["10 20 30 40 50", "50 20 30 40 10", "50 40 30 20 10", "10 40 30 20 50"],
        1,
        "Only the first and last elements swap places (10 and 50); the middle elements "
        "(20, 30, 40) are untouched. Reversing the entire array (\"50 40 30 20 10\") "
        "confuses this with a full array reversal.",
    ),
    _q(
        "One pass of bubble sort",
        "Trace ONE pass of this pseudocode for <b>onePass(A, 5)</b> with A = [9, 3, 7, 1, 5]:"
        "<pre>function onePass(Integer A[], Integer n)\n"
        "    for i = 0 to n - 2\n"
        "        if (A[i] &gt; A[i + 1])\n"
        "            Integer temp = A[i]\n"
        "            A[i] = A[i + 1]\n"
        "            A[i + 1] = temp\n"
        "        end if\n"
        "    end for\n"
        "    Print A\n"
        "end function</pre>"
        "What is the array after this single pass?",
        ["[3, 7, 1, 5, 9]", "[3, 9, 7, 1, 5]", "[1, 3, 5, 7, 9]", "[9, 3, 7, 1, 5]"],
        0,
        "A single bubble-sort pass compares adjacent pairs left to right, swapping when "
        "out of order: 9&gt;3 swap, 9&gt;7 swap, 9&gt;1 swap, 9&gt;5 swap — the largest "
        "value (9) \"bubbles\" all the way to the end, giving [3, 7, 1, 5, 9]. The fully "
        "sorted array would only appear after multiple passes, not just one.",
    ),
    _q(
        "One pass of selection sort",
        "Trace ONE pass of this pseudocode for <b>selectionPass(A, 5)</b> with "
        "A = [8, 4, 6, 2, 7]:"
        "<pre>function selectionPass(Integer A[], Integer n)\n"
        "    Integer minIndex = 0\n"
        "    for i = 1 to n - 1\n"
        "        if (A[i] &lt; A[minIndex])\n"
        "            minIndex = i\n"
        "        end if\n"
        "    end for\n"
        "    Integer temp = A[0]\n"
        "    A[0] = A[minIndex]\n"
        "    A[minIndex] = temp\n"
        "    Print A\n"
        "end function</pre>"
        "What is the array after this single pass?",
        ["[2, 4, 6, 8, 7]", "[2, 8, 6, 4, 7]", "[4, 8, 6, 2, 7]", "[8, 4, 6, 2, 7]"],
        0,
        "Selection sort's one pass scans the whole array for the minimum (2, at index 3) "
        "and swaps it into position 0, giving [2, 4, 6, 8, 7]. Unlike bubble sort, the "
        "other elements keep their relative order — only positions 0 and 3 change.",
    ),
    _q(
        "Reversing an array",
        "Trace this pseudocode for <b>reverseArray(A, 5)</b> with A = [1, 2, 3, 4, 5]:"
        "<pre>function reverseArray(Integer A[], Integer n)\n"
        "    Integer left = 0, right = n - 1\n"
        "    while (left &lt; right)\n"
        "        Integer temp = A[left]\n"
        "        A[left] = A[right]\n"
        "        A[right] = temp\n"
        "        left = left + 1\n"
        "        right = right - 1\n"
        "    end while\n"
        "    Print A\n"
        "end function</pre>"
        "What is printed?",
        ["[5, 4, 3, 2, 1]", "[1, 2, 3, 4, 5]", "[5, 2, 3, 4, 1]", "[1, 4, 3, 2, 5]"],
        0,
        "The two pointers swap elements from both ends moving inward (swap indices 0&4, "
        "then 1&3), fully reversing the array to [5, 4, 3, 2, 1]. Swapping only the "
        "outermost pair once (\"[5, 2, 3, 4, 1]\") stops the trace too early.",
    ),
    _q(
        "Counting occurrences",
        "Trace this pseudocode for <b>countValue(A, 6, 2)</b> with A = [2, 5, 2, 8, 2, 9]:"
        "<pre>function countValue(Integer A[], Integer n, Integer key)\n"
        "    Integer count = 0\n"
        "    for i = 0 to n - 1\n"
        "        if (A[i] == key)\n"
        "            count = count + 1\n"
        "        end if\n"
        "    end for\n"
        "    Print count\n"
        "end function</pre>"
        "What is printed?",
        ["2", "3", "4", "1"],
        1,
        "The value 2 appears at indices 0, 2, and 4 — three times total. Stopping after "
        "the second match (\"2\") would undercount the occurrence at index 4.",
    ),
    _q(
        "Second largest element",
        "Trace this pseudocode for <b>secondLargest(A, 6)</b> with A = [12, 35, 1, 10, 34, 1]:"
        "<pre>function secondLargest(Integer A[], Integer n)\n"
        "    Integer first = -1, second = -1\n"
        "    for i = 0 to n - 1\n"
        "        if (A[i] &gt; first)\n"
        "            second = first\n"
        "            first = A[i]\n"
        "        else if (A[i] &gt; second)\n"
        "            second = A[i]\n"
        "        end if\n"
        "    end for\n"
        "    Print second\n"
        "end function</pre>"
        "What is printed?",
        ["35", "34", "12", "10"],
        1,
        "first ends up as 35 (the largest), and second is updated to 34 once 34 is seen "
        "(it's bigger than the previous second, 12, but not bigger than first, 35). "
        "Answering 12 stops tracking updates to second too early, missing the later 34.",
    ),
    _q(
        "Checking sorted order",
        "Trace this pseudocode for <b>isSorted(A, 5)</b> with A = [2, 4, 4, 7, 9]:"
        "<pre>function isSorted(Integer A[], Integer n)\n"
        "    for i = 0 to n - 2\n"
        "        if (A[i] &gt; A[i + 1])\n"
        "            return false\n"
        "        end if\n"
        "    end for\n"
        "    return true\n"
        "end function</pre>"
        "What is returned?",
        ["true", "false", "0", "4"],
        0,
        "Every adjacent pair satisfies A[i] &lt;= A[i+1] (2&lt;=4, 4&lt;=4, 4&lt;=7, "
        "7&lt;=9), including the repeated 4s since the check is a strict &gt; that only "
        "fails on a genuine decrease, so the loop completes and returns true.",
    ),
    _q(
        "String reversal",
        "Trace this pseudocode for <b>reverseString(\"ACCENT\")</b>:"
        "<pre>function reverseString(String s)\n"
        "    Integer n = length(s)\n"
        "    String rev = \"\"\n"
        "    for i = n - 1 to 0 step -1\n"
        "        rev = rev + s[i]\n"
        "    end for\n"
        "    Print rev\n"
        "end function</pre>"
        "What is printed?",
        ["ACCENT", "TNECCA", "TNECAA", "CCENTA"],
        1,
        "The loop walks the string from the last character to the first, appending each "
        "one, so \"ACCENT\" becomes \"TNECCA\". Reading the letters out of order (e.g. "
        "\"TNECAA\") is an easy transcription slip when tracing character by character.",
    ),
    _q(
        "Palindrome check",
        "Trace this pseudocode for <b>isPalindrome(\"MALAYALAM\")</b>:"
        "<pre>function isPalindrome(String s)\n"
        "    Integer left = 0, right = length(s) - 1\n"
        "    while (left &lt; right)\n"
        "        if (s[left] != s[right])\n"
        "            return false\n"
        "        end if\n"
        "        left = left + 1\n"
        "        right = right - 1\n"
        "    end while\n"
        "    return true\n"
        "end function</pre>"
        "What is returned?",
        ["true", "false", "9", "0"],
        0,
        "\"MALAYALAM\" reads the same forwards and backwards, so every s[left]/s[right] "
        "comparison matches as the pointers close in, and the loop finishes without ever "
        "triggering the false return, so it returns true.",
    ),
    _q(
        "Counting vowels",
        "Trace this pseudocode for <b>countVowels(\"pseudocode\")</b>:"
        "<pre>function countVowels(String s)\n"
        "    Integer count = 0\n"
        "    for i = 0 to length(s) - 1\n"
        "        Character c = s[i]\n"
        "        if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u')\n"
        "            count = count + 1\n"
        "        end if\n"
        "    end for\n"
        "    Print count\n"
        "end function</pre>"
        "What is printed?",
        ["3", "4", "5", "6"],
        2,
        "\"pseudocode\" contains the vowels e, u, o, o, e — five in total. Miscounting by "
        "treating the two o's as one occurrence would wrongly give 4.",
    ),
    _q(
        "Character frequency",
        "Trace this pseudocode for <b>charFrequency(\"banana\", 'a')</b>:"
        "<pre>function charFrequency(String s, Character target)\n"
        "    Integer count = 0\n"
        "    for i = 0 to length(s) - 1\n"
        "        if (s[i] == target)\n"
        "            count = count + 1\n"
        "        end if\n"
        "    end for\n"
        "    Print count\n"
        "end function</pre>"
        "What is printed?",
        ["2", "3", "4", "1"],
        1,
        "\"banana\" has 'a' at positions 1, 3, and 5 — three occurrences. Counting only "
        "the first two occurrences (\"2\") misses the final 'a' at the end of the string.",
    ),
    _q(
        "Rotating an array",
        "Trace this pseudocode for <b>rotateLeft(A, 5)</b> with A = [1, 2, 3, 4, 5]:"
        "<pre>function rotateLeft(Integer A[], Integer n)\n"
        "    Integer first = A[0]\n"
        "    for i = 0 to n - 2\n"
        "        A[i] = A[i + 1]\n"
        "    end for\n"
        "    A[n - 1] = first\n"
        "    Print A\n"
        "end function</pre>"
        "What is printed?",
        ["[2, 3, 4, 5, 1]", "[5, 1, 2, 3, 4]", "[1, 2, 3, 4, 5]", "[5, 4, 3, 2, 1]"],
        0,
        "Each element shifts one position left (A[i] = A[i+1]), and the saved first "
        "element (1) wraps around to the last slot, giving [2, 3, 4, 5, 1]. Placing it at "
        "the front instead (\"[5, 1, 2, 3, 4]\") describes a right rotation, not this code.",
    ),
    _q(
        "Merging two sorted arrays",
        "Trace this pseudocode for <b>mergeArrays(A, B, 3, 3)</b> with A = [2, 5, 8] "
        "and B = [1, 4, 9]:"
        "<pre>function mergeArrays(Integer A[], Integer B[], Integer n, Integer m)\n"
        "    Integer i = 0, j = 0\n"
        "    while (i &lt; n and j &lt; m)\n"
        "        if (A[i] &lt;= B[j])\n"
        "            Print A[i]\n"
        "            i = i + 1\n"
        "        else\n"
        "            Print B[j]\n"
        "            j = j + 1\n"
        "        end if\n"
        "    end while\n"
        "    while (i &lt; n)\n"
        "        Print A[i]\n"
        "        i = i + 1\n"
        "    end while\n"
        "    while (j &lt; m)\n"
        "        Print B[j]\n"
        "        j = j + 1\n"
        "    end while\n"
        "end function</pre>"
        "What is the full sequence printed?",
        ["1 2 4 5 8 9", "2 5 8 1 4 9", "1 2 4 8 5 9", "2 1 5 4 8 9"],
        0,
        "The two-pointer merge always prints the smaller of the two current front "
        "elements: 1, then 2, then 4, then 5, then 8, then the leftover 9 — the classic "
        "merge step of merge sort. Simply printing A then B in order ignores the "
        "interleaving comparison the code actually performs.",
    ),
    _q(
        "Duplicate detection",
        "Trace this pseudocode for <b>hasDuplicate(A, 6)</b> with A = [5, 1, 9, 3, 5, 7]:"
        "<pre>function hasDuplicate(Integer A[], Integer n)\n"
        "    for i = 0 to n - 2\n"
        "        for j = i + 1 to n - 1\n"
        "            if (A[i] == A[j])\n"
        "                return true\n"
        "            end if\n"
        "        end for\n"
        "    end for\n"
        "    return false\n"
        "end function</pre>"
        "What is returned?",
        ["true", "false", "5", "-1"],
        0,
        "The nested loop compares every pair of elements; when i=0 (A[0]=5) and j=4 "
        "(A[4]=5) match, it returns true immediately. Because 5 does repeat in this "
        "array, false would be the wrong conclusion.",
    ),
    _q(
        "Counting words",
        "Trace this pseudocode for <b>countWords(\"THIS IS A TEST STRING\")</b>:"
        "<pre>function countWords(String s)\n"
        "    Integer count = 1\n"
        "    for i = 0 to length(s) - 1\n"
        "        if (s[i] == ' ')\n"
        "            count = count + 1\n"
        "        end if\n"
        "    end for\n"
        "    Print count\n"
        "end function</pre>"
        "What is printed?",
        ["4", "5", "6", "20"],
        1,
        "count starts at 1 (accounting for the first word) and increments once per space; "
        "the string has 4 spaces separating 5 words, so the final count is 5. Printing "
        "the number of spaces alone (4) forgets the initial count of 1 for the first word.",
    ),
    _q(
        "Finding a unique element via XOR",
        "Trace this pseudocode for <b>findUnique(A, 5)</b> with A = [4, 3, 4, 5, 3] "
        "(every value except one appears exactly twice):"
        "<pre>function findUnique(Integer A[], Integer n)\n"
        "    Integer result = 0\n"
        "    for i = 0 to n - 1\n"
        "        result = result ^ A[i]\n"
        "    end for\n"
        "    Print result\n"
        "end function</pre>"
        "What is printed?",
        ["3", "4", "5", "0"],
        2,
        "XOR-ing every element cancels out values that appear in pairs (a ^ a == 0) and "
        "leaves only the value that appears once — here that's 5, since 4 and 3 each "
        "appear twice. This trick avoids needing any extra storage to find the odd one out.",
    ),
]


# ==================================================================== #
# 18. Pseudocode Practice — Set 3
# ==================================================================== #
# ==================================================================== #
# Set 3 — Recursion & data structures: recursive factorial/Fibonacci/
# sum/GCD/power/digit-sum, recursive binary search and Tower of Hanoi,
# recursion print-order traces (pre- vs post-recursive-call), stack and
# queue operation traces (including balanced parentheses and a queue
# built from two stacks), full bubble/selection sort traces, and
# time-complexity analysis of loops and recursive calls.
# ==================================================================== #
PSEUDOCODE_PRACTICE_QUESTIONS_3 = [
    _q(
        "Recursive factorial",
        "Trace this pseudocode for <b>factorial(6)</b>:"
        "<pre>function factorial(Integer n)\n"
        "    if (n &lt;= 1)\n"
        "        return 1\n"
        "    end if\n"
        "    return n * factorial(n - 1)\n"
        "end function</pre>"
        "What does factorial(6) return?",
        ["120", "720", "360", "5040"],
        1,
        "factorial(6) = 6*5*4*3*2*1 = 720. 5040 is 7! — an easy slip if you multiply one "
        "extra term (7*6*5*4*3*2*1) by miscounting where the recursion bottoms out.",
    ),
    _q(
        "Recursive Fibonacci",
        "Trace this pseudocode for <b>fib(7)</b>:"
        "<pre>function fib(Integer n)\n"
        "    if (n &lt;= 1)\n"
        "        return n\n"
        "    end if\n"
        "    return fib(n - 1) + fib(n - 2)\n"
        "end function</pre>"
        "What does fib(7) return?",
        ["8", "13", "21", "5"],
        1,
        "The Fibonacci sequence starting fib(0)=0, fib(1)=1 continues 1, 2, 3, 5, 8, 13 — "
        "so fib(7)=13. Answering 21 (fib(8)) is an off-by-one that shifts the whole "
        "sequence forward by one index.",
    ),
    _q(
        "Recursive sum of natural numbers",
        "Trace this pseudocode for <b>sumRec(6)</b>:"
        "<pre>function sumRec(Integer n)\n"
        "    if (n == 0)\n"
        "        return 0\n"
        "    end if\n"
        "    return n + sumRec(n - 1)\n"
        "end function</pre>"
        "What does sumRec(6) return?",
        ["15", "20", "21", "36"],
        2,
        "sumRec(6) unwinds to 6+5+4+3+2+1+0 = 21. 15 is the sum of only 1 through 5 "
        "(i.e., sumRec(5)), a common result of stopping the unwind one call too early.",
    ),
    _q(
        "Recursive array sum",
        "Trace this pseudocode for <b>arraySumRec(A, 4)</b> with A = [5, 10, 15, 20]:"
        "<pre>function arraySumRec(Integer A[], Integer n)\n"
        "    if (n == 0)\n"
        "        return 0\n"
        "    end if\n"
        "    return A[n - 1] + arraySumRec(A, n - 1)\n"
        "end function</pre>"
        "What does arraySumRec(A, 4) return?",
        ["30", "45", "50", "35"],
        2,
        "Each call peels off the last element (A[n-1]) and adds it to the recursive sum "
        "of the rest, unwinding to 20+15+10+5 = 50. Missing the last element A[3]=20 by "
        "misreading the base case would give 30 instead.",
    ),
    _q(
        "Recursive GCD (Euclidean algorithm)",
        "Trace this pseudocode for <b>gcd(48, 18)</b>:"
        "<pre>function gcd(Integer a, Integer b)\n"
        "    if (b == 0)\n"
        "        return a\n"
        "    end if\n"
        "    return gcd(b, a mod b)\n"
        "end function</pre>"
        "What does gcd(48, 18) return?",
        ["6", "9", "12", "18"],
        0,
        "The calls proceed gcd(48,18) -> gcd(18,12) -> gcd(12,6) -> gcd(6,0), and since "
        "b==0 the base case returns a=6. Stopping the trace one call too early at "
        "gcd(12,6) and reading its first argument (12) instead of continuing to the "
        "actual base case is the typical mistake that produces the wrong answer 12.",
    ),
    _q(
        "Recursive power function",
        "Trace this pseudocode for <b>power(3, 4)</b>:"
        "<pre>function power(Integer base, Integer exp)\n"
        "    if (exp == 0)\n"
        "        return 1\n"
        "    end if\n"
        "    return base * power(base, exp - 1)\n"
        "end function</pre>"
        "What does power(3, 4) return?",
        ["12", "27", "64", "81"],
        3,
        "power(3,4) multiplies base by itself exp times: 3*3*3*3 = 81. 64 would be the "
        "result for a different base (4^3 or 2^6), a mix-up that's easy to make when "
        "swapping which argument controls the recursion depth.",
    ),
    _q(
        "Recursive digit sum",
        "Trace this pseudocode for <b>digitSumRec(9327)</b>:"
        "<pre>function digitSumRec(Integer n)\n"
        "    if (n &lt; 10)\n"
        "        return n\n"
        "    end if\n"
        "    return (n mod 10) + digitSumRec(n / 10)\n"
        "end function</pre>"
        "(Assume integer division.) What does digitSumRec(9327) return?",
        ["19", "21", "23", "12"],
        1,
        "Each call extracts the last digit and adds it to the recursive result on the "
        "remaining digits: 7 + (2 + (3 + 9)) = 7+2+3+9 = 21. Dropping the first digit "
        "extracted (7) from the final sum would wrongly give 14, not among the options here.",
    ),
    _q(
        "Recursive binary search — call count",
        "Trace this pseudocode for <b>binSearchRec(A, 0, 7, 16)</b> with "
        "A = [2, 4, 6, 8, 10, 12, 14, 16]:"
        "<pre>function binSearchRec(Integer A[], Integer low, Integer high, Integer key)\n"
        "    if (low &gt; high)\n"
        "        return -1\n"
        "    end if\n"
        "    Integer mid = (low + high) / 2\n"
        "    if (A[mid] == key)\n"
        "        return mid\n"
        "    else if (A[mid] &lt; key)\n"
        "        return binSearchRec(A, mid + 1, high, key)\n"
        "    else\n"
        "        return binSearchRec(A, low, mid - 1, key)\n"
        "    end if\n"
        "end function</pre>"
        "Including the initial call, how many total calls to binSearchRec are made "
        "before the key is found?",
        ["2", "3", "4", "5"],
        2,
        "mid sequence is 3 (A[3]=8&lt;16), 5 (A[5]=12&lt;16), 6 (A[6]=14&lt;16), 7 "
        "(A[7]=16, found) — that's 4 calls total including the initial one. Counting only "
        "the recursive calls and forgetting to include the initial call would give 3.",
    ),
    _q(
        "Tower of Hanoi",
        "Trace this pseudocode for <b>hanoi(4, 'A', 'C', 'B')</b>:"
        "<pre>function hanoi(Integer n, String from, String to, String aux)\n"
        "    if (n == 0)\n"
        "        return 0\n"
        "    end if\n"
        "    Integer moves = hanoi(n - 1, from, aux, to)\n"
        "    moves = moves + 1\n"
        "    moves = moves + hanoi(n - 1, aux, to, from)\n"
        "    return moves\n"
        "end function</pre>"
        "What total move count does hanoi(4, 'A', 'C', 'B') return?",
        ["8", "15", "16", "12"],
        1,
        "Tower of Hanoi always needs 2^n - 1 moves for n disks; for n=4 that's 2^4-1 = "
        "15. Answering 16 (2^4) forgets to subtract the 1 — a very common formula slip.",
    ),
    _q(
        "Recursion print order — before the call",
        "Trace this pseudocode for <b>printDesc(4)</b>:"
        "<pre>function printDesc(Integer n)\n"
        "    if (n == 0)\n"
        "        return\n"
        "    end if\n"
        "    Print n\n"
        "    printDesc(n - 1)\n"
        "end function</pre>"
        "In what order is output printed?",
        ["4 3 2 1", "1 2 3 4", "4 3 2 1 0", "0 1 2 3 4"],
        0,
        "Because Print happens BEFORE the recursive call, each value is printed on the "
        "way down before recursing further, giving 4, 3, 2, 1 (the base case n==0 returns "
        "without printing). This descending order is the opposite of what you'd get if "
        "the print statement came after the recursive call instead.",
    ),
    _q(
        "Recursion print order — after the call",
        "Trace this pseudocode for <b>printAsc(4)</b>:"
        "<pre>function printAsc(Integer n)\n"
        "    if (n == 0)\n"
        "        return\n"
        "    end if\n"
        "    printAsc(n - 1)\n"
        "    Print n\n"
        "end function</pre>"
        "In what order is output printed?",
        ["4 3 2 1", "1 2 3 4", "1 2 3 4 0", "4 2 3 1"],
        1,
        "Because the recursive call happens BEFORE the Print, nothing is printed while "
        "descending to the base case; printing only happens as each call unwinds, so the "
        "smallest value (1) prints first and the largest (4) prints last — 1, 2, 3, 4. "
        "This is the reverse of a function that prints before recursing.",
    ),
    _q(
        "Stack operation trace",
        "Trace this pseudocode:"
        "<pre>function stackTrace()\n"
        "    Stack S = empty\n"
        "    push(S, 5)\n"
        "    push(S, 15)\n"
        "    push(S, 25)\n"
        "    pop(S)\n"
        "    push(S, 35)\n"
        "    push(S, 45)\n"
        "    pop(S)\n"
        "    Print top(S)\n"
        "    Print size(S)\n"
        "end function</pre>"
        "What is printed (top(S), then size(S))?",
        ["25 then 3", "35 then 3", "45 then 3", "35 then 4"],
        1,
        "After push 5,15,25 and a pop (removing 25), the stack is [5,15]; pushing 35 and "
        "45 then popping (removing 45) leaves [5,15,35] — top is 35, size is 3. "
        "Forgetting the second pop would leave 45 on top instead.",
    ),
    _q(
        "Queue operation trace",
        "Trace this pseudocode:"
        "<pre>function queueTrace()\n"
        "    Queue Q = empty\n"
        "    enqueue(Q, 100)\n"
        "    enqueue(Q, 200)\n"
        "    enqueue(Q, 300)\n"
        "    dequeue(Q)\n"
        "    enqueue(Q, 400)\n"
        "    dequeue(Q)\n"
        "    enqueue(Q, 500)\n"
        "    Print front(Q)\n"
        "    Print size(Q)\n"
        "end function</pre>"
        "What is printed (front(Q), then size(Q))?",
        ["100 then 3", "200 then 3", "300 then 3", "300 then 2"],
        2,
        "A queue is FIFO: after enqueuing 100,200,300 and dequeuing (removes 100), then "
        "enqueuing 400 and dequeuing again (removes 200), then enqueuing 500, the queue "
        "holds [300,400,500] — front is 300 and size is 3. A stack-style (LIFO) trace "
        "would incorrectly assume the most recently added item leaves first.",
    ),
    _q(
        "Balanced parentheses using a stack",
        "Trace this pseudocode for <b>isBalanced(\"(()))(\")</b>:"
        "<pre>function isBalanced(String s)\n"
        "    Stack S = empty\n"
        "    for i = 0 to length(s) - 1\n"
        "        if (s[i] == '(')\n"
        "            push(S, s[i])\n"
        "        else if (s[i] == ')')\n"
        "            if (isEmpty(S))\n"
        "                return false\n"
        "            end if\n"
        "            pop(S)\n"
        "        end if\n"
        "    end for\n"
        "    return isEmpty(S)\n"
        "end function</pre>"
        "What does isBalanced(\"(()))(\") return?",
        ["true", "false", "0", "1"],
        1,
        "Processing left to right: '(' push, '(' push, ')' pop, ')' pop (stack now "
        "empty), then the fifth character ')' arrives with an empty stack, so the "
        "function returns false immediately — the trailing '(' is never even reached. "
        "This early-exit behavior is exactly why a stack correctly rejects mismatched "
        "closing brackets without scanning the whole string.",
    ),
    _q(
        "Implementing a queue with two stacks",
        "Trace this pseudocode:"
        "<pre>function twoStackQueue()\n"
        "    Stack S1 = empty, S2 = empty\n"
        "    push(S1, 1)\n"
        "    push(S1, 2)\n"
        "    push(S1, 3)\n"
        "    while (not isEmpty(S1))\n"
        "        push(S2, top(S1))\n"
        "        pop(S1)\n"
        "    end while\n"
        "    Print top(S2)\n"
        "end function</pre>"
        "What is printed?",
        ["1", "2", "3", "Error"],
        0,
        "S1 ends up as [1,2,3] with 3 on top; transferring every element into S2 reverses "
        "the order, so S2 becomes [3,2,1] with 1 on top. This reversal trick is exactly "
        "how a queue's FIFO order (first pushed, 1, becomes first accessible) can be "
        "recovered using two stacks.",
    ),
    _q(
        "Full bubble sort trace",
        "Trace this pseudocode to completion for <b>bubbleSort(A, 4)</b> with "
        "A = [5, 1, 4, 2]:"
        "<pre>function bubbleSort(Integer A[], Integer n)\n"
        "    for i = 0 to n - 2\n"
        "        for j = 0 to n - 2 - i\n"
        "            if (A[j] &gt; A[j + 1])\n"
        "                Integer temp = A[j]\n"
        "                A[j] = A[j + 1]\n"
        "                A[j + 1] = temp\n"
        "            end if\n"
        "        end for\n"
        "    end for\n"
        "    Print A\n"
        "end function</pre>"
        "What is printed after the sort completes?",
        ["[1, 2, 4, 5]", "[1, 4, 2, 5]", "[2, 1, 4, 5]", "[5, 4, 2, 1]"],
        0,
        "Bubble sort's outer loop repeats enough passes to fully sort the array in "
        "ascending order, so the shrinking inner-loop bound (n-2-i) still guarantees "
        "every out-of-order adjacent pair gets fixed across passes, ending at "
        "[1, 2, 4, 5]. A single-pass result like [1, 4, 2, 5] would only be correct "
        "if the outer loop ran once instead of running to completion.",
    ),
    _q(
        "Full selection sort trace",
        "Trace this pseudocode to completion for <b>selectionSort(A, 5)</b> with "
        "A = [29, 10, 14, 37, 13]:"
        "<pre>function selectionSort(Integer A[], Integer n)\n"
        "    for i = 0 to n - 2\n"
        "        Integer minIdx = i\n"
        "        for j = i + 1 to n - 1\n"
        "            if (A[j] &lt; A[minIdx])\n"
        "                minIdx = j\n"
        "            end if\n"
        "        end for\n"
        "        Integer temp = A[i]\n"
        "        A[i] = A[minIdx]\n"
        "        A[minIdx] = temp\n"
        "    end for\n"
        "    Print A\n"
        "end function</pre>"
        "What is printed after the sort completes?",
        ["[10, 13, 14, 29, 37]", "[10, 14, 13, 29, 37]", "[13, 10, 14, 29, 37]", "[29, 10, 14, 37, 13]"],
        0,
        "Each outer iteration finds the minimum of the unsorted remainder and swaps it "
        "into the next position, building up the sorted prefix 10, then 13, then 14, "
        "then 29, then 37 — the fully sorted [10, 13, 14, 29, 37]. Swapping only the "
        "first pass's minimum into place (\"[10, 14, 13, 29, 37]\") stops the trace after "
        "one iteration instead of running the outer loop to completion.",
    ),
    _q(
        "Time complexity — nested loops",
        "What is the time complexity of this pseudocode, in terms of n?"
        "<pre>function mystery(Integer n)\n"
        "    Integer count = 0\n"
        "    for i = 1 to n\n"
        "        for j = 1 to n\n"
        "            count = count + 1\n"
        "        end for\n"
        "    end for\n"
        "    return count\n"
        "end function</pre>",
        ["O(n)", "O(n log n)", "O(n^2)", "O(2^n)"],
        2,
        "Each of the n outer iterations runs a full n-iteration inner loop, giving n*n "
        "total operations — O(n^2). Calling this O(n log n) confuses it with algorithms "
        "like merge sort that combine a linear pass with a halving/doubling structure, "
        "which isn't present here since both loops are simple full-range counters.",
    ),
    _q(
        "Time complexity — recursive halving",
        "What is the time complexity of this pseudocode, in terms of n?"
        "<pre>function mystery2(Integer n)\n"
        "    if (n &lt;= 1)\n"
        "        return 0\n"
        "    end if\n"
        "    return 1 + mystery2(n / 2)\n"
        "end function</pre>",
        ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
        1,
        "Each recursive call cuts n in half, so the number of calls needed to shrink n "
        "down to 1 is proportional to log2(n) — the same halving pattern that makes "
        "binary search O(log n). Calling this O(n) would be true only if n decreased by "
        "a fixed amount (like n-1) each call, not by half.",
    ),
    _q(
        "Time complexity — exponential recursion",
        "What is the time complexity of this pseudocode, in terms of n?"
        "<pre>function countPaths(Integer n)\n"
        "    if (n &lt;= 0)\n"
        "        return 1\n"
        "    end if\n"
        "    return countPaths(n - 1) + countPaths(n - 1)\n"
        "end function</pre>",
        ["O(n)", "O(n^2)", "O(log n)", "O(2^n)"],
        3,
        "Every call (except the base case) spawns two more calls, each reducing n by "
        "only 1, so the total number of calls doubles at each of the n levels — a "
        "recursion tree with 2^n leaves, giving O(2^n). This is the same explosive "
        "growth pattern seen in naive (non-memoized) recursive Fibonacci, which is why "
        "both are considered inefficient without caching intermediate results.",
    ),
]


# ==================================================================== #
# 19. MS Office Practice — Set 1 (Word)
# ==================================================================== #
# Set 1: MS Word -- formatting shortcuts, mail merge, references (footnotes/
# endnotes/TOC/citations), page setup (breaks/sections/headers-footers),
# track changes & comments, styles, find & replace, watermark
MS_OFFICE_PRACTICE_QUESTIONS = [
    _q(
        "Word shortcuts",
        "Which keyboard shortcut applies <b>bold</b> formatting to selected text in Word?",
        ["Ctrl+I", "Ctrl+B", "Ctrl+U", "Ctrl+D"],
        1,
        "Ctrl+B toggles bold on the current selection. Ctrl+I is italic and Ctrl+U is "
        "underline -- the three are grouped together on the Home tab but each has its own "
        "distinct shortcut.",
    ),
    _q(
        "Word shortcuts",
        "Which shortcut underlines the selected text in Microsoft Word?",
        ["Ctrl+U", "Ctrl+E", "Ctrl+L", "Ctrl+Shift+U"],
        0,
        "Ctrl+U toggles underline formatting. Ctrl+E and Ctrl+L are paragraph alignment "
        "shortcuts (center and left-align), not character formatting, so they don't affect "
        "underline at all.",
    ),
    _q(
        "Mail merge",
        "A company needs to send 500 personalized letters, each addressed to a different "
        "customer using names and addresses stored in an Excel sheet. Which Word feature "
        "should they use to generate all 500 letters automatically?",
        ["Track Changes", "Mail Merge", "Format Painter", "Quick Parts"],
        1,
        "Mail Merge combines a single Word template (the main document) with a data source "
        "-- such as an Excel list -- inserting each row's fields to produce one personalized "
        "document per recipient. Track Changes only records edits and has nothing to do with "
        "generating bulk personalized documents.",
    ),
    _q(
        "Mail merge",
        "In a Word mail merge, which of the following can serve as the <b>data source</b> "
        "supplying recipient records?",
        [
            "An Excel worksheet, an Access database, or an Outlook contacts list",
            "Only a plain .txt file",
            "Only another Word document",
            "The Clipboard history pane",
        ],
        0,
        "Word's mail merge wizard accepts several data source types, most commonly an Excel "
        "spreadsheet, an Access database, or Outlook contacts, as long as the data is arranged "
        "in rows and columns with a header row. A plain text file isn't a supported structured "
        "source in the standard wizard flow.",
    ),
    _q(
        "References",
        "Which shortcut inserts a footnote at the cursor position in Word?",
        ["Alt+Ctrl+F", "Alt+Ctrl+D", "Ctrl+F", "Ctrl+Shift+F"],
        0,
        "Alt+Ctrl+F inserts a footnote reference and moves the cursor to the footnote area at "
        "the bottom of the page. Ctrl+F instead opens the Navigation pane to find text, which "
        "is unrelated to footnotes.",
    ),
    _q(
        "References",
        "Which shortcut inserts an endnote in Word, placing the note at the end of the "
        "document instead of the bottom of the page?",
        ["Alt+Ctrl+D", "Alt+Ctrl+F", "Ctrl+End", "Ctrl+Shift+E"],
        0,
        "Alt+Ctrl+D inserts an endnote, which collects at the very end of the document (or "
        "section), unlike footnotes which appear at the bottom of the current page. Ctrl+End "
        "simply moves the cursor to the end of the document and inserts nothing.",
    ),
    _q(
        "References",
        "You have applied Heading 1 and Heading 2 styles throughout a long report. What is "
        "the fastest way to generate an automatically-updatable table of contents?",
        [
            "Manually type each heading and page number at the top of the document",
            "Use References > Table of Contents, which builds the list from the heading styles",
            "Take a screenshot of the heading list and paste it in",
            "Use Find & Replace to search for the word 'Chapter'",
        ],
        1,
        "Word's Table of Contents tool scans the document for text formatted with heading "
        "styles (Heading 1, Heading 2, etc.) and builds a linked, page-numbered list that can "
        "be refreshed with 'Update Table' whenever content changes. Typing it manually defeats "
        "the purpose, since page numbers shift as the document is edited.",
    ),
    _q(
        "Page setup",
        "A report needs its first three pages in portrait orientation and the remaining "
        "pages, containing a wide table, in landscape orientation -- all within one Word file. "
        "What should be inserted between the two parts?",
        ["A simple page break", "A section break (Next Page)", "A column break", "A line break"],
        1,
        "A section break creates an independent section that can have its own orientation, "
        "margins, and headers/footers, which is required to mix portrait and landscape pages "
        "in a single document. A plain page break only starts a new page and inherits the same "
        "page setup as before it.",
    ),
    _q(
        "Page setup",
        "Which keyboard shortcut inserts a manual page break at the cursor in Word?",
        ["Ctrl+Enter", "Shift+Enter", "Ctrl+Shift+Enter", "Alt+Enter"],
        0,
        "Ctrl+Enter inserts a page break, forcing subsequent text onto a new page regardless "
        "of how much space is left. Shift+Enter instead inserts a line break within the same "
        "paragraph, without starting a new page.",
    ),
    _q(
        "Page setup",
        "To edit the header of a Word document so a company logo appears on every page, what "
        "is the quickest way to enter header-editing mode?",
        [
            "Double-click inside the top margin area of the page",
            "Press Ctrl+Alt+H",
            "Select the whole document and press Delete",
            "Open the Mailings tab",
        ],
        0,
        "Double-clicking in the top margin activates the header area for editing (and grays "
        "out the body text), which is the standard way to add content that repeats on every "
        "page. There is no default Ctrl+Alt+H shortcut for this in Word.",
    ),
    _q(
        "Track changes",
        "Which shortcut toggles Track Changes on or off in Word?",
        ["Ctrl+Shift+E", "Ctrl+T", "Ctrl+Shift+T", "Ctrl+E"],
        0,
        "Ctrl+Shift+E toggles Track Changes, which then records every insertion, deletion, and "
        "formatting change made by each editor with colored markup. Ctrl+E is unrelated -- it "
        "center-aligns the current paragraph.",
    ),
    _q(
        "Comments",
        "Which shortcut inserts a new comment on selected text in Word?",
        ["Ctrl+Alt+M", "Ctrl+Shift+M", "Ctrl+M", "Alt+C"],
        0,
        "Ctrl+Alt+M inserts a comment balloon anchored to the current selection, letting a "
        "reviewer leave feedback without altering the document text itself. Ctrl+M is a "
        "different command entirely -- it indents the current paragraph.",
    ),
    _q(
        "Formatting tools",
        "You want to copy the exact font, color, and size formatting from one paragraph and "
        "apply it to five other scattered paragraphs without repeating the action each time. "
        "How should you use the Format Painter?",
        [
            "Single-click Format Painter, which applies formatting only once",
            "Double-click Format Painter so it stays active until you press Esc",
            "Format Painter can only be used once per document, ever",
            "Right-click and choose 'Repeat Formatting' after every paragraph",
        ],
        1,
        "Double-clicking the Format Painter button keeps it 'sticky', letting you paint the "
        "same formatting onto multiple separate selections in a row; pressing Esc or clicking "
        "the button again turns it off. A single click only applies the formatting to the very "
        "next selection and then deactivates automatically.",
    ),
    _q(
        "Word shortcuts",
        "Which shortcut applies double line spacing to the selected paragraphs?",
        ["Ctrl+1", "Ctrl+2", "Ctrl+5", "Ctrl+D"],
        1,
        "Ctrl+2 sets double (2.0) line spacing. Ctrl+1 sets single spacing and Ctrl+5 sets 1.5 "
        "line spacing, following the same numeric-key pattern for quick spacing changes.",
    ),
    _q(
        "Word shortcuts",
        "Which shortcut justifies a paragraph so that both its left and right edges align "
        "evenly with the margins?",
        ["Ctrl+E", "Ctrl+L", "Ctrl+J", "Ctrl+R"],
        2,
        "Ctrl+J applies justified alignment, stretching spacing within each line so text meets "
        "both margins evenly, which is common in newspaper-style columns. Ctrl+E centers text "
        "instead and does not align both edges.",
    ),
    _q(
        "Word shortcuts",
        "Which shortcut opens the Find and Replace dialog in Word?",
        ["Ctrl+F", "Ctrl+H", "Ctrl+R", "Ctrl+G"],
        1,
        "Ctrl+H opens Find and Replace directly on the Replace tab, allowing text to be "
        "searched for and swapped in bulk. Ctrl+F opens only the Navigation pane for finding "
        "text, without a replace option.",
    ),
    _q(
        "Styles",
        "A 200-page document uses the built-in 'Normal' style for all body text. If you "
        "modify the Normal style's font to Calibri 12pt, what happens to the existing body "
        "text?",
        [
            "Nothing changes until each paragraph is reformatted manually",
            "All text using the Normal style updates automatically to the new font",
            "Only newly typed text uses the new font; existing text is unaffected",
            "The document becomes corrupted and must be reopened",
        ],
        1,
        "Word styles are dynamic definitions -- any text tagged with a given style updates "
        "instantly when that style's properties change, which is exactly why using styles "
        "(instead of manual formatting) makes large documents easy to restyle consistently.",
    ),
    _q(
        "Page setup",
        "Which tab in Word contains the option to add a diagonal 'CONFIDENTIAL' or 'DRAFT' "
        "watermark across every page?",
        ["Design", "Review", "Mailings", "View"],
        0,
        "The Design tab includes a Watermark option that overlays semi-transparent text or an "
        "image behind the page content, commonly used to mark drafts or confidential material. "
        "The Review tab instead holds proofing and collaboration tools like spell check and "
        "Track Changes.",
    ),
    _q(
        "References",
        "A student needs to insert in-text citations from various sources and later "
        "auto-generate a formatted bibliography in APA style. Which Word feature handles this?",
        [
            "The References tab's Citations & Bibliography group",
            "The Mailings tab's Start Mail Merge tool",
            "The Insert tab's WordArt gallery",
            "The Home tab's Styles gallery",
        ],
        0,
        "The Citations & Bibliography group under the References tab lets you add sources, "
        "insert matching in-text citations, choose a style like APA or MLA, and then generate "
        "a compiled Bibliography or Works Cited list automatically. WordArt is purely a "
        "decorative text-styling tool with no connection to sourcing.",
    ),
    _q(
        "Word shortcuts",
        "Which shortcut opens the 'Go To' dialog, allowing you to jump directly to a specific "
        "page, section, or bookmark in a long document?",
        ["Ctrl+G", "Ctrl+P", "Ctrl+N", "Ctrl+Home"],
        0,
        "Ctrl+G opens the Go To dialog, where you can type a page number, section, or bookmark "
        "name to jump straight there, which is much faster than scrolling through a long "
        "document. Ctrl+Home instead just jumps to the very beginning of the document.",
    ),
]


# ==================================================================== #
# 20. MS Office Practice — Set 2 (Excel)
# ==================================================================== #
# Set 2: MS Excel -- lookup and logic formulas (VLOOKUP/HLOOKUP/IF), aggregation
# formulas (SUM/SUMIF/COUNTIF), text concatenation, absolute vs relative vs mixed
# references, pivot tables, conditional formatting, sorting/filtering, charts,
# freeze panes, named ranges, data validation, and shortcuts
MS_OFFICE_PRACTICE_QUESTIONS_2 = [
    _q(
        "Excel formulas",
        "You need to look up an employee ID in column A of the current sheet and return the "
        "matching name from column B of 'Sheet2', requiring an exact match. Which formula is "
        "correct?",
        [
            "<pre>=VLOOKUP(A2,Sheet2!A:B,2,FALSE)</pre>",
            "<pre>=VLOOKUP(A2,Sheet2!A:B,1,TRUE)</pre>",
            "<pre>=HLOOKUP(A2,Sheet2!A:B,2,FALSE)</pre>",
            "<pre>=LOOKUP(A2,Sheet2!A:B)</pre>",
        ],
        0,
        "VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup]) searches the first "
        "column of the range for A2, then returns the value from the 2nd column of that range; "
        "FALSE forces an exact match. HLOOKUP would instead search across a horizontal row, "
        "which doesn't fit this column-based data.",
    ),
    _q(
        "Excel formulas",
        "A worksheet stores monthly figures across columns (Jan, Feb, Mar...) in row 1, with "
        "one row per product below. To find the value in the 'Mar' column for a given product "
        "row, which function searches a horizontal header row and returns a value from a "
        "specified row beneath it?",
        ["VLOOKUP", "HLOOKUP", "INDEX only", "COUNTIF"],
        1,
        "HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup]) searches along the "
        "top row of a range for a match and returns a value from the row you specify below it "
        "-- the horizontal counterpart to VLOOKUP. VLOOKUP instead searches down the first "
        "column, which wouldn't locate a header like 'Mar' across a row.",
    ),
    _q(
        "Excel formulas",
        "Which formula correctly displays 'Pass' if the value in B2 is 40 or above, and "
        "'Fail' otherwise?",
        [
            "<pre>=IF(B2>=40,\"Pass\",\"Fail\")</pre>",
            "<pre>=IF(B2>=40,Pass,Fail)</pre>",
            "<pre>=IF(\"Pass\",B2>=40,\"Fail\")</pre>",
            "<pre>=SUMIF(B2>=40,\"Pass\",\"Fail\")</pre>",
        ],
        0,
        "IF(logical_test, value_if_true, value_if_false) evaluates B2>=40 and returns the text "
        "in quotes for the matching branch; text results must be wrapped in quotation marks, "
        "which option B omits. SUMIF is an aggregation function for summing ranges by "
        "criteria, not for returning arbitrary text based on a condition.",
    ),
    _q(
        "Excel formulas",
        "Which formula adds up every value in the range C2 through C50?",
        [
            "<pre>=SUM(C2:C50)</pre>",
            "<pre>=SUM(C2,C50)</pre>",
            "<pre>=TOTAL(C2:C50)</pre>",
            "<pre>=ADD(C2:C50)</pre>",
        ],
        0,
        "SUM(range) adds all numeric values within the specified range; using a colon (C2:C50) "
        "defines a continuous block of cells. SUM(C2,C50) would instead add only the two "
        "individual cells C2 and C50, ignoring everything in between.",
    ),
    _q(
        "Excel formulas",
        "You want to total only the sales amounts in column C where the region in column B is "
        "'North'. Which formula does this correctly?",
        [
            "<pre>=SUMIF(B:B,\"North\",C:C)</pre>",
            "<pre>=SUMIF(C:C,\"North\",B:B)</pre>",
            "<pre>=COUNTIF(B:B,\"North\")</pre>",
            "<pre>=SUM(B:B,\"North\",C:C)</pre>",
        ],
        0,
        "SUMIF(range, criteria, sum_range) checks the criteria against the first range (B:B "
        "for 'North') and sums the corresponding cells in sum_range (C:C). COUNTIF would only "
        "count how many cells in B:B say 'North', without adding any sales figures at all.",
    ),
    _q(
        "Excel formulas",
        "Which formula returns the number of cells in range A2:A200 that contain the text "
        "'Completed'?",
        [
            "<pre>=COUNTIF(A2:A200,\"Completed\")</pre>",
            "<pre>=SUMIF(A2:A200,\"Completed\")</pre>",
            "<pre>=COUNT(A2:A200,\"Completed\")</pre>",
            "<pre>=IF(A2:A200,\"Completed\")</pre>",
        ],
        0,
        "COUNTIF(range, criteria) counts how many cells in the range match the given criteria, "
        "here tallying every cell that reads 'Completed'. SUMIF requires a sum_range and is "
        "meant for adding numbers, not counting text matches, and used this way would error.",
    ),
    _q(
        "Excel formulas",
        "Which formula joins the first name in A2 and last name in B2 into one cell as "
        "'John Smith', with a space between them?",
        [
            "<pre>=CONCAT(A2,\" \",B2)</pre>",
            "<pre>=SUM(A2,B2)</pre>",
            "<pre>=CONCAT(A2,B2)</pre>",
            "<pre>=VLOOKUP(A2,B2)</pre>",
        ],
        0,
        "CONCAT(A2,\" \",B2) (or equivalently =A2&\" \"&B2) joins the text values with an "
        "explicit space in between so the names don't run together. Leaving out the space "
        "argument, as in option C, would produce 'JohnSmith' with no separator.",
    ),
    _q(
        "Excel references",
        "You write a formula in cell C2 referencing a tax rate stored in E1, then drag/copy "
        "the formula down to C3, C4, and so on. If E1 must stay fixed for every copied row, "
        "how should E1 be written in the formula?",
        ["E1", "$E1", "E$1", "$E$1"],
        3,
        "$E$1 is an absolute reference: locking both the column and row with dollar signs "
        "means it stays pointed at E1 no matter where the formula is copied. A plain E1 is a "
        "relative reference that would shift to E2, E3, and so on as you copy it downward.",
    ),
    _q(
        "Excel references",
        "In a formula, the reference <pre>$A1</pre> is copied one column to the right and one "
        "row down. What happens to it?",
        [
            "It stays exactly $A1 in both position and value",
            "The column stays locked at A, but the row updates to 2, giving $A2",
            "The row stays locked at 1, but the column updates to B, giving $B1",
            "Both column and row update, giving B2",
        ],
        1,
        "$A1 is a mixed reference: the dollar sign before 'A' locks the column so it never "
        "changes, while the row number (no dollar sign) is relative and shifts normally when "
        "copied downward, becoming $A2. A$1 would instead lock the row while letting the "
        "column shift.",
    ),
    _q(
        "Pivot tables",
        "A sales dataset has 50,000 rows with columns for Region, Product, Salesperson, and "
        "Amount. You need a quick summary of total sales by Region and Product without writing "
        "any formulas. What feature is best suited for this?",
        ["Conditional Formatting", "PivotTable", "Data Validation", "Freeze Panes"],
        1,
        "A PivotTable lets you drag Region and Product into Rows/Columns and Amount into "
        "Values to instantly aggregate and summarize large datasets, without writing SUMIF "
        "formulas manually. Conditional Formatting only changes cell appearance based on "
        "rules -- it doesn't aggregate or restructure data.",
    ),
    _q(
        "Conditional formatting",
        "You want every cell in a sales column that exceeds 100000 to automatically turn "
        "green. Which feature should you apply?",
        [
            "Data Validation with a custom formula",
            "Conditional Formatting > Highlight Cell Rules > Greater Than",
            "Sort & Filter > Custom Sort",
            "Freeze Panes",
        ],
        1,
        "Conditional Formatting's 'Greater Than' rule automatically applies formatting, such "
        "as a green fill, to any cell whose value exceeds a threshold you set, and updates live "
        "as data changes. Data Validation instead restricts what can be typed into a cell -- it "
        "doesn't change a cell's appearance based on its value.",
    ),
    _q(
        "Sorting and filtering",
        "After enabling filter dropdown arrows on a table's header row, what is this Excel "
        "feature called?",
        ["PivotTable", "AutoFilter", "Freeze Panes", "Data Validation"],
        1,
        "AutoFilter adds dropdown arrows to each header cell, letting users show only rows "
        "matching chosen criteria per column, and is turned on via Data > Filter. Freeze Panes "
        "is unrelated -- it only keeps rows or columns visible while scrolling, without "
        "filtering any data.",
    ),
    _q(
        "Charts",
        "You want to visualize how a company's monthly revenue has changed over the past two "
        "years. Which chart type best shows this trend over time?",
        ["Pie chart", "Line chart", "Doughnut chart", "Radar chart"],
        1,
        "A line chart plots data points across a continuous axis like time, making it the "
        "standard choice for showing trends and changes over months or years. A pie chart "
        "instead shows how parts contribute to a single whole at one point in time, not change "
        "over a period.",
    ),
    _q(
        "Charts",
        "You want to show what percentage of total quarterly expenses each department "
        "(Marketing, IT, HR, Sales) accounts for. Which chart type is most appropriate?",
        ["Line chart", "Scatter chart", "Pie chart", "Stock chart"],
        2,
        "A pie chart is designed to show how individual categories contribute proportionally "
        "to one whole, which fits comparing each department's share of total expenses. A line "
        "chart is built for trends across a continuous axis like time, not for a single "
        "point-in-time proportional breakdown.",
    ),
    _q(
        "Excel shortcuts",
        "Which shortcut inserts the current date as a static value into the selected cell?",
        ["Ctrl+;", "Ctrl+Shift+;", "Ctrl+D", "Ctrl+T"],
        0,
        "Ctrl+; inserts today's date as a fixed, unchanging value at the moment it's pressed. "
        "Ctrl+Shift+; is the related shortcut for inserting the current time instead, not the "
        "date.",
    ),
    _q(
        "Excel shortcuts",
        "While typing a formula and editing a cell reference, pressing which key cycles the "
        "reference through relative, absolute, and mixed forms (e.g., A1 -> $A$1 -> A$1 -> "
        "$A1)?",
        ["F2", "F4", "F9", "F5"],
        1,
        "F4 cycles the reference style of the selected reference in a formula, saving you from "
        "manually typing dollar signs each time. F2 instead simply enters edit mode for the "
        "active cell and has no effect on reference locking.",
    ),
    _q(
        "Excel views",
        "A worksheet has 10,000 rows with column headers in row 1. You want the header row to "
        "stay visible at the top no matter how far down you scroll. Which feature should you "
        "use?",
        ["Freeze Panes", "Split Window only", "Group and Outline", "Page Break Preview"],
        0,
        "View > Freeze Panes > Freeze Top Row locks row 1 in place so it remains visible while "
        "the rest of the sheet scrolls beneath it. Page Break Preview instead only shows where "
        "pages will split when printing and has nothing to do with keeping headers visible "
        "on-screen.",
    ),
    _q(
        "Named ranges",
        "Instead of writing <pre>=SUM(B2:B50)</pre> repeatedly across many formulas, you "
        "assign the range B2:B50 the name 'SalesData' via Formulas > Define Name. What is the "
        "main benefit of doing this?",
        [
            "It automatically sorts the range alphabetically",
            "Formulas become easier to read and maintain by referencing 'SalesData' instead "
            "of a raw cell range",
            "It converts the range into a PivotTable",
            "It prevents the values in the range from ever being edited",
        ],
        1,
        "A named range lets formulas reference a meaningful label like SalesData instead of a "
        "raw address, making formulas such as =SUM(SalesData) more readable and easier to "
        "reuse if the range needs to move. It does not sort data or lock cells from editing -- "
        "those are separate features (Sort and Protect Sheet, respectively).",
    ),
    _q(
        "Data validation",
        "You want a cell to only accept one of three values -- 'Low', 'Medium', or 'High' -- "
        "offered to the user as a dropdown. Which Excel feature enforces this?",
        [
            "Data Validation with a List source",
            "Conditional Formatting",
            "Freeze Panes",
            "Goal Seek",
        ],
        0,
        "Data > Data Validation, with 'List' as the allowed criteria, restricts entry to the "
        "specified values and shows them as a dropdown arrow in the cell. Conditional "
        "Formatting only changes how a cell looks based on its content -- it cannot restrict "
        "what a user is allowed to type in.",
    ),
    _q(
        "Excel shortcuts",
        "Which shortcut toggles the AutoFilter dropdown arrows on and off for the currently "
        "selected data range?",
        ["Ctrl+Shift+L", "Ctrl+L", "Ctrl+Shift+F", "Ctrl+F3"],
        0,
        "Ctrl+Shift+L applies or removes AutoFilter dropdown arrows on the header row of the "
        "selected range in one keystroke. Ctrl+F3 instead opens the Name Manager for creating "
        "and editing named ranges, which is unrelated to filtering.",
    ),
]


# ==================================================================== #
# 21. MS Office Practice — Set 3 (PowerPoint/Outlook)
# ==================================================================== #
# Set 3: MS PowerPoint (slide master, transitions vs animations, presenter view,
# slide sorter) plus general Office/Outlook (To/CC/BCC, rules, calendar invites,
# file formats, PDF export, OneDrive co-authoring & sharing permissions,
# AutoSave) and common cross-app shortcuts
MS_OFFICE_PRACTICE_QUESTIONS_3 = [
    _q(
        "PowerPoint design",
        "You need every slide in a 40-slide deck to show the company logo in the same corner "
        "and use the same title font, and you want to update this look in one place rather "
        "than editing each slide individually. Which feature should you edit?",
        ["Slide Sorter view", "Slide Master", "Presenter View", "Notes Page view"],
        1,
        "The Slide Master (View > Slide Master) defines the shared layout, placeholders, and "
        "formatting inherited by every slide using it, so one edit there propagates across the "
        "whole deck. Slide Sorter is just a view for rearranging slide order and doesn't hold "
        "any shared design elements.",
    ),
    _q(
        "PowerPoint effects",
        "In PowerPoint, what is the key difference between a 'Transition' and an 'Animation'?",
        [
            "Transitions and animations are two names for the exact same feature",
            "A transition is the effect that plays when moving between two slides; an "
            "animation is the effect applied to an individual object within a single slide",
            "Animations only work on text, while transitions only work on images",
            "Transitions require PowerPoint Designer; animations do not",
        ],
        1,
        "Transitions (Transitions tab) control how the presentation moves from one whole slide "
        "to the next, such as a fade or wipe, while animations (Animations tab) control how "
        "individual elements -- like a bullet point or picture -- enter, emphasize, or exit "
        "within a single slide. They're configured on separate ribbon tabs because they target "
        "different scopes.",
    ),
    _q(
        "PowerPoint delivery",
        "During a live presentation with a projector connected, a presenter wants to see "
        "speaker notes, a timer, and a preview of the next slide on their laptop screen, while "
        "the audience on the projector sees only the current slide in full screen. Which "
        "feature provides this?",
        ["Presenter View", "Reading View", "Outline View", "Slide Sorter View"],
        0,
        "Presenter View splits the display so the presenter's screen shows notes, elapsed "
        "time, and the upcoming slide, while the audience-facing screen shows only the current "
        "slide at full screen. Reading View instead shows the same single slide-at-a-time "
        "experience on one screen, with no separate presenter-only information.",
    ),
    _q(
        "PowerPoint shortcuts",
        "Which shortcut starts the slide show beginning from the very first slide, regardless "
        "of which slide is currently selected in the editor?",
        ["F5", "Shift+F5", "Ctrl+F5", "Alt+F5"],
        0,
        "F5 always starts the slide show from Slide 1. Shift+F5 instead starts the slide show "
        "from whichever slide is currently active in the editor, which is useful when "
        "resuming a rehearsal partway through.",
    ),
    _q(
        "Outlook basics",
        "When composing an email, you add three colleagues to CC. What does putting them in "
        "CC (rather than To) signal, and how does BCC differ from both?",
        [
            "CC recipients are copied for information/visibility while remaining visible to "
            "everyone; BCC recipients are hidden from all other recipients",
            "CC and BCC are functionally identical; both hide the recipient",
            "CC recipients must reply; BCC recipients are automatically deleted from the "
            "thread",
            "CC is only used for internal company addresses, BCC for external ones",
        ],
        0,
        "To lists the primary intended recipients, CC (carbon copy) adds people for visibility "
        "whose addresses everyone else can see, and BCC (blind carbon copy) also sends a copy "
        "but hides that recipient's address from everyone else on the email. Reply behavior "
        "and address type have nothing to do with the distinction -- it's purely about who is "
        "visible to whom.",
    ),
    _q(
        "Outlook automation",
        "Every week you receive dozens of newsletter emails and want them automatically moved "
        "into a 'Newsletters' folder as soon as they arrive, without manual sorting. Which "
        "Outlook feature accomplishes this?",
        ["Rules", "Quick Steps only", "Categories", "Focused Inbox"],
        0,
        "Outlook Rules (File > Manage Rules & Alerts) let you define conditions, such as "
        "sender or subject keywords, and automatically apply an action like moving the message "
        "to a specific folder as it arrives. Categories only apply a colored label for "
        "organization -- they don't move or filter incoming mail automatically.",
    ),
    _q(
        "Outlook calendar",
        "You're scheduling a meeting with five colleagues and want to see each person's free "
        "and busy time slots before picking a time. Which Outlook calendar feature shows this?",
        ["Scheduling Assistant", "Automatic Replies", "Quick Parts", "Focused Inbox"],
        0,
        "The Scheduling Assistant, available when creating a meeting invite, overlays each "
        "invitee's free/busy availability so you can pick a time that works for everyone. "
        "Automatic Replies is an unrelated feature that sends an out-of-office response to "
        "incoming emails.",
    ),
    _q(
        "File formats",
        "What is the default, XML-based file format for PowerPoint presentations since "
        "PowerPoint 2007, replacing the older binary .ppt format?",
        [".pptx", ".ppsx", ".potx", ".pdf"],
        0,
        ".pptx is the modern default format, built on an open XML structure that produces "
        "smaller, more robust files than the legacy binary .ppt format. .potx is instead used "
        "specifically for PowerPoint template files, not standard presentations.",
    ),
    _q(
        "File formats",
        "You've finished a Word report and need to send a version that recipients can view "
        "and print with guaranteed identical formatting on any device, but cannot easily edit. "
        "What should you do?",
        [
            "Save a copy as .docx and rename the file extension to .pdf manually",
            "Use File > Export (or Save As) and choose PDF",
            "Email the .docx file as-is; formatting is always identical everywhere",
            "Print the document and scan it back in",
        ],
        1,
        "File > Export > Create PDF/XPS Document (or Save As with PDF selected) converts the "
        "document into a fixed-layout PDF that renders identically everywhere and isn't easily "
        "editable. Simply renaming a .docx file's extension to .pdf does not actually convert "
        "the file format and produces a broken file.",
    ),
    _q(
        "OneDrive and sharing",
        "Two colleagues open the same Word document stored on OneDrive at the same time and "
        "both start typing. What happens?",
        [
            "The second person to open it is locked out entirely",
            "Real-time co-authoring lets both edit simultaneously, with each other's changes "
            "syncing live",
            "Excel supports this but Word does not",
            "The file automatically splits into two separate copies",
        ],
        1,
        "Files stored on OneDrive or SharePoint support real-time co-authoring, so multiple "
        "people can edit the same document simultaneously and see each other's changes appear "
        "live, with a name tag showing who is editing which part. Co-authoring works across "
        "Word, Excel, and PowerPoint alike, not just one app.",
    ),
    _q(
        "Cross-app shortcuts",
        "Which shortcut key, used consistently across Word, Excel, and PowerPoint, opens the "
        "Print dialog/pane?",
        ["Ctrl+P", "Ctrl+O", "Ctrl+W", "Ctrl+F2"],
        0,
        "Ctrl+P opens the Print backstage view in every major Office application, showing "
        "print settings and a preview. Ctrl+O instead opens the Open dialog for loading an "
        "existing file, which is unrelated to printing.",
    ),
    _q(
        "Cross-app shortcuts",
        "Which function key opens the 'Save As' dialog across Word, Excel, and PowerPoint?",
        ["F2", "F5", "F12", "F9"],
        2,
        "F12 opens Save As, letting you choose a new file name, location, or format for the "
        "current document. F5 instead starts a slide show in PowerPoint or opens Go To in "
        "Word/Excel -- it has no Save As function.",
    ),
    _q(
        "Cross-app shortcuts",
        "Which shortcut creates a new blank file in Word, Excel, or PowerPoint?",
        ["Ctrl+N", "Ctrl+O", "Ctrl+S", "Ctrl+F"],
        0,
        "Ctrl+N opens a new blank document, workbook, or presentation depending on the active "
        "application. Ctrl+S instead saves the current file and does not create a new one.",
    ),
    _q(
        "PowerPoint views",
        "Which PowerPoint view displays small thumbnails of every slide in a grid, making it "
        "easy to drag slides into a new order or delete several at once?",
        ["Normal view", "Slide Sorter view", "Notes Page view", "Outline view"],
        1,
        "Slide Sorter view lays out all slides as thumbnails in a grid, which is ideal for "
        "reordering, duplicating, or deleting slides in bulk by dragging them around. Notes "
        "Page view instead shows one slide at a time along with its speaker notes beneath it, "
        "meant for reviewing or printing notes rather than reordering.",
    ),
    _q(
        "Outlook automation",
        "You're going on vacation for a week and want anyone who emails you to receive an "
        "instant reply saying you're away and when you'll return. Which Outlook feature "
        "should you configure?",
        ["Automatic Replies (Out of Office)", "Rules only", "Delay Delivery", "Categories"],
        0,
        "Automatic Replies (File > Automatic Replies), often called Out of Office, "
        "automatically sends a preset message to anyone who emails you while it's enabled. "
        "Delay Delivery instead only postpones when your own outgoing messages are sent -- it "
        "does not reply to incoming mail.",
    ),
    _q(
        "Cross-app shortcuts",
        "After making several edits, you decide to undo the last two changes and then redo "
        "one of them. Which shortcuts accomplish this in any Office app?",
        [
            "Ctrl+Z to undo, Ctrl+Y (or F4) to redo",
            "Ctrl+X to undo, Ctrl+V to redo",
            "Alt+Z to undo, Alt+Y to redo",
            "Ctrl+Backspace to undo, Ctrl+Delete to redo",
        ],
        0,
        "Ctrl+Z steps backward through the undo history, and Ctrl+Y (with F4 as an "
        "alternative in many Office apps) reapplies the most recently undone action. Ctrl+X "
        "and Ctrl+V are Cut and Paste -- clipboard operations that have nothing to do with "
        "undo history.",
    ),
    _q(
        "PowerPoint views",
        "A presenter wants a printed handout showing each slide alongside the detailed "
        "speaker notes written for it. Which view should be used to review and format this "
        "before printing?",
        ["Notes Page view", "Reading View", "Slide Sorter view", "Slide Master view"],
        0,
        "Notes Page view shows a smaller image of the slide with the full speaker notes typed "
        "beneath it, formatted specifically for printing reference pages. Slide Sorter view "
        "shows only slide thumbnails in a grid with no notes text visible at all.",
    ),
    _q(
        "OneDrive and sharing",
        "When sharing a file link stored on OneDrive, you can choose whether the recipient "
        "gets 'Can edit' or 'Can view' permission. What is the practical difference?",
        [
            "'Can edit' allows changing the file's content; 'Can view' only allows opening "
            "and reading it, not modifying it",
            "'Can view' allows editing but not downloading",
            "There is no difference; both permissions are identical",
            "'Can edit' expires after 24 hours automatically while 'Can view' does not",
        ],
        0,
        "'Can edit' (Editor) permission lets the recipient modify the actual file content, "
        "while 'Can view' (Viewer) restricts them to opening and reading it without being able "
        "to save changes back to the shared file. Both permission levels are available "
        "indefinitely unless an expiration is explicitly set -- that isn't a default "
        "distinction between the two.",
    ),
    _q(
        "OneDrive and sharing",
        "A file is saved directly to a OneDrive folder on your PC. As you keep typing, you "
        "notice you never need to press Ctrl+S because the document title bar simply shows "
        "the file is already saved. Which feature is responsible?",
        ["AutoSave", "Track Changes", "AutoCorrect", "AutoFormat"],
        0,
        "AutoSave automatically and continuously saves changes to files stored on OneDrive or "
        "SharePoint, removing the need to manually press Ctrl+S. AutoCorrect is unrelated -- it "
        "only fixes typos and common spelling mistakes as you type, not saving behavior.",
    ),
    _q(
        "PowerPoint shortcuts",
        "While editing a presentation in Normal view, which shortcut inserts a new blank "
        "slide right after the current one?",
        ["Ctrl+M", "Ctrl+N", "Ctrl+Shift+M", "Ctrl+Enter"],
        0,
        "Ctrl+M inserts a new slide immediately after the currently selected slide, using a "
        "layout similar to the one before it. Ctrl+N instead opens an entirely new, separate "
        "presentation file rather than adding a slide to the current one.",
    ),
]


# ==================================================================== #
# 22. OOPs Practice — Set 1
# ==================================================================== #
# Set 1: The four pillars of OOP -- encapsulation, abstraction, inheritance,
# polymorphism -- covering definitions, compile-time vs runtime polymorphism,
# data hiding, and scenario-based "identify the pillar" questions.
OOPS_PRACTICE_QUESTIONS = [
    _q(
        "Encapsulation",
        "Which of the following best defines encapsulation in object-oriented programming?",
        [
            "Acquiring properties and behavior from another class",
            "Bundling data and the methods that operate on it into a single unit, while "
            "restricting direct access to that data",
            "Hiding unnecessary implementation details and exposing only essential features",
            "Allowing an object to take many forms depending on context",
        ],
        1,
        "Encapsulation binds an object's data and the methods that act on it together, and "
        "restricts direct outside access to that data (usually via private fields with public "
        "getters/setters). Option A describes inheritance and option D describes polymorphism, "
        "not encapsulation.",
    ),
    _q(
        "Abstraction",
        "What is the primary goal of abstraction in OOP?",
        [
            "To hide implementation details and show only essential features to the user",
            "To combine data and methods into one class",
            "To let a subclass reuse a superclass's code",
            "To allow a single method name to behave differently",
        ],
        0,
        "Abstraction focuses on 'what' an object does rather than 'how' it does it, exposing a "
        "simplified interface while hiding internal complexity. Combining data and methods "
        "(option B) describes encapsulation, a related but distinct concept.",
    ),
    _q(
        "Inheritance",
        "Inheritance in OOP primarily models which kind of relationship between two classes?",
        ["HAS-A", "IS-A", "USES-A", "CONTAINS-A"],
        1,
        "Inheritance creates an IS-A relationship -- a Car IS-A Vehicle, a Dog IS-A Animal -- "
        "where the child class extends and specializes the parent class. HAS-A relationships "
        "(option A) are instead modeled through composition.",
    ),
    _q(
        "Polymorphism",
        "Polymorphism in OOP refers to the ability of...",
        [
            "a class to hide its internal data from other classes",
            "an object or method to take on many forms depending on the context it is used in",
            "a subclass to inherit fields from its parent class",
            "a program to allocate memory automatically at runtime",
        ],
        1,
        "Polymorphism (literally 'many forms') lets the same method name or object behave "
        "differently depending on the object's actual type or the arguments supplied. Option A "
        "describes encapsulation and option C describes inheritance.",
    ),
    _q(
        "Compile-time polymorphism",
        "Method overloading, where multiple methods share a name but differ in parameter list, "
        "is an example of which type of polymorphism?",
        [
            "Runtime polymorphism",
            "Compile-time (static) polymorphism",
            "Dynamic binding",
            "Late binding",
        ],
        1,
        "Overloading is resolved by the compiler at compile time based on the method signature "
        "(number, type, or order of parameters), so it is called compile-time or static "
        "polymorphism. Runtime/dynamic/late binding (options A, C, D) all refer instead to "
        "overriding, which is resolved when the program actually runs.",
    ),
    _q(
        "Runtime polymorphism",
        "Method overriding, where a subclass redefines a method inherited from its superclass "
        "with the same signature, is an example of which type of polymorphism?",
        [
            "Compile-time polymorphism",
            "Static polymorphism",
            "Runtime (dynamic) polymorphism",
            "Ad-hoc polymorphism",
        ],
        2,
        "Overriding is resolved at runtime through dynamic method dispatch -- the runtime looks "
        "at the actual object type, not the reference type, to decide which method body to "
        "execute. This is why it's called runtime or dynamic polymorphism, unlike overloading "
        "which is settled at compile time.",
    ),
    _q(
        "Encapsulation",
        "<pre>class BankAccount {\n"
        "  private double balance;\n"
        "  public void deposit(double amt) { balance += amt; }\n"
        "  public double getBalance() { return balance; }\n"
        "}</pre> The <code>balance</code> field is marked <b>private</b> and can only be "
        "changed through <code>deposit()</code>, never accessed directly from outside the "
        "class. Which OOP pillar is being demonstrated?",
        ["Encapsulation", "Abstraction", "Inheritance", "Polymorphism"],
        0,
        "The balance field is hidden (private) and only reachable through controlled public "
        "methods -- this is data hiding, the hallmark of encapsulation. It is not abstraction, "
        "which would instead hide *how* deposit() computes the new balance rather than "
        "restricting access to the field itself.",
    ),
    _q(
        "Abstraction",
        "<pre>abstract class Shape {\n"
        "  abstract double area();\n"
        "}\n"
        "class Circle extends Shape {\n"
        "  double radius;\n"
        "  double area() { return 3.14 * radius * radius; }\n"
        "}</pre> Client code only ever calls <code>shape.area()</code> without knowing how "
        "each shape calculates its area internally. This is an example of:",
        ["Encapsulation", "Abstraction", "Multiple inheritance", "Operator overloading"],
        1,
        "Abstraction lets client code depend only on the essential contract (an area() method "
        "exists) while the messy calculation details stay hidden inside each subclass. "
        "Encapsulation is a related but different idea -- it's about restricting access to an "
        "object's internal data, not about hiding an algorithm's implementation.",
    ),
    _q(
        "Inheritance",
        "<pre>class Vehicle {\n"
        "  void start() { System.out.println(\"Engine started\"); }\n"
        "}\n"
        "class Car extends Vehicle {\n"
        "  void openSunroof() { System.out.println(\"Sunroof open\"); }\n"
        "}</pre> <code>Car</code> automatically gets the <code>start()</code> method without "
        "rewriting it. Which OOP pillar enables this code reuse?",
        ["Polymorphism", "Encapsulation", "Inheritance", "Abstraction"],
        2,
        "Inheritance lets Car acquire Vehicle's members automatically, avoiding duplicate code "
        "for shared behavior. Polymorphism would instead be relevant if Car changed how "
        "start() behaves via overriding, which isn't happening here.",
    ),
    _q(
        "Polymorphism",
        "<pre>Shape s = new Circle();\n"
        "s.area();  // calls Circle's area(), even though s is declared as Shape</pre> The "
        "method that actually executes is chosen based on the object's real type at runtime, "
        "not its declared reference type. This behavior is called:",
        [
            "Static binding",
            "Dynamic method dispatch (runtime polymorphism)",
            "Constructor chaining",
            "Data hiding",
        ],
        1,
        "Because the actual object (Circle) determines which overridden method runs, not the "
        "reference type (Shape), this is dynamic method dispatch -- the mechanism behind "
        "runtime polymorphism. Static binding (option A) is the opposite: it resolves the call "
        "at compile time, as happens with overloaded or non-virtual methods.",
    ),
    _q(
        "Encapsulation",
        "'Data hiding' in OOP is most closely associated with which access practice?",
        [
            "Making all fields public so any class can modify them directly",
            "Declaring fields private and exposing controlled access through public "
            "getter/setter methods",
            "Declaring every method as static",
            "Using multiple constructors in a class",
        ],
        1,
        "Data hiding restricts a class's internal state from being changed arbitrarily by "
        "outside code -- typically achieved by marking fields private and providing public "
        "accessor methods that can validate or control changes. Making fields public (option "
        "A) does the opposite of hiding data.",
    ),
    _q(
        "Abstraction",
        "Which two language constructs are the primary tools used to achieve abstraction in "
        "most OOP languages?",
        [
            "Constructors and destructors",
            "Abstract classes and interfaces",
            "Static variables and static methods",
            "Loops and conditionals",
        ],
        1,
        "Abstract classes and interfaces let you declare a method's contract (its name and "
        "signature) without committing to an implementation, forcing subclasses to supply the "
        "details while callers only rely on the contract. Constructors and destructors (option "
        "A) manage object creation/cleanup, not abstraction.",
    ),
    _q(
        "Encapsulation",
        "What is the main purpose of providing getter and setter methods for a private field?",
        [
            "To make the field accessible and modifiable in a controlled, validated way from "
            "outside the class",
            "To convert the field into a static member",
            "To allow the field to be inherited by unrelated classes",
            "To enable operator overloading on the field",
        ],
        0,
        "Getters and setters give outside code a controlled doorway to read or update a "
        "private field, letting the class enforce validation rules (e.g., rejecting a negative "
        "balance) that direct field access would bypass. This is a standard technique for "
        "implementing encapsulation.",
    ),
    _q(
        "Inheritance",
        "The main motivation for using inheritance instead of writing each class from scratch "
        "is:",
        [
            "It hides an object's internal state from other objects",
            "It allows a single method to behave differently for different inputs",
            "It enables code reuse by letting a new class acquire the fields and methods of an "
            "existing class",
            "It converts compile-time errors into runtime errors",
        ],
        2,
        "Inheritance lets a derived class reuse and extend an existing class's code instead of "
        "duplicating it, and then add or override only what's different. Option A describes "
        "encapsulation and option B describes polymorphism.",
    ),
    _q(
        "Compile-time polymorphism",
        "<pre>class Calculator {\n"
        "  int add(int a, int b) { return a + b; }\n"
        "  double add(double a, double b) { return a + b; }\n"
        "  int add(int a, int b, int c) { return a + b + c; }\n"
        "}</pre> The three <code>add</code> methods above are an example of:",
        [
            "Method overriding",
            "Method overloading",
            "Constructor chaining",
            "Runtime polymorphism",
        ],
        1,
        "All three methods share the name add but differ in the number or type of parameters, "
        "which is precisely method overloading -- a compile-time polymorphism technique. "
        "Overriding (option A) would require these methods to appear in a subclass with an "
        "identical signature to a superclass method.",
    ),
    _q(
        "Runtime polymorphism",
        "<pre>class Animal {\n"
        "  void sound() { System.out.println(\"Some sound\"); }\n"
        "}\n"
        "class Dog extends Animal {\n"
        "  void sound() { System.out.println(\"Bark\"); }\n"
        "}</pre> <code>Dog</code> redefining <code>sound()</code> with the exact same "
        "signature as <code>Animal</code>'s version is an example of:",
        [
            "Method overloading",
            "Constructor overloading",
            "Method overriding",
            "Encapsulation",
        ],
        2,
        "Dog supplies its own implementation of a method it inherited, keeping the same name "
        "and signature as the parent's version -- this is method overriding, which enables "
        "runtime polymorphism. It is not overloading, since overloading requires different "
        "signatures within the same scope.",
    ),
    _q(
        "Encapsulation",
        "Which real-world analogy best illustrates encapsulation?",
        [
            "A medicine capsule that bundles multiple ingredients inside a shell, hiding them "
            "from direct handling",
            "A driver operating a car without knowing how the engine's internal combustion "
            "works",
            "A child inheriting eye color from a parent",
            "A universal remote that can control a TV, AC, or music system depending on which "
            "mode is selected",
        ],
        0,
        "A capsule packages ingredients together and shields them behind an outer shell, "
        "mirroring how encapsulation bundles data with methods and hides it behind a "
        "controlled interface. Option B is the classic analogy for abstraction, and option D "
        "describes polymorphism.",
    ),
    _q(
        "Abstraction",
        "Which real-world analogy best illustrates abstraction?",
        [
            "A bank locker that only the owner can open with a key",
            "A driver pressing the accelerator to speed up a car without needing to know how "
            "fuel injection works internally",
            "A son inheriting his father's surname",
            "Filling out the same form differently depending on whether you are a student or "
            "an employee",
        ],
        1,
        "The driver interacts only with a simple interface (the pedal) while the complex "
        "mechanics stay hidden -- exactly what abstraction does by exposing essential "
        "operations and hiding implementation detail. Option A is a better fit for "
        "encapsulation/access control, not abstraction.",
    ),
    _q(
        "Abstraction vs encapsulation",
        "How does abstraction differ from encapsulation?",
        [
            "They are two names for the exact same concept with no practical difference",
            "Abstraction hides implementation complexity and shows only essential behavior, "
            "while encapsulation hides an object's internal data and bundles it with the "
            "methods that operate on it",
            "Abstraction is only possible in interfaces, while encapsulation is only possible "
            "in abstract classes",
            "Abstraction applies to variables, while encapsulation applies only to methods",
        ],
        1,
        "Abstraction is a design-level idea about hiding *how* something works and exposing "
        "only *what* it does, whereas encapsulation is an implementation-level technique for "
        "protecting an object's data using access modifiers. They're related -- both hide "
        "detail -- but they operate at different levels and are commonly tested as a pair in "
        "interviews.",
    ),
    _q(
        "Compile-time polymorphism",
        "When a class has multiple overloaded versions of a method, how does the compiler "
        "decide which version to call at compile time?",
        [
            "By checking which version was written first in the source file",
            "By matching the number, type, and order of arguments in the call against each "
            "method's parameter list",
            "By picking the version with the shortest method body",
            "Overload resolution always happens at runtime, not compile time",
        ],
        1,
        "The compiler compares the arguments in the call site against each overloaded method's "
        "signature (parameter count, types, and order) to find the best match, and binds the "
        "call at compile time. This is exactly why overloading is classified as compile-time/"
        "static polymorphism, unlike overriding which is resolved at runtime (making option D "
        "incorrect).",
    ),
]


# ==================================================================== #
# 23. OOPs Practice — Set 2
# ==================================================================== #
# Set 2: Class mechanics -- constructors (default/parameterized/copy), overloading
# vs overriding, access modifiers (public/private/protected/default), static vs
# instance members, this/super keywords, and constructor chaining.
OOPS_PRACTICE_QUESTIONS_2 = [
    _q(
        "Constructors",
        "What is a default constructor?",
        [
            "A constructor that accepts one or more parameters to initialize fields",
            "A no-argument constructor, either written explicitly or automatically supplied by "
            "the compiler when no constructor is defined",
            "A constructor used only to copy another object's data",
            "A static method that creates objects without using the `new` keyword",
        ],
        1,
        "If a class defines no constructor at all, the compiler automatically inserts a public "
        "no-argument default constructor that initializes fields to their default values. Once "
        "you write any constructor of your own, though, this automatic default constructor is "
        "no longer generated.",
    ),
    _q(
        "Constructors",
        "<pre>class Point {\n"
        "  int x, y;\n"
        "  Point(int x, int y) {\n"
        "    this.x = x;\n"
        "    this.y = y;\n"
        "  }\n"
        "}</pre> The constructor shown above, which takes arguments to set initial field "
        "values, is called a:",
        ["Default constructor", "Copy constructor", "Parameterized constructor", "Static constructor"],
        2,
        "A parameterized constructor accepts arguments so the caller can supply custom initial "
        "values for an object's fields at creation time, as Point(x, y) does here. Once such a "
        "constructor is defined, the compiler no longer auto-generates a no-argument default "
        "constructor unless one is written explicitly.",
    ),
    _q(
        "Constructors",
        "A copy constructor is a constructor that:",
        [
            "Creates a new object by copying the field values of an existing object of the "
            "same class",
            "Automatically deletes an object once it goes out of scope",
            "Can only be called once per program execution",
            "Converts an object of one class into an object of an unrelated class",
        ],
        0,
        "A copy constructor takes another object of the same class as an argument and "
        "initializes the new object's fields from it -- commonly written explicitly in C++ "
        "(e.g., Point(const Point &p)). Care is needed with fields that are references or "
        "pointers, since a naive copy constructor produces a shallow copy rather than a deep "
        "copy.",
    ),
    _q(
        "Overloading",
        "Which statement correctly describes method overloading?",
        [
            "Defining multiple methods in the same class with the same name but different "
            "parameter lists",
            "Redefining a superclass method in a subclass with an identical signature",
            "Declaring a method as `final` so it cannot be changed",
            "Hiding a superclass's static method by declaring one with the same name in a "
            "subclass",
        ],
        0,
        "Overloading means giving several methods (or constructors) the same name within the "
        "same class as long as their parameter lists differ in number, type, or order. Option "
        "B describes overriding, a completely different mechanism that requires an inheritance "
        "relationship.",
    ),
    _q(
        "Overriding",
        "Which of the following is a strict requirement for a subclass method to override a "
        "superclass method?",
        [
            "The subclass method must have a different name from the superclass method",
            "The subclass method must have the same name and the same (or compatible) "
            "parameter list as the superclass method",
            "The superclass method must be declared `static`",
            "The subclass must be in a different package from the superclass",
        ],
        1,
        "Overriding requires the subclass to redefine a method with an identical name and "
        "parameter list (signature) as the one it inherits, so the runtime can substitute the "
        "subclass's version via dynamic dispatch. A static superclass method (option C) "
        "actually cannot be overridden at all -- it can only be hidden, not overridden.",
    ),
    _q(
        "Overloading vs overriding",
        "Which pair correctly matches each concept with when it is resolved?",
        [
            "Overloading -> resolved at runtime; Overriding -> resolved at compile time",
            "Overloading -> resolved at compile time; Overriding -> resolved at runtime",
            "Both overloading and overriding are always resolved at compile time",
            "Both overloading and overriding are always resolved at runtime",
        ],
        1,
        "Overloading is settled by the compiler by matching argument types against available "
        "signatures (static binding), while overriding is settled at runtime based on the "
        "actual object type (dynamic binding). Mixing these up is one of the most common OOP "
        "exam traps.",
    ),
    _q(
        "Access modifiers",
        "A member declared `public` in a class is accessible from:",
        [
            "Only within the same class",
            "Only within the same package",
            "Anywhere the class itself is accessible, including other packages",
            "Only by subclasses, never by unrelated classes",
        ],
        2,
        "public is the least restrictive access modifier -- a public member can be used from "
        "any code that can see the class at all, regardless of package or inheritance "
        "relationship. private (option A's behavior) is the opposite extreme, restricting "
        "access to the declaring class only.",
    ),
    _q(
        "Access modifiers",
        "A member declared `private` in a class is accessible from:",
        [
            "Any class in the same package",
            "Only within the class in which it is declared",
            "Any subclass, even in a different package",
            "Anywhere in the program",
        ],
        1,
        "private is the most restrictive access modifier, confining visibility strictly to the "
        "declaring class itself -- not even subclasses can access it directly. This is the "
        "mechanism most commonly used to implement data hiding for encapsulation.",
    ),
    _q(
        "Access modifiers",
        "A member declared `protected` is accessible from:",
        [
            "The same class, same package, and subclasses (even in other packages)",
            "Only the exact class it is declared in, nowhere else",
            "Only unrelated classes in a different package",
            "Only static methods within the same class",
        ],
        0,
        "protected widens visibility beyond package-private to also include subclasses outside "
        "the package, which is exactly the level of access a base class typically grants to "
        "fields or methods meant for subclass reuse. It's more open than private but more "
        "restrictive than public.",
    ),
    _q(
        "Access modifiers",
        "When a class member has no access modifier keyword at all (the 'default' access "
        "level in Java), it is accessible from:",
        [
            "Anywhere in the program, just like public",
            "Only within the same package",
            "Only within the exact class, like private",
            "Only from subclasses regardless of package",
        ],
        1,
        "Default (package-private) access falls between private and protected in "
        "restrictiveness -- it exposes the member to any class in the same package but hides "
        "it from classes in other packages, even subclasses. This is the implicit access level "
        "when no modifier keyword is written.",
    ),
    _q(
        "Static vs instance members",
        "A `static` field in a class:",
        [
            "Has a separate copy for every object created from the class",
            "Is shared by all instances of the class and belongs to the class itself rather "
            "than any one object",
            "Can never be modified once the program starts running",
            "Must always be declared `private`",
        ],
        1,
        "A static field belongs to the class rather than to any individual object, so all "
        "instances share one single copy -- changing it through one object is visible through "
        "every other object. Instance (non-static) fields, by contrast, get a fresh "
        "independent copy per object.",
    ),
    _q(
        "Static vs instance members",
        "Which statement about instance (non-static) fields is correct?",
        [
            "Each object of the class gets its own independent copy of the field",
            "All objects of the class share exactly one copy of the field",
            "Instance fields can be accessed without creating any object",
            "Instance fields are automatically shared with all subclasses as static fields",
        ],
        0,
        "Every object created from the class allocates its own separate memory for instance "
        "fields, so modifying one object's field doesn't affect another object's copy. This is "
        "the opposite of static fields, which are shared across all instances (option B "
        "describes static, not instance, fields).",
    ),
    _q(
        "this keyword",
        "What does the `this` keyword refer to inside a non-static method?",
        [
            "The immediate superclass of the current object",
            "The current object on which the method was invoked",
            "A static instance shared by all objects",
            "The class itself, not any particular object",
        ],
        1,
        "this is a reference to the current object -- commonly used to disambiguate an "
        "instance field from a constructor/method parameter of the same name (e.g., this.x = "
        "x;) or to pass the current object elsewhere. super (not this) is used to refer to the "
        "parent class, so option A is incorrect.",
    ),
    _q(
        "super keyword",
        "What is the `super` keyword primarily used for?",
        [
            "To refer to the current object's own fields",
            "To access the parent class's members or invoke the parent class's constructor "
            "from a subclass",
            "To declare a method that cannot be overridden",
            "To create a new object without calling any constructor",
        ],
        1,
        "super lets a subclass explicitly reach into its immediate parent class -- calling "
        "super.someMethod() to invoke the parent's version, or super(args) as the first "
        "statement in a constructor to run the parent's constructor. This is distinct from "
        "`this`, which refers to the current object itself, not the parent.",
    ),
    _q(
        "Constructor chaining",
        "<pre>class Box {\n"
        "  int side;\n"
        "  Box() {\n"
        "    this(10);\n"
        "  }\n"
        "  Box(int side) {\n"
        "    this.side = side;\n"
        "  }\n"
        "}</pre> The no-argument constructor calling `this(10)` to invoke the other "
        "constructor in the same class is an example of:",
        [
            "Constructor overriding",
            "Constructor chaining",
            "Static binding",
            "Copy construction",
        ],
        1,
        "Constructor chaining is when one constructor invokes another constructor of the same "
        "class (using this(...)) or of its parent class (using super(...)) to avoid "
        "duplicating initialization logic. Note that constructors cannot be overridden at all "
        "(option A is meaningless), since they aren't inherited by subclasses.",
    ),
    _q(
        "Constructor chaining",
        "In a subclass constructor, if you don't explicitly write a call to `super(...)`, "
        "what happens?",
        [
            "The compiler leaves the parent class completely uninitialized",
            "The compiler automatically inserts a call to the parent class's no-argument "
            "constructor as the first statement",
            "The program fails to compile",
            "The parent class's constructor is skipped entirely and never runs",
        ],
        1,
        "Unless you explicitly call super(args) or this(args) as the first line, the compiler "
        "implicitly inserts a call to the parent's no-argument constructor, ensuring the "
        "parent portion of the object is initialized before the subclass's own initialization "
        "runs. If the parent has no no-argument constructor available, this implicit call "
        "fails to compile, which is a common gotcha.",
    ),
    _q(
        "Static vs instance members",
        "Why can a `static` method not directly access a non-static (instance) field of its "
        "class?",
        [
            "Because static methods run before the class is even loaded into memory",
            "Because a static method belongs to the class and isn't tied to any particular "
            "object, while an instance field only exists once an object is created",
            "Because instance fields are always declared `private`",
            "Static methods actually can always access instance fields directly with no "
            "restriction",
        ],
        1,
        "A static method can be called without ever creating an object (e.g., "
        "ClassName.method()), so there is no guaranteed object instance whose field it could "
        "read -- instance fields only come into existence when an object is constructed. To "
        "access an instance field from a static context, the method must be given a specific "
        "object reference to work with.",
    ),
    _q(
        "Overloading",
        "Can two methods in the same class be considered overloaded if they have identical "
        "names and identical parameter lists, but different return types?",
        [
            "Yes, return type alone is always enough to distinguish overloaded methods",
            "No, overloading requires the parameter lists to differ; return type alone is not "
            "sufficient and causes a compile error",
            "Yes, but only if one of the methods is static",
            "No, because methods with the same name are never allowed in one class",
        ],
        1,
        "The compiler distinguishes overloaded methods purely by their parameter lists "
        "(number, type, order) -- two methods with identical parameters but different return "
        "types are treated as a duplicate declaration and cause a compile-time error. This is "
        "a frequently tested gotcha, since it seems intuitive that return type should matter "
        "but it does not.",
    ),
    _q(
        "Constructors",
        "A copy constructor that simply copies a reference-type field's reference (rather than "
        "creating a new copy of the referenced object) produces what is known as a:",
        ["Deep copy", "Shallow copy", "Static copy", "Virtual copy"],
        1,
        "A shallow copy duplicates the field values as-is, so if a field holds a reference to "
        "another object, both the original and the copy end up pointing to the *same* "
        "underlying object -- changes through one affect the other. A deep copy instead "
        "recursively duplicates referenced objects too, so the two copies become fully "
        "independent.",
    ),
    _q(
        "Constructors",
        "<pre>class Student {\n"
        "  Student() { System.out.println(\"No-arg\"); }\n"
        "  Student(String name) { System.out.println(\"Parameterized\"); }\n"
        "}\n"
        "Student s = new Student(\"Asha\");</pre> Which constructor executes when this code "
        "runs?",
        [
            "The no-argument constructor, because it is always tried first",
            "The parameterized constructor, because the call's argument list matches its "
            "signature",
            "Both constructors run one after another",
            "Neither constructor runs; this is a compile error",
        ],
        1,
        "Java (and similarly C++/C#) picks the constructor whose parameter list matches the "
        "arguments supplied at the call site -- here, passing a String selects the "
        "Student(String name) constructor. Constructors behave like overloaded methods: the "
        "compiler matches by signature, not by declaration order.",
    ),
]


# ==================================================================== #
# 24. OOPs Practice — Set 3
# ==================================================================== #
# Set 3: Advanced OOP -- abstract classes vs interfaces, multiple inheritance and
# the diamond problem, composition vs inheritance, overriding rules (covariant
# returns, final and static methods), and object lifecycle (constructor order,
# garbage collection).
OOPS_PRACTICE_QUESTIONS_3 = [
    _q(
        "Abstract class vs interface",
        "Which statement correctly distinguishes an abstract class from an interface in most "
        "mainstream OOP languages (e.g., Java)?",
        [
            "An interface can have constructors and instance fields with state, while an "
            "abstract class cannot",
            "An abstract class can have constructors, instance fields, and a mix of "
            "implemented and abstract methods, while a traditional interface could not hold "
            "instance state",
            "Abstract classes and interfaces are identical in every respect",
            "An abstract class cannot be extended by more than one subclass",
        ],
        1,
        "An abstract class behaves like a regular class that also permits abstract "
        "(unimplemented) methods, so it can hold instance fields, define constructors, and mix "
        "concrete and abstract methods. A classic interface, by contrast, historically could "
        "declare only method signatures and constants, with no instance state or constructors "
        "of its own.",
    ),
    _q(
        "Abstract class vs interface",
        "In modern Java (8+), interfaces can additionally include which of the following, "
        "beyond plain abstract method declarations?",
        [
            "Constructors that run when the interface is 'instantiated' directly",
            "`default` and `static` methods that provide actual method bodies",
            "Private instance fields holding mutable object state",
            "Nothing else; interfaces are still restricted to abstract methods only",
        ],
        1,
        "Java 8 introduced default methods (with a body, usable by implementing classes "
        "without forcing an override) and static methods on interfaces, loosening the old "
        "'interfaces have no implementation' rule. Interfaces still cannot be instantiated "
        "directly or hold general mutable instance state the way a class can, so options A and "
        "C remain incorrect.",
    ),
    _q(
        "Multiple inheritance",
        "Why do languages like Java and C# disallow a class from extending more than one "
        "class (no multiple class inheritance)?",
        [
            "Because inheritance itself is not supported in these languages",
            "To avoid ambiguity when two parent classes define a conflicting method or field "
            "with the same name (the diamond problem)",
            "Because multiple inheritance is impossible to implement in any programming "
            "language",
            "Because these languages don't support polymorphism",
        ],
        1,
        "Allowing a class to inherit implementation from two parents creates ambiguity if both "
        "parents define a member with the same signature -- the compiler wouldn't know which "
        "one to use. Java and C# sidestep this by allowing a class to extend only one class "
        "but implement multiple interfaces instead, since interfaces (traditionally) "
        "contribute no conflicting implementation.",
    ),
    _q(
        "Diamond problem",
        "<pre>      A\n"
        "    /   \\\n"
        "   B     C\n"
        "    \\   /\n"
        "      D</pre> If class D inherits from both B and C, and both B and C independently "
        "override a method originally defined in A, what ambiguity does D face? This scenario "
        "is known as:",
        [
            "The diamond problem",
            "Constructor chaining",
            "Data hiding",
            "Operator overloading",
        ],
        0,
        "The diamond problem arises when a class inherits from two classes that share a common "
        "ancestor, and it becomes unclear which inherited (possibly overridden) version of a "
        "member D should use. This is precisely why languages restrict multiple inheritance of "
        "implementation via classes, while still permitting a class to implement multiple "
        "interfaces.",
    ),
    _q(
        "Diamond problem",
        "How do languages like Java avoid the diamond problem while still offering some form "
        "of 'multiple inheritance'?",
        [
            "By banning inheritance entirely",
            "By allowing a class to implement multiple interfaces (which traditionally carry "
            "no conflicting implementation), instead of extending multiple classes",
            "By requiring every class to be declared `final`",
            "By making all methods static so they can never conflict",
        ],
        1,
        "Since a class can implement any number of interfaces, and interfaces traditionally "
        "contributed no field state or method bodies, there was no ambiguous implementation to "
        "resolve. Even with Java 8's default methods, the language forces the implementing "
        "class to explicitly resolve any conflict if two interfaces provide clashing default "
        "methods, rather than silently picking one.",
    ),
    _q(
        "Composition vs inheritance",
        "Which relationship does composition model between two classes?",
        [
            "IS-A, the same relationship modeled by inheritance",
            "HAS-A, where one class contains an instance of another as a field",
            "USES-A-BRIEFLY, where a class calls another's static method once",
            "No relationship; composition is unrelated to class design",
        ],
        1,
        "Composition models a HAS-A relationship -- for example, a Car HAS-A Engine, where the "
        "Engine is a field inside Car rather than something Car extends. This is distinct from "
        "inheritance's IS-A relationship (e.g., Car IS-A Vehicle).",
    ),
    _q(
        "Composition vs inheritance",
        "Why do many OOP design guidelines favor 'composition over inheritance' when it's a "
        "close call?",
        [
            "Because composition creates tighter coupling to the exact implementation of the "
            "reused class",
            "Because composition lets you reuse behavior via object references without "
            "inheriting all of a base class's fields and methods, giving more flexibility to "
            "change behavior at runtime",
            "Because inheritance never allows code reuse",
            "Because composition removes the need for constructors entirely",
        ],
        1,
        "With composition, a class holds a reference to another object and can swap that "
        "object out or delegate selectively, avoiding the rigid, all-or-nothing coupling that "
        "comes from extending a base class. Deep inheritance hierarchies can become fragile -- "
        "a change in a base class can unexpectedly break many subclasses -- which composition "
        "tends to avoid.",
    ),
    _q(
        "Overriding rules",
        "<pre>class Animal {\n"
        "  Animal reproduce() { return new Animal(); }\n"
        "}\n"
        "class Dog extends Animal {\n"
        "  Dog reproduce() { return new Dog(); }\n"
        "}</pre> Dog's `reproduce()` returns `Dog` instead of `Animal`, yet this is still "
        "considered a valid override because Dog is a subtype of Animal. This is called:",
        [
            "Return type overloading",
            "A covariant return type",
            "Constructor chaining",
            "Static method hiding",
        ],
        1,
        "A covariant return type lets an overriding method return a more specific (subtype) "
        "type than the method it overrides, as long as that subtype is compatible with the "
        "original return type. This flexibility was added precisely so overriding methods "
        "don't have to widen their return type back to the exact parent type.",
    ),
    _q(
        "Overriding rules",
        "Declaring a method as `final` in its class means:",
        [
            "The method can be overloaded but never overridden by any subclass",
            "The method cannot be overridden by any subclass",
            "The method automatically becomes static",
            "The method can only be called once during the program's execution",
        ],
        1,
        "Marking a method final locks in its implementation, preventing any subclass from "
        "providing a different version through overriding -- this is often done to protect "
        "behavior that must stay consistent across the whole hierarchy. It has no effect on "
        "overloading, since overloading happens within the same class, not through "
        "inheritance.",
    ),
    _q(
        "Overriding rules",
        "What does declaring an entire class as `final` prevent?",
        [
            "The class from being instantiated at all",
            "The class from being extended (no subclass can be created from it)",
            "The class's methods from being overloaded",
            "The class from having any static members",
        ],
        1,
        "A final class cannot be subclassed at all -- String in Java is a well-known example, "
        "final specifically to prevent anyone from creating a modified subclass that could "
        "break assumptions relied on elsewhere. It says nothing about instantiation (final "
        "classes can still be instantiated normally) or about overloading within the class "
        "itself.",
    ),
    _q(
        "Overriding rules",
        "<pre>class Parent {\n"
        "  static void greet() { System.out.println(\"Parent\"); }\n"
        "}\n"
        "class Child extends Parent {\n"
        "  static void greet() { System.out.println(\"Child\"); }\n"
        "}</pre> Child re-declaring `greet()` with the same signature as Parent's static "
        "method is technically called:",
        [
            "Overriding, resolved dynamically at runtime just like instance methods",
            "Method hiding, resolved statically based on the reference type, not true "
            "overriding",
            "A compile error, since static methods can never be redeclared",
            "Constructor chaining",
        ],
        1,
        "Static methods are resolved based on the declared (compile-time) reference type "
        "rather than the actual object type, so Child's greet() doesn't override Parent's -- "
        "it merely hides it. This is a frequently tested trap: calling the method through a "
        "Parent-typed reference invokes Parent's version even if the object is actually a "
        "Child.",
    ),
    _q(
        "Overriding rules",
        "Why can a `private` method in a superclass not be overridden by a subclass?",
        [
            "Because private methods are automatically converted to public in subclasses",
            "Because private methods aren't inherited/visible to the subclass at all, so a "
            "same-named method in the subclass is treated as a brand-new, unrelated method",
            "Because private methods can only be called by the JVM internally",
            "Private methods actually can be overridden exactly like public methods",
        ],
        1,
        "Since a subclass has no visibility into its parent's private members, a method with a "
        "matching name and signature in the subclass isn't overriding anything -- it's simply "
        "an independent method that happens to share a name. Overriding requires the method to "
        "be visible and inherited, which private explicitly prevents.",
    ),
    _q(
        "Object lifecycle",
        "When you create an object of a subclass, in what order do the parent and child class "
        "constructors execute?",
        [
            "The child class constructor runs completely first, then the parent class "
            "constructor runs",
            "The parent class constructor runs first (directly or via an implicit/explicit "
            "super() call), then the child class constructor's own body runs",
            "Both constructors run simultaneously",
            "Only the child class constructor ever runs; the parent's constructor is skipped",
        ],
        1,
        "Because a subclass constructor always invokes a parent constructor as its very first "
        "action (explicitly with super(...) or implicitly by the compiler), the parent portion "
        "of the object is fully initialized before the child class's own constructor body "
        "executes. This guarantees inherited fields are ready before subclass-specific "
        "initialization relies on them.",
    ),
    _q(
        "Abstract class vs interface",
        "Can a class contain an abstract method without the class itself being declared "
        "`abstract`?",
        [
            "Yes, any class can freely mix in abstract methods",
            "No, a class with even one abstract method must itself be declared abstract, "
            "since it is incomplete and cannot be instantiated directly",
            "Yes, but only if the class has no constructors",
            "No, because abstract methods are only allowed inside interfaces",
        ],
        1,
        "An abstract method has no body, so a class containing one is inherently incomplete -- "
        "the language requires the class itself to be marked abstract, which also blocks "
        "direct instantiation until a concrete subclass fills in the missing implementations. "
        "Abstract methods aren't exclusive to interfaces either (option D); abstract classes "
        "commonly declare them too.",
    ),
    _q(
        "Multiple inheritance",
        "A class implementing several interfaces at once is an example of:",
        [
            "Multiple inheritance of implementation, identical to inheriting from multiple "
            "classes",
            "Multiple inheritance of type (the class gains multiple contracts/types it "
            "satisfies), without inheriting conflicting implementations",
            "The diamond problem occurring automatically",
            "Constructor chaining across interfaces",
        ],
        1,
        "Implementing multiple interfaces lets a class be treated as multiple distinct types "
        "(satisfying multiple contracts) without the conflicting-implementation ambiguity that "
        "multiple class inheritance would introduce. This is why languages that forbid "
        "extending multiple classes still allow implementing multiple interfaces freely.",
    ),
    _q(
        "Object lifecycle",
        "In languages with automatic garbage collection (like Java), when does an object "
        "typically become eligible for garbage collection?",
        [
            "As soon as its constructor finishes running",
            "When there are no more reachable references pointing to it from active parts of "
            "the program",
            "Only when the programmer calls a `delete` keyword explicitly",
            "Immediately after any method on it is called",
        ],
        1,
        "The garbage collector periodically identifies objects that are no longer reachable "
        "through any live reference chain from active code, and reclaims their memory "
        "automatically. Unlike C++, most garbage-collected languages have no explicit delete "
        "keyword (option C) -- memory management is handled behind the scenes.",
    ),
    _q(
        "Object lifecycle",
        "How does a destructor in C++ differ from Java's garbage collector in terms of when "
        "cleanup happens?",
        [
            "They behave identically in both languages with no meaningful difference",
            "A C++ destructor runs deterministically when an object goes out of scope or is "
            "explicitly deleted, while Java's garbage collector reclaims memory at an "
            "unpredictable time chosen by the JVM",
            "Java objects are destroyed the instant they go out of scope, exactly like C++",
            "C++ destructors are called by a background garbage collector, just like Java",
        ],
        1,
        "C++ gives deterministic, immediate cleanup -- a destructor runs the moment an "
        "object's lifetime ends (scope exit or delete) -- which is why C++ is often used for "
        "precise resource management. Java's garbage collector, by contrast, reclaims "
        "unreachable objects at a time of its own choosing, so relying on finalize() for "
        "timely cleanup is discouraged.",
    ),
    _q(
        "Composition vs inheritance",
        "<pre>class Engine {\n"
        "  void start() { System.out.println(\"Engine running\"); }\n"
        "}\n"
        "class Car {\n"
        "  private Engine engine = new Engine();\n"
        "  void drive() { engine.start(); }\n"
        "}</pre> Car holding a reference to an Engine object as a field, rather than extending "
        "Engine, demonstrates:",
        [
            "Inheritance",
            "Composition (a HAS-A relationship)",
            "Interface segregation",
            "Operator overloading",
        ],
        1,
        "Car doesn't extend Engine (which would be an odd IS-A claim -- a car is not a kind of "
        "engine); instead it holds an Engine instance as a field and delegates to it, which is "
        "composition's HAS-A pattern. This is generally a safer design choice here than "
        "inheritance, since a car legitimately contains an engine rather than being one.",
    ),
    _q(
        "Abstract class vs interface",
        "Can an abstract class contain fully implemented (concrete) methods alongside "
        "abstract ones?",
        [
            "No, every method in an abstract class must be abstract",
            "Yes, an abstract class can freely mix concrete methods (with a body) and "
            "abstract methods (without a body) in the same class",
            "No, abstract classes may only contain fields, never methods",
            "Yes, but only if the class has no constructor",
        ],
        1,
        "Unlike a traditional interface, an abstract class is allowed to provide fully "
        "working, inherited-as-is methods alongside abstract ones that subclasses must "
        "implement themselves. This flexibility makes abstract classes useful for sharing "
        "common code while still forcing subclasses to fill in specific behavior.",
    ),
    _q(
        "Overriding rules",
        "Which of these is a valid rule that an overriding method must follow with respect to "
        "the method it overrides?",
        [
            "The overriding method may reduce the visibility of the method (e.g., change "
            "public to private)",
            "The overriding method cannot have a more restrictive access modifier than the "
            "overridden method (e.g., cannot change public to private)",
            "The overriding method must always be declared `static`",
            "The overriding method must throw more checked exceptions than the overridden one",
        ],
        1,
        "Overriding rules require the subclass method to be at least as accessible as the "
        "method it overrides -- narrowing public down to private, for instance, would violate "
        "the superclass's contract and is disallowed by the compiler. It's fine to widen "
        "access (e.g., protected to public), but never to restrict it below the original "
        "level.",
    ),
]


# ==================================================================== #
# 25. Java Practice — Set 1
# ==================================================================== #
# Set 1: primitive types & ranges, casting/promotion, operators (%, ++/--, &&/||, bitwise),
# control statements (if/switch/loop, fall-through), output-prediction snippets.
JAVA_PRACTICE_QUESTIONS = [
    _q(
        "Primitive types",
        "What is the valid range of values for a Java <code>byte</code>?",
        ["-128 to 127", "0 to 255", "-32768 to 32767", "-256 to 255"],
        0,
        "A byte is 8 bits and signed, giving 2^8 = 256 possible values split around zero: "
        "-128 to 127. 0 to 255 would be the range for an 8-bit unsigned type, which Java's "
        "byte is not.",
    ),
    _q(
        "Integer literals",
        "What happens when you compile and run this code?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        long big = 3000000000;\n"
        "        System.out.println(big);\n"
        "    }\n"
        "}</pre>",
        [
            "Compiles fine and prints 3000000000",
            "Compile-time error: integer literal is too large",
            "Prints a negative number due to overflow",
            "Throws a NumberFormatException at runtime",
        ],
        1,
        "An integer literal without a suffix defaults to type int, whose max value is about "
        "2.1 billion, so 3000000000 doesn't fit and fails to compile. Writing 3000000000L "
        "(with the L suffix) would make it a long literal and compile fine.",
    ),
    _q(
        "Narrowing cast",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        int i = 130;\n"
        "        byte b = (byte) i;\n"
        "        System.out.println(b);\n"
        "    }\n"
        "}</pre>",
        ["126", "-126", "130", "2"],
        1,
        "Narrowing an int to a byte keeps only the low 8 bits. 130 is 10000010 in binary, and "
        "as a signed byte that bit pattern represents -126 (130 - 256). It does not simply clip "
        "to the nearest valid byte value.",
    ),
    _q(
        "Type promotion",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        char c = 'A';\n"
        "        int i = c + 1;\n"
        "        System.out.println(i);\n"
        "    }\n"
        "}</pre>",
        ["66", "B", "A1", "Compile error"],
        0,
        "In an arithmetic expression, char is automatically promoted to int, so 'A' (65) + 1 "
        "becomes the int 66, and that's what gets printed. It would only print 'B' if the "
        "result were explicitly cast back to char.",
    ),
    _q(
        "Modulo operator",
        "What does <pre>System.out.println(-7 % 3);</pre> print?",
        ["-1", "1", "2", "-2"],
        0,
        "In Java, the result of % takes the sign of the dividend, not the divisor. -7 / 3 "
        "truncates toward zero to -2, and -2 * 3 = -6, leaving a remainder of -7 - (-6) = -1.",
    ),
    _q(
        "Increment operators",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        int i = 5;\n"
        "        System.out.println(i++ + \" \" + ++i);\n"
        "    }\n"
        "}</pre>",
        ["5 7", "5 6", "6 7", "6 6"],
        0,
        "i++ (postfix) yields the current value 5 and then bumps i to 6; the next operand ++i "
        "(prefix) bumps i to 7 first and yields 7. So the concatenation prints \"5 7\", not "
        "\"6 7\", because postfix returns the pre-increment value.",
    ),
    _q(
        "Increment operators",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        int i = 5;\n"
        "        i = i++ + ++i;\n"
        "        System.out.println(i);\n"
        "    }\n"
        "}</pre>",
        ["12", "13", "11", "10"],
        0,
        "Operands are evaluated left to right: i++ reads 5 (i becomes 6), then ++i increments "
        "i to 7 and yields 7. The sum 5 + 7 = 12 is then assigned to i, overwriting the "
        "intermediate increments, so the final value is 12, not 13.",
    ),
    _q(
        "Short-circuit evaluation",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    static boolean check() {\n"
        "        System.out.println(\"called\");\n"
        "        return true;\n"
        "    }\n"
        "    public static void main(String[] args) {\n"
        "        boolean result = false && check();\n"
        "        System.out.println(result);\n"
        "    }\n"
        "}</pre>",
        ["called, then false", "false", "true", "called, then true"],
        1,
        "&& short-circuits: once the left operand is false, the overall expression can't be "
        "true, so check() is never called and only \"false\" prints. If & (bitwise, non-"
        "short-circuiting) were used instead, \"called\" would print too.",
    ),
    _q(
        "Short-circuit evaluation",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    static boolean check() {\n"
        "        System.out.println(\"called\");\n"
        "        return true;\n"
        "    }\n"
        "    public static void main(String[] args) {\n"
        "        boolean result = true || check();\n"
        "        System.out.println(result);\n"
        "    }\n"
        "}</pre>",
        ["called, then true", "true", "called, then false", "false"],
        1,
        "|| short-circuits: once the left operand is true, the overall expression is already "
        "known to be true, so check() is skipped and only \"true\" prints. The distractor "
        "\"called\\ntrue\" would be correct only for the non-short-circuiting | operator.",
    ),
    _q(
        "Bitwise vs logical operators",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    static boolean check() {\n"
        "        System.out.println(\"called\");\n"
        "        return true;\n"
        "    }\n"
        "    public static void main(String[] args) {\n"
        "        boolean result = false & check();\n"
        "        System.out.println(result);\n"
        "    }\n"
        "}</pre>",
        ["false", "called, then false", "true", "called, then true"],
        1,
        "Unlike &&, the bitwise & operator on booleans always evaluates both operands, so "
        "check() runs and prints \"called\" even though the left side alone already decides "
        "the AND result is false. The final result is still false.",
    ),
    _q(
        "Bitwise operators",
        "What does <pre>System.out.println(5 ^ 3);</pre> print?",
        ["6", "8", "2", "7"],
        0,
        "5 is 101 and 3 is 011 in binary; XOR flips bits that differ, giving 110, which is 6. "
        "8 would be the result of 5 + 3, and 2 would be the result of 5 & 3, so it's easy to "
        "confuse these bitwise operators.",
    ),
    _q(
        "Bitwise shift operators",
        "What does <pre>System.out.println(5 &lt;&lt; 2);</pre> print?",
        ["20", "10", "7", "25"],
        0,
        "A left shift by n bits multiplies the value by 2^n. 5 << 2 multiplies 5 by 4, giving "
        "20. 10 would only be correct for a shift of 1 (5 << 1).",
    ),
    _q(
        "Bitwise shift operators",
        "What does this print?"
        "<pre>System.out.println((-8 &gt;&gt; 1) + \" \" + (-8 &gt;&gt;&gt; 1));</pre>",
        ["-4 2147483644", "-4 -4", "4 2147483644", "-4 4"],
        0,
        ">> is an arithmetic shift that preserves the sign bit, so -8 >> 1 stays negative "
        "and gives -4. >>> is an unsigned shift that fills with zeros regardless of sign, so "
        "on -8's 32-bit representation it produces a huge positive number, 2147483644.",
    ),
    _q(
        "Ternary operator",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        int a = 5;\n"
        "        double b = 10.5;\n"
        "        System.out.println(true ? a : b);\n"
        "    }\n"
        "}</pre>",
        ["5", "5.0", "10.5", "Compile error"],
        1,
        "Even though the condition selects a, the ternary operator's result type is decided "
        "by both branches together: since one branch is int and the other double, binary "
        "numeric promotion widens a to double, so the printed value is 5.0, not 5.",
    ),
    _q(
        "Control statements",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        int x = 5;\n"
        "        if (x &gt; 2)\n"
        "            if (x &gt; 10)\n"
        "                System.out.println(\"A\");\n"
        "            else\n"
        "                System.out.println(\"B\");\n"
        "    }\n"
        "}</pre>",
        ["A", "B", "Nothing is printed", "Compile error"],
        1,
        "An else without braces always binds to the nearest unmatched if — here that's "
        "\"if (x > 10)\", not the outer \"if (x > 2)\". Since x > 2 is true but x > 10 is "
        "false, the else branch runs and \"B\" prints.",
    ),
    _q(
        "Switch fall-through",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        int x = 2;\n"
        "        switch (x) {\n"
        "            case 1: System.out.print(\"one\");\n"
        "            case 2: System.out.print(\"two\");\n"
        "            case 3: System.out.print(\"three\");\n"
        "                break;\n"
        "            case 4: System.out.print(\"four\");\n"
        "        }\n"
        "    }\n"
        "}</pre>",
        ["two", "twothree", "onetwothree", "twothreefour"],
        1,
        "Execution jumps to the matching case (2) and then falls through every subsequent "
        "case until it hits a break, so both \"two\" and \"three\" print before the break "
        "stops it. Case 1 is skipped entirely since it comes before the matching case.",
    ),
    _q(
        "Switch on String",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        String s = \"cat\";\n"
        "        switch (s) {\n"
        "            case \"dog\": System.out.println(\"Dog\"); break;\n"
        "            case \"cat\": System.out.println(\"Cat\"); break;\n"
        "            default: System.out.println(\"Other\");\n"
        "        }\n"
        "    }\n"
        "}</pre>",
        ["Cat", "Dog", "Other", "Compile error: switch cannot use String"],
        0,
        "Java (since version 7) allows switch on String, comparing with .equals() semantics "
        "internally, so \"cat\" matches the \"cat\" case and prints \"Cat\". It is not a "
        "compile error, unlike switching on arbitrary objects.",
    ),
    _q(
        "do-while loop",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        int i = 10;\n"
        "        do {\n"
        "            System.out.println(i);\n"
        "            i++;\n"
        "        } while (i &lt; 5);\n"
        "    }\n"
        "}</pre>",
        ["10", "Nothing is printed", "Infinite loop", "5"],
        0,
        "A do-while loop always runs its body at least once before checking the condition. "
        "Here it prints 10, then checks i < 5 (now 11 < 5), which is false, so it stops "
        "after exactly one iteration — a plain while loop would print nothing at all.",
    ),
    _q(
        "Labeled break",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        outer:\n"
        "        for (int i = 0; i &lt; 3; i++) {\n"
        "            for (int j = 0; j &lt; 3; j++) {\n"
        "                if (j == 1) break outer;\n"
        "                System.out.println(i + \"\" + j);\n"
        "            }\n"
        "        }\n"
        "    }\n"
        "}</pre>",
        ["00", "00, 01, 02", "00, 10, 20", "Compile error"],
        0,
        "A labeled break exits the labeled outer loop entirely, not just the inner one. On "
        "the first outer iteration, \"00\" prints, then j becomes 1 and break outer terminates "
        "both loops immediately, so no other pairs ever print.",
    ),
    _q(
        "For loop mechanics",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        for (int i = 0, j = 10; i &lt; 3; i++, j--) {\n"
        "            System.out.print(i + \"\" + j + \" \");\n"
        "        }\n"
        "    }\n"
        "}</pre>",
        ["010 19 28 ", "0 10 1 9 2 8", "010 110 210", "Infinite loop"],
        0,
        "A for loop's init and update clauses can each hold multiple comma-separated "
        "statements, here initializing i and j together and updating both each iteration. "
        "The loop runs for i = 0, 1, 2 (paired with j = 10, 9, 8), printing \"010 19 28 \".",
    ),
]


# ==================================================================== #
# 26. Java Practice — Set 2
# ==================================================================== #
# Set 2: classes/objects & constructors, inheritance & super, overloading vs overriding,
# interfaces vs abstract classes, exception handling (try/catch/finally, checked vs unchecked).
JAVA_PRACTICE_QUESTIONS_2 = [
    _q(
        "Default constructors",
        "What does this program print?"
        "<pre>class Box {}\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        Box b = new Box();\n"
        "        System.out.println(b != null);\n"
        "    }\n"
        "}</pre>",
        ["true", "false", "Compile error: no constructor", "NullPointerException"],
        0,
        "When a class defines no constructor at all, the compiler automatically supplies a "
        "public no-argument default constructor, so new Box() works fine and b is non-null. "
        "A compile error would only occur if some other constructor were defined without a "
        "no-arg one, and the caller still tried to use new Box().",
    ),
    _q(
        "Constructor chaining",
        "What does this program print?"
        "<pre>class Box {\n"
        "    int size;\n"
        "    Box() {\n"
        "        this(10);\n"
        "        System.out.println(\"no-arg\");\n"
        "    }\n"
        "    Box(int size) {\n"
        "        this.size = size;\n"
        "        System.out.println(\"arg: \" + size);\n"
        "    }\n"
        "}\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        new Box();\n"
        "    }\n"
        "}</pre>",
        ["arg: 10, then no-arg", "no-arg, then arg: 10", "arg: 10", "no-arg"],
        0,
        "this(10) must be the first statement in the no-arg constructor, and it transfers "
        "control to the Box(int) constructor immediately, which runs and prints \"arg: 10\" "
        "first. Only after that call returns does execution resume after this(10) and print "
        "\"no-arg\".",
    ),
    _q(
        "Constructors and inheritance",
        "What does this program print?"
        "<pre>class Animal {\n"
        "    Animal() { System.out.println(\"Animal\"); }\n"
        "}\n"
        "class Dog extends Animal {\n"
        "    Dog() { System.out.println(\"Dog\"); }\n"
        "}\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        new Dog();\n"
        "    }\n"
        "}</pre>",
        ["Animal, then Dog", "Dog, then Animal", "Animal", "Dog"],
        0,
        "Every constructor implicitly calls super() as its first statement unless another "
        "constructor call is written explicitly, so the parent Animal constructor fully runs "
        "before the Dog constructor's own body executes. That's why \"Animal\" prints before "
        "\"Dog\".",
    ),
    _q(
        "Method overloading resolution",
        "What does this program print?"
        "<pre>class Test {\n"
        "    static void show(int x) { System.out.println(\"int\"); }\n"
        "    static void show(long x) { System.out.println(\"long\"); }\n"
        "    static void show(Integer x) { System.out.println(\"Integer\"); }\n"
        "    public static void main(String[] args) {\n"
        "        show(5);\n"
        "    }\n"
        "}</pre>",
        ["int", "long", "Integer", "Compile error: ambiguous"],
        0,
        "Java's overload resolution prefers the most specific applicable method without "
        "boxing or varargs first: an exact primitive match (show(int)) beats a widening match "
        "(show(long)) and both beat autoboxing (show(Integer)), which is tried only in a "
        "later resolution phase. So show(5) picks show(int).",
    ),
    _q(
        "Method overriding & polymorphism",
        "What does this program print?"
        "<pre>class Animal {\n"
        "    void sound() { System.out.println(\"Some sound\"); }\n"
        "}\n"
        "class Cat extends Animal {\n"
        "    void sound() { System.out.println(\"Meow\"); }\n"
        "}\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        Animal a = new Cat();\n"
        "        a.sound();\n"
        "    }\n"
        "}</pre>",
        ["Meow", "Some sound", "Compile error", "Runtime exception"],
        0,
        "Instance methods are dispatched dynamically based on the object's actual runtime "
        "type, not the reference's declared type. Since a refers to a Cat object, a.sound() "
        "calls Cat's override and prints \"Meow\", even though a is declared as Animal.",
    ),
    _q(
        "Field hiding",
        "What does this program print?"
        "<pre>class Animal {\n"
        "    String name = \"Animal\";\n"
        "}\n"
        "class Cat extends Animal {\n"
        "    String name = \"Cat\";\n"
        "}\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        Animal a = new Cat();\n"
        "        System.out.println(a.name);\n"
        "    }\n"
        "}</pre>",
        ["Animal", "Cat", "Compile error", "null"],
        0,
        "Unlike methods, fields are not polymorphic in Java — field access is resolved at "
        "compile time using the reference's declared type, not the object's runtime type. "
        "Since a is declared as Animal, a.name reads Animal's field and prints \"Animal\".",
    ),
    _q(
        "Calling overridden methods",
        "What does this program print?"
        "<pre>class Animal {\n"
        "    void sound() { System.out.println(\"Some sound\"); }\n"
        "}\n"
        "class Cat extends Animal {\n"
        "    void sound() {\n"
        "        super.sound();\n"
        "        System.out.println(\"Meow\");\n"
        "    }\n"
        "}\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        new Cat().sound();\n"
        "    }\n"
        "}</pre>",
        ["Some sound, then Meow", "Meow, then Some sound", "Meow", "Some sound"],
        0,
        "super.sound() explicitly invokes the parent class's version of the overridden "
        "method, which runs first and prints \"Some sound\". Control then returns to Cat's "
        "sound() method, which continues and prints \"Meow\".",
    ),
    _q(
        "Abstract classes",
        "What happens when you try to compile this code?"
        "<pre>abstract class Shape {\n"
        "    abstract void draw();\n"
        "}\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        Shape s = new Shape();\n"
        "    }\n"
        "}</pre>",
        [
            "Compile error: Shape is abstract and cannot be instantiated",
            "Runtime exception",
            "Prints nothing, compiles fine",
            "Compiles fine but draw() is never called",
        ],
        0,
        "An abstract class may declare methods without bodies, so the compiler cannot build a "
        "complete, usable object from it directly — new Shape() is rejected at compile time. "
        "You must first create a concrete subclass that implements draw() and instantiate "
        "that instead.",
    ),
    _q(
        "Interface default methods",
        "What does this program print?"
        "<pre>interface Greet {\n"
        "    default void hello() { System.out.println(\"Hello\"); }\n"
        "}\n"
        "class English implements Greet {}\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        new English().hello();\n"
        "    }\n"
        "}</pre>",
        ["Hello", "Compile error: must override hello()", "Runtime exception", "Nothing prints"],
        0,
        "Java 8+ interfaces can provide default method implementations, which implementing "
        "classes inherit automatically without needing to override them. Since English "
        "doesn't override hello(), it simply uses Greet's default body and prints \"Hello\".",
    ),
    _q(
        "Interface conflicts",
        "What happens when you try to compile this code?"
        "<pre>interface A { default void greet() { System.out.println(\"A\"); } }\n"
        "interface B { default void greet() { System.out.println(\"B\"); } }\n"
        "class C implements A, B {\n"
        "}</pre>",
        [
            "Compile error: C must override greet()",
            "Prints A",
            "Prints B",
            "Prints A then B",
        ],
        0,
        "When a class implements two interfaces that provide conflicting default methods "
        "with the same signature, Java refuses to guess which one you meant. The compiler "
        "forces C to explicitly override greet() (optionally calling A.super.greet() or "
        "B.super.greet() inside it) to resolve the ambiguity.",
    ),
    _q(
        "final methods",
        "What happens when you try to compile this code?"
        "<pre>class Animal {\n"
        "    final void sound() { System.out.println(\"Sound\"); }\n"
        "}\n"
        "class Dog extends Animal {\n"
        "    void sound() { System.out.println(\"Bark\"); }\n"
        "}</pre>",
        [
            "Compile error: cannot override final method",
            "Prints Bark when Dog's sound() runs",
            "Prints Sound when Dog's sound() runs",
            "Compiles fine; both methods coexist",
        ],
        0,
        "Marking a method final prevents any subclass from overriding it, which is exactly "
        "what Dog attempts here, so the compiler rejects it. This is commonly used to lock "
        "down behavior that must not change in subclasses, such as security-sensitive logic.",
    ),
    _q(
        "final classes",
        "What happens when you try to compile this code?"
        "<pre>final class Utility {\n"
        "    static int square(int x) { return x * x; }\n"
        "}\n"
        "class Helper extends Utility {\n"
        "}</pre>",
        [
            "Compile error: cannot inherit from final class Utility",
            "Compiles fine; Helper inherits square()",
            "Runtime exception when Helper is used",
            "Compiles fine but square() is inaccessible",
        ],
        0,
        "A class declared final cannot be subclassed at all, so \"class Helper extends "
        "Utility\" is rejected at compile time. This is how classes like java.lang.String are "
        "protected from being extended and having their guarantees broken.",
    ),
    _q(
        "try-catch-finally order",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        try {\n"
        "            System.out.println(\"try\");\n"
        "            throw new RuntimeException(\"err\");\n"
        "        } catch (RuntimeException e) {\n"
        "            System.out.println(\"catch\");\n"
        "        } finally {\n"
        "            System.out.println(\"finally\");\n"
        "        }\n"
        "    }\n"
        "}</pre>",
        ["try, catch, finally", "try, finally, catch", "try, catch", "catch, finally"],
        0,
        "The try block runs until the exception is thrown, control transfers to the matching "
        "catch block, and finally always runs last regardless of whether an exception "
        "occurred or was caught. So the order is strictly try, then catch, then finally.",
    ),
    _q(
        "finally with return",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    static int test() {\n"
        "        try {\n"
        "            return 1;\n"
        "        } finally {\n"
        "            System.out.println(\"finally\");\n"
        "        }\n"
        "    }\n"
        "    public static void main(String[] args) {\n"
        "        System.out.println(test());\n"
        "    }\n"
        "}</pre>",
        ["finally, then 1", "1, then finally", "1", "finally"],
        0,
        "Even when a try block returns, Java runs the finally block before the method "
        "actually hands control back to the caller, so \"finally\" prints first. Only after "
        "that does test() truly return 1, which main() then prints.",
    ),
    _q(
        "Checked vs unchecked exceptions",
        "Which of these is a checked exception that a method must either catch or declare "
        "with <code>throws</code>?",
        ["IOException", "NullPointerException", "ArrayIndexOutOfBoundsException", "ArithmeticException"],
        0,
        "IOException extends Exception directly (not RuntimeException), making it a checked "
        "exception the compiler forces you to handle or declare. The other three all extend "
        "RuntimeException, so they're unchecked and can be thrown without any such "
        "declaration.",
    ),
    _q(
        "Catch block ordering",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        try {\n"
        "            int[] arr = new int[2];\n"
        "            arr[5] = 1;\n"
        "        } catch (ArithmeticException e) {\n"
        "            System.out.println(\"Arithmetic\");\n"
        "        } catch (ArrayIndexOutOfBoundsException e) {\n"
        "            System.out.println(\"ArrayIndex\");\n"
        "        } catch (Exception e) {\n"
        "            System.out.println(\"Exception\");\n"
        "        }\n"
        "    }\n"
        "}</pre>",
        ["ArrayIndex", "Arithmetic", "Exception", "Compile error: unreachable catch block"],
        0,
        "Catch blocks are checked top to bottom, and the JVM picks the first one whose type "
        "matches the thrown exception. ArrayIndexOutOfBoundsException doesn't match "
        "ArithmeticException, so it falls to the second catch, which matches exactly.",
    ),
    _q(
        "Exception hierarchy",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        try {\n"
        "            String s = null;\n"
        "            s.length();\n"
        "        } catch (Exception e) {\n"
        "            System.out.println(\"Caught: \" + e.getClass().getSimpleName());\n"
        "        }\n"
        "    }\n"
        "}</pre>",
        [
            "Caught: NullPointerException",
            "Compile error: NullPointerException not caught",
            "Caught: Exception",
            "Runtime crash, not caught",
        ],
        0,
        "NullPointerException is a subclass of RuntimeException, which is itself a subclass "
        "of Exception, so a catch (Exception e) block matches and catches it. The exception's "
        "actual runtime class is still NullPointerException, which is what getSimpleName() "
        "reports.",
    ),
    _q(
        "Custom checked exceptions",
        "What happens when this program is run?"
        "<pre>class MyException extends Exception {\n"
        "    MyException(String msg) { super(msg); }\n"
        "}\n"
        "public class Main {\n"
        "    static void risky() throws MyException {\n"
        "        throw new MyException(\"custom error\");\n"
        "    }\n"
        "    public static void main(String[] args) throws MyException {\n"
        "        risky();\n"
        "    }\n"
        "}</pre>",
        [
            "Compiles fine; program terminates with an uncaught MyException printed to stderr",
            "Compile error: checked exception must be caught, not just declared",
            "Prints \"custom error\" and continues normally",
            "Nothing happens; the exception is silently ignored",
        ],
        0,
        "Declaring throws MyException on both risky() and main() satisfies the compiler's "
        "checked-exception rule without requiring a catch block. Since nothing ever catches "
        "it, it propagates out of main() and terminates the program with a stack trace.",
    ),
    _q(
        "Static method hiding",
        "What does this program print?"
        "<pre>class Animal {\n"
        "    static void greet() { System.out.println(\"Animal static\"); }\n"
        "}\n"
        "class Dog extends Animal {\n"
        "    static void greet() { System.out.println(\"Dog static\"); }\n"
        "}\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        Animal a = new Dog();\n"
        "        a.greet();\n"
        "    }\n"
        "}</pre>",
        ["Animal static", "Dog static", "Compile error", "Both are printed"],
        0,
        "Static methods belong to a class, not an object, so they cannot be overridden — "
        "only hidden. Calls to static methods through a reference are resolved at compile "
        "time using the reference's declared type (Animal), so \"Animal static\" prints, "
        "unlike the dynamic dispatch used for instance methods.",
    ),
    _q(
        "Interface fields",
        "What happens when you try to compile this code?"
        "<pre>interface Config {\n"
        "    int MAX = 100;\n"
        "}\n"
        "public class Main implements Config {\n"
        "    public static void main(String[] args) {\n"
        "        MAX = 200;\n"
        "        System.out.println(MAX);\n"
        "    }\n"
        "}</pre>",
        [
            "Compile error: cannot assign a value to final variable MAX",
            "Prints 200",
            "Prints 100",
            "Runtime exception",
        ],
        0,
        "Every field declared in an interface is implicitly public, static, and final, "
        "whether or not those keywords are written. Since MAX is final, the assignment "
        "MAX = 200 is rejected at compile time.",
    ),
]


# ==================================================================== #
# 27. Java Practice — Set 3
# ==================================================================== #
# Set 3: String immutability & pool (== vs equals), StringBuilder, wrapper classes &
# autoboxing, Collections basics (ArrayList/LinkedList/HashMap/TreeMap), static/final/
# finally/finalize distinction, basic multithreading (Runnable/Thread, synchronized).
JAVA_PRACTICE_QUESTIONS_3 = [
    _q(
        "String immutability",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        String s = \"Hello\";\n"
        "        s.concat(\" World\");\n"
        "        System.out.println(s);\n"
        "    }\n"
        "}</pre>",
        ["Hello", "Hello World", "World", "Compile error"],
        0,
        "Strings in Java are immutable — concat() returns a brand-new String containing the "
        "result but never modifies the original. Since that returned value is discarded "
        "(not assigned back to s), s still refers to the original unchanged \"Hello\".",
    ),
    _q(
        "String pool",
        "What does this print?"
        "<pre>String a = \"java\";\n"
        "String b = \"java\";\n"
        "System.out.println((a == b) + \" \" + a.equals(b));</pre>",
        ["true true", "false true", "true false", "false false"],
        0,
        "String literals are interned into a shared string pool, so two identical literals "
        "point to the exact same object, making == true as well as .equals() true. This "
        "would differ if either string were built with new String(...).",
    ),
    _q(
        "String pool vs new String",
        "What does this print?"
        "<pre>String a = \"java\";\n"
        "String b = new String(\"java\");\n"
        "System.out.println((a == b) + \" \" + a.equals(b));</pre>",
        ["false true", "true true", "true false", "false false"],
        0,
        "new String(\"java\") explicitly forces creation of a separate object on the heap "
        "outside the string pool, so a == b compares references and is false, even though "
        "the characters are identical. .equals() compares content, not identity, so it is "
        "still true.",
    ),
    _q(
        "String interning",
        "What does <pre>String a = \"java\";\n"
        "String b = new String(\"java\").intern();\n"
        "System.out.println(a == b);</pre> print?",
        ["true", "false", "Compile error", "NullPointerException"],
        0,
        "intern() looks up (or adds) the string's content in the shared string pool and "
        "returns that canonical pooled reference. Since \"java\" is already pooled from the "
        "literal a, b ends up pointing to the very same object as a, making == true.",
    ),
    _q(
        "StringBuilder",
        "What does this program print?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        StringBuilder sb = new StringBuilder(\"abc\");\n"
        "        sb.append(\"def\").reverse();\n"
        "        System.out.println(sb);\n"
        "    }\n"
        "}</pre>",
        ["fedcba", "abcdef", "cbafed", "Compile error"],
        0,
        "append() and reverse() both mutate the same StringBuilder in place and can be "
        "chained since each returns the StringBuilder itself. append(\"def\") makes it "
        "\"abcdef\", and reverse() then flips it to \"fedcba\".",
    ),
    _q(
        "String vs StringBuilder",
        "Why is StringBuilder generally preferred over String for building up text inside a "
        "loop with many iterations?",
        [
            "Because String concatenation creates a new String object on every operation due to immutability, while StringBuilder mutates an internal buffer",
            "Because String objects are cached automatically and are always faster",
            "Because String and StringBuilder perform identically in every scenario",
            "Because StringBuilder cannot hold more than one concatenation at a time",
        ],
        0,
        "Since Strings are immutable, every += or concat() call inside a loop allocates an "
        "entirely new String, which wastes time and memory over many iterations. "
        "StringBuilder instead grows and edits one internal char array, avoiding repeated "
        "allocation.",
    ),
    _q(
        "Integer caching",
        "What does this print?"
        "<pre>Integer a = 100;\n"
        "Integer b = 100;\n"
        "Integer c = 200;\n"
        "Integer d = 200;\n"
        "System.out.println((a == b) + \" \" + (c == d));</pre>",
        ["true false", "false true", "true true", "false false"],
        0,
        "Java caches boxed Integer values from -128 to 127, so autoboxing 100 twice reuses "
        "the same cached object, making a == b true. 200 falls outside that cache range, so "
        "each autoboxing creates a distinct object, making c == d false.",
    ),
    _q(
        "Autoboxing/unboxing",
        "What happens when this program runs?"
        "<pre>public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        Integer x = null;\n"
        "        int y = x;\n"
        "        System.out.println(y);\n"
        "    }\n"
        "}</pre>",
        [
            "Throws a NullPointerException at runtime",
            "Prints 0",
            "Prints null",
            "Compile error",
        ],
        0,
        "Assigning an Integer to an int triggers automatic unboxing, which calls x.intValue() "
        "behind the scenes. Since x is null, that method call fails with a "
        "NullPointerException at runtime — the code compiles fine because unboxing is a "
        "legal conversion, it just can't succeed on a null reference.",
    ),
    _q(
        "Wrapper class parsing",
        "What is the key difference between <code>Integer.parseInt(\"5\")</code> and "
        "<code>Integer.valueOf(\"5\")</code>?",
        [
            "parseInt returns a primitive int, while valueOf returns an Integer object (possibly reused from the cache)",
            "parseInt returns an Integer object, while valueOf returns a primitive int",
            "They are identical in every way, including their return type",
            "valueOf throws an exception for any numeric string",
        ],
        0,
        "parseInt is declared to return a primitive int, whereas valueOf returns a boxed "
        "Integer object, which for small values may come from the Integer cache instead of a "
        "new allocation. Both parse the same way and throw NumberFormatException for invalid "
        "input.",
    ),
    _q(
        "ArrayList vs LinkedList",
        "Which statement correctly compares ArrayList and LinkedList?",
        [
            "ArrayList gives faster random access (O(1)) via a backing array, while LinkedList is generally better for frequent insertions/removals at the ends",
            "LinkedList gives faster random access than ArrayList",
            "ArrayList cannot store duplicate elements, unlike LinkedList",
            "LinkedList is backed by a resizable array just like ArrayList",
        ],
        0,
        "ArrayList stores elements in a contiguous array, so indexing with get(i) is O(1), "
        "while LinkedList must walk node-by-node to reach an index, making random access "
        "O(n). LinkedList's doubly-linked structure instead makes adding/removing at the "
        "ends cheap without shifting elements.",
    ),
    _q(
        "ArrayList overload confusion",
        "What does this program print?"
        "<pre>import java.util.ArrayList;\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        ArrayList&lt;Integer&gt; list = new ArrayList&lt;&gt;();\n"
        "        list.add(10);\n"
        "        list.add(20);\n"
        "        list.add(30);\n"
        "        list.remove(1);\n"
        "        System.out.println(list);\n"
        "    }\n"
        "}</pre>",
        ["[10, 30]", "[10, 20]", "[20, 30]", "Compile error: ambiguous method call"],
        0,
        "ArrayList has two overloads: remove(int index) and remove(Object o). Since 1 is a "
        "primitive int literal, it resolves to remove(index), deleting the element at index "
        "1 (the value 20) and leaving [10, 30] — not the Integer object equal to 1, which "
        "isn't even in the list.",
    ),
    _q(
        "HashMap basics",
        "Which statement about java.util.HashMap is true?",
        [
            "It permits exactly one null key (and multiple null values) and does not guarantee any iteration order",
            "It does not allow null keys or null values under any circumstance",
            "It always maintains insertion order, like LinkedHashMap",
            "It always maintains keys in sorted order, like TreeMap",
        ],
        0,
        "HashMap allows a single null key plus any number of null values, but because it "
        "organizes entries by hash bucket, the order you iterate over them is unspecified "
        "and can change. Preserving insertion order or sorted order requires LinkedHashMap "
        "or TreeMap respectively.",
    ),
    _q(
        "TreeMap ordering",
        "What does this program print?"
        "<pre>import java.util.TreeMap;\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        TreeMap&lt;Integer, String&gt; map = new TreeMap&lt;&gt;();\n"
        "        map.put(3, \"c\");\n"
        "        map.put(1, \"a\");\n"
        "        map.put(2, \"b\");\n"
        "        System.out.println(map.keySet());\n"
        "    }\n"
        "}</pre>",
        ["[1, 2, 3]", "[3, 1, 2]", "[3, 2, 1]", "Order is undefined, like HashMap"],
        0,
        "TreeMap keeps its entries sorted by key at all times (natural ordering for "
        "Integer), regardless of insertion order, so keySet() always yields [1, 2, 3]. This "
        "is the key difference from HashMap, whose iteration order is unspecified.",
    ),
    _q(
        "ConcurrentModificationException",
        "What happens when this program runs?"
        "<pre>import java.util.*;\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        List&lt;Integer&gt; list = new ArrayList&lt;&gt;(Arrays.asList(1, 2, 3, 4));\n"
        "        for (Integer n : list) {\n"
        "            if (n == 2) list.remove(n);\n"
        "        }\n"
        "    }\n"
        "}</pre>",
        [
            "Throws a ConcurrentModificationException at runtime",
            "Prints normally, list becomes [1, 3, 4]",
            "Prints normally, list stays [1, 2, 3, 4]",
            "Compile error",
        ],
        0,
        "The for-each loop uses an Iterator internally, and structurally modifying the list "
        "(via list.remove) while iterating invalidates that iterator's expected modification "
        "count. The next call to next() detects the mismatch and throws "
        "ConcurrentModificationException; Iterator.remove() should be used instead.",
    ),
    _q(
        "Static variables",
        "What does this program print?"
        "<pre>class Counter {\n"
        "    static int count = 0;\n"
        "    Counter() { count++; }\n"
        "}\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        new Counter();\n"
        "        new Counter();\n"
        "        new Counter();\n"
        "        System.out.println(Counter.count);\n"
        "    }\n"
        "}</pre>",
        ["3", "0", "1", "Compile error"],
        0,
        "A static field belongs to the class as a whole, not to any single instance, so all "
        "three Counter objects increment the same shared count. After three constructions, "
        "count is 3, not reset to 1 for each new object.",
    ),
    _q(
        "Static initialization blocks",
        "What does this program print?"
        "<pre>class Demo {\n"
        "    static { System.out.println(\"static block\"); }\n"
        "    Demo() { System.out.println(\"constructor\"); }\n"
        "}\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        System.out.println(\"main start\");\n"
        "        new Demo();\n"
        "        new Demo();\n"
        "    }\n"
        "}</pre>",
        [
            "main start, static block, constructor, constructor",
            "static block, main start, constructor, constructor",
            "main start, static block, constructor, static block, constructor",
            "static block, constructor, constructor, main start",
        ],
        0,
        "A class is only loaded and initialized on its first active use, so Demo's static "
        "block doesn't run until the first \"new Demo()\" line — after \"main start\" has "
        "already printed. The static block then runs exactly once, followed by a "
        "constructor call each time, so the second new Demo() only prints \"constructor\".",
    ),
    _q(
        "final variables",
        "What does this program print?"
        "<pre>import java.util.*;\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        final StringBuilder sb = new StringBuilder(\"Hi\");\n"
        "        sb.append(\" there\");\n"
        "        System.out.println(sb);\n"
        "    }\n"
        "}</pre>",
        ["Hi there", "Compile error: cannot modify final variable", "Hi", "Runtime exception"],
        0,
        "final only prevents the variable sb from being reassigned to point at a different "
        "object; it says nothing about the object's own mutability. Calling append() mutates "
        "the StringBuilder's internal contents, which is perfectly legal, so it prints "
        "\"Hi there\".",
    ),
    _q(
        "final vs finally vs finalize",
        "Which statement correctly distinguishes final, finally, and finalize()?",
        [
            "final is a modifier that prevents reassignment/overriding/subclassing, finally is a block that always runs after try/catch, and finalize() is a method the garbage collector may call before reclaiming an object",
            "final and finally are interchangeable keywords, and finalize() is a keyword used to close file resources",
            "finally is a modifier, final is a block executed after try/catch, and finalize() starts a new thread",
            "finalize() is automatically invoked before every method call to clean up local variables",
        ],
        0,
        "These three look alike but serve unrelated purposes: final is a keyword/modifier, "
        "finally is a block guaranteeing cleanup code runs, and finalize() is a (now "
        "deprecated) Object method the JVM could call during garbage collection. Confusing "
        "these three is one of the most common traps in Java exams.",
    ),
    _q(
        "Runnable vs Thread",
        "What is the main advantage of implementing Runnable instead of extending Thread to "
        "define a task?",
        [
            "A class implementing Runnable can still extend another class, since Java doesn't support multiple class inheritance",
            "Runnable-based tasks always run faster than Thread subclasses",
            "Only classes that extend Thread can actually be executed by the JVM",
            "Runnable automatically makes the task's methods synchronized",
        ],
        0,
        "Since Java classes can only extend one superclass, extending Thread uses up your "
        "one inheritance slot. Implementing Runnable instead leaves the class free to extend "
        "something else, and the Runnable can still be handed to a Thread object to execute.",
    ),
    _q(
        "synchronized keyword",
        "In this class, what does declaring increment() as <code>synchronized</code> "
        "prevent?"
        "<pre>class Counter {\n"
        "    private int count = 0;\n"
        "    synchronized void increment() { count++; }\n"
        "    int getCount() { return count; }\n"
        "}</pre>",
        [
            "Two threads from executing increment() on the same object at exactly the same time, avoiding a race condition on count",
            "The method from ever throwing an exception",
            "Any other method of the class from ever being called",
            "The class from being instantiated more than once",
        ],
        0,
        "synchronized makes a thread acquire the object's intrinsic lock before entering the "
        "method, so only one thread at a time can execute increment() on a given Counter "
        "instance, preventing lost updates from interleaved count++ operations. It does not "
        "block other, non-synchronized methods like getCount() from running concurrently.",
    ),
]


# ==================================================================== #
# 28. Web Technology Practice — Set 1
# ==================================================================== #
# Set 1: semantic HTML tags, form input types & validation, the box model (padding/border/box-sizing,
# margin collapsing), CSS selector specificity (id/class/element, inline, !important), positioning
# (relative/absolute/fixed/sticky), flexbox (justify-content/align-items), CSS grid, and em/rem/px units.
WEBTECH_PRACTICE_QUESTIONS = [
    _q(
        "Semantic HTML",
        "Which HTML5 semantic element should you use to mark up a self-contained blog post that "
        "could be distributed and read independently (e.g., via an RSS feed)?",
        ["&lt;div&gt;", "&lt;article&gt;", "&lt;section&gt;", "&lt;span&gt;"],
        1,
        "<pre>&lt;article&gt;</pre> represents independent, self-contained content that makes "
        "sense on its own outside the page's context, which is exactly what a syndicated blog "
        "post needs. <pre>&lt;div&gt;</pre> carries no semantic meaning at all, so screen "
        "readers and search engines can't tell what role that content plays.",
    ),
    _q(
        "Semantic HTML",
        "Which tag is the semantically correct choice for wrapping a website's main navigation "
        "menu links?",
        ["&lt;menu&gt;", "&lt;nav&gt;", "&lt;ul&gt;", "&lt;header&gt;"],
        1,
        "<pre>&lt;nav&gt;</pre> explicitly marks a block of primary navigation links, which "
        "helps screen readers and SEO crawlers identify and jump to it. "
        "<pre>&lt;header&gt;</pre> represents introductory content in general, not "
        "specifically a set of navigation links, so it isn't the right fit here.",
    ),
    _q(
        "Semantic HTML",
        "A page has a top section holding the site logo and a bottom section holding copyright "
        "text. Which pair of semantic tags best represents these two sections?",
        [
            "&lt;top&gt; and &lt;bottom&gt;",
            "&lt;head&gt; and &lt;foot&gt;",
            "&lt;header&gt; and &lt;footer&gt;",
            "&lt;div id=\"header\"&gt; and &lt;div id=\"footer\"&gt;",
        ],
        2,
        "<pre>&lt;header&gt;</pre> and <pre>&lt;footer&gt;</pre> are HTML5 semantic elements "
        "purpose-built for introductory and closing page content. Note that "
        "<pre>&lt;head&gt;</pre> is reserved strictly for document metadata (title, meta tags, "
        "links) and cannot hold visible page content, so it can't be reused for this.",
    ),
    _q(
        "Forms",
        "Which input type automatically validates that the entered text looks like a properly "
        "formatted email address, and typically shows an email-optimized keyboard on mobile "
        "devices?",
        [
            "&lt;input type=\"text\"&gt;",
            "&lt;input type=\"email\"&gt;",
            "&lt;input type=\"mail\"&gt;",
            "&lt;input type=\"address\"&gt;",
        ],
        1,
        "<pre>type=\"email\"</pre> triggers the browser's built-in email-format validation and "
        "a mobile-friendly keyboard layout, with no JavaScript required. "
        "<pre>type=\"mail\"</pre> is not a valid HTML input type at all, and "
        "<pre>type=\"text\"</pre> is generic and performs no validation.",
    ),
    _q(
        "Forms",
        "A form needs to let users pick exactly one shipping option out of three choices. Which "
        "input type enforces that only one can be selected at a time, when they all share the "
        "same name attribute?",
        [
            "&lt;input type=\"checkbox\"&gt;",
            "&lt;input type=\"radio\"&gt;",
            "&lt;select multiple&gt;",
            "&lt;input type=\"option\"&gt;",
        ],
        1,
        "Radio buttons sharing the same <pre>name</pre> form a mutually exclusive group, so "
        "selecting one automatically deselects the others. Checkboxes, by contrast, allow "
        "multiple simultaneous selections, which is the opposite of what's needed here.",
    ),
    _q(
        "Forms",
        "Given this field:<pre>&lt;input type=\"text\" name=\"username\" required&gt;</pre>"
        "What happens if a user tries to submit the form while leaving this field empty?",
        [
            "The form submits normally, ignoring the attribute",
            "The browser blocks submission and shows a built-in validation message",
            "A JavaScript error is thrown",
            "The field is silently auto-filled with a default value",
        ],
        1,
        "<pre>required</pre> is native HTML5 form validation: the browser itself blocks "
        "submission and displays a prompt asking the user to fill the field, with no JavaScript "
        "needed. It doesn't throw a script error or invent a default value for you.",
    ),
    _q(
        "Box model",
        "Given this CSS with the default box-sizing:"
        "<pre>.box {\n  width: 200px;\n  padding: 20px;\n  border: 5px solid black;\n}</pre>"
        "What is the box's total rendered width?",
        ["200px", "220px", "230px", "250px"],
        3,
        "With the default <pre>box-sizing: content-box</pre>, the declared width applies only "
        "to the content area, so padding and border are added on top: "
        "200 + (2 x 20 padding) + (2 x 5 border) = 250px. It's a common trap to assume the "
        "declared width already equals the element's final rendered width.",
    ),
    _q(
        "Box model",
        "Using the same rule as before but adding <pre>box-sizing: border-box;</pre>:"
        "<pre>.box {\n  box-sizing: border-box;\n  width: 200px;\n  padding: 20px;\n  "
        "border: 5px solid black;\n}</pre>What is the box's total rendered width now?",
        ["150px", "200px", "230px", "250px"],
        1,
        "<pre>border-box</pre> makes the declared width include the padding and border, so the "
        "element renders at exactly the specified 200px, with the content area shrinking to "
        "fit. This is why frameworks like Bootstrap set border-box globally, to make sizing "
        "more predictable than the content-box default.",
    ),
    _q(
        "Box model",
        "Two sibling &lt;div&gt;s are stacked vertically in normal flow. The first has "
        "margin-bottom: 30px, and the second has margin-top: 20px. What is the actual vertical "
        "gap between them?",
        ["50px", "30px", "20px", "10px"],
        1,
        "Adjacent vertical margins of normal-flow block elements collapse into a single margin "
        "equal to the larger of the two, so the gap is 30px, not their sum. This margin "
        "collapsing behavior applies only to vertical margins in normal flow, never to "
        "horizontal margins or to flex/grid item margins.",
    ),
    _q(
        "CSS specificity",
        "Given:<pre>#title { color: blue; }\n.title { color: red; }\nh1 { color: green; }</pre>"
        "Applied to:<pre>&lt;h1 id=\"title\" class=\"title\"&gt;Hello&lt;/h1&gt;</pre>"
        "What color is the text rendered in?",
        ["green", "red", "blue", "black"],
        2,
        "ID selectors carry more specificity weight (0,1,0,0) than class selectors (0,0,1,0) or "
        "element selectors (0,0,0,1), so <pre>#title</pre>'s blue wins regardless of the order "
        "the rules were written in. Source order only acts as a tiebreaker when specificity is "
        "equal, which isn't the case here.",
    ),
    _q(
        "CSS specificity",
        "An element has an inline style, <pre>style=\"color: blue\"</pre>, and a stylesheet rule "
        "<pre>.text { color: red !important; }</pre> also applies to it. Which color is actually "
        "shown?",
        [
            "Blue, because inline styles always win over stylesheets",
            "Red, because !important overrides even inline styles",
            "It depends purely on source order in the file",
            "Neither applies; the browser falls back to its default color",
        ],
        1,
        "<pre>!important</pre> elevates a declaration above the normal cascade, and it beats "
        "even inline styles, so red wins. Without <pre>!important</pre>, an inline style would "
        "normally outrank any external or internal stylesheet selector, but that rule doesn't "
        "hold once !important is involved.",
    ),
    _q(
        "CSS positioning",
        "An element has <pre>position: relative; top: 10px; left: 10px;</pre>. Relative to what "
        "is it visually offset, and what happens to the space it originally occupied in the "
        "layout?",
        [
            "Offset relative to the nearest positioned ancestor; the original space is removed",
            "Offset relative to its own normal position; the original space is preserved (a gap is left)",
            "Offset relative to the viewport; the original space is removed",
            "It has no visual effect unless a width is also set",
        ],
        1,
        "Relative positioning shifts an element visually away from where it would normally sit, "
        "but it still reserves its original spot in the document flow, leaving a gap behind. "
        "Being offset relative to the nearest positioned ancestor is instead how absolute "
        "positioning behaves, not relative.",
    ),
    _q(
        "CSS positioning",
        "A &lt;div&gt; has <pre>position: absolute; top: 0; right: 0;</pre> and is nested inside "
        "a parent that has <pre>position: relative;</pre>. Where does the div end up?",
        [
            "Pinned to the top-right corner of the browser viewport",
            "Pinned to the top-right corner of its relatively-positioned parent",
            "It stays in normal flow at its original spot",
            "Pinned to the top-right corner of the &lt;body&gt; element, always",
        ],
        1,
        "An absolutely positioned element is placed relative to its nearest ancestor that has a "
        "non-static position value, so here it anchors to the relative parent's box. If no "
        "positioned ancestor existed at all, it would instead fall back to positioning relative "
        "to the initial containing block, roughly the viewport.",
    ),
    _q(
        "CSS positioning",
        "Which CSS position value keeps an element, such as a header bar, pinned to the same "
        "spot on the screen even as the page is scrolled?",
        ["static", "relative", "fixed", "inherit"],
        2,
        "<pre>fixed</pre> positions an element relative to the viewport and removes it from "
        "normal document flow, so it stays visually locked in place while the rest of the page "
        "scrolls beneath it. <pre>static</pre>, the default value, cannot be offset with "
        "top/left/right/bottom at all.",
    ),
    _q(
        "CSS positioning",
        "<pre>position: sticky; top: 0;</pre> is applied to a table header cell inside a "
        "scrollable container. How does it behave as the user scrolls?",
        [
            "It behaves exactly like position: static",
            "It scrolls normally with the page until it reaches the top of its container, then sticks in place",
            "It is always fixed to the top of the browser window, ignoring its container",
            "It is permanently removed from the document flow",
        ],
        1,
        "<pre>sticky</pre> is a hybrid: the element scrolls with its container like a normal "
        "element until it reaches the specified threshold (here, the top), at which point it "
        "sticks in place, but only within the bounds of its own containing block. That "
        "container boundary is what distinguishes it from <pre>fixed</pre>, which is always "
        "anchored to the viewport regardless of its parent.",
    ),
    _q(
        "Flexbox",
        "Given:<pre>.container {\n  display: flex;\n  justify-content: space-between;\n}</pre>"
        "What does justify-content: space-between do to the flex items along the main axis?",
        [
            "Centers all items with no space between them",
            "Places equal space between items, with the first and last items flush against the container edges",
            "Stacks the items vertically instead of horizontally",
            "Adds equal space around every item, including the outer edges",
        ],
        1,
        "<pre>space-between</pre> distributes the remaining free space evenly between items "
        "while pushing the first item flush to the start edge and the last item flush to the "
        "end edge. Adding equal space around every item, including the outer edges, describes "
        "<pre>space-around</pre> instead, which is a different value.",
    ),
    _q(
        "Flexbox",
        "In a flex container with the default <pre>flex-direction: row;</pre>, which property "
        "controls how items align along the cross axis (vertically)?",
        ["justify-content", "align-items", "flex-wrap", "align-self (set on the container)"],
        1,
        "<pre>align-items</pre> controls cross-axis alignment, which is vertical when the main "
        "axis runs horizontally in row direction. <pre>justify-content</pre> instead controls "
        "alignment along the main axis, and <pre>align-self</pre> is applied to individual flex "
        "items, not to the container itself.",
    ),
    _q(
        "CSS Grid",
        "Given:<pre>.grid {\n  display: grid;\n  grid-template-columns: 1fr 2fr 1fr;\n}</pre>"
        "How is the available width divided among the three columns?",
        [
            "Equally, about 33.3% each",
            "The first and third columns get an equal share; the middle column gets twice as much space",
            "Only the first column receives any width at all",
            "The values are ignored unless grid-template-rows is also set",
        ],
        1,
        "The <pre>fr</pre> unit divides the available free space proportionally, and the ratio "
        "1:2:1 means the middle column ends up twice as wide as each outer column. "
        "<pre>grid-template-rows</pre> is a completely independent property and isn't required "
        "for column sizing to take effect.",
    ),
    _q(
        "Layout models",
        "You need to lay out a photo gallery where items must align precisely along both rows "
        "and columns simultaneously, like a spreadsheet grid. Which CSS layout model is "
        "purpose-built for this two-dimensional layout?",
        ["Flexbox", "CSS Grid", "Floats", "Inline-block"],
        1,
        "CSS Grid is explicitly designed for two-dimensional layout, letting you define and "
        "align rows and columns together in one system. Flexbox, in contrast, is fundamentally "
        "one-dimensional, laying items out along a single row or a single column at a time.",
    ),
    _q(
        "CSS units",
        "Given:<pre>html { font-size: 16px; }\n.parent { font-size: 2rem; }\n"
        ".child { font-size: 1.5em; }</pre>Assuming .child is nested inside .parent, what is the "
        "child element's actual computed pixel font size?",
        ["16px", "24px", "32px", "48px"],
        3,
        "<pre>rem</pre> is always relative to the root (&lt;html&gt;) element's font size, so "
        "the parent's 2rem computes to 32px (2 x 16px). <pre>em</pre> on the child is relative "
        "to its own parent's computed font size rather than the root, so 1.5em means "
        "1.5 x 32px = 48px, not 1.5 x 16px, which is the mistake this question is designed to "
        "catch.",
    ),
]


# ==================================================================== #
# 29. Web Technology Practice — Set 2
# ==================================================================== #
# Set 2: var/let/const scoping & hoisting, closures, arrow-function `this` vs regular functions,
# reference vs value semantics, event bubbling & delegation, DOM selection & manipulation,
# JSON.stringify/parse, loose vs strict equality, typeof quirks, the event loop (setTimeout closures,
# microtasks vs macrotasks, async/await ordering), and array method output prediction.
WEBTECH_PRACTICE_QUESTIONS_2 = [
    _q(
        "Scoping",
        "Given this code:<pre>function test() {\n  if (true) {\n    var x = 10;\n  }\n"
        "  console.log(x);\n}\ntest();</pre>What is logged?",
        ["10", "undefined", "ReferenceError: x is not defined", "null"],
        0,
        "<pre>var</pre> is function-scoped rather than block-scoped, so declaring it inside the "
        "<pre>if</pre> block still attaches <pre>x</pre> to the entire function, making it "
        "readable after the block ends. Had <pre>x</pre> been declared with <pre>let</pre> or "
        "<pre>const</pre> instead, it would be confined to the if block and this line would "
        "throw a ReferenceError.",
    ),
    _q(
        "Hoisting",
        "Given this code:<pre>console.log(a);\nvar a = 5;\n\nconsole.log(b);\nlet b = 5;</pre>"
        "What happens when this runs?",
        [
            "Prints undefined, then 5",
            "Prints undefined, then throws a ReferenceError",
            "Throws a ReferenceError immediately on the very first line",
            "Prints 5, then 5",
        ],
        1,
        "<pre>var</pre> declarations are hoisted and pre-initialized to undefined, so reading "
        "<pre>a</pre> before its assignment prints undefined without error. <pre>let</pre> "
        "declarations are hoisted too, but remain in the temporal dead zone until their "
        "declaration line executes, so accessing <pre>b</pre> beforehand throws a "
        "ReferenceError instead of returning undefined.",
    ),
    _q(
        "const semantics",
        "Given this code:<pre>const obj = { a: 1 };\nobj.a = 2;\nobj = { a: 3 };\n"
        "console.log(obj.a);</pre>What happens when this runs?",
        ["Prints 3", "Prints 2", "Prints 1", "TypeError: Assignment to constant variable"],
        3,
        "<pre>const</pre> only locks the variable binding itself, not the contents of the "
        "object it points to, so <pre>obj.a = 2</pre> mutates the object successfully. The "
        "following line, <pre>obj = { a: 3 }</pre>, tries to rebind <pre>obj</pre> to an "
        "entirely new object, which is exactly what const forbids, so it throws a TypeError "
        "before the final console.log ever runs.",
    ),
    _q(
        "Closures",
        "Given this code:<pre>function makeCounter() {\n  let count = 0;\n  return function() {\n"
        "    count++;\n    return count;\n  };\n}\nconst counter = makeCounter();\n"
        "console.log(counter());\nconsole.log(counter());</pre>What is logged?",
        ["1 then 1", "0 then 1", "1 then 2", "undefined then undefined"],
        2,
        "The inner returned function forms a closure over <pre>count</pre>, retaining a live "
        "reference to that same variable across separate calls instead of resetting it each "
        "time. Each call to <pre>counter()</pre> increments that one persistent value, so the "
        "two calls print 1 and then 2.",
    ),
    _q(
        "this binding",
        "Given this code:<pre>const obj = {\n  name: 'Bot',\n"
        "  greetRegular: function () { return this.name; },\n"
        "  greetArrow: () =&gt; { return this.name; }\n};\n"
        "console.log(obj.greetRegular(), obj.greetArrow());</pre>"
        "What is logged (assuming the surrounding top-level this has no name property)?",
        ["Bot Bot", "undefined undefined", "Bot undefined", "undefined Bot"],
        2,
        "A regular function's <pre>this</pre> is determined by how it's called, so "
        "<pre>obj.greetRegular()</pre> binds this to obj, making this.name resolve to 'Bot'. "
        "An arrow function has no this of its own; it lexically captures this from its "
        "surrounding scope at definition time rather than from obj, so this.name there is "
        "undefined.",
    ),
    _q(
        "Reference semantics",
        "Given this code:<pre>const arr1 = [1, 2, 3];\nconst arr2 = arr1;\narr2.push(4);\n"
        "console.log(arr1.length);</pre>What is logged?",
        ["3", "4", "undefined", "TypeError"],
        1,
        "Arrays and objects are assigned by reference in JavaScript, so <pre>arr2 = arr1</pre> "
        "doesn't clone the array, it just points a second variable at the same underlying "
        "array. Mutating it through arr2.push(4) is therefore visible through arr1 too, so "
        "both report a length of 4.",
    ),
    _q(
        "Events",
        "A button is nested inside a &lt;div&gt;, and both have click event listeners attached. "
        "In the default bubbling phase, in what order do the listeners fire when the button is "
        "clicked, and which event method stops the outer div's handler from also running?",
        [
            "Div fires first, then button; stopped with preventDefault()",
            "Button fires first, then div, as the event bubbles up; stopped with stopPropagation()",
            "Only the button's handler ever fires, by default",
            "Div fires first, then button; stopped with stopPropagation()",
        ],
        1,
        "In the default bubbling phase, an event fires on the innermost target first (the "
        "button), then propagates upward through its ancestors (the div). Calling "
        "<pre>event.stopPropagation()</pre> inside the button's handler halts that bubbling; "
        "<pre>preventDefault()</pre> instead cancels a default browser action like a link "
        "navigating, and doesn't affect propagation at all.",
    ),
    _q(
        "Events",
        "A list has 100 &lt;li&gt; items, and more can be added dynamically later. Instead of "
        "attaching a click listener to every &lt;li&gt;, what technique lets a single listener "
        "on the parent &lt;ul&gt; correctly handle clicks on any item, including ones added in "
        "the future?",
        [
            "Event delegation, using event.target inside a single listener on the parent",
            "Inline onclick attributes added to each &lt;li&gt;",
            "A setInterval polling loop checking for clicks",
            "Cloning the entire &lt;ul&gt; node after every update",
        ],
        0,
        "Event delegation relies on bubbling: one listener on the parent inspects "
        "<pre>event.target</pre> to figure out which child was actually clicked, so it "
        "automatically covers items added to the list later too. Attaching a handler to each "
        "existing &lt;li&gt; individually would miss any items created after the handlers were "
        "originally wired up.",
    ),
    _q(
        "DOM selection",
        "What is a key difference between <pre>document.getElementById('x')</pre> and "
        "<pre>document.querySelector('#x')</pre>?",
        [
            "They are functionally and performance-wise identical in every way",
            "getElementById takes a raw ID (no # prefix) and is typically faster; querySelector accepts any CSS selector, making it more flexible but generally a bit slower",
            "querySelector can only select elements by class name, never by ID",
            "getElementById returns an array of matching elements; querySelector returns only one",
        ],
        1,
        "<pre>getElementById</pre> is a specialized, highly optimized lookup that takes just "
        "the bare ID string. <pre>querySelector</pre> accepts the full power of CSS selector "
        "syntax (hence needing the # prefix), which is more versatile but typically has "
        "slightly more overhead. Both actually return a single element (or null), not an "
        "array.",
    ),
    _q(
        "DOM manipulation",
        "Given this code:<pre>const li = document.createElement('li');\n"
        "li.textContent = 'New item';\ndocument.querySelector('ul').appendChild(li);</pre>"
        "What does this code do?",
        [
            "Replaces the entire &lt;ul&gt; with a brand-new &lt;li&gt;",
            "Creates a new &lt;li&gt; element, sets its visible text, and appends it as the last child of the &lt;ul&gt;",
            "Throws an error, because textContent can't be set before the element is appended",
            "Removes all existing &lt;li&gt; elements from the list first",
        ],
        1,
        "<pre>createElement</pre> builds a detached element in memory, <pre>textContent</pre> "
        "safely sets its visible text without any HTML parsing, and <pre>appendChild</pre> "
        "inserts it as the new last child of the selected &lt;ul&gt;. None of the existing "
        "children are touched or removed in the process.",
    ),
    _q(
        "JSON",
        "Given this code:<pre>const data = { name: 'Ann', greet: function(){}, age: undefined, "
        "active: true };\nconsole.log(JSON.stringify(data));</pre>What is logged?",
        [
            '{"name":"Ann","greet":null,"age":null,"active":true}',
            '{"name":"Ann","active":true}',
            '{"name":"Ann","greet":function(){},"age":undefined,"active":true}',
            "An error is thrown because functions can't be serialized",
        ],
        1,
        "<pre>JSON.stringify</pre> silently omits any object property whose value is a "
        "function or undefined, so both greet and age disappear entirely from the output. It "
        "does not throw an error for this, and it only converts functions/undefined to null "
        "when they appear as array elements, not as plain object properties.",
    ),
    _q(
        "JSON",
        "Given this code:<pre>const str = '{\"id\": 1, \"tags\": [\"a\", \"b\"]}';\n"
        "const obj = JSON.parse(str);\nconsole.log(typeof obj, obj.tags[1]);</pre>"
        "What is logged?",
        ["string b", "object b", "object undefined", "TypeError"],
        1,
        "<pre>JSON.parse</pre> converts a valid JSON string into a genuine JavaScript object, "
        "so <pre>typeof obj</pre> is 'object', not 'string'. <pre>obj.tags[1]</pre> then "
        "accesses the second element of the parsed array, which is 'b'. A common mistake is "
        "assuming the result is still a string just because the input was one.",
    ),
    _q(
        "Equality",
        "Given this code:<pre>console.log('5' == 5);\nconsole.log('5' === 5);\n"
        "console.log(null == undefined);\nconsole.log(null === undefined);</pre>"
        "What is logged, in order?",
        [
            "true true true true",
            "false false false false",
            "true false true false",
            "true false false false",
        ],
        2,
        "<pre>==</pre> performs type coercion before comparing, so the string '5' is converted "
        "to a number and matches 5, and null is loosely treated as equal to undefined. "
        "<pre>===</pre> requires both type and value to match with no coercion at all, so "
        "'5' === 5 is false, and null === undefined is also false since they are different "
        "types.",
    ),
    _q(
        "typeof quirks",
        "Given this code:<pre>console.log(typeof null);\nconsole.log(typeof []);\n"
        "console.log(typeof undefined);</pre>What is logged, in order?",
        [
            "'null' 'array' 'undefined'",
            "'object' 'object' 'undefined'",
            "'object' 'array' 'object'",
            "'undefined' 'object' 'undefined'",
        ],
        1,
        "<pre>typeof null</pre> famously returns 'object' due to a long-standing bug baked "
        "into JavaScript from its earliest days, which can't be fixed now without breaking "
        "existing websites. Arrays also report as 'object' via typeof since they're a "
        "specialized kind of object; use <pre>Array.isArray()</pre> if you actually need to "
        "distinguish an array.",
    ),
    _q(
        "Event loop",
        "Given this code:<pre>for (var i = 0; i &lt; 3; i++) {\n"
        "  setTimeout(() =&gt; console.log(i), 0);\n}</pre>What is logged?",
        ["0 1 2", "3 3 3", "0 0 0", "undefined undefined undefined"],
        1,
        "Because <pre>var</pre> is function-scoped, all three scheduled callbacks close over "
        "the exact same <pre>i</pre> variable, and by the time any timer actually fires (after "
        "the whole loop has finished running), i has already reached 3. This is the classic "
        "example used to motivate switching to let, which creates a fresh binding per "
        "iteration.",
    ),
    _q(
        "Event loop",
        "Given this code:<pre>for (let i = 0; i &lt; 3; i++) {\n"
        "  setTimeout(() =&gt; console.log(i), 0);\n}</pre>What is logged?",
        ["3 3 3", "0 1 2", "2 1 0", "undefined undefined undefined"],
        1,
        "<pre>let</pre> creates a new, independent binding of <pre>i</pre> for every loop "
        "iteration, so each scheduled callback closes over its own snapshot of i's value at "
        "that point in time. That produces the intuitive 0, 1, 2 output, unlike the single "
        "shared variable that var produces in the same loop structure.",
    ),
    _q(
        "Event loop",
        "Given this code:<pre>console.log('A');\nsetTimeout(() =&gt; console.log('B'), 0);\n"
        "Promise.resolve().then(() =&gt; console.log('C'));\nconsole.log('D');</pre>"
        "What is logged, in order?",
        ["A B C D", "A D C B", "A D B C", "A C D B"],
        1,
        "All synchronous code runs to completion first, so 'A' and 'D' log immediately, back "
        "to back. Before the event loop moves on to the next macrotask (the setTimeout "
        "callback), it fully drains the microtask queue, where the Promise's .then() callback "
        "lives, so 'C' logs before 'B' even though both were scheduled at roughly the same "
        "time.",
    ),
    _q(
        "Async/await",
        "Given this code:<pre>async function foo() {\n  console.log('1');\n  await null;\n"
        "  console.log('2');\n}\nconsole.log('3');\nfoo();\nconsole.log('4');</pre>"
        "What is logged, in order?",
        ["3 1 2 4", "1 2 3 4", "3 1 4 2", "3 4 1 2"],
        2,
        "Code inside an async function runs synchronously up until its first await, so calling "
        "<pre>foo()</pre> immediately logs '1' before control returns to the caller. The line "
        "right after the call, console.log('4'), then runs synchronously, and only once the "
        "current synchronous script finishes does the microtask queue resume foo() past its "
        "await to log '2' last.",
    ),
    _q(
        "Array methods",
        "Given this code:<pre>const nums = [1, 2, 3];\nconst result1 = nums.map(n =&gt; n * 2);\n"
        "const result2 = nums.forEach(n =&gt; n * 2);\nconsole.log(result1, result2);</pre>"
        "What is logged?",
        ["[2,4,6] [2,4,6]", "[2,4,6] undefined", "undefined [2,4,6]", "[1,2,3] [1,2,3]"],
        1,
        "<pre>map</pre> builds and returns a brand-new array from the callback's return "
        "values, so result1 is [2,4,6]. <pre>forEach</pre> always returns undefined no matter "
        "what its callback returns, because it exists purely for side effects rather than for "
        "constructing a new array.",
    ),
    _q(
        "NaN",
        "Given this code:<pre>console.log(NaN === NaN);\nconsole.log(Number.isNaN(NaN));\n"
        "console.log(Number.isNaN('hello'));</pre>What is logged, in order?",
        ["true true false", "false true false", "false false true", "true false true"],
        1,
        "NaN is the one JavaScript value that is never equal to itself, so "
        "<pre>NaN === NaN</pre> is false. <pre>Number.isNaN()</pre> checks specifically for the "
        "actual NaN value without doing any type coercion, so it correctly returns true only "
        "for real NaN and false for a string like 'hello', unlike the older global isNaN(), "
        "which would coerce 'hello' first.",
    ),
]


# ==================================================================== #
# 30. Web Technology Practice — Set 3
# ==================================================================== #
# Set 3: HTTP methods (GET/POST/PUT/PATCH/DELETE), HTTP status codes (2xx/3xx/4xx), the
# client-server request-response model, cookies vs server-side sessions, localStorage vs
# sessionStorage vs cookies, REST API principles (statelessness, resource/verb mapping),
# HTTP vs HTTPS/TLS, web security concepts (XSS vs CSRF vs SQL injection), and browser rendering
# basics (DOM/CSSOM and the critical rendering path).
WEBTECH_PRACTICE_QUESTIONS_3 = [
    _q(
        "HTTP methods",
        "A search form submits query terms that appear in the URL (e.g., ?q=shoes) and can be "
        "bookmarked or cached. A login form submits a password that should never appear in the "
        "URL or browser history. Which HTTP methods are typically used for these two forms, "
        "respectively?",
        [
            "POST for the search form, GET for the login form",
            "GET for the search form, POST for the login form",
            "GET for both forms",
            "POST for both forms",
        ],
        1,
        "GET requests append data as visible URL query parameters and are cacheable and "
        "bookmarkable, which is ideal for a shareable search. POST instead sends data in the "
        "request body, keeping sensitive values like passwords out of the URL bar and browser "
        "history entirely.",
    ),
    _q(
        "HTTP methods",
        "An API endpoint lets clients update a user record. Sending the entire user object "
        "replaces every field, while sending only {\"email\": \"new@x.com\"} should update just "
        "that one field, leaving the rest untouched. Which HTTP methods correspond to these two "
        "behaviors, respectively?",
        [
            "PATCH for the full replace, PUT for the partial update",
            "PUT for the full replace, PATCH for the partial update",
            "POST for both operations",
            "GET for the full replace, POST for the partial update",
        ],
        1,
        "PUT is defined to replace the entire target resource with the given payload, so any "
        "fields left out are typically wiped or reset. PATCH is designed specifically for "
        "partial modifications, updating only the fields actually included in the request "
        "body.",
    ),
    _q(
        "HTTP methods",
        "Which HTTP method is the conventional choice for a REST API endpoint that removes a "
        "resource, such as an endpoint targeting /users/42?",
        ["GET", "DELETE", "POST", "OPTIONS"],
        1,
        "DELETE is the HTTP verb semantically reserved for removing the resource identified by "
        "the request URL. Using GET to trigger deletion is a well-known anti-pattern, since GET "
        "requests are supposed to be safe and side-effect-free, and browsers or crawlers may "
        "pre-fetch them without warning.",
    ),
    _q(
        "HTTP status codes",
        "A client sends a POST request to create a new article. What status code should the "
        "server return on success to specifically indicate that a new resource was created, "
        "rather than returning a generic success code?",
        ["200 OK", "201 Created", "204 No Content", "202 Accepted"],
        1,
        "201 Created specifically communicates that the request resulted in a brand-new "
        "resource being made, often paired with a Location header pointing to it. 200 OK is a "
        "more generic success code, more typically used for GET requests or updates that don't "
        "create anything new.",
    ),
    _q(
        "HTTP status codes",
        "A company permanently moves a page from /old-page to /new-page and wants search "
        "engines to update their indexes and transfer SEO ranking to the new URL forever. Which "
        "redirect status code should they use?",
        [
            "302 Found (a temporary redirect)",
            "301 Moved Permanently",
            "304 Not Modified",
            "307 Temporary Redirect",
        ],
        1,
        "301 tells both browsers and search engines that the move is permanent, so they should "
        "update their indexes and bookmarks and transfer SEO value to the new URL. 302 and 307 "
        "instead signal a temporary redirect, meaning the original URL should still be treated "
        "as the canonical one going forward.",
    ),
    _q(
        "HTTP status codes",
        "A client requests a user resource that simply doesn't exist, versus a case where a "
        "client sends a malformed JSON body the server can't even parse. Which status codes "
        "correspond to these two situations, respectively?",
        [
            "400 for the missing user, 404 for the malformed body",
            "404 for the missing user, 400 for the malformed body",
            "404 for both situations",
            "500 for both situations",
        ],
        1,
        "404 Not Found means the requested resource simply doesn't exist at that URL. 400 Bad "
        "Request instead signals that the request itself was malformed or invalid, such as "
        "unparsable JSON, meaning the problem is with what the client sent, not with what it "
        "asked for.",
    ),
    _q(
        "HTTP status codes",
        "A user tries to open an admin dashboard. Case A: they aren't logged in at all. Case B: "
        "they're logged in, but their account lacks admin privileges. Which status codes fit "
        "Case A and Case B, respectively?",
        [
            "403 for Case A, 401 for Case B",
            "401 for Case A, 403 for Case B",
            "404 for both cases",
            "401 for both cases",
        ],
        1,
        "401 Unauthorized really means 'unauthenticated': the server doesn't know who this "
        "visitor is yet, matching Case A. 403 Forbidden means the server does know who you are "
        "but you still lack permission for that specific resource, which matches Case B, a "
        "logged-in user without the right privileges.",
    ),
    _q(
        "Client-server model",
        "In the classic client-server model underlying the web, which statement correctly "
        "describes the roles involved?",
        [
            "The server initiates requests to the client, which responds with data",
            "The client sends a request to the server, which processes it and sends back a response",
            "The client and server must run on the same physical machine by definition",
            "The client stores all application logic; the server only stores static files",
        ],
        1,
        "The client, such as a browser, initiates a request, and the server listens for and "
        "processes that request before returning a response; this request-response cycle "
        "underpins HTTP. The two sides are typically separate machines communicating over a "
        "network, not necessarily the same device.",
    ),
    _q(
        "Cookies",
        "A server sets a cookie via a Set-Cookie response header right after a user logs in. "
        "What happens on that user's subsequent requests to the same domain?",
        [
            "The cookie is discarded immediately and is never reused",
            "The browser automatically attaches that cookie to every subsequent request to the matching domain",
            "The user must manually copy the cookie value into each new request",
            "Cookies are only ever sent once, on the single very next request",
        ],
        1,
        "Once set, a cookie is automatically included by the browser in the headers of every "
        "later request to the matching domain, subject to its path, expiry, and security "
        "attributes, which is how servers maintain login state across separate requests. This "
        "automatic re-sending behavior is also exactly what makes cookies a common target for "
        "CSRF attacks.",
    ),
    _q(
        "Sessions vs cookies",
        "In typical server-side session management, what is actually stored on the client (in "
        "a cookie) versus what is stored on the server?",
        [
            "The full user data is stored directly in the cookie; nothing lives server-side",
            "Only a session ID is stored in the cookie; the actual session data lives on the server, keyed by that ID",
            "Sessions and cookies are simply two names for the same technology",
            "The server stores the cookie itself, while the client stores the session ID",
        ],
        1,
        "Typically only a small, opaque session identifier is sent to the browser and stored as "
        "a cookie, while the real session data, such as user info or cart contents, stays on "
        "the server in memory or a database, looked up by that ID. This keeps sensitive data "
        "off the client and limits what's exposed if a request is ever intercepted.",
    ),
    _q(
        "Web storage",
        "A developer wants some data to survive even after the browser tab is closed and "
        "reopened days later, while other data should be cleared as soon as that tab is closed. "
        "Which Web Storage APIs fit these two needs, respectively?",
        [
            "sessionStorage for the persistent data, localStorage for the tab-only data",
            "localStorage for the persistent data, sessionStorage for the tab-only data",
            "Both APIs behave identically and persist forever",
            "Cookies must be used for both cases; Web Storage can't do either",
        ],
        1,
        "<pre>localStorage</pre> data has no expiration and persists across browser restarts "
        "and tab closures until it's explicitly cleared. <pre>sessionStorage</pre> is instead "
        "scoped to a single tab or window and is automatically wiped as soon as that tab "
        "closes.",
    ),
    _q(
        "Web storage",
        "Which of the following is a key difference between localStorage/sessionStorage and "
        "cookies?",
        [
            "Web Storage data is automatically sent to the server with every HTTP request, just like cookies",
            "Web Storage is never sent to the server automatically and typically offers a much larger storage limit than cookies",
            "Cookies can store several megabytes of data; Web Storage is limited to about 4KB",
            "There is no real difference; the two are fully interchangeable",
        ],
        1,
        "Unlike cookies, data placed in localStorage or sessionStorage stays purely on the "
        "client and is never automatically included in HTTP request headers; JavaScript must "
        "explicitly read and send it if the server needs it. Web Storage also typically allows "
        "several megabytes per origin, far more than the roughly 4KB commonly allotted to a "
        "single cookie.",
    ),
    _q(
        "REST APIs",
        "REST APIs are commonly described as 'stateless'. What does that actually mean?",
        [
            "The server keeps no memory of the client between requests; each request must carry all the information needed to process it",
            "The client is never allowed to store any data at all",
            "The API never returns any data, only bare status codes",
            "State must be encoded in the URL path and is never allowed in headers",
        ],
        0,
        "Statelessness means the server doesn't retain any client-specific context between "
        "requests, so each request must be self-contained, typically carrying an auth token or "
        "credentials needed to process it independently of any prior request. This design "
        "improves scalability, since any server instance can handle any incoming request "
        "without needing access to shared session memory.",
    ),
    _q(
        "REST APIs",
        "In a well-designed REST API for a blog, which URL and method combination correctly "
        "follows REST conventions for fetching a single post with ID 7?",
        [
            "POST /getPost?id=7",
            "GET /posts/7",
            "GET /posts/create/7",
            "DELETE /posts/7",
        ],
        1,
        "REST conventions favor nouns (resources) in the URL path, with the HTTP verb itself "
        "conveying the action, so GET /posts/7 cleanly reads as 'retrieve post 7'. Baking a "
        "verb into the URL as well, like /getPost, duplicates responsibility between the URL "
        "and the HTTP method and breaks REST's resource-oriented style.",
    ),
    _q(
        "HTTPS/TLS",
        "What does HTTPS add on top of plain HTTP?",
        [
            "A faster transfer protocol with no security-related changes",
            "A TLS/SSL encryption layer that secures data in transit between client and server",
            "Automatic caching of every response by default",
            "A requirement that all data be transmitted as JSON",
        ],
        1,
        "HTTPS wraps ordinary HTTP traffic inside TLS (formerly called SSL), encrypting data in "
        "transit so eavesdroppers on the network can't read or tamper with it, while also "
        "verifying the server's identity via a certificate. It doesn't alter the underlying "
        "HTTP methods or data formats themselves, only the transport security wrapped around "
        "them.",
    ),
    _q(
        "Web security",
        "An attacker manages to inject a &lt;script&gt; tag into a comment field that later gets "
        "rendered, unescaped, on a page viewed by other users, letting that script steal their "
        "cookies. What is this attack called?",
        [
            "SQL Injection",
            "Cross-Site Scripting (XSS)",
            "Cross-Site Request Forgery (CSRF)",
            "A man-in-the-middle attack",
        ],
        1,
        "XSS involves injecting malicious client-side script into a trusted website so that it "
        "executes inside other users' browsers, which is exactly what happens with an "
        "unescaped comment field like this. It's distinct from CSRF, which tricks a user's "
        "browser into making an unwanted request rather than injecting any executable script "
        "at all.",
    ),
    _q(
        "Web security",
        "A user is logged into their bank in one browser tab. A malicious site open in another "
        "tab silently submits a hidden form to the bank's 'transfer funds' endpoint, and "
        "because the browser automatically attaches the bank's session cookie, the transfer "
        "succeeds without the user's knowledge. What is this attack called?",
        [
            "Cross-Site Scripting (XSS)",
            "SQL Injection",
            "Cross-Site Request Forgery (CSRF)",
            "DNS spoofing",
        ],
        2,
        "CSRF exploits the browser's automatic inclusion of cookies to trick an already "
        "authenticated user's browser into unknowingly submitting a request they never "
        "intended to make. Unlike XSS, CSRF doesn't require injecting any script into the "
        "vulnerable site at all; it simply forges a request that rides along on the victim's "
        "existing session.",
    ),
    _q(
        "Web security",
        "A login form builds a database query by directly inserting user input, like "
        "SELECT * FROM users WHERE username = '&lt;input&gt;'. An attacker enters "
        "' OR '1'='1 as the username and bypasses authentication entirely. What is this "
        "vulnerability called, and what is the standard fix?",
        [
            "XSS; fixed by escaping HTML output",
            "SQL Injection; fixed by using parameterized queries or prepared statements",
            "CSRF; fixed by adding anti-CSRF tokens",
            "Buffer overflow; fixed by limiting input length alone",
        ],
        1,
        "SQL Injection happens when untrusted input is concatenated directly into a SQL query "
        "string, letting an attacker alter the query's actual logic. The standard defense is "
        "parameterized queries, or prepared statements, which treat user input strictly as "
        "data values and never as executable SQL code, regardless of what characters it "
        "contains.",
    ),
    _q(
        "Browser rendering",
        "When a browser loads a page, it parses the HTML into one tree structure and the CSS "
        "into another. What are these two trees called, and how do they combine to produce "
        "what's actually painted on screen?",
        [
            "The DOM (from HTML) and CSSOM (from CSS) combine to form the render tree",
            "Only the DOM is needed; CSS is applied afterward with no separate tree at all",
            "The CSSOM is built first and automatically generates the DOM from it",
            "The render tree is built directly from the raw HTML text, skipping both trees",
        ],
        0,
        "The browser parses HTML into the DOM (Document Object Model) and CSS into the CSSOM "
        "(CSS Object Model) as two separate tree structures, then merges them into the render "
        "tree, which holds only the visible nodes along with their computed styles. Building "
        "both trees independently is necessary because CSS rules can come from many different "
        "sources and must all be resolved before layout can even begin.",
    ),
    _q(
        "Browser rendering",
        "A page includes a large &lt;script&gt; tag, without async or defer, placed in the "
        "&lt;head&gt; before any visible content. How does this typically affect page load, and "
        "why?",
        [
            "It has no effect at all, since scripts always run only after rendering finishes",
            "It blocks HTML parsing and rendering until the script finishes downloading and executing, delaying first paint",
            "It speeds up rendering by pre-loading resources the page will need",
            "It only affects how CSS loads, not HTML parsing",
        ],
        1,
        "A synchronous &lt;script&gt; placed in the head is render-blocking: the browser must "
        "pause HTML parsing entirely, fetch the script, and execute it before it can continue "
        "building the DOM, which delays when content first appears on screen. Adding async or "
        "defer attributes, or simply moving the script to the end of the body, lets parsing "
        "continue in the meantime, improving the critical rendering path.",
    ),
]


PRACTICE_SETS = [
    {
        "id": 4001,
        "slug": "practice-cloud-fundamentals-1",
        "title": "Cloud Fundamentals & Service Models — Set 1",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Cloud Fundamentals"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Cloud Fundamentals · Set 1 of 20 questions</p>
<p>Situational questions on cloud service models, deployment models, scaling, storage and cost —
each poses a short real-world scenario rather than a bare definition. Submit to see your score,
then use <b>View Result</b> to reopen any past attempt with full explanations for every question.</p>
""",
        "hint": "Read each scenario for what it's actually asking for (cost predictability? "
                 "least management overhead? surviving a whole data-center outage?) — the "
                 "distractors are usually real cloud terms that just don't fit this specific need.",
        "boilerplate": {},
        "samples": [],
        "questions": CLOUD_FUNDAMENTALS_QUESTIONS,
    },
    {
        "id": 4002,
        "slug": "practice-cloud-security-1",
        "title": "Cloud Security & Shared Responsibility — Set 1",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Cloud Security"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Cloud Security · Set 1 of 20 questions</p>
<p>Situational questions on the shared responsibility model, IAM, encryption, and cloud-native
security tooling. Submit to see your score, then use <b>View Result</b> to reopen any past attempt
with full explanations for every question.</p>
""",
        "hint": "The shared responsibility model is the single most-tested idea here — for any "
                 "scenario, ask 'was this the provider's job or the customer's, given the service "
                 "model (IaaS/PaaS/SaaS)?' first.",
        "boilerplate": {},
        "samples": [],
        "questions": CLOUD_SECURITY_QUESTIONS,
    },
    {
        "id": 4003,
        "slug": "practice-network-security-1",
        "title": "Network Security — Attacks & Defenses — Set 1",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Network Security"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Network Security · Set 1 of 20 questions</p>
<p>Situational questions on attacks, social engineering, and the defenses that stop them. Submit
to see your score, then use <b>View Result</b> to reopen any past attempt with full explanations
for every question.</p>
""",
        "hint": "First identify what's actually happening in the scenario (an attack? a "
                 "vulnerability? a missing control?), then match it to the term that describes "
                 "that exact thing — many wrong options are real terms for a DIFFERENT attack.",
        "boilerplate": {},
        "samples": [],
        "questions": NETWORK_SECURITY_QUESTIONS,
    },
    {
        "id": 4004,
        "slug": "practice-networking-fundamentals-1",
        "title": "Networking Fundamentals — OSI, Protocols & Ports — Set 1",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Networking Fundamentals"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Networking Fundamentals · Set 1 of 20 questions</p>
<p>Situational questions on OSI layers, TCP/UDP, protocols, ports and subnetting. Submit to see
your score, then use <b>View Result</b> to reopen any past attempt with full explanations for
every question.</p>
""",
        "hint": "For OSI-layer questions, ask what KIND of address or unit is involved (MAC = "
                 "layer 2, IP = layer 3, port = layer 4) — that usually pins down the layer "
                 "immediately.",
        "boilerplate": {},
        "samples": [],
        "questions": NETWORKING_FUNDAMENTALS_QUESTIONS,
    },
    {
        "id": 4005,
        "slug": "practice-devops-containers-1",
        "title": "DevOps & Containers — Set 1",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "DevOps & Containers"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · DevOps & Containers · Set 1 of 20 questions</p>
<p>Situational questions on CI/CD, containers, deployment strategies and operational practice.
Submit to see your score, then use <b>View Result</b> to reopen any past attempt with full
explanations for every question.</p>
""",
        "hint": "Most of these hinge on a specific pain point described in the scenario (slow "
                 "releases, config drift, no rollback plan) — match the practice that solves "
                 "THAT specific pain, not just any DevOps buzzword.",
        "boilerplate": {},
        "samples": [],
        "questions": DEVOPS_CONTAINERS_QUESTIONS,
    },
    {
        "id": 4006,
        "slug": "practice-cloud-fundamentals-2",
        "title": "Cloud Fundamentals & Service Models — Set 2",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Cloud Fundamentals"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Cloud Fundamentals · Set 2 of 20 questions</p>
<p>A second, entirely different set of 20 situational questions — regions, databases, caching,
cost optimization and multi-region architecture. No concept overlaps with Set 1.</p>
""",
        "hint": "Several of these are cost-optimization scenarios (right-sizing, spot instances, "
                 "egress, budget alerts) — a recurring theme in real cloud exams, so it's worth "
                 "being fluent in the vocabulary even beyond this one set.",
        "boilerplate": {},
        "samples": [],
        "questions": CLOUD_FUNDAMENTALS_QUESTIONS_2,
    },
    {
        "id": 4007,
        "slug": "practice-cloud-security-2",
        "title": "Cloud Security & Shared Responsibility — Set 2",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Cloud Security"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Cloud Security · Set 2 of 20 questions</p>
<p>A second, entirely different set of 20 situational questions — PaaS shared responsibility,
account isolation, container security and compliance attestation. No concept overlaps with Set 1.</p>
""",
        "hint": "Notice how many of these are about isolation boundaries at different scales — "
                 "account-level, container-level, key-level. That's the recurring theme worth "
                 "internalizing, not just the individual terms.",
        "boilerplate": {},
        "samples": [],
        "questions": CLOUD_SECURITY_QUESTIONS_2,
    },
    {
        "id": 4008,
        "slug": "practice-network-security-2",
        "title": "Network Security — Attacks & Defenses — Set 2",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Network Security"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Network Security · Set 2 of 20 questions</p>
<p>A second, entirely different set of 20 situational questions — the social-engineering and
attack variants Set 1 didn't cover: smishing, vishing, whaling, BEC, spoofing, malware types and
physical/social techniques. No concept overlaps with Set 1.</p>
""",
        "hint": "Most of Set 2 is naming variants of things you already understand from Set 1 "
                 "(phishing → smishing/vishing/whaling/BEC) — focus on what makes each variant's "
                 "delivery channel or target different, not the underlying idea.",
        "boilerplate": {},
        "samples": [],
        "questions": NETWORK_SECURITY_QUESTIONS_2,
    },
    {
        "id": 4009,
        "slug": "practice-networking-fundamentals-2",
        "title": "Networking Fundamentals — OSI, Protocols & Ports — Set 2",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Networking Fundamentals"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Networking Fundamentals · Set 2 of 20 questions</p>
<p>A second, entirely different set of 20 situational questions — transport/application layers,
POP3 vs IMAP, load-balancing algorithms, jitter, MTU and traceroute. No concept overlaps with Set 1.</p>
""",
        "hint": "A few of these (RTT, jitter, MTU) are precise technical terms that sound similar "
                 "— make sure you can state the one-line distinction between each pair rather "
                 "than relying on a fuzzy sense that they're 'network performance stuff'.",
        "boilerplate": {},
        "samples": [],
        "questions": NETWORKING_FUNDAMENTALS_QUESTIONS_2,
    },
    {
        "id": 4010,
        "slug": "practice-devops-containers-2",
        "title": "DevOps & Containers — Set 2",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "DevOps & Containers"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · DevOps & Containers · Set 2 of 20 questions</p>
<p>A second, entirely different set of 20 situational questions — Kubernetes autoscaling, service
mesh, GitOps, DORA metrics, and testing/reliability practices. No concept overlaps with Set 1.</p>
""",
        "hint": "This set leans more toward measurement and process (DORA metrics, MTTR, alert "
                 "fatigue, environment parity) than tooling — the real exam questions on this "
                 "topic tend to test whether you understand WHY a practice exists, not just its "
                 "name.",
        "boilerplate": {},
        "samples": [],
        "questions": DEVOPS_CONTAINERS_QUESTIONS_2,
    },
    {
        "id": 4011,
        "slug": "practice-cloud-fundamentals-3",
        "title": "Cloud Fundamentals & Service Models — Set 3",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Cloud Fundamentals"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Cloud Fundamentals · Set 3 of 20 questions</p>
<p>A third, entirely different set of 20 situational questions — migration strategy, sharding,
consistency models, messaging patterns and RPO/RTO planning. No concept overlaps with Sets 1-2.</p>
""",
        "hint": "This set drifts into distributed-systems territory (idempotency, circuit "
                 "breakers, consistency models) — these come up in cloud exams because "
                 "cloud-native architecture and distributed systems are the same conversation.",
        "boilerplate": {},
        "samples": [],
        "questions": CLOUD_FUNDAMENTALS_QUESTIONS_3,
    },
    {
        "id": 4012,
        "slug": "practice-cloud-security-3",
        "title": "Cloud Security & Shared Responsibility — Set 3",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Cloud Security"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Cloud Security · Set 3 of 20 questions</p>
<p>A third, entirely different set of 20 situational questions — confidential computing, ABAC,
threat modeling, red/blue/purple teams and governance artifacts. No concept overlaps with Sets 1-2.</p>
""",
        "hint": "A few of these (red/blue/purple team, threat modeling, playbooks) are process "
                 "and organizational concepts rather than technical controls — don't skip them "
                 "assuming only tools get tested.",
        "boilerplate": {},
        "samples": [],
        "questions": CLOUD_SECURITY_QUESTIONS_3,
    },
    {
        "id": 4013,
        "slug": "practice-network-security-3",
        "title": "Network Security — Attacks & Defenses — Set 3",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Network Security"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Network Security · Set 3 of 20 questions</p>
<p>A third, entirely different set of 20 situational questions — wireless/Bluetooth attacks,
credential stuffing vs password spraying, APTs, and the detection/response toolchain (SIEM, EDR,
SOC). No concept overlaps with Sets 1-2.</p>
""",
        "hint": "Credential stuffing vs password spraying is a classic pair the exam loves to "
                 "test as a 'spot the difference' question — know which direction each one "
                 "attacks (many passwords/one account vs one password/many accounts).",
        "boilerplate": {},
        "samples": [],
        "questions": NETWORK_SECURITY_QUESTIONS_3,
    },
    {
        "id": 4014,
        "slug": "practice-networking-fundamentals-3",
        "title": "Networking Fundamentals — OSI, Protocols & Ports — Set 3",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Networking Fundamentals"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Networking Fundamentals · Set 3 of 20 questions</p>
<p>A third, entirely different set of 20 situational questions — the last two OSI layers, TCP's
handshake/teardown mechanics, CIDR, BGP/OSPF, and topology/addressing edge cases. No concept
overlaps with Sets 1-2.</p>
""",
        "hint": "Between Sets 1-3 you've now covered all 7 OSI layers individually — if you can "
                 "state what each layer does in one sentence without looking, that alone "
                 "resolves a large share of networking MCQs.",
        "boilerplate": {},
        "samples": [],
        "questions": NETWORKING_FUNDAMENTALS_QUESTIONS_3,
    },
    {
        "id": 4015,
        "slug": "practice-devops-containers-3",
        "title": "DevOps & Containers — Set 3",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "DevOps & Containers"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · DevOps & Containers · Set 3 of 20 questions</p>
<p>A third, entirely different set of 20 situational questions — Kubernetes-native objects
(namespaces, Ingress, ConfigMaps, Persistent Volumes), SRE practice, and release/observability
depth. No concept overlaps with Sets 1-2.</p>
""",
        "hint": "This set is the most Kubernetes-specific of the three — if K8s isn't actually "
                 "part of your exam's scope, treat it as bonus depth rather than a priority.",
        "boilerplate": {},
        "samples": [],
        "questions": DEVOPS_CONTAINERS_QUESTIONS_3,
    },
    {
        "id": 5001,
        "slug": "practice-pseudocode-1",
        "title": "Pseudocode Practice — Set 1",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Pseudocode"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Pseudocode · Set 1 of 20 questions</p>
<p>Trace basic control-flow pseudocode — if/else-if chains, while/for loop accumulators, nested
loops, compound conditions, boolean flags and digit manipulation — the exact style tested in
TCS/Infosys/Wipro/Accenture technical rounds. Every snippet is shown inline; submit to see your
score, then use <b>View Result</b> to reopen any past attempt with full explanations.</p>
""",
        "hint": "Trace variable values line by line on paper rather than guessing — most wrong "
                 "answers come from an off-by-one loop boundary or missing an else-if branch, "
                 "not from misunderstanding the algorithm.",
        "boilerplate": {},
        "samples": [],
        "questions": PSEUDOCODE_PRACTICE_QUESTIONS,
    },
    {
        "id": 5002,
        "slug": "practice-pseudocode-2",
        "title": "Pseudocode Practice — Set 2",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Pseudocode"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Pseudocode · Set 2 of 20 questions</p>
<p>A second, entirely different set of 20 questions — array & string pseudocode: traversal,
linear/binary search, swapping, one-pass sorting, duplicate detection and classic string
operations (reverse, palindrome, vowel count). No concept overlaps with Set 1.</p>
""",
        "hint": "For search/sort traces, track the actual index variables (i, j, low, high) in a "
                 "small table as you go — it's far more reliable than trying to hold the whole "
                 "trace in your head.",
        "boilerplate": {},
        "samples": [],
        "questions": PSEUDOCODE_PRACTICE_QUESTIONS_2,
    },
    {
        "id": 5003,
        "slug": "practice-pseudocode-3",
        "title": "Pseudocode Practice — Set 3",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Pseudocode"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Pseudocode · Set 3 of 20 questions</p>
<p>A third, entirely different set of 20 questions — recursion (factorial, Fibonacci, GCD, Tower
of Hanoi), stack/queue traces, full sorting-algorithm traces, and time-complexity identification.
No concept overlaps with Sets 1-2.</p>
""",
        "hint": "For recursion questions, draw the call stack rather than trying to trace it "
                 "purely mentally — write down each call as it's made and each value as it "
                 "returns, in order.",
        "boilerplate": {},
        "samples": [],
        "questions": PSEUDOCODE_PRACTICE_QUESTIONS_3,
    },
    {
        "id": 5004,
        "slug": "practice-ms-office-1",
        "title": "MS Office Practice — Set 1 (Word)",
        "difficulty": "Easy",
        "topics": [PRACTICE_SET_TAG, "MS Office"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · MS Office (Word) · Set 1 of 20 questions</p>
<p>The most commonly tested MS Word questions — formatting shortcuts, mail merge, footnotes/TOC/
citations, page setup, track changes and styles. Submit to see your score, then use
<b>View Result</b> to reopen any past attempt with full explanations.</p>
""",
        "hint": "Keyboard shortcuts and feature names are pure recall — if a shortcut question "
                 "trips you up, that's a sign to go memorize the Word shortcut list directly "
                 "rather than reasoning it out.",
        "boilerplate": {},
        "samples": [],
        "questions": MS_OFFICE_PRACTICE_QUESTIONS,
    },
    {
        "id": 5005,
        "slug": "practice-ms-office-2",
        "title": "MS Office Practice — Set 2 (Excel)",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "MS Office"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · MS Office (Excel) · Set 2 of 20 questions</p>
<p>A second, entirely different set of 20 questions — Excel formulas and functions (VLOOKUP,
HLOOKUP, IF, SUM, SUMIF/COUNTIF), absolute vs relative references, pivot tables, conditional
formatting and charts. No concept overlaps with Set 1.</p>
""",
        "hint": "For formula questions, read the exact arguments in order (lookup value, range, "
                 "column index, exact/approximate match) — most wrong answers swap two arguments "
                 "or get the TRUE/FALSE match flag backwards.",
        "boilerplate": {},
        "samples": [],
        "questions": MS_OFFICE_PRACTICE_QUESTIONS_2,
    },
    {
        "id": 5006,
        "slug": "practice-ms-office-3",
        "title": "MS Office Practice — Set 3 (PowerPoint & Outlook)",
        "difficulty": "Easy",
        "topics": [PRACTICE_SET_TAG, "MS Office"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · MS Office (PowerPoint & Outlook) · Set 3 of 20 questions</p>
<p>A third, entirely different set of 20 questions — PowerPoint (Slide Master, transitions vs
animations, Presenter View), Outlook (To/CC/BCC, rules, scheduling) and cross-app basics (file
formats, OneDrive co-authoring, shortcuts). No concept overlaps with Sets 1-2.</p>
""",
        "hint": "A few of these are shared across the whole Office suite (Ctrl+P, F12, Ctrl+Z) "
                 "rather than app-specific — don't assume every shortcut question is about the "
                 "app named in the title.",
        "boilerplate": {},
        "samples": [],
        "questions": MS_OFFICE_PRACTICE_QUESTIONS_3,
    },
    {
        "id": 5007,
        "slug": "practice-oops-1",
        "title": "OOPs Practice — Set 1 (Four Pillars)",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "OOPs"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · OOPs · Set 1 of 20 questions</p>
<p>The four pillars of OOP — encapsulation, abstraction, inheritance and polymorphism — with
scenario questions that ask you to identify which pillar is being demonstrated. Submit to see
your score, then use <b>View Result</b> to reopen any past attempt with full explanations.</p>
""",
        "hint": "Encapsulation and abstraction get confused constantly — encapsulation is about "
                 "HIDING internal state (private fields), abstraction is about hiding "
                 "IMPLEMENTATION complexity behind a simple interface. Ask which one the "
                 "scenario is really about.",
        "boilerplate": {},
        "samples": [],
        "questions": OOPS_PRACTICE_QUESTIONS,
    },
    {
        "id": 5008,
        "slug": "practice-oops-2",
        "title": "OOPs Practice — Set 2 (Class Mechanics)",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "OOPs"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · OOPs · Set 2 of 20 questions</p>
<p>A second, entirely different set of 20 questions — constructors (default/parameterized/copy),
overloading vs overriding, access modifiers, static vs instance members, and <code>this</code>/
<code>super</code>. No concept overlaps with Set 1.</p>
""",
        "hint": "Overloading is resolved at compile time by the method signature; overriding is "
                 "resolved at runtime by the actual object type — that one distinction answers "
                 "most of this set.",
        "boilerplate": {},
        "samples": [],
        "questions": OOPS_PRACTICE_QUESTIONS_2,
    },
    {
        "id": 5009,
        "slug": "practice-oops-3",
        "title": "OOPs Practice — Set 3 (Advanced)",
        "difficulty": "Hard",
        "topics": [PRACTICE_SET_TAG, "OOPs"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · OOPs · Set 3 of 20 questions</p>
<p>A third, entirely different set of 20 questions — abstract classes vs interfaces, the diamond
problem, composition vs inheritance, overriding rules (covariant returns, <code>final</code>) and
object lifecycle. No concept overlaps with Sets 1-2.</p>
""",
        "hint": "For the diamond-problem style questions, remember most mainstream OOP languages "
                 "block multiple inheritance of classes specifically, while still allowing a "
                 "class to implement multiple interfaces.",
        "boilerplate": {},
        "samples": [],
        "questions": OOPS_PRACTICE_QUESTIONS_3,
    },
    {
        "id": 5010,
        "slug": "practice-java-1",
        "title": "Java Practice — Set 1 (Syntax & Operators)",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Java"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Java · Set 1 of 20 questions</p>
<p>Core syntax output-prediction questions — primitive ranges & casting, operators (%, ++/--,
&&/||, bitwise) and control statements including switch fall-through. Every snippet is shown
inline; submit to see your score, then use <b>View Result</b> for full explanations.</p>
""",
        "hint": "For every output-prediction snippet, trace it on paper line by line rather than "
                 "eyeballing it — pre vs post increment and operator precedence are exactly where "
                 "eyeballing goes wrong.",
        "boilerplate": {},
        "samples": [],
        "questions": JAVA_PRACTICE_QUESTIONS,
    },
    {
        "id": 5011,
        "slug": "practice-java-2",
        "title": "Java Practice — Set 2 (OOP in Java)",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Java"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Java · Set 2 of 20 questions</p>
<p>A second, entirely different set of 20 questions — inheritance & <code>super</code>,
overloading vs overriding, interfaces vs abstract classes, and exception handling
(try/catch/finally execution order, checked vs unchecked). No concept overlaps with Set 1.</p>
""",
        "hint": "For try/catch/finally output questions, remember finally always runs — even "
                 "after a return in the try or catch block — trace the actual execution order, "
                 "don't assume return exits immediately.",
        "boilerplate": {},
        "samples": [],
        "questions": JAVA_PRACTICE_QUESTIONS_2,
    },
    {
        "id": 5012,
        "slug": "practice-java-3",
        "title": "Java Practice — Set 3 (Core Library & Gotchas)",
        "difficulty": "Hard",
        "topics": [PRACTICE_SET_TAG, "Java"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Java · Set 3 of 20 questions</p>
<p>A third, entirely different set of 20 questions — String immutability & the string pool
(<code>==</code> vs <code>.equals()</code>), autoboxing, Collections basics, the classic
<code>static</code>/<code>final</code>/<code>finally</code>/<code>finalize</code> mix-up, and
basic multithreading. No concept overlaps with Sets 1-2.</p>
""",
        "hint": "== vs .equals() on Strings is the single most-repeated Java exam question across "
                 "every company — know exactly when string literals share a pooled instance and "
                 "when 'new String(...)' breaks that.",
        "boilerplate": {},
        "samples": [],
        "questions": JAVA_PRACTICE_QUESTIONS_3,
    },
    {
        "id": 5013,
        "slug": "practice-web-technology-1",
        "title": "Web Technology Practice — Set 1 (HTML & CSS)",
        "difficulty": "Easy",
        "topics": [PRACTICE_SET_TAG, "Web Technology"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Web Technology · Set 1 of 20 questions</p>
<p>HTML & CSS fundamentals — semantic tags, form input types, the box model, selector
specificity, positioning and flexbox/grid basics. Submit to see your score, then use
<b>View Result</b> to reopen any past attempt with full explanations.</p>
""",
        "hint": "Specificity questions are won by counting selector types in order (inline > ID > "
                 "class/attribute/pseudo-class > element) — don't guess by which rule 'looks' "
                 "more specific.",
        "boilerplate": {},
        "samples": [],
        "questions": WEBTECH_PRACTICE_QUESTIONS,
    },
    {
        "id": 5014,
        "slug": "practice-web-technology-2",
        "title": "Web Technology Practice — Set 2 (JavaScript & DOM)",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Web Technology"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Web Technology · Set 2 of 20 questions</p>
<p>A second, entirely different set of 20 questions — var/let/const scoping & hoisting, closures,
<code>this</code> binding in arrow vs regular functions, DOM manipulation, and async ordering
(callbacks, promises, microtasks vs macrotasks). No concept overlaps with Set 1.</p>
""",
        "hint": "For async output-order questions, remember the priority: synchronous code first, "
                 "then all queued microtasks (Promise callbacks), then macrotasks (setTimeout) — "
                 "trace it in that order, not the order things appear in the source.",
        "boilerplate": {},
        "samples": [],
        "questions": WEBTECH_PRACTICE_QUESTIONS_2,
    },
    {
        "id": 5015,
        "slug": "practice-web-technology-3",
        "title": "Web Technology Practice — Set 3 (Protocols & Architecture)",
        "difficulty": "Medium",
        "topics": [PRACTICE_SET_TAG, "Web Technology"],
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p class="text-muted">Practice Set · Web Technology · Set 3 of 20 questions</p>
<p>A third, entirely different set of 20 questions — HTTP methods & status codes, the
client-server model, cookies vs sessions vs local/sessionStorage, REST basics, HTTPS/TLS, and
web security concepts (XSS/CSRF/SQL injection). No concept overlaps with Sets 1-2.</p>
""",
        "hint": "Status code questions are won by knowing the hundred-range meaning first (2xx "
                 "success, 3xx redirect, 4xx client error, 5xx server error) before worrying "
                 "about the exact number.",
        "boilerplate": {},
        "samples": [],
        "questions": WEBTECH_PRACTICE_QUESTIONS_3,
    },
]
