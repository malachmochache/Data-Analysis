from datetime import date, datetime

# Class to represent a payment made by a policyholder
class Payment:
    def __init__(self, amount, due_date):
        if amount <= 0:
            raise ValueError("amount must be greater than zero.")
        if not isinstance(due_date, date):
            raise TypeError("due_date must be a date object.")
        
        # Initialize payment with amount, and dates
        self.amount = amount
        self.due_date = due_date
        self.paid = False
        self.paid_date = None

    def process_payment(self, date_paid):
        if not isinstance(date_paid, date):
            raise TypeError("date_paid must be a date object.")
        if self.paid:
            raise Exception("Payment has already been processed.")
        self.paid = True
        self.paid_date = date_paid
    
    def is_late(self):
        # Determine if the payment is/was overdue
        cdate = self.paid_date if self.paid else datetime.now().date()
        return cdate > self.due_date
    
    def get_penalty(self):
         return self.amount * 0.05 if self.is_late() else 0.0
    
    def reminder(self):
        if not self.paid:
            return f"Reminder: Payment of ${self.amount} is due by {self.due_date}"
        return "Payment already completed."
    
    def __str__(self):
        status = "Paid" if self.paid else "Pending"
        return f"Amount: {self.amount}, Status: {status}, Due Date: {self.due_date} Penalty: {self.get_penalty()}"
