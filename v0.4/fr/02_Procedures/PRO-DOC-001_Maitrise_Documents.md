# Procedure de Maitrise des Documents et Enregistrements

| | |
|---|---|
| **Reference** | PRO-DOC-001 |
| **Version** | 0.4 |
| **Date de creation** | 10/02/2026 |
| **Date de revision** | 18/02/2026 |
| **Redige par** | Roxane Wicky |
| **Approuve par** | Roxane Wicky |

> **Legende :** :red_circle: [A REMPLIR] = obligatoire, manquant | :yellow_circle: [RECOMMANDE] = recommande | :green_circle: = deja rempli | :blue_circle: [A VERIFIER] = a confirmer

---

## 1. Objet

Definir les regles de creation, approbation, diffusion, mise a jour et archivage de tous les documents et enregistrements du Systeme de Management de la Qualite (SMQ) de Plus Sarl.

> **S1 — Gestion documentaire : Maitrise documentaire et amelioration continue (cf. CTX-QUA-001, section 1.1) :** Les informations liees a la production et a la conformite sont conservees dans le systeme FileMaker et dans les echanges d'e-mails et WeChat. Ces elements assurent la tracabilite des operations et alimentent le suivi des non-conformites, l'audit interne et la revue de direction, permettant l'amelioration continue du systeme de management de la qualite. 🟢

## 2. Domaine d'application

Cette procedure s'applique a l'ensemble des documents du SMQ :
- Politique qualite, objectifs, cartographie
- Procedures, instructions de travail
- Formulaires et enregistrements
- Documents d'origine externe (normes, specifications clients, exigences reglementaires douanieres, etc.)
- Documents operationnels (factures douanieres, factures clients, bons de livraison, accuses de reception de commandes)

> **Note :** Le chapitre 8.3 (Conception et developpement) est exclu du domaine d'application du SMQ de Plus Sarl. L'entreprise ne realise aucune activite de conception ; elle assure la coordination industrielle entre clients europeens et fabricants chinois.

## 3. Responsabilites

| Responsabilite | Qui |
|---|---|
| Creation et mise a jour des documents | :green_circle: Roxane Wicky (gerante) |
| Approbation des documents | :green_circle: Roxane Wicky (gerante) |
| Diffusion et archivage | :green_circle: Roxane Wicky (gerante) |
| Conservation des donnees techniques de fabrication | :green_circle: Partenaires chinois (Yuyao Mould Factory et Whang) |
| Comptabilite et fiduciaire | :green_circle: Paradiso (fiduciaire) |

> **Note :** Plus Sarl etant une entreprise unipersonnelle, l'ensemble des responsabilites documentaires incombe a la gerante, Roxane Wicky. La fiduciaire Paradiso assure la gestion comptable.

## 4. Types de documents

| Type | Codification | Exemple |
|---|---|---|
| Politique | POL-XXX-NNN | POL-QUA-001 |
| Domaine d'application | DOM-XXX-NNN | DOM-QUA-001 |
| Contexte | CTX-XXX-NNN | CTX-QUA-001 |
| Cartographie | CRT-XXX-NNN | CRT-QUA-001 |
| Objectifs | OBJ-XXX-NNN | OBJ-QUA-001 |
| Leadership / Management | M1-XXX-NNN | M1-DIR-001 |
| Fiche processus | FIC-PRO-NNN | FIC-PRO-001, FIC-PRO-002 |
| Procedure | PRO-XXX-NNN | PRO-DOC-001 |
| Formulaire | FOR-XXX-NNN | FOR-EVF-001 |
| Checklist | CHK-XXX-NNN | CHK-AUD-001 |
| Liste de gestion | LST-XXX-NNN | LST-DOC-001 |
| Document externe | EXT-XXX-NNN | EXT-NRM-001 |

**Legende :** XXX = domaine (QUA=qualite, DOC=documents, AUD=audit, NCF=non-conformite, ACR=actions correctives, ACH=achats, EVF=evaluation fournisseur, SAT=satisfaction, RDR=revue direction, CMP=competences, RCL=reclamations, CTR=controle)

## 5. Procedure de gestion documentaire

### 5.1 Creation d'un document

