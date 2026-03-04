# CH-BLOC-001 — Réception Commande

## Fiche Processus Chain — Bloc 1

| Élément | Détail |
|---------|--------|
| **Code** | CH-BLOC-001 |
| **Ligne** | 01 SALES |
| **Intitulé** | Réception d'une Commande Client |
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

- Commande client (email, téléphone, RFQ)
- Historique client (commandes précédentes)
- Référence produit existant (catalogue)

## Données de sortie

- Commande enregistrée dans le dossier ORDER_20XX
- Type de commande identifié (produit existant, modification outillage, nouvel outillage, sourcing)
- Transmission vers BLOC 2 (Création Fiche de Commande)

---

## Actions détaillées

| # | Action | Description | Responsable | Document associé |
|---|--------|-------------|-------------|-----------------|
| 1 | Charger et enregistrer la commande | Enregistrer la commande sur le bureau et dans le dossier ORDER_20XX sous la même nomenclature que le client | 01 SALES | Dossier ORDER_20XX |
| 2 | Identifier le type de commande | Déterminer s'il s'agit d'un produit existant, d'une modification d'outillage, d'un nouvel outillage ou de sourcing | 01 SALES | — |

---

## Critères de passage au bloc suivant

- Commande enregistrée dans ORDER_20XX
- Nomenclature client respectée
- Type de commande identifié

---

## Interactions

| Vers | Nature |
|------|--------|
| BLOC 2 — Création Fiche de Commande | Transfert du dossier commande |

---

*Réf. ISO 9001:2015 — §8.2.1, §8.2.2*
