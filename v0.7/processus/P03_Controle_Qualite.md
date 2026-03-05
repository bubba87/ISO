# P03 - Processus Contrôle Qualité

| **Processus**       | P03 - Contrôle Qualité                               |
|----------------------|------------------------------------------------------|
| **Type**            | Réalisation                                           |
| **Pilote**          | Rôle Qualité                                          |
| **Version**         | v0.7                                                  |
| **Date**            | 2026-03-04                                            |
| **Référence**       | PR-P03-CQ                                             |
| **Norme ISO 9001**  | Chapitres 8.6, 9.1, 10.2                             |

---

## 1. Objet et domaine d'application

Ce processus décrit les activités de contrôle qualité de **Plus Sàrl** pour ses opérations internationales de monitoring industriel et de sourcing. Il couvre les quatre types d'inspection (IPC, DUPRO, PSI, Loading Check), la gestion des non-conformités, les audits fournisseurs et l'analyse des données qualité.

---

## 2. Références normatives

- ISO 9001:2015, Chapitres 8.6 (Libération des produits et services), 9.1 (Surveillance, mesure, analyse et évaluation), 10.2 (Non-conformité et actions correctives)
- Manuel Qualité Plus Sàrl (MQ-001)
- Normes produits et réglementations applicables

---

## 3. Rôles et responsabilités

| Rôle                        | Responsabilités principales                                          |
|-----------------------------|----------------------------------------------------------------------|
| **Qualité**                 | Planification inspections, exécution contrôles, gestion NC, reporting |
| **Achats**                  | Communication des exigences fournisseur, suivi des actions correctives |
| **Commercial**              | Transmission des exigences client, validation des critères           |
| **Direction**               | Arbitrage sur les NC critiques, validation des actions majeures      |
| **Fournisseur**             | Mise à disposition pour inspection, traitement des NC                |

---

## 4. Types d'inspection

| Type            | Nom complet                          | Moment                           | Objectif                                    |
|-----------------|--------------------------------------|----------------------------------|---------------------------------------------|
| **IPC**         | Initial Production Check             | Début de production              | Vérifier les matières premières, composants et paramètres de production |
| **DUPRO**       | During Production Check              | En cours de production (30-50 %) | Contrôler la qualité en cours, détecter les dérives |
| **PSI**         | Pre-Shipment Inspection              | Production terminée (100 %)      | Vérification finale avant expédition        |
| **Loading Check** | Contrôle au chargement             | Au moment du chargement          | Vérifier l'emballage, l'étiquetage et le chargement |

---

## 5. Données d'entrée et de sortie

### Données d'entrée
- Cahier des charges et spécifications client (P01)
- Bon de commande et exigences qualité (P02)
- Planning de production fournisseur
- Normes et réglementations applicables
- Critères d'acceptation définis (AQL, tolérances)

### Données de sortie
- Rapports d'inspection (IPC, DUPRO, PSI, Loading Check)
- Fiches de non-conformité (FM-P03-NC)
- Décision de libération / refus / tri
- Rapports d'audit fournisseur (FM-P03-AUD)
- Statistiques et tendances qualité

---

## 6. Description des activités

### A1 - Planification des inspections

Le Rôle Qualité définit le plan d'inspection en fonction de la commande, du fournisseur (historique, classification) et des exigences client. Il détermine le type, le moment et les critères d'inspection.

### A2 - Préparation des inspections

Le Rôle Qualité prépare les documents d'inspection : checklist basée sur les spécifications, plan d'échantillonnage (AQL), outils de mesure nécessaires, critères d'acceptation/refus.

### A3 - Exécution des inspections (IPC)

Le Rôle Qualité réalise l'Initial Production Check en début de production pour vérifier les matières premières, les composants, les paramètres de production et la compréhension des spécifications par le fournisseur.

### A4 - Exécution des inspections (DUPRO)

