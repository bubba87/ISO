# REVUE COMPLÈTE DU DOSSIER v0.5 — Analyse Approfondie

## Plus Sàrl — Système de Management de la Qualité ISO 9001:2015

**Date de revue** : 2026-03-04
**Version auditée** : v0.5
**Méthode** : Cross-référencement du PDF source (UPDATE_ALL_260304.pdf) avec les 37 fichiers markdown du dossier v0.5
**Fichiers analysés** : 9 MQ + 6 processus + 8 documents opérationnels + 4 chaînes processus + 8 blocs + 2 diagrammes

---

## SYNTHÈSE EXÉCUTIVE

| Catégorie | Score | Commentaire |
|-----------|-------|-------------|
| Couverture ISO 9001:2015 | **85%** | 23/28 sous-clauses couvertes, 3 partielles, 2 manquantes |
| Fidélité au PDF source | **75%** | Le PDF contient des informations opérationnelles non reprises dans les fichiers MD |
| Cohérence interne | **8/10** | Terminologie cohérente mais plusieurs incohérences entre PDF source et MD |
| Complétude contenu | **6/10** | Couche stratégique solide, couche opérationnelle largement à développer |
| Approbation formelle | **2/10** | Aucun document officiellement approuvé (tous ☐ En vigueur non cochés) |
| Utilisabilité opérationnelle | **5/10** | Bons templates mais manque de procédures pas-à-pas |
| **Score global** | **6.5/10** | Fondation solide, mais des écarts importants à combler avant certification |

---

## PARTIE 1 — INFORMATIONS MANQUANTES

### 1.1 MANQUES CRITIQUES (bloquants pour la certification)

---

#### A. Domaine d'application formalisé (§4.3) — ABSENT

**Constat** : Aucun document dédié ne déclare formellement le domaine d'application du SMQ. C'est une exigence explicite de la norme ISO 9001:2015 §4.3.

**Ce qui doit être documenté** :
- Périmètre organisationnel : Plus Sàrl, siège de Cudrefin (Suisse)
- Activités couvertes : coordination industrielle internationale, sourcing, suivi de production, contrôle qualité, logistique
- Zones géographiques : Europe (clients) ↔ Chine (fournisseurs principaux) ↔ Worldwide (sourcing)
- Processus inclus : M1, P01, P02, P03, P04, S1
- **Exclusions justifiées** (voir point B)

**Impact audit** : Non-conformité majeure certaine. Un auditeur demandera ce document en tout premier lieu.

---

#### B. Exclusion du §8.3 — Conception & Développement — NON DOCUMENTÉE

**Constat** : Le §8.3 n'est mentionné nulle part dans le dossier. Or, Plus Sàrl ne conçoit pas les produits — la conception relève des clients et des fournisseurs. Cette exclusion est parfaitement légitime mais **doit être explicitement documentée et justifiée**.

**Justification à rédiger** :
> « Le §8.3 (Conception et développement des produits et services) n'est pas applicable. Plus Sàrl intervient exclusivement en tant qu'intermédiaire de coordination industrielle. La conception des produits est réalisée par les clients (qui fournissent les spécifications techniques et plans) ou par les fournisseurs (qui conçoivent les outillages). Plus Sàrl ne modifie, ne conçoit et ne développe aucun produit ou service au sens de la norme. »

**Impact audit** : Non-conformité majeure. Sans cette justification, l'auditeur considérera que le §8.3 s'applique et constatera l'absence de tout processus de conception.

---

#### C. Approbation formelle des documents (§7.5.2) — AUCUNE

**Constat** : Le registre documentaire `DOC_Gestion_Documentaire.md` montre **tous les documents avec le statut ☐ (non coché)**. Aucun document du dossier ne porte :
- Date d'approbation
- Nom de l'approbateur
- Numéro de version validé
- Historique des révisions

**Le PDF source** mentionne que la politique qualité a été signée le 19 février 2026, mais cette date n'apparaît dans aucun fichier MD.

**Action requise** :
1. Ajouter un cartouche d'approbation dans chaque document (date, version, approbateur)
2. Cocher les cases « En vigueur » dans le registre documentaire
3. Créer un historique de révision dans chaque fichier

**Impact audit** : Non-conformité majeure. L'auditeur vérifiera systématiquement que les documents sont approuvés et contrôlés.

---

#### D. Matrice de compétences / Skill Matrix (§7.2) — ABSENTE

**Constat** : Référencée à 3 reprises (MQ_03, MQ_05, MQ_07) comme « gérée séparément », mais totalement absente du dossier. ISO 9001:2015 §7.2 exige des **informations documentées** sur les compétences.

