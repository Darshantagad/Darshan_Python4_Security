# Python for Cloud Security Learning
What: A script that stores data about a server (IP, Name, Status).

Why: In Cloud Security, you can't protect what you can't identify.

Where: Used in "Inventory Management" in AWS/Azure.

How: By assigning strings, integers, and booleans to clear variable names.

The Algorithm & Flowchart
Start

Input: Define server details.

Process: Combine data into a readable string.

Output: Display the "Audit Report."

End

Add: git add . (Gather both new files).

Commit: git commit -m "Added Asset ID and Firewall Logic projects"

Push: git push


Project 2: The Logic Gate Firewall (Medium)
Goal: Master "Conditionals" (Branching) to block "Bad Actors."

1. 3W1H
What: An if/else logic gate that checks an incoming IP.

Why: This is how firewalls (like AWS Security Groups) decide to allow or drop traffic.

Where: At the edge of every cloud network.

How: Using comparison operators (==).

2. The Algorithm & Flowchart

Start

Input: Define a banned_ip. Get an incoming_ip.

Decision (Diamond): Does incoming_ip == banned_ip?

YES: Output "BLOCK" and log it.

NO: Output "ALLOW."


Project 3 (Medium): The Threat Intel Inventory

1. 3W1H: Lists & Collections
What: A List is an ordered sequence of items (like a row of lockers). A Dictionary is a collection of "Key-Value" pairs (like a real dictionary: Word -> Definition).

Why: In Cloud Security, a "Blacklist" contains thousands of bad IPs. You cannot create a variable for each one (ip1, ip2, ip3). You put them all in one List.

Where: Every AWS "Security Group" is essentially a list of rules.

How: Lists use square brackets []. Dictionaries use curly braces {}.

2. OS & Networking: What is a "Subnet"?
Before the project, you need to understand the "Map."

3W1H: A Subnet is a small slice of a larger network.

Logic: Imagine a building. The building is the Network. The "Accounting Dept" on the 2nd floor is a Subnet.

Security: You often want to block an entire Subnet (e.g., "Block everyone on the 2nd floor") rather than one person.

3. The Algorithm: The "Threat Intelligence Scanner"
Start.

Define a List of known_malware_ips.

Define a Dictionary of server_status (e.g., "Web-Server": "Online").

Input: Get an IP to check.

Decision (Diamond): Is the IP IN the list?

YES: Alert!

NO: Proceed.