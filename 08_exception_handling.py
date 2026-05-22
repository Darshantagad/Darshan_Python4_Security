# Project 8: Bulletproof Security Log Parser
# Logic: Using Exception Handling to protect scripts from unexpected runtime crashes

# Simulating a raw stream of data coming from a cloud firewall log.
# Notice that the third entry is bad data (a text string instead of a valid numeric port)

raw_log_stream = ["80", "443", "MALICIOUS_TEXT_INJECTION", "22", "3389"]

print("---INITIALIZING LOG PARSER PARADIGM ---")

for log_entry in raw_log_stream:
    try:
        # Risky Operation: Trying to convert text to an integer port number.
        # This will fail spectacularly on line 3!
        parsed_port = int(log_entry)
        
        if parsed_port == 22 or parsed_port == 3389:
            print(f"[ALERT]: High-risk port {parsed_port} detected in stream.")
            
        else:
            print(f"[INFO]: Port {parsed_port} processed normally.")
            
    except ValueError as error_details:
        print(f"\n[CRITICAL ERROR HANDLED]: Parsing failed for entry '{log_entry}'.")
        print(f"Reason: {error_details}")
        print("Action: Malicious entry isolated. Continuing system stream execution...\n")

print("--- STREAM PARSING COMPLETED SUCCESSFULLY ---")