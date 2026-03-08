#!/usr/bin/env python3
"""
Generates the standalone HTML digital dossier and the consolidated SQS document
for the QMS ISO 9001:2015 of Plus Sàrl — v0.7

Dependencies: pip install markdown weasyprint fpdf2
"""

import base64
import re
import subprocess
import markdown
from pathlib import Path

BASE = Path(__file__).parent
OUT = BASE / "export"
OUT.mkdir(exist_ok=True)

# ── Ordered document structure ──────────────────────────────────────────

SECTIONS = [
    ("Quality Manual", [
        ("MQ_01 — Introduction", "manuel_qualite/MQ_01_Introduction.md"),
        ("MQ_02 — Activities and Organization", "manuel_qualite/MQ_02_Activites.md"),
        ("MQ_03 — QMS Support", "manuel_qualite/MQ_03_Support_SMQ.md"),
        ("MQ_04 — Context of the Organization", "manuel_qualite/MQ_04_Contexte.md"),
        ("MQ_05 — Leadership", "manuel_qualite/MQ_05_Leadership.md"),
        ("MQ_06 — Planning", "manuel_qualite/MQ_06_Planification.md"),
        ("MQ_07 — Support", "manuel_qualite/MQ_07_Support.md"),
        ("MQ_08 — Operational Activities", "manuel_qualite/MQ_08_Realisation.md"),
        ("MQ_09 — Performance Evaluation", "manuel_qualite/MQ_09_Evaluation.md"),
        ("MQ_10 — Improvement", "manuel_qualite/MQ_10_Amelioration.md"),
    ]),
    ("Process Sheets", [
        ("PM01 — Strategic Management", "processus/PM01_Leadership.md"),
        ("P01 — Commercial Management", "processus/P01_Commercial.md"),
        ("P02 — Procurement and Sourcing", "processus/P02_Achats_Sous_traitance.md"),
        ("P03 — Quality Control", "processus/P03_Controle_Qualite.md"),
        ("P04 — Logistics and Delivery", "processus/P04_Logistique_Livraison.md"),
        ("PS01 — Document Management", "processus/PS01_Gestion_Documentaire.md"),
        ("PS02 — Competence Management", "processus/PS02_Gestion_Competences.md"),
        ("PS03 — Continuous Improvement", "processus/PS03_Amelioration_Continue.md"),
    ]),
    ("Support Documents", [
        ("Supplier Quality Agreement", "documents/DOC_Accord_Qualite_Fournisseur.md"),
        ("Internal Audit", "documents/DOC_Audit_Interne.md"),
        ("Supplier Evaluation", "documents/DOC_Evaluation_Fournisseur.md"),
        ("Document Management", "documents/DOC_Gestion_Documentaire.md"),
        ("Non-Conformity", "documents/DOC_Non_Conformite.md"),
        ("Quality Objectives", "documents/DOC_Objectifs_Qualite.md"),
        ("Management Review", "documents/DOC_Revue_Direction.md"),
        ("Customer Satisfaction", "documents/DOC_Satisfaction_Client.md"),
    ]),
    ("Process Chains", [
        ("CHAIN-01 — Existing Product Order", "chaines_processus/CHAIN-01_Commande_Produit_Existant.md"),
        ("CHAIN-02 — Tooling Modification", "chaines_processus/CHAIN-02_Commande_Modification_Outillage.md"),
        ("CHAIN-03 — New Tooling", "chaines_processus/CHAIN-03_Commande_Nouvel_Outillage.md"),
        ("CHAIN-04 — Sourcing", "chaines_processus/CHAIN-04_Commande_Sourcing.md"),
    ]),
    ("BLOC Sheets", [
        ("BLOC 001 — Order Reception", "chaines_processus/CH-BLOC-001_Reception_Commande.md"),
        ("BLOC 002 — Order Sheet", "chaines_processus/CH-BLOC-002_Fiche_Commande.md"),
        ("BLOC 003 — Transport Sheet", "chaines_processus/CH-BLOC-003_Fiche_Transport.md"),
        ("BLOC 004 — Technical Study", "chaines_processus/CH-BLOC-004_Etude_Technique.md"),
        ("BLOC 005 — Order Validation", "chaines_processus/CH-BLOC-005_Validation_Commande.md"),
        ("BLOC 006 — Production & Quality", "chaines_processus/CH-BLOC-006_Production_Qualite.md"),
        ("BLOC 007 — Delivery & Customs", "chaines_processus/CH-BLOC-007_Livraison_Douane.md"),
        ("BLOC 008 — Goods Acceptance", "chaines_processus/CH-BLOC-008_Acceptation_Marchandise.md"),
    ]),
]

DIAGRAMS = [
    ("ISO 9001 Process Map", "diagrammes/processus_iso9001.drawio"),
    ("General Process Chain", "diagrammes/chaine_processus_general.drawio"),
]


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def read_md(path):
    full = BASE / path
    if full.exists():
        return full.read_text(encoding='utf-8')
    return f"*File not found: {path}*"


def read_file(path):
    full = BASE / path
    if full.exists():
        return full.read_text(encoding='utf-8')
    return ""


