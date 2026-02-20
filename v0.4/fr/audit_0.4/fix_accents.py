#!/usr/bin/env python3
"""
Correction des accents français dans les fichiers Markdown du SMQ.
Remplace systématiquement les mots sans accents par leurs formes correctes.
"""

import re
import os
import glob

# Dictionnaire de remplacement : mot_sans_accent → mot_avec_accent
# Classé par longueur décroissante pour éviter les remplacements partiels
REPLACEMENTS = {
    # --- Mots très longs (20+ caractères) ---
    "professionnelles": "professionnelles",  # pas d'accent manquant
    "intracommunautaire": "intracommunautaire",

    # --- Noms composés / expressions ---
    "systeme de management de la qualite": "système de management de la qualité",
    "Systeme de Management de la Qualite": "Système de Management de la Qualité",
    "amelioration continue": "amélioration continue",
    "Amelioration continue": "Amélioration continue",
    "propriete intellectuelle": "propriété intellectuelle",
    "societe a responsabilite limitee": "société à responsabilité limitée",
    "Societe a responsabilite limitee": "Société à responsabilité limitée",

    # --- Mots en -ité / -ite ---
    "qualite": "qualité",
    "securite": "sécurité",
    "conformite": "conformité",
    "responsabilite": "responsabilité",
    "responsabilites": "responsabilités",
    "tracabilite": "traçabilité",
    "reactivite": "réactivité",
    "efficacite": "efficacité",
    "disponibilite": "disponibilité",
    "fiabilite": "fiabilité",
    "rentabilite": "rentabilité",
    "perennite": "pérennité",
    "confidentialite": "confidentialité",
    "continuite": "continuité",
    "capacite": "capacité",
    "capacites": "capacités",
    "activite": "activité",
    "activites": "activités",
    "opportunite": "opportunité",
    "opportunites": "opportunités",
    "priorite": "priorité",
    "priorites": "priorités",
    "propriete": "propriété",
    "proprietes": "propriétés",
    "necessite": "nécessité",
    "faisabilite": "faisabilité",
    "integrite": "intégrité",
    "quantite": "quantité",
    "quantites": "quantités",
    "impartialite": "impartialité",
    "independance": "indépendance",

    # --- Mots en -tion ---
    "creation": "création",
    "evaluation": "évaluation",
    "evaluations": "évaluations",
    "reclamation": "réclamation",
    "reclamations": "réclamations",
    "expedition": "expédition",
    "expeditions": "expéditions",
    "verification": "vérification",
    "verifications": "vérifications",
    "amelioration": "amélioration",
    "ameliorations": "améliorations",
    "remuneration": "rémunération",
    "repetition": "répétition",
    "prevention": "prévention",
    "reapparition": "réapparition",
    "planification": "planification",  # pas d'accent manquant
    "legislation": "législation",
    "evolution": "évolution",
    "evolutions": "évolutions",
    "operation": "opération",
    "operations": "opérations",
    "specification": "spécification",
    "specifications": "spécifications",
    "modification": "modification",  # pas d'accent manquant
    "declaration": "déclaration",
    "negociation": "négociation",
    "coordination": "coordination",  # pas d'accent manquant
    "communication": "communication",  # pas d'accent manquant
    "information": "information",  # pas d'accent manquant
    "presentation": "présentation",
    "determination": "détermination",
    "reglementation": "réglementation",
    "facturation": "facturation",  # pas d'accent manquant

    # --- Mots en -ement / -ment ---
    "systeme": "système",
    "systemes": "systèmes",
    "developpement": "développement",
    "element": "élément",
    "elements": "éléments",
    "reglement": "règlement",
    "reglements": "règlements",
    "equipement": "équipement",
    "equipements": "équipements",
    "evenement": "événement",
    "evenements": "événements",
    "completement": "complètement",
    "entierement": "entièrement",
    "regulierement": "régulièrement",
    "referentiel": "référentiel",
    "etablissement": "établissement",

    # --- Mots en -ence / -ance ---
    "reference": "référence",
    "references": "références",
    "experience": "expérience",
    "experiences": "expériences",
    "competence": "compétence",
    "competences": "compétences",
    "coherence": "cohérence",
    "independance": "indépendance",
    "defaillance": "défaillance",
    "tolerance": "tolérance",
    "tolerances": "tolérances",

    # --- Mots en -ure / -ure ---
    "procedure": "procédure",
    "procedures": "procédures",
    "cloture": "clôture",
    "cloturer": "clôturer",

    # --- Mots en -ere / -ère ---
    "critere": "critère",
    "criteres": "critères",
    "matiere": "matière",
    "matieres": "matières",
    "maniere": "manière",
    "premiere": "première",
    "premieres": "premières",
    "derniere": "dernière",
    "dernieres": "dernières",
    "douaniere": "douanière",
    "douanieres": "douanières",
    "financiere": "financière",
    "financieres": "financières",
    "reguliere": "régulière",
    "regulieres": "régulières",
    "entiere": "entière",
    "entieres": "entières",

    # --- Mots en -ee ---
    "annee": "année",
    "annees": "années",
    "donnee": "donnée",
    "donnees": "données",
    "duree": "durée",
    "entree": "entrée",
    "detaillee": "détaillée",
    "detaillees": "détaillées",
    "interessee": "intéressée",
    "interessees": "intéressées",
    "concernee": "concernée",
    "concernees": "concernées",
    "realisee": "réalisée",
    "realisees": "réalisées",
    "planifiee": "planifiée",
    "externalisee": "externalisée",
    "formalisee": "formalisée",
    "identifiee": "identifiée",

    # --- Mots en -é (participe passé masculin) ---
    "cree": "créé",
    "redige": "rédigé",
    "approuve": "approuvé",
    "recommande": "recommandé",
    "recommandee": "recommandée",
    "externalise": "externalisé",
    "externalises": "externalisés",
    "realise": "réalisé",
    "realises": "réalisés",
    "integre": "intégré",
    "integree": "intégrée",
    "integres": "intégrés",
    "defini": "défini",
    "definie": "définié",
    "definies": "définies",
    "definis": "définis",
    "determine": "déterminé",
    "determinee": "déterminée",
    "determines": "déterminés",
    "identifie": "identifié",
    "identifies": "identifiés",
    "formalise": "formalisé",
    "formalises": "formalisés",
    "elabore": "élaboré",
    "verifie": "vérifié",
    "planifie": "planifié",
    "reserve": "réservé",
    "presente": "présenté",
    "presentes": "présentés",
    "enregistre": "enregistré",
    "enregistree": "enregistrée",
    "enregistres": "enregistrés",
    "deplace": "déplacé",
    "deplaces": "déplacés",
    "controle": "contrôle",
    "controles": "contrôles",
    "controlee": "contrôlée",
    "evalue": "évalué",
    "evaluee": "évaluée",
    "evalues": "évalués",
    "assure": "assuré",  # Careful - can also be verb "assure" without accent
    "ameliore": "amélioré",
    "amelioree": "améliorée",
    "confirme": "confirmé",
    "confirmee": "confirmée",
    "confirmes": "confirmés",

    # --- Mots en -er (infinitifs) ---
    "creer": "créer",
    "verifier": "vérifier",
    "ameliorer": "améliorer",
    "etablir": "établir",
    "reevaluer": "réévaluer",
    "reevalue": "réévalue",
    "repeter": "répéter",
    "evaluer": "évaluer",
    "gerer": "gérer",
    "generer": "générer",

    # --- Mots en -eur ---
    "numero": "numéro",
    "numeros": "numéros",
    "numerotation": "numérotation",

    # --- Mots en -egie / -ique ---
    "strategie": "stratégie",
    "strategique": "stratégique",
    "strategiques": "stratégiques",
    "specifique": "spécifique",
    "specifiques": "spécifiques",
    "reglementaire": "réglementaire",
    "reglementaires": "réglementaires",
    "operationnel": "opérationnel",
    "operationnelle": "opérationnelle",
    "operationnels": "opérationnels",
    "operationnelles": "opérationnelles",
    "periodique": "périodique",
    "periodiques": "périodiques",
    "intermediaire": "intermédiaire",
    "complementaire": "complémentaire",
    "complementaires": "complémentaires",
    "prealable": "préalable",
    "systematique": "systématique",
    "systematiquement": "systématiquement",
    "geographique": "géographique",
    "geopolitique": "géopolitique",
    "economique": "économique",

    # --- Mots en -al / -el ---
    "general": "général",
    "generale": "générale",
    "generales": "générales",
    "independant": "indépendant",
    "independante": "indépendante",
    "immediat": "immédiat",
    "immediat": "immédiat",

    # --- Mots communs ---
    "societe": "société",
    "societes": "sociétés",
    "gerante": "gérante",
    "legende": "légende",
    "role": "rôle",
    "roles": "rôles",
    "piece": "pièce",
    "pieces": "pièces",
    "resultat": "résultat",
    "resultats": "résultats",
    "resume": "résumé",
    "synthese": "synthèse",
    "methode": "méthode",
    "methodes": "méthodes",
    "echeance": "échéance",
    "echeances": "échéances",
    "ecart": "écart",
    "ecarts": "écarts",
    "echange": "échange",
    "echanges": "échanges",
    "etape": "étape",
    "etapes": "étapes",
    "etat": "état",
    "etiquetage": "étiquetage",
    "perime": "périmé",
    "perimee": "périmée",
    "perimetre": "périmètre",
    "modele": "modèle",
    "modeles": "modèles",
    "requete": "requête",
    "enquete": "enquête",
    "detaille": "détaillé",
    "detailles": "détaillés",
    "detailler": "détailler",
    "remplace": "remplacé",
    "remplacement": "remplacement",  # pas d'accent manquant
    "prevue": "prévue",
    "prevues": "prévues",
    "prevu": "prévu",
    "prevus": "prévus",
    "repond": "répond",
    "repondre": "répondre",
    "reponse": "réponse",
    "reponses": "réponses",
    "objectif": "objectif",  # pas d'accent manquant
    "acces": "accès",
    "succes": "succès",
    "apres": "après",
    "aupres": "auprès",
    "progres": "progrès",
    "exigence": "exigence",  # pas d'accent manquant
    "exigences": "exigences",  # pas d'accent manquant
    "pertinente": "pertinente",  # pas d'accent manquant
    "etre": "être",
    "maitrise": "maîtrise",
    "maitriser": "maîtriser",
    "entretien": "entretien",  # pas d'accent manquant
    "reperage": "repérage",
    "adequation": "adéquation",
    "delegation": "délégation",
    "remuneration": "rémunération",

    # --- Verbes conjugués courants ---
    "definit": "définit",
    "definir": "définir",
    "etablit": "établit",
    "determine": "détermine",  # 3e pers
    "presente": "présente",  # 3e pers
    "assure": "assure",  # attention : pas d'accent (3e pers du présent)
    "veille": "veille",  # pas d'accent manquant
    "prevoit": "prévoit",
    "repond": "répond",
    "refere": "réfère",
    "genere": "généré",

    # --- Mots courts avec accent ---
    "deja": "déjà",
    "a ete": "a été",
    "ont ete": "ont été",
    "ete": "été",  # careful - only "été" as past participle

    # --- Mots avec ô ---
    "controle": "contrôle",
    "controles": "contrôles",
    "role": "rôle",
    "roles": "rôles",
    "cloture": "clôture",

    # --- Mots avec ç ---
    "tracabilite": "traçabilité",
    "francais": "français",
    "francaise": "française",
    "recoit": "reçoit",
    "recu": "reçu",
    "recue": "reçue",
    "recus": "reçus",
    "facons": "façons",
    "facon": "façon",
    "lecons": "leçons",
    "lecon": "leçon",

    # --- Mots avec î ---
    "maitrise": "maîtrise",
    "maitriser": "maîtriser",
    "maitrisee": "maîtrisée",
    "connaitre": "connaître",
    "connaissance": "connaissance",  # pas d'accent manquant
    "apparaitre": "apparaître",

    # --- Mots avec è ---
    "synthese": "synthèse",
    "modele": "modèle",
    "critere": "critère",
    "reglement": "règlement",
    "regle": "règle",
    "regles": "règles",
    "acces": "accès",
    "succes": "succès",
    "apres": "après",
    "aupres": "auprès",
    "progres": "progrès",

    # --- Début de phrase (majuscule) ---
    "Systeme": "Système",
    "Societe": "Société",
    "Evaluation": "Évaluation",
    "Evaluations": "Évaluations",
    "Elabore": "Élaboré",
    "Element": "Élément",
    "Elements": "Éléments",
    "Etablir": "Établir",
    "Etabli": "Établi",
    "Etablissement": "Établissement",
    "Etape": "Étape",
    "Etapes": "Étapes",
    "Etat": "État",
    "Ecart": "Écart",
    "Ecarts": "Écarts",
    "Echange": "Échange",
    "Echanges": "Échanges",
    "Echeance": "Échéance",
    "Etre": "Être",
    "Evenement": "Événement",
    "Evolution": "Évolution",
    "Equipement": "Équipement",
    "Expedition": "Expédition",
    "Experience": "Expérience",
    "Reference": "Référence",
    "References": "Références",
    "Referentiel": "Référentiel",
    "Resultat": "Résultat",
    "Resultats": "Résultats",
    "Resume": "Résumé",
    "Reponse": "Réponse",
    "Reponses": "Réponses",
    "Reactivite": "Réactivité",
    "Reclamation": "Réclamation",
    "Reclamations": "Réclamations",
    "Reglementaire": "Réglementaire",
    "Reglementaires": "Réglementaires",
    "Reglementation": "Réglementation",
    "Reglement": "Règlement",
    "Regle": "Règle",
    "Realise": "Réalisé",
    "Redige": "Rédigé",
    "Recommande": "Recommandé",
    "Procedure": "Procédure",
    "Procedures": "Procédures",
    "Presentation": "Présentation",
    "Prevention": "Prévention",
    "Prealable": "Préalable",
    "Prevue": "Prévue",
    "Prevu": "Prévu",
    "Perimetre": "Périmètre",
    "Perime": "Périmé",
    "Periodique": "Périodique",
    "Numero": "Numéro",
    "Necessite": "Nécessité",
    "Necessaire": "Nécessaire",
    "Negociation": "Négociation",
    "Methode": "Méthode",
    "Maitrise": "Maîtrise",
    "Legislation": "Législation",
    "Legende": "Légende",
    "Independant": "Indépendant",
    "Intermediaire": "Intermédiaire",
    "Integre": "Intégré",
    "Integration": "Intégration",
    "Identifie": "Identifié",
    "Gerante": "Gérante",
    "General": "Général",
    "Generale": "Générale",
    "Generalites": "Généralités",
    "Genere": "Généré",
    "Developpement": "Développement",
    "Detaille": "Détaillé",
    "Detaillee": "Détaillée",
    "Defini": "Défini",
    "Definit": "Définit",
    "Definir": "Définir",
    "Determine": "Déterminé",
    "Determination": "Détermination",
    "Declaration": "Déclaration",
    "Defaillance": "Défaillance",
    "Creation": "Création",
    "Cree": "Créé",
    "Creer": "Créer",
    "Controle": "Contrôle",
    "Controles": "Contrôles",
    "Cloture": "Clôture",
    "Competence": "Compétence",
    "Competences": "Compétences",
    "Coherence": "Cohérence",
    "Complementaire": "Complémentaire",
    "Amelioration": "Amélioration",
    "Ameliore": "Amélioré",
    "Adequation": "Adéquation",
    "Activite": "Activité",
    "Activites": "Activités",

    # Termes spécifiques ISO / documents
    "Strategie": "Stratégie",
    "Strategique": "Stratégique",
    "Strategiques": "Stratégiques",
    "Specifique": "Spécifique",
    "Specifiques": "Spécifiques",
    "Operationnel": "Opérationnel",
    "Operationnelle": "Opérationnelle",
    "Operationnels": "Opérationnels",
    "Systematique": "Systématique",
    "Securite": "Sécurité",
    "Conformite": "Conformité",
    "Tracabilite": "Traçabilité",
    "Efficacite": "Efficacité",
    "Disponibilite": "Disponibilité",
    "Fiabilite": "Fiabilité",
    "Rentabilite": "Rentabilité",
    "Perennite": "Pérennité",
    "Confidentialite": "Confidentialité",
    "Continuite": "Continuité",
    "Capacite": "Capacité",
    "Faisabilite": "Faisabilité",
    "Propriete": "Propriété",
    "Opportunite": "Opportunité",
    "Opportunites": "Opportunités",
    "Priorite": "Priorité",
    "Priorites": "Priorités",
    "Responsabilite": "Responsabilité",
    "Responsabilites": "Responsabilités",
    "Qualite": "Qualité",
    "Verification": "Vérification",
    "Verifier": "Vérifier",

    # Special: "A REMPLIR", "A VERIFIER" => "À REMPLIR", "À VÉRIFIER"
    "A REMPLIR": "À REMPLIR",
    "A VERIFIER": "À VÉRIFIER",
    "A CONFIRMER": "À CONFIRMER",

    # --- Mots avec "à" (préposition) ---
    # These are handled separately in context-aware function
}

