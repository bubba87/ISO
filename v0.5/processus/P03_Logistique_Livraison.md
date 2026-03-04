# P03 — Logistique & Livraison

## Fiche Processus

| Élément | Détail |
|---------|--------|
| **Code** | P03 |
| **Type** | Opérationnel |
| **Rôle pilote** | Rôle Logistique |
| **Finalité** | Coordonner les expéditions internationales depuis les fournisseurs jusqu'aux clients, dans les délais et conditions convenus |

---

## Données d'entrée

- Commandes validées (de P01)
- Informations d'expédition des fournisseurs (de P02)
- Rapport d'inspection finale — autorisation d'expédition (de P04)
- Exigences de livraison client (incoterms, destination, délai)

## Données de sortie

- Documents de transport (BL, AWB, CMR)
- Documents douaniers
- Confirmation de livraison
- Suivi des expéditions en temps réel
- Signalement des anomalies logistiques

---

## Activités principales

| # | Activité | Rôle responsable | Documents associés |
|---|----------|-----------------|-------------------|
| 1 | Planifier l'expédition selon les exigences client | Rôle Logistique | Planning expéditions |
| 2 | Sélectionner le transporteur / transitaire | Rôle Logistique | Panel transporteurs |
| 3 | Coordonner avec le fournisseur pour le chargement | Rôle Logistique + Rôle Achats | Instructions d'expédition |
| 4 | Préparer la documentation (transport, douane) | Rôle Logistique | Documents export/import |
| 5 | Suivre l'expédition | Rôle Logistique | Tracking |
| 6 | Confirmer la réception au client | Rôle Logistique + Rôle Commercial | Confirmation livraison |
| 7 | Traiter les litiges transport | Rôle Logistique + Rôle Qualité | DOC_Non_Conformite.md |

---

## Interactions

| Processus | Nature de l'interaction |
|-----------|----------------------|
| M1 — Direction | Reporte les performances logistiques |
| P01 — Commercial | Reçoit les exigences de livraison, informe sur le statut |
| P02 — Achats | Reçoit les informations fournisseur pour l'expédition |
| P04 — Qualité | Reçoit l'autorisation d'expédition, signale les anomalies |

---

## Indicateurs

| Indicateur | Cible | Fréquence |
|-----------|-------|-----------|
| Taux de livraison à temps | ≥ 90% | Trimestriel |
| Taux de litiges transport | ≤ 2% | Trimestriel |
| Délai moyen de transit | Selon incoterm | Mensuel |
| Coût logistique / CA | Tendance stable ou baisse | Trimestriel |

---

## Swimlane — Flux du processus

```
┌─────────────┬──────────────────────────────────────────────────────────────┐
│ Rôle        │ [Exigences livraison] ──────────────→ [Info client livré]  │
│ Commercial  │                                                            │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Rôle        │         ↓ Info fournisseur                                 │
│ Achats      │         [Coordonner chargement]                            │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Rôle        │                 ↓ Autorisation expédition (PSI OK)         │
│ Qualité     │                 [Loading check si requis]                  │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Rôle        │ [Planifier expédition] → [Sélectionner transporteur] →     │
│ Logistique  │ [Préparer documents] → [Coordonner chargement] →          │
│             │ [Suivre expédition] → [Confirmer livraison]                │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Transporteur│              ↓ Instructions                                │
│ (externe)   │              [Transporter] → [Livrer]                      │
└─────────────┴──────────────────────────────────────────────────────────────┘
```

---

*Réf. ISO 9001:2015 — §8.5, §8.6*
