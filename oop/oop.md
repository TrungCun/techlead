# OOP (Object Oriented Programming)

OOP là viết tắt của Object-oriented programming (lập trình hướng đối tượng). OOP là một mô hình lập trình dựa trên khái niệm Object (đối tượng).

## 1: Các thành phần
Trong OOP sẽ bao gồm 2 thành phần chính là Class và Object:

### 1.1: Class
Class (lớp) trong OOP là các template hay cấu trúc để phục vụ cho việc xây dựng nên các Object (đối tượng). Trong đó sẽ bao gồm một tập hợp các Attribute và Methods để  định nghĩa các đặc tính và hành vi cho các Object.
Ví dụ về một class:
```
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
```
- Attributes: định nghĩa các thông tin, đặc điểm cũng như các thuộc tính của Object.
- Methods: định nghĩa các hành vi, phương thức cũng như các hành động thường có của Object.

### 1.2: Object
Methods: định nghĩa các hành vi, phương thức cũng như các hành động thường có của Object.

Ví dụ về object book của class PhysicalProduct và ebook của DigitalProduct
```
  book = PhysicalProduct('OOP book', price = 250000, weight = 0.5, stock= 100)
  ebook = DigitalProduct('E-book OOP', price = 150000, download_link='http://downloadlink.com/oop')
```

## 2: Project minh họa OOP
Cấu trúc project
```
oop/
├── ecommerce/
│   ├── __init__.py
│   ├── products.py
│   ├── users.py
│   ├── cart.py
│   ├── orders.py
│   ├── payments.py
│
├── main.py
├── oop.md
```
ecommerce/ chứa mã nguồn các class và logic nghiệp vụ.
main.py => script chạy thử project.

Workflow:
- Một admin tạo ra các đối tượng PhysicalProduct và DigitalProduct.
- Một Customer đăng nhập. Nhận một đối tượng Cart trống.
- Customer gọi customer.add_to_cart(). Lớp Cart tạo ra một CartItem() và thêm vào danh sách _items của nó.
- Hệ thống tạo một đối tượng Order mới, sao chép các CartItem thành các OrderItem (để "đóng băng" giá và sản phẩm tại thời điểm mua).
- Order gọi phương thức process() của đối tượng PaymentMethod được chọn.
- Nếu thành công, order.mark_as_paid() được gọi.
- Một Admin xem danh sách các đơn hàng "PAID" và gọi order.ship_order().
- Trạng thái đơn hàng chuyển thành SHIPPED.
## 2: Các đặc tính quan trọng.
### 2.1: Encapsulation

Encapsulation là một kỹ thuật lập trình nền tảng được sử dụng để gom nhóm các attributes và methods cần thiết vào một Object. Kỹ thuật này còn được biết với tên gọi khác là Data/Information Hiding.

Data Hiding trong lập trình hướng đối tượng OOP thường dùng để bảo vệ các thành phần bên trong của Object (thường gọi là private). Các thành phần bên ngoài sẽ không được can thiệp và sử dụng các thành phần này trực tiếp mà phải thông qua các phương thức công khai (public).

Với các thành phần được ẩn đi trong class, cần có phương thức để giao tiếp với chúng => sử dụng setter và getter.

- Getter: Cung cấp quyền chỉ đọc(read-only) cho thuộc tính. Return giá trị của thuộc tính.
 - Ví dụ về Getter:
 ```
   def price(self):
      # getter method for price
      return self._price
 ```
- Setter: Cung cấp quyền ghi(write) vào một thuộc tính. Kiểm soát giá trị đầu vào bằng những điều kiện.
- Ví dụ về Setter:
```
  @price.setter
  def  price(self, new_price:float):
    #  setter method for price
     if new_price < 0:
        raise ValueError("Price cannot be negative")
     self._price = new_price
```
### 2.2: Abstraction

Abstraction trong lập trình hướng đối tượng OOP là một kỹ thuật lập trình dùng để đơn giản hoá cấu trúc của chương trình, tập trung vào những phần quan trọng và có ý nghĩa. Những phần phức tạp sẽ được loại bỏ hay ẩn giấu đi (hiding).

ABC (Abstract Base Class) và @abstractmethod là cách thức thực thi đặc tính này trong python.

