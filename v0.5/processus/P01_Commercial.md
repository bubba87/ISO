# P01 — Commercial

## Fiche Processus

| Élément | Détail |
|---------|--------|
| **Code** | P01 |
| **Type** | Opérationnel |
| **Rôle pilote** | Rôle Commercial |
| **Finalité** | Gérer la relation client, transformer les demandes en commandes, assurer la satisfaction client |

---

## Données d'entrée

- Demandes clients (consultations, appels d'offres, commandes)
- Exigences spécifiques des clients (cahier des charges, spécifications)
- Informations marché et veille concurrentielle
- Retours de satisfaction et réclamations clients

## Données de sortie

- Devis validés
- Confirmations de commande
- Contrats et accords commerciaux
- Rapports de satisfaction client
- Transfert des exigences vers P02 (Achats) et P03 (Logistique)

---

## Activités principales

| # | Activité | Rôle responsable | Documents associés |
|---|----------|-----------------|-------------------|
| 1 | Réceptionner et analyser la demande client | Rôle Commercial | — |
| 2 | Vérifier la faisabilité (technique, délai, coût) | Rôle Commercial + Rôle Achats | — |
| 3 | Émettre le devis | Rôle Commercial | Devis |
| 4 | Négocier et finaliser les conditions | Rôle Commercial | Contrat / Confirmation |
| 5 | Enregistrer la commande | Rôle Commercial | Bon de commande |
| 6 | Transmettre les exigences aux processus aval | Rôle Commercial | Fiche commande |
| 7 | Suivre l'avancement et informer le client | Rôle Commercial | Rapports d'avancement |
| 8 | Traiter les réclamations | Rôle Commercial + Rôle Qualité | DOC_Non_Conformite.md |
| 9 | Mesurer la satisfaction client | Rôle Commercial | DOC_Satisfaction_Client.md |

---

## Interactions

| Processus | Nature de l'interaction |
|-----------|----------------------|
| M1 — Direction | Reporte les résultats commerciaux, reçoit les orientations stratégiques |
| P02 — Achats | Transmet les besoins de sourcing, reçoit les informations fournisseurs |
| P03 — Logistique | Transmet les exigences de livraison |
| P04 — Qualité | Transmet les réclamations, reçoit les rapports d'inspection |

---

## Indicateurs

| Indicateur | Cible | Fréquence |
|-----------|-------|-----------|
| Taux de transformation devis → commande | ≥ 30% | Trimestriel |
| Satisfaction client | ≥ 85% | Annuel |
| Délai moyen de réponse aux demandes | ≤ 48h | Mensuel |
| Nombre de réclamations | Tendance à la baisse | Trimestriel |

---

## Swimlane — Flux du processus

```
┌─────────────┬──────────────────────────────────────────────────────────────┐
│ Client      │ [Demande / Consultation] ──────────────────→ [Validation]  │
│ (externe)   │                                    ↑              │        │
│             │                              [Devis]              ↓        │
│             │                                    ↑     [Commande confirmée]
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Rôle        │ [Réception demande] → [Analyse faisabilité] →             │
│ Commercial  │ [Émission devis] → [Négociation] → [Enregistrement] →     │
│             │ [Suivi avancement] → [Satisfaction client]                 │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Rôle        │           ↑ Info faisabilité                               │
│ Achats      │           (capacité fournisseurs, coûts)                   │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Rôle        │                              ↓ Exigences livraison         │
│ Logistique  │                                                            │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Rôle        │                    ↓ Rapports inspection                   │
│ Qualité     │                    ↑ Réclamations                          │
└─────────────┴──────────────────────────────────────────────────────────────┘
```

---

*Réf. ISO 9001:2015 — §8.2, §9.1.2*