1. Identifier le besoin de creer un nouveau document
2. Rediger le document en utilisant le modele correspondant (modeles stockes dans le dossier SMQ)
3. Attribuer une reference selon la codification definie en section 4
4. Indiquer la version (1.0 pour la creation)
5. Dater et approuver (signature de Roxane Wicky)

### 5.2 Approbation

- Tout document du SMQ est approuve par la gerante, Roxane Wicky, avant diffusion
- L'approbation est materialisee par la signature et la date sur le document

### 5.3 Diffusion et stockage

Les documents approuves sont stockes sur les supports suivants :

| Support de stockage | Contenu | Responsable |
|---|---|---|
| **FileMaker** (logiciel principal) | Bibliotheque de produits, suivi des commandes, prix, suivi du transport | :green_circle: Roxane Wicky |
| **Fichiers informatiques locaux** (ordinateur) | Documents SMQ, procedures, formulaires, enregistrements qualite | :green_circle: Roxane Wicky |
| **Archives e-mail** | Echanges avec clients, transporteurs, douanes | :green_circle: Roxane Wicky |
| **WeChat** | Echanges operationnels avec les partenaires chinois | :green_circle: Roxane Wicky |
| **Fichiers chez le partenaire chinois** | Donnees techniques de fabrication, plans, moules, specifications de production | :green_circle: Yuyao Mould Factory / Whang |
| **Fiduciaire Paradiso** | Documents comptables, declarations fiscales | :green_circle: Paradiso |

**Structure de stockage sur l'ordinateur :**

```
SMQ/
|-- 01_Politique_et_objectifs/
|-- 02_Contexte_et_processus/
|-- 03_Procedures/
|-- 04_Formulaires_vierges/
|-- 05_Enregistrements/
|   |-- [Annee]/
|       |-- Non_conformites/
|       |-- Evaluations_fournisseurs/
|       |-- Satisfaction_client/
|       |-- Audits/
|       |-- Revue_direction/
|       |-- Commandes/
|-- 06_Documents_externes/
|   |-- Normes/
|   |-- Specifications_clients/
|   |-- Documents_fournisseur/
```

### 5.4 Mise a jour (revision)

1. Identifier le besoin de modification
2. Modifier le document
3. Incrementer le numero de version (1.0 -> 1.1 pour modification mineure, 1.0 -> 2.0 pour modification majeure)
4. Mettre a jour la date de revision
5. Noter la modification dans l'historique des revisions
6. Approuver et remplacer l'ancienne version

### 5.5 Documents perimes

- Les versions perimees sont deplacees dans un dossier "Archive" avec la mention "PERIME"
- Duree de conservation des archives : 3 ans minimum

### 5.6 Documents d'origine externe

| Document externe | Source | Lieu de stockage | Responsable de la mise a jour |
|---|---|---|---|
| Norme ISO 9001:2015 | SNV / ISO | Dossier SMQ > 06_Documents_externes > Normes | :green_circle: Roxane Wicky |
| Specifications techniques clients | Clients europeens (~10 clients actifs) | Dossier SMQ > 06_Documents_externes > Specifications_clients + FileMaker | :green_circle: Roxane Wicky |
| Donnees techniques de fabrication (plans, moules) | Yuyao Mould Factory / Whang | Fichiers chez le partenaire chinois + copie locale | :green_circle: Roxane Wicky / Partenaire chinois |
| Documents douaniers et reglementaires | Autorites douanieres / transitaires | Archives e-mail + dossier local | :green_circle: Roxane Wicky |
| Rapports d'inspection fournisseur | Partenaires chinois | Dossier SMQ > 06_Documents_externes > Documents_fournisseur | :green_circle: Roxane Wicky |
| Documents comptables | Fiduciaire Paradiso | Fiduciaire + copie locale | :green_circle: Paradiso / Roxane Wicky |

## 6. Gestion des enregistrements

### 6.1 Documents operationnels generes par l'activite

