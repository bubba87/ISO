#!/usr/bin/env python3
"""
Troisième passe — correction des accents DANS les blocs de code (diagrammes ASCII).
"""

import re
import os

REPLACEMENTS = {
    "delais": "délais",
    "delai": "délai",
    "echantillons": "échantillons",
    "echantillon": "échantillon",
    "parallele": "parallèle",
    "aerien": "aérien",
    "necessaire": "nécessaire",
    "necessaires": "nécessaires",
    "quantites": "quantités",
    "qualite": "qualité",
    "responsabilites": "responsabilités",
    "definies": "définies",
    "faisabilite": "faisabilité",
    "conformite": "conformité",
    "Delais": "Délais",
    "etape": "étape",
    "echanges": "échanges",
    "Echanges": "Échanges",
    "pieces": "pièces",
    "aupres": "auprès",
    "expedition": "expédition",
    "realise": "réalise",
    "Creation": "Création",
    "legislation": "législation",
    "souhaite": "souhaité",
    "detectee": "détectée",
    "detectees": "détectées",
    "Verification": "Vérification",
    "reception": "réception",
    "Comprehension": "Compréhension",
    "References": "Références",
    "Accuse": "Accusé",
}

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Find code blocks and apply replacements inside them
    parts = re.split(r'(```.*?```)', content, flags=re.DOTALL)

    for i in range(len(parts)):
        # Only process code blocks (odd indices)
        if i % 2 == 0:
            continue

        text = parts[i]
        sorted_replacements = sorted(REPLACEMENTS.items(), key=lambda x: len(x[0]), reverse=True)
        for old, new in sorted_replacements:
            pattern = r'\b' + re.escape(old) + r'\b'
            text = re.sub(pattern, new, text)
        parts[i] = text

    content = ''.join(parts)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    md_files = []
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in ['.git', 'en']]
        for f in files:
            if f.endswith('.md'):
                md_files.append(os.path.join(root, f))

    md_files.sort()

    modified = 0
    for filepath in md_files:
        rel_path = os.path.relpath(filepath, base_dir)
        if fix_file(filepath):
            modified += 1
            print(f"  ✓ Corrigé (blocs code) : {rel_path}")

    print(f"\nRésultat : {modified} fichiers modifiés (blocs de code)")


if __name__ == '__main__':
    main()
