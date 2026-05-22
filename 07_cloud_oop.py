# Project 7: Cloud Infrastructure Compliance Auditor (OOP)
# Logic: Using Classes to model real cloud resources dynamically


#Constructor : SEts up the traits for the every new server we createclass CloudServer:
    
class CloudServer:
    # The Constructor: Sets up the traits for every new server we create
    def __init__(self, name, ip, iam_role, is_public):
        self.name = name
        self.ip = ip
        self.iam_role = iam_role
        self.is_public = is_public

    # Method: An action this cloud server object can take or evaluate
    def audit_security(self):
        print(f"\n[AUDITING]: Evaluating policy for {self.name} ({self.ip})...")
        
        # Algorithmic Policy Check: Public servers should NEVER have Admin roles
        if self.is_public and self.iam_role == "Admin":
            print(f"[CRITICAL VIOLATION]: {self.name} is PUBLIC and has ADMIN access!")
        else:
            print(f"[COMPLIANT]: {self.name} meets organizational security standards.")

# --- USING THE BLUEPRINT (Instantiating Objects) ---

# Creating Object 1: A risky web application server
web_server = CloudServer("Prod-Web-App", "54.210.4.19", "Admin", is_public=True)

# Creating Object 2: A protected backend database server
db_server = CloudServer("Prod-Backend-DB", "10.0.1.5", "Database-Read-Write", is_public=False)

# Triggering our automated security audit rules
web_server.audit_security()
db_server.audit_security()
    

