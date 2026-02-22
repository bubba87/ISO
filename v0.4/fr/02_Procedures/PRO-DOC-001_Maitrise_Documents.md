# Procédure de Maîtrise des Documents et Enregistrements

| | |
|---|---|
| **Référence** | PRO-DOC-001 |
| **Version** | 0.4 |
| **Date de création** | 10/02/2026 |
| **Date de revision** | 18/02/2026 |
| **Rédigé par** | Roxane Wicky |
| **Approuve par** | Roxane Wicky |

> **Légende :** :red_circle: [À REMPLIR] = obligatoire, manquant | :yellow_circle: [RECOMMANDE] = recommandé | :green_circle: = déjà rempli | :blue_circle: [À VÉRIFIER] = a confirmer

---

## 1. Objet

Définir les règles de création, approbation, diffusion, mise à jour et archivage de tous les documents et enregistrements du Système de Management de la Qualité (SMQ) de Plus Sarl.

> **S1 — Gestion documentaire : Maîtrise documentaire et amélioration continue (cf. CTX-QUA-001, section 1.1) :** Les informations liées à la production et à la conformité sont conservées dans le système FileMaker et dans les échanges d'e-mails et WeChat. Ces éléments assurent la traçabilité des opérations et alimentent le suivi des non-conformites, l'audit interne et la revue de direction, permettant l'amélioration continue du système de management de la qualité. 🟢

## 2. Domaine d'application

Cette procédure s'applique à l\'ensemble des documents du SMQ :
- Politique qualité, objectifs, cartographie
- Procédures, instructions de travail
- Formulaires et enregistrements
- Documents d'origine externe (normes, spécifications clients, exigences réglementaires douanières, etc.)
- Documents opérationnels (factures douanières, factures clients, bons de livraison, accuses de reception de commandes)

> **Note :** Le chapitre 8.3 (Conception et développement) est exclu du domaine d'application du SMQ de Plus Sarl. L'entreprise ne réalise aucune activité de conception ; elle assure la coordination industrielle entre clients européens et fabricants chinois.

## 3. Responsabilités

| Responsabilité | Qui |
|---|---|
| Création et mise à jour des documents | :green_circle: Roxane Wicky (gérante) |
| Approbation des documents | :green_circle: Roxane Wicky (gérante) |
| Diffusion et archivage | :green_circle: Roxane Wicky (gérante) |
| Conservation des données techniques de fabrication | :green_circle: Partenaires chinois (Yuyao Mould Factory et Oukailuo) |
| Comptabilite et fiduciaire | :green_circle: Paradiso (fiduciaire) |

> **Note :** Plus Sarl étant une entreprise unipersonnelle, l'ensemble des responsabilités documentaires incombe à la gérante, Roxane Wicky. La fiduciaire Paradiso assure la gestion comptable.

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
| Procédure | PRO-XXX-NNN | PRO-DOC-001 |
| Formulaire | FOR-XXX-NNN | FOR-EVF-001 |
| Checklist | CHK-XXX-NNN | CHK-AUD-001 |
| Liste de gestion | LST-XXX-NNN | LST-DOC-001 |
| Document externe | EXT-XXX-NNN | EXT-NRM-001 |

**Légende :** XXX = domaine (QUA=qualité, DOC=documents, AUD=audit, NCF=non-conformité, ACR=actions correctives, ACH=achats, EVF=évaluation fournisseur, AQF=accord qualité fournisseur, SAT=satisfaction, RDR=revue direction, CMP=compétences, RCL=réclamations, CTR=contrôle)

## 5. Procédure de gestion documentaire

### 5.1 Création d'un document

1. Identifier le besoin de créer un nouveau document
2. Rediger le document en utilisant le modèle correspondant (modèles stockés dans le dossier SMQ)
3. Attribuer une référence selon la codification définié en section 4
4. Indiquer la version (1.0 pour la création)
5. Dater et approuver (signature de Roxane Wicky)

### 5.2 Approbation

- Tout document du SMQ est approuvé par la gérante, Roxane Wicky, avant diffusion
- L'approbation est materialisee par la signature et la date sur le document

### 5.3 Diffusion et stockage

Les documents approuves sont stockés sur les supports suivants :

| Support de stockage | Contenu | Responsable |
|---|---|---|
| **FileMaker** (logiciel principal) | Bibliotheque de produits, suivi des commandes, prix, suivi du transport | :green_circle: Roxane Wicky |
| **Fichiers informatiques locaux** (ordinateur) | Documents SMQ, procédures, formulaires, enregistrements qualité | :green_circle: Roxane Wicky |
| **Archivés e-mail** | Échanges avec clients, transporteurs, douanes | :green_circle: Roxane Wicky |
| **WeChat** | Échanges opérationnels avec les partenaires chinois | :green_circle: Roxane Wicky |
| **Fichiers chez le partenaire chinois** | Données techniques de fabrication, plans, moules, spécifications de production | :green_circle: Yuyao Mould Factory / Oukailuo |
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

