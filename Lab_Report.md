# Báo cáo Lab AI Team: Từ Stakeholder đến Team Health & Growth Plan

**Dự án:** Hệ thống AI Agent hỗ trợ HR lọc & đánh giá CV (Auto-CV Screener Agent)
**Thành viên:** Phước (Tech Lead), Hải (Product Lead), Nam (AI/Data Engineer)

---

## TRANG 1: PHASE 1 - STAKEHOLDER MAP & CHIẾN LƯỢC

### Ma trận Stakeholder
| Stakeholder | Vị trí (Influence × Interest) | Nhãn | Stance | Mối quan tâm chính |
| :--- | :--- | :--- | :--- | :--- |
| Trưởng phòng Nhân sự (Pilot) | Cao × Cao | Champion | Ủng hộ | Giảm tải tuyển dụng, độ chính xác match JD |
| Giảng viên hướng dẫn / Mentor AI | Cao × Cao | Champion | Ủng hộ | Tính ứng dụng, kiến trúc (RAG/Agent), tiến độ |
| Chuyên viên Bảo mật & Pháp chế | Cao × Thấp | Blocker | Chưa ủng hộ | Rủi ro lộ PII, tuân thủ Nghị định 13 |
| Tech Lead (bên Pilot) | Cao × Thấp | Blocker | Trung lập | Chi phí API token, độ trễ, ảo giác (hallucination) |
| Recruiter trực tiếp sử dụng | Thấp × Cao | Supporter| Ủng hộ | Giao diện dễ dùng, giải thích lý do Pass/Fail |
| Ứng viên nộp CV | Thấp × Thấp | Bystander | Trung lập | Tính công bằng, không bị loại oan |

### 4 Chiến lược hành động cụ thể (1–2 tuần tới)
1. **HR Head (Champion - Tận dụng):** Cung cấp 50 JD & 200 CV để benchmark. *Hành động:* Hải gửi demo pipeline trước thứ Năm, lịch 30p thứ Sáu chốt Rubric.
2. **Mentor (Champion - Tận dụng):** Bảo chứng kỹ thuật. *Hành động:* Phước gửi tài liệu AI Architecture & độ trễ trước 18:00 Chủ Nhật.
3. **IT Security (Blocker - Hóa giải rủi ro):** Có quyền phủ quyết. *Hành động:* Nam dựng module Masking PII 100%, gửi tài liệu Data Privacy trước thứ Ba.
4. **Tech Lead Pilot (Blocker - Thuyết phục):** Lo ngại chi phí. *Hành động:* Phước xây bảng Unit Economics (≤$0.02/CV) & fallback local model trình bày tuần tới.

---

## TRANG 2: PHASE 2 - PITCH & RACI MATRIX

### Bản Pitch (Conclusion First) gửi HR Head
**Kết luận / Đề xuất:** Đề xuất thử nghiệm AI Agent Sàng lọc CV trong 2 tuần trên 1 vị trí (50 CV) giúp giảm 70% thời gian sơ loại, giữ chân ứng viên tốt.
**Lý do chính:**
- Tiết kiệm nguồn lực: Rút từ 3–5 phút xuống <15s/CV.
- Đánh giá đa chiều: Đọc hiểu ngữ cảnh kinh nghiệm theo đúng Rubric, không chỉ khớp từ khóa.
- Bảo mật & minh bạch: Ẩn danh hóa 100% PII, có trích dẫn lý do Đạt/Không đạt.
**Bằng chứng:** Thử nghiệm nội bộ (100 CV) cho thấy độ tương đồng đánh giá đạt 86%, False Negative <5%, chi phí ~$0.015/CV.
**Small Ask:** Xin 1 JD thực tế kèm tiêu chí ưu tiên để cấu hình và gửi lại kết quả chạy thử 10 CV trước 17:00 Thứ Sáu.

### Kịch bản Phản biện (Objection Handling)
*Phản biện:* AI dễ bị "ảo giác", bỏ sót ứng viên hoặc thiên vị giới tính/tuổi tác.
*Cách xử lý:*
- Kỹ thuật: Hệ thống tự động Masking (tên, tuổi, giới tính) trước khi đưa vào LLM. Chấm điểm rập khuôn theo Rubric cố định.
- Quy trình (Human-in-the-loop): AI chỉ phân loại (Tier 1/2/3) kèm trích dẫn. Recruiter bấm duyệt cuối cùng.

