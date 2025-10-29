# Stacks

Stack là một danh sách có thứ tự trong đó việc chèn và xóa được thực hiện ở một đầu, được gọi là top - đỉnh. Phần tử cuối cùng được chèn là phần tử đầu tiên sẽ bị xóa. Do đó, nó được gọi là Last in First out (LIFO) hoặc First in Last out (FILO) list.

Các phép toán cơ bản và độ phức tạp thời gian:
- push(element): Thêm một phần tử vào đỉnh (top) của stack. $O(1)$
- pop(): Xóa và trả về phần tử ở đỉnh của stack.$O(1)$
- top()): Trả về phần tử ở đỉnh stack mà không xóa nó. $O(1)$
- isEmpty(): Kiểm tra xem stack có rỗng không (trả về true/false).$O(1)$
- size(): Trả về số lượng phần tử hiện có trong stack. $O(1)$

## Stacks Implementation

### Simple Array Implementation
Sử dụng một mảng (array) để lưu trữ các phần tử. Một biến được dùng để theo dõi chỉ số của phần tử trên cùng.

Ưu: Hiệu suất truy cập (Cache Locality) cao. Các phần tử nằm liền kề nhau trong bộ nhớ, giúp CPU truy cập nhanh hơn do cơ chế cache.

Nhược: Kích thước cố định, không thể tăng thêm kích thước cho stacks nếu cần.

### Dynamic Array Implementation
Cải thiện độ phức tạp quá trình resize bằng cách sử dụng kỹ thuật nhân đôi mảng. Nếu mảng đã đầy, hãy tạo một mảng mới có kích thước gấp đôi và sao chép các mục.

### Linked List Implementation

Cách khác để triển khai ngăn xếp là sử dụng Danh sách liên kết. Thao tác push được thực hiện bằng cách chèn phần tử vào đầu danh sách. Hoạt động pop được thực hiện bằng cách xóa nút từ đầu (the header/top node).

Các thao tác push() và pop() thực hiện tại đầu head của linked list.

Ưu: Kích thước động kích thước stack có thể tăng hoặc giảm linh hoạt, chỉ bị giới hạn bởi bộ nhớ hệ thống. Không bao giờ xảy ra "overflow" do đầy mảng.

## The Call Stack (Ngăn xếp cuộc gọi hàm)
- Mỗi khi một hàm được gọi (ví dụ funcA() gọi funcB()), một "Stack Frame" (khung ngăn xếp) chứa các biến cục bộ, địa chỉ trả về, và tham số của hàm đó sẽ được push vào Call Stack.
- Khi hàm funcB() thực thi xong, stack frame của nó được pop ra, và quyền điều khiển quay trở lại funcA() tại địa chỉ đã lưu.

## Các thuật toán có áp dụng.

Duyệt đồ thị theo chiều sâu (Depth-First Search - DFS): Sử dụng một stack để theo dõi các đỉnh cần thăm. Cố găng đi sâu nhất có thể trước khi quay lui.

Các bài toán Backtracking (Quay lui): Stack (thường là Call Stack) được dùng để lưu trạng thái hiện tại. Khi đi vào ngõ cụt, nó "quay lui" (pop trạng thái) và thử nhánh khác.

445-503

# Queue
Hàng đợi là một danh sách có thứ tự trong đó việc thêm được thực hiện ở một đầu (phía sau) và việc xóa được thực hiện ở đầu kia (phía trước). Phần tử đầu tiên được thêm là phần tử đầu tiên sẽ bị xóa. Do đó, nó được gọi là First in First out (FIFO) hoặc Last in Last out (LILO).

Các phép toán cơ bản:
- enqueue(element) (hoặc add): Thêm một phần tử vào cuối (rear/tail) của hàng đợi.

- dequeue() (hoặc poll, remove): Xóa và trả về phần tử ở đầu (front/head) của hàng đợi.

- peek() (hoặc front()): Trả về phần tử ở đầu hàng đợi mà không xóa nó.

- isEmpty(): Kiểm tra xem hàng đợi có rỗng không.

- size(): Trả về số lượng phần tử.

## Queue Implementation
### Linked List-based Queue

Đây là cách triển khai "chuẩn" và dễ hiểu nhất để đạt được $O(1)$ cho mọi thao tác.

Cơ chế: Dùng danh sách liên kết (thường là liên kết đơn) và duy trì hai con trỏ: head (front) và tail (rear).

### Array-based Queue
Triển khai với array/list thông thường => gặp vấn đề với việc lấy ra phần tử pop(). Khi pop(0), các phần tử còn lại trong mảng phải dịch sang trái một đơn vị => tốn nhiều tài nguyên và thời gian.