### 5.4 Mise à jour (revision)

1. Identifier le besoin de modification
2. Modifier le document
3. Incrementer le numéro de version (1.0 -> 1.1 pour modification mineure, 1.0 -> 2.0 pour modification majeure)
4. Mettre a jour la date de revision
5. Noter la modification dans l'historique des revisions
6. Approuver et remplacer l'ancienne version

### 5.5 Documents perimes

- Les versions perimees sont deplacees dans un dossier "Archive" avec la mention "PERIME"
- Duree de conservation des archivés : 3 ans minimum

### 5.6 Documents d'origine externe

| Document externe | Source | Lieu de stockage | Responsable de la mise à jour |
|---|---|---|---|
| Norme ISO 9001:2015 | SNV / ISO | Dossier SMQ > 06_Documents_externes > Normes | :green_circle: Roxane Wicky |
| Specifications techniques clients | Clients européens (~10 clients actifs) | Dossier SMQ > 06_Documents_externes > Specifications_clients + FileMaker | :green_circle: Roxane Wicky |
| Données techniques de fabrication (plans, moules) | Yuyao Mould Factory / Oukailuo | Fichiers chez le partenaire chinois + copie locale | :green_circle: Roxane Wicky / Partenaire chinois |
| Documents douaniers et réglementaires | Autorites douanières / transitaires | Archivés e-mail + dossier local | :green_circle: Roxane Wicky |
| Rapports d'inspection fournisseur | Partenaires chinois | Dossier SMQ > 06_Documents_externes > Documents_fournisseur | :green_circle: Roxane Wicky |
| Documents comptables | Fiduciaire Paradiso | Fiduciaire + copie locale | :green_circle: Paradiso / Roxane Wicky |

## 5bis. Maîtrise des informations documentées (clause 7.5)

> **Source :** UPDATE 7.5-8.7 — Informations documentées (21/02/2026) 🟢

Plus Sarl détermine, crée, met à jour et maîtrise les informations documentées nécessaires à l'efficacité de son système de management de la qualité et à la conformité des produits et services fournis.

### Exigences de maîtrise

Plus Sarl veille à assurer :
- **l'accessibilité** aux seules personnes autorisées
- **la lisibilité** et l'identification des documents
- **la conservation** appropriée des enregistrements
- **la protection** contre toute perte, détérioration ou utilisation non maîtrisée

### Confidentialité des données

Les données techniques, commerciales et contractuelles, y compris les designs et spécifications appartenant aux clients, sont traitées comme **strictement confidentielles**.

La confidentialité est assurée notamment par :
- un accès sécurisé aux systèmes informatiques
- la limitation des échanges aux interlocuteurs concernés
- l'organisation structurée des supports numériques
- la protection des accès aux bases de données et aux messageries
- la transmission contrôlée des informations aux partenaires industriels

Ces dispositions garantissent la traçabilité des opérations, la protection de la propriété intellectuelle des clients, la conformité aux exigences réglementaires ainsi que la continuité des activités.

---

## 6. Gestion des enregistrements

### 6.1 Documents opérationnels générés par l'activité

| Type de document opérationnel | Support de création | Lieu de stockage |
|---|---|---|
| Factures douanières | Logiciel / e-mail | Archivés e-mail + dossier local |
| Factures clients | FileMaker / logiciel comptable | FileMaker + dossier local |
| Bons de livraison | FileMaker / e-mail | FileMaker + archivés e-mail |
| Accuses de reception de commandes | E-mail | Archivés e-mail |
| Suivi de transport | FileMaker | FileMaker |
| Échanges avec partenaires chinois | WeChat / e-mail | WeChat + archivés e-mail |
| Documents comptables | Fiduciaire Paradiso | Fiduciaire + copie locale |

### 6.2 Duree de conservation

| Type d'enregistrement | Duree minimale de conservation |
|---|---|
| Politique qualité (versions successives) | Duree de la certification + 1 an |
| Revue de direction | 3 ans |
| Audits internes | 3 ans |
| Non-conformites et actions correctives | 3 ans |
| Évaluations fournisseurs | 3 ans |
| Réclamations clients | 3 ans |
| Satisfaction client | 3 ans |
| Commandes clients | 5 ans (obligation legale suisse) |
| Factures | 10 ans (obligation legale suisse) |
| Données techniques produits (moules) | Duree de vie du moule + 3 ans |