### RACI Matrix (Giai đoạn MVP)
| STT | Công việc trọng tâm | Hải (Product) | Phước (Tech) | Nam (AI/Data) | Stakeholder |
|:-:|:---|:-:|:-:|:-:|:---|
| 1 | Xác định Use Case & Rubric chấm CV | **A** | C | C | C (HR Head) |
| 2 | Xây dựng Data Pipeline & Masking PII | I | C | **A (kiêm R)**| I (IT Security)|
| 3 | Phát triển Core AI Agent & Prompting | C | **A** | R | I |
| 4 | Đánh giá Benchmark & Giảm Hallucination| C | C | **A (kiêm R)**| C (Mentor AI) |
| 5 | Thiết kế UI/UX & Tích hợp Demo Web | C | **A (kiêm R)**| I | I |
| 6 | Chạy Pilot thực tế & Đánh giá kết quả | **A (kiêm R)**| I | C | I (Recruiter) |

---

## TRANG 3: PHASE 3 - AI TEAM DESIGN

### 1. Kiến trúc: Embedded AI Team
*Lý do:* MVP từ 0 lên 1 cần loại bỏ độ trễ bàn giao. AI (Nam), Tech (Phước), Product (Hải) chạy chung 1 luồng, tinh chỉnh thuật toán ngay lập tức từ feedback người dùng.

### 2. Core Roles & Extended Roles
* **Core Roles (Cần ngay - MVP):**
  - AI Product & Domain Lead (Hải): Chốt UX, định nghĩa Rubric CV.
  - Fullstack & Architecture Lead (Phước): Backend API, Security/Masking, UI.
  - AI/Data Engineer (Nam): Agent Workflow, Prompt/RAG Pipeline, Evaluation.
* **Extended Roles (Chỉ bổ sung khi Scale):**
  - MLOps & LLMOps Specialist: Giám sát token/latency khi scale.
  - AI Legal & Data Compliance Officer: Rà soát luật lao động & PII.

### 3. Priority Resourcing
| Capability Gap | Phương án | Lý do lựa chọn | Thời điểm |
| :--- | :--- | :--- | :--- |
| **Domain Expertise (HR Rubrics)**| **Partner** | Hợp tác 2-3 HR Lead tại cty Pilot để chuẩn hóa tiêu chí. | Tuần 1-2 |
| **Data Annotation (Test CV)** | **Outsource** | Thuê CTV part-time gán nhãn 300 CV. Rẻ hơn thuê full-time. | Tuần 3 |
| **Kiểm định Pháp lý (Compliance)**| **Partner** | Xin tư vấn từ chính phòng Pháp chế của cty Pilot. | Tuần 4 |

### 4. Squad Goal
> *"Team của chúng tôi sở hữu toàn bộ luồng xử lý AI Agent và giao diện hỗ trợ sàng lọc ứng viên và chịu trách nhiệm đưa quy trình lọc CV thủ công tốn thời gian của HR từ hiện trạng đọc tay 5 phút/CV đến trạng thái tự động phân loại sơ loại chính xác $\ge 85\%$ chỉ trong 15 giây/CV kèm trích dẫn minh bạch trước 30/09."*

---

## TRANG 4: PHASE 4 - TEAM HEALTH & GROWTH PLAN

### Đánh giá Team Health
* **Tốc độ & Cộng tác:** Tốt (Embedded 3 người ra quyết định nhanh).
* **Chất lượng AI:** Rủi ro Hallucination & Data Privacy; thiếu tập dữ liệu chuẩn.
* **Competency Gap (L1 $\rightarrow$ L3):**
  - Hải (L2): Cần lên L3 (Xây dựng hệ thống Rubric chuẩn mực HR).
  - Nam (L2): Cần lên L3 (Làm chủ Eval Pipeline, tính False Negative).
  - Phước (L2): Cần lên L3 (Tối ưu token cost, Zero-Data Retention).

### 30-Day Growth Plan (Kế hoạch hành động 30 ngày)
| Area | Hành động cụ thể (Action) | Owner | Deadline |
| :--- | :--- | :--- | :--- |
| **Domain Expertise**| Tổ chức 2 Workshop với HR Head để map tiêu chí chấm CV thủ công thành Prompt Rubric có trọng số. | **Hải** | Tuần 1 |
| **AI Evaluation** | Setup dán nhãn Outsourcing 300 CV (Ground-Truth). Chạy test tính độ sai số, benchmark mô hình. | **Nam** | Tuần 2 |
| **Tech/Compliance** | Hoàn thiện Module Data Masking chặn 100% PII. Lập bảng Unit Economics (API/CV) báo cáo Tech Lead. | **Phước** | Tuần 3 |
