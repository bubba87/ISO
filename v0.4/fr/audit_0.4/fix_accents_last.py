#!/usr/bin/env python3
"""
Dernière passe — mots restants.
"""

import re
import os

REPLACEMENTS = {
    # --- formalites ---
    "formalites": "formalités",
    "Formalites": "Formalités",

    # --- examinee ---
    "examinee": "examinée",
    "examinees": "examinées",

    # --- detaillant ---
    "detaillant": "détaillant",
    "detaillee": "détaillée",
    "detaillees": "détaillées",
    "detailles": "détaillés",
    "detaille": "détaillé",

    # --- penalites ---
    "penalites": "pénalités",
    "penalite": "pénalité",

    # --- immediatement ---
    "immediatement": "immédiatement",

    # --- conformement ---
    "conformement": "conformément",

    # --- Entree ---
    "Entree": "Entrée",
    "entree": "entrée",
    "entrees": "entrées",

    # --- associes ---
    "associees": "associées",
    "associee": "associée",
    "associes": "associés",
    "associe": "associé",

    # --- utilises ---
    "utilisees": "utilisées",
    "utilisee": "utilisée",
    "utilises": "utilisés",
    "utilise": "utilisé",

    # --- lancee ---
    "lancees": "lancées",
    "lancee": "lancée",
    "lances": "lancés",
    "lance": "lancé",

    # --- dedouanement ---
    "Dedouanement": "Dédouanement",
    "dedouanement": "dédouanement",

    # --- reservation ---
    "Reservation": "Réservation",
    "reservation": "réservation",
    "reservations": "réservations",

    # --- selection ---
    "Selection": "Sélection",
    "selection": "sélection",
    "selections": "sélections",

    # --- resolution ---
    "Resolution": "Résolution",
    "resolution": "résolution",

    # --- Preparation ---
    "Preparation": "Préparation",
    "preparation": "préparation",

    # --- cout ---
    "couts": "coûts",
    "cout": "coût",

    # --- Gerer/gerer ---
    "Gerer": "Gérer",
    "gerer": "gérer",
    "gere": "gère",

    # --- Creer/creer ---
    "Creer": "Créer",
    "creer": "créer",

    # --- Recevoir (already correct) ---

    # --- immediat ---
    "immediat": "immédiat",
    "immediats": "immédiats",
    "immediate": "immédiate",
    "immediates": "immédiates",

    # --- elargi ---
    "elargi": "élargi",
    "elargie": "élargie",
    "elargis": "élargis",
    "elargies": "élargies",

    # --- separe/separement ---
    "separement": "séparément",
    "separee": "séparée",
    "separees": "séparées",
    "separes": "séparés",
    "separe": "séparé",

    # --- identifie (was missed in pass2 for present tense "identifie") ---
    # Already handled as "identifié" in pass2

    # --- Specificite ---
    "specificite": "spécificité",
    "specificites": "spécificités",

    # --- Efficacite ---
    "efficacite": "efficacité",
    "Efficacite": "Efficacité",

    # --- Representant ---
    "representant": "représentant",
    "Representant": "Représentant",

    # --- Delegue ---
    "delegue": "délégué",
    "deleguee": "déléguée",
    "delegues": "délégués",

    # --- derogation ---
    "derogation": "dérogation",
    "derogations": "dérogations",

    # --- deterioration ---
    "deterioration": "détérioration",

    # --- prevues ---
    "prevues": "prévues",
    "prevue": "prévue",
    "prevus": "prévus",
    "prevu": "prévu",

    # --- verifie (present tense) ---
    # Already handled

    # --- Reexaminer ---
    "reexaminer": "réexaminer",

    # --- evaluer ---
    "evaluer": "évaluer",
    "Evaluer": "Évaluer",

    # --- Competences (dans les diagrammes) ---
    "Competences": "Compétences",
    "competences": "compétences",

    # --- exigee ---
    "exigee": "exigée",

    # --- capacite (dans les blocs code) ---
    "capacite": "capacité",

    # --- signale (remaining) ---
    "Signale": "Signalé",

    # --- Deploiement ---
    "deploiement": "déploiement",
    "Deploiement": "Déploiement",

    # --- Legiferer / reglementaire ---
    "reglementaire": "réglementaire",
    "reglementaires": "réglementaires",
    "reglementation": "réglementation",

    # --- Recommande ---
    # Already correct with accents from first pass

    # --- Synthese ---
    "synthese": "synthèse",
    "Synthese": "Synthèse",

    # --- Enquete ---
    "enquetes": "enquêtes",
    "enquete": "enquête",

    # --- satisfait ---
    # Already correct

    # --- Reseau ---
    "reseau": "réseau",
    "reseaux": "réseaux",
}


def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    sorted_replacements = sorted(REPLACEMENTS.items(), key=lambda x: len(x[0]), reverse=True)
    for old, new in sorted_replacements:
        if old == new:
            continue
        pattern = r'\b' + re.escape(old) + r'\b'
        content = re.sub(pattern, new, content)

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
            print(f"  ✓ {rel_path}")

    print(f"\nRésultat : {modified}/{len(md_files)} fichiers modifiés")


if __name__ == '__main__':
    main()
