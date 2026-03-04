# CH-BLOC-007 — Contrôle Qualité

## Fiche Processus Chain — Bloc 7

| Élément | Détail |
|---------|--------|
| **Code** | CH-BLOC-007 |
| **Ligne** | 04 QUALITY |
| **Intitulé** | Contrôle Qualité & Inspections |
| **Rôle pilote** | Rôle Qualité |
| **Processus parent** | P04 — Contrôle Qualité & Non-conformités |

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

- Exigences qualité client (depuis BLOC 1)
- Plan d'inspection (depuis BLOC 2)
- Demande d'inspection IPC (depuis BLOC 3)
- Demande d'inspection DUPRO / PSI (depuis BLOC 4)

## Données de sortie

- Rapport IPC (Initial Production Check)
- Rapport DUPRO (During Production)
- Rapport PSI (Pre-Shipment Inspection)
- Décision : Libération ou Refus d'expédition
- Fiche de non-conformité (si applicable)

---

## Actions détaillées

| # | Action | Description | Responsable | Document associé |
|---|--------|-------------|-------------|-----------------|
| 1 | IPC — Inspection démarrage production | Vérifier les échantillons de pré-production, matières premières, outillage | Rôle Qualité | Rapport IPC |
| 2 | DUPRO — Inspection en cours de production | Contrôler la qualité pendant la production (en cours de fabrication) | Rôle Qualité | Rapport DUPRO |
| 3 | PSI — Inspection avant expédition | Inspection finale sur produits finis, prêts à l'expédition | Rôle Qualité | Rapport PSI |
| 4 | Décision : Libérer / Refuser | Statuer sur la conformité : libérer l'expédition ou ouvrir une non-conformité | Rôle Qualité | Décision libération |

---

## Critères de passage au bloc suivant

- **Si conforme** : Libération d'expédition émise → BLOC 5
- **Si non conforme** : Fiche NC ouverte → BLOC 8 pour traitement

---

## Interactions

| Vers | Nature |
|------|--------|
| BLOC 3 — Lancement Production | Réception demande IPC |
| BLOC 4 — Suivi Production | Réception demande DUPRO / PSI |
| BLOC 5 — Préparation Expédition | Émission libération d'expédition |
| BLOC 8 — Clôture & Feedback | Transmission des non-conformités |

---

*Réf. ISO 9001:2015 — §8.6, §8.7, §10.2*
