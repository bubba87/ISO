# REVUE DU DOSSIER v0.5 — Informations Manquantes & Améliorations

## Plus Sàrl — Système de Management de la Qualité ISO 9001:2015

**Date de revue** : 2026-03-04
**Version auditée** : v0.5
**Fichiers audités** : 37 fichiers (9 MQ + 6 processus + 8 documents + 12 chaînes processus + 2 diagrammes)

---

## SYNTHÈSE

| Catégorie | Score | Commentaire |
|-----------|-------|-------------|
| Couverture ISO 9001:2015 | **89%** | 25/28 sous-clauses bien couvertes, 2 partielles, 1 manquante |
| Cohérence interne | **9/10** | Zéro lien cassé, terminologie cohérente, rôles alignés |
| Complétude contenu | **7/10** | Couche stratégique excellente, couche opérationnelle à développer |
| Utilisabilité | **6/10** | Bons documents de référence, mais manque de procédures opérationnelles |
| **Score global** | **7.5/10** | Fondation solide, détails d'exécution à compléter |

---

## 1. INFORMATIONS MANQUANTES

### 1.1 Manques critiques (impact certification)

#### A. Déclaration explicite du domaine d'application (§4.3)

**Constat** : Le domaine d'application du SMQ est implicite (dans INDEX.md et la cartographie) mais il n'existe aucun document dédié déclarant formellement :
- Les limites organisationnelles couvertes
- Les processus inclus (M1, P01-P04, S1)
- Les exclusions justifiées

**Action requise** : Créer un document `DOM-QUA-001_Domaine_Application.md` ou ajouter une section dédiée dans le Manuel Qualité.

#### B. Exclusion formelle du §8.3 — Conception & Développement

**Constat** : Aucune mention du §8.3 dans l'ensemble du dossier. Plus Sàrl étant un intermédiaire de sourcing, la conception produit relève des clients et fournisseurs. Cette exclusion est légitime mais **doit être documentée et justifiée**.

**Action requise** : Ajouter dans le domaine d'application :
> « Le §8.3 (Conception et développement) n'est pas applicable au modèle d'affaires de Plus Sàrl. La conception des produits relève de la responsabilité des clients et des fournisseurs. Plus Sàrl intervient exclusivement en coordination, suivi et contrôle qualité. »

#### C. Statut d'approbation des documents (§7.5.2)

**Constat** : Le registre documentaire `DOC_Gestion_Documentaire.md` montre tous les documents avec le statut `☐ En vigueur` (case non cochée). Aucun document du dossier ne porte d'indication formelle d'approbation (date, approbateur, signature).

**Action requise** :
- Valider chaque document avec date et approbateur
- Cocher les cases « En vigueur » dans le registre
- Ajouter un historique de version dans chaque fichier

#### D. Programme d'audit interne incomplet (§9.2)

**Constat** : Le template `DOC_Audit_Interne.md` contient une matrice programme T1-T4 par processus, mais :
- Aucun auditeur n'est assigné
- Aucune date planifiée
- Pas d'exigence d'indépendance de l'auditeur documentée

**Action requise** :
- Remplir la matrice du programme d'audit (processus × trimestre)
- Assigner les auditeurs (internes ou externes qualifiés)
- Documenter la règle : « L'auditeur ne peut pas auditer son propre processus »

#### E. Matrice de compétences / Skill Matrix (§7.2)

**Constat** : Référencée à plusieurs reprises dans MQ_07 et MQ_03 comme « gérée séparément », mais absente du dossier v0.5. ISO 9001:2015 exige des informations documentées sur les compétences.

**Action requise** : Créer `DOC_Matrice_Competences.md` avec :
- Compétences requises par rôle
- Niveau actuel par personne
- Besoins en formation identifiés
- Enregistrements de formation

---

### 1.2 Manques importants (qualité du SMQ)

#### F. Procédures opérationnelles (PR_*) absentes

