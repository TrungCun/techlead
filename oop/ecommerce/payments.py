from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    '''
    A base class represents a payment method in an e-commerce system.
    Demonstrates ABSTRACTION
    '''
    @abstractmethod
    def process(self, amount: float) -> bool:
        # process payment , return true if successful, false otherwise
        pass

class CreditCardPayment(PaymentMethod):
    # concrete implementation
    def __init__(self, card_number: str, expiry: str, cvv: str):
        self.card_number = card_number
        self.expiry = expiry
        self.cvv = cvv
        print("CreditCardPayment initialized")

    def process(self, amount: float) -> bool:
        print(f"Processing credit card payment of {amount:,.0f} VND by {self.card_number[-4:]}...")
        return True

class CODPayment(PaymentMethod):
    def process(self, amount: float) -> bool:
        print(f"Processing Cash on Delivery payment of {amount:,.0f} VND...")
        return True