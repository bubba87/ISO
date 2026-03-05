#!/usr/bin/env python3
"""
Génère le dossier numérique HTML standalone et le document consolidé SQS
pour le SMQ ISO 9001:2015 de Plus Sàrl — v0.7
"""

import os
import re
import subprocess
import markdown
from pathlib import Path

BASE = Path(__file__).parent
OUT = BASE / "export"
OUT.mkdir(exist_ok=True)

# ── Structure ordonnée des documents ──────────────────────────────────────────

SECTIONS = [
    ("Manuel Qualité", [
        ("MQ_01 — Introduction", "manuel_qualite/MQ_01_Introduction.md"),
        ("MQ_02 — Activités et Organisation", "manuel_qualite/MQ_02_Activites.md"),
        ("MQ_03 — Support du SMQ", "manuel_qualite/MQ_03_Support_SMQ.md"),
        ("MQ_04 — Contexte de l'organisme", "manuel_qualite/MQ_04_Contexte.md"),
        ("MQ_05 — Leadership", "manuel_qualite/MQ_05_Leadership.md"),
        ("MQ_06 — Planification", "manuel_qualite/MQ_06_Planification.md"),
        ("MQ_07 — Support", "manuel_qualite/MQ_07_Support.md"),
        ("MQ_08 — Réalisation", "manuel_qualite/MQ_08_Realisation.md"),
        ("MQ_09 — Évaluation des performances", "manuel_qualite/MQ_09_Evaluation.md"),
        ("MQ_10 — Amélioration", "manuel_qualite/MQ_10_Amelioration.md"),
    ]),
    ("Fiches Processus", [
        ("PM01 — Pilotage stratégique", "processus/PM01_Leadership.md"),
        ("P01 — Gestion commerciale", "processus/P01_Commercial.md"),
        ("P02 — Achats et sourcing", "processus/P02_Achats_Sous_traitance.md"),
        ("P03 — Contrôle qualité", "processus/P03_Controle_Qualite.md"),
        ("P04 — Logistique et livraison", "processus/P04_Logistique_Livraison.md"),
        ("PS01 — Gestion documentaire", "processus/PS01_Gestion_Documentaire.md"),
        ("PS02 — Gestion des compétences", "processus/PS02_Gestion_Competences.md"),
        ("PS03 — Amélioration continue", "processus/PS03_Amelioration_Continue.md"),
    ]),
    ("Documents Support", [
        ("Accord Qualité Fournisseur", "documents/DOC_Accord_Qualite_Fournisseur.md"),
        ("Audit Interne", "documents/DOC_Audit_Interne.md"),
        ("Évaluation Fournisseur", "documents/DOC_Evaluation_Fournisseur.md"),
        ("Gestion Documentaire", "documents/DOC_Gestion_Documentaire.md"),
        ("Non-Conformité", "documents/DOC_Non_Conformite.md"),
        ("Objectifs Qualité", "documents/DOC_Objectifs_Qualite.md"),
        ("Revue de Direction", "documents/DOC_Revue_Direction.md"),
        ("Satisfaction Client", "documents/DOC_Satisfaction_Client.md"),
    ]),
    ("Chaînes de Processus", [
        ("CHAIN-01 — Commande Produit Existant", "chaines_processus/CHAIN-01_Commande_Produit_Existant.md"),
        ("CHAIN-02 — Modification Outillage", "chaines_processus/CHAIN-02_Commande_Modification_Outillage.md"),
        ("CHAIN-03 — Nouvel Outillage", "chaines_processus/CHAIN-03_Commande_Nouvel_Outillage.md"),
        ("CHAIN-04 — Sourcing", "chaines_processus/CHAIN-04_Commande_Sourcing.md"),
    ]),
    ("Fiches BLOC", [
        ("BLOC 001 — Réception Commande", "chaines_processus/CH-BLOC-001_Reception_Commande.md"),
        ("BLOC 002 — Fiche Commande", "chaines_processus/CH-BLOC-002_Fiche_Commande.md"),
        ("BLOC 003 — Fiche Transport", "chaines_processus/CH-BLOC-003_Fiche_Transport.md"),
        ("BLOC 004 — Étude Technique", "chaines_processus/CH-BLOC-004_Etude_Technique.md"),
        ("BLOC 005 — Validation Commande", "chaines_processus/CH-BLOC-005_Validation_Commande.md"),
        ("BLOC 006 — Production & Qualité", "chaines_processus/CH-BLOC-006_Production_Qualite.md"),
        ("BLOC 007 — Livraison & Douane", "chaines_processus/CH-BLOC-007_Livraison_Douane.md"),
        ("BLOC 008 — Acceptation Marchandise", "chaines_processus/CH-BLOC-008_Acceptation_Marchandise.md"),
    ]),
]


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def read_md(path):
    full = BASE / path
    if full.exists():
        return full.read_text(encoding='utf-8')
    return f"*Fichier non trouvé : {path}*"


