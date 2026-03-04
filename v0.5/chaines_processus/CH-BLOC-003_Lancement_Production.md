# CH-BLOC-003 — Lancement Production

## Fiche Processus Chain — Bloc 3

| Élément | Détail |
|---------|--------|
| **Code** | CH-BLOC-003 |
| **Ligne** | 02 MANUFACTURE |
| **Intitulé** | Lancement de la Production Fournisseur |
| **Rôle pilote** | Rôle Achats |
| **Processus parent** | P02 — Achats & Sous-traitance |

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

- Bon de commande fournisseur validé (depuis BLOC 2)
- Spécifications techniques du produit
- Planning de production confirmé
- Exigences qualité (plan d'inspection)

## Données de sortie

- Production lancée chez le fournisseur
- Confirmation de démarrage
- Planning de production détaillé
- Demande d'inspection IPC transmise à BLOC 7

---

## Actions détaillées

| # | Action | Description | Responsable | Document associé |
|---|--------|-------------|-------------|-----------------|
| 1 | Émettre bon de commande fournisseur | Envoyer le PO officiel au fournisseur avec toutes les spécifications | Rôle Achats | Purchase Order (PO) |
| 2 | Confirmer planning production | Obtenir la confirmation du fournisseur sur les délais | Rôle Achats | Confirmation fournisseur |
| 3 | Vérifier capacité matières premières | S'assurer que le fournisseur dispose des matières premières nécessaires | Rôle Achats | — |
| 4 | Démarrer production | Confirmer le lancement effectif de la production | Rôle Achats | Rapport de démarrage |

---

## Critères de passage au bloc suivant

- PO accepté par le fournisseur
- Matières premières disponibles
- Production effectivement démarrée
- IPC (inspection démarrage) planifiée

---

## Interactions

| Vers | Nature |
|------|--------|
| BLOC 2 — Revue & Planification | Retour si problème fournisseur |
| BLOC 4 — Suivi Production | Transmission du suivi de production |
| BLOC 7 — Contrôle Qualité | Déclenchement de l'inspection IPC |

---

*Réf. ISO 9001:2015 — §8.4.1, §8.4.2*
