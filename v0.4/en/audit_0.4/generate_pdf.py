#!/usr/bin/env python3
"""
PDF Generator for the ISO 9001:2015 audit dossier — Plus Sarl
Combines MQ-001 + INDEX into a single PDF for submission to SQS.
"""

import markdown
from weasyprint import HTML
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

CSS = """
@page {
    size: A4;
    margin: 20mm 18mm 25mm 18mm;
    @bottom-center {
        content: "Plus Sarl — Quality Manual v0.4 — Page " counter(page) " / " counter(pages);
        font-size: 8pt;
        color: #666;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    @top-right {
        content: "MQ-001 — ISO 9001:2015";
        font-size: 7pt;
        color: #999;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
}

@page:first {
    @top-right { content: none; }
    @bottom-center { content: none; }
}

body {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.5;
    color: #222;
}

h1 {
    font-size: 22pt;
    color: #1a365d;
    border-bottom: 3px solid #1a365d;
    padding-bottom: 8px;
    margin-top: 30px;
    page-break-before: auto;
}

h2 {
    font-size: 16pt;
    color: #1a365d;
    border-bottom: 1.5px solid #cbd5e0;
    padding-bottom: 5px;
    margin-top: 25px;
    page-break-before: always;
}

h2:first-of-type {
    page-break-before: auto;
}

h3 {
    font-size: 12pt;
    color: #2d3748;
    margin-top: 18px;
}

h4 {
    font-size: 10.5pt;
    color: #4a5568;
    margin-top: 12px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 9pt;
    page-break-inside: auto;
}

tr {
    page-break-inside: avoid;
}

th {
    background-color: #1a365d;
    color: white;
    padding: 6px 8px;
    text-align: left;
    font-weight: 600;
    font-size: 8.5pt;
}

td {
    padding: 5px 8px;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: top;
}

tr:nth-child(even) td {
    background-color: #f7fafc;
}

blockquote {
    border-left: 3px solid #3182ce;
    padding: 8px 12px;
    margin: 10px 0;
    background-color: #ebf8ff;
    font-size: 9pt;
    color: #2c5282;
}

code, pre {
    font-family: 'Courier New', monospace;
    font-size: 8.5pt;
    background-color: #f7fafc;
    border: 1px solid #e2e8f0;
    border-radius: 3px;
}

pre {
    padding: 10px;
    overflow-x: auto;
    white-space: pre-wrap;
    page-break-inside: avoid;
}

code {
    padding: 1px 4px;
}

hr {
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 20px 0;
}

strong {
    color: #1a202c;
}

ul, ol {
    margin: 5px 0;
    padding-left: 20px;
}

li {
    margin: 3px 0;
}

.cover-page {
    text-align: center;
    padding-top: 120px;
    page-break-after: always;
}

.cover-page h1 {
    font-size: 32pt;
    border: none;
    color: #1a365d;
    margin-bottom: 10px;
}

.cover-page .subtitle {
    font-size: 18pt;
    color: #2d3748;
    margin-bottom: 40px;
}

.cover-page .company {
    font-size: 14pt;
    color: #4a5568;
    margin-bottom: 5px;
}

.cover-page .info {
    font-size: 11pt;
    color: #718096;
    margin: 3px 0;
}

.cover-page .badge {
    display: inline-block;
    background-color: #1a365d;
    color: white;
    padding: 8px 25px;
    border-radius: 5px;
    font-size: 11pt;
    margin-top: 40px;
}

.cover-page .footer-note {
    margin-top: 60px;
    font-size: 9pt;
    color: #a0aec0;
}

.separator {
    page-break-before: always;
    text-align: center;
    padding-top: 200px;
}

.separator h1 {
    font-size: 26pt;
    border: none;
    color: #1a365d;
}

.separator .desc {
    font-size: 12pt;
    color: #4a5568;
    margin-top: 20px;
}
"""

COVER_HTML = """
<div class="cover-page">
    <h1>QUALITY MANUAL</h1>
    <div class="subtitle">Quality Management System<br>ISO 9001:2015</div>
    <hr style="width:200px; margin:30px auto; border-top:2px solid #1a365d;">
    <div class="company">Plus Sarl</div>
    <div class="info">Route de Montet 11, 1588 Cudrefin, Switzerland</div>
    <div class="info">IDE No.: CH-645.4.101.228-7</div>
    <div class="info">Managing Director: Roxane Wicky</div>
    <div class="info">Certification body: SQS</div>
    <div class="badge">VERSION 0.4 — WORKING VERSION</div>
    <div class="info" style="margin-top:30px;">Reference: MQ-001</div>
    <div class="info">Date: 22/02/2026</div>
    <div class="footer-note">This document is strictly confidential.<br>
    It is intended for the certification body SQS as part of the ISO 9001:2015 audit.</div>
</div>
"""

PART2_SEPARATOR = """
<div class="separator">
    <h1>PART 2</h1>
    <div class="desc">AUDIT DOSSIER INDEX<br>
    ISO 9001:2015 — QMS Document Correspondence</div>
</div>
"""


def md_to_html(md_path):
    """Convert a markdown file to HTML."""
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    extensions = ['tables', 'toc', 'fenced_code', 'nl2br']
    html = markdown.markdown(md_content, extensions=extensions)
    return html


def main():
    mq_path = os.path.join(SCRIPT_DIR, 'MQ-001_Quality_Manual.md')
    index_path = os.path.join(SCRIPT_DIR, 'INDEX_AUDIT_DOSSIER.md')
    output_path = os.path.join(SCRIPT_DIR, 'AUDIT_DOSSIER_ISO9001_Plus_Sarl_v0.4.pdf')

    print("Generating ISO 9001 audit dossier PDF...")
    print(f"  MQ-001: {mq_path}")
    print(f"  INDEX:  {index_path}")

    # Convert MD files to HTML
    mq_html = md_to_html(mq_path)
    index_html = md_to_html(index_path)

    # Combine everything
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>{CSS}</style>
</head>
<body>
    {COVER_HTML}
    {mq_html}
    {PART2_SEPARATOR}
    {index_html}
</body>
</html>"""

    # Generate PDF
    HTML(string=full_html).write_pdf(output_path)

    file_size = os.path.getsize(output_path) / 1024
    print(f"\nPDF generated successfully!")
    print(f"  File: {output_path}")
    print(f"  Size: {file_size:.0f} KB")


if __name__ == '__main__':
    main()
