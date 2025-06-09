# Class to manage policyholder information and actions
class Policyholder:
    def __init__(self, policyholder_id, name, email, active=True):
        # Validate input types
        if not isinstance(name, str) or not isinstance(email, str):
            raise ValueError("Invalid input for Policyholder initialization.")
        
        # Initialize a policyholder with ID, name, email, and status
        self.policyholder_id = policyholder_id
        self.name = name
        self.email = email
        self.active = active
        self.products = []  # List of products registered by the policyholder
        self.payments = []  # List of payments made by the policyholder
    
    def suspend(self):
        #Suspend the policyholder's account
        if not self.active:
            raise Exception(f"Policyholder {self.policyholder_id} is already suspended.")
        self.active = False
    
    def reactivate(self):
        # Reactivate a suspended policyholder's account
        if self.active:
            raise Exception(f"Policyholder {self.policyholder_id} is already active.")
        else:
            self.active = True
    
    def register_product(self, product):
        # Add a product to the policyholder's list of registered products
        if product in self.products:
            raise Exception("Product already registered.")
        if not product.active:
            raise Exception("Cannot register a suspended product.")
        self.products.append(product)
    
    def add_payment(self, payment):
        self.payments.append(payment) # Record a payment in the policyholder's payment history
    
    def __str__(self):
        status = "Active" if self.active else "Suspended"
        return (f"ID: {self.policyholder_id}, Name: {self.name}, Email: {self.email}, Status: {status}, "
                f"Products: {[p.name for p in self.products]}, Payments: {[p.amount for p in self.payments]}")