# Revue de la version v0.6 — SMQ ISO 9001:2015 Plus Sarl

**Date de revue** : 2026-03-04
**Version analysee** : v0.6
**Fichiers analyses** : 37 fichiers (9 MQ + 6 processus + 12 chaines + 8 documents + 2 drawio)

---

## Synthese

La v0.6 represente la **premiere version formellement structuree** du dossier ISO 9001. Par rapport a la v0.5, les changements principaux sont :

- Ajout de **cartouches de metadonnees** standardises (version, date, approbation, references normatives)
- Restructuration avec **sections numerotees** et references ISO explicites
- Enrichissement du contenu et meilleure formalisation
- Suppression des 3 fichiers de revue de la v0.5

La structure (37 fichiers) reste identique. Aucun fichier n'a ete ajoute ni supprime (hors fichiers de revue).

**Verdict global : 75-80% pret pour audit ISO 9001:2015** — avec des lacunes critiques a combler.

---

## 1. Non-conformites critiques (a corriger AVANT audit)

### 1.1 Processus PS02 — Gestion des competences : ABSENT

- **Clause ISO** : 7.2 (Competences)
- **Constat** : PS02 est reference dans MQ_02, MQ_03, MQ_04, MQ_06, MQ_07 mais **aucun fichier de processus n'existe**
- **Impact** : Non-conformite majeure quasi certaine en audit
- **Action** : Creer `processus/PS02_Gestion_Competences.md`
- **Contenu requis** : Identification des besoins, plan de formation, evaluation, matrice de competences

### 1.2 Matrice de competences : ABSENTE

- **Clause ISO** : 7.2 (Competences)
- **Constat** : Trois references identiques dans MQ_03 et MQ_07 indiquent "sera presentee ulterieurement"
- **Impact** : L'auditeur exigera la preuve de la demonstration des competences
- **Action** : Creer la matrice detaillee (roles x competences, niveaux E/S/B)

### 1.3 Processus PS03 — Amelioration continue : ABSENT

- **Clause ISO** : 10.3 (Amelioration continue)
- **Constat** : MQ_10 reference PS03 dans son en-tete mais ce processus n'existe nulle part dans la cartographie (MQ_02)
- **Impact** : Incoherence documentaire + processus manquant
- **Action** : Creer `processus/PS03_Amelioration_Continue.md` ou integrer dans M1

### 1.4 Classification des non-conformites : INCOHERENTE

- **Clause ISO** : 8.7, 10.2
- **Constat** :
  - MQ_10 definit 4 niveaux : Mineure / Significative / Majeure / Critique
  - DOC_Non_Conformite definit : Mineure / Majeure / Critique / Bloquante
- **Impact** : Deux systemes de classification dans le meme SMQ = non-conformite
- **Action** : Harmoniser sur une seule echelle dans tous les documents

---

## 2. Incoherences de codification (non-conformites mineures)

### 2.1 PM01 vs M1

- MQ_02, MQ_04, MQ_06 utilisent **PM01** (Pilotage strategique)
- Le fichier processus s'appelle **M1_Leadership.md**
- **Action** : Choisir une seule codification et l'appliquer partout

### 2.2 P03/P04 potentiellement inverses

- MQ_02 section 2.3 definit : P03 = Monitoring/QC, P04 = Logistique
- Fichiers : P03_Logistique_Livraison.md, P04_Controle_Qualite.md
- **Action** : Verifier et aligner la numerotation entre manuel et fichiers

### 2.3 PS01 vs S1

- Le manuel reference **PS01** (Gestion documentaire)
- Le fichier s'appelle **S1_Gestion_Documentaire.md**
- **Action** : Harmoniser la nomenclature

### 2.4 PS03 non cartographie

- PS03 apparait dans l'en-tete de MQ_10 mais n'est cite ni dans MQ_02 ni dans MQ_04
- **Action** : Ajouter PS03 a la cartographie officielle ou retirer la reference

---

## 3. Documents et formulaires manquants

### 3.1 Formulaires references mais non fournis

| Code | Intitule | Reference dans |
|------|----------|---------------|
| FM-P01-SAT | Enquete Satisfaction Client (template) | P01_Commercial |
| FM-P02-AQF | Accord Qualite Fournisseur (template) | P02_Achats |
| FM-P02-EVAL | Evaluation Fournisseur (template) | P02_Achats |
| IT-P04-ECH | Instruction echantillonnage AQL | P04_Controle_Qualite |

