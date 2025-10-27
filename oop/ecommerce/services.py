from ecommerce.users import Customer
from ecommerce.payments import PaymentMethod
from ecommerce.orders import Order

class CheckoutService:
  @staticmethod
  def process_checkout(customer: Customer, payment_method: PaymentMethod) -> Order:
      '''
      process checkout for a customer using a payment method
      '''
      print(f"\nStart Checkout for {customer.username}")
      cart = customer.cart

      if not cart.items:
          print("Cart is empty. Cannot proceed to checkout.")
          return None

      # create order from cart
      order = Order.create_from_cart(cart, customer)

      # process payment
      order.process_payment(payment_method)

      cart.clear()  # clear cart after checkout
      print(f"Checkout completed for {customer.username}. Order ID: {order.order_id}\n")

      return order