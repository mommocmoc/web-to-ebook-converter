---
name: web-to-ebook-converter
description: Convert web articles, longform X posts, and blogs into CJK-optimized A5 PDF ebooks with diagrams.
version: 1.0.0
author: mommocmoc
license: MIT
---

# Web to A5 eBook Converter

This skill standardizes the end-to-end workflow of converting web articles, X/Twitter longform essays, Substack posts, and technical blogs into beautifully typeset, CJK-optimized A5 portrait PDF ebooks.

## Supported Agents & Environments
- **Claude Code**: `.claude/skills/web-to-ebook-converter/`
- **Antigravity (AGY)**: `.agent/skills/web-to-ebook-converter/` or `~/.gemini/antigravity/skills/`
- **Codex**: `.codex/skills/web-to-ebook-converter/`
- **Hermes**: `~/.hermes/skills/publishing/web-to-ebook-converter/`

## Quick Install
```bash
# Universal install via npx skills
npx skills add mommocmoc/web-to-ebook-converter

# Install specifically for Claude Code
npx skills add mommocmoc/web-to-ebook-converter -a claude-code -g -y

# Install specifically for Antigravity
npx skills add mommocmoc/web-to-ebook-converter -a antigravity -g -y

# Install specifically for Codex
npx skills add mommocmoc/web-to-ebook-converter -a codex -g -y
```

## Features & Standards
1. **A5 Publication Layout (`148mm × 210mm`)**:
   - Margins: Top 18mm, Left 14mm, Bottom 20mm, Right 14mm.
   - Dynamic page numbering: `@bottom-center { content: counter(page); font-size: 8.5pt; color: #888; }`.
   - Typography: Clean serif/sans-serif fallbacks (`Apple SD Gothic Neo`, `Nanum Myeongjo`, `Noto Serif CJK`).
   - Line height `1.76`, `word-break: keep-all; text-align: justify;`.
2. **Lossless Media Asset Preservation**:
   - Automatically parses media entities, fetches original image assets locally, and anchors them in matching context.
3. **Headless Chrome PDF Rendering**:
   - Uses native Google Chrome print-to-pdf engine without headers/footers for pixel-perfect vector output.