# Words where we must NOT replace (would break references, English text, etc.)
SKIP_PATTERNS = [
    r'[A-Z]{2,}-[A-Z]{2,}-\d{3}',  # Document references like CTX-QUA-001
    r'FIC-PRO-\d{3}',
    r'M\d-[A-Z]{3}-\d{3}',
    r'CHK-[A-Z]{3}-\d{3}',
    r'LST-[A-Z]{3}-\d{3}',
    r'EXT-[A-Z]{3}-\d{3}',
    r'NC_\d{4}_\d{4}',  # NC references
    r'SHIP_\d{5}',
    r'CFM\d{8}',
    r'CH-\d{3}\.\d\.\d{3}\.\d{3}-\d',  # IDE number
    r'http[s]?://\S+',  # URLs
]


def should_skip_line(line):
    """Check if line should be skipped (code block markers, etc.)."""
    stripped = line.strip()
    if stripped.startswith('```'):
        return True
    return False


def apply_replacements(text):
    """Apply accent corrections to text."""
    lines = text.split('\n')
    in_code_block = False
    result = []

    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue

        if in_code_block:
            result.append(line)
            continue

        # Apply replacements
        modified = line

        # Sort replacements by length (longest first) to avoid partial matches
        sorted_replacements = sorted(REPLACEMENTS.items(), key=lambda x: len(x[0]), reverse=True)

        for old, new in sorted_replacements:
            if old == new:
                continue  # Skip identity replacements

            # Use word boundary matching
            # Be careful with special regex characters
            old_escaped = re.escape(old)
            pattern = r'(?<![a-zA-ZÀ-ÿ])' + old_escaped + r'(?![a-zA-ZÀ-ÿ])'
            modified = re.sub(pattern, new, modified)

        result.append(modified)

    return '\n'.join(result)


