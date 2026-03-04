# CH-BLOC-001 — Réception Commande

## Fiche Processus Chain — Bloc 1

| Élément | Détail |
|---------|--------|
| **Code** | CH-BLOC-001 |
| **Ligne** | 01 SALES |
| **Intitulé** | Réception & Enregistrement de la Commande |
| **Rôle pilote** | Rôle Commercial |
| **Processus parent** | P01 — Commercial |

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

- Demande client (email, téléphone, RFQ)
- Cahier des charges / spécifications produit
- Historique client (commandes précédentes)
- Référence produit existant (catalogue)

## Données de sortie

- Commande enregistrée dans le système
- Confirmation de réception au client
- Dossier commande initié
- Transmission vers BLOC 2 (Revue & Planification)

---

## Actions détaillées

| # | Action | Description | Responsable | Document associé |
|---|--------|-------------|-------------|-----------------|
| 1 | Réceptionner la commande client | Recevoir et enregistrer la demande (email, WeChat, téléphone) | Rôle Commercial | — |
| 2 | Vérifier références produit existant | Confirmer que le produit existe dans le catalogue / historique fournisseur | Rôle Commercial | Catalogue produits |
| 3 | Confirmer prix, délai, quantité | Vérifier les conditions commerciales avec le fournisseur si nécessaire | Rôle Commercial | Grille tarifaire |
| 4 | Émettre confirmation de commande | Envoyer l'accusé de réception et la confirmation formelle au client | Rôle Commercial | Confirmation de commande |

---

## Critères de passage au bloc suivant

- Commande enregistrée et numérotée
- Références produit validées
- Conditions commerciales confirmées
- Client informé de la prise en charge

---

## Interactions

| Vers | Nature |
|------|--------|
| BLOC 2 — Revue & Planification | Transfert du dossier commande pour revue de faisabilité |
| BLOC 7 — Contrôle Qualité | Transmission des exigences qualité spécifiques au client |

---

*Réf. ISO 9001:2015 — §8.2.1, §8.2.2*