=> Cải tiến với Hàng đợi vòng (Circular Queue / Ring Buffer).

 Cơ chế:
 - Sử dụng một mảng có kích thước cố định (N). Dùng hai chỉ số (index) là front và rear. Thay vì dịch chuyển phần tử, ta dịch chuyển các chỉ số này.
 - Khi front hoặc rear đi đến cuối mảng, nó sẽ "quay vòng" lại đầu mảng.


 Ưu điểm: Hiệu suất $O(1)$ cho cả hai thao tác. Tận dụng cache (cache locality) tốt hơn linked list.

 Nhược điểm: Kích thước cố định. Phải xử lý logic "đầy".

 ## Các thuật toán có áp dụng.
### Thuật toán tìm kiếm theo chiều rộng (Breadth-First Search - BFS)
BFS dùng để duyệt đồ thị (graph) hoặc cây (tree) theo từng "cấp độ".
Cơ chế:
- Bắt đầu từ một đỉnh start, enqueue nó vào Queue.
- Khi Queue còn phần tử, dequeue một đỉnh u.
- enqueue tất cả các hàng xóm v của u (mà chưa được thăm) vào Queue.

=>Queue đảm bảo rằng bạn duyệt hết các đỉnh ở "cấp 1" (hàng xóm của start) trước khi bạn duyệt các đỉnh ở "cấp 2" (hàng xóm của hàng xóm).

225-387

# Hashing

Hashing là một kỹ thuật được sử dụng để lưu trữ và truy xuất thông tin càng nhanh càng tốt. Nó được sử dụng để thực hiện các tìm kiếm tối ưu.

Các thành phần chính:
- Hash Table
- Hash Functions
- Collisions(Xung đột - xảy ra khi các giá trị giống nhau được tạo ra từ các dữ liệu nguồn khác nhau)
- Collision Resolution Techniques(Kỹ thuật giải quyết xung đột)

## Hash table
Hash table là một tổng quát của mảng. Với mảng, ta lưu phần tử có key là k tại vị trí k của mảng. Điều đó có nghĩa là, cho trước một khóa k, chúng ta tìm thấy phần tử có khóa k bằng cách chỉ tìm ở vị trí thứ k của mảng

## Hash function
Hash Function được sử dụng để chuyển đổi key thành index. Lý tưởng nhất là hash function nên ánh xạ từng khóa có thể tới một vị trí index duy nhất.

Với một tập hợp các phần tử, hash function ánh xạ từng mục vào một vị trí duy nhất được gọi là perfect hash function(hàm băm hoàn hảo). Tuy nhiên sẽ rất khó và tốn tài nguyên để thực hiện. Trong thực tế ta chỉ cần đảm bảo xử lý được xung đột mà không cần tạo được một hashing hoàn hảo.

=> Mục tiêu của chúng ta là tạo ra một hàm băm giảm thiểu số lần collisions(xung đột), dễ tính toán và phân bổ đồng đều các phần tử trong bảng băm.

## Collisions

Các hàm băm được sử dụng để ánh xạ từng key tới một không gian địa chỉ khác nhau, nhưng thực tế không thể tạo một hàm băm như vậy và vấn đề được gọi là collision(xung đột). Xung đột là tình trạng hai bản ghi được lưu trữ ở cùng một vị trí.

## Collision Resolution
Va chạm xảy ra khi hai khóa khác nhau $k_1 \neq k_2$ nhưng lại được băm vào cùng một vị trí: $h(k_1) = h(k_2)$. Đây là điều không thể tránh khỏi (theo Nguyên lý chuồng bồ câu) khi số lượng khóa $n$ lớn hơn số lượng vị trí $m$.

Để giải quyết xung đột, có hai phương pháp chính:

### Separate Chaining
Đây là phương pháp đơn giản nhất: Mỗi vị trí $T[j]$ trong bảng băm không lưu trữ một phần tử, mà trỏ đến một cấu trúc dữ liệu khác (thường là danh sách liên kết) chứa tất cả các phần tử $k$ sao cho $h(k) = j$.

### Open Addressing
Trong phương pháp này, tất cả các phần tử đều được lưu trữ ngay trong chính bảng băm. Không có con trỏ, không có cấu trúc dữ liệu phụ. Khi va chạm xảy ra, chúng ta "dò" (probe) các vị trí khác trong bảng theo một trình tự nhất định cho đến khi tìm thấy một ô trống.

- Linear Probing: Hàm dò là: $h(k, i) = (h'(k) + i) \mod m$ (với $h'$ là hàm băm ban đầu).
Nói đơn giản: Nếu $h(k)$ bị chiếm, hãy thử $h(k)+1$, rồi $h(k)+2$, $h(k)+3$,...

- Quadratic Probing: Hàm dò là: $h(k, i) = (h'(k) + c_1 i + c_2 i^2) \mod m$.
Cách phổ biến: $h(k, i) = (h'(k) + i^2) \mod m$.
Nghĩa là: Thử $h(k)$, rồi $h(k)+1$, $h(k)+4$, $h(k)+9$,...

- Double Hashing: Đây được coi là kỹ thuật địa chỉ mở tốt nhất. Ý tưởng là sử dụng hai hàm băm độc lập, $h_1$ và $h_2$.Hàm dò là: $h(k, i) = (h_1(k) + i \cdot h_2(k)) \mod m$.

169-205