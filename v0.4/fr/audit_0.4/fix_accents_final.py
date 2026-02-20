#!/usr/bin/env python3
"""
Passe finale de correction des accents français.
Traite TOUT le contenu (y compris les blocs de code/diagrammes ASCII).
"""

import re
import os

REPLACEMENTS = {
    # --- telephone ---
    "telephone": "téléphone",
    "Telephone": "Téléphone",
    "telephones": "téléphones",

    # --- probleme ---
    "problemes": "problèmes",
    "probleme": "problème",
    "Problemes": "Problèmes",
    "Probleme": "Problème",

    # --- Donnees ---
    "DONNEES": "DONNÉES",
    "Donnees": "Données",
    "donnees": "données",

    # --- periode ---
    "Periode": "Période",
    "periode": "période",
    "periodes": "périodes",

    # --- validee/validees ---
    "validees": "validées",
    "validee": "validée",

    # --- creee ---
    "creee": "créée",
    "creees": "créées",
    "cree": "créé",

    # --- finalisee ---
    "finalisees": "finalisées",
    "finalisee": "finalisée",

    # --- acceptees ---
    "acceptees": "acceptées",
    "acceptee": "acceptée",

    # --- adaptees ---
    "adaptees": "adaptées",
    "adaptee": "adaptée",

    # --- conservees ---
    "conservees": "conservées",
    "conservee": "conservée",

    # --- enregistrees ---
    "enregistrees": "enregistrées",
    "enregistree": "enregistrée",

    # --- planifiees ---
    "planifiees": "planifiées",
    "planifiee": "planifiée",

    # --- traitees ---
    "traitees": "traitées",
    "traitee": "traitée",

    # --- liees/lies/lie ---
    "liees": "liées",
    "liee": "liée",
    "lies": "liés",

    # --- limitees/limite (adjectif) ---
    "limitees": "limitées",
    "limitee": "limitée",

    # --- simplifiee/simplifie ---
    "simplifiees": "simplifiées",
    "simplifiee": "simplifiée",
    "simplifies": "simplifiés",
    "simplifie": "simplifié",

    # --- complete (adjectif féminin) ---
    "completes": "complètes",
    "complete": "complète",

    # --- cloturee/cloturer ---
    "Cloturees": "Clôturées",
    "Cloturee": "Clôturée",
    "Cloturer": "Clôturer",
    "cloturees": "clôturées",
    "cloturee": "clôturée",
    "cloturer": "clôturer",
    "cloture": "clôturé",

    # --- soldee/solde ---
    "Soldees": "Soldées",
    "Soldee": "Soldée",
    "soldees": "soldées",
    "soldee": "soldée",

    # --- remplacee/remplaces ---
    "remplacees": "remplacées",
    "remplacee": "remplacée",
    "remplaces": "remplacés",

    # --- recues/recus/recue ---
    "recues": "reçues",
    "recue": "reçue",
    "recus": "reçus",
    "recu": "reçu",

    # --- role ---
    "Role": "Rôle",
    "role": "rôle",
    "roles": "rôles",

    # --- eventuels/eventuelles ---
    "eventuelles": "éventuelles",
    "eventuelle": "éventuelle",
    "eventuels": "éventuels",
    "eventuel": "éventuel",

    # --- methode ---
    "Methodes": "Méthodes",
    "Methode": "Méthode",
    "methodes": "méthodes",
    "methode": "méthode",

    # --- electronique ---
    "electroniques": "électroniques",
    "electronique": "électronique",

    # --- Quantite ---
    "Quantites": "Quantités",
    "Quantite": "Quantité",
    "quantites": "quantités",
    "quantite": "quantité",

    # --- emises/emis ---
    "emises": "émises",
    "emise": "émise",
    "emis": "émis",

    # --- Modele ---
    "Modeles": "Modèles",
    "Modele": "Modèle",
    "modeles": "modèles",
    "modele": "modèle",

    # --- arret ---
    "arrets": "arrêts",
    "arret": "arrêt",

    # --- ecoulee ---
    "ecoulees": "écoulées",
    "ecoulee": "écoulée",

    # --- Planifie (adjectif) ---
    "Planifies": "Planifiés",
    "Planifiee": "Planifiée",
    "Planifie": "Planifié",
    "planifie": "planifié",

    # --- Enregistre (participe) ---
    "Enregistres": "Enregistrés",
    "Enregistre": "Enregistré",
    "enregistre": "enregistré",

    # --- declaree ---
    "declarees": "déclarées",
    "declaree": "déclarée",
    "declares": "déclarés",
    "declare": "déclaré",

    # --- gere/geres ---
    "geres": "gérés",
    "geree": "gérée",
    "gerees": "gérées",

    # --- resumee ---
    "resumees": "résumées",
    "resumee": "résumée",

    # --- renouvele ---
    "renouveles": "renouvelés",
    "renouvelee": "renouvelée",
    "renouvele": "renouvelé",

    # --- organise (participe passé) ---
    "organisee": "organisée",
    "organisees": "organisées",
    "organises": "organisés",

    # --- PREALABLE ---
    "PREALABLE": "PRÉALABLE",
    "prealable": "préalable",
    "prealables": "préalables",
    "Prealable": "Préalable",

    # --- qualifie ---
    "qualifiees": "qualifiées",
    "qualifiee": "qualifiée",
    "qualifies": "qualifiés",
    "qualifie": "qualifié",

    # --- PRIORITE ---
    "PRIORITE": "PRIORITÉ",
    "priorite": "priorité",

    # --- financiere ---
    "financieres": "financières",
    "financiere": "financière",

    # --- Comprehension ---
    "Comprehension": "Compréhension",
    "comprehension": "compréhension",

    # --- References ---
    "References": "Références",

    # --- Verification ---
    "Verification": "Vérification",
    "verification": "vérification",

    # --- Accusé ---
    "Accuse": "Accusé",
    "accuse": "accusé",

    # --- Faisabilite ---
    "Faisabilite": "Faisabilité",
    "faisabilite": "faisabilité",

    # --- legislation ---
    "legislation": "législation",
    "Legislation": "Législation",

    # --- Echanges ---
    "Echanges": "Échanges",
    "echanges": "échanges",

    # --- etape ---
    "etapes": "étapes",
    "etape": "étape",

    # --- responsabilites (dans les blocs code) ---
    "responsabilites": "responsabilités",
    "Responsabilites": "Responsabilités",

    # --- aupres ---
    "aupres": "auprès",

    # --- expedition ---
    "expeditions": "expéditions",
    "expedition": "expédition",

    # --- Creation (dans les blocs code) ---
    "Creation": "Création",
    "creation": "création",

    # --- reception (dans les blocs code) ---
    "receptions": "réceptions",

    # --- Aleas ---
    "Aleas": "Aléas",
    "aleas": "aléas",

    # --- signale ---
    "signale": "signalé",
    "signalee": "signalée",

    # --- CONTROLE (majuscules dans diagrammes) ---
    "CONTROLE": "CONTRÔLE",
    "QUALITE": "QUALITÉ",

    # --- numero ---
    "numero": "numéro",
    "Numero": "Numéro",
    "numeros": "numéros",

    # --- prets ---
    "prets": "prêts",

    # --- Resultats ---
    "Resultats": "Résultats",
    "resultats": "résultats",

    # --- conformes/conforme remains correct, no accent needed ---

    # --- sensibilise (participe passé) ---
    "sensibilises": "sensibilisés",
    "sensibilisee": "sensibilisée",
    "sensibilisees": "sensibilisées",

    # --- ANALYSE ---
    "ANALYSE PREALABLE": "ANALYSE PRÉALABLE",

    # --- Demande recue ---
    "Demande recue": "Demande reçue",
}