**Le PDF source** est plus détaillé sur les compétences :
- Connaissance technique des produits
- Maîtrise des exigences clients
- Capacité de coordination internationale
- Compréhension qualité et réglementaire
- Expérience professionnelle et pratique continue

**Action requise** : Créer `DOC_Matrice_Competences.md` avec :

| Rôle | Compétence requise | Niveau requis | Personne | Niveau actuel | Formation prévue |
|------|-------------------|---------------|----------|---------------|------------------|
| Direction | Management stratégique | Expert | | | |
| Direction | ISO 9001:2015 | Avancé | | | |
| Rôle Commercial | Négociation internationale | Avancé | | | |
| Rôle Achats | Sourcing international | Expert | | | |
| etc. | | | | | |

**Impact audit** : Non-conformité majeure. L'auditeur demandera les preuves de compétence pour chaque rôle.

---

#### E. Programme d'audit interne planifié (§9.2) — VIDE

**Constat** : Le template `DOC_Audit_Interne.md` contient une matrice T1-T4 par processus avec des cases à cocher, mais :
- Aucune date précise planifiée
- Aucun auditeur assigné
- Pas de règle d'indépendance documentée (l'auditeur ne doit pas auditer son propre processus)
- Pas de critères de priorisation (processus plus risqués = audits plus fréquents)

**Action requise** :
1. Remplir la matrice avec des dates concrètes
2. Assigner des auditeurs (internes ou externes)
3. Documenter : « L'auditeur ne peut pas auditer le processus dont il est responsable »
4. Justifier la fréquence (ex. P04 Qualité audité 2x/an car critique)

**Impact audit** : Non-conformité majeure. Un programme d'audit vide = pas d'audit planifié.

---

### 1.2 INCOHÉRENCES ENTRE LE PDF SOURCE ET LES DOCUMENTS v0.5

Ce sont des informations **présentes dans le PDF source** (UPDATE_ALL_260304.pdf) mais **absentes ou différentes** dans les fichiers markdown v0.5.

---

#### F. Outils opérationnels : FileMaker et WeChat — NON MENTIONNÉS

**Dans le PDF source** : FileMaker est mentionné comme l'outil central pour :
- Création et suivi des commandes
- Fiches de production
- Fiches de transport
- Registre des non-conformités (à formaliser)
- Suivi des livraisons

WeChat est mentionné comme canal de communication opérationnel avec les partenaires chinois.

**Dans le dossier v0.5** : MQ_07 mentionne « ERP, messagerie, outils de suivi de commandes » de façon générique. Aucune mention de FileMaker ni de WeChat.

**Risque** : L'auditeur demandera quels sont les outils concrets utilisés. Des réponses vagues ne sont pas suffisantes.

**Action requise** : Mettre à jour MQ_07 §7.1.2 et §7.4 avec les outils réels :
- ERP : **FileMaker** (gestion commandes, production, transport, qualité)
- Communication fournisseurs chinois : **WeChat** + email
- Communication clients : **Email** + téléphone + visioconférence
- Stockage documentaire : **Ordinateur / Cloud** (préciser)

---

#### G. Objectifs qualité : délais de livraison spécifiques — NON REPRIS

**Dans le PDF source** (§6.2), les objectifs de délai sont très précis :
- Transport maritime/ferroviaire : livraison dans **1-2 semaines ouvrées** de la date prévue
- Transport aérien : livraison dans **2-4 jours ouvrés** de la date prévue

**Dans le dossier v0.5** : MQ_06 indique simplement « ≥ 90% de livraisons à temps » sans définir ce que « à temps » signifie précisément ni distinguer les modes de transport.

**Action requise** : Aligner MQ_06 et DOC_Objectifs_Qualite avec les critères du PDF source.

---

#### H. Actions en cours (mentionnées en rouge dans le PDF) — NON CAPTURÉES

**Le PDF source** identifie clairement des actions en cours :

1. **Formalisation de la fiche de contrôle qualité fabricant** — à coordonner avec « YAN » lors du prochain voyage en Chine
2. **Formalisation du registre de non-conformités dans FileMaker**
3. **Renforcement du processus formel de libération produit**
4. **Renforcement du suivi formel fournisseur** pour une meilleure traçabilité

Ces actions sont marquées en rouge dans le PDF, signifiant qu'elles sont prioritaires et en cours.

**Dans le dossier v0.5** : Aucune de ces actions n'est documentée nulle part.

**Action requise** : Créer un registre des actions en cours ou les intégrer dans le document de revue de direction.

---

#### I. Contexte : focus Chine vs. « Worldwide » — INCOHÉRENCE

**Dans le PDF source** : Plus Sàrl est décrit comme un « intermédiaire de coordination industrielle internationale entre clients européens et partenaires manufacturiers chinois ». Le focus est clairement Chine.

