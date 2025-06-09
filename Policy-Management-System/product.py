# Class to represent an insurance product
class Product:
    def __init__(self, product_id, name, price, active=True):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("price must be non-negative numeric.")
        
        # Initialize product with ID, name, price, and status
        self.product_id = product_id
        self.name = name
        self.price = price
        self.active = active

    def update(self, name=None, price=None):
        # Update the price and name of the product
        if price is not None and price < 0:
            raise ValueError("Price cannot be negative.")
        if name:
            self.name = name
        if price:
            self.price = price
            
    def suspend(self):
        # Mark the product as inactive (suspended)
        if not self.active:
            raise Exception("Product is already suspended.")
        self.active = False
    
    def activate(self):
        self.active = True

    def __str__(self):
        # Return a string summary of a product
        status = "Active" if self.active else "Suspended"
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Status: {status}"