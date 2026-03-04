# CH-BLOC-002 — Création Fiche de Commande

## Fiche Processus Chain — Bloc 2

| Élément | Détail |
|---------|--------|
| **Code** | CH-BLOC-002 |
| **Ligne** | 01 SALES |
| **Intitulé** | Création d'une Fiche de Commande |
| **Rôle pilote** | Rôle Commercial |
| **Processus parent** | P01 — Commercial |
| **Source** | PROCESS_CHAIN_PRODUIT_EXISTANT_260304.doc |

---

## Applicable aux types de commande

| Type | Applicable |
|------|-----------|
| 1. Commande produit existant | Oui |
| 2. Commande modification outillage | Oui |
| 3. Commande nouvel outillage | Oui |
| 4. Commande de sourcing | Oui |

---

## Données d'entrée

- Commande enregistrée (depuis BLOC 1)
- Fichier commande client (PDF)
- Catalogue produits (bibliothèque déroulante)

## Données de sortie

- Fiche de commande complète
- Commande PDF archivée sous l'onglet PDF
- Informations transmises vers BLOC 3 (Fiche de Transport) et BLOC 4 (Étude Technique)

---

## Actions détaillées

| # | Action | Description | Responsable | Document associé |
|---|--------|-------------|-------------|-----------------|
| 1 | Créer une nouvelle fiche de commande | Création d'une nouvelle fiche dans le système | 01 SALES | Fiche de commande |
| 2 | Ajouter la commande en PDF sous l'onglet PDF | Télécharger le fichier commande client au format PDF | 01 SALES | PDF commande |
| 3 | Ajouter le nom du client, la date et l'échéance | Renseigner les informations d'identification de la commande, inclure l'échéance s'il y en a une | 01 SALES | Fiche de commande |
| 4 | Sélectionner le nom du produit | Sélectionner le produit dans la bibliothèque déroulante | 01 SALES | Bibliothèque produits |
| 5 | Ajouter la quantité commandée | Ajouter la quantité commandée et la quantité finale (identique) | 01 SALES | Fiche de commande |
| 6 | Ajouter la référence de la commande | Référence identique à celle du client | 01 SALES | Fiche de commande |

---

## Critères de passage au bloc suivant

- Fiche de commande complète (client, date, échéance, produit, quantité, référence)
- PDF de la commande archivé
- Produit sélectionné dans la bibliothèque

---

## Interactions

| Vers | Nature |
|------|--------|
| BLOC 1 — Réception Commande | Retour si informations manquantes |
| BLOC 3 — Création Fiche de Transport | Transmission pour organiser le transport |
| BLOC 4 — Étude Technique Fournisseurs | Transmission pour étude technique |

---

*Réf. ISO 9001:2015 — §8.2.3, §8.1*
