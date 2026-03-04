# Chaîne Processus - CHAIN-01 : Commande Produit Existant

| **Document**       | CHAIN-01_Commande_Produit_Existant         |
|--------------------|---------------------------------------------|
| **Version**        | v0.7                                        |
| **Date**           | 2026-03-04                                  |
| **Classification** | Interne                                     |
| **Processus**      | Chaîne Processus - Réalisation              |
| **Rédaction**      | Rôle Qualité                                |
| **Approbation**    | Direction                                   |

---

## 1. Objet

Ce document décrit la chaîne processus complète pour le traitement d'une **commande de produit existant** chez Plus Sàrl. Il s'agit du flux standard applicable lorsqu'un client commande un produit déjà référencé, avec un fournisseur déjà évalué et un outillage existant.

---

## 2. Domaine d'application

Cette chaîne s'applique à toute commande client portant sur un produit existant dans le catalogue de Plus Sàrl, indépendamment de la localisation géographique du client ou du fournisseur.

---

## 3. Spécificités de la chaîne « Produit Existant »

| Caractéristique                  | Description                                                        |
|----------------------------------|--------------------------------------------------------------------|
| Phase de développement           | Aucune — produit déjà développé et validé                          |
| Évaluation fournisseur           | Déjà réalisée — fournisseur qualifié et référencé                  |
| Outillage                        | Existant — aucune création ni modification d'outillage nécessaire  |
| Délai de réalisation             | Le plus court parmi les 4 types de commandes                      |
| Inspection                       | Contrôle qualité standard selon les spécifications existantes      |

---

## 4. Lignes processus

La chaîne s'articule autour de **4 lignes processus** :

| Code | Ligne             | Rôle pilote          | Fonction principale                              |
|------|-------------------|----------------------|--------------------------------------------------|
| 01   | SALES             | Rôle Commercial      | Gestion commerciale, relation client, facturation |
| 02   | MANUFACTURE       | Rôle Achats          | Coordination fournisseurs, suivi de production    |
| 03   | DELIVERY          | Rôle Logistique      | Transport, livraison, douane                      |
| 04   | QUALITY           | Rôle Qualité         | Contrôle conformité, validation qualité           |

---

## 5. Vue d'ensemble des 8 blocs

```
BLOC 1          BLOC 2          BLOC 3          BLOC 4
Réception       Fiche de        Fiche de        Étude
commande        commande        transport       technique
[01 SALES]      [01 SALES]      [03 DELIVERY]   [02 MANUFACTURE]
    │               │               │               │
    ▼               ▼               ▼               ▼
BLOC 5          BLOC 6          BLOC 7          BLOC 8
Validation      Production      Livraison       Acceptation
commande        & Qualité       & Douane        marchandise
[01 SALES]      [02 MANUF.      [03 DELIVERY    [04 QUALITY
                 04 QUALITY]     01 SALES]        01 SALES]
```

---

## 6. Détail des blocs par ligne processus

### BLOC 1 — Réception d'une commande client

| Réf. détail | Ligne    | Actions                                                                                      |
|-------------|----------|----------------------------------------------------------------------------------------------|
| CH-BLOC-001 | 01 SALES | Télécharger et enregistrer la commande sur le bureau et dans le dossier ORDER_20XX sous la même nomenclature que le client |

### BLOC 2 — Création d'une fiche de commande

| Réf. détail | Ligne    | Actions                                                                                              |
|-------------|----------|------------------------------------------------------------------------------------------------------|
| CH-BLOC-002 | 01 SALES | 1. Création d'une nouvelle fiche de commande                                                         |
|             |          | 2. Ajout de la commande en PDF sous l'onglet PDF                                                     |
|             |          | 3. Téléchargement de la commande sous le fichier                                                     |
|             |          | 4. Ajouter le nom du client, la date et l'échéance s'il y en a une                                  |
|             |          | 5. Sélectionner le nom du produit dans la bibliothèque déroulante                                    |
|             |          | 6. Ajout de la quantité commandée et la quantité finale (identique)                                  |
|             |          | 7. Ajouter la référence de la commande, identique à celle du client                                 |

### BLOC 3 — Création d'une fiche de transport

| Réf. détail | Ligne       | Actions                                                                              |
|-------------|-------------|--------------------------------------------------------------------------------------|
| CH-BLOC-003 | 03 DELIVERY | 1. Création d'une fiche de transport ou ajout sur un transport existant               |
|             |             | 2. Validation des délais de livraison par le transporteur                             |
|             |             | 3. Définition du type de livraison                                                   |

### BLOC 4 — Étude technique avec les fournisseurs

| Réf. détail | Ligne          | Actions                                                                         |
|-------------|----------------|---------------------------------------------------------------------------------|
| CH-BLOC-004 | 02 MANUFACTURE | 1. Définir le statut de la commande (liste déroulante)                           |
|             |                | 2. Envoi des informations aux fournisseurs requis                                |
|             |                | 3. Validation des délais de production par les fournisseurs                      |

### BLOC 5 — Validation de commande

| Réf. détail | Ligne    | Actions                                                                                      |
|-------------|----------|----------------------------------------------------------------------------------------------|
| CH-BLOC-005 | 01 SALES | 1. Imprimer l'AR pour préparer à l'envoi pour valider avec le client                         |
|             |          | 2. Envoyer l'AR au client avec les détails de livraison et prix par produit                  |
|             |          | 3. Retour du client si nécessaire ou acceptation ou refus                                    |

