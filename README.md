# Projet de Certification ISO 9001:2015 — Plus Sarl

## Objectif

Ce depot contient l'ensemble des documents necessaires a la mise en place d'un Systeme de Management de la Qualite (SMQ) conforme a la norme ISO 9001:2015 pour **Plus Sarl**.

## Profil de l'entreprise

| Element | Detail |
|---|---|
| Raison sociale | Plus Sarl |
| Siege social | Route de Montet 11, 1588 Cudrefin, Suisse (canton de Fribourg) |
| Forme juridique | Sarl (Societe a responsabilite limitee) |
| Annee de fondation | 2007 |
| Effectif | 1 salariee (gerante) |
| Gerante | Roxane Wicky |
| Associes | Roxane Wicky, Olav Wicky, Capucine Wicky |
| Activite | Coordination industrielle Chine-Europe : developpement de moules, injection plastique, pieces industrielles, vis |
| Fabrication | Externalisee en Chine (Yuyao Mould Factory, Whang) |
| Clients | ~10 clients actifs, europeens (B2B) |
| Fiduciaire | Paradiso |
| Organisme de certification | SQS |
| Exclusion | Chapitre 8.3 (Conception et developpement) — les designs sont la propriete des clients |

## Version actuelle : v0.4 (18/02/2026)

### Historique des versions

| Version | Date | Langue | Description |
|---|---|---|---|
| v0.1 | 10/02/2026 | FR | Modeles initiaux generiques (21 documents) |
| v0.2 | 10/02/2026 | FR | Personnalisation avec les donnees de Plus Sarl (source PDF interview) |
| v0.3 | 12/02/2026 | FR + EN | Integration des reponses complementaires. Ajout legende, cartographie interactive, suivi des informations manquantes |
| v0.4 | 18/02/2026 | FR | Integration de 4 PDFs UPDATE du manuel qualite (chapitres 2.1, 2.2, 2.2.1, 3/3.1). 3 nouveaux documents. 24 fichiers |

### Nouveautes v0.4

- **UPDATE 2.1** : Activites et organisation de la production externalisee (5 processus formalises)
- **UPDATE 2.2** : Relation client et comprehension des besoins
- **UPDATE 2.2.1** : Analyse et validation des demandes clients (revue de commande)
- **UPDATE 3/3.1** : Organisation, roles, responsabilites et autorites detailles par processus
- **3 nouveaux documents** : M1-DIR-001 (Leadership), PRO-LOG-001 (Logistique), FIC-PRO-002 (Fiche processus Logistique)

## Structure du depot

```
ISO/
|-- README.md                              # Ce fichier
|-- GUIDE_CERTIFICATION.md                 # Guide complet etape par etape
|-- PLANNING.md                            # Planning detaille sur 12 mois
|-- QUESTIONS.md                           # Questions / reponses pour personnalisation
|
|-- source/                                # PDFs sources (interview, updates)
|   |-- ISO9001_RW_260210.pdf              # Interview initiale
|   |-- UPDATE_ISO9001_2.1_260218.pdf      # Chapitre 2.1 — Production externalisee
|   |-- UPDATE_ISO9001_2.2_RW_260218.pdf   # Chapitre 2.2 — Relation client
|   |-- UPDATE_ISO9001_RW_2.2.1_260218.pdf # Chapitre 2.2.1 — Revue de commande
|   |-- ISO9001_UDPATE_RW_3.260218.pdf     # Chapitre 3/3.1 — Roles et responsabilites
|   |-- (+ PDFs formulaires sources)
|
|-- modeles/                               # Templates generiques v0.1
|-- v0.1/ ... v0.3/                        # Versions anterieures
|
|-- v0.4/
    |-- fr/                                # Version courante (francais)
        |-- LEGENDE.md                     # Systeme de legende des champs
        |-- INFORMATIONS_MANQUANTES_v0.4.md # Suivi des informations a completer
        |-- CRT-QUA-001_Cartographie_Processus.drawio  # Cartographie interactive
        |
        |-- 01_Documents_Obligatoires/     # 8 documents
        |   |-- POL-QUA-001  Politique Qualite
        |   |-- CTX-QUA-001  Contexte de l'Organisation
        |   |-- DOM-QUA-001  Domaine d'Application
        |   |-- CRT-QUA-001  Cartographie des Processus
        |   |-- OBJ-QUA-001  Objectifs Qualite
        |   |-- FIC-PRO-001  Fiche Processus O2 — Achats
        |   |-- FIC-PRO-002  Fiche Processus O3 — Logistique      [NOUVEAU v0.4]
        |   |-- M1-DIR-001   Leadership et Responsabilites         [NOUVEAU v0.4]
        |
        |-- 02_Procedures/                 # 6 procedures
        |   |-- PRO-DOC-001  Maitrise des Documents
        |   |-- PRO-ACH-001  Achats et Sous-traitance
        |   |-- PRO-AUD-001  Audit Interne
        |   |-- PRO-NCF-001  Non-Conformites
        |   |-- PRO-ACR-001  Actions Correctives
        |   |-- PRO-LOG-001  Logistique et Livraison               [NOUVEAU v0.4]
        |
        |-- 03_Formulaires_Registres/      # 6 formulaires
        |   |-- FOR-EVF-001  Evaluation Fournisseurs
        |   |-- FOR-SAT-001  Satisfaction Client
        |   |-- FOR-RDR-001  Revue de Direction
        |   |-- FOR-CMP-001  Competences et Formation
        |   |-- FOR-RCL-001  Reclamations Client
        |   |-- FOR-CTR-001  Controle Reception
        |
        |-- 04_Checklists/                 # 1 checklist
            |-- CHK-AUD-001  Checklist Audit ISO 9001
```

**Total : 24 fichiers** (21 de base + 3 nouveaux en v0.4)

## Processus formalises

| Code | Processus | Type |
|---|---|---|
| **M1** | Leadership et strategie | Management |
| **M2** | Amelioration continue | Management |
| **M3** | Revue de direction | Management |
| **O1** | Commercial | Operationnel |
| **O2** | Achats et sous-traitance | Operationnel |
| **O3** | Logistique et livraison | Operationnel |
| **O4** | Controle qualite | Operationnel |
| **S1** | Gestion documentaire | Support |
| **S2** | Competences et formations | Support |
| **S3** | Ressources et infrastructure | Support |

> Pilote de tous les processus : Roxane Wicky (entreprise unipersonnelle)

## Codification des documents

| Prefixe | Type de document |
|---|---|
| POL | Politique |
| DOM | Domaine |
| CTX | Contexte |
| CRT | Cartographie |
| OBJ | Objectifs |
| FIC | Fiche processus |
| PRO | Procedure |
| FOR | Formulaire |
| CHK | Checklist |
| M1 | Leadership / Management |

## Legende des champs

| Symbole | Signification |
|---|---|
| 🟢 | Deja rempli |
| 🔴 [A REMPLIR] | Obligatoire, manquant |
| 🟡 [RECOMMANDE] | Recommande |
| 🔵 [A VERIFIER] | A confirmer |

## Comment utiliser ce depot

1. **Version courante** : Travailler dans `v0.4/fr/`
2. **Suivi** : Consulter `INFORMATIONS_MANQUANTES_v0.4.md` pour les champs restants
3. **Sources** : Les PDFs de reference sont dans `source/`
4. **Historique** : Les versions anterieures sont conservees (v0.1 a v0.3)
5. **Versionning** : Utiliser git pour tracer les evolutions
