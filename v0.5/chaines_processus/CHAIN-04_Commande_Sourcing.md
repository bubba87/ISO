# CHAIN-04 — Commande de Sourcing

## Chaîne Processus Complète

| Élément | Détail |
|---------|--------|
| **Code** | CHAIN-04 |
| **Type de commande** | Sourcing (recherche de fournisseur / produit) |
| **Statut** | À compléter |
| **Diagramme** | [chaine_processus_general.drawio](../diagrammes/chaine_processus_general.drawio) |

---

## Description

Cette chaîne processus couvre le flux complet d'une **commande de sourcing** — lorsqu'un client recherche un nouveau fournisseur ou un nouveau produit qui n'est pas encore dans le portefeuille. Cela inclut la recherche, l'évaluation et la qualification de nouveaux partenaires industriels.

---

## Flux des 8 Blocs

```
CLIENT  ──→  [BLOC 1] ──→ [BLOC 2] ──→ [BLOC 3] ──→ [BLOC 4] ──→ [BLOC 5] ──→ [BLOC 6] ──→  CLIENT
              Réception    Revue &      Lancement    Suivi         Préparation   Suivi          Produit
              Demande      Sourcing &   Production   Production    Expédition    Livraison      Sourcé
              Sourcing     Qualification 1er lot     1er lot            ↑          & Livré
                                            │            │              │
                                            └──→ [BLOC 7] ─────────────┘
                                                 Contrôle Qualité
                                                       │
                                                 [BLOC 8]
                                                 Clôture & Feedback
```

---

## Spécificités « Sourcing »

- **Phase de recherche fournisseur** : identification, benchmark, audit fournisseur potentiel (BLOC 2 fortement étendu)
- **Qualification fournisseur** : évaluation initiale, visite usine, AQF (Accord Qualité Fournisseur)
- **Échantillonnage** : commande d'échantillons avant première commande série
- **Délai le plus long** : processus complet de qualification pouvant prendre plusieurs mois
- **Risque maximal** : fournisseur non encore éprouvé, inspections renforcées

---

## Détail par bloc

> *Les fiches détaillées spécifiques à ce type de commande seront complétées ultérieurement.*
> *En attendant, les fiches génériques CH-BLOC-001 à CH-BLOC-008 s'appliquent avec les adaptations ci-dessus.*

| Bloc | Fiche générique | Adaptation requise |
|------|----------------|-------------------|
| BLOC 1 | [CH-BLOC-001](CH-BLOC-001_Reception_Commande.md) | Réception cahier des charges sourcing |
| BLOC 2 | [CH-BLOC-002](CH-BLOC-002_Revue_Planification.md) | Recherche fournisseurs, audit, qualification, AQF |
| BLOC 3 | [CH-BLOC-003](CH-BLOC-003_Lancement_Production.md) | Commande échantillons / première série |
| BLOC 4 | [CH-BLOC-004](CH-BLOC-004_Suivi_Production.md) | Suivi rapproché première production |
| BLOC 5 | [CH-BLOC-005](CH-BLOC-005_Preparation_Expedition.md) | Standard |
| BLOC 6 | [CH-BLOC-006](CH-BLOC-006_Suivi_Livraison.md) | Standard |
| BLOC 7 | [CH-BLOC-007](CH-BLOC-007_Controle_Qualite.md) | Inspections renforcées (nouveau fournisseur) |
| BLOC 8 | [CH-BLOC-008](CH-BLOC-008_Cloture_Feedback.md) | Évaluation initiale fournisseur + décision qualification |

---

*Réf. ISO 9001:2015 — §8.1, §8.2, §8.4.1, §8.4.2*
