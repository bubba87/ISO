#!/usr/bin/env python3
"""
Generate translated EN PDFs from Markdown source files.
Each MD file in sources_eng_md/ is converted to a PDF in sources_eng/.
"""

import markdown
from weasyprint import HTML
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MD_DIR = os.path.join(SCRIPT_DIR, 'sources_eng_md')
OUT_DIR = os.path.join(SCRIPT_DIR, 'sources_eng')

CSS = """
@page {
    size: A4;
    margin: 20mm 18mm 25mm 18mm;
    @bottom-center {
        content: "Plus Sarl — ISO 9001:2015 — Page " counter(page);
        font-size: 8pt;
        color: #666;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
}

body {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #222;
}

h1 {
    font-size: 18pt;
    color: #1a365d;
    border-bottom: 2px solid #1a365d;
    padding-bottom: 6px;
    margin-top: 20px;
}

h2 {
    font-size: 14pt;
    color: #1a365d;
    margin-top: 18px;
}

h3 {
    font-size: 12pt;
    color: #2d3748;
    margin-top: 14px;
}

strong {
    color: #1a202c;
}

ul, ol {
    margin: 5px 0;
    padding-left: 25px;
}

li {
    margin: 4px 0;
}

hr {
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 15px 0;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 10pt;
}

th {
    background-color: #1a365d;
    color: white;
    padding: 6px 8px;
    text-align: left;
}

td {
    padding: 5px 8px;
    border-bottom: 1px solid #e2e8f0;
}
"""


def md_to_pdf(md_path, pdf_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    html_body = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><style>{CSS}</style></head>
<body>{html_body}</body>
</html>"""

    HTML(string=full_html).write_pdf(pdf_path)
    size_kb = os.path.getsize(pdf_path) / 1024
    print(f"  Generated: {os.path.basename(pdf_path)} ({size_kb:.0f} KB)")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    if not os.path.exists(MD_DIR):
        print(f"Error: {MD_DIR} not found")
        sys.exit(1)

    md_files = sorted([f for f in os.listdir(MD_DIR) if f.endswith('.md')])
    print(f"Generating {len(md_files)} EN PDFs...")

    for md_file in md_files:
        pdf_file = md_file.replace('.md', '.pdf')
        md_path = os.path.join(MD_DIR, md_file)
        pdf_path = os.path.join(OUT_DIR, pdf_file)
        md_to_pdf(md_path, pdf_path)

    print(f"\nDone! {len(md_files)} PDFs generated in {OUT_DIR}")


if __name__ == '__main__':
    main()
