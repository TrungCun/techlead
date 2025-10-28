# Big O

## What is Big O ?
Big O hay Big O notation là kí hiệu toán học dùng để mô tả hiệu suất của một thuật toán. Mô tả về khía cạnh thời gian.  Nó thể hiện thuật toán sẽ chạy chậm như thế nào khi kích thước dữ liệu đầu vào tăng lên.

Big O tập trung vào tốc độ tăng trưởng (growth rate) ở trường hợp xấu nhất (worst-case scenario) với một quy tắc cơ bản:
- Bỏ qua các hằng số. Một thuật toán mất $2n$ giây và một thuật toán mất $n$ giây đều được coi là $O(n)$
- Chỉ giữ lại số hạng lớn nhất. Khi kích thước đầu vào $n$ trở nên rất lớn, chỉ số hạng có tốc độ tăng trưởng nhanh nhất mới thực sự quan trọng. Một thuật toán có độ phức tạp $O(n^2 + n)$ ta coi nó có độ phức tạp $O(n^2)$.
## Tốc độ giải thuật của các trường hợp
Một thuật toán sẽ có hiệu suất khác nhau tùy thuộc vào đầu vào.

- Best Case (Trường hợp tốt nhất): Chi phí tối thiểu mà thuật toán phải chịu. Coi là trường hợp lí tưởng nhất.
- Average Case (Trường hợp trung bình): Chi phí trung bình khi chạy thuật toán với tất cả các đầu vào có thể. Đây thường là phân tích hữu ích nhất trong thực tế, nhưng cũng là phân tích khó thực hiện nhất về mặt toán học.
- Worst Case (Trường hợp xấu nhất): Chi phí tối đa mà thuật toán phải chịu với một đầu vào có kích thước $n$. Thuật toán sẽ không bao giờ chạy chậm hơn mức này. Big O được dùng để chỉ Worst Case
## Giới hạn Asymptotic:  $O$, $\Omega$, và $\Theta$ trong Phân tích Thuật toán
- Big O ($O$) -  Giới hạn trên (Upper Bound). Là trường hợp xâu nhất. Thuật toán sẽ không chạy chậm hơn mức này.
- $\Omega$ (Big Omega) — Giới hạn dưới (Lower Bound). là trường hợp tốt nhất (Best Case). Đặt ra một mức sàn cho thời gian giải thuật, thời gian không thể nhanh hơn mức này dù đầu vào có tốt đến đâu.
- $\Theta$ (Big Theta) — Giới hạn chặt. Khi Best Case và Worst Case giống nhau về tốc độ tăng trưởng. Là ký hiệu mạnh nhất và chính xác nhất. Nó mô tả một thuật toán có thời gian chạy được "kẹp chặt" giữa cả giới hạn trên và giới hạn dưới.
## Các độ phức tạp cho Big O
- $O(1)$ - Thời gian hằng số: thuật toán mất thời gian không đổi, bất kể n lớn đến đâu.
- $O(logn)$ - Thời gian logarit: thuật toán có thời gian tăng lên chậm. Khi n tăng gấp đôi, thời gian chỉ tăng thêm một bước cố định.
- $O(n)$ - Thời gian tuyến tính: Thời gian tăng tỉ lệ thuận với n. Nếu n tăng gấp đôi,  thời gian chạy cũng tăng gấp đôi.
- $O(n logn)$ - Thời gian log - tuyến tính: Nhanh hơn $O(n^2)$ nhưng chậm hơn $O(n)$. Là độ phức tạp chuẩn cho các thuật toán sắp xếp hiệu quả.
- $O(n^2)$ - Thời gian bậc 2: Tăng theo bình phương của n. Nếu n tăng 10 lần, thời gian sẽ tăng 100 lần. Xảy ra với các giải thuật có vòng lặp lồng nhau.
- $O(2^n)$ - Thời gian hàm mũ: Cực kỳ chậm. Thời gian chạy tăng gấp đôi mỗi khi thêm một phần tử vào $n$.
- $O(n!)$ — Thời gian giai thừa: Chậm nhất.

---
# Array
Array (mảng)  là 1 tập hợp các phần tử được lưu dưới dạng những ô nhớ liền kề nhau.

Phân tích độ phức tạp:
- Truy cập (Access): O(1)
- Tìm kiếm (Search): O(n). Nếu là mảng đã sắp xếp => binary search có độ phức tạp còn  $O(logn)$.
- Chèn (Insertion): O(n)
- Xoá (Deletion): O(n)

Mảng đa chiều thực chất không tồn tại trong bộ nhớ. Nó chỉ là một cách trừu tượng hóa. Trong bộ nhớ, nó vẫn là mảng 1 chiều.

# Linked List
Danh sách liên kết là 1 cấu trúc dữ liệu được sử dụng để lưu trữ 1 tập hợp các dữ liệu. Danh sách liên kết có các tính chất sau:
- Các phần tử trong danh sách liên kết được kết nối bằng con trỏ.
- Phần tử cuối trỏ tới NULL.
- Có thể tăng hoặc giảm số lượng phần tử trong quá trình thực thi chương trình.
- Tối ưu dung lượng bộ nhớ.

Có 2 giải thuật chính đối với danh sách liên kết là:
- Insert: Chèn một phần tử vào vị trí bất kỳ trong danh sách liên kết.
- Delete: Xóa một phần tử ở vị trí bất kỳ trong danh sách liên kết.