Ví dụ về Abstraction:
```
class PaymentMethod(ABC):
    '''
    A base class represents a payment method in an e-commerce system.
    Demonstrates ABSTRACTION
    '''
    @abstractmethod
    def process(self, amount: float) -> bool:
        # process payment , return true if successful, false otherwise
        pass
```
Lớp CheckoutService (hoặc lớp Order) cần xử lý thanh toán. Tuy nhiên, logic nghiệp vụ cấp cao này không nên quan tâm đến việc thanh toán được xử lý như thế nào. Nó không cần biết về API của cổng thanh toán thẻ tín dụng, hay quy trình của COD.

### 2.3: Inheritance

Inheritance trong lập trình hướng đối tượng OOP là một cơ chế xây dựng class mới dựa trên các class đã có. Các class kế thừa sẽ bao gồm toàn bộ các attributes và methods từ base class (lớp cơ sở) hay parent class (lớp cha).

Sử dụng Inheritance sẽ giúp các nhà phát triển tái sử dụng được các class đã có, giảm thiểu các duplication (sự trùng lặp) không cần thiết.

Ví dụ về tính Inheritance. Class PhysicalProduct là lớp con của class Product.
```
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
```

Inheritance trong OOP bao gồm 2 loại chính:
- Single Inheritance (đơn kế thừa): class chỉ có thể kế thừa từ một parent class duy nhất.
- Multiple inheritance (đa kế thừa): class có thể kế thừa từ nhiều parent class.

### 2.4: Polymorphism

Polymorphism trong lập trình hướng đối tượng OOP cho phép một Object có thể có nhiều hình dạng và hành vi khác nhau.

Bản chất từ Polymorphism cấu tạo từ 2 chữ Hy Lạp: "poly" nghĩa là nhiều và "morph" nghĩa là hình dạng. Từ đó Polymorphism có thể tạm dịch là "đa hình".

Polymorphism trong OOP được chia làm 2 loại:

- Static Polymorphism (đa hình tĩnh): là cơ chế định nghĩa lại các methods cùng tên, nhưng có thể khác số lượng hoặc kiểu của tham số. Static Polymorphism còn được gọi là Method Overloading.

- Dynamic Polymorphism (đa hình động): là cơ chế định nghĩa lại các methods cùng tên, cùng tham số và kiểu trả về từ parent class. Dynamic Polymorphism còn được gọi là Method Overriding.

Sự khác biệt lớn nhất giữa Static và Dynamic Polymorphism là: Static Polymorphism được xử lý tại thời điểm biên dịch (compile-time). Dynamic Polymorphism được xử lý tại thời điểm chạy chương trình (runtime).

Ví dụ về tính Polymorphism:
```
class PaymentMethod(ABC):
    '''
    A base class represents a payment method in an e-commerce system.
    Demonstrates ABSTRACTION
    '''
    @abstractmethod
    def process(self, amount: float) -> bool:
        # process payment , return true if successful, false otherwise
        pass
```
 - PaymentMethod là một interface (lớp trừu tượng) định nghĩa phương thức process(). => Các lớp con CreditCardPayment và CODPayment cung cấp các cách triển khai đa hình là các phương thức thanh toán khác nhau.
 ```

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
 ```

## 3: Một vài khái niệm quan trọng.
### 3.1: Contructor
Trong OOP, constructor (hay hàm khởi tạo) là một phương thức (method) rất đặc biệt bên trong một lớp (class). Nó sẽ tự động được gọi ngay tại thời điểm bạn tạo ra một đối tượng (instance) mới từ lớp đó

Nhiệm vụ của nó là khởi tạo các giá trị ban đầu cho các thuộc tính của đối tượng.

Ví dụ về một constructor:
```
    def __init__(self, card_number: str, expiry: str, cvv: str):
        self.card_number = card_number
        self.expiry = expiry
        self.cvv = cvv
        print("CreditCardPayment initialized")
```

Và cách nó được khởi tạo khi đối tượng được tạo.
```
  print('3: checkout and payment')
  credit_card = CreditCardPayment(card_number = '1234-5678-9012-3456', expiry = '12/25', cvv = '123')
```

### 3.2: Self
Self là một tham số (parameter) đại diện cho chính đối tượng (instance) đang gọi phương thức đó. Với ý tưởng đơn giản là tự tham chiếu đến chính bản thân nó.

