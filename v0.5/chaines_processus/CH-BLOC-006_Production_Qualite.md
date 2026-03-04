# CH-BLOC-006 — Production & Qualité

## Fiche Processus Chain — Bloc 6

| Élément | Détail |
|---------|--------|
| **Code** | CH-BLOC-006 |
| **Ligne** | 02 MANUFACTURE + 04 QUALITY |
| **Intitulé** | Production et Contrôle Qualité |
| **Rôle pilote** | Rôle Achats + Rôle Qualité |
| **Processus parent** | P02 — Achats & Sous-traitance / P04 — Contrôle Qualité |
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

- Commande validée par le client (depuis BLOC 5)
- Spécifications techniques et exigences qualité
- Fournisseur confirmé (depuis BLOC 4)

## Données de sortie

- Confirmation de production envoyée au fournisseur
- Pièces produites et conformes
- Validation qualité par le fournisseur
- Marchandise prête pour livraison

---

## Actions détaillées

| # | Action | Description | Responsable | Document associé |
|---|--------|-------------|-------------|-----------------|
| 1 | Envoyer la confirmation de production au fournisseur | Confirmer le lancement de la production via WeChat ou email | 02 MANUFACTURE | Confirmation production |
| 2 | Validation de la conformité des pièces par le fournisseur | Le fournisseur effectue le contrôle qualité et valide la conformité des pièces produites | 04 QUALITY | Rapport contrôle qualité |

---

## Critères de passage au bloc suivant

- Production lancée et confirmée par le fournisseur
- Conformité des pièces validée
- Marchandise prête à l'expédition

---

## Interactions

| Vers | Nature |
|------|--------|
| BLOC 5 — Validation Commande | Réception de la commande validée |
| BLOC 7 — Livraison & Douane | Marchandise prête pour expédition |
| BLOC 8 — Acceptation Marchandise | Résultats qualité pour la confirmation finale |

---

*Réf. ISO 9001:2015 — §8.4.2, §8.4.3, §8.6*
