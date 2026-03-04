# CH-BLOC-007 — Livraison & Douane

## Fiche Processus Chain — Bloc 7

| Élément | Détail |
|---------|--------|
| **Code** | CH-BLOC-007 |
| **Ligne** | 03 DELIVERY + 01 SALES |
| **Intitulé** | Livraison & Douane |
| **Rôle pilote** | Rôle Logistique + Rôle Commercial |
| **Processus parent** | P03 — Logistique & Livraison / P01 — Commercial |
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

- Marchandise prête à l'expédition (depuis BLOC 6)
- Fiche de transport (depuis BLOC 3)
- Informations client (adresse de livraison, Incoterms)

## Données de sortie

- Bulletin de livraison émis
- Facture commerciale envoyée au transporteur
- Marchandise expédiée et suivie
- Client informé de la date de livraison

---

## Actions détaillées

| # | Action | Description | Responsable | Document associé |
|---|--------|-------------|-------------|-----------------|
| 1 | Créer un bulletin de livraison | Émettre le bulletin de livraison pour l'expédition | 03 DELIVERY | Bulletin de livraison (BL) |
| 2 | Envoyer la facture commerciale au transporteur | Transmettre la facture commerciale (CI) au transporteur | 01 SALES | Facture commerciale (CI) |
| 3 | Définir les spécificités au fournisseur | Communiquer les spécificités s'il y en a (délai, jour de livraison, etc.) | 03 DELIVERY | Instructions spéciales |
| 4 | Suivi de l'envoi jusqu'à la livraison | Assurer le suivi de l'expédition avec le transporteur jusqu'à la livraison | 03 DELIVERY | Tracking |
| 5 | Suivi douanier jusqu'à la livraison | Coordonner les formalités douanières avec le transporteur et l'agent en douane | 03 DELIVERY | Déclaration douanière |
| 6 | Informer le client de la date de livraison | Communiquer au client la date de livraison validée par le transporteur | 01 SALES | Email / confirmation |

---

## Critères de passage au bloc suivant

- Bulletin de livraison émis
- Marchandise expédiée
- Suivi transport et douane en cours
- Client informé de la date de livraison

---

## Interactions

| Vers | Nature |
|------|--------|
| BLOC 3 — Fiche de Transport | Réception des informations de transport planifiées |
| BLOC 6 — Production & Qualité | Réception marchandise prête à expédier |
| BLOC 8 — Acceptation Marchandise | Marchandise livrée, passage à l'acceptation |

---

*Réf. ISO 9001:2015 — §8.5.4, §8.6*