**Constat** : Le dossier contient uniquement des fiches processus de haut niveau. Aucune procédure opérationnelle détaillée (étape par étape) n'existe.

**Procédures recommandées** :
| Code | Titre | Processus | Priorité |
|------|-------|-----------|----------|
| PR-P01-001 | Traitement des commandes clients | P01 | Haute |
| PR-P02-001 | Sélection et qualification fournisseur | P02 | Haute |
| PR-P02-002 | Évaluation périodique fournisseur | P02 | Haute |
| PR-P03-001 | Gestion des expéditions internationales | P03 | Haute |
| PR-P04-001 | Inspections qualité (IPC/DUPRO/PSI) | P04 | Haute |
| PR-P04-002 | Gestion des non-conformités | P04 | Haute |
| PR-M1-001 | Revue de direction | M1 | Moyenne |
| PR-S1-001 | Maîtrise documentaire | S1 | Moyenne |

#### G. Matrice RACI manquante

**Constat** : Les rôles sont bien définis dans MQ_03, mais certaines responsabilités sont partagées sans clarification (ex. P01 et P02 partagent la « vérification de faisabilité »). Aucune matrice RACI (Responsible/Accountable/Consulted/Informed) n'existe.

**Action requise** : Créer une matrice RACI couvrant les activités clés de chaque processus.

#### H. Chaînes processus CHAIN-02, 03, 04 incomplètes

**Constat** : Sur 4 types de commande, seul CHAIN-01 (Produit existant) est entièrement détaillé. Les trois autres sont des squelettes (≈30% complétés).

**Détail des manques par chaîne** :

| Chaîne | Manque principal |
|--------|-----------------|
| CHAIN-02 (Modification outillage) | Processus de validation de la modification, portes d'approbation, critères de validation des pièces modifiées |
| CHAIN-03 (Nouvel outillage) | Phase de conception (cahier des charges → plans → simulation), processus d'homologation T0/T1, rôle ingénieur/designer |
| CHAIN-04 (Sourcing) | Procédure d'audit fournisseur, jalons de qualification, exigences first-article inspection |

#### I. Registre des risques insuffisant (§6.1)

**Constat** : Le registre dans MQ_06 contient 8 risques identifiés. Pour une entreprise de coordination internationale, plusieurs risques critiques sont absents :

| Risque manquant | Catégorie | Impact potentiel |
|----------------|-----------|-----------------|
| Fluctuation des devises (EUR/CNY/USD) | Financier | Marge commerciale |
| Cybersécurité / perte de données | Opérationnel | Continuité d'activité |
| Dépendance personnel clé (entreprise individuelle) | Organisationnel | Continuité d'activité |
| Pandémie / force majeure | Environnemental | Chaîne d'approvisionnement |
| Propriété intellectuelle client | Juridique | Responsabilité contractuelle |
| Changements réglementaires (douanes, normes) | Réglementaire | Conformité |

---

### 1.3 Manques mineurs (clarifications)

| # | Élément | Localisation | Détail |
|---|---------|-------------|--------|
| J | Barème de notation fournisseur | DOC_Evaluation_Fournisseur | L'échelle 0-10 n'a pas de descripteurs (que vaut un 7 vs un 8 ?) |
| K | Taux de réponse enquête satisfaction | DOC_Satisfaction_Client | Aucune cible de taux de retour définie |
| L | Question NPS incohérente | DOC_Satisfaction_Client Q14 | Utilise une échelle 1-5 au lieu du standard NPS (0-10) |
| M | Données de référence (baseline) | MQ_06, MQ_09 | Les cibles KPI (85% satisfaction, 90% OTD, ≤5% NC) n'ont pas de données historiques |
| N | Devise de référence | Documents commerciaux | Aucune devise spécifiée dans les templates (EUR? CHF? USD?) |
| O | Protocole de substitution | MQ_03 | Aucun backup défini si un rôle est indisponible |
| P | Délai d'escalade NC | MQ_10 vs DOC_Non_Conformite | MQ_10 définit « ≤ 5 jours ouvrés » pour NC Majeure, mais le template ne le rappelle pas |

