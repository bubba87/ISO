# Fiche Détail Bloc - CH-BLOC-005 : Validation de Commande

| **Document**       | CH-BLOC-005_Validation_Commande               |
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

Cette fiche décrit les actions détaillées du **BLOC 5 — Validation de commande** dans le cadre de la chaîne processus de commande produit existant.

---

## 2. Ligne processus

| Code ligne | Ligne     | Rôle pilote     |
|------------|-----------|-----------------|
| 01         | SALES     | Rôle Commercial |

---

## 3. Entrées du bloc

| Élément                            | Provenance                        |
|------------------------------------|-----------------------------------|
| Fiche de commande complète         | BLOC 2 — Fiche de commande       |
| Délais de livraison validés        | BLOC 3 — Fiche de transport      |
| Délais de production validés       | BLOC 4 — Étude technique         |
| Prix par produit                   | Système de gestion commerciale    |

---

## 4. Actions détaillées

| N° | Action                                                                                          | Responsable     | Outil / Support                  |
|----|-------------------------------------------------------------------------------------------------|-----------------|----------------------------------|
| 1  | Imprimer l'accusé de réception (AR) pour préparer à l'envoi et valider avec le client           | Rôle Commercial | Système de gestion des commandes |
| 2  | Envoyer l'AR au client avec les détails de livraison et prix par produit                        | Rôle Commercial | E-mail                           |
| 3  | Retour du client si nécessaire : acceptation ou refus                                           | Rôle Commercial | E-mail / téléphone               |

---

## 5. Contenu de l'accusé de réception (AR)

| Élément                        | Description                                         |
|--------------------------------|-----------------------------------------------------|
| Référence commande             | Identique à la référence du client                   |
| Détail des produits            | Désignation, quantités commandées                    |
| Prix par produit               | Prix unitaire et montant total                       |
| Délais de livraison            | Date de livraison prévisionnelle validée             |
| Conditions de livraison        | Type de transport, incoterms                         |
| Conditions de paiement         | Modalités de paiement convenues                      |

---

## 6. Scénarios de retour client

| Retour client   | Action suivante                                                    |
|-----------------|--------------------------------------------------------------------|
| Acceptation     | Passage au BLOC 6 — Confirmation de production                    |
| Refus           | Analyse des motifs, ajustement de l'offre ou clôture du dossier   |
| Modification    | Mise à jour de la fiche de commande, nouvel AR si nécessaire      |

---

## 7. Sorties du bloc

| Élément                               | Destination                      |
|---------------------------------------|----------------------------------|
| AR envoyé et validé par le client     | BLOC 6 — Production et qualité  |
| Commande confirmée                    | BLOC 6 — Production et qualité  |
| Dossier clôturé (en cas de refus)     | Archivage                        |

---

## 8. Points de contrôle

| Contrôle                                   | Critère d'acceptation                                 | Responsable     |
|--------------------------------------------|-------------------------------------------------------|-----------------|
| AR complet et conforme                     | Tous les éléments requis présents                      | Rôle Commercial |
| Prix et délais cohérents                   | Conformes aux validations des BLOCS 3 et 4             | Rôle Commercial |
| Retour client enregistré                   | Réponse formelle du client (acceptation/refus/modif.)  | Rôle Commercial |

---

## 9. Documents associés

| Référence   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Chaîne Processus — Commande Produit Existant  |
| CH-BLOC-003 | Fiche détail — Fiche de transport            |
| CH-BLOC-004 | Fiche détail — Étude technique               |
| CH-BLOC-006 | Fiche détail — Production et qualité         |

---

## Références normatives

| Clause ISO 9001:2015 | Exigence                                              |
|-----------------------|-------------------------------------------------------|
| 8.2.3                 | Revue des exigences relatives aux produits             |
| 8.2.1                 | Communication avec les clients                         |

---

*Document contrôlé - Toute copie imprimée est considérée comme non contrôlée.*
*Plus Sàrl - Système de Management de la Qualité ISO 9001:2015 - v0.6*