Le Rôle Qualité réalise le During Production Check à 30-50 % d'avancement pour contrôler la qualité des produits en cours, détecter les dérives et prendre des mesures correctives précoces.

### A5 - Exécution des inspections (PSI)

Le Rôle Qualité réalise la Pre-Shipment Inspection à 100 % de la production terminée. Inspection finale selon le plan d'échantillonnage AQL. Décision de libération, refus ou tri.

### A6 - Exécution des inspections (Loading Check)

Le Rôle Qualité réalise le Loading Check au moment du chargement pour vérifier l'emballage, le marquage, l'étiquetage, la quantité et les conditions de chargement.

### A7 - Gestion des non-conformités

Le Rôle Qualité identifie, enregistre et classifie les non-conformités selon 4 niveaux (cf. FM-P03-NC). Il conduit l'analyse des causes racines, définit les actions correctives et en assure le suivi.

### A8 - Audits fournisseurs

Le Rôle Qualité planifie et réalise les audits fournisseurs (sur site ou à distance) selon le programme annuel. Les résultats alimentent l'évaluation fournisseur (FM-P02-EVAL).

### A9 - Analyse des données et reporting qualité

Le Rôle Qualité compile et analyse les données qualité (taux de conformité, tendances NC, performance fournisseurs), produit les tableaux de bord et présente les résultats en revue de direction.

---

## 7. Diagramme swimlane

```
 PROCESSUS P03 - CONTRÔLE QUALITÉ
 ============================================================================

 Rôle                 | Flux des activités
 ============================================================================
                      |
 QUALITÉ              |  [A1 Planifier]    [A2 Préparer]
                      |  les inspections -> documents et
                      |  (type, moment,    checklists
                      |   critères)             |
                      |                         v
                      |      +------------------+------------------+
                      |      |                  |                  |
                      |      v                  v                  v
                      |  [A3 IPC]          [A4 DUPRO]        [A5 PSI]
                      |  Initial           During             Pre-Shipment
                      |  Production        Production         Inspection
                      |  Check             Check              (AQL)
                      |      |                  |                  |
                      |      v                  v                  v
                      |  Rapport IPC       Rapport DUPRO     Rapport PSI
                      |  OK / NC           OK / NC           PASS/FAIL/PENDING
                      |      |                  |                  |
                      |      +------------------+------------------+
                      |                         |
                      |                         v
                      |                    [A6 Loading Check]
                      |                    Emballage, marquage,
                      |                    chargement
                      |                         |
                      |          +--------------+---------------+
                      |          |              |               |
                      |          v              v               v
                      |     CONFORME      NON-CONFORME    [A8 Audits]
                      |     Libération    [A7 Gestion NC]  fournisseurs
                      |     (P03)         (FM-P03-NC)      (FM-P03-AUD)
                      |                        |               |
                      |                        v               v
                      |                   Analyse cause   Résultats -->
                      |                   racine -->      FM-P02-EVAL
                      |                   Action corrective
                      |                        |
                      |                        v
                      |              [A9 Analyser et reporter]
                      |              Tableaux de bord qualité
                      |              Revue de direction (PM01)
                      |
 ============================================================================
                      |
 ACHATS               |  Transmettre    ---> Suivre les  ---> Mettre à jour
                      |  les exigences       actions          le panel
                      |  fournisseur         correctives      fournisseurs
                      |                      fournisseurs
                      |
 ============================================================================
                      |
 COMMERCIAL           |  Transmettre les exigences client
                      |  Valider les critères d'acceptation
                      |  Communiquer les résultats au client
                      |
 ============================================================================
                      |
 DIRECTION            |  Arbitrer les NC critiques (Niveau 4)
                      |  Valider les actions majeures
                      |
 ============================================================================
                      |
 FOURNISSEUR          |  Mettre à       ---> Traiter    ---> Prouver
                      |  disposition         les NC          l'efficacité
                      |  pour inspection                     des corrections
                      |
 ============================================================================
```

