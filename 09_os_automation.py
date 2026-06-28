# Project 9: Automated OS Ping Scanner
# Logic: Using the 'subprocess' module to execute live operating system comm

import subprocess
# the target We want to test(GPDNS)
target_host = "8.8.8.8"

print(f"--- LAUNCHING OS INTEGRATION: PINGING {target_host} ---")

#Executing a real system command via python
# Windows Note: '-n 2' tells Windows to send exactly 2 ping packets instead of 4 (saves time)
# Linux/Mac Note: If you were on Linux, you would use '-c 2' instead of '-n 2'


command_result = subprocess.run(["ping", "-n", "2", target_host], capture_output=True, text=True)
# The OS returns a 'returncode'. 0 means 'Success', anything else means 'Failed'

if command_result.returncode == 0:
    print(f"[SUCCESS]: Host {target_host} is reachable and responding!")
    # Printing the actual raw text that came back from the Windows Command Prompt
    print("\n--- RAW OS OUTPUT ---")
    print(command_result.stdout)
    
else: 
    print(f"[CRITICAL]: Host {target_host} is unreachable or blocking our packets.")