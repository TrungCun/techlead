import uuid
from datetime import datetime
from ecommerce.cart import Cart, CartItem
from ecommerce.payments import PaymentMethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ecommerce.users import Customer
from ecommerce.payments import PaymentMethod

class OrderItem:
    '''
    A class represents an item in an order.
    Demonstrates Composition
    '''
    def __init__(self, product_id: str, name: str, quantity: int, frozen_price: float):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.frozen_price = frozen_price  # price at the time of order

    def get_subtotal(self) -> float:
        return self.frozen_price * self.quantity

class Order:
    '''
    status and info of an order
    '''
    def __init__(self, customer: 'Customer', shipping_address: str):
        self.order_id = str(uuid.uuid4())
        self.customer = customer
        self.shipping_address = shipping_address
        self.created_at = datetime.now()

        # Composition
        self.items: list[OrderItem] = []
        self.total_amount: float = 0.0

        # encapsulation
        self._status: str = "PENDING" # (PENDING, PAID, SHIPPED, CANCELLED)

    @property
    def status(self) -> str:
        # getter for status
        return self._status

    @staticmethod
    def create_from_cart(cart: Cart, customer: 'Customer') -> 'Order':
        '''
        factory method to create order from customer's cart
        '''
        order = Order(customer.user_id, customer.shipping_address)

        for cart_item in cart.items:
            order_item = OrderItem(
                product_id=cart_item.product.product_id,
                name=cart_item.product.name,
                quantity=cart_item.quantity,
                frozen_price=cart_item.product.price
            )
            order.items.append(order_item)

        order.total_amount = cart.calculate_total()
        return order

    def process_payment(self, payment_method: PaymentMethod):
        '''
        process payment for the order
        '''
        print(f"oder {self.order_id}: processing payment...")
        if payment_method.process(self.total_amount):
            self.mark_as_paid()
        else:
            print("Payment failed.")

    # Encapsulation
    def mark_as_paid(self):
        if self._status != "PENDING":
            self._status = "PAID"
            print(f"Order {self.order_id} marked as PAID.")
        else:
            print(f"Order {self.order_id} cannot be marked as PAID from status {self._status}.")

    def marked_as_shipped(self):
        if self._status == "PAID":
            self._status = "SHIPPED"
            print(f"Order {self.order_id} marked as SHIPPED.")
        else:
            print(f"Order {self.order_id} cannot be marked as SHIPPED from status {self._status}.")
    def __str__(self):
      item_list = "\n".join(f"  - {item.name} (x{item.quantity})" for item in self.items)
      return(
          f"Order ID: {self.order_id}\n"
          f"Status: {self.status}\n"
          f"Total Amount: {self.total_amount:,.0f} VND\n"
          f"List Items:\n{item_list}"
      )