### 6.3 Sauvegarde

🟢 Le système FileMaker est hébergé chez **Gramatec SA** en Suisse. L'enregistrement est automatique. Les données sont stockées chez Gramatec. En cas de perte, vol ou problème sur le système, Gramatec SA est disposé à ressortir l'ensemble des données.

Les données sont protégées par :
- **Hébergement suisse** : Gramatec SA, fournisseur de services informatiques basé en Suisse 🟢
- **Sauvegarde automatique** : enregistrement automatique des données FileMaker 🟢
- **Restauration garantie** : Gramatec SA assure la récupération complète des données en cas d'incident 🟢
- **Gestion des accès** à FileMaker (accès restreint à la gérante)

> 🟡 [RECOMMANDÉ] Il est recommandé de compléter le dispositif par :
> - Une vérification périodique (mensuelle) de l'intégrité des sauvegardes
> - Un test de restauration annuel pour valider la capacité de récupération des données
> - La documentation du contrat avec Gramatec SA (SLA, localisation des données, politique de confidentialité)

> **Source :** Récap 13 points (22/02/2026) — Point #9 résolu.

## 7. Inventaire des moules

:green_circle: Un inventaire des moules existe. Les moules sont la propriété des clients.

| Élément | Détail |
|---|---|
| **Inventaire** | :green_circle: Existant |
| **Propriété** | :green_circle: Propriété des clients |
| **Lieu de stockage** | Chez les partenaires chinois (Hardeng Yuyao Mould Factory / Oukailuo) |
| **Responsable du suivi** | Roxane Wicky (gérante) |
| **Conservation** | Duree de vie du moule + 3 ans (cf. section 6.2) |

> **Note :** Les moules étant la propriété des clients, Plus Sarl assure la coordination de leur stockage et de leur maintenance chez les partenaires chinois. La traçabilité des moules est assurée via FileMaker et les échanges avec les partenaires.

## 8. Liste maitresse des documents

| Référence | Titre | Version | Date | Statut |
|---|---|---|---|---|
| POL-QUA-001 | Politique Qualité | 0.4 | 18/02/2026 | En vigueur |
| DOM-QUA-001 | Domaine d'application | 0.4 | 18/02/2026 | En vigueur |
| CTX-QUA-001 | Contexte de l'organisation | 0.4 | 18/02/2026 | En vigueur |
| CRT-QUA-001 | Cartographie des processus | 0.4 | 18/02/2026 | En vigueur |
| OBJ-QUA-001 | Objectifs qualité | 0.4 | 18/02/2026 | En vigueur |
| FIC-PRO-001 | Fiche processus O2 - Achats et sous-traitance | 0.4 | 18/02/2026 | En vigueur |
| **FIC-PRO-002** | **Fiche processus O3 - Logistique et livraison** | **0.4** | **18/02/2026** | **En vigueur** 🟢 |
| **M1-DIR-001** | **Leadership et attribution des responsabilités** | **0.4** | **18/02/2026** | **En vigueur** 🟢 |
| PRO-DOC-001 | Maîtrise des documents | 0.4 | 18/02/2026 | En vigueur |
| PRO-AUD-001 | Audit interne | 0.4 | 18/02/2026 | En vigueur |
| PRO-NCF-001 | Non-conformites | 0.4 | 18/02/2026 | En vigueur |
| PRO-ACR-001 | Actions correctives | 0.4 | 18/02/2026 | En vigueur |
| PRO-ACH-001 | Achats et sous-traitance | 0.4 | 18/02/2026 | En vigueur |
| **PRO-LOG-001** | **Logistique et livraison** | **0.4** | **18/02/2026** | **En vigueur** 🟢 |
| FOR-EVF-001 | Évaluation fournisseurs | 0.4 | 18/02/2026 | En vigueur |
| FOR-SAT-001 | Satisfaction client | 0.4 | 18/02/2026 | En vigueur |
| FOR-RDR-001 | Revue de direction | 0.4 | 18/02/2026 | En vigueur |
| FOR-CMP-001 | Compétences et formation | 0.4 | 18/02/2026 | En vigueur |
| FOR-RCL-001 | Réclamations client | 0.4 | 18/02/2026 | En vigueur |
| FOR-CTR-001 | Contrôle reception | 0.4 | 18/02/2026 | En vigueur |
| **FOR-AQF-001** | **Accord qualité fournisseur — Hardeng Yuyao Mould Factory** | **0.4** | **22/02/2026** | **En vigueur** 🟢 |
| **FOR-AQF-002** | **Accord qualité fournisseur — Oukailuo** | **0.4** | **22/02/2026** | **En vigueur** 🟢 |
| CHK-AUD-001 | Checklist audit ISO 9001 | 0.4 | 18/02/2026 | En vigueur |
| LST-DOC-001 | Liste de gestion documentaire | 0.4 | 18/02/2026 | En vigueur |