def md_to_html(md_text):
    return markdown.markdown(
        md_text,
        extensions=['tables', 'fenced_code', 'codehilite', 'toc'],
        extension_configs={'codehilite': {'guess_lang': False}}
    )


# ── 1. Standalone HTML generation with drawio diagrams ─────────────────────

def build_html():
    nav_items = []
    content_sections = []

    # -- Document sections --
    for group_name, docs in SECTIONS:
        nav_items.append(f'<div class="nav-group">{group_name}</div>')
        for doc_title, doc_path in docs:
            doc_id = slugify(doc_title)
            nav_items.append(
                f'<a class="nav-link" data-target="{doc_id}" '
                f'href="#{doc_id}">{doc_title}</a>'
            )
            md_content = read_md(doc_path)
            html_content = md_to_html(md_content)
            content_sections.append(
                f'<section id="{doc_id}" class="doc-section">'
                f'{html_content}</section>'
            )

    # -- Diagram sections --
    nav_items.append('<div class="nav-group">Diagrams</div>')
    diagram_data = []
    for diag_title, diag_path in DIAGRAMS:
        diag_id = slugify(diag_title)
        nav_items.append(
            f'<a class="nav-link" data-target="{diag_id}" '
            f'href="#{diag_id}">{diag_title}</a>'
        )
        xml_content = read_file(diag_path)
        b64 = base64.b64encode(xml_content.encode('utf-8')).decode('ascii')
        diagram_data.append((diag_id, diag_title, b64))
        content_sections.append(
            f'<section id="{diag_id}" class="doc-section diagram-section">'
            f'<h1>{diag_title}</h1>'
            f'<div class="diagram-toolbar">'
            f'<button onclick="diagramZoom(\'{diag_id}\', 1.2)">Zoom +</button>'
            f'<button onclick="diagramZoom(\'{diag_id}\', 0.8)">Zoom -</button>'
            f'<button onclick="diagramReset(\'{diag_id}\')">Reset</button>'
            f'<button onclick="diagramFit(\'{diag_id}\')">Fit</button>'
            f'</div>'
            f'<div class="diagram-container" id="container-{diag_id}">'
            f'<div class="diagram-inner" id="inner-{diag_id}" '
            f'data-xml="{b64}"></div>'
            f'</div>'
            f'</section>'
        )

    nav_html = '\n'.join(nav_items)
    content_html = '\n'.join(content_sections)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>QMS ISO 9001:2015 — Plus Sàrl — v0.7</title>
<style>
:root {{
  --sidebar-w: 320px;
  --accent: #1a56db;
  --accent-light: #e8eefb;
  --bg: #f8f9fa;
  --text: #1f2937;
  --border: #d1d5db;
  --header-h: 64px;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; color: var(--text); background: var(--bg); }}

/* Header */
.header {{
  position: fixed; top: 0; left: 0; right: 0; height: var(--header-h);
  background: var(--accent); color: #fff; display: flex; align-items: center;
  padding: 0 24px; z-index: 100; box-shadow: 0 2px 8px rgba(0,0,0,.15);
}}
.header h1 {{ font-size: 18px; font-weight: 600; }}
.header .version {{ margin-left: 16px; background: rgba(255,255,255,.2); padding: 2px 10px; border-radius: 12px; font-size: 13px; }}
.header .company {{ margin-left: auto; font-size: 14px; opacity: .9; }}
.header .menu-btn {{
  display: none; background: none; border: none; color: #fff; font-size: 24px;
  cursor: pointer; margin-right: 12px;
}}

/* Sidebar */
.sidebar {{
  position: fixed; top: var(--header-h); left: 0; bottom: 0; width: var(--sidebar-w);
  background: #fff; border-right: 1px solid var(--border); overflow-y: auto;
  padding: 16px 0; z-index: 90; transition: transform .3s;
}}
.nav-group {{
  padding: 12px 20px 6px; font-size: 11px; text-transform: uppercase;
  letter-spacing: 1px; color: #6b7280; font-weight: 700; margin-top: 8px;
}}
.nav-link {{
  display: block; padding: 7px 20px 7px 28px; font-size: 13px; color: var(--text);
  text-decoration: none; border-left: 3px solid transparent; transition: all .15s;
  line-height: 1.4;
}}
.nav-link:hover {{ background: var(--accent-light); color: var(--accent); }}
.nav-link.active {{ border-left-color: var(--accent); color: var(--accent); background: var(--accent-light); font-weight: 600; }}

/* Search */
.search-box {{
  padding: 8px 16px; margin-bottom: 8px;
}}
.search-box input {{
  width: 100%; padding: 8px 12px; border: 1px solid var(--border); border-radius: 6px;
  font-size: 13px; outline: none;
}}
.search-box input:focus {{ border-color: var(--accent); box-shadow: 0 0 0 3px rgba(26,86,219,.15); }}