**Dans le dossier v0.5** : MQ_02 et MQ_04 utilisent « fournisseurs dans le monde entier », « Worldwide ». L'INDEX dit aussi « sourcing Worldwide ».

**Recommandation** : Clarifier. Si le cœur d'activité est la Chine avec possibilité d'extension, le formuler ainsi :
> « Principalement orienté vers des partenaires industriels en Chine, avec capacité de sourcing étendue à d'autres zones géographiques. »

---

#### J. Fournisseurs spécifiques (Yuyao, Oukailuo) — DISPARUS

**Dans la v0.4** : Des accords qualité spécifiques existaient (FOR-AQF-001_Accord_Qualite_Yuyao, FOR-AQF-002_Accord_Qualite_Oukailuo).

**Dans la v0.5** : Ces accords ont été remplacés par un template générique. C'est acceptable pour la documentation, mais il faudrait conserver les accords signés comme **enregistrements** (preuves de fonctionnement du SMQ).

**Action requise** : S'assurer que les AQF signés avec Yuyao et Oukailuo existent (même en dehors du repo Git) et sont référencés dans le registre documentaire.

---

### 1.3 CLAUSES ISO 9001:2015 INSUFFISAMMENT COUVERTES

---

#### K. §8.5.3 — Propriété des clients — TRÈS SOMMAIRE

**Constat** : MQ_08 §8.2.1 mentionne « Gérer la propriété du client (si applicable) » en une ligne. Or, pour une société de coordination industrielle, la propriété client est un sujet majeur :
- **Plans et dessins techniques** transmis aux fournisseurs
- **Outillages et moules** stockés chez les fournisseurs chinois
- **Échantillons de référence** envoyés pour production
- **Données confidentielles** (spécifications, prix)

**Action requise** : Créer une section dédiée dans MQ_08 ou un document séparé couvrant :
- Types de propriétés client gérées
- Méthode d'identification et de protection chez le fournisseur
- Procédure en cas de perte, dommage ou détérioration
- Clause spécifique dans l'AQF sur la propriété client
- Engagement de confidentialité / NDA

---

#### L. §8.5.4 — Préservation — ABSENT

**Constat** : Aucune mention de la préservation des produits pendant le stockage, le transport et la livraison. Pour une entreprise de coordination logistique internationale, c'est un point critique :
- Emballage adapté au transport maritime/aérien/ferroviaire
- Protection contre l'humidité, les chocs, la corrosion
- Conditions de stockage chez le fournisseur avant expédition
- Vérification de l'état à réception (Loading Check déjà mentionné dans §8.5)

**Action requise** : Ajouter une section §8.5.4 dans MQ_08 documentant les exigences de préservation.

---

#### M. §8.5.5 — Activités après livraison — ABSENT

**Constat** : Aucune mention des activités post-livraison. Même si Plus Sàrl est un intermédiaire, les activités suivantes sont pertinentes :
- Suivi de la satisfaction après livraison
- Support technique post-livraison
- Gestion des garanties fournisseur
- Traitement des retours

**Action requise** : Documenter, même brièvement, les activités post-livraison applicables.

---

#### N. §6.1 — Registre des risques incomplet

**Constat** : Le registre dans MQ_06 contient 8 risques/opportunités. Plusieurs risques critiques pour une PME de coordination internationale sont absents :

| Risque manquant | Catégorie | Justification |
|----------------|-----------|---------------|
| Fluctuation EUR/CNY/USD | Financier | Impact direct sur les marges (mentionné dans SWOT MQ_04 mais pas dans le registre §6.1) |
| Cybersécurité / perte de données | Opérationnel | FileMaker contient toutes les données clients et fournisseurs |
| Dépendance personne clé | Organisationnel | Plus Sàrl est une structure légère, la perte du dirigeant = arrêt total |
| Pandémie / force majeure | Environnemental | Leçon COVID ; impact chaîne Chine-Europe |
| Propriété intellectuelle client | Juridique | Plans techniques transmis aux fournisseurs chinois |
| Non-conformité réglementaire douanière | Réglementaire | Import/export entre Suisse, UE et Chine |

**Remarque** : La fluctuation des taux de change est mentionnée dans le SWOT (MQ_04 ligne « Menaces ») mais absente du registre des risques (MQ_06 §6.1). C'est une incohérence interne.

---

#### O. §9.1.2 — Satisfaction client : échelle NPS incorrecte

**Constat** : Dans DOC_Satisfaction_Client.md, la question 14 (NPS — Net Promoter Score) utilise une échelle 1-5, alors que le NPS standard utilise une échelle **0-10**.

**Action requise** : Soit utiliser l'échelle NPS standard (0-10), soit renommer la question pour ne pas la qualifier de « NPS ».

---