---

## 8. Flux de gestion des non-conformités

```
  Détection NC
       |
       v
  Enregistrement (FM-P03-NC)
       |
       v
  Classification (4 niveaux)
  +--------------------------------------------------+
  | Niveau 1 : Mineure       - Défaut esthétique mineur  |
  | Niveau 2 : Significative - Non-respect spécification |
  | Niveau 3 : Majeure       - Impact conformité/SMQ     |
  | Niveau 4 : Critique      - Arrêt livraison immédiat  |
  +--------------------------------------------------+
       |
       v
  Décision immédiate
  (Accepter / Trier / Refuser / Arrêt immédiat)
       |
       v
  Analyse cause racine
  (5 Pourquoi, Ishikawa)
       |
       v
  Action corrective
       |
       v
  Vérification d'efficacité
       |
       v
  Clôture NC
```

---

## 9. Interactions avec les autres processus

| Processus              | Nature de l'interaction                                |
|------------------------|--------------------------------------------------------|
| PM01 - Leadership        | Reporting qualité, revue de direction, arbitrage NC    |
| P01 - Commercial       | Exigences client, critères d'acceptation, retour qualité |
| P02 - Achats           | Exigences fournisseur, évaluation, actions correctives |
| P04 - Logistique       | Loading Check, libération pour expédition              |
| PS01 - Gestion Documentaire | Archivage rapports, NC, audits                       |

---

## 10. Indicateurs de performance (KPI)

| Indicateur                                | Formule / Méthode                              | Objectif       | Fréquence    |
|-------------------------------------------|------------------------------------------------|----------------|--------------|
| Taux de conformité PSI (PASS)             | PSI PASS / Total PSI x 100                    | >= 90 %        | Mensuelle    |
| Taux de non-conformités détectées         | NC détectées / Total inspections x 100         | Tendance baisse | Mensuelle   |
| Délai moyen de clôture des NC             | Somme des délais clôture NC / Nombre NC        | < 15 jours     | Mensuelle    |
| Taux d'efficacité des actions correctives | AC efficaces / AC vérifiées x 100             | >= 85 %        | Trimestrielle |
| Taux de réalisation du plan d'inspection  | Inspections réalisées / Inspections planifiées | >= 95 %        | Mensuelle    |
| Taux de réalisation des audits fournisseurs | Audits réalisés / Audits planifiés x 100     | 100 %          | Annuelle     |
| Coût de non-qualité                       | Total coûts NC / Chiffre d'affaires x 100     | < 2 %          | Trimestrielle |

---

## 11. Documents et enregistrements associés

| Code         | Intitulé                              | Type          |
|--------------|---------------------------------------|---------------|
| PR-P03-CQ    | Procédure Contrôle Qualité           | Procédure     |
| FM-P03-NC    | Fiche de Non-Conformité              | Formulaire    |
| FM-P03-AUD   | Rapport d'Audit Interne             | Formulaire    |
| FM-P03-IPC   | Rapport IPC                           | Formulaire    |
| FM-P03-DUPRO | Rapport DUPRO                        | Formulaire    |
| FM-P03-PSI   | Rapport PSI                           | Formulaire    |
| FM-P03-LC    | Rapport Loading Check                 | Formulaire    |
| IT-P03-ECH   | Instruction échantillonnage AQL      | Instruction   |

---

## 12. Amélioration continue

L'amélioration du processus contrôle qualité s'appuie sur :
- L'analyse statistique des non-conformités et des tendances
- L'évaluation de l'efficacité des actions correctives
- L'optimisation des plans d'inspection selon la performance fournisseur
- La formation continue des inspecteurs
- Le benchmarking des meilleures pratiques du secteur

---

*Document contrôlé - Plus Sàrl - Système de Management de la Qualité ISO 9001:2015*
*Version v0.7 - 2026-03-04*
