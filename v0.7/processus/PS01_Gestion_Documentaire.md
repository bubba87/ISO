# PS01 - Processus de Gestion Documentaire

| **Processus**       | PS01 - Gestion Documentaire                            |
|----------------------|------------------------------------------------------|
| **Type**            | Support                                               |
| **Pilote**          | Rôle Gestion Documentaire                             |
| **Version**         | v0.7                                                  |
| **Date**            | 2026-03-04                                            |
| **Référence**       | PR-PS01-GD                                              |
| **Norme ISO 9001**  | Chapitres 7.5                                         |

---

## 1. Objet et domaine d'application

Ce processus décrit la gestion documentaire du Système de Management de la Qualité (SMQ) de **Plus Sàrl**. Il couvre la création, la révision, l'approbation, la diffusion, l'archivage et la destruction des documents et enregistrements du SMQ.

---

## 2. Références normatives

- ISO 9001:2015, Chapitre 7.5 (Informations documentées)
- Manuel Qualité Plus Sàrl (MQ-001)

---

## 3. Rôles et responsabilités

| Rôle                        | Responsabilités principales                                          |
|-----------------------------|----------------------------------------------------------------------|
| **Gestion Documentaire**    | Administration du système documentaire, contrôle des versions, diffusion |
| **Pilotes de processus**    | Rédaction et mise à jour des documents de leur processus             |
| **Direction**               | Approbation des documents stratégiques (Manuel, Politique)           |
| **Responsable Qualité**     | Vérification de la conformité documentaire, approbation des procédures |

---

## 4. Système de codification

### 4.1 Types de documents

| Code Préfixe | Type de document          | Description                                          |
|-------------|---------------------------|------------------------------------------------------|
| **MQ**      | Manuel Qualité             | Document stratégique décrivant le SMQ                |
| **PR**      | Procédure                  | Description détaillée d'un processus                 |
| **IT**      | Instruction de travail     | Mode opératoire détaillé pour une tâche spécifique   |
| **FM**      | Formulaire                 | Modèle à remplir pour enregistrer des données        |
| **EN**      | Enregistrement             | Preuve de la réalisation d'une activité              |

### 4.2 Convention de codification

Le code d'un document suit la structure suivante :

```
[TYPE]-[PROCESSUS]-[IDENTIFIANT]
```

**Exemples :**
- `MQ-001` : Manuel Qualité, document principal
- `PR-P01-COM` : Procédure du processus P01 Commercial
- `IT-P04-ECH` : Instruction de travail échantillonnage AQL (P04)
- `FM-P02-AQF` : Formulaire Accord Qualité Fournisseur (P02)
- `EN-P03-POD` : Enregistrement preuves de livraison (P03)

### 4.3 Convention de version

Les versions suivent le format **vX.Y** :
- **X** (majeur) : Modification structurelle ou de fond significative
- **Y** (mineur) : Correction, ajustement, mise à jour mineure

Exemples : v0.1, v0.7, v1.0, v1.1, v2.0

---

## 5. Données d'entrée et de sortie

### Données d'entrée
- Besoin de création ou de modification documentaire
- Exigences normatives et réglementaires
- Retours d'audit (interne ou externe)
- Demandes des pilotes de processus
- Documents obsolètes à réviser

### Données de sortie
- Documents approuvés et diffusés
- Registre documentaire à jour (FM-PS01-GD)
- Documents obsolètes archivés ou détruits
- Historique des versions

---

## 6. Description des activités

### A1 - Identification du besoin documentaire

Le Rôle Gestion Documentaire ou le Pilote de processus identifie le besoin de créer, modifier ou supprimer un document. Le besoin est formalisé et justifié.

### A2 - Rédaction ou révision du document

Le rédacteur désigné (généralement le Pilote du processus concerné) rédige ou révise le document en respectant les modèles et la codification définis. Le document est identifié avec son code, sa version, sa date et son statut.

### A3 - Vérification

Le Rôle Gestion Documentaire vérifie la conformité du document : respect de la codification, cohérence avec le SMQ, absence de contradictions, complétude.

### A4 - Approbation

Le document est approuvé par le responsable habilité selon la matrice d'approbation :
- Manuel Qualité, Politique : Direction
- Procédures : Responsable Qualité
- Instructions de travail, Formulaires : Pilote de processus

### A5 - Diffusion et mise à disposition

Le Rôle Gestion Documentaire diffuse le document approuvé aux destinataires concernés, met à jour le registre documentaire (FM-PS01-GD) et s'assure du retrait des versions obsolètes.

### A6 - Gestion des enregistrements et archivage

Le Rôle Gestion Documentaire assure la conservation des enregistrements selon les durées de rétention définies, dans des conditions garantissant leur lisibilité, intégrité et accessibilité.

### A7 - Revue périodique et destruction

Le Rôle Gestion Documentaire conduit une revue périodique (annuelle) de la documentation pour identifier les documents à mettre à jour ou à détruire. Les documents au-delà de leur durée de rétention sont détruits de manière contrôlée.

