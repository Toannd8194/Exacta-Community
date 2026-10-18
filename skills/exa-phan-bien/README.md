# exa-phan-bien — Phản biện thử bản thảo

[English](README_EN.md)

## Chức năng

Giả lập phản biện độc lập (mutually blind) cho bản thảo y sinh học, thêm các cổng kiểm tra thường gặp ở bài báo của tác giả Việt Nam (đạo đức, hướng dẫn báo cáo, cỡ mẫu, ngôn ngữ nhân quả) và bảng hành động bằng tiếng Việt.

Lớp phủ tiếng Việt của [`nature-reviewer`](../nature-reviewer/README_EN.md): nạp skill gốc rồi áp dụng các quy tắc tiếng Việt.

> Bản Community: một báo cáo phản biện đầy đủ theo tiêu chí trong nước. Skill nền `nature-reviewer` vẫn cho ba phản biện độc lập theo chuẩn quốc tế chung. Bản Pro áp tiêu chí trong nước cho cả ba phản biện và phần tổng hợp, kèm tóm tắt hành động bằng tiếng Việt.

## Ví dụ sử dụng

```text
Phản biện thử bản thảo này như reviewer của tạp chí quốc tế, rồi tóm tắt việc cần sửa bằng tiếng Việt.
```

## Quy tắc chung

- Hướng dẫn cho AI viết bằng tiếng Anh; trao đổi với người dùng bằng tiếng Việt.
- Không gửi bản thảo hoặc dữ liệu người bệnh ra dịch vụ bên ngoài.
- Không bịa số liệu, tài liệu tham khảo hay số quyết định; chỗ thiếu ghi `[CẦN BỔ SUNG: ...]`.
- Xem đầy đủ trong [AGENTS.md](../../AGENTS.md).