def md_to_html(md_text):
    return markdown.markdown(
        md_text,
        extensions=['tables', 'fenced_code', 'codehilite', 'toc'],
        extension_configs={'codehilite': {'guess_lang': False}}
    )


# ── 1. Génération HTML standalone ─────────────────────────────────────────────

def build_html():
    nav_items = []
    content_sections = []
    first_id = None

    for group_name, docs in SECTIONS:
        group_slug = slugify(group_name)
        nav_items.append(f'<div class="nav-group">{group_name}</div>')

        for doc_title, doc_path in docs:
            doc_id = slugify(doc_title)
            if first_id is None:
                first_id = doc_id
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

    nav_html = '\n'.join(nav_items)
    content_html = '\n'.join(content_sections)

    html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SMQ ISO 9001:2015 — Plus Sàrl — v0.7</title>
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

/* Cartouche metadata */
.doc-section > table:first-child {{ max-width: 500px; background: #f9fafb; border-radius: 8px; overflow: hidden; }}
.doc-section > table:first-child th {{ background: var(--accent); color: #fff; }}

/* Print */
@media print {{
  .sidebar, .header, .search-box, .menu-btn {{ display: none !important; }}
  .content {{ margin: 0; padding: 16px; max-width: 100%; }}
  .doc-section {{ display: block !important; page-break-after: always; }}
  .doc-section:last-child {{ page-break-after: avoid; }}
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
  <h1>SMQ ISO 9001:2015</h1>
  <span class="version">v0.7</span>
  <span class="company">Plus Sàrl — Monitoring industriel &amp; Sourcing mondial</span>
</header>

<nav class="sidebar">
  <div class="search-box">
    <input type="text" id="search" placeholder="Rechercher un document..." autocomplete="off">
  </div>
  {nav_html}
</nav>

<main class="content">
  {content_html}
</main>

<script>
// Navigation
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
  }});
}});

// Search
document.getElementById('search').addEventListener('input', e => {{
  const q = e.target.value.toLowerCase();
  document.querySelectorAll('.nav-link').forEach(link => {{
    link.style.display = link.textContent.toLowerCase().includes(q) ? '' : 'none';
  }});
}});

