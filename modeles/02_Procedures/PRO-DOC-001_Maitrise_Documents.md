# Procedure de Maitrise des Documents et Enregistrements

| | |
|---|---|
| **Reference** | PRO-DOC-001 |
| **Version** | 1.0 |
| **Date de creation** | [JJ/MM/AAAA] |
| **Date de revision** | [JJ/MM/AAAA] |
| **Redige par** | [Nom de la gerante] |
| **Approuve par** | [Nom de la gerante] |

---

## 1. Objet

Definir les regles de creation, approbation, diffusion, mise a jour et archivage de tous les documents et enregistrements du Systeme de Management de la Qualite (SMQ) de DUMMY Sarl.

## 2. Domaine d'application

Cette procedure s'applique a l'ensemble des documents du SMQ :
- Politique qualite, objectifs, cartographie
- Procedures, instructions de travail
- Formulaires et enregistrements
- Documents d'origine externe (normes, specifications clients, etc.)

## 3. Responsabilites

| Responsabilite | Qui |
|---|---|
| Creation et mise a jour des documents | Gerante |
| Approbation des documents | Gerante |
| Diffusion et archivage | Gerante |

## 4. Types de documents

| Type | Codification | Exemple |
|---|---|---|
| Politique | POL-XXX-NNN | POL-QUA-001 |
| Domaine d'application | DOM-XXX-NNN | DOM-QUA-001 |
| Contexte | CTX-XXX-NNN | CTX-QUA-001 |
| Cartographie | CRT-XXX-NNN | CRT-QUA-001 |
| Objectifs | OBJ-XXX-NNN | OBJ-QUA-001 |
| Fiche processus | FIC-PRO-NNN | FIC-PRO-001 |
| Procedure | PRO-XXX-NNN | PRO-DOC-001 |
| Formulaire | FOR-XXX-NNN | FOR-EVF-001 |
| Checklist | CHK-XXX-NNN | CHK-AUD-001 |
| Document externe | EXT-XXX-NNN | EXT-NRM-001 |

**Legende :** XXX = domaine (QUA=qualite, DOC=documents, AUD=audit, NCF=non-conformite, ACR=actions correctives, ACH=achats, EVF=evaluation fournisseur, SAT=satisfaction, RDR=revue direction, CMP=competences, RCL=reclamations, CTR=controle)

## 5. Procedure de gestion documentaire

### 5.1 Creation d'un document

1. Identifier le besoin de creer un nouveau document
2. Rediger le document en utilisant le modele correspondant
3. Attribuer une reference selon la codification
4. Indiquer la version (1.0 pour la creation)
5. Dater et signer (approuver)

### 5.2 Approbation

- Tout document du SMQ est approuve par la gerante avant diffusion
- L'approbation est materialisee par la signature et la date sur le document

### 5.3 Diffusion

- Les documents approuves sont stockes dans : [lieu de stockage - dossier informatique, cloud, classeur]
- Emplacement principal : [Ex : Dossier "SMQ" sur l'ordinateur / OneDrive / Google Drive]
- Structure de stockage :

```
SMQ/
|-- 01_Politique_et_objectifs/
|-- 02_Contexte_et_processus/
|-- 03_Procedures/
|-- 04_Formulaires_vierges/
|-- 05_Enregistrements/
|   |-- [Annee]/
|       |-- Controles_reception/
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
- Duree de conservation des archives : [3 ans minimum / duree de la certification]

### 5.6 Documents d'origine externe

| Document externe | Source | Lieu de stockage | Responsable de la mise a jour |
|---|---|---|---|
| Norme ISO 9001:2015 | SNV / ISO | [Emplacement] | Gerante |
| Specifications clients | Clients | [Emplacement] | Gerante |
| Rapports d'inspection fournisseur | Partenaire chinois | [Emplacement] | Gerante |
| [A completer] | | | |

## 6. Gestion des enregistrements

### Duree de conservation

| Type d'enregistrement | Duree minimale de conservation |
|---|---|
| Politique qualite (versions successives) | Duree de la certification + 1 an |
| Revue de direction | 3 ans |
| Audits internes | 3 ans |
| Non-conformites et actions correctives | 3 ans |
| Controles a reception | 3 ans |
| Evaluations fournisseurs | 3 ans |
| Reclamations clients | 3 ans |
| Satisfaction client | 3 ans |
| Commandes clients | 5 ans (obligation legale suisse) |
| Factures | 10 ans (obligation legale suisse) |
| Dossiers de conception | Duree de vie du moule + 3 ans |

### Sauvegarde

- Sauvegarde informatique : [Methode - ex : sauvegarde automatique cloud + disque externe hebdomadaire]
- Frequence : [Ex : quotidienne (cloud) + hebdomadaire (disque externe)]
- Verification : [Ex : mensuelle]

## 7. Liste maitresse des documents

| Reference | Titre | Version | Date | Statut |
|---|---|---|---|---|
| POL-QUA-001 | Politique Qualite | 1.0 | [date] | En vigueur |
| DOM-QUA-001 | Domaine d'application | 1.0 | [date] | En vigueur |
| CTX-QUA-001 | Contexte de l'organisation | 1.0 | [date] | En vigueur |
| CRT-QUA-001 | Cartographie des processus | 1.0 | [date] | En vigueur |
| OBJ-QUA-001 | Objectifs qualite | 1.0 | [date] | En vigueur |
| FIC-PRO-001 | Fiche processus (type) | 1.0 | [date] | En vigueur |
| PRO-DOC-001 | Maitrise des documents | 1.0 | [date] | En vigueur |
| PRO-AUD-001 | Audit interne | 1.0 | [date] | En vigueur |
| PRO-NCF-001 | Non-conformites | 1.0 | [date] | En vigueur |
| PRO-ACR-001 | Actions correctives | 1.0 | [date] | En vigueur |
| PRO-ACH-001 | Achats et sous-traitance | 1.0 | [date] | En vigueur |
| [Ajouter les formulaires...] | | | | |

---

> **Instructions de remplissage :**
> 1. Definissez votre lieu de stockage principal (dossier informatique, cloud, etc.)
> 2. Creez la structure de dossiers indiquee en 5.3
> 3. Mettez a jour la liste maitresse a chaque creation/modification de document
> 4. Gardez cette procedure simple - elle doit refleter ce que vous faites reellement
