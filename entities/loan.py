class Loan:
    def __init__(self, loan_amount, amount_paid, monthly_payments):
        self.loan_amount = loan_amount
        self.amount_paid = amount_paid
        self.monthly_payments = monthly_payments
        self.amount_left = self.loan_amount - self.amount_paid
