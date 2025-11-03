# Thuật toán sắp xếp

## Các Thuật toán Đơn giản ($O(n^2)$)
### Insertion Sort (Sắp xếp chèn)

Ý tưởng: Duyệt qua mảng, với mỗi phần tử, ta chèn nó vào đúng vị trí trong phần mảng đã được sắp xếp phía bên trái.
- Bắt đầu từ phần tử thứ hai trong mảng.
- So sánh phần tử hiện tại với các phần tử trước đó.
- Di chuyển các phần tử nhỏ hơn lên một vị trí để tạo chỗ trống.
- Chèn phần tử hiện tại vào vị trí thích hợp.

Độ phức tạp:
- Best case: $O(n)$
- Average case: $O(n^2)$
- Worst case: $O(n^2)$

### Selection Sort (Sắp xếp chọn)
Sắp xếp từng phần tử một. Tìm phần tử nhỏ nhất trong mảng chưa sắp xếp và đổi chỗ nó với phần tử đầu tiên của mảng chưa sắp xếp. Lặp lại quá trình này cho phần còn lại.

- Duyệt qua toàn bộ mảng để tìm phần tử nhỏ nhất.
- Hoán đổi phần tử nhỏ nhất với phần tử đầu tiên của mảng.
- Tiếp tục với phần còn lại của mảng (bỏ qua phần tử đầu tiên đã được sắp xếp).

Độ phức tạp:
- Best case: $O(n)$
- Average case: $O(n^2)$
- Worst case: $O(n^2)$

### Bubble Sort (Sắp xếp nổi bọt)
Lặp đi lặp lại việc so sánh các cặp phần tử liền kề và đổi chỗ chúng nếu chúng sai thứ tự. Các phần tử "nhẹ" (nhỏ) sẽ "nổi" lên đầu, và các phần tử "nặng" (lớn) sẽ "chìm" xuống cuối

- Bắt đầu từ đầu danh sách, so sánh hai phần tử đầu tiên.
- Nếu phần tử thứ nhất lớn hơn phần tử thứ hai, hoán đổi chúng.
- Tiếp tục với cặp phần tử tiếp theo cho đến cuối danh sách.
- Lặp lại quá trình trên cho đến khi không có sự hoán đổi nào xảy ra trong một lần duyệt.

Độ phức tạp:
- Best case: $O(n)$
- Average case: $O(n^2)$
- Worst case: $O(n^2)$

## Các Thuật toán Hiệu quả ($O(n \log n)$)
### Merge Sort (Sắp xếp trộn)

Một thuật toán Chia để trị (Divide and Conquer) cổ điển. Chia mảng thành hai nửa, sắp xếp từng nửa và sau đó trộn chúng lại.

- Chia mảng thành hai nửa cho đến khi mỗi phần chỉ còn một phần tử.
- Trộn hai mảng con đã được sắp xếp thành một mảng duy nhất.

### Quick Sort (Sắp xếp nhanh)

Quick Sort là thuật toán sắp xếp hiệu quả, sử dụng phương pháp chia để trị, chọn một pivot và phân chia mảng thành hai phần dựa trên pivot.

- Chọn một phần tử làm pivot - thường sẽ lấy giữa.
- Phân chia mảng thành hai phần: phần nhỏ hơn pivot và phần lớn hơn pivot.
- Đệ quy áp dụng thuật toán cho hai phần này

406 462