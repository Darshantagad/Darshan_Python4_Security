# Project 3: Threat Intelligence & Asset Management
# Logic: Using Lists to store multiple "Bad Actors"


# 1. LIST: Our Threat Intel Feed (The Blacklist)
blacklist = ["192.168.1.10", "10.0.0.5", "172.16.0.100"]



# 2. DICTIONARY: Cloud Asset Inventory
# Format: "Name": "IP Address"
assets = {
    "Web-Gateway": "192.168.1.1",
    "Database": "10.0.0.5",
    "backup-Storage": "172.16.0.50"
}
# 3. LOGIC: Checking for a "Breach"

target_asset = "Database"
asset_ip = assets[target_asset] #ip from the dictionary

print(f"---SCANNING ASSET: {target_asset} ({asset_ip})---")
if asset_ip in blacklist:
    print(f"CRITICAL: {target_asset} is communnicating with a BLACKLISTED IP!")
else:
    print(F"CLEAN: No malicious activity detected on {target_asset}.")
    
# LIST: Common insecure ports targeted in Cloud environments
suspicious_ports = [21, 22, 23, 3389]
# VARIABLE: The port being scanned right now
current_port = 22

if current_port in suspicious_ports:
    print(f"[ALERT] Port {current_port} is open! Insecure Protocol Detected!")
else:
    print(f"[INFO] Port {current_port} is not on the high-risk list.")