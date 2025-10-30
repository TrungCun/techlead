tree: 341-429
BST 501-539
Binary search: 400 - 456
DFS và BFS 404 - 437

# Tree

  Tree (cây) là một cấu trúc dữ liệu (data structure) cơ bản và quan trọng, thuộc loại phi tuyến tính (non-linear). Nó được dùng để biểu diễn mối quan hệ phân cấp (hierarchical relationship) giữa các phần tử dữ liệu. Hãy nghĩ về nó như một tập hợp các nút (nodes) được kết nối với nhau bởi các cạnh (edges).

Tree là một cấu trúc dữ liệu tương tự như một linked list nhưng thay vì mỗi node chỉ đơn giản chỉ đến node tiếp theo theo kiểu tuyến tính, ở tree mỗi node trỏ đến một số node khác.

## Các thuật ngữ cơ bản:
Nút (Node): Nút Gốc (Root), Nút Lá (Leaf), Nút Trong (Internal Node)
- Nút (Node): Là thành phần cơ bản nhất của cây, chứa dữ liệu (key hoặc value) và các con trỏ (pointers) hoặc tham chiếu đến các nút con của nó. Mỗi vòng tròn bạn thấy trong sơ đồ cây thường biểu diễn một nút.
- Nút Gốc (Root Node): Là nút đặc biệt nằm ở vị trí cao nhất trong cây (mức 0). Nó là nút duy nhất không có nút cha (parent node). Mọi cây không rỗng đều có chính xác một nút gốc. Đây là điểm xuất phát để truy cập vào các nút khác trong cây.
- Nút Lá (Leaf Node): Là các nút nằm ở tận cùng của các nhánh, tức là chúng không có bất kỳ nút con nào (null children). Chúng đại diện cho điểm kết thúc của một đường đi trên cây.
- Nút Trong (Internal Node): Là bất kỳ nút nào không phải là nút gốc và cũng không phải là nút lá. Nói cách khác, đây là những nút có ít nhất một nút con và cũng có một nút cha.

Quan hệ giữa các Nút: Nút Cha (Parent), Nút Con (Child), Nút Anh Em (Sibling)
- Nút Cha (Parent Node): Một nút A được gọi là nút cha của nút B nếu có một cạnh nối trực tiếp từ A xuống B. Mỗi nút (trừ nút gốc) chỉ có duy nhất một nút cha.
- Nút Con (Child Node): Ngược lại với nút cha, nút B được gọi là nút con của nút A nếu có cạnh nối từ A xuống B. Một nút cha có thể có một hoặc nhiều nút con.
- Nút Anh Em (Sibling Nodes): Là các nút có cùng một nút cha. Chúng nằm cùng một cấp (level) trong cây và là con của cùng một nút.

Cạnh (Edge) đơn giản là đường nối trực tiếp giữa hai nút, cụ thể là giữa một nút cha và một nút con của nó. Cạnh biểu diễn mối quan hệ trực thuộc giữa hai nút này. Số cạnh trong một cây luôn bằng số nút trừ đi 1 (Edges = Nodes – 1).

Đường đi (Path): Là một chuỗi các nút liên tiếp được nối với nhau bằng các cạnh, bắt đầu từ một nút gốc (thường là nút gốc của cây hoặc cây con) đến một nút đích. Ví dụ: đường đi từ nút gốc A đến nút lá E có thể là A -> B -> D -> E.

## Phân loại
### Cây Nhị phân (Binary Tree – BT)

Là một cây mà mỗi nút có tối đa hai nút con, thường được gọi là con trái (left child) và con phải (right child). Một nút có thể không có con nào, chỉ có con trái, chỉ có con phải, hoặc có cả hai.

Cây nhị phân có một số dạng đặc biệt:

- Cây nhị phân đầy đủ (Full Binary Tree): Mỗi nút trong cây đều có 0 hoặc 2 nút con.
- Cây nhị phân hoàn chỉnh (Complete Binary Tree): Tất cả các mức, trừ mức cuối cùng có thể, đều được lấp đầy hoàn toàn, và các nút ở mức cuối cùng được xếp từ trái sang phải.
- Cây nhị phân hoàn hảo (Perfect Binary Tree): Là cây nhị phân đầy đủ mà tất cả các nút lá đều ở cùng một mức (độ sâu).

### Cây Nhị phân Tìm kiếm (Binary Search Tree – BST)
Cây Nhị phân Tìm kiếm (Binary Search Tree – BST) là một loại cây nhị phân đặc biệt với một thuộc tính thứ tự quan trọng:

- Với mọi nút trong cây, tất cả các khóa (keys) trong cây con trái của nó đều nhỏ hơn khóa của nút đó.
- Tất cả các khóa trong cây con phải của nó đều lớn hơn (hoặc bằng, tùy quy ước) khóa của nút đó.
- Cả cây con trái và cây con phải cũng đều phải là các cây nhị phân tìm kiếm.

hiệu quả của BST phụ thuộc vào hình dạng của cây. Trong trường hợp xấu nhất (ví dụ: thêm các phần tử đã sắp xếp tăng dần), cây có thể bị suy biến (degenerate) thành một danh sách liên kết, khiến thao tác tìm kiếm mất thời gian O(n).

### Cây Nhị phân Tìm kiếm Cân bằng (Balanced BST)
Mục tiêu của Balanced BST là duy trì chiều cao của cây ở mức thấp nhất có thể (gần với log n) ngay cả khi thêm hoặc xóa các nút, đảm bảo hiệu suất O(log n) cho các thao tác chính.

Cây AVL (AVL Tree): Thực hiện các phép xoay để tự cân bằng

Cây Đỏ Đen (Red-Black Tree):

## Cây Heap

Cây Heap (Heap) là một cấu trúc dữ liệu dựa trên cây nhị phân hoàn chỉnh (complete binary tree) đặc biệt, thỏa mãn tính chất Heap (Heap Property):

- Max Heap: Khóa của mỗi nút cha luôn lớn hơn hoặc bằng khóa của các nút con của nó. Do đó, nút gốc luôn chứa giá trị lớn nhất.
- Min Heap: Khóa của mỗi nút cha luôn nhỏ hơn hoặc bằng khóa của các nút con của nó. Nút gốc chứa giá trị nhỏ nhất.

## Các phép toán

### Duyệt theo chiều sâu (Depth-First Search – DFS)
Đi sâu xuống một nhánh trước khi quay đầu và sang nhnash khác.
-  Preorder (NLR – Node Left Right)
- Inorder (LNR – Left Node Right)
- Postorder (LRN – Left Right Node)


### Duyệt theo chiều rộng (Breadth-First Search – BFS)

Duyệt tất cả các node ở cùng một mức trước khi đi sâu xuống. Bắt đầu từ nút gốc, đưa gốc vào hàng đợi. Chừng nào hàng đợi còn phần tử, lấy một nút ra, “thăm” nút đó, sau đó lần lượt đưa các nút con (nếu có) của nó vào cuối hàng đợi (thường là từ trái sang phải).

# Các thuật toán tìm kiếm

## Binary Search
Thuật toán tìm kiếm hoạt động dựa trên nguyên tắc nguyên tắc "chia để trị" (Divide and Conquer).Nó được sử dụng để tìm vị trí của một giá trị cụ thể (phần tử mục tiêu) trong một mảng đã được sắp xếp.

Điều kiện tiên quyết và quan trọng nhất để thực hiện tìm kiếm nhị phân là: Dữ liệu phải được sắp xếp (thường là tăng dần)

Ý tưởng tổng quát: Tìm kiếm giá trị K trong một mảng đã sắp xếp => liên tục chia đôi khoảng tìm kiếm dựa trên so sánh giá trị K với giá trị mid của khoảng tìm kiếm.

## BFS

Tìm kiếm theo chiều rộng (BFS) là một thuật toán để duyệt hoặc tìm kiếm trên các cấu trúc dữ liệu đồ thị (Graph) hoặc cây (Tree).

Tư tưởng cốt lõi của nó là "khám phá theo từng lớp" (level by level). Bắt đầu từ một đỉnh, khám phá tất cả các hàng xóm của nó rồi di chuyển vào sâu hơn.

Dựa trên cấu trúc dữ liệu queue nhằm thực hiện giải thuật. Đảm bảo rằng các đỉnh được phát hiện ở lớp $k$ sẽ luôn được xử lý trước các đỉnh được phát hiện ở lớp $k+1$.

## DFS
Tư tưởng cốt lõi của nó là "ưu tiên đi sâu". Bắt đầu từ một đỉnh gốc, nó sẽ chọn một đỉnh hàng xóm và ngay lập tức đi sâu vào khám phá đỉnh đó. Nó tiếp tục đi sâu qua các hàng xóm của hàng xóm, cho đến khi nào nó đến một đỉnh không còn hàng xóm nào (chưa được thăm) để đi tiếp (một "ngõ cụt"). Khi đó, nó sẽ "quay lui" (backtrack) về đỉnh trước đó và thử một con đường (một hàng xóm) khác.

Dựa trên Ngăn xếp (Stack) hoặc Đệ quy