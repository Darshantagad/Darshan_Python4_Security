# Project 6: Automated Security Incident Logger
# Logic: Writing data to the Operating System for Audit Trails

def log_incident(message):
    # 'a' stands for Append (adds to the end)
    # 'with' ensures the file is saved properly even if the computer crashes
    with open("seccurtiy_logs.txt", "a") as log_file:
        log_file.write(f"[SECURITY ALERT] {message}\n")
        
    print(f"Success: Incident '{message}' has been recorded.")    
    
log_incident("Brute force attack detected on Port 22")
log_incident("Unencrypted S3 Bucket created by user: Admin_D")
log_incident("Database access requested from unauthorized IP: 192.168.5.5")