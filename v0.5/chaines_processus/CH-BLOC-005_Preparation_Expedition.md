# CH-BLOC-005 — Préparation Expédition

## Fiche Processus Chain — Bloc 5

| Élément | Détail |
|---------|--------|
| **Code** | CH-BLOC-005 |
| **Ligne** | 03 DELIVERY |
| **Intitulé** | Préparation de l'Expédition |
| **Rôle pilote** | Rôle Logistique |
| **Processus parent** | P03 — Logistique & Livraison |

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

- Confirmation production terminée (depuis BLOC 4)
- Libération qualité (depuis BLOC 7)
- Exigences de livraison client (Incoterms, destination)
- Documents fournisseur (packing list, etc.)

## Données de sortie

- Planning d'expédition confirmé
- Transporteur sélectionné et réservé
- Documents de transport préparés (BL, CI, packing list, certificats)
- Chargement vérifié (loading check)

---

## Actions détaillées

| # | Action | Description | Responsable | Document associé |
|---|--------|-------------|-------------|-----------------|
| 1 | Planifier expédition | Définir la date d'expédition, le mode de transport et l'Incoterm | Rôle Logistique | Planning expédition |
| 2 | Sélectionner transporteur | Choisir le transporteur adapté (maritime, aérien, routier) et négocier le tarif | Rôle Logistique | Devis transport |
| 3 | Préparer documents (BL, douane, CI) | Établir les documents de transport, factures commerciales, certificats d'origine | Rôle Logistique | BL, CI, Packing List |
| 4 | Coordonner chargement (Loading) | Superviser ou faire superviser le chargement des marchandises | Rôle Logistique + Rôle Qualité | Loading check report |

---

## Critères de passage au bloc suivant

- Libération qualité obtenue (BLOC 7)
- Transporteur confirmé
- Tous les documents de transport prêts
- Chargement vérifié et conforme

---

## Interactions

| Vers | Nature |
|------|--------|
| BLOC 4 — Suivi Production | Réception info fin de production |
| BLOC 6 — Suivi Livraison | Transmission tracking et documents |
| BLOC 7 — Contrôle Qualité | Réception de la libération d'expédition |

---

*Réf. ISO 9001:2015 — §8.5.4, §8.6*
