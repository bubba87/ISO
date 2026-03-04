# P02 - Processus Achats et Sous-traitance

| **Processus**       | P02 - Achats et Sous-traitance                       |
|----------------------|------------------------------------------------------|
| **Type**            | Réalisation                                           |
| **Pilote**          | Rôle Achats                                           |
| **Version**         | v0.7                                                  |
| **Date**            | 2026-03-04                                            |
| **Référence**       | PR-P02-ACH                                            |
| **Norme ISO 9001**  | Chapitres 8.4, 8.6                                   |

---

## 1. Objet et domaine d'application

Ce processus décrit les activités d'achat et de sous-traitance de **Plus Sàrl** pour ses opérations internationales de monitoring industriel et de sourcing. Il couvre la sélection, la qualification et l'évaluation des fournisseurs à travers le monde, ainsi que la gestion des commandes et la réception des produits/services.

---

## 2. Références normatives

- ISO 9001:2015, Chapitres 8.4 (Maîtrise des processus, produits et services fournis par des prestataires externes), 8.6 (Libération des produits et services)
- Manuel Qualité Plus Sàrl (MQ-001)

---

## 3. Rôles et responsabilités

| Rôle                        | Responsabilités principales                                          |
|-----------------------------|----------------------------------------------------------------------|
| **Achats**                  | Sourcing, négociation, commandes, suivi fournisseurs                 |
| **Qualité**                 | Qualification fournisseurs, audits, suivi des non-conformités        |
| **Direction**               | Validation des fournisseurs stratégiques, budgets                    |
| **Logistique**              | Coordination des réceptions et transports internationaux             |
| **Fournisseur**             | Livraison conforme, respect de l'AQF, communication                 |

---

## 4. Données d'entrée et de sortie

### Données d'entrée
- Besoins d'achat issus du processus P01 (Commercial)
- Cahier des charges / spécifications techniques
- Panel fournisseurs existant
- Historique de performance fournisseurs
- Exigences réglementaires applicables par pays

### Données de sortie
- Bons de commande validés
- Accord Qualité Fournisseur (AQF) signé
- Évaluation fournisseur (FM-P02-EVAL)
- Panel fournisseurs mis à jour
- Produits/services réceptionnés conformes

---

## 5. Description des activités

### A1 - Identification du besoin d'achat

Le Rôle Achats réceptionne le besoin d'achat issu du processus P01 ou d'un besoin interne. Il vérifie la complétude des spécifications et identifie les sources d'approvisionnement potentielles à l'international.

### A2 - Recherche et présélection de fournisseurs

Le Rôle Achats identifie des fournisseurs potentiels sur les marchés internationaux, analyse leurs capacités et procède à une présélection sur la base de critères définis (capacité, certifications, localisation, références).

### A3 - Qualification des fournisseurs

Le Rôle Achats, en coordination avec le Rôle Qualité, procède à la qualification des fournisseurs présélectionnés : audit sur site ou à distance, vérification des certifications, évaluation des capacités de production, signature de l'Accord Qualité Fournisseur (FM-P02-AQF).

### A4 - Consultation et négociation

Le Rôle Achats lance les consultations auprès des fournisseurs qualifiés, compare les offres (prix, délais, conditions, Incoterms) et conduit les négociations.

### A5 - Passation de commande

Le Rôle Achats émet le bon de commande avec les spécifications complètes, les exigences qualité, les délais de livraison et les conditions logistiques (Incoterms, mode de transport).

### A6 - Suivi de commande et relances

Le Rôle Achats assure le suivi de l'exécution de la commande auprès du fournisseur, vérifie le respect des délais et déclenche les relances si nécessaire.

### A7 - Réception et contrôle

Le Rôle Achats coordonne avec le Rôle Logistique et le Rôle Qualité la réception des produits/services. Les contrôles définis par le processus P04 sont déclenchés (IPC, DUPRO, PSI, Loading Check selon le cas).

### A8 - Évaluation périodique des fournisseurs

Le Rôle Achats, en coordination avec le Rôle Qualité, procède à l'évaluation périodique des fournisseurs selon les critères pondérés définis dans FM-P02-EVAL. Les fournisseurs sont classés A/B/C et le panel est mis à jour.

---

## 6. Diagramme swimlane