### 1.4 MANQUES IMPORTANTS (qualité du SMQ)

---

#### P. Procédures opérationnelles (PR_*) — AUCUNE

**Constat** : Le dossier contient des fiches processus de haut niveau et des templates de formulaires, mais **aucune procédure opérationnelle** détaillant le « comment faire » pas-à-pas. La norme n'exige pas de « procédures » au sens strict, mais l'auditeur s'attend à voir des descriptions suffisantes des activités.

**Procédures prioritaires à créer** :

| Code | Titre | Urgence | Justification |
|------|-------|---------|---------------|
| PR-P01-001 | Traitement d'une commande client | Haute | Processus cœur de métier |
| PR-P02-001 | Sélection et qualification fournisseur | Haute | Processus critique pour la qualité |
| PR-P03-001 | Gestion des expéditions internationales | Haute | Multiples parties prenantes |
| PR-P04-001 | Inspection qualité (IPC/DUPRO/PSI) | Haute | Processus de libération |
| PR-P04-002 | Traitement des non-conformités | Haute | Exigence §10.2 |
| PR-S1-001 | Maîtrise documentaire | Moyenne | Support du SMQ |
| PR-M1-001 | Revue de direction | Moyenne | Exigence §9.3 |
| PR-P02-002 | Évaluation périodique fournisseur | Moyenne | Exigence §8.4 |

---

#### Q. Matrice RACI — ABSENTE

**Constat** : Les rôles sont bien définis dans MQ_03, mais certaines zones grises existent. Par exemple :
- Qui est **Responsable** vs **Accountable** pour la libération d'une commande ?
- Qui est **Consulté** lors de la sélection d'un nouveau fournisseur ?
- Le Rôle Qualité et le Rôle Achats partagent la « vérification de faisabilité » (MQ_02 §2.2.1) — qui décide en cas de désaccord ?

**Action requise** : Créer une matrice RACI pour les activités clés de chaque processus.

---

#### R. Chaînes processus CHAIN-02, 03, 04 — SQUELETTIQUES

**Constat** : Sur 4 types de commande :
- **CHAIN-01** (Produit existant) : entièrement détaillé avec 8 blocs complets
- **CHAIN-02** (Modification outillage) : squelette avec « fiches détaillées à compléter ultérieurement »
- **CHAIN-03** (Nouvel outillage) : squelette avec « fiches détaillées à compléter ultérieurement »
- **CHAIN-04** (Sourcing) : squelette avec « fiches détaillées à compléter ultérieurement »

De plus, les liens dans CHAIN-02/03/04 pointent vers des noms de fichiers différents (CH-BLOC-002_Revue_Planification.md, CH-BLOC-003_Lancement_Production.md, etc.) qui ne correspondent pas aux noms réels des fichiers (CH-BLOC-002_Fiche_Commande.md, CH-BLOC-003_Fiche_Transport.md, etc.). **Ce sont des liens cassés.**

**Action requise** :
1. Corriger les liens dans CHAIN-02, 03, 04 pour pointer vers les bons fichiers
2. Compléter les fiches détaillées pour chaque type de commande

---

#### S. Protocole de substitution des rôles — ABSENT

**Constat** : Aucun plan de continuité en cas d'indisponibilité d'un rôle. Pour une structure légère comme Plus Sàrl, c'est un risque majeur.

**Action requise** : Documenter dans MQ_03 ou MQ_07 :
- Qui remplace qui en cas d'absence ?
- Quelles sont les délégations d'autorité ?
- Comment les accès aux systèmes sont-ils assurés ?

---

### 1.5 MANQUES MINEURS (améliorations de qualité)

| # | Élément | Localisation | Détail |
|---|---------|-------------|--------|
| T | Barème de notation fournisseur | DOC_Evaluation_Fournisseur | L'échelle 0-10 n'a pas de descripteurs (que vaut un 7 vs un 8 ?) |
| U | Cible taux de retour enquête satisfaction | DOC_Satisfaction_Client | Aucune cible de taux de réponse définie (ex. ≥ 60%) |
| V | Données historiques (baseline) KPI | MQ_06, MQ_09, DOC_Objectifs | Toutes les cibles sont définies (85%, 90%, 5%...) mais aucune donnée de référence |
| W | Devise de référence | Tous les templates commerciaux | Aucune devise spécifiée (EUR? CHF? USD? CNY?) |
| X | Format de date incohérent | Templates vs Manuel | Templates utilisent `____/____/________`, MQ utilise `AAAA-MM-JJ` |
| Y | MQ_01 Introduction manquant | Manuel Qualité | Le chapitre 1 est absent — le MQ commence au chapitre 2 |
| Z | Glossaire des abréviations | Ensemble du dossier | Aucun glossaire pour IPC, DUPRO, PSI, AQF, NC, BL, CI, POD, NPS, RACI, etc. |

