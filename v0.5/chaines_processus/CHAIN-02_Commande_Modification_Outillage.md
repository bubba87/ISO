# CHAIN-02 — Commande Modification Outillage

## Chaîne Processus Complète

| Élément | Détail |
|---------|--------|
| **Code** | CHAIN-02 |
| **Type de commande** | Modification d'un outillage existant |
| **Statut** | À compléter |
| **Diagramme** | [chaine_processus_general.drawio](../diagrammes/chaine_processus_general.drawio) |

---

## Description

Cette chaîne processus couvre le flux complet d'une **commande de modification d'outillage** — lorsqu'un client demande une adaptation, correction ou amélioration d'un outillage (moule, gabarit, matrice) déjà existant chez un fournisseur.

---

## Flux des 8 Blocs

```
CLIENT  ──→  [BLOC 1] ──→ [BLOC 2] ──→ [BLOC 3] ──→ [BLOC 4] ──→ [BLOC 5] ──→ [BLOC 6] ──→  CLIENT
              Réception    Revue &      Lancement    Suivi         Préparation   Suivi          Outillage
              Commande     Planif.      Modification Modification  Expédition    Livraison      Modifié
                                            │            │              ↑
                                            └──→ [BLOC 7] ─────────────┘
                                                 Contrôle Qualité
                                                       │
                                                 [BLOC 8]
                                                 Clôture & Feedback
```

---

## Spécificités « Modification Outillage »

- **Phase d'étude technique** : analyse des modifications requises (BLOC 2 étendu)
- **Validation échantillons** : pièces d'essai après modification avant production série
- **Risque plus élevé** : impact potentiel sur les tolérances et la qualité
- **Inspections renforcées** : contrôle dimensionnel spécifique post-modification

---

## Détail par bloc

> *Les fiches détaillées spécifiques à ce type de commande seront complétées ultérieurement.*
> *En attendant, les fiches génériques CH-BLOC-001 à CH-BLOC-008 s'appliquent avec les adaptations ci-dessus.*

| Bloc | Fiche générique | Adaptation requise |
|------|----------------|-------------------|
| BLOC 1 | [CH-BLOC-001](CH-BLOC-001_Reception_Commande.md) | Inclure plan de modification technique |
| BLOC 2 | [CH-BLOC-002](CH-BLOC-002_Revue_Planification.md) | Étude technique + validation faisabilité modification |
| BLOC 3 | [CH-BLOC-003](CH-BLOC-003_Lancement_Production.md) | Lancement modification outillage chez le fournisseur |
| BLOC 4 | [CH-BLOC-004](CH-BLOC-004_Suivi_Production.md) | Suivi modification + échantillons d'essai |
| BLOC 5 | [CH-BLOC-005](CH-BLOC-005_Preparation_Expedition.md) | Standard |
| BLOC 6 | [CH-BLOC-006](CH-BLOC-006_Suivi_Livraison.md) | Standard |
| BLOC 7 | [CH-BLOC-007](CH-BLOC-007_Controle_Qualite.md) | Inspection dimensionnelle renforcée |
| BLOC 8 | [CH-BLOC-008](CH-BLOC-008_Cloture_Feedback.md) | Validation définitive modification outillage |

---

*Réf. ISO 9001:2015 — §8.1, §8.2, §8.4, §8.5.6*
