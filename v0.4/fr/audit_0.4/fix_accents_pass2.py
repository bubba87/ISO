#!/usr/bin/env python3
"""
Deuxième passe de correction des accents français.
Corrige les mots manqués par la première passe + répare les sur-corrections.
"""

import re
import os
import glob

# ===== 1. RÉPARATIONS DE SUR-CORRECTIONS =====
# Le premier script a changé "réalise" (présent) en "réalisé" dans certains contextes
OVER_CORRECTIONS = [
    ("ne réalisé aucune", "ne réalise aucune"),
    ("ne réalisé pas", "ne réalise pas"),
]

# ===== 2. MOTS MANQUANTS — dictionnaire complet =====
REPLACEMENTS = {
    # --- délai(s) ---
    "delais": "délais",
    "delai": "délai",

    # --- européen(s/ne/nes) ---
    "europeens": "européens",
    "europeennes": "européennes",
    "europeenne": "européenne",
    "europeen": "européen",

    # --- spécialisé(e/s/es) ---
    "specialisee": "spécialisée",
    "specialisees": "spécialisées",
    "specialises": "spécialisés",
    "specialise": "spécialisé",

    # --- développé(s/e/es) ---
    "developpes": "développés",
    "developpee": "développée",
    "developpees": "développées",
    "developpe": "développé",

    # --- stocké(s/e/es) ---
    "stockes": "stockés",
    "stockee": "stockée",
    "stockees": "stockées",
    "stocke": "stocké",

    # --- coordonné(s/e/es) ---
    "coordonnee": "coordonnée",
    "coordonnees": "coordonnées",
    "coordonnes": "coordonnés",
    "coordonne": "coordonné",

    # --- situé(s/e/es) ---
    "situes": "situés",
    "situee": "située",
    "situees": "situées",
    "situe": "situé",

    # --- localisé(s/e/es) ---
    "localises": "localisés",
    "localisee": "localisée",
    "localisees": "localisées",
    "localise": "localisé",

    # --- aérien(ne/s/nes) ---
    "aeriens": "aériens",
    "aeriennes": "aériennes",
    "aerienne": "aérienne",
    "aerien": "aérien",

    # --- chaîne(s) ---
    "chaines": "chaînes",
    "chaine": "chaîne",

    # --- élevé(e/s/es) ---
    "elevees": "élevées",
    "elevee": "élevée",
    "eleves": "élevés",
    "eleve": "élevé",

    # --- conçoit ---
    "concoit": "conçoit",

    # --- employé(e/s/es) ---
    "employees": "employées",
    "employee": "employée",
    "employes": "employés",
    "employe": "employé",

    # --- effectué(e/s/es) ---
    "effectuees": "effectuées",
    "effectuee": "effectuée",
    "effectues": "effectués",
    "effectue": "effectué",

    # --- livré(e/s/es) ---
    "livrees": "livrées",
    "livree": "livrée",
    "livres": "livrés",

    # --- analysé(e/s/es) ---
    "analysees": "analysées",
    "analysee": "analysée",
    "analyses": "analysés",

    # --- nécessaire(s) ---
    "necessaires": "nécessaires",
    "necessaire": "nécessaire",

    # --- stabilité ---
    "stabilite": "stabilité",

    # --- justifié(e/s/es) ---
    "justifiees": "justifiées",
    "justifiee": "justifiée",
    "justifies": "justifiés",
    "justifie": "justifié",

    # --- proposé(e/s/es) ---
    "proposees": "proposées",
    "proposee": "proposée",
    "proposes": "proposés",

    # --- décidé(e/s/es) ---
    "decidees": "décidées",
    "decidee": "décidée",
    "decides": "décidés",
    "decide": "décidé",

    # --- détecté(e/s/es) ---
    "detectees": "détectées",
    "detectee": "détectée",
    "detectes": "détectés",
    "detecte": "détecté",

    # --- endommagé(e/s/es) ---
    "endommages": "endommagés",
    "endommagee": "endommagée",
    "endommagees": "endommagées",

    # --- détail(s) ---
    "details": "détails",
    "detail": "détail",

    # --- réactiv(e/ité) ---
    "reactive": "réactive",
    "reactivite": "réactivité",

    # --- réceptionn(e/er/é) ---
    "receptionne": "réceptionne",
    "receptionner": "réceptionner",
    "receptionnes": "réceptionnes",

    # --- échantillon(s) ---
    "echantillons": "échantillons",
    "echantillon": "échantillon",

    # --- parallèle(s) ---
    "paralleles": "parallèles",
    "parallele": "parallèle",

    # --- indisponibilité ---
    "indisponibilite": "indisponibilité",

    # --- étant ---
    "etant": "étant",

    # --- contrôle(s/r/é) (certains manqués) ---
    "controle": "contrôle",
    "controles": "contrôles",
    "controler": "contrôler",
    "controlee": "contrôlée",
    "controlees": "contrôlées",
    "controles": "contrôlés",

    # --- pièce(s) (vérifier les restants) ---
    "pieces": "pièces",
    "piece": "pièce",

    # --- précédent(e/s/es) ---
    "precedente": "précédente",
    "precedentes": "précédentes",
    "precedents": "précédents",
    "precedent": "précédent",

    # --- présent(s/e/es) ---
    "presents": "présents",
    "presente": "présente",
    "presentes": "présentes",
    "present": "présent",

    # --- douanière(s) ---
    "douanieres": "douanières",
    "douaniere": "douanière",

    # --- sensibilité ---
    "sensibilite": "sensibilité",

    # --- chiffré(s/e/es) ---
    "chiffres": "chiffrés",

    # --- expédié(e/s/es) ---
    "expediees": "expédiées",
    "expediee": "expédiée",
    "expedies": "expédiés",
    "expedite": "expédié",  # typo "expedites" → "expédiées"

    # --- antérieur(e/s) ---
    "anterieure": "antérieure",
    "anterieures": "antérieures",
    "anterieur": "antérieur",
    "anterieurs": "antérieurs",

    # --- postérieur(e/s) ---
    "posterieure": "postérieure",
    "posterieures": "postérieures",
    "posterieur": "postérieur",

    # --- extérieur(e/s) ---
    "exterieure": "extérieure",
    "exterieures": "extérieures",
    "exterieurs": "extérieurs",
    "exterieur": "extérieur",

    # --- intérieur(e/s) ---
    "interieure": "intérieure",
    "interieures": "intérieures",
    "interieurs": "intérieurs",
    "interieur": "intérieur",

    # --- inférieur(e/s) ---
    "inferieure": "inférieure",
    "inferieures": "inférieures",
    "inferieurs": "inférieurs",
    "inferieur": "inférieur",

    # --- supérieur(e/s) ---
    "superieure": "supérieure",
    "superieures": "supérieures",
    "superieurs": "supérieurs",
    "superieur": "supérieur",

    # --- manière ---
    "maniere": "manière",
    "manieres": "manières",

    # --- matière ---
    "matiere": "matière",
    "matieres": "matières",

    # --- première(s) / premier ---
    "premieres": "premières",
    "premiere": "première",

    # --- dernière(s) / dernier ---
    "dernieres": "dernières",
    "derniere": "dernière",

    # --- critère(s) ---
    "criteres": "critères",
    "critere": "critère",

    # --- légère(s) ---
    "legeres": "légères",
    "legere": "légère",

    # --- régulière(s) / régulier ---
    "regulieres": "régulières",
    "reguliere": "régulière",
    "regulierement": "régulièrement",
    "reguliers": "réguliers",
    "regulier": "régulier",

    # --- particulière(s) / particulier ---
    "particulieres": "particulières",
    "particuliere": "particulière",
    "particuliers": "particuliers",
    "particulier": "particulier",

    # --- financière(s) / financier ---
    "financieres": "financières",
    "financiere": "financière",

    # --- formalisé(e/s/es) ---
    "formalisees": "formalisées",
    "formalisee": "formalisée",
    "formalises": "formalisés",
    "formalise": "formalisé",

    # --- réalisé(e/s/es) --- seulement les formes clairement passé composé
    "realisees": "réalisées",
    "realisee": "réalisée",
    "realises": "réalisés",

    # --- programmé(e/s) ---
    "programmees": "programmées",
    "programmee": "programmée",
    "programmes": "programmés",

    # --- reporté(e/s) ---
    "reportees": "reportées",
    "reportee": "reportée",
    "reportes": "reportés",

    # --- désigné(e/s) ---
    "designees": "désignées",
    "designee": "désignée",
    "designes": "désignés",
    "designe": "désigné",

    # --- intégré(e/s/es) ---
    "integrees": "intégrées",
    "integree": "intégrée",
    "integres": "intégrés",
    "integre": "intégré",

    # --- évalué(e/s/es) ---
    "evaluees": "évaluées",
    "evaluee": "évaluée",
    "evalues": "évalués",
    "evalue": "évalué",

    # --- mesuré(e/s) ---
    "mesurees": "mesurées",
    "mesuree": "mesurée",
    "mesures": "mesurés",

    # --- rédigé(e/s) ---
    "redigees": "rédigées",
    "redigee": "rédigée",
    "rediges": "rédigés",
    "redige": "rédigé",

    # --- envoyé(e/s) ---
    "envoyees": "envoyées",
    "envoyee": "envoyée",
    "envoyes": "envoyés",

    # --- vérifié(e/s) ---
    "verifiees": "vérifiées",
    "verifiee": "vérifiée",
    "verifies": "vérifiés",
    "verifie": "vérifié",

    # --- documenté(e/s) ---
    "documentees": "documentées",
    "documentee": "documentée",
    "documentes": "documentés",
    "documente": "documenté",

    # --- spécifié(e/s) ---
    "specifiees": "spécifiées",
    "specifiee": "spécifiée",
    "specifies": "spécifiés",
    "specifie": "spécifié",

    # --- sensibilisation ---
    "sensibilisation": "sensibilisation",  # déjà correct, pas d'accent manquant

    # --- réclamé(e/s) ---
    "reclamees": "réclamées",
    "reclamee": "réclamée",
    "reclames": "réclamés",
    "reclame": "réclamé",

    # --- classé(e/s) ---
    "classees": "classées",
    "classee": "classée",

    # --- archivé(e/s) ---
    "archivees": "archivées",
    "archivee": "archivée",
    "archives": "archivés",

    # --- externalisé(e/s) ---
    "externalisees": "externalisées",
    "externalisee": "externalisée",
    "externalises": "externalisés",
    "externalise": "externalisé",

    # --- annoncé(e/s) ---
    "annoncees": "annoncées",
    "annoncee": "annoncée",
    "annonces": "annoncés",

    # --- défini(e/s/es) ---
    "definies": "définies",
    "definie": "définie",
    "definis": "définis",
    "defini": "défini",

    # --- opéré(e/s) ---
    "operees": "opérées",
    "operee": "opérée",
    "operes": "opérés",
    "opere": "opéré",

    # --- pondéré(e/s) ---
    "ponderees": "pondérées",
    "ponderee": "pondérée",
    "ponderes": "pondérés",
    "pondere": "pondéré",

    # --- délibéré(e/s) ---
    "deliberees": "délibérées",
    "deliberee": "délibérée",
    "deliberes": "délibérés",
    "delibere": "délibéré",

    # --- événement(s) ---
    "evenements": "événements",
    "evenement": "événement",

    # --- exigé(e/s) ---
    "exigees": "exigées",
    "exigee": "exigée",
    "exiges": "exigés",
    "exige": "exigé",

    # --- généré(e/s) ---
    "generees": "générées",
    "generee": "générée",
    "generes": "générés",
    "genere": "généré",

    # --- impliqué(e/s) ---
    "impliquees": "impliquées",
    "impliquee": "impliquée",
    "impliques": "impliqués",
    "implique": "impliqué",

    # --- identifié(e/s) ---
    "identifiees": "identifiées",
    "identifiee": "identifiée",
    "identifies": "identifiés",
    "identifie": "identifié",

    # --- imprimé(e/s) ---
    "imprimees": "imprimées",
    "imprimee": "imprimée",
    "imprimes": "imprimés",
    "imprime": "imprimé",

    # --- concerné(e/s) ---
    "concernees": "concernées",
    "concernee": "concernée",
    "concernes": "concernés",
    "concerne": "concerné",

    # --- entièrement ---
    "entierement": "entièrement",

    # --- sécurisé(e/s) ---
    "securisees": "sécurisées",
    "securisee": "sécurisée",
    "securises": "sécurisés",
    "securise": "sécurisé",

    # --- fourni(e/s) (already correct, no accent needed) ---

    # --- expédier ---
    "expedier": "expédier",

    # --- réaliser --- présent (attention: ne pas changer en "réalisé")
    "realise": "réalise",  # présent indicatif 3e pers.
    "realiser": "réaliser",

    # --- expedites (typo in original) ---
    "expedites": "expédiées",

    # --- Additional missing words ---
    "sensibilise": "sensibilisé",
    "sensibilises": "sensibilisés",
    "sensibilisee": "sensibilisée",
    "sensibilisees": "sensibilisées",

    # --- résumé ---
    "resume": "résumé",

    # --- réservé(e/s) ---
    "reservees": "réservées",
    "reservee": "réservée",
    "reserves": "réservés",
    "reserve": "réservé",

    # --- protégé(e/s) ---
    "protegees": "protégées",
    "protegee": "protégée",
    "proteges": "protégés",
    "protege": "protégé",

    # --- assuré(e) ---
    "assuree": "assurée",
    "assurees": "assurées",

    # --- sélectionné(e/s) ---
    "selectionnees": "sélectionnées",
    "selectionnee": "sélectionnée",
    "selectionnes": "sélectionnés",
    "selectionne": "sélectionné",

    # --- déterminé(e/s) ---
    "determinee": "déterminée",
    "determinees": "déterminées",
    "determines": "déterminés",
    "determine": "déterminé",

    # --- considéré(e/s) ---
    "considerees": "considérées",
    "consideree": "considérée",
    "consideres": "considérés",
    "considere": "considéré",
}