---

## 2. AMÉLIORATIONS POTENTIELLES

### 2.1 Améliorations structurelles (haute valeur ajoutée)

#### 1. Arbres de décision pour les situations critiques

Créer des logigrammes décisionnels pour les cas fréquents :

```
PSI échoue → Quelles options ?
├── Refaire l'inspection (défauts mineurs corrigibles)
├── Négocier dérogation client (défauts cosmétiques)
├── Rejeter le lot (NC critique)
│   ├── Action corrective fournisseur
│   └── Relancer production
└── Tri sélectif (défauts localisés)
```

Cas à documenter :
- Échec PSI (Pre-Shipment Inspection)
- Client demande livraison urgente hors planning
- Fournisseur ne répond plus
- Réclamation client post-livraison
- Détection de contrefaçon matières premières

#### 2. Tableau de bord KPI mensuel

Créer un template de reporting mensuel avec indicateurs visuels :

| Indicateur | Cible | Réel | Tendance | Statut |
|-----------|-------|------|----------|--------|
| Satisfaction client | ≥ 85% | __%  | ↑↓→ | Vert/Jaune/Rouge |
| Livraison à temps | ≥ 90% | __%  | ↑↓→ | Vert/Jaune/Rouge |
| Taux NC | ≤ 5%  | __%  | ↑↓→ | Vert/Jaune/Rouge |
| Score fournisseur moyen | ≥ 70/100 | __/100 | ↑↓→ | Vert/Jaune/Rouge |

#### 3. Matrice de traçabilité clause → document

Créer une matrice croisée permettant de retrouver immédiatement quel document répond à quelle clause ISO 9001:2015 :

| Clause ISO | Document(s) principal(s) | Document(s) secondaire(s) |
|-----------|------------------------|--------------------------|
| §4.1 | MQ_04_Contexte | — |
| §4.2 | MQ_04_Contexte | — |
| §4.3 | *À créer* | INDEX.md |
| §5.1 | MQ_05_Leadership | M1_Leadership |
| §5.2 | MQ_05_Leadership | — |
| §5.3 | MQ_03_Support_SMQ | Tous processus |
| §6.1 | MQ_06_Planification | — |
| §6.2 | MQ_06_Planification | DOC_Objectifs_Qualite |
| §7.1-7.4 | MQ_07_Support | — |
| §7.5 | MQ_07_Support | DOC_Gestion_Documentaire, S1 |
| §8.1 | MQ_08_Realisation | CHAIN-01 à 04 |
| §8.2 | MQ_08_Realisation | P01_Commercial, CH-BLOC-001/002 |
| §8.3 | *Exclusion à documenter* | — |
| §8.4 | MQ_08_Realisation | P02, DOC_AQF, DOC_Eval_Fournisseur |
| §8.5-8.6 | MQ_08_Realisation | P03, P04, CH-BLOC-005 à 007 |
| §8.7 | MQ_08_Realisation | DOC_Non_Conformite, P04 |
| §9.1 | MQ_09_Evaluation | DOC_Satisfaction_Client, DOC_Objectifs |
| §9.2 | MQ_09_Evaluation | DOC_Audit_Interne |
| §9.3 | MQ_09_Evaluation | DOC_Revue_Direction |
| §10.1-10.3 | MQ_10_Amelioration | DOC_Non_Conformite |

#### 4. Instructions de travail (IT_*) prioritaires

Pour les tâches les plus critiques, développer des instructions pas-à-pas :

| Code | Titre | Urgence |
|------|-------|---------|
| IT-P04-001 | Réalisation d'une inspection PSI | Haute |
| IT-P04-002 | Rédaction d'un rapport d'inspection | Haute |
| IT-P02-001 | Audit fournisseur sur site | Haute |
| IT-P03-001 | Préparation des documents douaniers | Moyenne |
| IT-P01-001 | Traitement d'une réclamation client | Moyenne |
| IT-S1-001 | Création et codification d'un document | Basse |

