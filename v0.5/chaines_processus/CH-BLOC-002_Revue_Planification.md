# CH-BLOC-002 — Revue & Planification

## Fiche Processus Chain — Bloc 2

| Élément | Détail |
|---------|--------|
| **Code** | CH-BLOC-002 |
| **Ligne** | 01 SALES |
| **Intitulé** | Revue de Commande & Planification |
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

- Dossier commande (depuis BLOC 1)
- Capacité fournisseur confirmée
- Planning de production disponible
- Conditions de livraison requises

## Données de sortie

- Revue de commande validée
- Planning de production confirmé
- Bon de commande fournisseur préparé
- Planning communiqué au client

---

## Actions détaillées

| # | Action | Description | Responsable | Document associé |
|---|--------|-------------|-------------|-----------------|
| 1 | Revue de commande (faisabilité) | Vérifier la faisabilité technique, délai et coût avec le fournisseur | Rôle Commercial + Rôle Achats | Check-list revue commande |
| 2 | Planifier le délai de production | Définir le planning de fabrication en accord avec le fournisseur | Rôle Commercial | Planning production |
| 3 | Transmettre commande au fournisseur | Préparer et envoyer le bon de commande fournisseur | Rôle Achats | Bon de commande |
| 4 | Confirmer planning au client | Communiquer le délai de livraison prévisionnel au client | Rôle Commercial | Email / confirmation |

---

## Critères de passage au bloc suivant

- Revue de commande signée / validée
- Fournisseur confirmé et disponible
- Planning accepté par le client
- Bon de commande fournisseur émis

---

## Interactions

| Vers | Nature |
|------|--------|
| BLOC 1 — Réception Commande | Retour si revue non conforme |
| BLOC 3 — Lancement Production | Transmission du bon de commande fournisseur |
| BLOC 7 — Contrôle Qualité | Transmission du plan d'inspection requis |

---

*Réf. ISO 9001:2015 — §8.2.3, §8.1*
