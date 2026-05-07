#Project 1: Cloud Asset Metadata (Project 1: The Asset Identifier)
# Logic : Using variables to store infrastructure data

server_name =  "Cloud-Vault-01"
ip_address = "192.168.1.50" #private IP
open_ports = 3
is_secure = True # security status

print(f"--- ASSET REPORT----")
print(f"Name:{server_name} | IP: {ip_address}")
print(f"Security Status:{is_secure}")

