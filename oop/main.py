'''
file running e-commerce system
'''
from ecommerce.products import PhysicalProduct, DigitalProduct
from ecommerce.users import Customer, Admin
from ecommerce.payments import CreditCardPayment, CODPayment
from ecommerce.services import CheckoutService

def run_simulation():
  print('1:admin create products')
  admin = Admin('admin1', 'adminhash')

  book = PhysicalProduct('OOP book', price = 250000, weight = 0.5, stock= 100)
  ebook = DigitalProduct('E-book OOP', price = 150000, download_link='http://downloadlink.com/oop')

  admin.add_product(book.name, book.price)
  admin.add_product(ebook.name, ebook.price)

  print('2:customer login and shopping')
  customer = Customer('customer1', 'customerhash', '123 A St')
  customer.login()

  # add to cart
  customer.add_to_cart(book, quantity=2)
  customer.add_to_cart(ebook, quantity=1)

  # customer view cart
  customer.view_cart()


  print('3: checkout and payment')
  credit_card = CreditCardPayment(card_number = '1234-5678-9012-3456', expiry = '12/25', cvv = '123')

  order = CheckoutService.process_checkout(customer, credit_card)
  print('4: checking staus after payment')
  print(order)

  print(f"Number of items in the shopping cart: {len(customer.cart)}")

  print('5: admin ship order')
  admin.ship_order(order)
  print('status last order: {order.status}')


if __name__ == "__main__":
  run_simulation()