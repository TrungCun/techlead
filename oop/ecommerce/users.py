
import uuid
from abc import ABC
from ecommerce.cart import Cart
from ecommerce.products import Product
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ecommerce.orders import Order

class User(ABC):
    '''
    A base class represents a user in an e-commerce system.
    '''
    def __init__(self, username: str, password_hash: str):
        self._user_id = str(uuid.uuid4())
        self.username = username
        self._password_hash = password_hash  # Encapsulation

    @property
    def user_id(self) -> str:
        return self._user_id

    def login(self) -> bool:
        # dummy login function
        print(f"User {self.username} logged in.")
        return True

class Customer(User):
    '''
    A class represents a customer in an e-commerce system.
    Demonstrates INHERITANCE
    '''
    def __init__(self, username: str, password_hash: str, shipping_address: str):
        super().__init__(username, password_hash)
        self.shipping_address = shipping_address

        self.cart = Cart()  # Composition

    def add_to_cart(self, product: Product, quantity: int = 1):
        # Note: This will raise an OutOfStockError if the cart.add_item fails.
        # You may want to add try...except here later.
        self.cart.add_item(product, quantity)

    def view_cart(self):
        if not self.cart.items:
            print("Cart is empty.")
            return

        for item in self.cart.items:
            print(f"- {item.product.name} (x{item.quantity}): {item.get_subtotal():,.0f} VND")

        print('total cart:', self.cart.calculate_total())

class Admin(User):
    '''
    A class represents an admin in an e-commerce system.
    Demonstrates INHERITANCE
    '''

    def __init__(self, username: str, password_hash: str):
        super().__init__(username, password_hash)

    def add_product(self, product_name: str, price: float):
        print(f"Admin {self.username} add '{product_name}'.")

    def ship_order(self, order: 'Order'):
        print(f"Admin {self.username} shipped order {order.order_id}.")

        order.marked_as_shipped()