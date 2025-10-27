# ecommerce/cart.py

from ecommerce.products import Product, PhysicalProduct


'''
cart has - a cart item
cart item has - a product
'''
class CartItem:
    '''
    A class represents an item in the shopping cart.
    Demonstrates Composition
    '''

    def __init__(self, product: Product, quantity: int):
        self.product = product # CartItem has - a Product
        self.quantity = quantity

    def get_subtotal(self) -> float:
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} x {self.quantity} - Thành tiền: {self.get_subtotal():,.0f} VND"


class Cart:
    '''
    A class represents a shopping cart.
    Demonstrates Composition  and Encapsulation
    '''

    def __init__(self):
        '''
        Use dict for quick access by product_id
        '''
        self._items: dict[str, CartItem] = {}

    @property
    def items(self) -> list[CartItem]:
        #  getter return a list of cart items
        return list(self._items.values())

    def add_item(self, product: Product, quantity: int = 1):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        # Check cart (physical products only)
        if isinstance(product, PhysicalProduct):
            current_quantity_in_cart = self._items.get(product.product_id, CartItem(product, 0)).quantity

        if product.product_id in self._items:
            self._items[product.product_id].quantity += quantity
        else:
            self._items[product.product_id] = CartItem(product, quantity)

        print(f"Added {quantity} of {product.name} to cart.")

    def calculate_total(self) -> float:
        # caculate total price of cart
        return sum(item.get_subtotal() for item in self._items.values())

    def clear(self):
        #  clear all items in cart after payment
        self._items.clear()

    def __len__(self):
        return len(self._items)