// Init: show section from hash or first
(function() {{
  const hash = location.hash.slice(1);
  const target = hash ? document.getElementById(hash) : document.querySelector('.doc-section');
  if (target) {{
    target.classList.add('active');
    const link = document.querySelector('.nav-link[data-target="' + target.id + '"]');
    if (link) link.classList.add('active');
  }}
}})();
</script>
</body>
</html>'''

    out_file = OUT / "SMQ_Plus_Sarl_v0.7.html"
    out_file.write_text(html, encoding='utf-8')
    print(f"[OK] Dossier HTML standalone : {out_file}")
    return out_file


# ── 2. Génération du document consolidé SQS ───────────────────────────────────

def build_sqs_document():
    parts = []

    # Page de titre (en markdown)
    parts.append("""---
title: "Système de Management de la Qualité ISO 9001:2015"
subtitle: "Dossier de certification — Plus Sàrl"
author: "Plus Sàrl — Monitoring industriel & Sourcing mondial"
date: "Mars 2026 — Version 0.7"
---

\\newpage

# Dossier SMQ — Plus Sàrl

**Objet** : Présentation du Système de Management de la Qualité de Plus Sàrl en vue de la certification ISO 9001:2015

**Organisme** : Plus Sàrl
**Activité** : Monitoring industriel et sourcing à l'échelle mondiale
**Version** : v0.7
**Date** : Mars 2026
**Classification** : Confidentiel — À l'attention de l'organisme de certification

---

## Table des matières

### Partie I — Manuel Qualité (Chapitres 1 à 10)
### Partie II — Fiches Processus (PM01, P01-P04, PS01-PS03)
### Partie III — Documents Support (Formulaires et registres)
### Partie IV — Chaînes de Processus et Fiches BLOC

\\newpage

""")

    for group_name, docs in SECTIONS:
        parts.append(f"\n\n\\newpage\n\n# PARTIE : {group_name}\n\n---\n\n")
        for doc_title, doc_path in docs:
            md = read_md(doc_path)
            parts.append(f"\n\n\\newpage\n\n{md}\n\n")

    consolidated = '\n'.join(parts)
    md_file = OUT / "SMQ_Plus_Sarl_v0.7_SQS.md"
    md_file.write_text(consolidated, encoding='utf-8')
    print(f"[OK] Document consolidé MD : {md_file}")

    # PDF via pandoc
    pdf_file = OUT / "SMQ_Plus_Sarl_v0.7_SQS.pdf"
    try:
        subprocess.run([
            'pandoc', str(md_file),
            '-o', str(pdf_file),
            '--pdf-engine=pdflatex',
            '-V', 'geometry:margin=2.5cm',
            '-V', 'fontsize=11pt',
            '-V', 'documentclass=report',
            '-V', 'lang=fr',
            '--toc', '--toc-depth=3',
            '-V', 'toc-title=Table des matières',
            '-V', 'mainfont=DejaVu Sans',
            '--highlight-style=tango',
        ], check=True, capture_output=True, text=True)
        print(f"[OK] PDF : {pdf_file}")
    except subprocess.CalledProcessError as e:
        print(f"[!!] PDF pdflatex échoué, tentative avec wkhtmltopdf...")
        try:
            html_tmp = OUT / "_tmp_sqs.html"
            subprocess.run([
                'pandoc', str(md_file),
                '-o', str(html_tmp),
                '--standalone', '--toc', '--toc-depth=3',
                '-c', '',  # no external css
                '--metadata', 'title=SMQ Plus Sàrl v0.7',
            ], check=True, capture_output=True, text=True)
            # Try weasyprint or just keep HTML
            try:
                subprocess.run([
                    'pandoc', str(md_file),
                    '-o', str(pdf_file),
                    '--pdf-engine=weasyprint',
                    '--toc', '--toc-depth=3',
                ], check=True, capture_output=True, text=True)
                print(f"[OK] PDF (weasyprint) : {pdf_file}")
            except Exception:
                print(f"[!!] PDF non généré — utilisez le HTML standalone ou convertissez le DOCX")
        except Exception:
            print(f"[!!] PDF non généré — utilisez le HTML standalone ou convertissez le DOCX")

    # DOCX via pandoc
    docx_file = OUT / "SMQ_Plus_Sarl_v0.7_SQS.docx"
    try:
        subprocess.run([
            'pandoc', str(md_file),
            '-o', str(docx_file),
            '--toc', '--toc-depth=3',
            '--highlight-style=tango',
        ], check=True, capture_output=True, text=True)
        print(f"[OK] DOCX : {docx_file}")
    except subprocess.CalledProcessError as e:
        print(f"[!!] DOCX échoué : {e.stderr}")

    return md_file, pdf_file, docx_file


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 60)
    print("  Génération du dossier SMQ Plus Sàrl v0.7")
    print("=" * 60)
    print()
    build_html()
    print()
    build_sqs_document()
    print()
    print("=" * 60)
    print(f"  Fichiers générés dans : {OUT}")
    print("=" * 60)