```
 PROCESSUS P02 - ACHATS ET SOUS-TRAITANCE
 ============================================================================

 Rôle                 | Flux des activités
 ============================================================================
                      |
 ACHATS               |  [A1 Identifier]   [A2 Rechercher]   [A4 Consulter]
                      |  le besoin    --->  et présélec-  --> et négocier
                      |  d'achat            tionner            les offres
                      |      |              fournisseurs           |
                      |      |                   |                 v
                      |      |                   v           [A5 Passer]
                      |      |              [A3 Qualifier]   la commande
                      |      |              fournisseurs     (BC + specs)
                      |      |              (avec Qualité)        |
                      |      |                   |                 v
                      |      |                   v           [A6 Suivre]
                      |      |              Signer AQF       la commande
                      |      |              (FM-P02-AQF)     et relancer
                      |      |                                    |
                      |      |                                    v
                      |      |                              [A7 Réceptionner]
                      |      |                              et contrôler
                      |      |                                    |
                      |      |                                    v
                      |      +----------------------------->[A8 Évaluer]
                      |                                     les fournisseurs
                      |                                     (FM-P02-EVAL)
                      |                                     Classement A/B/C
                      |
 ============================================================================
                      |
 QUALITÉ              |  Participer à  ---> Auditer les  ---> Contrôler à
                      |  la qualification    fournisseurs      réception
                      |  (critères)          (sur site ou      (P04)
                      |                      à distance)
                      |
 ============================================================================
                      |
 DIRECTION            |  Valider les fournisseurs stratégiques
                      |  Approuver les budgets d'achat
                      |
 ============================================================================
                      |
 LOGISTIQUE           |  Coordonner le ---> Organiser la ---> Confirmer
                      |  transport          réception         la réception
                      |  international      des produits
                      |
 ============================================================================
                      |
 FOURNISSEUR          |  Répondre aux ---> Signer    ---> Livrer     ---> Traiter
                      |  consultations     l'AQF          conforme        les NC
                      |
 ============================================================================
```

---

## 7. Interactions avec les autres processus

| Processus              | Nature de l'interaction                                |
|------------------------|--------------------------------------------------------|
| PM01 - Leadership        | Validation stratégie achats, budgets                   |
| P01 - Commercial       | Réception des besoins clients, retour faisabilité      |
| P04 - Logistique       | Coordination transport et réception internationale     |
| P03 - Contrôle Qualité | Inspections à la source, contrôle réception            |
| PS01 - Gestion Documentaire | Archivage AQF, évaluations, commandes               |

---

## 8. Indicateurs de performance (KPI)

| Indicateur                                | Formule / Méthode                              | Objectif       | Fréquence    |
|-------------------------------------------|------------------------------------------------|----------------|--------------|
| Taux de conformité des livraisons         | Livraisons conformes / Total livraisons x 100  | >= 95 %        | Mensuelle    |
| Taux de respect des délais fournisseurs   | Livraisons à temps / Total livraisons x 100    | >= 90 %        | Mensuelle    |
| Nombre de fournisseurs qualifiés          | Comptage des fournisseurs classés A ou B       | Tendance hausse | Semestrielle |
| Taux de non-conformités fournisseurs      | NC fournisseurs / Total réceptions x 100       | < 5 %          | Mensuelle    |
| Délai moyen de traitement des commandes   | Somme des délais / Nombre de commandes         | < 5 jours      | Mensuelle    |
| Taux de réalisation des évaluations       | Évaluations réalisées / Évaluations planifiées | 100 %          | Annuelle     |

---

## 9. Documents et enregistrements associés

| Code         | Intitulé                              | Type          |
|--------------|---------------------------------------|---------------|
| PR-P02-ACH   | Procédure Achats et Sous-traitance   | Procédure     |
| FM-P02-AQF   | Accord Qualité Fournisseur           | Formulaire    |
| FM-P02-EVAL  | Évaluation Fournisseur               | Formulaire    |
| FM-P02-BC    | Bon de commande                       | Formulaire    |
| EN-P02-PAN   | Panel Fournisseurs                    | Enregistrement|

---

## 10. Amélioration continue

L'amélioration du processus achats s'appuie sur :
- L'analyse des évaluations fournisseurs et des tendances
- Le suivi des non-conformités d'origine fournisseur
- L'optimisation des délais et coûts d'approvisionnement
- La diversification géographique du panel fournisseurs
- Le retour d'expérience des inspections (P04)

---

*Document contrôlé - Plus Sàrl - Système de Management de la Qualité ISO 9001:2015*
*Version v0.7 - 2026-03-04*
