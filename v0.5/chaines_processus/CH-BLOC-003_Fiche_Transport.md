# CH-BLOC-003 — Création Fiche de Transport

## Fiche Processus Chain — Bloc 3

| Élément | Détail |
|---------|--------|
| **Code** | CH-BLOC-003 |
| **Ligne** | 03 DELIVERY |
| **Intitulé** | Création d'une Fiche de Transport |
| **Rôle pilote** | Rôle Logistique |
| **Processus parent** | P03 — Logistique & Livraison |
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

- Fiche de commande validée (depuis BLOC 2)
- Exigences de livraison client
- Historique transporteurs

## Données de sortie

- Fiche de transport créée ou mise à jour
- Délais de livraison validés par le transporteur
- Type de livraison défini

---

## Actions détaillées

| # | Action | Description | Responsable | Document associé |
|---|--------|-------------|-------------|-----------------|
| 1 | Créer une fiche de transport ou ajouter sur un transport existant | Création d'une nouvelle fiche de transport ou ajout de la commande sur un transport déjà planifié | 03 DELIVERY | Fiche de transport |
| 2 | Valider les délais de livraison par le transporteur | Obtenir la confirmation des délais de livraison auprès du transporteur | 03 DELIVERY | Confirmation transporteur |
| 3 | Définir le type de livraison | Déterminer le mode de transport (maritime, aérien, routier, etc.) | 03 DELIVERY | Fiche de transport |

---

## Critères de passage au bloc suivant

- Fiche de transport créée et renseignée
- Délais de livraison confirmés par le transporteur
- Type de livraison défini

---

## Interactions

| Vers | Nature |
|------|--------|
| BLOC 2 — Fiche de Commande | Réception des informations commande |
| BLOC 7 — Livraison & Douane | Transmission des informations transport pour l'expédition |

---

*Réf. ISO 9001:2015 — §8.5.4*