---

### 2.2 Améliorations de contenu (valeur moyenne)

#### 5. Barème de notation fournisseur détaillé

Le scoring actuel (0-10 sur 6 critères) manque de descripteurs. Proposition :

| Score | Niveau | Description |
|-------|--------|-------------|
| 9-10 | Excellent | Zéro NC, livraison anticipée, communication proactive |
| 7-8 | Bon | <2% NC mineures, livraison à temps, bonne réactivité |
| 5-6 | Acceptable | 2-5% NC, retards occasionnels, réactivité correcte |
| 3-4 | Insuffisant | >5% NC, retards fréquents, communication difficile |
| 1-2 | Inacceptable | NC critiques, non-respect des délais, AQF non respecté |

#### 6. Protocole de gestion de la propriété client

Pour le §8.5.3 (propriété des clients), documenter :
- Quels types de propriétés client sont gérés (plans, outillages, moules, échantillons)
- Comment les identifier et les protéger chez le fournisseur
- Procédure en cas de perte ou dommage
- Clause à inclure dans l'AQF

#### 7. Plan de continuité d'activité

En tant qu'entreprise individuelle, le risque de « personne clé » est maximal. Documenter :
- Accès aux systèmes critiques (identifiants, mots de passe)
- Liste des fournisseurs avec contacts directs
- Procédures d'urgence en cas d'indisponibilité du dirigeant
- Fournisseurs alternatifs pré-qualifiés

#### 8. Templates pré-remplis

Améliorer l'utilisabilité des formulaires :
- Pré-remplir l'en-tête « Plus Sàrl » dans tous les templates
- Ajouter des catégories standard dans FM-P04-NC (ex. « Défaut matière », « Hors tolérance », « Défaut visuel »)
- Ajouter des exemples dans les formulaires vierges

---

### 2.3 Améliorations cosmétiques (basse priorité)

| # | Amélioration | Impact |
|---|-------------|--------|
| 9 | Ajouter un MQ_01 « Introduction » au manuel qualité | Navigation — le chapitre 1 est absent |
| 10 | Standardiser le format de date dans les templates (`AAAA-MM-JJ` partout) | Cohérence |
| 11 | Ajouter un numéro de version dans le footer de chaque fichier | Traçabilité |
| 12 | Créer un glossaire des termes et abréviations (IPC, DUPRO, PSI, AQF, NC, BL, CI, POD...) | Accessibilité |
| 13 | Traduire les termes anglais utilisés (Loading Check, Skill Matrix, Proof of Delivery) ou les normaliser | Cohérence linguistique |

---

## 3. PLAN D'ACTION RECOMMANDÉ

### Phase 1 — Avant audit de certification (priorité haute)

| # | Action | Responsable | Délai estimé |
|---|--------|-------------|-------------|
| 1 | Rédiger le document de domaine d'application (§4.3 + exclusion §8.3) | Direction | 1 semaine |
| 2 | Compléter le registre documentaire (FM-S1-GD) — approbation de tous les documents | Rôle Gestion Doc. | 1 semaine |
| 3 | Remplir le programme d'audit interne (FM-P04-AUD) | Rôle Qualité | 1 semaine |
| 4 | Créer la matrice de compétences (Skill Matrix) | Direction | 2 semaines |
| 5 | Rédiger les 6 procédures opérationnelles prioritaires (PR_*) | Tous les rôles | 4-6 semaines |
| 6 | Compléter le registre des risques (ajouter 6 risques manquants) | Direction | 1 semaine |

### Phase 2 — Renforcement du SMQ (priorité moyenne)

