#!/usr/bin/env python3
"""
Web to eBook Converter Script for Antigravity & Hermes
Usage:
  python3 scripts/convert.py --url "https://x.com/..." --name "My_Book"
"""
import argparse
import json
import os
import re
import subprocess
import urllib.request

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.path.join(BASE_DIR, "cache")
IMG_DIR = os.path.join(CACHE_DIR, "images")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
ICLOUD_DIR = "/Users/deute1615/Library/Mobile Documents/com~apple~CloudDocs/SuperCow"

os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_x_article(status_id):
    api_url = f"https://api.fxtwitter.com/status/{status_id}"
    req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    return data.get('tweet', {}).get('article', {})

def download_image(url, filename):
    dest = os.path.join(IMG_DIR, filename)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp, open(dest, 'wb') as f:
        f.write(resp.read())
    return dest

def render_html_to_pdf(html_path, pdf_path):
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(ICLOUD_DIR):
        icloud_pdf = os.path.join(ICLOUD_DIR, os.path.basename(pdf_path))
        import shutil
        shutil.copy2(pdf_path, icloud_pdf)
        print(f"[+] Synced to iCloud: {icloud_pdf}")
    print(f"[+] PDF Successfully created: {pdf_path}")

def main():
    parser = argparse.ArgumentParser(description="Convert web articles to A5 PDF eBook")
    parser.add_argument("--url", required=True, help="Article URL")
    parser.add_argument("--name", default="Converted_EBook", help="Output filename")
    args = parser.parse_args()

    print(f"[*] Processing URL: {args.url}")
    # X status pattern
    x_match = re.search(r'status/(\d+)', args.url)
    if x_match:
        status_id = x_match.group(1)
        print(f"[*] Detected X Article ID: {status_id}")
        article = fetch_x_article(status_id)
        print(f"[*] Title: {article.get('title')}")
        
        # Download cover & media
        cover_info = article.get('cover_media', {}).get('media_info', {})
        if cover_info.get('original_img_url'):
            c_path = download_image(cover_info['original_img_url'], f"{status_id}_cover.jpg")
            print(f"[+] Downloaded cover: {c_path}")

        for idx, m in enumerate(article.get('media_entities', [])):
            m_url = m['media_info']['original_img_url']
            m_path = download_image(m_url, f"{status_id}_media_{idx}.jpg")
            print(f"[+] Downloaded media {idx}: {m_path}")

        print("\n[!] Article parsed and assets ready in cache/.")
        print("[!] Next step: Have AI translate content blocks and write to cache/book.html, then run render_html_to_pdf().")

if __name__ == "__main__":
    main()
