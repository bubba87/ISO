# Fiche Détail Bloc - CH-BLOC-007 : Livraison & Douane

| **Document**       | CH-BLOC-007_Livraison_Douane                  |
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

Cette fiche décrit les actions détaillées du **BLOC 7 — Livraison & Douane** dans le cadre de la chaîne processus de commande produit existant. Ce bloc implique deux lignes processus : DELIVERY et SALES.

---

## 2. Lignes processus

| Code ligne | Ligne       | Rôle pilote       |
|------------|-------------|-------------------|
| 03         | DELIVERY    | Rôle Logistique   |
| 01         | SALES       | Rôle Commercial   |

---

## 3. Entrées du bloc

| Élément                            | Provenance                        |
|------------------------------------|-----------------------------------|
| Conformité des pièces validée      | BLOC 6 — Production et qualité   |
| Fiche de transport                 | BLOC 3 — Fiche de transport      |
| Informations commerciales          | BLOC 2 — Fiche de commande       |

---

## 4. Actions détaillées

| N° | Action                                                                                             | Ligne       | Responsable       | Outil / Support                    |
|----|----------------------------------------------------------------------------------------------------|-------------|--------------------|------------------------------------|
| 1  | Création d'un bulletin de livraison                                                                | 03 DELIVERY | Rôle Logistique   | Système de gestion des transports  |
| 2  | Envoi de la facture commerciale au transporteur                                                    | 01 SALES    | Rôle Commercial   | E-mail                             |
| 3  | Définition des spécificités s'il y en a au fournisseur (délai, jour de livraison, etc.)            | 03 DELIVERY | Rôle Logistique   | E-mail / messagerie                |
| 4  | Suivi de l'envoi jusqu'à la livraison avec le transporteur                                         | 03 DELIVERY | Rôle Logistique   | Système de suivi / tracking        |
| 5  | Suivi douanier jusqu'à la livraison avec le transporteur et l'agent en douane                      | 03 DELIVERY | Rôle Logistique   | Communication agent en douane      |
| 6  | Informer le client de la date de livraison validée par le transporteur                             | 01 SALES    | Rôle Commercial   | E-mail                             |

---

## 5. Éléments du bulletin de livraison

| Élément                     | Description                                         |
|-----------------------------|-----------------------------------------------------|
| Référence commande          | Identique à la référence client                      |
| Désignation produit         | Description des produits livrés                      |
| Quantités                   | Nombre d'unités expédiées                            |
| Poids et dimensions         | Caractéristiques physiques du colis                  |
| Adresse de livraison        | Adresse complète du destinataire                     |
| Mode de transport           | Type de livraison défini au BLOC 3                   |
| Date d'expédition           | Date de départ effectif                              |
| Date de livraison prévue    | Date estimée d'arrivée                               |

---

## 6. Suivi douanier

| Étape                          | Description                                                    | Responsable       |
|--------------------------------|----------------------------------------------------------------|--------------------|
| Documents d'exportation        | Préparation des documents requis pour l'exportation             | Rôle Logistique   |
| Déclaration douanière          | Déclaration en douane au départ                                 | Agent en douane    |
| Suivi transit                  | Suivi du transit douanier international                         | Rôle Logistique   |
| Dédouanement à destination     | Coordination du dédouanement à l'arrivée                        | Agent en douane    |
| Confirmation livraison         | Validation de la réception par le destinataire                  | Rôle Logistique   |

---

## 7. Sorties du bloc

| Élément                                | Destination                          |
|----------------------------------------|--------------------------------------|
| Bulletin de livraison                  | BLOC 8 — Acceptation marchandise    |
| Facture commerciale transmise          | Transporteur / Agent en douane       |
| Date de livraison communiquée          | Client                               |
| Preuve de livraison                    | BLOC 8 — Acceptation marchandise    |

---

## 8. Points de contrôle

| Contrôle                                        | Critère d'acceptation                               | Responsable       |
|-------------------------------------------------|------------------------------------------------------|--------------------|
| Bulletin de livraison complet                   | Tous les éléments requis renseignés                   | Rôle Logistique   |
| Facture commerciale envoyée au transporteur     | Document conforme transmis avant expédition           | Rôle Commercial   |
| Suivi d'envoi actif                             | Numéro de tracking disponible et fonctionnel          | Rôle Logistique   |
| Dédouanement effectué                           | Aucun blocage douanier                                | Rôle Logistique   |
| Client informé de la date de livraison          | Communication envoyée avec date validée               | Rôle Commercial   |

---

## 9. Documents associés

| Référence   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Chaîne Processus — Commande Produit Existant  |
| CH-BLOC-003 | Fiche détail — Fiche de transport            |
| CH-BLOC-006 | Fiche détail — Production et qualité         |
| CH-BLOC-008 | Fiche détail — Acceptation marchandise       |

---

## Références normatives

| Clause ISO 9001:2015 | Exigence                                              |
|-----------------------|-------------------------------------------------------|
| 8.5.4                 | Préservation                                           |
| 8.5.2                 | Identification et traçabilité                          |
| 8.1                   | Planification et maîtrise opérationnelles              |

---

*Document contrôlé - Toute copie imprimée est considérée comme non contrôlée.*
*Plus Sàrl - Système de Management de la Qualité ISO 9001:2015 - v0.6*
