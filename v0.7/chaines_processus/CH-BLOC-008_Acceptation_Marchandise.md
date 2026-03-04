# Fiche Détail Bloc - CH-BLOC-008 : Acceptation de Marchandise

| **Document**       | CH-BLOC-008_Acceptation_Marchandise           |
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

Cette fiche décrit les actions détaillées du **BLOC 8 — Acceptation de marchandise** dans le cadre de la chaîne processus de commande produit existant. Ce bloc implique deux lignes processus : QUALITY et SALES.

---

## 2. Lignes processus

| Code ligne | Ligne     | Rôle pilote     |
|------------|-----------|-----------------|
| 04         | QUALITY   | Rôle Qualité    |
| 01         | SALES     | Rôle Commercial |

---

## 3. Entrées du bloc

| Élément                            | Provenance                       |
|------------------------------------|----------------------------------|
| Marchandise livrée                 | BLOC 7 — Livraison & Douane     |
| Bulletin de livraison              | BLOC 7 — Livraison & Douane     |
| Preuve de livraison                | BLOC 7 — Livraison & Douane     |
| Rapport de contrôle qualité        | BLOC 6 — Production et qualité  |

---

## 4. Actions détaillées

| N° | Action                                                                          | Ligne      | Responsable     | Outil / Support                  |
|----|---------------------------------------------------------------------------------|------------|-----------------|----------------------------------|
| 1  | Mail de confirmation au client de la conformité de la marchandise               | 04 QUALITY | Rôle Qualité    | E-mail                           |
| 2  | Envoi de la facture au client                                                   | 01 SALES   | Rôle Commercial | E-mail / système de facturation  |
| 3  | Envoi de la déclaration douanière au client s'il y en a                         | 01 SALES   | Rôle Commercial | E-mail                           |
| 4  | Paiement du client                                                              | 01 SALES   | Rôle Commercial | Système comptable                |
| 5  | Clôture du dossier                                                              | 01 SALES   | Rôle Commercial | Système de gestion des commandes |

---

## 5. Documents transmis au client

| Document                         | Condition d'envoi             | Responsable     |
|----------------------------------|-------------------------------|-----------------|
| Mail de conformité               | Systématique                  | Rôle Qualité    |
| Facture                          | Systématique                  | Rôle Commercial |
| Déclaration douanière            | Si applicable (import/export) | Rôle Commercial |

---

## 6. Processus de clôture du dossier

| Étape                        | Description                                                  | Responsable     |
|------------------------------|--------------------------------------------------------------|-----------------|
| Confirmation de conformité   | Validation que la marchandise est conforme                    | Rôle Qualité    |
| Facturation                  | Émission et envoi de la facture au client                     | Rôle Commercial |
| Documents douaniers          | Envoi de la déclaration douanière si applicable               | Rôle Commercial |
| Encaissement                 | Suivi et confirmation du paiement client                      | Rôle Commercial |
| Clôture                      | Fermeture administrative du dossier de commande               | Rôle Commercial |

---

## 7. Sorties du bloc

| Élément                               | Destination          |
|---------------------------------------|----------------------|
| Confirmation de conformité envoyée    | Client               |
| Facture envoyée                       | Client               |
| Déclaration douanière envoyée         | Client (si applicable)|
| Paiement reçu                         | Comptabilité         |
| Dossier clôturé                       | Archivage            |

---

## 8. Points de contrôle

| Contrôle                                     | Critère d'acceptation                              | Responsable     |
|----------------------------------------------|-----------------------------------------------------|-----------------|
| Conformité confirmée au client               | Mail de confirmation envoyé                          | Rôle Qualité    |
| Facture envoyée                              | Facture conforme à la commande et aux prix convenus  | Rôle Commercial |
| Déclaration douanière transmise              | Document complet et conforme (si applicable)         | Rôle Commercial |
| Paiement reçu                                | Montant conforme à la facture, dans les délais       | Rôle Commercial |
| Dossier complet et clôturé                   | Tous les documents archivés, statut « clôturé »      | Rôle Commercial |

---

## 9. Documents associés

| Référence   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Chaîne Processus — Commande Produit Existant  |
| CH-BLOC-006 | Fiche détail — Production et qualité         |
| CH-BLOC-007 | Fiche détail — Livraison et douane           |
| PR-P03-CQ   | Processus Contrôle Qualité                   |
| FM-P03-NC   | Fiche de Non-Conformité                      |
| FM-P01-SAT  | Enquête Satisfaction Client                  |

---

## Références normatives

| Clause ISO 9001:2015 | Exigence                                              |
|-----------------------|-------------------------------------------------------|
| 8.6                   | Libération des produits et services                    |
| 8.2.1                 | Communication avec les clients                         |
| 7.5                   | Informations documentées                               |
| 9.1.2                 | Satisfaction du client                                 |

---

*Document contrôlé - Toute copie imprimée est considérée comme non contrôlée.*
*Plus Sàrl - Système de Management de la Qualité ISO 9001:2015 - v0.7*
