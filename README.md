# Web to A5 eBook Converter

Convert web articles, X (Twitter) longform essays, Substack posts, and technical blogs into beautifully typeset, CJK-optimized A5 PDF ebooks with images.

Designed for AI coding agents (**Claude Code**, **Antigravity**, **Codex**, **Hermes**) and human builders.

---

## ⚡ Quick Install

You can install this skill across your agents using [`npx skills`](https://github.com/vercel-labs/skills):

```bash
# Universal install (interactive agent selection)
npx skills add mommocmoc/web-to-ebook-converter

# Install globally for Claude Code
npx skills add mommocmoc/web-to-ebook-converter -a claude-code -g -y

# Install globally for Antigravity (AGY)
npx skills add mommocmoc/web-to-ebook-converter -a antigravity -g -y

# Install globally for Codex
npx skills add mommocmoc/web-to-ebook-converter -a codex -g -y
```

---

## 📐 Publication & Layout Standards

- **Page Dimension**: A5 Portrait (`148mm × 210mm`)
- **Print Engine**: Google Chrome Headless (`--headless --disable-gpu --no-pdf-header-footer --print-to-pdf=...`)
- **Typography**: CJK publication font stacks (`Apple SD Gothic Neo`, `Nanum Myeongjo`, `Noto Serif KR/CJK`) with justify alignment and word-break preservation.
- **Dynamic Counters**: `@bottom-center { content: counter(page); font-size: 8.5pt; color: #888; }`
- **Asset Preservation**: Lossless media entity extraction into local cache before compiling to avoid broken remote URLs.

---

## 🚀 Usage

Inside your agent session (Claude Code, Antigravity, or Codex):
> *"Turn this article into an A5 PDF ebook: https://x.com/..."*

Or run directly via CLI:
```bash
python3 scripts/convert.py --url "https://x.com/..." --name "My_Book"
```

---

## License

MIT © [mommocmoc](https://github.com/mommocmoc)