---

## PARTIE 2 — AMÉLIORATIONS POTENTIELLES

### 2.1 AMÉLIORATIONS À HAUTE VALEUR AJOUTÉE

---

#### 1. Matrice de traçabilité clause ISO → document

Créer une matrice croisée permettant de localiser instantanément quel document couvre quelle clause. C'est un outil indispensable pour l'audit.

| Clause ISO 9001:2015 | Exigence | Document(s) principal(s) | Statut |
|----------------------|----------|-------------------------|--------|
| §4.1 | Contexte de l'organisme | MQ_04_Contexte | Couvert |
| §4.2 | Parties intéressées | MQ_04_Contexte | Couvert |
| §4.3 | Domaine d'application | **À CRÉER** | MANQUANT |
| §4.4 | SMQ et processus | INDEX.md, MQ_03 | Couvert |
| §5.1 | Leadership et engagement | MQ_05_Leadership, M1_Leadership | Couvert |
| §5.2 | Politique qualité | MQ_05_Leadership | Couvert |
| §5.3 | Rôles, responsabilités | MQ_03_Support_SMQ | Couvert |
| §6.1 | Risques et opportunités | MQ_06_Planification | Partiel (risques incomplets) |
| §6.2 | Objectifs qualité | MQ_06, DOC_Objectifs_Qualite | Couvert |
| §6.3 | Planification des modifications | MQ_06_Planification | Couvert |
| §7.1 | Ressources | MQ_07_Support | Couvert |
| §7.2 | Compétences | MQ_07_Support | Partiel (Skill Matrix absente) |
| §7.3 | Sensibilisation | MQ_07_Support | Couvert |
| §7.4 | Communication | MQ_07_Support | Couvert |
| §7.5 | Informations documentées | MQ_07, DOC_Gestion_Documentaire, S1 | Couvert |
| §8.1 | Planification opérationnelle | MQ_08, CHAIN-01 à 04 | Partiel |
| §8.2 | Exigences produits/services | MQ_08, P01_Commercial | Couvert |
| §8.3 | Conception et développement | **Exclusion à documenter** | MANQUANT |
| §8.4 | Maîtrise fournisseurs | MQ_08, P02, DOC_AQF, DOC_Eval | Couvert |
| §8.5 | Production et prestation | MQ_08, P03, P04, CH-BLOC | Couvert |
| §8.5.3 | Propriété du client | MQ_08 (1 ligne) | INSUFFISANT |
| §8.5.4 | Préservation | — | MANQUANT |
| §8.5.5 | Activités après livraison | — | MANQUANT |
| §8.6 | Libération | MQ_08 | Couvert |
| §8.7 | Éléments de sortie NC | MQ_08, DOC_Non_Conformite | Couvert |
| §9.1 | Surveillance et mesure | MQ_09, DOC_Objectifs | Couvert |
| §9.1.2 | Satisfaction client | MQ_09, DOC_Satisfaction_Client | Couvert (NPS à corriger) |
| §9.2 | Audit interne | MQ_09, DOC_Audit_Interne | Partiel (programme vide) |
| §9.3 | Revue de direction | MQ_09, DOC_Revue_Direction | Couvert |
| §10.1 | Amélioration générale | MQ_10_Amelioration | Couvert |
| §10.2 | NC et actions correctives | MQ_10, DOC_Non_Conformite | Couvert |
| §10.3 | Amélioration continue | MQ_10_Amelioration | Couvert |

---

#### 2. Arbres de décision pour situations critiques

Créer des logigrammes décisionnels pour les cas fréquents. Cela facilitera la prise de décision rapide et démontrera la maturité du SMQ à l'auditeur.

**Cas prioritaires** :

**a) Échec PSI (Pre-Shipment Inspection)**
```
PSI échoue
├── Défauts mineurs corrigibles
│   └── Fournisseur corrige → Re-inspection → PSI OK → Expédition
├── Défauts cosmétiques
│   └── Négocier dérogation client → Client accepte ?
│       ├── Oui → Expédition avec dérogation documentée
│       └── Non → Retour au fournisseur
├── NC critique
│   └── Rejeter le lot → Fiche NC → Action corrective fournisseur → Relancer production
└── Défauts localisés
    └── Tri sélectif → Expédition partielle + remplacement
```

**b) Fournisseur ne répond plus**
```
Pas de réponse sous 48h
├── Relance WeChat + Email + Téléphone
│   └── Réponse obtenue → Reprise du suivi normal
├── Pas de réponse sous 5 jours
│   └── Alerte Direction → Contact alternatif chez le fournisseur
├── Pas de réponse sous 10 jours
│   └── Activation fournisseur alternatif
│       └── Information client du retard potentiel
└── Risque de non-livraison
    └── Déclenchement plan de contingence
        └── Mise à jour évaluation fournisseur → Reclassification potentielle
```

