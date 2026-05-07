# Project 4: Automated Port Scanner Simulator
# Logic: Using Loops to iterate through network ranges
# Networking Note: These are ports currently running services
# 22 = SSH, 80 = HTTP, 443 = HTTPS, 3306 = MySQL

active_ports = [22, 80, 443, 3306]
print("--- CLOUD SECURITY SCAN STARTING ---")


# The Algorithm: Scan the common port range (1 to 1024)
# We use range(1, 1025) because the stop number is not included.

for port in range(1, 1025):
    if port in active_ports:
        print(f"[!] DANGER: Port {port} is OPEN in this instance!")
        
    print("--SCAN COMPLETE --")