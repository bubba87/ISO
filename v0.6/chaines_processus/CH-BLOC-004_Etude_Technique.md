# Fiche Détail Bloc - CH-BLOC-004 : Étude Technique avec les Fournisseurs

| **Document**       | CH-BLOC-004_Etude_Technique                   |
|--------------------|-----------------------------------------------|
| **Version**        | v0.6                                          |
| **Date**           | 2026-03-04                                    |
| **Classification** | Interne                                       |
| **Processus**      | Chaîne Processus - Réalisation                |
| **Chaîne réf.**    | CHAIN-01 — Commande Produit Existant          |
| **Rédaction**      | Rôle Qualité                                  |
| **Approbation**    | Direction                                     |

---

## 1. Objet

Cette fiche décrit les actions détaillées du **BLOC 4 — Étude technique avec les fournisseurs** dans le cadre de la chaîne processus de commande produit existant.

---

## 2. Ligne processus

| Code ligne | Ligne          | Rôle pilote   |
|------------|----------------|---------------|
| 02         | MANUFACTURE    | Rôle Achats   |

---

## 3. Entrées du bloc

| Élément                            | Provenance                     |
|------------------------------------|--------------------------------|
| Fiche de commande complète         | BLOC 2 — Fiche de commande    |
| Spécifications produit             | Bibliothèque produits          |
| Informations fournisseurs qualifiés| Panel fournisseurs             |

---

## 4. Actions détaillées

| N° | Action                                                                  | Responsable   | Outil / Support                  |
|----|-------------------------------------------------------------------------|---------------|----------------------------------|
| 1  | Définir le statut de la commande (liste déroulante)                     | Rôle Achats   | Système de gestion des commandes |
| 2  | Envoi des informations aux fournisseurs requis                          | Rôle Achats   | E-mail / messagerie              |
| 3  | Validation des délais de production par les fournisseurs                | Rôle Achats   | E-mail / messagerie              |

---

## 5. Statuts de commande

| Statut                  | Description                                                  |
|-------------------------|--------------------------------------------------------------|
| En attente              | Commande reçue, en attente de traitement fournisseur          |
| En cours                | Informations envoyées au fournisseur, en attente de retour    |
| Délais validés          | Fournisseur a confirmé les délais de production               |
| En production           | Production lancée chez le fournisseur                         |

---

## 6. Sorties du bloc

| Élément                              | Destination                      |
|--------------------------------------|----------------------------------|
| Statut de commande mis à jour        | BLOC 5 — Validation commande    |
| Délais de production validés         | BLOC 5 — Validation commande    |
| Confirmation fournisseur             | BLOC 6 — Production et qualité  |

---

## 7. Points de contrôle

| Contrôle                                     | Critère d'acceptation                              | Responsable   |
|----------------------------------------------|-----------------------------------------------------|---------------|
| Statut de commande correctement défini       | Statut cohérent avec l'avancement réel               | Rôle Achats   |
| Informations envoyées aux bons fournisseurs  | Fournisseurs correspondant au produit commandé       | Rôle Achats   |
| Délais de production confirmés               | Délais compatibles avec l'échéance client            | Rôle Achats   |

---

## 8. Documents associés

| Référence   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Chaîne Processus — Commande Produit Existant  |
| CH-BLOC-002 | Fiche détail — Fiche de commande             |
| CH-BLOC-005 | Fiche détail — Validation commande           |
| CH-BLOC-006 | Fiche détail — Production et qualité         |

---

## Références normatives

| Clause ISO 9001:2015 | Exigence                                              |
|-----------------------|-------------------------------------------------------|
| 8.4                   | Maîtrise des processus, produits et services externalisés |
| 8.4.3                 | Informations à l'attention des prestataires externes   |
| 8.1                   | Planification et maîtrise opérationnelles              |

---

*Document contrôlé - Toute copie imprimée est considérée comme non contrôlée.*
*Plus Sàrl - Système de Management de la Qualité ISO 9001:2015 - v0.6*
