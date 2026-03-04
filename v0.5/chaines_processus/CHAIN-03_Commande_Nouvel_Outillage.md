# CHAIN-03 — Commande Nouvel Outillage

## Chaîne Processus Complète

| Élément | Détail |
|---------|--------|
| **Code** | CHAIN-03 |
| **Type de commande** | Création d'un nouvel outillage |
| **Statut** | À compléter |
| **Diagramme** | [chaine_processus_general.drawio](../diagrammes/chaine_processus_general.drawio) |

---

## Description

Cette chaîne processus couvre le flux complet d'une **commande de nouvel outillage** — lorsqu'un client a besoin de la création d'un moule, d'une matrice ou d'un gabarit entièrement nouveau pour une nouvelle production.

---

## Flux des 8 Blocs

```
CLIENT  ──→  [BLOC 1] ──→ [BLOC 2] ──→ [BLOC 3] ──→ [BLOC 4] ──→ [BLOC 5] ──→ [BLOC 6] ──→  CLIENT
              Réception    Revue &      Lancement    Suivi         Préparation   Suivi          Nouvel
              Commande     Planif.      Fabrication  Fabrication   Expédition    Livraison      Outillage
                                            │            │              ↑
                                            └──→ [BLOC 7] ─────────────┘
                                                 Contrôle Qualité
                                                       │
                                                 [BLOC 8]
                                                 Clôture & Feedback
```

---

## Spécificités « Nouvel Outillage »

- **Phase de conception** : étude technique complète, plans, simulations (BLOC 2 significativement étendu)
- **Sélection fournisseur spécialisé** : qualification potentielle d'un nouveau fournisseur outillage
- **Échantillonnage et validation** : T0, T1 samples avant approbation définitive
- **Délai plus long** : processus significativement plus long que produit existant
- **Inspections spécifiques outillage** : contrôle dimensionnel outillage + pièces d'essai

---

## Détail par bloc

> *Les fiches détaillées spécifiques à ce type de commande seront complétées ultérieurement.*
> *En attendant, les fiches génériques CH-BLOC-001 à CH-BLOC-008 s'appliquent avec les adaptations ci-dessus.*

| Bloc | Fiche générique | Adaptation requise |
|------|----------------|-------------------|
| BLOC 1 | [CH-BLOC-001](CH-BLOC-001_Reception_Commande.md) | Inclure cahier des charges technique complet |
| BLOC 2 | [CH-BLOC-002](CH-BLOC-002_Revue_Planification.md) | Conception outillage, sélection fournisseur spécialisé |
| BLOC 3 | [CH-BLOC-003](CH-BLOC-003_Lancement_Production.md) | Lancement fabrication outillage |
| BLOC 4 | [CH-BLOC-004](CH-BLOC-004_Suivi_Production.md) | Suivi fabrication outillage + samples T0/T1 |
| BLOC 5 | [CH-BLOC-005](CH-BLOC-005_Preparation_Expedition.md) | Emballage spécifique outillage |
| BLOC 6 | [CH-BLOC-006](CH-BLOC-006_Suivi_Livraison.md) | Standard |
| BLOC 7 | [CH-BLOC-007](CH-BLOC-007_Controle_Qualite.md) | Contrôle dimensionnel outillage + validation pièces |
| BLOC 8 | [CH-BLOC-008](CH-BLOC-008_Cloture_Feedback.md) | Validation et homologation outillage |

---

*Réf. ISO 9001:2015 — §8.1, §8.2, §8.4, §8.5.1*