**c) Réclamation client post-livraison**
```
Réclamation reçue
├── Enregistrer dans FileMaker (fiche NC)
├── Accusé réception client ≤ 24h
├── Classifier : Critique / Majeure / Mineure
├── Analyse cause avec fournisseur
│   ├── Cause fournisseur → Action corrective fournisseur + AQF
│   ├── Cause transport → Réclamation transporteur
│   └── Cause coordination → Action corrective interne
├── Proposition de résolution client ≤ 5 jours
│   ├── Remplacement → Lancer nouvelle production
│   ├── Avoir / Remboursement → Accord commercial
│   └── Retouche locale → Coordination solution
└── Vérification efficacité sous 30 jours
```

---

#### 3. Tableau de bord KPI mensuel

Créer un template de reporting mensuel avec indicateurs visuels :

| Indicateur | Processus | Cible | Mois M-1 | Mois M | Tendance | Statut |
|-----------|-----------|-------|----------|--------|----------|--------|
| Satisfaction client | P01 | ≥ 85% | ___% | ___% | ↑↓→ | 🟢🟡🔴 |
| Taux transformation devis | P01 | ≥ 30% | ___% | ___% | ↑↓→ | 🟢🟡🔴 |
| Score moyen fournisseurs | P02 | ≥ 70/100 | ___/100 | ___/100 | ↑↓→ | 🟢🟡🔴 |
| Livraison à temps | P03 | ≥ 90% | ___% | ___% | ↑↓→ | 🟢🟡🔴 |
| Litiges transport | P03 | ≤ 2% | ___% | ___% | ↑↓→ | 🟢🟡🔴 |
| Taux NC | P04 | ≤ 5% | ___% | ___% | ↑↓→ | 🟢🟡🔴 |
| Délai clôture NC | P04 | ≤ 10j | ___j | ___j | ↑↓→ | 🟢🟡🔴 |
| Revue de direction | M1 | Oui | — | — | — | 🟢🔴 |

**Seuils** : 🟢 Cible atteinte | 🟡 Écart < 10% | 🔴 Écart > 10% ou cible non atteinte

---

#### 4. Plan de continuité d'activité (PCA)

En tant qu'entreprise légère, le risque de « personne clé » est maximal. Documenter :

| Élément | Détail à compléter |
|---------|-------------------|
| Accès aux systèmes critiques | Liste des accès FileMaker, email, cloud, WeChat, banque |
| Contacts fournisseurs | Liste avec contacts directs (nom, tel, email, WeChat) |
| Contacts clients | Liste avec contacts directs |
| Procédures d'urgence | Qui prend le relais en cas d'indisponibilité du dirigeant ? |
| Fournisseurs alternatifs | Au moins 1 fournisseur alternatif pré-qualifié par type de produit |
| Sauvegarde données | Stratégie de backup (fréquence, emplacement, test de restauration) |

---

### 2.2 AMÉLIORATIONS DE VALEUR MOYENNE

---

#### 5. Barème de notation fournisseur avec descripteurs

L'évaluation fournisseur utilise un score 0-10 sur 6 critères, mais sans descripteurs explicites. Proposition :

| Score | Niveau | Description opérationnelle |
|-------|--------|---------------------------|
| 9-10 | Excellent | Zéro NC, livraison anticipée ou à la date, communication proactive, suggestions d'amélioration |
| 7-8 | Bon | < 2% NC mineures, livraison à temps, bonne réactivité (< 24h), AQF respecté |
| 5-6 | Acceptable | 2-5% NC, retards occasionnels (< 1 semaine), réactivité correcte (24-48h) |
| 3-4 | Insuffisant | > 5% NC, retards fréquents, communication difficile, AQF partiellement respecté |
| 1-2 | Inacceptable | NC critiques, non-respect des délais, AQF non respecté, absence de communication |
| 0 | Rejet | Refus de coopérer, fraude, contrefaçon |

---

#### 6. Enrichissement de l'AQF avec clauses manquantes

L'Accord Qualité Fournisseur actuel est bien structuré mais pourrait être enrichi :

| Clause manquante | Détail |
|-----------------|--------|
| Propriété client (§8.5.3) | Protection des plans, moules et échantillons du client |
| Clause de confidentialité | NDA sur les données techniques, commerciales et clients |
| Conditions d'expédition | Exigences d'emballage, marquage, documents accompagnants |
| Gestion des changements | Obligation d'informer Plus Sàrl de tout changement (matières, procédé, personnel clé) |
| Substances interdites | Conformité REACH, RoHS si applicable |
| Force majeure | Clause standard de force majeure et obligations d'information |

