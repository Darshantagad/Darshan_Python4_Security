# Project 2: Mini Firewall Logic
# Logic: Branching based on networking data

banned_ip = "10.0.0.5"
incoming_ip = input("Enter incoming IP address: ")

# The Logic Gate

if incoming_ip == banned_ip:
    print("[ALERT] Connection blocked! This IP is malicious.")
else:
    print("[Safe] Connecton allowed. Traffic passed.")