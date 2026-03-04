# CH-BLOC-004 — Étude Technique Fournisseurs

## Fiche Processus Chain — Bloc 4

| Élément | Détail |
|---------|--------|
| **Code** | CH-BLOC-004 |
| **Ligne** | 02 MANUFACTURE |
| **Intitulé** | Étude Technique avec les Fournisseurs |
| **Rôle pilote** | Rôle Achats |
| **Processus parent** | P02 — Achats & Sous-traitance |
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

- Fiche de commande (depuis BLOC 2)
- Spécifications techniques du produit
- Liste des fournisseurs qualifiés

## Données de sortie

- Statut de la commande défini
- Informations transmises aux fournisseurs
- Délais de production validés par les fournisseurs

---

## Actions détaillées

| # | Action | Description | Responsable | Document associé |
|---|--------|-------------|-------------|-----------------|
| 1 | Définir le statut de la commande | Sélectionner le statut dans la liste déroulante | 02 MANUFACTURE | Fiche de commande |
| 2 | Envoyer les informations aux fournisseurs requis | Transmettre les spécifications et la commande aux fournisseurs concernés | 02 MANUFACTURE | Email / WeChat |
| 3 | Valider les délais de production par les fournisseurs | Obtenir la confirmation des délais de fabrication | 02 MANUFACTURE | Confirmation fournisseur |

---

## Critères de passage au bloc suivant

- Statut commande défini
- Fournisseurs informés et confirmés
- Délais de production validés

---

## Interactions

| Vers | Nature |
|------|--------|
| BLOC 2 — Fiche de Commande | Réception des informations commande |
| BLOC 5 — Validation Commande | Transmission des délais pour préparer l'AR client |
| BLOC 6 — Production & Qualité | Lancement de la production |

---

*Réf. ISO 9001:2015 — §8.4.1, §8.4.2, §8.4.3*