---

#### 7. Templates pré-remplis et exemples

Améliorer l'utilisabilité des formulaires :
- Pré-remplir l'en-tête « Plus Sàrl » dans tous les templates
- Ajouter des catégories standard dans FM-P04-NC (ex. « Défaut matière », « Hors tolérance dimensionnelle », « Défaut visuel », « Défaut fonctionnel », « Erreur quantité », « Emballage défectueux »)
- Fournir un exemple rempli pour chaque template
- Standardiser le format de date (`AAAA-MM-JJ` partout)

---

### 2.3 AMÉLIORATIONS COSMÉTIQUES

| # | Amélioration | Impact |
|---|-------------|--------|
| 8 | Ajouter un MQ_01 « Introduction au SMQ » | Navigation — le MQ commence au ch. 2 |
| 9 | Créer un glossaire (IPC, DUPRO, PSI, AQF, NC, BL, CI, POD, NPS, RACI...) | Accessibilité |
| 10 | Standardiser le format de date `AAAA-MM-JJ` dans tous les templates | Cohérence |
| 11 | Ajouter un numéro de version + cartouche dans le footer de chaque fichier | Traçabilité |
| 12 | Corriger les liens cassés dans CHAIN-02, 03, 04 | Intégrité |
| 13 | Traduire ou normaliser les termes anglais (Loading Check, Skill Matrix, Proof of Delivery) | Cohérence linguistique |

---

## PARTIE 3 — PLAN D'ACTION PRIORISÉ

### Phase 1 — Avant audit de certification (CRITIQUE — 4-6 semaines)

| # | Action | Réf. | Responsable | Effort estimé |
|---|--------|------|-------------|---------------|
| 1 | Créer le domaine d'application + exclusion §8.3 | A, B | Direction | 1 jour |
| 2 | Ajouter cartouche d'approbation dans chaque document + cocher le registre | C | Rôle Gestion Doc. | 2 jours |
| 3 | Créer la matrice de compétences (Skill Matrix) | D | Direction | 3 jours |
| 4 | Remplir le programme d'audit interne avec dates et auditeurs | E | Rôle Qualité | 1 jour |
| 5 | Mettre à jour MQ_07 avec les outils réels (FileMaker, WeChat) | F | Direction | 0.5 jour |
| 6 | Aligner les objectifs de délai avec le PDF source | G | Direction | 0.5 jour |
| 7 | Documenter les actions en cours du PDF source | H | Direction | 0.5 jour |
| 8 | Compléter le registre des risques (6 risques manquants) | N | Direction | 1 jour |
| 9 | Documenter §8.5.3 propriété client, §8.5.4 préservation, §8.5.5 post-livraison | K, L, M | Rôle Qualité | 2 jours |
| 10 | Créer la matrice de traçabilité clause → document | Amél. 1 | Rôle Gestion Doc. | 1 jour |
| 11 | Corriger l'échelle NPS (0-10 ou renommer) | O | Rôle Commercial | 0.5 jour |
| 12 | Corriger les liens cassés dans CHAIN-02, 03, 04 | R | Rôle Gestion Doc. | 0.5 jour |

**Effort total Phase 1** : ~13 jours-homme

---

### Phase 2 — Renforcement du SMQ (IMPORTANT — 6-8 semaines)

| # | Action | Réf. | Responsable | Effort estimé |
|---|--------|------|-------------|---------------|
| 13 | Rédiger les 8 procédures opérationnelles prioritaires | P | Tous les rôles | 16 jours |
| 14 | Compléter CHAIN-02, CHAIN-03, CHAIN-04 | R | Rôle Commercial + Achats | 6 jours |
| 15 | Créer la matrice RACI | Q | Direction | 2 jours |
| 16 | Créer le barème de notation fournisseur détaillé | T | Rôle Qualité | 1 jour |
| 17 | Documenter le protocole de substitution des rôles | S | Direction | 1 jour |
| 18 | Ajouter les données baseline aux KPI | V | Direction | 2 jours |
| 19 | Enrichir l'AQF avec clauses manquantes | Amél. 6 | Rôle Achats | 2 jours |

**Effort total Phase 2** : ~30 jours-homme

---

### Phase 3 — Optimisation continue (SOUHAITABLE — au fil du temps)