| Type de document operationnel | Support de creation | Lieu de stockage |
|---|---|---|
| Factures douanieres | Logiciel / e-mail | Archives e-mail + dossier local |
| Factures clients | FileMaker / logiciel comptable | FileMaker + dossier local |
| Bons de livraison | FileMaker / e-mail | FileMaker + archives e-mail |
| Accuses de reception de commandes | E-mail | Archives e-mail |
| Suivi de transport | FileMaker | FileMaker |
| Echanges avec partenaires chinois | WeChat / e-mail | WeChat + archives e-mail |
| Documents comptables | Fiduciaire Paradiso | Fiduciaire + copie locale |

### 6.2 Duree de conservation

| Type d'enregistrement | Duree minimale de conservation |
|---|---|
| Politique qualite (versions successives) | Duree de la certification + 1 an |
| Revue de direction | 3 ans |
| Audits internes | 3 ans |
| Non-conformites et actions correctives | 3 ans |
| Evaluations fournisseurs | 3 ans |
| Reclamations clients | 3 ans |
| Satisfaction client | 3 ans |
| Commandes clients | 5 ans (obligation legale suisse) |
| Factures | 10 ans (obligation legale suisse) |
| Donnees techniques produits (moules) | Duree de vie du moule + 3 ans |

### 6.3 Sauvegarde

:green_circle: Sauvegarde cloud, hebergement chez fournisseur de services informatiques. Les donnees FileMaker et les fichiers du SMQ sont sauvegardes automatiquement dans le cloud.

Les donnees sont protegees par :
- **Sauvegarde cloud automatique** : les donnees FileMaker et les fichiers du SMQ sont sauvegardes automatiquement dans le cloud, heberge chez le fournisseur de services informatiques
- **Gestion des acces** a FileMaker (acces restreint a la gerante)

> :yellow_circle: [RECOMMANDE] Il est recommande de completer le dispositif de sauvegarde cloud par :
> - Une verification periodique (mensuelle) de l'integrite des sauvegardes
> - Un test de restauration annuel pour valider la capacite de recuperation des donnees
> - La documentation du contrat avec le fournisseur de services cloud (SLA, localisation des donnees, politique de confidentialite)

## 7. Inventaire des moules

:green_circle: Un inventaire des moules existe. Les moules sont la propriete des clients.

| Element | Detail |
|---|---|
| **Inventaire** | :green_circle: Existant |
| **Propriete** | :green_circle: Propriete des clients |
| **Lieu de stockage** | Chez les partenaires chinois (Yuyao Mould Factory / Whang) |
| **Responsable du suivi** | Roxane Wicky (gerante) |
| **Conservation** | Duree de vie du moule + 3 ans (cf. section 6.2) |

> **Note :** Les moules etant la propriete des clients, Plus Sarl assure la coordination de leur stockage et de leur maintenance chez les partenaires chinois. La tracabilite des moules est assuree via FileMaker et les echanges avec les partenaires.

## 8. Liste maitresse des documents

| Reference | Titre | Version | Date | Statut |
|---|---|---|---|---|
| POL-QUA-001 | Politique Qualite | 0.4 | 18/02/2026 | En vigueur |
| DOM-QUA-001 | Domaine d'application | 0.4 | 18/02/2026 | En vigueur |
| CTX-QUA-001 | Contexte de l'organisation | 0.4 | 18/02/2026 | En vigueur |
| CRT-QUA-001 | Cartographie des processus | 0.4 | 18/02/2026 | En vigueur |
| OBJ-QUA-001 | Objectifs qualite | 0.4 | 18/02/2026 | En vigueur |
| FIC-PRO-001 | Fiche processus O2 - Achats et sous-traitance | 0.4 | 18/02/2026 | En vigueur |
| **FIC-PRO-002** | **Fiche processus O3 - Logistique et livraison** | **0.4** | **18/02/2026** | **En vigueur** 🟢 |
| **M1-DIR-001** | **Leadership et attribution des responsabilites** | **0.4** | **18/02/2026** | **En vigueur** 🟢 |
| PRO-DOC-001 | Maitrise des documents | 0.4 | 18/02/2026 | En vigueur |
| PRO-AUD-001 | Audit interne | 0.4 | 18/02/2026 | En vigueur |
| PRO-NCF-001 | Non-conformites | 0.4 | 18/02/2026 | En vigueur |
| PRO-ACR-001 | Actions correctives | 0.4 | 18/02/2026 | En vigueur |
| PRO-ACH-001 | Achats et sous-traitance | 0.4 | 18/02/2026 | En vigueur |
| **PRO-LOG-001** | **Logistique et livraison** | **0.4** | **18/02/2026** | **En vigueur** 🟢 |
| FOR-EVF-001 | Evaluation fournisseurs | 0.4 | 18/02/2026 | En vigueur |
| FOR-SAT-001 | Satisfaction client | 0.4 | 18/02/2026 | En vigueur |
| FOR-RDR-001 | Revue de direction | 0.4 | 18/02/2026 | En vigueur |
| FOR-CMP-001 | Competences et formation | 0.4 | 18/02/2026 | En vigueur |
| FOR-RCL-001 | Reclamations client | 0.4 | 18/02/2026 | En vigueur |
| FOR-CTR-001 | Controle reception | 0.4 | 18/02/2026 | En vigueur |
| CHK-AUD-001 | Checklist audit ISO 9001 | 0.4 | 18/02/2026 | En vigueur |
| LST-DOC-001 | Liste de gestion documentaire | 0.4 | 18/02/2026 | En vigueur |