## 9. Liste de gestion documentaire (LST-DOC-001)

La liste de gestion documentaire ci-dessous recense l'ensemble des documents du SMQ avec leur statut actuel. Cette liste est tenue a jour par la gérante.

| Nom du document | Référence/code | Version | Date de mise à jour | Responsable | Emplacement |
|---|---|---|---|---|---|
| Politique Qualité | POL-QUA-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Domaine d'application | DOM-QUA-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Contexte de l'organisation | CTX-QUA-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Cartographie des processus | CRT-QUA-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Objectifs qualité | OBJ-QUA-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Fiche processus O2 - Achats et sous-traitance | FIC-PRO-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| **Fiche processus O3 - Logistique et livraison** | **FIC-PRO-002** | **0.4** | **18/02/2026** | **Roxane Wicky** | **Ordinateur / Dossier SMQ** 🟢 |
| **Leadership et attribution des responsabilités** | **M1-DIR-001** | **0.4** | **18/02/2026** | **Roxane Wicky** | **Ordinateur / Dossier SMQ** 🟢 |
| Maîtrise des documents | PRO-DOC-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Audit interne | PRO-AUD-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Non-conformites | PRO-NCF-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Actions correctives | PRO-ACR-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Achats et sous-traitance | PRO-ACH-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| **Logistique et livraison** | **PRO-LOG-001** | **0.4** | **18/02/2026** | **Roxane Wicky** | **Ordinateur / Dossier SMQ** 🟢 |
| Évaluation fournisseurs | FOR-EVF-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Satisfaction client | FOR-SAT-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Revue de direction | FOR-RDR-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Compétences et formation | FOR-CMP-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Réclamations client | FOR-RCL-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Contrôle reception | FOR-CTR-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| **Accord qualité Yuyao** | **FOR-AQF-001** | **0.4** | **22/02/2026** | **Roxane Wicky** | **Ordinateur / Dossier SMQ** 🟢 |
| **Accord qualité Oukailuo** | **FOR-AQF-002** | **0.4** | **22/02/2026** | **Roxane Wicky** | **Ordinateur / Dossier SMQ** 🟢 |
| Checklist audit ISO 9001 | CHK-AUD-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |
| Liste de gestion documentaire | LST-DOC-001 | 0.4 | 18/02/2026 | Roxane Wicky | Ordinateur / Dossier SMQ |

---

## Historique des revisions

| Version | Date | Description de la modification | Auteur |
|---|---|---|---|
| 0.1 | 10/02/2026 | Création initiale | Roxane Wicky |
| 0.2 | 10/02/2026 | Ajout de la liste de gestion documentaire (LST-DOC-001) alignee sur le modèle de la gérante. Ajout du type de document LST (Liste de gestion). Mise à jour de la liste maitresse avec tous les documents du SMQ en version 0.2. | Roxane Wicky |
| 0.3 | 12/02/2026 | Intégration des réponses (Oukailuo, Paradiso, SQS, cloud, echantillonnage CQ). Ajout du système de légende des champs. | Roxane Wicky |
| 0.4 | 18/02/2026 | Intégration UPDATE 2.1 S1 : ajout référence au rôle formalisé de la gestion documentaire (CTX-QUA-001 section 1.1). Ajout de 3 nouveaux documents à la liste maitresse et à la liste de gestion : M1-DIR-001, FIC-PRO-002, PRO-LOG-001. Ajout du type de document M1 (Leadership). | Roxane Wicky |
| 0.4 | 21/02/2026 | Intégration UPDATE 7.5 : ajout section 5bis — Maîtrise des informations documentées (clause 7.5). Exigences de maîtrise (accessibilité, lisibilité, conservation, protection). Confidentialité des données techniques et mesures de protection. | Roxane Wicky |
| 0.4 | 22/02/2026 | Récap 13 points — Point #9 : sauvegarde précisée (Gramatec SA, Suisse, enregistrement automatique, restauration garantie). Renommage Whang → Oukailuo. Ajout FOR-AQF-001 (Yuyao) et FOR-AQF-002 (Oukailuo) à la liste maîtresse et à la liste de gestion (RECAP point #2). Ajout codification AQF. | Roxane Wicky |
