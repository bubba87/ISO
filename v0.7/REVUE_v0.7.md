# REVUE v0.7 — Rapport de Revision

**Date**: 2026-03-09
**Version**: 0.7
**Auteur**: Claude (revision automatisee)

---

## 1. Structure du repertoire

| Composant | Nombre | Statut |
|-----------|--------|--------|
| Manuel qualite (MQ_01 a MQ_10) | 10 fichiers | OK |
| Processus (PM01, P01-P04, PS01-PS03) | 8 fichiers | OK |
| Chaines de processus (CHAIN-01 a CHAIN-04) | 4 fichiers | OK |
| Blocs detail (CH-BLOC-001 a CH-BLOC-008) | 8 fichiers | OK |
| Documents operationnels | 8 fichiers | OK |
| Instructions de travail (IT-P03-*) | 5 fichiers | OK |
| Diagrammes drawio | 6 fichiers | OK |
| Scripts de generation | 3 fichiers (.py) | OK |
| Exports (HTML, MD, DOCX, PDF) | 4 fichiers | OK |
| Mirror anglais (eng/) | Structure complete | PARTIEL |

**Total fichiers v0.7**: ~102 fichiers

---

## 2. Diagrammes interactifs

| Diagramme | Pages | Langue | Navigation | Statut |
|-----------|-------|--------|------------|--------|
| processus_iso9001.drawio | 1 | EN | - | OK |
| chaine_processus_general.drawio | 1 | EN | - | OK |
| vue_ensemble_interactive.drawio | 1 | EN | - | OK (v1) |
| vue_ensemble_interactive_v2.drawio | 16 | EN | 3 niveaux | OK |
| **vue_ensemble_interactive_v3.drawio** | **30** | **FR** | **3 niveaux** | **NOUVEAU** |
| vue_ensemble_interactive_v3c.drawio | ~20 | FR | 2 niveaux | OK (draft) |

### v3 - Architecture des 30 pages

| Niveau | Pages | Contenu |
|--------|-------|---------|
| 1 - Vue globale | VUE D'ENSEMBLE v3 | Swimlane: DIRECTION, VENTES, FABRICATION, LIVRAISON, QUALITE, SUPPORT |
| 2 - Processus | PM01, P01, P02, P03, P04, PS01, PS02, PS03 | Chaque processus en swimlane PDCA |
| 2 - Chaines | CHAIN-01 a CHAIN-04 | Chaque type de commande en swimlane 4 roles |
| 2 - Chaine generale | Chaine Processus Generale | Vue consolidee 8 blocs, 4 swimlanes |
| 3 - BLOCs | BLOC 1 a BLOC 8 | Detail swimlane par bloc avec sous-actions |
| 3 - SOUS-BLOCs | SOUS-BLOC 1 a SOUS-BLOC 8 | Niveau le plus profond, groupes d'actions |

---

## 3. Verification des references

### INDEX.md (FR)
- **52 references verifiees**: Toutes pointent vers des fichiers existants
- Ajout du diagramme v3 dans la section Diagrammes
- Date mise a jour: 2026-03-09

### INDEX.md (EN)
- Toutes les references existantes valides
- Ajout du diagramme v3

### Liens internes v3.drawio
- **30 pages**, **30 liens internes**
- **0 lien casse**
- **0 page orpheline**
- Tous les 8 BLOCs lient vers leurs SOUS-BLOCs respectifs

---

## 4. Coherence processus

| Code | Processus MD | Drawio overview | Drawio v3 | Statut |
|------|-------------|-----------------|-----------|--------|
| PM01 | OK | OK | OK | OK |
| P01 | OK | OK | OK | OK |
| P02 | OK | OK | OK | OK |
| P03 | OK | OK | OK | OK |
| P04 | OK | OK | OK | OK |
| PS01 | OK | OK | OK | OK |
| PS02 | OK | Absent en v2 | OK (nouveau) | OK |
| PS03 | OK | OK | OK | OK |

---

## 5. Points d'attention

### Ameliorations apportees (v3)
1. **PS02 desormais inclus** dans le diagramme interactif (absent en v2)
2. **Toutes les pages en format swimlane** (coherent avec la norme ISO)
3. **Navigation 3 niveaux** : Overview → Processus/Bloc → Sous-Bloc
4. **4 types de commande** ont chacun leur page dediee (CHAIN-01 a CHAIN-04)
5. **Langue francaise** harmonisee sur tout le diagramme

### Points restants (pre-existants)
1. **Mirror anglais incomplet**: 5 instructions de travail (IT-P03-*) absentes dans `eng/documents/`
2. **Exports a regenerer**: Les fichiers HTML/PDF/DOCX dans `export/` datent du 2026-03-08 et ne contiennent pas encore le v3
3. **processus_iso9001.drawio et chaine_processus_general.drawio** datent de v0.6 (2026-03-04) — a considerer pour mise a jour

### Recommandations
1. Regenerer les exports avec `build_dossier.py` apres validation
2. Completer le mirror anglais pour les IT-P03-*
3. Considerer la mise a jour des diagrammes v0.6 vers la nomenclature v0.7

---

## 6. Conformite ISO 9001:2015

| Clause | Couverture | Documents |
|--------|------------|-----------|
| §4 Contexte | OK | MQ_04, PM01 |
| §5 Leadership | OK | MQ_05, PM01 |
| §6 Planification | OK | MQ_06, PM01 (risques, objectifs) |
| §7 Support | OK | MQ_07, PS01, PS02 |
| §8 Realisation | OK | MQ_08, P01-P04, CHAIN-01 a 04, BLOC 1-8 |
| §9 Evaluation | OK | MQ_09, DOC_Audit, DOC_Satisfaction |
| §10 Amelioration | OK | MQ_10, PS03, DOC_Non_Conformite |

---

*Revision effectuee le 2026-03-09 — v0.7*
