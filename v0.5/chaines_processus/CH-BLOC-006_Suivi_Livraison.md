# CH-BLOC-006 — Suivi Livraison

## Fiche Processus Chain — Bloc 6

| Élément | Détail |
|---------|--------|
| **Code** | CH-BLOC-006 |
| **Ligne** | 03 DELIVERY |
| **Intitulé** | Suivi Livraison & Confirmation |
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

- Expédition en cours (depuis BLOC 5)
- Numéro de tracking / BL
- Documents de transport
- Informations douanières

## Données de sortie

- Confirmation de livraison au client
- Preuve de livraison (POD)
- Documents de transport archivés
- Information de clôture vers BLOC 8

---

## Actions détaillées

| # | Action | Description | Responsable | Document associé |
|---|--------|-------------|-------------|-----------------|
| 1 | Suivre expédition en transit | Monitorer le transport en temps réel (tracking, contact transporteur) | Rôle Logistique | Tracking report |
| 2 | Gérer dédouanement & formalités | Coordonner les opérations douanières (export Chine, import destination) | Rôle Logistique | Déclaration douane |
| 3 | Confirmer réception chez le client | Obtenir la confirmation de bonne réception des marchandises | Rôle Logistique + Rôle Commercial | POD (Proof of Delivery) |
| 4 | Archiver documents de transport | Classer et archiver tous les documents liés au transport | Rôle Logistique | Dossier transport complet |

---

## Critères de passage au bloc suivant

- Marchandise livrée au client
- POD obtenu
- Aucune réclamation transport
- Documents archivés

---

## Interactions

| Vers | Nature |
|------|--------|
| BLOC 5 — Préparation Expédition | Retour si problème transport |
| BLOC 8 — Clôture & Feedback | Transmission de la confirmation de livraison |
| BLOC 1 — Réception Commande | Information au client via Sales |

---

*Réf. ISO 9001:2015 — §8.5.4, §8.6*
