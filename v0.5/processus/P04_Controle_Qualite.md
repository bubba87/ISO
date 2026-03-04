# P04 — Contrôle Qualité & Non-conformités

## Fiche Processus

| Élément | Détail |
|---------|--------|
| **Code** | P04 |
| **Type** | Opérationnel |
| **Rôle pilote** | Rôle Qualité |
| **Finalité** | Assurer la conformité des produits par les inspections, gérer les non-conformités, piloter l'amélioration continue |

---

## Données d'entrée

- Spécifications produit et exigences client (de P01)
- Informations de production (de P02)
- Critères d'acceptation définis dans l'AQF
- Réclamations clients
- Résultats d'audits précédents

## Données de sortie

- Rapports d'inspection (IPC, DUPRO, PSI)
- Autorisation ou refus d'expédition
- Fiches de non-conformité
- Actions correctives
- Rapports d'audit interne
- Indicateurs qualité pour la revue de direction

---

## Activités principales

| # | Activité | Rôle responsable | Documents associés |
|---|----------|-----------------|-------------------|
| 1 | Définir le plan d'inspection par commande | Rôle Qualité | Plan d'inspection |
| 2 | Réaliser les inspections (IPC, DUPRO, PSI) | Rôle Qualité | Rapports d'inspection |
| 3 | Décider de la libération ou du refus | Rôle Qualité | Autorisation d'expédition |
| 4 | Enregistrer et traiter les non-conformités | Rôle Qualité | DOC_Non_Conformite.md |
| 5 | Analyser les causes (5 Pourquoi, Ishikawa) | Rôle Qualité + Rôle Achats | Analyse des causes |
| 6 | Mettre en œuvre les actions correctives | Rôle Qualité | Plan d'actions |
| 7 | Vérifier l'efficacité des actions | Rôle Qualité | Suivi actions |
| 8 | Réaliser les audits internes | Rôle Qualité | DOC_Audit_Interne.md |
| 9 | Piloter l'amélioration continue | Rôle Qualité + Direction | MQ_10_Amelioration.md |

---

## Types d'inspection

| Type | Phase | Objectif | Taux d'échantillonnage |
|------|-------|----------|----------------------|
| IPC | Démarrage production | Valider matières, outillages, premiers articles | 100% premiers articles |
| DUPRO | En cours de production | Vérifier la qualité en série | Selon AQL ou plan |
| PSI | Avant expédition | Validation finale de la conformité | Selon AQL (niveau II) |
| Loading Check | Chargement | Conditionnement et chargement conforme | Visuel |

---

## Gestion des non-conformités

### Flux de traitement

1. Détection (inspection, réclamation client, audit)
2. Enregistrement (fiche NC)
3. Action immédiate (isolement, blocage)
4. Analyse des causes
5. Action corrective
6. Vérification d'efficacité
7. Clôture

### Classification

| Niveau | Impact | Délai traitement |
|--------|--------|-----------------|
| Critique | Sécurité / réglementaire | Immédiat |
| Majeure | Fonctionnel / client | ≤ 5 jours |
| Mineure | Esthétique / sans impact client | ≤ 15 jours |
| Observation | Amélioration potentielle | Prochaine revue |

---

## Interactions

| Processus | Nature de l'interaction |
|-----------|----------------------|
| M1 — Direction | Reporte les indicateurs qualité, résultats d'audit |
| P01 — Commercial | Reçoit les exigences client et réclamations |
| P02 — Achats | Coordonne les inspections chez les fournisseurs, traite les NC |
| P03 — Logistique | Autorise ou bloque l'expédition |
| S1 — Gestion Doc. | Enregistre et archive les documents qualité |

---

## Indicateurs

| Indicateur | Cible | Fréquence |
|-----------|-------|-----------|
| Taux de non-conformité | ≤ 5% | Trimestriel |
| Délai moyen de clôture NC | ≤ 10 jours | Trimestriel |
| Taux d'actions correctives efficaces | ≥ 90% | Semestriel |
| Audits internes réalisés vs planifiés | 100% | Annuel |

---

## Swimlane — Flux du processus

```
┌─────────────┬──────────────────────────────────────────────────────────────┐
│ Client      │ [Réclamation] ──→                    ←── [Rapport qualité] │
│ (externe)   │                                                            │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Rôle        │ [Exigences] ──→                                            │
│ Commercial  │                                                            │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Rôle        │ [Définir plan inspection] → [IPC] → [DUPRO] → [PSI] →     │
│ Qualité     │ [Décision libération] → [Enregistrer NC si applicable] →   │
│             │ [Analyser causes] → [Action corrective] →                  │
│             │ [Vérifier efficacité] → [Clôturer]                         │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Rôle        │            ↑ Info production         ↓ Demande correction  │
│ Achats      │            [Coordonner accès site]   [Suivre correction]   │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Fournisseur │            ↓ Accès production        ↑ Correction          │
│ (externe)   │            [Permettre inspection]    [Corriger]            │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Rôle        │                         ↓ Autorisation expédition          │
│ Logistique  │                         [Procéder à l'expédition]          │
└─────────────┴──────────────────────────────────────────────────────────────┘
```

---

*Réf. ISO 9001:2015 — §8.5, §8.6, §8.7, §9.2, §10.2*