def fix_preposition_a(text):
    """Fix 'a' → 'à' when used as preposition in common patterns."""
    patterns = [
        # "a" before articles/determinants
        (r'\b([Cc]onforme) a la\b', r'\1 à la'),
        (r'\b([Cc]onforme) a l\'', r'\1 à l\''),
        (r'\b([Cc]onforme) au\b', r'\1 au'),
        (r'\b([Cc]onforme) aux\b', r'\1 à'),  # Actually "conforme aux"
        (r'\bdestine a\b', r'destiné à'),
        (r'\b[Dd]estine a\b', r'destiné à'),
        (r'\bface a\b', r'face à'),
        (r'\bFace a\b', r'Face à'),
        (r'\bgrace a\b', r'grâce à'),
        (r'\bGrace a\b', r'Grâce à'),
        (r'\bgrâce a\b', r'grâce à'),
        (r'\bquant a\b', r'quant à'),
        (r'\bvise a\b', r'visé à'),  # actually "visée à"
        (r'\bvisee a\b', r'visée à'),
        (r'\bapplicable a\b', r'applicable à'),
        (r'\bapplicables a\b', r'applicables à'),
        (r'\brelatif a\b', r'relatif à'),
        (r'\brelatifs a\b', r'relatifs à'),
        (r'\brelative a\b', r'relative à'),
        (r'\brelatives a\b', r'relatives à'),
        (r'\bliee a\b', r'liée à'),
        (r'\bliees a\b', r'liées à'),
        (r'\blies a\b', r'liés à'),
        (r'\blie a\b', r'lié à'),
        (r'\bliée a\b', r'liée à'),
        (r'\bliées a\b', r'liées à'),
        (r'\bliés a\b', r'liés à'),
        (r'\blié a\b', r'lié à'),
        (r'\bsusceptible a\b', r'susceptible à'),
        (r'\bsusceptibles a\b', r'susceptibles à'),
        (r'\b([Mm])ise a disposition\b', r'\1ise à disposition'),
        (r'\b([Mm])ise a jour\b', r'\1ise à jour'),
        (r'\b([Mm])is a jour\b', r'\1is à jour'),
        (r'\b([Mm])ise a niveau\b', r'\1ise à niveau'),
        (r'\b([Mm])ise en oeuvre\b', r'\1ise en œuvre'),
        (r'\b([Mm])ise en œuvre\b', r'\1ise en œuvre'),
        (r'\bA REMPLIR\b', r'À REMPLIR'),
        (r'\bA VERIFIER\b', r'À VÉRIFIER'),
        (r'\bA CONFIRMER\b', r'À CONFIRMER'),
        (r'\bA ce titre\b', r'À ce titre'),
        (r'\bA ce stade\b', r'À ce stade'),
        (r'\bA chaque\b', r'À chaque'),
        (r'\bA distance\b', r'À distance'),
        (r'\bA partir\b', r'À partir'),
        (r'\bA mesurer\b', r'À mesurer'),
        (r'\bA acquerir\b', r'À acquérir'),
        (r'\bA acquérir\b', r'À acquérir'),
        (r' a un ', r' à un '),
        (r' a une ', r' à une '),
        (r' a la ', r' à la '),
        (r' a l\'', r' à l\''),
        (r' a le ', r' à le '),  # rare, usually "au"
        (r' a les ', r' à les '),  # rare, usually "aux"
        (r' a des ', r' à des '),
        (r' a ce ', r' à ce '),
        (r' a cette ', r' à cette '),
        (r' a ces ', r' à ces '),
        (r' a cet ', r' à cet '),
        (r' a chaque ', r' à chaque '),
        (r' a tout ', r' à tout '),
        (r' a toute ', r' à toute '),
        (r' a toutes ', r' à toutes '),
        (r' a tous ', r' à tous '),
    ]

    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)

    return text


