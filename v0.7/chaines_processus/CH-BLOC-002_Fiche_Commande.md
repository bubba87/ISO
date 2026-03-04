# Fiche Détail Bloc - CH-BLOC-002 : Création d'une Fiche de Commande

| **Document**       | CH-BLOC-002_Fiche_Commande                    |
|--------------------|-----------------------------------------------|
| **Version**        | v0.7                                          |
| **Date**           | 2026-03-04                                    |
| **Classification** | Interne                                       |
| **Processus**      | Chaîne Processus - Réalisation                |
| **Chaîne réf.**    | CHAIN-01 — Commande Produit Existant          |
| **Rédaction**      | Rôle Qualité                                  |
| **Approbation**    | Direction                                     |

---

## 1. Objet

Cette fiche décrit les actions détaillées du **BLOC 2 — Création d'une fiche de commande** dans le cadre de la chaîne processus de commande produit existant.

---

## 2. Ligne processus

| Code ligne | Ligne     | Rôle pilote     |
|------------|-----------|-----------------|
| 01         | SALES     | Rôle Commercial |

---

## 3. Entrées du bloc

| Élément                            | Provenance                     |
|------------------------------------|--------------------------------|
| Commande client enregistrée        | BLOC 1 — Réception commande   |
| Fichier classé dans ORDER_20XX     | BLOC 1 — Réception commande   |
| Bibliothèque produits              | Système interne                |

---

## 4. Actions détaillées

| N° | Action                                                                                        | Responsable     | Outil / Support                  |
|----|-----------------------------------------------------------------------------------------------|-----------------|----------------------------------|
| 1  | Création d'une nouvelle fiche de commande                                                     | Rôle Commercial | Système de gestion des commandes |
| 2  | Ajout de la commande en PDF sous l'onglet PDF                                                 | Rôle Commercial | Système de gestion des commandes |
| 3  | Téléchargement de la commande sous le fichier                                                 | Rôle Commercial | Système de gestion des commandes |
| 4  | Ajouter le nom du client, la date et l'échéance s'il y en a une                              | Rôle Commercial | Système de gestion des commandes |
| 5  | Sélectionner le nom du produit dans la bibliothèque déroulante                                | Rôle Commercial | Bibliothèque produits            |
| 6  | Ajout de la quantité commandée et la quantité finale (identique)                              | Rôle Commercial | Système de gestion des commandes |
| 7  | Ajouter la référence de la commande, identique à celle du client                             | Rôle Commercial | Système de gestion des commandes |

---

## 5. Champs de la fiche de commande

| Champ                    | Description                                          | Obligatoire |
|--------------------------|------------------------------------------------------|-------------|
| Nom du client            | Raison sociale du client                             | Oui         |
| Date de commande         | Date de réception de la commande                     | Oui         |
| Échéance                 | Date de livraison souhaitée par le client             | Si applicable|
| Produit                  | Sélection dans la bibliothèque déroulante            | Oui         |
| Quantité commandée       | Nombre d'unités commandées                           | Oui         |
| Quantité finale          | Identique à la quantité commandée                    | Oui         |
| Référence commande       | Identique à la référence du client                   | Oui         |
| PDF de la commande       | Document original de la commande client              | Oui         |

---

## 6. Sorties du bloc

| Élément                          | Destination                      |
|----------------------------------|----------------------------------|
| Fiche de commande complète       | BLOC 3 — Fiche de transport     |
| Fiche de commande complète       | BLOC 4 — Étude technique        |
| Fiche de commande complète       | BLOC 5 — Validation commande    |

---

## 7. Points de contrôle

| Contrôle                                       | Critère d'acceptation                                | Responsable     |
|------------------------------------------------|------------------------------------------------------|-----------------|
| Tous les champs obligatoires renseignés        | Aucun champ obligatoire vide                          | Rôle Commercial |
| PDF de la commande attaché                     | Document lisible et complet                           | Rôle Commercial |
| Produit correctement sélectionné               | Correspondance avec la commande client                | Rôle Commercial |
| Référence commande conforme                    | Identique à la référence du client                    | Rôle Commercial |
| Quantités cohérentes                           | Quantité commandée = quantité finale                  | Rôle Commercial |

---

## 8. Documents associés

| Référence   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Chaîne Processus — Commande Produit Existant  |
| CH-BLOC-001 | Fiche détail — Réception commande            |
| CH-BLOC-003 | Fiche détail — Fiche de transport            |

---

## Références normatives

| Clause ISO 9001:2015 | Exigence                                              |
|-----------------------|-------------------------------------------------------|
| 8.2.2                 | Détermination des exigences relatives aux produits     |
| 8.2.3                 | Revue des exigences relatives aux produits             |
| 7.5                   | Informations documentées                               |

---

*Document contrôlé - Toute copie imprimée est considérée comme non contrôlée.*
*Plus Sàrl - Système de Management de la Qualité ISO 9001:2015 - v0.7*
