# Fiche Détail Bloc - CH-BLOC-006 : Production et Qualité

| **Document**       | CH-BLOC-006_Production_Qualite                |
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

Cette fiche décrit les actions détaillées du **BLOC 6 — Production et qualité** dans le cadre de la chaîne processus de commande produit existant. Ce bloc implique deux lignes processus : MANUFACTURE et QUALITY.

---

## 2. Lignes processus

| Code ligne | Ligne          | Rôle pilote    |
|------------|----------------|----------------|
| 02         | MANUFACTURE    | Rôle Achats    |
| 04         | QUALITY        | Rôle Qualité   |

---

## 3. Entrées du bloc

| Élément                            | Provenance                      |
|------------------------------------|---------------------------------|
| Commande validée par le client     | BLOC 5 — Validation commande   |
| Spécifications produit             | Bibliothèque produits           |
| Informations fournisseur           | BLOC 4 — Étude technique       |

---

## 4. Actions détaillées

| N° | Action                                                                                                      | Ligne          | Responsable    | Outil / Support       |
|----|-------------------------------------------------------------------------------------------------------------|----------------|----------------|-----------------------|
| 1  | Envoyer la confirmation de production au fournisseur (e-mail ou messagerie)                                  | 02 MANUFACTURE | Rôle Achats    | E-mail / messagerie   |
| 2  | Validation de la conformité des pièces par le fournisseur suite au contrôle qualité                          | 04 QUALITY     | Rôle Qualité   | Rapport de contrôle   |

---

## 5. Processus de contrôle qualité

| Étape                        | Description                                                  | Responsable    |
|------------------------------|--------------------------------------------------------------|----------------|
| Contrôle fournisseur         | Le fournisseur réalise le contrôle qualité selon les spécifications | Fournisseur    |
| Rapport de contrôle          | Le fournisseur transmet le rapport de contrôle qualité        | Fournisseur    |
| Validation conformité        | Vérification du rapport et validation de la conformité        | Rôle Qualité   |
| Libération production        | Autorisation d'expédition si conformité validée               | Rôle Qualité   |

---

## 6. Sorties du bloc

| Élément                                | Destination                    |
|----------------------------------------|--------------------------------|
| Confirmation de production envoyée     | Fournisseur                    |
| Conformité des pièces validée          | BLOC 7 — Livraison & Douane   |
| Rapport de contrôle qualité            | Archivage qualité              |

---

## 7. Points de contrôle

| Contrôle                                          | Critère d'acceptation                            | Responsable    |
|---------------------------------------------------|--------------------------------------------------|----------------|
| Confirmation de production envoyée                | Accusé de réception du fournisseur                | Rôle Achats    |
| Rapport de contrôle qualité reçu                  | Rapport complet et conforme aux spécifications    | Rôle Qualité   |
| Conformité des pièces validée                     | Toutes les pièces conformes aux exigences         | Rôle Qualité   |

---

## 8. Documents associés

| Référence   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Chaîne Processus — Commande Produit Existant  |
| CH-BLOC-005 | Fiche détail — Validation commande           |
| CH-BLOC-007 | Fiche détail — Livraison et douane           |

---

## Références normatives

| Clause ISO 9001:2015 | Exigence                                              |
|-----------------------|-------------------------------------------------------|
| 8.4                   | Maîtrise des processus, produits et services externalisés |
| 8.5.1                 | Maîtrise de la production et de la prestation de service  |
| 8.6                   | Libération des produits et services                    |

---

*Document contrôlé - Toute copie imprimée est considérée comme non contrôlée.*
*Plus Sàrl - Système de Management de la Qualité ISO 9001:2015 - v0.6*
