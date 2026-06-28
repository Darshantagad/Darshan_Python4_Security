# Project 10: Real-world TCP Port Scanner
# Logic: Using low-level sockets to check real network states

# 'localhost' means your own computer. This is a safe loopback address: 127.0.0.1

import socket 

target_host = "localhost"
# Common ports to scan on a local Windows machine
# 135 = Microsoft RPC (usually open on Windows), 443 = HTTPS website traffic

ports_to_scan = [135, 443, 8080]
print(f"--- INITIATING NETWORK INTEL ON: {target_host} ---")

for port in ports_to_scan:
    
# 1. Create a socket object
    # AF_INET = Specifies IPv4 addresses. SOCK_STREAM = Specifies TCP connections.
    
    scanner_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # CRITICAL: If a port is closed, don't freeze the script. Give up after 1.5 seconds
    scanner_socket.settimeout(1.5)
    
    
    # connect_ex() attempts the connection. 
    # It returns 0 if successful. It returns an error number if it fails.
    
    result = scanner_socket.connect_ex((target_host, port))
    
    if result == 0:
        print(f"[!] ALERT: Port {port} is live and OPEN on this machine!")
    else:
        print(f"[INFO]: Port {port} is closed or filtered.")
        
    scanner_socket.close()
print("--- NETWORK DISCOVERY COMPLETED ---")