# Context-aware fixes (only in specific phrases)
CONTEXT_FIXES = [
    # "organise" as past participle (not present tense) in specific contexts
    ("dossier est organise", "dossier est organisé"),
    ("manière organisee", "manière organisée"),
    # "limite" as adjective
    ("impact limite", "impact limité"),
    ("Impact limite", "Impact limité"),
    ("nombre limite de", "nombre limité de"),
    ("limites de compétence", "limites de compétence"),  # correct as-is (noun plural)
    # "complete" where it means "complet" (adjective)
    ("SWOT complete", "SWOT complète"),
    ("matrice complete", "matrice complète"),
    ("correspondance complete", "correspondance complète"),
    ("traçabilité complete", "traçabilité complète"),
    ("gestion complete", "gestion complète"),
    ("sections completes", "sections complètes"),
    ("adresse complete", "adresse complète"),
    ("Structure documentaire complete", "Structure documentaire complète"),
    ("Analyse SWOT complete", "Analyse SWOT complète"),
    ("contrôle qualité complete", "contrôle qualité complète"),
    # "lie" as past participle
    ("risque lie", "risque lié"),
    ("Retard de livraison lie", "Retard de livraison lié"),
    # "Réalisé" → "Réalise" for present tense (any remaining over-corrections)
    ("Planifie / Réalisé", "Planifié / Réalisé"),
    # Solde specific
    ("Solde le", "Soldé le"),
    ("Solde par", "Soldé par"),
]


def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Step 1: Context-aware fixes first
    for old, new in CONTEXT_FIXES:
        content = content.replace(old, new)

    # Step 2: Apply word-boundary replacements on ALL content (including code blocks)
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

    print(f"Passe finale — correction des accents : {len(md_files)} fichiers")
    print("=" * 60)

    for filepath in md_files:
        rel_path = os.path.relpath(filepath, base_dir)
        if fix_file(filepath):
            modified += 1
            print(f"  ✓ {rel_path}")
        else:
            print(f"  - {rel_path}")

    print("=" * 60)
    print(f"Résultat : {modified}/{len(md_files)} fichiers modifiés")


if __name__ == '__main__':
    main()