## 9. Liste de gestion documentaire (LST-DOC-001)

La liste de gestion documentaire ci-dessous recense l'ensemble des documents du SMQ avec leur statut actuel. Cette liste est tenue a jour par la gerante.

| Nom du document | Reference/code | Version | Date de mise a jour | Responsable | Emplacement |
|---|---|---|---|---|---|
| Politique Qualite | POL-QUA-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Domaine d'application | DOM-QUA-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Contexte de l'organisation | CTX-QUA-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Cartographie des processus | CRT-QUA-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Objectifs qualite | OBJ-QUA-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Fiche processus O2 - Achats et sous-traitance | FIC-PRO-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| **Fiche processus O3 - Logistique et livraison** | **FIC-PRO-002** | **0.4** | **18/02/2026** | **Roxane Wicky** | **Ordinateur / Dossier SMQ** 🟢 |
| **Leadership et attribution des responsabilites** | **M1-DIR-001** | **0.4** | **18/02/2026** | **Roxane Wicky** | **Ordinateur / Dossier SMQ** 🟢 |
| Maitrise des documents | PRO-DOC-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Audit interne | PRO-AUD-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Non-conformites | PRO-NCF-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Actions correctives | PRO-ACR-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Achats et sous-traitance | PRO-ACH-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| **Logistique et livraison** | **PRO-LOG-001** | **0.4** | **18/02/2026** | **Roxane Wicky** | **Ordinateur / Dossier SMQ** 🟢 |
| Evaluation fournisseurs | FOR-EVF-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Satisfaction client | FOR-SAT-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Revue de direction | FOR-RDR-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Competences et formation | FOR-CMP-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Reclamations client | FOR-RCL-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Controle reception | FOR-CTR-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Checklist audit ISO 9001 | CHK-AUD-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Liste de gestion documentaire | LST-DOC-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |

---

## Historique des revisions

| Version | Date | Description de la modification | Auteur |
|---|---|---|---|
| 0.1 | 10/02/2026 | Creation initiale | Roxane Wicky |
| 0.2 | 10/02/2026 | Ajout de la liste de gestion documentaire (LST-DOC-001) alignee sur le modele de la gerante. Ajout du type de document LST (Liste de gestion). Mise a jour de la liste maitresse avec tous les documents du SMQ en version 0.2. | Roxane Wicky |
| 0.3 | 12/02/2026 | Integration des reponses (Whang, Paradiso, SQS, cloud, echantillonnage CQ). Ajout du systeme de legende des champs. | Roxane Wicky |
| 0.4 | 18/02/2026 | Integration UPDATE 2.1 S1 : ajout reference au role formalise de la gestion documentaire (CTX-QUA-001 section 1.1). Ajout de 3 nouveaux documents a la liste maitresse et a la liste de gestion : M1-DIR-001, FIC-PRO-002, PRO-LOG-001. Ajout du type de document M1 (Leadership). | Roxane Wicky |
