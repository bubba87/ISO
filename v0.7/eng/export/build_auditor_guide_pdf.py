#!/usr/bin/env python3
"""
Generates the professional PDF of the SQS Auditor Guide for Plus Sarl v0.7
Dependencies: pip install markdown weasyprint
"""

import markdown
from pathlib import Path

BASE = Path(__file__).parent
MD_FILE = BASE / "SQS_Auditor_Guide_Plus_Sarl_v0.7.md"
PDF_FILE = BASE / "SQS_Auditor_Guide_Plus_Sarl_v0.7.pdf"


def build_pdf():
    from weasyprint import HTML

    md_text = MD_FILE.read_text(encoding='utf-8')

    # Remove YAML front matter
    if md_text.startswith('---'):
        end = md_text.find('---', 3)
        if end != -1:
            md_text = md_text[end + 3:].strip()

    # Remove \newpage markers (handled by CSS page breaks on h1)
    md_text = md_text.replace('\\newpage', '')

    html_content = markdown.markdown(
        md_text,
        extensions=['tables', 'fenced_code', 'toc'],
    )

    pdf_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
@page {{
  size: A4;
  margin: 25mm 20mm 30mm 20mm;
  @top-left {{
    content: "SQS Auditor Guide — Plus Sarl";
    font-size: 8pt;
    color: #6b7280;
    font-family: 'Segoe UI', system-ui, sans-serif;
  }}
  @top-right {{
    content: "v0.7 — March 2026";
    font-size: 8pt;
    color: #6b7280;
    font-family: 'Segoe UI', system-ui, sans-serif;
  }}
  @bottom-center {{
    content: counter(page);
    font-size: 9pt;
    color: #6b7280;
    font-family: 'Segoe UI', system-ui, sans-serif;
  }}
  @bottom-right {{
    content: "Confidential";
    font-size: 7pt;
    color: #9ca3af;
    font-family: 'Segoe UI', system-ui, sans-serif;
  }}
}}

@page :first {{
  margin: 0;
  @top-left {{ content: none; }}
  @top-right {{ content: none; }}
  @bottom-center {{ content: none; }}
  @bottom-right {{ content: none; }}
}}

body {{
  font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
  font-size: 10pt;
  line-height: 1.6;
  color: #1f2937;
}}

/* Cover page - first h1 */
body > h1:first-of-type {{
  page-break-after: always;
  font-size: 28pt;
  color: #1a56db;
  text-align: center;
  padding-top: 80mm;
  border: none;
}}

/* Section headers trigger page breaks */
h1 {{
  font-size: 18pt;
  color: #1a56db;
  border-bottom: 3px solid #1a56db;
  padding-bottom: 6px;
  margin: 24px 0 16px;
  page-break-before: always;
}}

h1:first-of-type {{
  page-break-before: avoid;
}}

h2 {{
  font-size: 13pt;
  color: #374151;
  margin: 20px 0 10px;
  border-left: 4px solid #1a56db;
  padding-left: 10px;
}}

h3 {{
  font-size: 11pt;
  color: #4b5563;
  margin: 16px 0 8px;
}}

h4 {{
  font-size: 10pt;
  color: #6b7280;
  margin: 12px 0 6px;
  font-style: italic;
}}

p {{
  margin: 6px 0;
  text-align: justify;
  line-height: 1.65;
}}

ul, ol {{
  margin: 6px 0 6px 18px;
  line-height: 1.6;
}}

li {{
  margin: 3px 0;
}}

table {{
  width: 100%;
  border-collapse: collapse;
  margin: 10px 0;
  font-size: 9pt;
}}

th {{
  background: #1a56db;
  color: #ffffff;
  padding: 8px 10px;
  text-align: left;
  font-weight: 600;
  font-size: 9pt;
  border: 1px solid #1a56db;
}}

td {{
  padding: 6px 10px;
  border: 1px solid #d1d5db;
  vertical-align: top;
}}

tr:nth-child(even) {{
  background: #f3f4f6;
}}

tr:nth-child(odd) {{
  background: #ffffff;
}}

blockquote {{
  border-left: 4px solid #1a56db;
  padding: 8px 14px;
  margin: 10px 0;
  background: #e8eefb;
  font-style: italic;
  font-size: 9.5pt;
  color: #374151;
}}

code {{
  background: #f3f4f6;
  padding: 1px 4px;
  border-radius: 3px;
  font-size: 9pt;
  font-family: 'Courier New', monospace;
}}

pre {{
  background: #1f2937;
  color: #e5e7eb;
  padding: 12px;
  border-radius: 6px;
  margin: 10px 0;
  font-size: 8pt;
  line-height: 1.4;
  overflow-wrap: break-word;
  white-space: pre-wrap;
}}

pre code {{
  background: none;
  padding: 0;
  color: inherit;
}}

hr {{
  border: none;
  border-top: 1px solid #d1d5db;
  margin: 16px 0;
}}

strong {{
  color: #111827;
}}

/* Metadata table at top of document */
body > table:first-of-type {{
  max-width: 450px;
  margin: 20px auto;
  border-radius: 6px;
  overflow: hidden;
}}

em {{
  font-size: 9pt;
  color: #6b7280;
}}
</style>
</head>
<body>
{html_content}
</body>
</html>'''

    HTML(string=pdf_html).write_pdf(str(PDF_FILE))
    print(f"[OK] Professional PDF: {PDF_FILE}")


if __name__ == '__main__':
    build_pdf()