| # | Action | Responsable | Délai estimé |
|---|--------|-------------|-------------|
| 7 | Compléter CHAIN-02, CHAIN-03, CHAIN-04 | Rôle Commercial + Rôle Achats | 3-4 semaines |
| 8 | Créer la matrice RACI | Direction | 1 semaine |
| 9 | Développer le barème de notation fournisseur détaillé | Rôle Qualité | 1 semaine |
| 10 | Créer les instructions de travail prioritaires (IT_*) | Rôle Qualité | 4-6 semaines |
| 11 | Ajouter les données de référence (baseline) aux KPI | Direction | 2 semaines |

### Phase 3 — Optimisation continue (priorité basse)

| # | Action | Responsable | Délai estimé |
|---|--------|-------------|-------------|
| 12 | Créer les arbres de décision (PSI fail, urgences, etc.) | Rôle Qualité | 2 semaines |
| 13 | Mettre en place le tableau de bord KPI mensuel | Direction | 1 semaine |
| 14 | Créer la matrice de traçabilité clause → document | Rôle Gestion Doc. | 1 semaine |
| 15 | Rédiger le plan de continuité d'activité | Direction | 2 semaines |
| 16 | Ajouter MQ_01, glossaire, templates pré-remplis | Rôle Gestion Doc. | 2 semaines |

---

## 4. POINTS FORTS DU DOSSIER (à conserver)

Le dossier v0.5 présente de nombreuses qualités remarquables qui constituent une base solide :

1. **Architecture processus exemplaire** : 6 processus clairement définis (M1, P01-P04, S1) avec interactions documentées
2. **Chaîne processus innovante** : L'approche par 8 blocs modulaires (CH-BLOC) est élégante et scalable
3. **Cohérence interne parfaite** : Zéro lien cassé sur 37 fichiers, terminologie homogène
4. **Rôles clairement séparés** : 6 rôles indépendants des personnes, bien documentés dans MQ_03
5. **Gestion fournisseur robuste** : Système d'évaluation multi-critères (6 critères pondérés, classification A/B/C)
6. **Templates opérationnels** : 8 formulaires prêts à l'emploi couvrant les enregistrements obligatoires
7. **Indicateurs mesurables** : 9 KPI avec cibles et fréquences de suivi
8. **Couverture ISO complète** : 89% des sous-clauses bien couvertes, aucune clause majeure oubliée
9. **Approche PDCA intégrée** : Boucle d'amélioration continue visible dans tous les processus
10. **Adaptée à l'international** : Documentation pensée pour le contexte multi-pays (Chine, Europe, Worldwide)

---

## 5. TABLEAU RÉCAPITULATIF DES MANQUES

| Réf | Manque | Clause ISO | Sévérité | Phase |
|-----|--------|-----------|----------|-------|
| A | Domaine d'application explicite | §4.3 | Critique | 1 |
| B | Exclusion §8.3 documentée | §4.3, §8.3 | Critique | 1 |
| C | Approbation documents | §7.5.2 | Critique | 1 |
| D | Programme audit complété | §9.2 | Critique | 1 |
| E | Matrice de compétences | §7.2 | Critique | 1 |
| F | Procédures opérationnelles (PR_*) | §7.5, §8.1 | Haute | 1 |
| G | Matrice RACI | §5.3 | Moyenne | 2 |
| H | CHAIN-02, 03, 04 complètes | §8.1 | Moyenne | 2 |
| I | Registre risques étendu | §6.1 | Moyenne | 1 |
| J | Barème notation fournisseur | §8.4 | Basse | 2 |
| K | Cible taux réponse satisfaction | §9.1.2 | Basse | 2 |
| L | Correction échelle NPS | §9.1.2 | Basse | 3 |
| M | Données baseline KPI | §9.1 | Basse | 2 |
| N | Devise de référence | — | Basse | 3 |
| O | Protocole de substitution rôle | §5.3 | Moyenne | 2 |
| P | Rappel délai escalade dans template NC | §10.2 | Basse | 3 |

---

*Revue réalisée le 2026-03-04 — Dossier v0.5*
*Prochaine revue recommandée : après complétion Phase 1*