/* Content */
.content {{
  margin-left: var(--sidebar-w); margin-top: var(--header-h); padding: 32px 48px 64px;
  max-width: 960px;
}}
.doc-section {{ display: none; }}
.doc-section.active {{ display: block; }}
.doc-section h1 {{ font-size: 24px; margin-bottom: 16px; color: var(--accent); border-bottom: 2px solid var(--accent); padding-bottom: 8px; }}
.doc-section h2 {{ font-size: 20px; margin: 28px 0 12px; color: #374151; }}
.doc-section h3 {{ font-size: 16px; margin: 20px 0 8px; color: #4b5563; }}
.doc-section h4 {{ font-size: 14px; margin: 16px 0 6px; color: #6b7280; }}
.doc-section p {{ margin: 8px 0; line-height: 1.7; }}
.doc-section ul, .doc-section ol {{ margin: 8px 0 8px 24px; line-height: 1.7; }}
.doc-section li {{ margin: 4px 0; }}
.doc-section table {{ width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 13px; }}
.doc-section th {{ background: #f3f4f6; padding: 10px 12px; text-align: left; border: 1px solid var(--border); font-weight: 600; }}
.doc-section td {{ padding: 8px 12px; border: 1px solid var(--border); vertical-align: top; }}
.doc-section tr:nth-child(even) {{ background: #fafbfc; }}
.doc-section blockquote {{ border-left: 4px solid var(--accent); padding: 12px 16px; margin: 12px 0; background: var(--accent-light); font-style: italic; }}
.doc-section code {{ background: #f3f4f6; padding: 2px 6px; border-radius: 3px; font-size: 13px; }}
.doc-section pre {{ background: #1f2937; color: #e5e7eb; padding: 16px; border-radius: 8px; overflow-x: auto; margin: 12px 0; font-size: 12px; line-height: 1.5; }}
.doc-section pre code {{ background: none; padding: 0; color: inherit; }}
.doc-section hr {{ border: none; border-top: 1px solid var(--border); margin: 24px 0; }}
.doc-section strong {{ color: #111827; }}

/* Metadata header */
.doc-section > table:first-child {{ max-width: 500px; background: #f9fafb; border-radius: 8px; overflow: hidden; }}
.doc-section > table:first-child th {{ background: var(--accent); color: #fff; }}

/* Diagram sections */
.diagram-toolbar {{
  display: flex; gap: 8px; margin-bottom: 12px; flex-wrap: wrap;
}}
.diagram-toolbar button {{
  padding: 6px 16px; border: 1px solid var(--border); border-radius: 6px;
  background: #fff; color: var(--text); font-size: 13px; cursor: pointer;
  transition: all .15s;
}}
.diagram-toolbar button:hover {{ background: var(--accent); color: #fff; border-color: var(--accent); }}
.diagram-container {{
  width: 100%; height: calc(100vh - 200px); min-height: 500px;
  border: 1px solid var(--border); border-radius: 8px; overflow: hidden;
  background: #fff; position: relative; cursor: grab;
}}
.diagram-container:active {{ cursor: grabbing; }}
.diagram-inner {{
  position: absolute; top: 0; left: 0;
  transform-origin: 0 0;
  transition: transform 0.1s ease-out;
}}
.diagram-inner svg {{ display: block; }}

/* Print */
@media print {{
  .sidebar, .header, .search-box, .menu-btn, .diagram-toolbar {{ display: none !important; }}
  .content {{ margin: 0; padding: 16px; max-width: 100%; }}
  .doc-section {{ display: block !important; page-break-after: always; }}
  .doc-section:last-child {{ page-break-after: avoid; }}
  .diagram-container {{ height: auto; overflow: visible; }}
}}

/* Mobile */
@media (max-width: 768px) {{
  .header .menu-btn {{ display: block; }}
  .sidebar {{ transform: translateX(-100%); }}
  .sidebar.open {{ transform: translateX(0); box-shadow: 4px 0 16px rgba(0,0,0,.2); }}
  .content {{ margin-left: 0; padding: 20px 16px; }}
}}
</style>
</head>
<body>

<header class="header">
  <button class="menu-btn" onclick="document.querySelector('.sidebar').classList.toggle('open')">&#9776;</button>
  <h1>QMS ISO 9001:2015</h1>
  <span class="version">v0.7</span>
  <span class="company">Plus S&agrave;rl &mdash; Industrial Follow-up &amp; Worldwide Sourcing</span>
</header>

<nav class="sidebar">
  <div class="search-box">
    <input type="text" id="search" placeholder="Search a document..." autocomplete="off">
  </div>
  {nav_html}
</nav>

<main class="content">
  {content_html}
</main>

<script>
// ── Navigation ──
document.querySelectorAll('.nav-link').forEach(link => {{
  link.addEventListener('click', e => {{
    e.preventDefault();
    const id = link.dataset.target;
    document.querySelectorAll('.doc-section').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
    document.getElementById(id).classList.add('active');
    link.classList.add('active');
    window.scrollTo(0, 0);
    document.querySelector('.sidebar').classList.remove('open');
    history.replaceState(null, '', '#' + id);
    // Render diagram if switching to a diagram section
    const inner = document.getElementById('inner-' + id);
    if (inner && !inner.dataset.rendered) renderDiagram(id);
  }});
}});

// ── Search ──
document.getElementById('search').addEventListener('input', e => {{
  const q = e.target.value.toLowerCase();
  document.querySelectorAll('.nav-link').forEach(link => {{
    link.style.display = link.textContent.toLowerCase().includes(q) ? '' : 'none';
  }});
}});

// ── Drawio rendering (pure XML to SVG) ──
const diagramState = {{}};

function parseMxGraphXml(xmlStr) {{
  const parser = new DOMParser();
  const doc = parser.parseFromString(xmlStr, 'text/xml');
  return doc;
}}

function mxCellToSvg(cells, svgEl, bounds) {{
  // Simple renderer: extract geometry and styles from mxCell elements
  cells.forEach(cell => {{
    const geom = cell.querySelector('mxGeometry');
    if (!geom) return;
    const x = parseFloat(geom.getAttribute('x') || 0);
    const y = parseFloat(geom.getAttribute('y') || 0);
    const w = parseFloat(geom.getAttribute('width') || 0);
    const h = parseFloat(geom.getAttribute('height') || 0);
    const style = cell.getAttribute('style') || '';
    const value = cell.getAttribute('value') || '';
    const isEdge = cell.getAttribute('edge') === '1';

    if (isEdge) {{
      // Draw edges as lines
      const source = cell.getAttribute('source');
      const target = cell.getAttribute('target');
      const pts = geom.querySelector('Array');
      // Simple edge: just draw from source to target center
      return; // handled below
    }}

    if (w > 0 && h > 0) {{
      bounds.minX = Math.min(bounds.minX, x);
      bounds.minY = Math.min(bounds.minY, y);
      bounds.maxX = Math.max(bounds.maxX, x + w);
      bounds.maxY = Math.max(bounds.maxY, y + h);

      // Parse fill and stroke from style
      let fill = '#ffffff';
      let stroke = '#333333';
      let fontSize = 12;
      let fontStyle = '';
      let rounded = false;

      style.split(';').forEach(s => {{
        const [k, v] = s.split('=');
        if (k === 'fillColor') fill = v;
        if (k === 'strokeColor') stroke = v;
        if (k === 'fontSize') fontSize = parseInt(v);
        if (k === 'fontStyle' && v === '1') fontStyle = 'font-weight:bold;';
        if (k === 'rounded' && v === '1') rounded = true;
      }});

      if (style.includes('swimlane')) {{
        // Swimlane header
        const startSize = parseInt(style.match(/startSize=(\d+)/)?.[1] || 30);
        const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('x', x); rect.setAttribute('y', y);
        rect.setAttribute('width', w); rect.setAttribute('height', h);
        rect.setAttribute('fill', 'none'); rect.setAttribute('stroke', stroke);
        rect.setAttribute('stroke-width', '1.5');
        if (rounded) rect.setAttribute('rx', '8');
        svgEl.appendChild(rect);

        const headerRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        headerRect.setAttribute('x', x); headerRect.setAttribute('y', y);
        headerRect.setAttribute('width', w); headerRect.setAttribute('height', startSize);
        headerRect.setAttribute('fill', fill); headerRect.setAttribute('stroke', stroke);
        headerRect.setAttribute('stroke-width', '1.5');
        if (rounded) headerRect.setAttribute('rx', '8');
        svgEl.appendChild(headerRect);

        if (value) {{
          const text = document.createElementNS('http://www.w3.org/2000/svg', 'foreignObject');
          text.setAttribute('x', x + 4); text.setAttribute('y', y + 2);
          text.setAttribute('width', w - 8); text.setAttribute('height', startSize - 4);
          const div = document.createElement('div');
          div.setAttribute('xmlns', 'http://www.w3.org/1999/xhtml');
          div.style.cssText = `font-size:${{fontSize}}px;${{fontStyle}}text-align:center;color:#333;line-height:${{startSize-4}}px;overflow:hidden;font-family:sans-serif;`;
          div.innerHTML = value;
          text.appendChild(div);
          svgEl.appendChild(text);
        }}
      }} else if (style.includes('text;') || style.includes('text;html=1')) {{
        // Text element
        if (value) {{
          const text = document.createElementNS('http://www.w3.org/2000/svg', 'foreignObject');
          text.setAttribute('x', x); text.setAttribute('y', y);
          text.setAttribute('width', w); text.setAttribute('height', h);
          const div = document.createElement('div');
          div.setAttribute('xmlns', 'http://www.w3.org/1999/xhtml');
          div.style.cssText = `font-size:${{fontSize}}px;${{fontStyle}}text-align:center;display:flex;align-items:center;justify-content:center;height:100%;color:#333;font-family:sans-serif;padding:2px;`;
          div.innerHTML = value;
          text.appendChild(div);
          svgEl.appendChild(text);
        }}
      }} else {{
        // Regular shape
        if (style.includes('ellipse')) {{
          const el = document.createElementNS('http://www.w3.org/2000/svg', 'ellipse');
          el.setAttribute('cx', x + w/2); el.setAttribute('cy', y + h/2);
          el.setAttribute('rx', w/2); el.setAttribute('ry', h/2);
          el.setAttribute('fill', fill); el.setAttribute('stroke', stroke);
          el.setAttribute('stroke-width', '1.5');
          svgEl.appendChild(el);
        }} else if (style.includes('rhombus')) {{
          const pts = `${{x+w/2}},${{y}} ${{x+w}},${{y+h/2}} ${{x+w/2}},${{y+h}} ${{x}},${{y+h/2}}`;
          const el = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
          el.setAttribute('points', pts);
          el.setAttribute('fill', fill); el.setAttribute('stroke', stroke);
          el.setAttribute('stroke-width', '1.5');
          svgEl.appendChild(el);
        }} else {{
          const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
          rect.setAttribute('x', x); rect.setAttribute('y', y);
          rect.setAttribute('width', w); rect.setAttribute('height', h);
          rect.setAttribute('fill', fill); rect.setAttribute('stroke', stroke);
          rect.setAttribute('stroke-width', '1.5');
          if (rounded || style.includes('rounded=1')) rect.setAttribute('rx', '8');
          svgEl.appendChild(rect);
        }}

        if (value) {{
          const text = document.createElementNS('http://www.w3.org/2000/svg', 'foreignObject');
          text.setAttribute('x', x + 4); text.setAttribute('y', y + 2);
          text.setAttribute('width', w - 8); text.setAttribute('height', h - 4);
          const div = document.createElement('div');
          div.setAttribute('xmlns', 'http://www.w3.org/1999/xhtml');
          div.style.cssText = `font-size:${{Math.min(fontSize, 11)}}px;${{fontStyle}}text-align:center;display:flex;align-items:center;justify-content:center;height:100%;color:#333;font-family:sans-serif;line-height:1.3;overflow:hidden;padding:2px;`;
          div.innerHTML = value;
          text.appendChild(div);
          svgEl.appendChild(text);
        }}
      }}
    }}
  }});
}}

function drawEdges(cells, svgEl, allCells) {{
  // Build a map of cell id -> center coordinates
  const centers = {{}};
  allCells.forEach(cell => {{
    const geom = cell.querySelector('mxGeometry');
    if (!geom) return;
    const x = parseFloat(geom.getAttribute('x') || 0);
    const y = parseFloat(geom.getAttribute('y') || 0);
    const w = parseFloat(geom.getAttribute('width') || 0);
    const h = parseFloat(geom.getAttribute('height') || 0);
    if (w > 0 && h > 0) {{
      centers[cell.getAttribute('id')] = {{ x: x + w/2, y: y + h/2, w, h, left: x, top: y }};
    }}
  }});

  // Add arrowhead marker
  let defs = svgEl.querySelector('defs');
  if (!defs) {{
    defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
    svgEl.insertBefore(defs, svgEl.firstChild);
  }}
  if (!defs.querySelector('#arrowhead')) {{
    const marker = document.createElementNS('http://www.w3.org/2000/svg', 'marker');
    marker.setAttribute('id', 'arrowhead');
    marker.setAttribute('markerWidth', '10'); marker.setAttribute('markerHeight', '7');
    marker.setAttribute('refX', '9'); marker.setAttribute('refY', '3.5');
    marker.setAttribute('orient', 'auto');
    const poly = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
    poly.setAttribute('points', '0 0, 10 3.5, 0 7');
    poly.setAttribute('fill', '#666');
    marker.appendChild(poly);
    defs.appendChild(marker);
  }}

  cells.forEach(cell => {{
    if (cell.getAttribute('edge') !== '1') return;
    const srcId = cell.getAttribute('source');
    const tgtId = cell.getAttribute('target');
    const src = centers[srcId];
    const tgt = centers[tgtId];
    if (!src || !tgt) return;

    const style = cell.getAttribute('style') || '';
    let strokeColor = '#666666';
    style.split(';').forEach(s => {{
      const [k, v] = s.split('=');
      if (k === 'strokeColor') strokeColor = v;
    }});

    const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    line.setAttribute('x1', src.x); line.setAttribute('y1', src.y);
    line.setAttribute('x2', tgt.x); line.setAttribute('y2', tgt.y);
    line.setAttribute('stroke', strokeColor);
    line.setAttribute('stroke-width', '1.5');
    line.setAttribute('marker-end', 'url(#arrowhead)');
    svgEl.appendChild(line);

    // Edge label
    const value = cell.getAttribute('value');
    if (value) {{
      const mx = (src.x + tgt.x) / 2;
      const my = (src.y + tgt.y) / 2;
      const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      text.setAttribute('x', mx); text.setAttribute('y', my - 4);
      text.setAttribute('text-anchor', 'middle');
      text.setAttribute('font-size', '10');
      text.setAttribute('fill', '#666');
      text.setAttribute('font-family', 'sans-serif');
      text.textContent = value.replace(/<[^>]+>/g, '');
      svgEl.appendChild(text);
    }}
  }});
}}

function renderDiagram(diagId) {{
  const inner = document.getElementById('inner-' + diagId);
  if (!inner || inner.dataset.rendered) return;
  inner.dataset.rendered = 'true';

  const xmlB64 = inner.dataset.xml;
  const xmlStr = atob(xmlB64);
  const doc = parseMxGraphXml(xmlStr);

  const cells = Array.from(doc.querySelectorAll('mxCell'));
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.style.overflow = 'visible';

  const bounds = {{ minX: Infinity, minY: Infinity, maxX: -Infinity, maxY: -Infinity }};
  mxCellToSvg(cells, svg, bounds);
  drawEdges(cells, svg, cells);

  const pad = 40;
  const vw = bounds.maxX - bounds.minX + pad * 2;
  const vh = bounds.maxY - bounds.minY + pad * 2;
  svg.setAttribute('viewBox', `${{bounds.minX - pad}} ${{bounds.minY - pad}} ${{vw}} ${{vh}}`);
  svg.setAttribute('width', vw);
  svg.setAttribute('height', vh);

  inner.appendChild(svg);

  // Fit to container
  const container = document.getElementById('container-' + diagId);
  const scale = Math.min(container.clientWidth / vw, container.clientHeight / vh, 1);
  diagramState[diagId] = {{ scale, tx: 0, ty: 0, vw, vh }};
  inner.style.transform = `scale(${{scale}})`;

  // Pan support
  let dragging = false, lastX = 0, lastY = 0;
  container.addEventListener('mousedown', e => {{ dragging = true; lastX = e.clientX; lastY = e.clientY; }});
  container.addEventListener('mousemove', e => {{
    if (!dragging) return;
    const st = diagramState[diagId];
    st.tx += e.clientX - lastX;
    st.ty += e.clientY - lastY;
    lastX = e.clientX; lastY = e.clientY;
    inner.style.transform = `translate(${{st.tx}}px, ${{st.ty}}px) scale(${{st.scale}})`;
  }});
  container.addEventListener('mouseup', () => {{ dragging = false; }});
  container.addEventListener('mouseleave', () => {{ dragging = false; }});

  // Mouse wheel zoom
  container.addEventListener('wheel', e => {{
    e.preventDefault();
    const factor = e.deltaY > 0 ? 0.9 : 1.1;
    diagramZoom(diagId, factor);
  }}, {{ passive: false }});
}}

function diagramZoom(diagId, factor) {{
  const st = diagramState[diagId];
  if (!st) return;
  st.scale *= factor;
  const inner = document.getElementById('inner-' + diagId);
  inner.style.transform = `translate(${{st.tx}}px, ${{st.ty}}px) scale(${{st.scale}})`;
}}

function diagramReset(diagId) {{
  const st = diagramState[diagId];
  if (!st) return;
  st.scale = 1; st.tx = 0; st.ty = 0;
  const inner = document.getElementById('inner-' + diagId);
  inner.style.transform = `scale(1)`;
}}

function diagramFit(diagId) {{
  const st = diagramState[diagId];
  if (!st) return;
  const container = document.getElementById('container-' + diagId);
  st.scale = Math.min(container.clientWidth / st.vw, container.clientHeight / st.vh, 1.5);
  st.tx = 0; st.ty = 0;
  const inner = document.getElementById('inner-' + diagId);
  inner.style.transform = `scale(${{st.scale}})`;
}}

// Init: show section from hash or first
(function() {{
  const hash = location.hash.slice(1);
  const target = hash ? document.getElementById(hash) : document.querySelector('.doc-section');
  if (target) {{
    target.classList.add('active');
    const link = document.querySelector('.nav-link[data-target="' + target.id + '"]');
    if (link) link.classList.add('active');
    // Render diagram if needed
    const inner = document.getElementById('inner-' + target.id);
    if (inner) renderDiagram(target.id);
  }}
}})();
</script>
</body>
</html>'''

    out_file = OUT / "SMQ_Plus_Sarl_v0.7.html"
    out_file.write_text(html, encoding='utf-8')
    print(f"[OK] Standalone HTML dossier: {out_file}")
    return out_file


# ── 2. Professional PDF generation via weasyprint ───────────────────────────

def build_pdf():
    """Generates a professional PDF via HTML + CSS + weasyprint."""
    from weasyprint import HTML

    # Build all sections as HTML
    body_parts = []

    # -- Cover page --
    body_parts.append('''
    <div class="cover-page">
      <div class="cover-top-bar"></div>
      <div class="cover-content">
        <div class="cover-badge">ISO 9001:2015</div>
        <h1 class="cover-title">Quality Management<br>System</h1>
        <div class="cover-separator"></div>
        <h2 class="cover-subtitle">Certification Dossier</h2>
        <div class="cover-company">Plus Sàrl</div>
        <div class="cover-activity">Industrial Follow-up &amp; Worldwide Sourcing</div>
        <div class="cover-meta">
          <table>
            <tr><td class="label">Version</td><td>0.7</td></tr>
            <tr><td class="label">Date</td><td>March 2026</td></tr>
            <tr><td class="label">Classification</td><td>Confidential</td></tr>
            <tr><td class="label">Recipient</td><td>SQS — Certification Body</td></tr>
          </table>
        </div>
      </div>
      <div class="cover-footer">
        <p>This document is the property of Plus Sàrl. Any unauthorized reproduction or distribution is prohibited.</p>
      </div>
    </div>
    ''')

    # -- Table of contents page --
    toc_items = []
    doc_counter = 0
    for group_name, docs in SECTIONS:
        toc_items.append(f'<div class="toc-group">{group_name}</div>')
        for doc_title, _ in docs:
            doc_counter += 1
            toc_items.append(f'<div class="toc-item"><span class="toc-num">{doc_counter}.</span> {doc_title}</div>')

    body_parts.append(f'''
    <div class="toc-page">
      <h1 class="toc-title">Table of Contents</h1>
      <div class="toc-list">
        {''.join(toc_items)}
      </div>
    </div>
    ''')

    # -- Document sections --
    for group_name, docs in SECTIONS:
        # Part separator page
        body_parts.append(f'''
        <div class="part-page">
          <div class="part-decoration"></div>
          <h1 class="part-title">{group_name}</h1>
          <div class="part-line"></div>
          <p class="part-count">{len(docs)} document{"s" if len(docs) > 1 else ""}</p>
        </div>
        ''')

        for doc_title, doc_path in docs:
            md_content = read_md(doc_path)
            html_content = md_to_html(md_content)
            body_parts.append(f'''
            <div class="document-section">
              {html_content}
            </div>
            ''')

    content = '\n'.join(body_parts)

    pdf_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
@page {{
  size: A4;
  margin: 25mm 20mm 30mm 20mm;
  @top-left {{
    content: "QMS ISO 9001:2015 — Plus Sàrl";
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

/* ── Cover Page ── */
.cover-page {{
  page: cover;
  page-break-after: always;
  height: 297mm;
  display: flex;
  flex-direction: column;
  position: relative;
  padding: 0;
}}
.cover-top-bar {{
  height: 8mm;
  background: linear-gradient(135deg, #1a56db, #2563eb);
  width: 100%;
}}
.cover-content {{
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 30mm 25mm;
  text-align: center;
}}
.cover-badge {{
  background: #1a56db;
  color: #fff;
  padding: 8px 28px;
  border-radius: 24px;
  font-size: 14pt;
  font-weight: 700;
  letter-spacing: 2px;
  margin-bottom: 20mm;
}}
.cover-title {{
  font-size: 28pt;
  font-weight: 700;
  color: #111827;
  margin: 0 0 8mm;
  line-height: 1.2;
}}
.cover-separator {{
  width: 60mm;
  height: 1mm;
  background: #1a56db;
  margin: 0 auto 8mm;
}}
.cover-subtitle {{
  font-size: 16pt;
  font-weight: 400;
  color: #4b5563;
  margin: 0 0 15mm;
}}
.cover-company {{
  font-size: 20pt;
  font-weight: 700;
  color: #1a56db;
  margin: 0 0 3mm;
}}
.cover-activity {{
  font-size: 11pt;
  color: #6b7280;
  margin: 0 0 15mm;
}}
.cover-meta {{
  margin-top: 10mm;
}}
.cover-meta table {{
  border-collapse: collapse;
  margin: 0 auto;
}}
.cover-meta td {{
  padding: 4px 16px;
  font-size: 10pt;
  color: #374151;
  border-bottom: 1px solid #e5e7eb;
}}
.cover-meta td.label {{
  font-weight: 600;
  color: #1a56db;
  text-align: right;
}}
.cover-footer {{
  background: #f3f4f6;
  padding: 6mm 20mm;
  text-align: center;
  font-size: 7pt;
  color: #9ca3af;
}}

/* ── Table of Contents ── */
.toc-page {{
  page-break-after: always;
}}
.toc-title {{
  font-size: 20pt;
  color: #1a56db;
  border-bottom: 3px solid #1a56db;
  padding-bottom: 8px;
  margin-bottom: 16px;
}}
.toc-group {{
  font-size: 11pt;
  font-weight: 700;
  color: #1a56db;
  margin: 14px 0 6px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  border-left: 4px solid #1a56db;
  padding-left: 10px;
}}
.toc-item {{
  font-size: 9.5pt;
  color: #374151;
  padding: 3px 0 3px 18px;
  border-bottom: 1px dotted #d1d5db;
}}
.toc-num {{
  color: #6b7280;
  margin-right: 6px;
  font-variant-numeric: tabular-nums;
}}

/* ── Part Separator ── */
.part-page {{
  page-break-before: always;
  page-break-after: always;
  height: 200mm;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}}
.part-decoration {{
  width: 20mm;
  height: 2mm;
  background: #1a56db;
  margin-bottom: 12mm;
  border-radius: 1mm;
}}
.part-title {{
  font-size: 26pt;
  color: #1a56db;
  font-weight: 700;
  margin: 0 0 8mm;
}}
.part-line {{
  width: 80mm;
  height: 0.5mm;
  background: #d1d5db;
  margin-bottom: 8mm;
}}
.part-count {{
  font-size: 11pt;
  color: #6b7280;
}}

/* ── Document Content ── */
.document-section {{
  page-break-before: always;
}}
.document-section h1 {{
  font-size: 16pt;
  color: #1a56db;
  border-bottom: 2px solid #1a56db;
  padding-bottom: 6px;
  margin: 0 0 12px;
}}
.document-section h2 {{
  font-size: 13pt;
  color: #374151;
  margin: 18px 0 8px;
  border-left: 4px solid #1a56db;
  padding-left: 10px;
}}
.document-section h3 {{
  font-size: 11pt;
  color: #4b5563;
  margin: 14px 0 6px;
}}
.document-section h4 {{
  font-size: 10pt;
  color: #6b7280;
  margin: 10px 0 4px;
  font-style: italic;
}}
.document-section p {{
  margin: 6px 0;
  text-align: justify;
  line-height: 1.65;
}}
.document-section ul, .document-section ol {{
  margin: 6px 0 6px 18px;
  line-height: 1.6;
}}
.document-section li {{
  margin: 3px 0;
}}
.document-section table {{
  width: 100%;
  border-collapse: collapse;
  margin: 10px 0;
  font-size: 9pt;
}}
.document-section th {{
  background: #1a56db;
  color: #ffffff;
  padding: 8px 10px;
  text-align: left;
  font-weight: 600;
  font-size: 9pt;
  border: 1px solid #1a56db;
}}
.document-section td {{
  padding: 6px 10px;
  border: 1px solid #d1d5db;
  vertical-align: top;
}}
.document-section tr:nth-child(even) {{
  background: #f3f4f6;
}}
.document-section tr:nth-child(odd) {{
  background: #ffffff;
}}
.document-section blockquote {{
  border-left: 4px solid #1a56db;
  padding: 8px 14px;
  margin: 10px 0;
  background: #e8eefb;
  font-style: italic;
  font-size: 9.5pt;
  color: #374151;
}}
.document-section code {{
  background: #f3f4f6;
  padding: 1px 4px;
  border-radius: 3px;
  font-size: 9pt;
  font-family: 'Courier New', monospace;
}}
.document-section pre {{
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
.document-section pre code {{
  background: none;
  padding: 0;
  color: inherit;
}}
.document-section hr {{
  border: none;
  border-top: 1px solid #d1d5db;
  margin: 16px 0;
}}
.document-section strong {{
  color: #111827;
}}

/* First table in section = metadata header */
.document-section > table:first-child {{
  max-width: 300px;
  margin-bottom: 16px;
  border-radius: 6px;
  overflow: hidden;
}}
</style>
</head>
<body>
{content}
</body>
</html>'''

    pdf_file = OUT / "SMQ_Plus_Sarl_v0.7_SQS.pdf"
    HTML(string=pdf_html).write_pdf(str(pdf_file))
    print(f"[OK] Professional PDF: {pdf_file}")
    return pdf_file


# ── 3. Enhanced DOCX generation ──────────────────────────────────────────────

def build_docx():
    """Generates a consolidated DOCX via pandoc with enhanced styles."""
    parts = []

    # Title page content
    parts.append("""---
title: "Quality Management System ISO 9001:2015"
subtitle: "Certification Dossier — Plus Sàrl"
author: "Plus Sàrl — Industrial Follow-up & Worldwide Sourcing"
date: "March 2026 — Version 0.7"
---

\\newpage

# QMS Dossier — Plus Sàrl

| | |
|---|---|
| **Purpose** | Presentation of the QMS for ISO 9001:2015 certification |
| **Organization** | Plus Sàrl |
| **Activity** | Industrial monitoring and worldwide sourcing |
| **Version** | v0.7 |
| **Date** | March 2026 |
| **Classification** | Confidential — For the attention of the SQS certification body |

\\newpage

""")

    part_num = 0
    for group_name, docs in SECTIONS:
        part_num += 1
        parts.append(f"\n\n\\newpage\n\n# Part {part_num} — {group_name}\n\n---\n\n")
        for doc_title, doc_path in docs:
            md = read_md(doc_path)
            parts.append(f"\n\n\\newpage\n\n{md}\n\n")

    consolidated = '\n'.join(parts)
    md_file = OUT / "SMQ_Plus_Sarl_v0.7_SQS.md"
    md_file.write_text(consolidated, encoding='utf-8')
    print(f"[OK] Consolidated MD document: {md_file}")

    # DOCX via pandoc
    docx_file = OUT / "SMQ_Plus_Sarl_v0.7_SQS.docx"
    try:
        subprocess.run([
            'pandoc', str(md_file),
            '-o', str(docx_file),
            '--toc', '--toc-depth=3',
            '--highlight-style=tango',
            '-V', 'toc-title=Table of Contents',
        ], check=True, capture_output=True, text=True)
        print(f"[OK] DOCX: {docx_file}")
    except subprocess.CalledProcessError as e:
        print(f"[!!] DOCX failed: {e.stderr}")

    return md_file, docx_file


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 60)
    print("  QMS Dossier Generation — Plus Sàrl v0.7")
    print("=" * 60)
    print()
    build_html()
    print()
    build_pdf()
    print()
    build_docx()
    print()
    print("=" * 60)
    print(f"  Files generated in: {OUT}")
    print("=" * 60)