def fix_oeuvre(text):
    """Fix 'oeuvre' → 'œuvre'."""
    text = text.replace('en oeuvre', 'en œuvre')
    text = text.replace("d'oeuvre", "d'œuvre")
    return text


def process_file(filepath):
    """Process a single markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Apply main replacements
    content = apply_replacements(content)

    # Fix preposition "à"
    content = fix_preposition_a(content)

    # Fix "œuvre"
    content = fix_oeuvre(content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        # Count changes
        changes = sum(1 for a, b in zip(original, content) if a != b)
        return True, changes
    return False, 0


def main():
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
    base_dir = os.path.normpath(os.path.join(base_dir, 'v0.4', 'fr'))

    # If script is in audit_0.4, go up appropriately
    if not os.path.exists(base_dir):
        base_dir = '/home/user/ISO/v0.4/fr'

    print(f"Correction des accents dans : {base_dir}")
    print("=" * 60)

    # Find all .md files
    md_files = glob.glob(os.path.join(base_dir, '**', '*.md'), recursive=True)
    md_files.sort()

    total_modified = 0
    for filepath in md_files:
        rel_path = os.path.relpath(filepath, base_dir)
        modified, changes = process_file(filepath)
        if modified:
            total_modified += 1
            print(f"  ✓ {rel_path} ({changes} caractères modifiés)")
        else:
            print(f"  - {rel_path} (aucun changement)")

    print("=" * 60)
    print(f"Fichiers traités : {len(md_files)}")
    print(f"Fichiers modifiés : {total_modified}")


if __name__ == '__main__':
    main()
