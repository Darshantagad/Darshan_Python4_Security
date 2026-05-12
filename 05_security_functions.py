# Project 5: Modular Security Auditor
# Logic: Using Functions to create reusable security tools


def run_security_audit(server_name, active_ports):
    print(f"\n---- Starting Audit for: {server_name}---")
    
    for port in active_ports:
        if port == 22:
            print(f"[!] CRITICAL: SSH (Port 22) is open on {server_name}!")
        elif port == 80:
            print(f"[?] WARNING: Unencrypted HTTP (Port 80) found on {server_name}.")
        else:
            print(f"[OK] Port {port} is active.")    
            
#calling the func 
web_ports = [80, 443]
db_ports = [22, 3306]  

run_security_audit("Production-Web-UI", web_ports)
run_security_audit("Backend-Database", db_ports)