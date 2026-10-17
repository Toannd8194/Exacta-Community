# exa-tim-tai-lieu — Tìm tài liệu PubMed/MeSH và kiểm tra tài liệu tham khảo

[English](README_EN.md)

## Chức năng

Chuyển câu hỏi lâm sàng tiếng Việt thành bảng PICO, chiến lược tìm kiếm PubMed/MeSH, gợi ý chuỗi tìm kiếm cho tài liệu Việt Nam, tìm tài liệu hỗ trợ cho từng luận điểm trong bản thảo, xuất file RIS/BibTeX cho Zotero/EndNote và kiểm tra danh mục tài liệu tham khảo.

Lớp phủ tiếng Việt của [`nature-academic-search`](../nature-academic-search/README_EN.md): nạp skill gốc rồi áp dụng các quy tắc tiếng Việt.

## Ví dụ sử dụng

```text
Xây dựng chiến lược tìm kiếm PubMed cho câu hỏi: tăng huyết áp ẩn giấu ở người bệnh đái tháo đường type 2.
```

## Quy tắc chung

- Hướng dẫn cho AI viết bằng tiếng Anh; trao đổi với người dùng bằng tiếng Việt.
- Không gửi bản thảo hoặc dữ liệu người bệnh ra dịch vụ bên ngoài.
- Không bịa số liệu, tài liệu tham khảo hay số quyết định; chỗ thiếu ghi `[CẦN BỔ SUNG: ...]`.
- Xem đầy đủ trong [AGENTS.md](../../AGENTS.md).