> **Note** : Les DOC_Satisfaction_Client, DOC_Accord_Qualite_Fournisseur et DOC_Evaluation_Fournisseur existent et pourraient couvrir ces besoins. Il faudrait aligner les references (FM-xxx vs DOC_xxx).

### 3.2 Instructions de travail absentes

Les instructions de travail (IT) ne sont pas documentees :
- IT inspection IPC
- IT inspection DUPRO
- IT inspection PSI
- IT Loading Check
- IT audit fournisseur

### 3.3 Chapitre MQ_01 absent

- Le manuel commence directement a MQ_02
- Un chapitre d'introduction (objet, domaine d'application, guide de lecture, historique) serait recommande
- **Severite** : Faible (pas d'exigence normative directe)

---

## 4. Chaines de processus incompletes

### 4.1 CHAIN-01 : Commande Produit Existant
- **Statut** : 100% complet
- KPI, RACI, references ISO : tous presents

### 4.2 CHAIN-02 : Commande Modification Outillage
- **Statut** : ~70% complet (marque "A completer")
- **Manque** : BLOC 3 et BLOC 7 non detailles, matrice RACI absente
- Criteres validation post-modification non documentes

### 4.3 CHAIN-03 : Commande Nouvel Outillage
- **Statut** : ~75% complet (marque "A completer")
- **Manque** : BLOC 3 et BLOC 7, matrice RACI, livrables T0/T1, propriete intellectuelle outillage

### 4.4 CHAIN-04 : Commande Sourcing
- **Statut** : ~70% complet (marque "A completer")
- **Manque** : BLOC 3 et BLOC 7, matrice RACI, criteres de selection fournisseur, processus audit fournisseur

### 4.5 Fiches BLOC (001-008)
- **Statut** : 100% complets (entrees/sorties/points de controle/responsabilites)

---

## 5. Problemes de formatage

### 5.1 Encodage UTF-8 inconsistant

| Fichier | Accents | Etat |
|---------|---------|------|
| MQ_02, MQ_03 | Preserves (Qualite, Activites) | OK |
| MQ_04 | Mixte (titres sans accents, contenu avec) | A corriger |
| MQ_05, MQ_06, MQ_08, MQ_09, MQ_10 | Absents (Qualite, Realisation, Evaluation) | A corriger |

- **Impact** : Documents moins professionnels pour un auditeur francophone
- **Action** : Uniformiser tous les fichiers en UTF-8 avec accents francais

### 5.2 Erreur de numerotation normative

- MQ_09 titre "9.1.3 Satisfaction du client"
- ISO 9001:2015 place la satisfaction client en **9.1.2**
- **Action** : Corriger la numerotation

### 5.3 Placeholder non resolu

- MQ_10, ligne 49 : "Reference sequentielle NC-AAAA-XXX"
- "XXX" est un placeholder
- **Action** : Remplacer par le format reel (ex: NC-2026-001)

---

## 6. KPIs : points d'attention

### 6.1 Couverture excellente
- **37 KPIs** definis au total (6-7 par processus)
- Cibles generalement realistes et mesurables

### 6.2 KPIs a ajuster

| KPI | Processus | Probleme | Action |
|-----|-----------|----------|--------|
| Taux de fidelisation client | P01 | Periode de reference non definie | Preciser (12 mois glissants ?) |
| Delai moyen de transit | P03 | Cible "Selon destination" = non mesurable | Definir cible par region/corridor |
| Taux documents a jour | S1 | Cible 100% = irrealiste | Ramener a 98% |

---

## 7. Documents operationnels : analyse

Les 8 documents du repertoire `/documents/` sont **tous complets et exploitables** :

| Document | Code | Completude |
|----------|------|-----------|
| Accord Qualite Fournisseur | FM-P02-AQF | 95% (formulaire a remplir) |
| Audit Interne | FM-P04-AUD | 100% |
| Evaluation Fournisseur | FM-P02-EVAL | 100% |
| Gestion Documentaire | FM-S1-GD | 100% |
| Non-Conformite | FM-P04-NC | 100% |
| Objectifs Qualite | FM-M1-OBJ | 100% |
| Revue de Direction | FM-M1-RD | 100% |
| Satisfaction Client | FM-P01-SAT | 100% |

---

## 8. Cross-references : analyse

### 8.1 Coherences verifiees
- Les 4 CHAIN referencing correctement les 8 BLOC
- Manuel Qualite ↔ Documents support : globalement coherent
- DOC_Objectifs_Qualite reprend les 6 objectifs de MQ_06
- DOC_Audit_Interne reprend la checklist ISO de MQ_09
- DOC_Revue_Direction reprend les entrees/sorties de MQ_09

### 8.2 Liens manquants
- Aucune reference croisee entre CHAIN/BLOC et documents operationnels
- Exemple : BLOC 6 devrait referencer FM-P04-NC ; BLOC 8 devrait referencer FM-P01-SAT

---

## 9. Points forts de la v0.6

- Couverture ISO 9001:2015 globalement bonne (clauses 4 a 10)
- Exclusion 8.3 (Conception) correctement justifiee et documentee
- 4 processus operationnels bien definis avec swimlanes
- 37 KPIs ambitieux et mesurables
- Gestion des risques formalisee (registre risques/opportunites dans MQ_06)
- Matrice RACI complete dans MQ_03
- 8 documents support coherents et exploitables
- 8 fiches BLOC completes avec entrees/sorties/points de controle
- Cartographie drawio avec processus et chaine generale

---

## 10. Plan d'action prioritaire

### Priorite 1 — CRITIQUE (avant tout audit)

| # | Action | Effort | Clause ISO |
|---|--------|--------|-----------|
| 1 | Creer processus PS02 (Gestion des competences) | 1 jour | 7.2 |
| 2 | Creer matrice de competences detaillee | 1 jour | 7.2 |
| 3 | Creer processus PS03 (Amelioration continue) ou l'integrer dans M1 | 0.5 jour | 10.3 |
| 4 | Harmoniser classification NC (MQ_10 vs DOC_Non_Conformite) | 0.5 jour | 8.7, 10.2 |
| 5 | Unifier nomenclature processus (PM01/M1, PS01/S1, P03/P04) | 0.5 jour | 4.4 |

### Priorite 2 — IMPORTANT (avant audit)

| # | Action | Effort |
|---|--------|--------|
| 6 | Finaliser CHAIN-02, CHAIN-03, CHAIN-04 (BLOC 3, 7, RACI) | 2 jours |
| 7 | Aligner references formulaires (FM-xxx vs DOC_xxx) | 0.5 jour |
| 8 | Corriger numerotation 9.1.3 → 9.1.2 dans MQ_09 | 5 min |
| 9 | Corriger encodage UTF-8 (MQ_05, MQ_06, MQ_08, MQ_09, MQ_10) | 1 jour |
| 10 | Ajouter cross-references CHAIN/BLOC → documents operationnels | 0.5 jour |

### Priorite 3 — SOUHAITABLE

| # | Action | Effort |
|---|--------|--------|
| 11 | Creer MQ_01 (Introduction au Manuel) | 0.5 jour |
| 12 | Creer instructions de travail (IT inspection IPC, DUPRO, PSI) | 2 jours |
| 13 | Affiner KPIs (fidelisation, transit, documents a jour) | 0.5 jour |
| 14 | Ajouter historique des revisions dans chaque document | 0.5 jour |
| 15 | Documenter propriete intellectuelle outillage (CHAIN-03) | 0.5 jour |

---

## 11. Risques pour la certification

| Risque | Probabilite | Severite | Clause |
|--------|------------|----------|--------|
| NC majeure : absence matrice competences | Tres elevee | Majeure | 7.2 |
| NC majeure : absence processus PS02 | Elevee | Majeure | 7.1.2 |
| NC majeure : classification NC incoherente | Moyenne | Significative | 10.2 |
| NC mineure : codification processus incoherente | Moyenne | Mineure | 4.4 |
| NC mineure : chaines processus incompletes | Moyenne | Mineure | 8.1 |
| NC mineure : KPIs mal definis | Faible | Mineure | 9.1 |

**Recommandation** : Ne pas presenter a l'audit avant resolution des actions Priorite 1.

---

## 12. Note de conformite README

Le README.md indique toujours "Version actuelle : v0.4" et une structure basee sur v0.4.
- **Action** : Mettre a jour le README pour refleter la structure v0.6

---

*Revue effectuee le 2026-03-04 — Version 0.6 du SMQ Plus Sarl*
