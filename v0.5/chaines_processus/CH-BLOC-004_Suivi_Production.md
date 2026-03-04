# CH-BLOC-004 — Suivi Production

## Fiche Processus Chain — Bloc 4

| Élément | Détail |
|---------|--------|
| **Code** | CH-BLOC-004 |
| **Ligne** | 02 MANUFACTURE |
| **Intitulé** | Suivi de la Production & Coordination |
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

- Production en cours (depuis BLOC 3)
- Rapports d'inspection IPC / DUPRO (depuis BLOC 7)
- Planning de livraison prévisionnel
- Communications fournisseur

## Données de sortie

- Rapports d'avancement production
- Alerte en cas de retard ou problème
- Confirmation de fin de production
- Déclenchement inspection PSI (via BLOC 7)

---

## Actions détaillées

| # | Action | Description | Responsable | Document associé |
|---|--------|-------------|-------------|-----------------|
| 1 | Suivre avancement production | Points réguliers avec le fournisseur (WeChat, email, visites) | Rôle Achats | Rapport d'avancement |
| 2 | Rapporter statut au client | Informer le client de l'état d'avancement et des délais | Rôle Commercial | Email / rapport client |
| 3 | Gérer aléas & retards production | Identifier et résoudre les problèmes (qualité, retard, capacité) | Rôle Achats | Fiche action corrective |
| 4 | Valider fin de production | Confirmer que la production est terminée et prête pour inspection finale | Rôle Achats | Confirmation fin production |

---

## Critères de passage au bloc suivant

- Production terminée conformément aux spécifications
- Inspection DUPRO satisfaisante (si applicable)
- PSI planifiée ou réalisée
- Marchandise prête à l'expédition

---

## Interactions

| Vers | Nature |
|------|--------|
| BLOC 3 — Lancement Production | Retour si relance fournisseur nécessaire |
| BLOC 5 — Préparation Expédition | Transmission de la confirmation de production terminée |
| BLOC 7 — Contrôle Qualité | Déclenchement inspections DUPRO et PSI |
| BLOC 1 — Réception Commande | Retour info au client via Sales |

---

*Réf. ISO 9001:2015 — §8.4.2, §8.4.3*
