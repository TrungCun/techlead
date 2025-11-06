# RAG (Retrieval-Augmented Generation)

Là một kỹ thuật giúp nâng cao khả năng của mô hình sinh (language model generation) bằng cách truy xuất thông tin liên quan từ kho tài liệu (tri thức) và sử dụng chúng cho quá trình sinh câu trả lời dựa trên LLMs.

=> RAG như là một phương pháp tiết kiệm, đơn giản hơn để cải thiện các mô hình LLM trong trường hợp cần cập nhật kiến thức thay vì fine-tunning.
- Kiến thức bị giới hạn trong thời điểm huấn luyện
- "Ảo giác" thông tin (Hallucinations)
- Không truy cập được dữ liệu cụ thể
- Chi phí cập nhật kiến thức rất cao

## "Ảo giác" thông tin (Hallucinations)
LLM tạo ra các thông tin sai sự thật nhưng lại trình bày trôi chảy rõ ràng. Là một lỗi hệ thông của LLM.

=> LLM hoạt động với logic cơ bản là dự đoán nội dung được sinh ra dựa trên tài liệu đã được trainning theo mức độ có khả năng liên quan nhất.

Nguyên nhân:
- Thiếu kiến thức nền tảng (Lack of Grounding)
- Dữ liệu huấn luyện có vấn đề
- Cách đặt câu hỏi (Prompting)

=> RAG (Retrieval-Augmented Generation) là giải pháp trực tiếp cho vấn đề này.

## RAG Cơ Bản
Hệ thống RAG cơ bản gồm 3 thành phần:
- Ingestion (Biến đổi dữ liệu): Xử lý dữ liệu được cung cấp và lưu trữ nhằm phục vụ truy xuất
- Retrieval (Truy xuất): Tìm kiếm thông tin liên quan từ nguồn dữ liệu bên ngoài
- Generation (Sinh nội dung): Sử dụng LLM để tạo câu trả lời dựa trên thông tin đã truy xuất.

### Ingestion:
Quá trình xử lý dữ liệu đầu vào nhằm phục vụ mục đích lưu trữ cho truy xuất.

Chunking: Chia nhỏ tài liệu thành các chunks nhỏ hơn  nhằm đảm bảo lưu trữ và đầu vào cho LLM nhưng vẫn duy trì ngữ nghĩa.

Các chiến lược chunking:
- Fixed-Size Splitting: Tạo các chunks cố định theo kích thước N ký tự => Rất tệ cho các văn bản thông thường.

- Recursive Character Splitting: Chiến lược phổ biến nhất. Sử dụng một danh sách các ký tự phân tách theo mức độ ưu tiên (eg: \n\n, \n, ., '' v.v...) Cố gắng chunks theo từng các ký tự phân tách, nếu kích thước chunks vẫn quá lớn, tiếp tục sử dụng các ký tự phân tách bên dưới để chia nhỏ hơn

- Semantic Chunking: Chunking dựa trên ý nghĩa của câu dựa trên các embedding model. Đánh giá ý nghĩa của các câu. Nếu có sự thay đổi đột ngột về ý nghĩa => một chunk mới. => chất lượng cao.

- Structure-Aware Splitting: Chunking dựa trên cấu trúc tài liệu. Sử dụng cho các dạng tài liệu đặc thù như Markdown, HTML hoặc Json.


Embeddings: Biến đổi các cấu query của user và các chunks từ docs trở thành vector để thực hiện lưu trữ, so sánh.

Dense embedding và Sparse embedding => 2 cơ chế embed cơ bản nhất, mang những đặc điểm khác nhau:
- Sparse embedding: matching các từ vựng của query và docs, Phù hợp cho các hệ thống yêu cầu tìm kiếm dựa trên các từ khóa quan trọng, như các tài liệu khoa học, không nắm bắt được đặc điểm về ngữ nghĩa.
- Dense embedding: Lưu trữ các vector embed của một chunks. Đảm bảo thông tin về ngữ cảnh.

### Retrieval
Tìm kiếm các chunks chứa thông tin được cho là có liên quan đến query mà người dùng cung cấp.

Similarity Search: Sử dụng các phép đo tương đồng giữa các vector embed đã được lưu trữ. Eg: cosine, L2,  dot product.

Keyword Search: Tìm kiếm các từ khóa giống nhau giữa query và các chunks. Là quá trình xử lý cho Spare embed.

### Generation

Sử dụng các LLM nhằm sinh ra câu trả lời dựa trên query người dùng cung cấp và dữ liệu được retrieval.
Tăng cường (Augmentation): Kết hợp query và các ngữ cảnh được truy xuất từ docs để tạo ra một prompt hợp lý cho LLM.

## Các kỹ thuật quan trọng.

### Cải thiện Truy xuất (Improving Retrieval - "Pre-Retrieval")
Query Transformation (Biến đổi Truy vấn): Sử dụng LLM để mở rộng, viết lại câu hỏi (ví dụ: sinh nhiều biến thể câu hỏi).

Hybrid Search (Tìm kiếm Lai ghép):Kết hợp kết quả từ Dense Vectors (sematic) và Sparse Vectors (keyword). Điển hình là cơ chế Reciprocal Rank Fusion (RRF).

### Cải thiện Ngữ cảnh (Improving Context - "Post-Retrieval")
Context Compression (Nén Ngữ cảnh): Loại bỏ các câu không liên quan khỏi các chunk đã truy xuất trước khi đưa vào LLM.