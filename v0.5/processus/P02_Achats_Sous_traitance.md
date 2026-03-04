# P02 — Achats & Sous-traitance

## Fiche Processus

| Élément | Détail |
|---------|--------|
| **Code** | P02 |
| **Type** | Opérationnel |
| **Rôle pilote** | Rôle Achats |
| **Finalité** | Identifier, sélectionner, évaluer et gérer les fournisseurs internationaux pour garantir la conformité des produits et services |

---

## Données d'entrée

- Besoins transmis par le Rôle Commercial (spécifications, quantités, délais)
- Critères de sélection fournisseurs
- Historique de performance des fournisseurs existants
- Exigences qualité et réglementaires

## Données de sortie

- Fournisseurs qualifiés et panel fournisseurs à jour
- Commandes fournisseurs émises
- Accords Qualité Fournisseur (AQF) signés
- Rapports d'évaluation fournisseurs
- Informations de production transmises à P03 et P04

---

## Activités principales

| # | Activité | Rôle responsable | Documents associés |
|---|----------|-----------------|-------------------|
| 1 | Identifier les fournisseurs potentiels à l'international | Rôle Achats | Panel fournisseurs |
| 2 | Évaluer et qualifier les fournisseurs | Rôle Achats + Rôle Qualité | DOC_Evaluation_Fournisseur.md |
| 3 | Négocier et signer l'Accord Qualité Fournisseur | Rôle Achats | DOC_Accord_Qualite_Fournisseur.md |
| 4 | Émettre les commandes fournisseurs | Rôle Achats | Bon de commande |
| 5 | Suivre la production chez le fournisseur | Rôle Achats + Rôle Qualité | Planning de production |
| 6 | Réévaluer périodiquement les fournisseurs | Rôle Achats | DOC_Evaluation_Fournisseur.md |
| 7 | Gérer les non-conformités fournisseurs | Rôle Achats + Rôle Qualité | DOC_Non_Conformite.md |
| 8 | Maintenir le panel fournisseurs (A/B/C) | Rôle Achats | Panel fournisseurs |

---

## Sélection et qualification

### Critères de sélection

- Capacité technique et de production
- Système qualité (certification ISO ou équivalent)
- Références et historique
- Compétitivité (prix, délais, conditions)
- Réactivité et communication
- Accessibilité pour les inspections

### Processus de qualification

1. Identification du besoin → recherche de fournisseurs
2. Pré-évaluation (questionnaire, documentation)
3. Audit initial ou visite sur site (si applicable)
4. Commande d'essai et évaluation des échantillons
5. Signature de l'AQF
6. Intégration au panel fournisseurs

---

## Interactions

| Processus | Nature de l'interaction |
|-----------|----------------------|
| M1 — Direction | Reçoit la stratégie achats, reporte la performance fournisseurs |
| P01 — Commercial | Reçoit les besoins clients, informe sur la faisabilité |
| P03 — Logistique | Transmet les informations d'expédition |
| P04 — Qualité | Coordonne les inspections, traite les NC fournisseurs |

---

## Indicateurs

| Indicateur | Cible | Fréquence |
|-----------|-------|-----------|
| Score moyen d'évaluation fournisseurs | ≥ 70/100 | Semestriel |
| Nombre de fournisseurs qualifiés (classe A) | Maintien ou croissance | Annuel |
| Taux de NC fournisseurs | ≤ 5% | Trimestriel |
| Délai moyen de qualification nouveau fournisseur | ≤ 30 jours | Sur événement |

---

## Swimlane — Flux du processus

```
┌─────────────┬──────────────────────────────────────────────────────────────┐
│ Rôle        │ [Besoin client] ─────────────────────────────→             │
│ Commercial  │                                                            │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Rôle        │ [Identifier fournisseurs] → [Pré-évaluer] →               │
│ Achats      │ [Négocier AQF] → [Émettre commande] →                     │
│             │ [Suivre production] → [Réévaluer fournisseur]              │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Rôle        │        ↑ Audit initial    ↑ Inspections    ↑ NC           │
│ Qualité     │        [Qualifier]        [Contrôler]      [Traiter NC]   │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Fournisseur │        ↓ Questionnaire    ↓ Production     ↓ Correction   │
│ (externe)   │        [Répondre]         [Produire]       [Corriger]     │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Rôle        │                                     ↓ Info expédition      │
│ Logistique  │                                     [Planifier transport]  │
└─────────────┴──────────────────────────────────────────────────────────────┘
```

---

*Réf. ISO 9001:2015 — §8.4*