| # | Action | Réf. | Responsable | Effort estimé |
|---|--------|------|-------------|---------------|
| 20 | Créer les arbres de décision | Amél. 2 | Rôle Qualité | 3 jours |
| 21 | Mettre en place le tableau de bord KPI mensuel | Amél. 3 | Direction | 2 jours |
| 22 | Rédiger le plan de continuité d'activité | Amél. 4 | Direction | 3 jours |
| 23 | Ajouter MQ_01 Introduction | Y | Rôle Gestion Doc. | 1 jour |
| 24 | Créer le glossaire | Z | Rôle Gestion Doc. | 1 jour |
| 25 | Templates pré-remplis + exemples | Amél. 7 | Rôle Gestion Doc. | 3 jours |
| 26 | Standardiser dates et footer dans tous les fichiers | X | Rôle Gestion Doc. | 1 jour |

**Effort total Phase 3** : ~14 jours-homme

---

## PARTIE 4 — POINTS FORTS DU DOSSIER (à préserver)

Le dossier v0.5 présente de nombreuses qualités qui constituent une base solide pour la certification :

1. **Architecture processus exemplaire** — 6 processus clairement définis (M1, P01-P04, S1) avec interactions documentées et diagrammes swimlane
2. **Chaîne processus innovante** — L'approche par 8 blocs modulaires (CH-BLOC) est élégante, scalable et bien adaptée aux 4 types de commande
3. **Manuel Qualité complet** — 9 chapitres couvrant les §4 à §10 de la norme, bien structurés et cohérents
4. **Rôles clairement séparés** — 6 rôles indépendants des personnes, facilitant la flexibilité organisationnelle
5. **Gestion fournisseur robuste** — Système d'évaluation multi-critères (6 critères pondérés, classification A/B/C) + AQF formalisé
6. **Templates opérationnels** — 8 formulaires prêts à l'emploi couvrant les principaux enregistrements
7. **Indicateurs mesurables** — 9 KPI avec cibles et fréquences de suivi dans MQ_09
8. **Cycle PDCA intégré** — Boucle d'amélioration continue visible dans MQ_10 et dans chaque processus
9. **Cohérence de la terminologie** — Utilisation homogène des termes dans l'ensemble du dossier
10. **Progression documentée** — L'évolution v0.1 → v0.2 → v0.3 → v0.4 → v0.5 montre une amélioration continue

---

## PARTIE 5 — TABLEAU RÉCAPITULATIF GLOBAL

| Réf | Manque | Clause ISO | Sévérité | Phase | Effort |
|-----|--------|-----------|----------|-------|--------|
| A | Domaine d'application | §4.3 | **Critique** | 1 | 1j |
| B | Exclusion §8.3 documentée | §4.3, §8.3 | **Critique** | 1 | incl. A |
| C | Approbation documents | §7.5.2 | **Critique** | 1 | 2j |
| D | Matrice de compétences | §7.2 | **Critique** | 1 | 3j |
| E | Programme audit planifié | §9.2 | **Critique** | 1 | 1j |
| F | Outils réels (FileMaker, WeChat) | §7.1, §7.4 | Haute | 1 | 0.5j |
| G | Objectifs délai spécifiques | §6.2 | Haute | 1 | 0.5j |
| H | Actions en cours du PDF | §10.2 | Haute | 1 | 0.5j |
| I | Contexte Chine vs Worldwide | §4.1 | Moyenne | 1 | 0.5j |
| J | AQF signés (Yuyao, Oukailuo) | §8.4 | Moyenne | 2 | 1j |
| K | Propriété client détaillée | §8.5.3 | Haute | 1 | 1j |
| L | Préservation | §8.5.4 | Haute | 1 | 0.5j |
| M | Activités post-livraison | §8.5.5 | Haute | 1 | 0.5j |
| N | Registre risques étendu | §6.1 | Haute | 1 | 1j |
| O | Échelle NPS | §9.1.2 | Basse | 1 | 0.5j |
| P | Procédures opérationnelles | §7.5, §8.1 | Haute | 2 | 16j |
| Q | Matrice RACI | §5.3 | Moyenne | 2 | 2j |
| R | CHAIN-02, 03, 04 + liens cassés | §8.1 | Moyenne | 2 | 6j |
| S | Protocole substitution rôles | §5.3 | Moyenne | 2 | 1j |
| T | Barème notation fournisseur | §8.4 | Basse | 2 | 1j |
| U | Cible taux réponse satisfaction | §9.1.2 | Basse | 3 | — |
| V | Données baseline KPI | §9.1 | Basse | 2 | 2j |
| W | Devise de référence | — | Basse | 3 | — |
| X | Format date cohérent | §7.5 | Basse | 3 | 1j |
| Y | MQ_01 Introduction | — | Basse | 3 | 1j |
| Z | Glossaire | — | Basse | 3 | 1j |

---

**Effort total estimé** : ~57 jours-homme (Phase 1: 13j + Phase 2: 30j + Phase 3: 14j)

---

*Revue complète réalisée le 2026-03-04*
*Dossier v0.5 — Plus Sàrl*
*Prochaine revue recommandée : après complétion Phase 1*