def fix_file(filepath):
    """Apply second-pass accent corrections to a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Step 1: Fix over-corrections first
    for wrong, correct in OVER_CORRECTIONS:
        content = content.replace(wrong, correct)

    # Step 2: Split content to skip code blocks
    parts = re.split(r'(```.*?```)', content, flags=re.DOTALL)

    for i in range(len(parts)):
        # Skip code blocks (odd indices)
        if i % 2 == 1:
            continue

        text = parts[i]

        # Sort replacements by length (longest first) to avoid partial matches
        sorted_replacements = sorted(REPLACEMENTS.items(), key=lambda x: len(x[0]), reverse=True)

        for old, new in sorted_replacements:
            if old == new:
                continue  # Skip no-ops

            # Word boundary matching (case-sensitive, lowercase)
            pattern = r'\b' + re.escape(old) + r'\b'
            text = re.sub(pattern, new, text)

            # Also handle Capitalized version
            old_cap = old[0].upper() + old[1:]
            new_cap = new[0].upper() + new[1:]
            pattern_cap = r'\b' + re.escape(old_cap) + r'\b'
            text = re.sub(pattern_cap, new_cap, text)

        parts[i] = text

    content = ''.join(parts)

    # Step 3: Fix "expedites directement" → "expédiées directement" (specific typo)
    content = content.replace("expedites directement", "expédiées directement")

    # Step 4: Fix specific context issues
    # "A modifier" → "À modifier" in specific contexts
    content = re.sub(r'\bA modifier\b', 'À modifier', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    md_files = []
    for root, dirs, files in os.walk(base_dir):
        # Skip .git and EN directories
        dirs[:] = [d for d in dirs if d not in ['.git', 'en']]
        for f in files:
            if f.endswith('.md'):
                md_files.append(os.path.join(root, f))

    md_files.sort()

    modified = 0
    total = len(md_files)

    print(f"Deuxième passe de correction des accents — {total} fichiers")
    print("=" * 60)

    for filepath in md_files:
        rel_path = os.path.relpath(filepath, base_dir)
        if fix_file(filepath):
            modified += 1
            print(f"  ✓ Corrigé : {rel_path}")
        else:
            print(f"  - Inchangé : {rel_path}")

    print("=" * 60)
    print(f"Résultat : {modified}/{total} fichiers modifiés")


if __name__ == '__main__':
    main()
