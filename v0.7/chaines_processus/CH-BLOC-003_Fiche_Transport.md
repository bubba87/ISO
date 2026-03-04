# Fiche Détail Bloc - CH-BLOC-003 : Création d'une Fiche de Transport

| **Document**       | CH-BLOC-003_Fiche_Transport                   |
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

Cette fiche décrit les actions détaillées du **BLOC 3 — Création d'une fiche de transport** dans le cadre de la chaîne processus de commande produit existant.

---

## 2. Ligne processus

| Code ligne | Ligne       | Rôle pilote       |
|------------|-------------|-------------------|
| 03         | DELIVERY    | Rôle Logistique   |

---

## 3. Entrées du bloc

| Élément                            | Provenance                     |
|------------------------------------|--------------------------------|
| Fiche de commande complète         | BLOC 2 — Fiche de commande    |
| Informations de livraison client   | BLOC 2 — Fiche de commande    |
| Délais souhaités par le client     | BLOC 2 — Fiche de commande    |

---

## 4. Actions détaillées

| N° | Action                                                                         | Responsable       | Outil / Support                  |
|----|--------------------------------------------------------------------------------|--------------------|----------------------------------|
| 1  | Création d'une fiche de transport ou ajout sur un transport existant            | Rôle Logistique   | Système de gestion des transports|
| 2  | Validation des délais de livraison par le transporteur                          | Rôle Logistique   | Communication transporteur       |
| 3  | Définition du type de livraison                                                | Rôle Logistique   | Système de gestion des transports|

---

## 5. Types de livraison

| Type de livraison       | Description                                              |
|-------------------------|----------------------------------------------------------|
| Transport maritime      | Pour les envois volumineux, délais plus longs             |
| Transport aérien        | Pour les envois urgents ou de faible volume               |
| Transport routier       | Pour les livraisons régionales ou continentales           |
| Transport ferroviaire   | Pour les envois intermédiaires volume/délai               |
| Transport express       | Pour les envois très urgents (courrier express)           |

---

## 6. Sorties du bloc

| Élément                             | Destination                         |
|-------------------------------------|-------------------------------------|
| Fiche de transport complète         | BLOC 5 — Validation commande       |
| Délais de livraison validés         | BLOC 5 — Validation commande       |
| Type de livraison défini            | BLOC 7 — Livraison & Douane        |

---

## 7. Points de contrôle

| Contrôle                                    | Critère d'acceptation                              | Responsable       |
|---------------------------------------------|----------------------------------------------------|--------------------|
| Fiche de transport créée ou mise à jour     | Toutes les informations requises renseignées        | Rôle Logistique   |
| Délais validés par le transporteur          | Délais compatibles avec l'échéance client           | Rôle Logistique   |
| Type de livraison approprié                 | Cohérent avec le volume, l'urgence et la destination| Rôle Logistique   |

---

## 8. Documents associés

| Référence   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Chaîne Processus — Commande Produit Existant  |
| CH-BLOC-002 | Fiche détail — Fiche de commande             |
| CH-BLOC-007 | Fiche détail — Livraison et douane           |

---

## Références normatives

| Clause ISO 9001:2015 | Exigence                                              |
|-----------------------|-------------------------------------------------------|
| 8.5.4                 | Préservation                                           |
| 8.1                   | Planification et maîtrise opérationnelles              |

---

*Document contrôlé - Toute copie imprimée est considérée comme non contrôlée.*
*Plus Sàrl - Système de Management de la Qualité ISO 9001:2015 - v0.7*
