# CH-BLOC-005 — Validation de Commande

## Fiche Processus Chain — Bloc 5

| Élément | Détail |
|---------|--------|
| **Code** | CH-BLOC-005 |
| **Ligne** | 01 SALES |
| **Intitulé** | Validation de la Commande avec le Client |
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

- Délais de production validés (depuis BLOC 4)
- Délais de livraison validés (depuis BLOC 3)
- Conditions commerciales (prix par produit)

## Données de sortie

- Accusé de réception (AR) envoyé au client
- Confirmation ou refus du client
- Commande validée pour lancement production

---

## Actions détaillées

| # | Action | Description | Responsable | Document associé |
|---|--------|-------------|-------------|-----------------|
| 1 | Imprimer l'AR pour préparer l'envoi | Préparer l'accusé de réception pour validation avec le client | 01 SALES | Accusé de réception (AR) |
| 2 | Envoyer l'AR au client avec les détails de livraison & prix par produit | Transmettre l'AR complet avec toutes les conditions commerciales et logistiques | 01 SALES | AR + détails livraison |
| 3 | Retour du client | Attendre la réponse du client : acceptation, demande de modification ou refus | 01 SALES | Email / confirmation client |

---

## Critères de passage au bloc suivant

- AR envoyé au client
- Réponse client obtenue
- **Si acceptation** : passage au BLOC 6 (Production)
- **Si modification nécessaire** : retour au BLOC 2 ou BLOC 4
- **Si refus** : clôture du dossier

---

## Interactions

| Vers | Nature |
|------|--------|
| BLOC 3 — Fiche de Transport | Réception des délais de livraison |
| BLOC 4 — Étude Technique | Réception des délais de production et prix |
| BLOC 6 — Production & Qualité | Lancement production après validation client |
| BLOC 2 — Fiche de Commande | Retour si modification nécessaire |

---

*Réf. ISO 9001:2015 — §8.2.3*