---

## 7. Diagramme swimlane

```
 PROCESSUS PS01 - GESTION DOCUMENTAIRE
 ============================================================================

 Rôle                 | Flux des activités
 ============================================================================
                      |
 GESTION              |  [A1 Identifier]         [A3 Vérifier]
 DOCUMENTAIRE         |  le besoin          ---> conformité du
                      |  documentaire            document
                      |       |                       |
                      |       |                       v
                      |       |                  Conforme ?
                      |       |                  OUI --> [A5]
                      |       |                  NON --> Retour au
                      |       |                          rédacteur
                      |       |                       |
                      |       |                       v
                      |       |              [A5 Diffuser]
                      |       |              et mettre à
                      |       |              disposition
                      |       |              (FM-PS01-GD)
                      |       |                   |
                      |       |                   v
                      |       |              [A6 Archiver]
                      |       |              enregistrements
                      |       |              (durées de rétention)
                      |       |                   |
                      |       |                   v
                      |       +------------>[A7 Revue périodique]
                      |                     et destruction
                      |                     contrôlée
                      |
 ============================================================================
                      |
 PILOTES DE           |  [A2 Rédiger / Réviser]
 PROCESSUS            |  le document selon
                      |  modèles et codification
                      |  (MQ/PR/IT/FM/EN)
                      |       |
                      |       v
                      |  Soumettre pour
                      |  vérification (A3)
                      |
 ============================================================================
                      |
 RESPONSABLE          |  [A4 Approuver]
 QUALITÉ              |  Procédures (PR)
                      |  Vérifier conformité SMQ
                      |
 ============================================================================
                      |
 DIRECTION            |  [A4 Approuver]
                      |  Manuel Qualité (MQ)
                      |  Politique Qualité
                      |
 ============================================================================
```

---

## 8. Durées de rétention des enregistrements

| Type d'enregistrement               | Durée de rétention | Lieu de stockage       |
|--------------------------------------|--------------------|------------------------|
| Manuel Qualité (versions antérieures) | 5 ans             | Serveur documentaire   |
| Procédures (versions antérieures)    | 3 ans              | Serveur documentaire   |
| Rapports d'audit                     | 5 ans              | Serveur documentaire   |
| Fiches de non-conformité             | 5 ans              | Serveur documentaire   |
| Rapports d'inspection                | 5 ans              | Serveur documentaire   |
| Évaluations fournisseurs             | 3 ans              | Serveur documentaire   |
| Comptes rendus revue de direction    | 5 ans              | Serveur documentaire   |
| Enquêtes satisfaction client         | 3 ans              | Serveur documentaire   |
| Bons de commande                     | 5 ans              | Serveur documentaire   |
| Documents de transport               | 5 ans              | Serveur documentaire   |

---

## 9. Interactions avec les autres processus

| Processus              | Nature de l'interaction                                |
|------------------------|--------------------------------------------------------|
| PM01 - Leadership        | Documents stratégiques, revue de direction             |
| P01 - Commercial       | Offres, contrats, enquêtes satisfaction                |
| P02 - Achats           | AQF, évaluations fournisseurs, commandes               |
| P04 - Logistique       | Documents de transport, preuves de livraison           |
| P03 - Contrôle Qualité | Rapports d'inspection, NC, audits                      |

---

## 10. Indicateurs de performance (KPI)

| Indicateur                                | Formule / Méthode                              | Objectif       | Fréquence    |
|-------------------------------------------|------------------------------------------------|----------------|--------------|
| Taux de documents à jour                  | Documents à jour / Total documents x 100       | 100 %          | Trimestrielle |
| Délai moyen de traitement documentaire    | Somme délais (création à approbation) / Nombre | < 10 jours     | Trimestrielle |
| Taux de conformité documentaire           | Documents conformes / Documents vérifiés x 100 | 100 %          | Semestrielle |
| Nombre de documents obsolètes en circulation | Comptage                                     | 0              | Trimestrielle |
| Taux de réalisation de la revue annuelle  | Documents revus / Documents à revoir x 100     | 100 %          | Annuelle     |

---

## 11. Documents et enregistrements associés

| Code         | Intitulé                              | Type          |
|--------------|---------------------------------------|---------------|
| PR-PS01-GD     | Procédure Gestion Documentaire       | Procédure     |
| FM-PS01-GD     | Registre documentaire                 | Formulaire    |
| IT-PS01-COD    | Instruction de codification           | Instruction   |
| FM-PS01-DEM    | Demande de modification documentaire  | Formulaire    |

---

## 12. Amélioration continue

L'amélioration du processus de gestion documentaire s'appuie sur :
- La revue annuelle de la documentation
- Les constats d'audit relatifs à la documentation
- La simplification des modèles et procédures
- La digitalisation et l'automatisation des flux documentaires
- Les retours des utilisateurs du système documentaire

---

*Document contrôlé - Plus Sàrl - Système de Management de la Qualité ISO 9001:2015*
*Version v0.7 - 2026-03-04*
