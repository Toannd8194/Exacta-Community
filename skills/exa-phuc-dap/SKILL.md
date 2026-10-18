---
name: exa-phuc-dap
description: "Vietnamese overlay for nature-response: draft, audit, or revise English responses to peer review and revision cover letters for Vietnamese authors, with a Vietnamese action plan and author check. Use for trả lời phản biện, thư phúc đáp, chỉnh sửa bản thảo theo ý kiến phản biện; mock review belongs to exa-phan-bien."
metadata:
  version: "0.1.0"
  base_skill: nature-response
---

# Exacta · Phúc đáp — Vietnamese Overlay

## Load order

1. Read [manifest.yaml](manifest.yaml) and every `always_load` file.
2. Read [../nature-response/SKILL.md](../nature-response/SKILL.md) and follow its routing
   protocol in full: task mode, decision-type gate, comment IDs, mutually blind per-reviewer
   responses, change mapping, red marking, QA, and readiness.
3. Apply the overrides below. On conflict, these overrides win.

Never load any file listed as frozen in `frozen/FROZEN.md`, including
`references/chinese-author-alignment.md` in the base skill.

## Overrides

### Vietnamese check block replaces 中文核对

Wherever the base skill would emit a `中文核对` block, emit instead (in Vietnamese):

```
### Kế hoạch xử lý cho tác giả
| Mã ý kiến | Phản biện yêu cầu gì (tóm tắt) | Hướng trả lời | Việc tác giả cần làm | Cần dữ liệu/phân tích mới? | Trạng thái |

### Ghi chú cho tác giả
- Chỗ trả lời có thể bị coi là né tránh hoặc thiếu bằng chứng: ...
- Thông tin còn thiếu: [CẦN BỔ SUNG: ...]
```

Emit it whenever the user writes in Vietnamese. It is an internal file for the authors and is
never included in a reviewer-facing response.

### Author notes in Vietnamese

Treat Vietnamese author notes as the base skill treats non-English notes: extract intent, never
translate them literally into the letter. Apply `../nature-shared/vn/vi-to-en.md` to every
English sentence drafted from Vietnamese notes.

### Tone

Polite, specific, and evidence-led. Avoid excessive gratitude formulas and avoid defensive
phrasing. Every "we have revised" must point to a manuscript location or a placeholder.

### Additional analyses

If a reviewer requests new statistics, route the analysis design to `exa-thong-ke`
and do not claim results that have not been computed.

### Community edition scope

- Classify **all** comments (the triage table with comment IDs, response action, and work
  needed) and the Vietnamese author plan.
- Draft point-by-point replies for **up to 5 comments** per request (Blocking and Major first,
  or the ones the user chooses).
- The complete response package — every reply, the revision cover letter, marked-manuscript
  changes, and package QA — with the Vietnamese plan and author check is an Exacta Pro
  capability; the base skill `nature-response` still drafts a general-standard package. If
  requested, follow `../nature-shared/vn/community-edition.md`.