### BLOC 6 — Production et qualité

| Réf. détail | Ligne          | Actions                                                                                         |
|-------------|----------------|-------------------------------------------------------------------------------------------------|
| CH-BLOC-006 | 02 MANUFACTURE | Envoyer la confirmation de production au fournisseur (e-mail ou messagerie)                      |
|             | 04 QUALITY     | Validation de la conformité des pièces par le fournisseur suite au contrôle qualité              |

### BLOC 7 — Livraison & Douane

| Réf. détail | Ligne       | Actions                                                                                          |
|-------------|-------------|--------------------------------------------------------------------------------------------------|
| CH-BLOC-007 | 03 DELIVERY | 1. Création d'un bulletin de livraison                                                           |
|             | 01 SALES    | 2. Envoi de la facture commerciale au transporteur                                               |
|             | 03 DELIVERY | 3. Définition des spécificités s'il y en a au fournisseur (délai, jour de livraison, etc.)       |
|             | 03 DELIVERY | 4. Suivi de l'envoi jusqu'à la livraison avec le transporteur                                    |
|             | 03 DELIVERY | 5. Suivi douanier jusqu'à la livraison avec le transporteur et l'agent en douane                 |
|             | 01 SALES    | 6. Informer le client de la date de livraison validée par le transporteur                        |

### BLOC 8 — Acceptation de marchandise

| Réf. détail | Ligne      | Actions                                                                                    |
|-------------|------------|--------------------------------------------------------------------------------------------|
| CH-BLOC-008 | 04 QUALITY | 1. Mail de confirmation au client de la conformité de la marchandise                        |
|             | 01 SALES   | 2. Envoi de la facture au client                                                           |
|             | 01 SALES   | 3. Envoi de la déclaration douanière au client s'il y en a                                 |
|             | 01 SALES   | 4. Paiement du client                                                                     |
|             | 01 SALES   | 5. Clôture du dossier                                                                     |

---

## 7. Matrice de responsabilité (RACI)

| Bloc   | Rôle Commercial | Rôle Achats | Rôle Logistique | Rôle Qualité |
|--------|-----------------|-------------|-----------------|--------------|
| BLOC 1 | R/A             | I           | I               | I            |
| BLOC 2 | R/A             | I           | I               | I            |
| BLOC 3 | I               | I           | R/A             | I            |
| BLOC 4 | I               | R/A         | I               | C            |
| BLOC 5 | R/A             | C           | C               | I            |
| BLOC 6 | I               | R/A         | I               | R/A          |
| BLOC 7 | R               | I           | R/A             | I            |
| BLOC 8 | R               | I           | I               | R/A          |

**Légende** : R = Réalise, A = Approuve, C = Consulté, I = Informé

---

## 8. Indicateurs de performance (KPI)

| KPI                                    | Objectif                  | Fréquence de mesure | Responsable       |
|----------------------------------------|---------------------------|---------------------|--------------------|
| Délai moyen de traitement commande     | ≤ délai contractuel       | Mensuelle           | Rôle Commercial    |
| Taux de conformité des livraisons      | ≥ 95 %                   | Mensuelle           | Rôle Qualité       |
| Taux de réclamations clients           | ≤ 3 %                    | Mensuelle           | Rôle Commercial    |
| Respect des délais fournisseurs        | ≥ 90 %                   | Mensuelle           | Rôle Achats        |
| Taux de dossiers clôturés dans le délai| ≥ 90 %                   | Mensuelle           | Rôle Commercial    |
| Taux de conformité au contrôle qualité | ≥ 97 %                   | Par commande        | Rôle Qualité       |
| Délai moyen de livraison               | ≤ délai annoncé au client | Mensuelle           | Rôle Logistique    |

---

## 9. Documents associés

| Référence    | Document                                  |
|--------------|-------------------------------------------|
| CH-BLOC-001  | Fiche détail — Réception commande         |
| CH-BLOC-002  | Fiche détail — Fiche de commande          |
| CH-BLOC-003  | Fiche détail — Fiche de transport         |
| CH-BLOC-004  | Fiche détail — Étude technique            |
| CH-BLOC-005  | Fiche détail — Validation commande        |
| CH-BLOC-006  | Fiche détail — Production et qualité      |
| CH-BLOC-007  | Fiche détail — Livraison et douane        |
| CH-BLOC-008  | Fiche détail — Acceptation marchandise    |

---

## Références normatives

| Clause ISO 9001:2015 | Exigence                                                        |
|-----------------------|-----------------------------------------------------------------|
| 8.1                   | Planification et maîtrise opérationnelles                        |
| 8.2                   | Exigences relatives aux produits et services                     |
| 8.4                   | Maîtrise des processus, produits et services externalisés        |
| 8.5                   | Production et prestation de service                              |
| 8.5.2                 | Identification et traçabilité                                    |
| 8.6                   | Libération des produits et services                              |

---

*Document contrôlé - Toute copie imprimée est considérée comme non contrôlée.*
*Plus Sàrl - Système de Management de la Qualité ISO 9001:2015 - v0.7*
