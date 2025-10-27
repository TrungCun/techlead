import uuid
from abc import ABC, abstractmethod

class Product(ABC):
  '''
  A base class represents a common product in an e-commerce system.
  Demonstrates ABSTRACTION
  '''
  def __init__(self, name: str, price: str):
      '''
      contructor function for a product
      args:
        name: str : name of the product
        price: float : price of the product
      '''
      self.product_id = str(uuid.uuid4())

      self.name = name
      self.price = price

  # Encapsulation
  @property
  def price(self):
      # getter method for price
      return self._price

  @price.setter
  def  price(self, new_price:float):
    #  setter method for price
     if new_price < 0:
        raise ValueError("Price cannot be negative")
     self._price = new_price

  def get_prodcut_id(self) -> str:
      '''
      getter method for id, only reading id
      do not create setter for id to prevent changing id
      '''
      return self._product_id


  @abstractmethod
  def calculate_shipping_cost(self) -> float:
     pass

  def __str__(self):
     return f"{self.name} - Giá: {self.price:,.0f} VND"

  def __repr__(self):
     return f"Product(name='{self.name}', price={self.price})"


class PhysicalProduct(Product):
    '''
    A class represents a physical product in an e-commerce system.
    Demonstrates INHERITANCE
    '''
    def __init__(self, name: str, price: float, weight: float, stock: int):
      super().__init__(name, price)
      self.weight = weight  # in kg
      self._stock = stock

    @property
    def stock(self) -> int:
        return self._stock

    def decrease_stock(self, quantity: int):
        if quantity > self._stock:
            raise ValueError("Not enough stock available for: {self.name}")
        self._stock -= quantity

    def calculate_shipping_cost(self) -> float:
    #  Polymorphism, shipping cost calulation base on weight
        return self.weight * 10000


class DigitalProduct(Product):
    '''
      A class represents a digital product in an e-commerce system.
      Demonstrates INHERITANCE
    '''
    def __init__(self, name: str, price: float, download_link: str):
      super().__init__(name, price)
      self.download_link = download_link

    def calculate_shipping_cost(self) -> float:
      return 0.0