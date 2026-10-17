# Frozen Content Registry

This directory holds upstream content that is **disabled** in the Exacta fork
(`exacta` branch). Nothing under `frozen/` is installed, routed, or executed. Agents must
not read, load, or run any file in this directory unless the repository owner explicitly asks
to unfreeze a specific item.

Files are moved with `git mv`, so upstream fixes still merge onto the moved paths. To unfreeze an
item, `git mv` it back to its original location and update the skill index in both root READMEs.

## Frozen skills

| Skill | Reason |
|---|---|
| `nature-downloader` | China-specific access (CNKI, CARSI); handles institutional login credentials and publisher API keys |
| `nature-paper-to-patent` | Chinese invention-patent (CNIPA) drafting; ships an npm dependency tree |
| `nature-paper-trans` | Translates papers into Simplified Chinese only |
| `nature-social-science` | Chinese-language social-science workbench |
| `nature-experiment-log` | Chinese-language; optional Feishu (Lark) group ingestion of lab data |
| `nature-image2ppt` | Sends slide images to external OCR / image APIs (Baidu PaddleOCR, OpenAI) |
| `nature-literature-pipeline` | Cron automation that pushes digests to Feishu / Telegram |
| `nature-ref-verifier` | Chinese-language instructions; Zotero write-back. Use `exa-tim-tai-lieu` for reference checks |
| `nature-proposal-writer` | Built around Chinese grant (NSFC) conventions. Replaced by `exa-de-cuong` |

## Frozen files

| Path | Reason |
|---|---|
| `index.html` | Upstream promotional website |
| `assets/nature-ai-gpt-claude-service.png` | Advertisement for an account top-up service |
| `assets/wechat-qr.jpg` | WeChat contact QR code |
| `assets/readme-banner-cn.png` | Chinese-language banner |
| `scripts/autoupdate-skills.sh` | Unattended network auto-update (supply-chain risk) |
| `github-workflows/update-star-history.yml` | Scheduled job that commits to the repository |
| `github-workflows/test-skill-tooling.yml` | CI that only tests frozen skills (downloader, image2ppt, paper-to-patent) |

## Rule-level freezes inside active skills

These files remain in place (moving them would break upstream routing and tests), but agents
must never load them in this fork. The `exa-*` skills provide the Vietnamese equivalents.

| File | Replacement |
|---|---|
| `skills/nature-writing/static/fragments/language/zh-to-en.md` | `skills/nature-shared/vn/vi-to-en.md` |
| `skills/nature-writing/references/chinese-author-workflow.md` | `skills/nature-shared/vn/vi-to-en.md` |
| `skills/nature-data/static/core/chinese-mode.md` | English mode only |
| `skills/nature-data/references/chinese-author-alignment.md` | `skills/nature-shared/vn/vi-to-en.md` |
| `skills/nature-citation/static/core/chinese-mode.md` | English mode only |
| `skills/nature-response/references/chinese-author-alignment.md` | `skills/nature-shared/vn/vi-to-en.md` |
| The `中文核对` (Chinese check) block in `nature-response` | Vietnamese check block defined in `exa-phuc-dap` |
| Text and claim modes of `skills/nature-citation/scripts/nature_citation.py` (`--text`, `--text-file`, `--claim`, `--claim-file`), which send manuscript passages to Crossref | `exa-tim-tai-lieu` claim-by-claim workflow (concept queries, export by PMID/DOI) |
| The Chinese-by-default slide language and Chinese planning files in `nature-paper2ppt` | `exa-trinh-chieu` (Vietnamese by default) |
| The OpenRouter route in `nature-figure` (`scripts/generate_openrouter_schematic.py`, `references/openrouter-image-generation.md`) | Local Python/R plotting or hand-built SVG only |

