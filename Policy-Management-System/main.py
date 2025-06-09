from policyholder import Policyholder
from product import Product
from payment import Payment
from datetime import datetime, timedelta

def main():
    try:
        # Create two sample insurance products
        life = Product(101, "Life Insurance", 1000)
        health = Product(102, "Health Insurance", 1500)

        # Create two policyholders
        john = Policyholder(1, "John Doe", "john@example.com")
        jane = Policyholder(2, "Jane Smith", "jane@example.com")
        
        # Register products with error handling
        try:
            john.register_product(life)
            jane.register_product(health)
        except Exception as e:
            print(f"Error while registering product: {e}")
        
        # Create payment records
        # One is past due, one is future due
        pay1 = Payment(1000, datetime.now().date() - timedelta(days=5))  # Past due
        pay2 = Payment(1500, datetime.now().date() + timedelta(days=5)) # Future due

        # Process the payments
        try:
            pay1.process_payment(datetime.now().date())
            pay2.process_payment(datetime.now().date())
        except Exception as e:
            print(f"Payment processing error: {e}")
        
        # Assign payments to each policyholder
        john.add_payment(pay1)
        jane.add_payment(pay2)
        
        # Display each policyholder's account details
        print("=== Policyholder Accounts ===")
        print(john)
        print(jane)
        # Display payment information
        print("\n=== Payment Info ===")
        print(pay1)
        print(pay2)

    except Exception as main_error:
        print(f"An error occurred: {main_error}")

if __name__ == "__main__":
    main()