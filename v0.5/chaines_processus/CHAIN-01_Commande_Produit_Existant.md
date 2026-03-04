# CHAIN-01 — Commande Produit Existant

## Chaîne Processus Complète

| Élément | Détail |
|---------|--------|
| **Code** | CHAIN-01 |
| **Type de commande** | Produit existant (référence catalogue) |
| **Statut** | Active — Fiche détaillée |
| **Diagramme** | [chaine_processus_general.drawio](../diagrammes/chaine_processus_general.drawio) |

---

## Description

Cette chaîne processus couvre le flux complet d'une **commande de produit existant** — c'est-à-dire un produit dont les références, les spécifications et les fournisseurs sont déjà connus et validés. Il s'agit du cas le plus fréquent et le plus direct.

---

## Flux des 8 Blocs

```
CLIENT  ──→  [BLOC 1] ──→ [BLOC 2] ──→ [BLOC 3] ──→ [BLOC 4] ──→ [BLOC 5] ──→ [BLOC 6] ──→  CLIENT
              Réception    Revue &      Lancement    Suivi         Préparation   Suivi          Produit
              Commande     Planif.      Production   Production    Expédition    Livraison      Livré
                                            │            │              ↑
                                            └──→ [BLOC 7] ─────────────┘
                                                 Contrôle Qualité
                                                       │
                                                 [BLOC 8]
                                                 Clôture & Feedback ──→ Retour SALES
```

---

## Détail par Ligne

### 01 SALES

| Bloc | Fiche | Actions clés |
|------|-------|-------------|
| **BLOC 1** — Réception Commande | [CH-BLOC-001](CH-BLOC-001_Reception_Commande.md) | Réceptionner commande, vérifier références produit, confirmer prix/délai/quantité, émettre confirmation |
| **BLOC 2** — Revue & Planification | [CH-BLOC-002](CH-BLOC-002_Revue_Planification.md) | Revue de faisabilité, planifier délai production, transmettre au fournisseur, confirmer planning client |

### 02 MANUFACTURE

| Bloc | Fiche | Actions clés |
|------|-------|-------------|
| **BLOC 3** — Lancement Production | [CH-BLOC-003](CH-BLOC-003_Lancement_Production.md) | Émettre PO fournisseur, confirmer planning, vérifier matières premières, démarrer production |
| **BLOC 4** — Suivi Production | [CH-BLOC-004](CH-BLOC-004_Suivi_Production.md) | Suivre avancement, rapporter au client, gérer aléas, valider fin de production |

### 03 DELIVERY

| Bloc | Fiche | Actions clés |
|------|-------|-------------|
| **BLOC 5** — Préparation Expédition | [CH-BLOC-005](CH-BLOC-005_Preparation_Expedition.md) | Planifier expédition, sélectionner transporteur, préparer documents, loading check |
| **BLOC 6** — Suivi Livraison | [CH-BLOC-006](CH-BLOC-006_Suivi_Livraison.md) | Suivre transit, gérer dédouanement, confirmer réception client, archiver documents |

### 04 QUALITY

| Bloc | Fiche | Actions clés |
|------|-------|-------------|
| **BLOC 7** — Contrôle Qualité | [CH-BLOC-007](CH-BLOC-007_Controle_Qualite.md) | IPC, DUPRO, PSI, décision libération/refus |
| **BLOC 8** — Clôture & Feedback | [CH-BLOC-008](CH-BLOC-008_Cloture_Feedback.md) | Enregistrer rapport final, traiter NC, réévaluer fournisseur, clôturer dossier |

---

## Spécificités « Produit Existant »

- **Pas de phase de développement** : le produit est déjà qualifié
- **Fournisseur déjà évalué** : pas besoin de processus de qualification
- **Outillage existant** : pas de création ou modification d'outillage
- **Délai plus court** : le flux est le plus rapide des 4 types de commande
- **Inspection standard** : plan d'inspection basé sur l'historique

---

## Indicateurs de performance

| Indicateur | Cible | Fréquence |
|-----------|-------|-----------|
| Délai global commande → livraison | Selon produit | Par commande |
| Taux de conformité PSI | ≥ 95% | Trimestriel |
| Taux de livraison à temps | ≥ 90% | Trimestriel |
| Réclamations client | Tendance à la baisse | Trimestriel |

---

*Réf. ISO 9001:2015 — §8.1, §8.2, §8.4, §8.5, §8.6*
