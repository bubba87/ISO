# CH-BLOC-008 — Acceptation de Marchandise

## Fiche Processus Chain — Bloc 8

| Élément | Détail |
|---------|--------|
| **Code** | CH-BLOC-008 |
| **Ligne** | 04 QUALITY + 01 SALES |
| **Intitulé** | Acceptation de Marchandise & Clôture |
| **Rôle pilote** | Rôle Qualité + Rôle Commercial |
| **Processus parent** | P04 — Contrôle Qualité / P01 — Commercial |
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

- Marchandise livrée au client (depuis BLOC 7)
- Résultats contrôle qualité (depuis BLOC 6)
- Documents de livraison et douane

## Données de sortie

- Mail de confirmation de conformité au client
- Facture envoyée au client
- Déclaration douanière transmise (si applicable)
- Paiement client reçu
- Dossier clôturé

---

## Actions détaillées

| # | Action | Description | Responsable | Document associé |
|---|--------|-------------|-------------|-----------------|
| 1 | Mail de confirmation de conformité au client | Envoyer la confirmation de conformité de la marchandise au client | 04 QUALITY | Email de conformité |
| 2 | Envoi de la facture au client | Émettre et envoyer la facture finale au client | 01 SALES | Facture client |
| 3 | Envoi de la déclaration douanière au client | Transmettre la déclaration douanière au client s'il y en a une | 01 SALES | Déclaration douanière |
| 4 | Paiement du client | Suivre et enregistrer le paiement du client | 01 SALES | Suivi paiement |
| 5 | Clôture du dossier | Fermer le dossier commande et archiver l'ensemble des documents | 01 SALES | Dossier clôturé |

---

## Critères de clôture

- Conformité confirmée au client
- Facture envoyée et paiement reçu
- Déclaration douanière transmise (si applicable)
- Dossier commande clôturé et archivé

---

## Interactions

| Vers | Nature |
|------|--------|
| BLOC 7 — Livraison & Douane | Réception confirmation de livraison |
| BLOC 6 — Production & Qualité | Réception des résultats qualité |
| M1 — Leadership | Données pour la revue de direction |

---

*Réf. ISO 9001:2015 — §8.6, §10.2, §10.3, §9.1*