```
def __init__(self, product_id: str, name: str, quantity: int, frozen_price: float):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.frozen_price = frozen_price  # price at the time of order

    def get_subtotal(self) -> float:
        return self.frozen_price * self.quantity
```
Các self.name, self.quantity nhằm tự tham chiếu tới các biến name và quantity trong phương thức. nhằm phân biệt với các name và quantity được truyền vào trong hàm.

### 3.3: S.O.L.I.D
SOLID trong lập trình hướng đối tượng là tập hợp các nguyên lý thiết kế phần mềm nhằm giúp lập trình viên tạo ra các hệ thống dễ bảo trì, dễ mở rộng và có tính ổn định. Các nguyên lý này bao gồm: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation và Dependency Inversion.

#### 3.3.1: Single Responsibility Principle (SRP)

Single Responsibility Principle (SRP) là nguyên lý đầu tiên của SOLID trong lập trình hướng đối tượng, ý nghĩa của nó có thể được hiểu như sau:

- Mỗi lớp (class) trong chương trình chỉ nên có một trách nhiệm duy nhất.
- Hay nói cách khác, một lớp chỉ nên có một lý do duy nhất để thay đổi.
 => khi thiết kế một class, nó chỉ nên có một tác dụng duy nhất nhằm giúp mã nguồn dễ hiểu, đơn giản, dễ duy trì và mở rộng hơn.

```
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
```

Lớp CheckoutService chỉ đảm nhiệm 1 nhiệm vụ duy nhất. Điều phối quy trình thanh toán.

Nó nhận Customer và PaymentMethod, sau đó gọi Order.create_from_cart(), order.process_payment(), và cart.clear()

Lớp Customer không tự xử lý checkout, lớp Order cũng không. CheckoutService gánh trách nhiệm "điều phối" này, giúp các lớp khác (như Customer, Order, Cart) giữ được đơn trách nhiệm của chúng.

#### 3.3.2: O - Open/Closed Principle (Nguyên tắc Đóng/Mở)

Open/Closed Principle (OCP) đề cập đến cách thiết kế phần mềm sao cho nó có thể mở rộng bằng cách thêm các tính năng mới mà không cần phải sửa đổi mã nguồn hiện có. Điều này giúp cho mã nguồn ổn định hơn, tránh việc sửa đổi dẫn đến lỗi không mong muốn.

Hệ thống của bạn "đóng" với việc sửa đổi CheckoutService. Lớp CheckoutService chỉ làm việc với PaymentMethod (một abstraction).

#### 3.2.3: Liskov Substitution Principle

Nguyên lý Liskov Substitution Principle (LSP) được đặt tên theo nhà khoa học máy tính Barbara Liskov và nó nói rằng: Các đối tượng của một lớp con phải có thể thay thế cho các đối tượng của lớp cha mà không làm thay đổi tính đúng đắn của chương trình.

Các lớp Product  Lớp CartItem được thiết kế để nhận một đối tượng Product (def __init__(self, product: Product, ...)). hoặc một ví dụ khác là CreditCardPayment và CODPayment đều có thể thay thế cho PaymentMethod trong CheckoutService.

#### 3.3.3: Interface Segregation Principle
Interface Segregation Principle (ISP) là một nguyên lý giúp đảm bảo rằng các lớp không bị ép buộc phải triển khai các phương thức mà chúng không sử dụng. Nói cách khác, thay vì tạo ra một giao diện lớn (fat interface) với nhiều phương thức mà không phải tất cả các lớp đều cần, bạn nên tách nó ra thành các interface nhỏ hơn, mỗi interface chỉ có những phương thức liên quan đến một nhóm nhiệm vụ cụ thể.

Lớp User không ép tất cả các hành vi vào lớp User. Thay vào đó, chúng ta tách biệt:

- Customer có add_to_cart(), view_cart().

- Admin có add_product(), ship_order().

#### 3.3.4: Dependency Inversion Principle

Dependency Inversion Principle (DIP) là nguyên lý cuối cùng trong SOLID, nó nhấn mạnh việc giảm sự phụ thuộc giữa các module cấp cao và module cấp thấp trong hệ thống bằng cách sử dụng các abstraction (lớp trừu tượng hoặc interface) thay vì các concretion (cụ thể, chi tiết triển khai).

CheckoutService và PaymentMethod:

- Module cấp cao: CheckoutService (chứa logic nghiệp vụ).

- Module cấp thấp: CreditCardPayment (chứa chi tiết kỹ thuật về cách xử lý thẻ).