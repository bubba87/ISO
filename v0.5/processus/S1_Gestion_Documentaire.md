# S1 — Gestion Documentaire

## Fiche Processus

| Élément | Détail |
|---------|--------|
| **Code** | S1 |
| **Type** | Support |
| **Rôle pilote** | Rôle Gestion Documentaire |
| **Finalité** | Maîtriser la création, la diffusion, la mise à jour et l'archivage des documents et enregistrements du SMQ |

---

## Données d'entrée

- Besoins de documentation des processus
- Exigences ISO 9001:2015 en matière d'informations documentées
- Documents à créer, modifier ou archiver
- Enregistrements générés par les processus

## Données de sortie

- Documents maîtrisés (validés, versionnés, diffusés)
- Liste de gestion documentaire à jour
- Archives organisées et accessibles
- Documents obsolètes retirés de la circulation

---

## Activités principales

| # | Activité | Rôle responsable | Documents associés |
|---|----------|-----------------|-------------------|
| 1 | Créer ou modifier un document | Rôle émetteur + Rôle Gestion Doc. | Modèle de document |
| 2 | Vérifier et valider le document | Rôle Qualité ou Direction | — |
| 3 | Codifier et versionner | Rôle Gestion Doc. | Codification |
| 4 | Diffuser aux rôles concernés | Rôle Gestion Doc. | Liste de diffusion |
| 5 | Retirer les versions obsolètes | Rôle Gestion Doc. | — |
| 6 | Archiver les enregistrements | Rôle Gestion Doc. | Règles d'archivage |
| 7 | Maintenir la liste de gestion documentaire | Rôle Gestion Doc. | DOC_Gestion_Documentaire.md |

---

## Codification des documents

| Préfixe | Type de document | Exemple |
|---------|-----------------|---------|
| MQ | Manuel Qualité | MQ_05_Leadership |
| PR | Procédure | PR_P02_Selection_Fournisseur |
| IT | Instruction de travail | IT_P04_Inspection_PSI |
| FM | Formulaire | FM_P04_Fiche_NC |
| EN | Enregistrement | EN_P02_Eval_Fournisseur_2026 |

### Convention de version

- Format : vX.Y (ex: v1.0, v1.1, v2.0)
- X = révision majeure (changement de fond)
- Y = révision mineure (correction, mise en forme)

---

## Conservation des enregistrements

| Type d'enregistrement | Durée de conservation | Responsable |
|----------------------|----------------------|-------------|
| Rapports d'inspection | 5 ans | Rôle Qualité |
| Fiches de non-conformité | 5 ans | Rôle Qualité |
| Évaluations fournisseurs | 3 ans | Rôle Achats |
| Comptes-rendus revue de direction | 5 ans | Direction |
| Rapports d'audit interne | 5 ans | Rôle Qualité |
| Enquêtes satisfaction client | 3 ans | Rôle Commercial |
| Contrats et commandes | 10 ans | Rôle Commercial |

---

## Interactions

| Processus | Nature de l'interaction |
|-----------|----------------------|
| Tous | Fournit les documents maîtrisés, collecte les enregistrements |
| M1 — Direction | Validation des documents stratégiques |
| P04 — Qualité | Coordination pour les documents qualité |

---

## Indicateurs

| Indicateur | Cible | Fréquence |
|-----------|-------|-----------|
| Liste documentaire à jour | 100% | Trimestriel |
| Documents obsolètes en circulation | 0 | Trimestriel |
| Temps moyen de validation d'un document | ≤ 5 jours | Sur événement |

---

## Swimlane — Flux du processus

```
┌─────────────┬──────────────────────────────────────────────────────────────┐
│ Rôle        │ [Besoin de document] → [Rédiger / Modifier] ──→           │
│ émetteur    │                                                            │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Rôle        │                    ↓ Vérification                          │
│ Qualité /   │                    [Valider le document] ──→               │
│ Direction   │                                                            │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Rôle        │         [Codifier] → [Versionner] → [Diffuser] →          │
│ Gestion     │         [Retirer obsolètes] → [Archiver] →                │
│ Doc.        │         [Mettre à jour la liste documentaire]              │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Tous les    │                              ↓ Documents diffusés          │
│ rôles       │                              [Utiliser les documents]      │
└─────────────┴──────────────────────────────────────────────────────────────┘
```

---

*Réf. ISO 9001:2015 — §7.5*
