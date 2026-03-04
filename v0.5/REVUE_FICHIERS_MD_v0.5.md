# REVUE DES FICHIERS .MD — Dossier v0.5

## Plus Sàrl — SMQ ISO 9001:2015

**Date de revue** : 2026-03-04
**Périmètre** : 35 fichiers .md du dossier v0.5 (9 MQ + 6 processus + 8 documents + 8 blocs + 4 chaînes)
**Méthode** : Relecture complète fichier par fichier, cross-référencement interne et vérification de cohérence

---

## TABLE DES MATIÈRES

1. [Synthèse globale](#1-synthèse-globale)
2. [Manuel Qualité (MQ_02 à MQ_10)](#2-manuel-qualité)
3. [Fiches Processus (M1, P01-P04, S1)](#3-fiches-processus)
4. [Documents Opérationnels (DOC_*)](#4-documents-opérationnels)
5. [Chaînes Processus (CHAIN-01 à 04 + 8 BLOCS)](#5-chaînes-processus)
6. [Problèmes transversaux](#6-problèmes-transversaux)
7. [Actions correctives par fichier](#7-actions-correctives-par-fichier)

---

## 1. SYNTHÈSE GLOBALE

### Constats principaux

| Catégorie | Verdict |
|-----------|---------|
| Qualité du français | Bon — professionnel, terminologie ISO correcte, pas de fautes significatives |
| Structure et cohérence interne | Correcte entre MQ et processus, mais incohérences MQ_06/MQ_09/MQ_10 sur les KPI/délais |
| Spécificité Plus Sàrl | **Faible** — les documents sont des templates génériques ; le contexte Chine/Europe est dilué |
| Liens et références croisées | **21 liens cassés** dans CHAIN-02/03/04 ; reste OK |
| Complétude ISO 9001:2015 | 9 clauses manquantes ou insuffisantes (voir détail ci-dessous) |
| Utilisabilité opérationnelle | Templates corrects mais pas prêts pour l'utilisation réelle sans adaptation |

### Clauses ISO manquantes ou insuffisantes dans les .md

| Clause | Exigence | Statut |
|--------|----------|--------|
| §4.3 | Domaine d'application du SMQ | **Absent** (pas de MQ_01) |
| §4.4 | SMQ et ses processus (carte d'interactions formelle) | **Absent** |
| §7.1.5 | Ressources de surveillance et mesure (étalonnage) | **Absent** |
| §7.1.6 | Connaissances organisationnelles | **Absent** |
| §8.3 | Conception & développement (ou exclusion formelle) | **Ni traité ni exclu** |
| §8.5.2 | Identification et traçabilité | **Absent** |
| §8.5.3 | Propriété du client | **1 ligne placeholder « si applicable »** |
| §8.5.4 | Préservation | **Absent** |
| §8.5.5 | Activités après livraison | **Absent** |

---

## 2. MANUEL QUALITÉ

### MQ_02_Activites.md

**Problèmes identifiés :**

- **Géographie volontairement vague** : « partenaires situés dans le monde entier » alors que l'activité est centrée sur la Chine. L'auditeur trouvera cela évasif. Reformuler : « principalement des partenaires industriels en Chine, avec capacité de sourcing étendue ».
- **« Portail client (si applicable) »** (ligne 43) — placeholder non résolu. Dire clairement si le portail existe ou non.
- **Tableau des processus incomplet** (lignes 20-25) : seuls 4 processus opérationnels listés. M1 (Leadership) et S1 (Gestion Documentaire) sont absents.
- **Référence ISO douteuse** : « Réf. ISO 9001:2015 — §4.2, §8.2 » — la clause 4.2 concerne les parties intéressées, pas les activités.

### MQ_03_Support_SMQ.md

**Problèmes identifiés :**

- **Titre trompeur** : « Support du SMQ » couvre en réalité les rôles et responsabilités (clause 5.3), pas le Support (clause 7). Confusion avec MQ_07.
- **Diagramme ASCII incorrect** : montre la Qualité en aval de la Logistique, alors que le contrôle qualité se fait AVANT l'expédition (confirmé dans MQ_08).
- **Pas de suppléance définie** : qui remplace qui en cas d'absence ? Critique pour une PME.
- **Pas de mention du cumul des rôles** : pour une petite structure, il faut expliciter qu'une personne peut tenir plusieurs rôles.
- **Pas de Responsable SMQ identifié** : même si ISO 9001:2015 a supprimé le « représentant de la direction », quelqu'un doit assurer la maintenance du SMQ.

### MQ_04_Contexte.md

**Problèmes identifiés :**

- **SWOT vague** : « Réseau de fournisseurs qualifiés dans le monde entier » — devrait mentionner la Chine explicitement.
- **Parties intéressées incomplètes** : manquent les banques/institutions financières (lettres de crédit), les assureurs (cargo), les autorités douanières suisses (OFDF/BAZG).
- **§4.3 Domaine d'application — ABSENT** : c'est une exigence normative. Doit déclarer le périmètre, les activités couvertes et les exclusions.
- **§4.4 SMQ et processus — ABSENT** : pas de carte formelle des interactions entre processus avec entrées/sorties/ressources.
- **Aucune réglementation spécifique mentionnée** : CE, REACH, RoHS, droit suisse (CO, LPD), régulations chinoises d'export.

### MQ_05_Leadership.md

**Problèmes identifiés :**

- **Politique qualité trop générique** : pourrait s'appliquer à n'importe quelle entreprise. Pas de mention du modèle d'affaires (production externalisée, sourcing), pas d'aspect interculturel.
- **Engagement manquant** : la politique ne contient pas l'engagement explicite de « satisfaire aux exigences applicables » (exigé par §5.2.1c).
- **Accessibilité** : « Affichée et accessible à tous les collaborateurs » — pour du personnel en déplacement international, l'accès digital devrait être prioritaire.
- **Skill Matrix** : référencée mais inexistante dans le dossier.

### MQ_06_Planification.md

**Problèmes identifiés :**

- **Échelle de risques incohérente** : les risques utilisent Élevé/Moyen/Faible, mais l'opportunité « Digitalisation » utilise « Positif/Élevé ». Pas la même échelle.
- **Pas de méthodologie de scoring** : les termes Élevé/Moyen/Faible ne sont pas définis.
- **Objectif #6 incohérent** : « Nombre d'actions correctives clôturées : 100% dans les délais ». Le nom dit « nombre » mais la cible est un « pourcentage ».
- **Conflit de délais avec MQ_10** : MQ_06 dit « délai moyen de traitement ≤ 10 jours » pour les réclamations, MQ_10 dit « Critique : Immédiat, Majeure : ≤ 5 jours ouvrés ».
- **Pas de valeurs de référence (baseline)** : les cibles (85%, 90%, 5%) n'ont aucune donnée de départ.
- **Grammaire** (ligne 8-9) : « Les attentes des parties intéressées » devrait être « Aux attentes des parties intéressées » pour le parallélisme avec « à son contexte ».

### MQ_07_Support.md

**Problèmes identifiés :**

- **Inspecteurs externes non qualifiés** : « inspecteurs locaux qualifiés » sans critères de qualification, sans supervision, sans procédure.
- **§7.1.5 — Ressources de surveillance ABSENT** : pas de mention de l'étalonnage ou vérification des instruments de mesure.
- **§7.1.6 — Connaissances organisationnelles ABSENT** : pas de gestion des connaissances (retours d'expérience, intelligence fournisseur).
- **Durée de conservation** : « durée de conservation définie par type de document » — placeholder non résolu, pas de durées concrètes.
- **Outils génériques** : « ERP, messagerie, outils de suivi » au lieu de FileMaker, WeChat, email (comme dans le PDF source).
- **Compétences linguistiques absentes** : français, anglais, chinois sont essentiels au métier mais non mentionnés.

### MQ_08_Realisation.md

**Problèmes identifiés :**

- **§8.3 — Conception & Développement** : le chapitre saute de §8.2.3 à §8.4 sans mention. L'exclusion doit être formellement documentée et justifiée.
- **§8.5.2 — Identification et traçabilité ABSENT** : aucune section sur le suivi des lots, numéros de production, certificats de conformité.
- **§8.5.3 — Propriété client** : « Gérer la propriété du client (si applicable) » — placeholder. Doit être traité formellement (plans, moules, échantillons).
- **§8.5.4 — Préservation ABSENT** : emballage, protection pendant transport, conditions de stockage.
- **§8.5.5 — Activités après livraison ABSENT** : garanties, support post-livraison, retours.
- **Pondération « Localisation : Faible »** : contradictoire pour un modèle basé sur l'inspection en usine.
- **Pas de mention des Incoterms** : fondamental pour le commerce international.
- **Pas de protection de la propriété intellectuelle** : critique pour la transmission de plans clients à des fabricants chinois.

### MQ_09_Evaluation.md

**Problèmes identifiés :**

- **Duplication des KPI avec MQ_06** : MQ_06 a 6 objectifs, MQ_09 a 9 KPI. Les 3 supplémentaires (taux transformation devis, nombre fournisseurs qualifiés, taux litiges transport) n'apparaissent qu'ici. Risque de divergence à la maintenance.
- **Audit : indépendance insuffisamment traitée** : pour une petite entreprise, l'audit du processus P04 (Qualité) par le Rôle Qualité est impossible. La règle « P04 doit être audité par un auditeur externe » devrait être explicite.
- **Éléments d'entrée de la revue de direction incomplets** : il manque « performance des prestataires externes » (exigé par §9.3.2 c4) et « résultats de la mise à jour de l'évaluation des risques ».

### MQ_10_Amelioration.md

**Problèmes identifiés :**

- **Conflit de délais avec MQ_06** : Observation = « Prochaine revue » = jusqu'à 6 mois. Trop long.
- **Cycle PDCA générique** : contenu de manuel scolaire. Devrait être contextualisé à Plus Sàrl.
- **Pas de lien avec le registre des risques** : l'amélioration continue devrait être connectée à la pensée basée sur le risque (§6.1).
- **Ambiguïté linguistique** : « Les suggestions des collaborateurs à tous les rôles » — reformuler : « Les suggestions des collaborateurs, quel que soit leur rôle ».

---

## 3. FICHES PROCESSUS

### M1_Leadership.md

- **Vague sur le contexte Plus Sàrl** : aucune référence au métier de coordination industrielle internationale.
- **Pas de cadre réglementaire** : droit suisse, réglementations EU, exigences chinoises — absents.
- **Pas de méthodologie de gestion des risques** : activité #5 dit « Analyser les risques » sans préciser comment.
- **Document mince** : lit plus comme un template que comme un processus réellement documenté.
- **Références croisées OK** : tous les liens vers MQ_05, MQ_06, MQ_07, DOC_Revue_Direction sont valides.

### P01_Commercial.md

- **Activités #1 et #2 sans documents associés** (marqué « --- ») : la réception des demandes client et l'analyse de faisabilité n'ont aucun enregistrement associé. C'est une lacune pour §8.2.3 (revue des exigences).
- **§8.2.3 — Revue de contrat ABSENTE** : avant d'accepter une commande, Plus Sàrl doit vérifier sa capacité à satisfaire les exigences. Pas de « revue des exigences » formelle.
- **Pas de mention des Incoterms** dans le processus commercial, alors que P03 y fait référence.
- **Pas de gestion des devises** : EUR/CHF/CNY/USD — impact direct sur les offres et marges.
- **Swimlane incohérent** : la flèche Qualité → Commercial pour les réclamations semble inversée.
- **Pas de protection de la PI** : transmission de spécifications clients à des fabricants chinois non traitée.

### P02_Achats_Sous_traitance.md

- **Sous-traitance non décrite** : le titre dit « Achats & Sous-traitance » mais le contenu ne traite que des achats. Si des sous-traitants existent (inspecteurs tiers, labo d'essai, transitaires), ils doivent être couverts.
- **Séquence AQF incohérente** : l'AQF est étape 5/6 dans la qualification (lignes 58-64) mais étape 3/8 dans le tableau des activités. Contradictoire.
- **Classification A/B/C sans critères** : mentionnée à l'activité #8 mais jamais définie dans le document.
- **Délai de qualification 30 jours irréaliste** : qualifier un fabricant chinois en 30 jours (avec évaluation d'échantillons et audit sur site) est très ambitieux. 60-90 jours serait plus réaliste.
- **Pas de mention des inspections coordonnées en Chine** : qui inspecte ? Inspecteurs internes ? Tiers (Bureau Veritas, SGS, Intertek) ?
- **Pas de protocole de communication avec les fournisseurs chinois** : langue, outils (WeChat), fuseaux horaires.
- **Pas de stratégie fournisseur alternatif** documentée.

### P03_Logistique_Livraison.md

- **Le processus le plus faible du dossier** pour une entreprise dont le cœur de métier est la coordination logistique internationale.
- **Pas de procédures douanières** : déclarations import/export, classifications tarifaires (codes SH), origine préférentielle, autorités suisses (OFDF/BAZG), exigences douanières EU — totalement absentes.
- **Pas de mention des Incoterms spécifiques** utilisés ni de leur impact sur les responsabilités.
- **Pas d'assurance transport** : couverture, responsabilité, procédures de réclamation.
- **Pas de documents d'expédition spécifiés** : packing list, facture commerciale, certificat d'origine, EUR.1.
- **« Loading check »** (ligne 78) : anglicisme non traduit. Utiliser « Vérification de chargement (loading check) ».
- **Indicateur « Délai moyen de transit — Selon incoterm »** : c'est un placeholder, pas une cible. Faut des valeurs par route.
- **Pas de panel de transporteurs qualifiés** : aucun critère de qualification, contrairement à P02 pour les fournisseurs.
- **Interaction S1 manquante** : P03 génère de nombreux documents (BL, AWB, CMR, docs douaniers) mais ne référence pas S1.

### P04_Controle_Qualite.md

- **Mélange opérationnel/management** : le processus contient l'audit interne (activité #8) et l'amélioration continue (activité #9), qui relèvent normalement du management/mesure (§9.2, §10.1).
- **« Taux de NC ≤ 5% »** : 5% de quoi ? Lots inspectés ? Commandes totales ? Pièces individuelles ? Ambigu.
- **Catégorie « Observation »** : n'est pas une vraie non-conformité. Confusion entre observations d'audit et NC produit.
- **Qui inspecte physiquement ?** La question fondamentale n'est pas traitée : inspecteurs internes en déplacement en Chine ou sociétés d'inspection tierces ?
- **AQL mentionné** (« Selon AQL », « niveau II ») mais sans préciser la norme (ISO 2859-1) ni les critères d'acceptation/rejet.
- **IPC, DUPRO, PSI** : jamais formellement définis. IPC = Initial Production Check, DUPRO = During Production Inspection, PSI = Pre-Shipment Inspection.
- **§7.1.5 et §8.5.2 manquants** : pas de référence à l'étalonnage ni à la traçabilité.

### S1_Gestion_Documentaire.md

- **« Rôle Gestion Documentaire »** comme pilote : implique un poste dédié. Pour une PME, expliciter que c'est probablement le même que « Rôle Qualité ».
- **Durées de conservation potentiellement non conformes** : « Contrats et commandes : 10 ans » est correct (CO art. 958f), mais « 3-5 ans » pour d'autres documents pourrait violer l'obligation légale suisse de 10 ans.
- **Pas de mention du numérique vs. physique** : quel outil ? SharePoint, Google Drive, serveur local ?
- **Pas de sauvegarde ni reprise d'activité** pour les documents électroniques.
- **Pas de contrôle d'accès ni confidentialité** : crucial avec des informations clients transmises à des fournisseurs chinois.
- **Pas de gestion des documents externes** : spécifications clients, certifications fournisseurs, normes.
- **Pas de gestion multilingue** : les documents existent en français, anglais, potentiellement chinois.
- **Codification incomplète** : manquent les codes pour politiques, organigrammes, registres de risques.

---

## 4. DOCUMENTS OPÉRATIONNELS

### DOC_Accord_Qualite_Fournisseur.md

- **Signataire inadéquat** : « Rôle Achats » n'a peut-être pas l'autorité juridique pour signer un accord. Devrait être « Direction ».
- **Conflit de délais** : §4 dit 48h pour plan de correction, §5 dit 24h ouvrées pour réponse.
- **Pas de clause PI** : protection de la propriété intellectuelle absente — critique pour des fabricants chinois.
- **Pas de clause de force majeure** : standard dans les accords internationaux.
- **Pas de droit applicable ni juridiction** : droit suisse ? Chinois ? Arbitrage ?
- **Langue de communication vide** : champ fondamental non rempli.
- **Cases à cocher §3** : mélanger des checkboxes (optionnelles) avec des engagements juridiques (obligatoires) est maladroit.
- **Placeholder FM-P02-AQF-XXX** : non résolu.

### DOC_Audit_Interne.md

- **Checklist trop maigre** : 6 questions pré-remplies + 2 vides. Insuffisant pour un audit réel ISO 9001.
- **Pas de statut « En cours » ni « Clôturé »** dans le plan d'actions (seulement « Ouvert »).
- **Pas d'audit fournisseur distant** : pour Plus Sàrl, les audits des fournisseurs chinois sont plus critiques que les audits internes.
- **Placeholder FM-P04-AUD-XXXX** : non résolu.
- **Pas de référence croisée** vers FM-P04-NC pour les constats donnant lieu à une fiche NC.

### DOC_Evaluation_Fournisseur.md

- **Pas de barème de conversion** : comment transformer un « Taux de NC » en note /10 ? Aucun guide.
- **Pas de critères spécifiques à la Chine** : capacité linguistique, qualité de la documentation d'export, certifications usine.
- **Compétitivité pondérée à 10%** : très faible pour une entreprise de sourcing.
- **Pas de données d'inspection (IPC/DUPRO/PSI)** en entrée, alors que c'est le cœur du modèle qualité.
- **Placeholder FM-P02-EVAL-XXX** : non résolu.

### DOC_Gestion_Documentaire.md

- **MQ_01 absent** du registre : le manuel commence à MQ_02 sans explication.
- **Incohérence de version** : MQ = v0.5 (brouillon) mais formulaires = v1.0 (publié). Contradictoire.
- **Un seul statut** « En vigueur » avec case à cocher : il faut aussi « Brouillon », « Obsolète », « En révision ».
- **Aucun formulaire pour P03 (Logistique)** : un processus cœur de métier sans aucun template.
- **Pas de procédure de maîtrise documentaire** : c'est un registre, pas une procédure. §7.5 exige la maîtrise des informations documentées.
- **« Serveur / Cloud »** comme lieu de stockage : trop vague.

### DOC_Non_Conformite.md

- **Le meilleur template du dossier** : flux complet détection → analyse → correction → vérification.
- **Types IPC/DUPRO/PSI listés** en §1 : bon, spécifique à Plus Sàrl.
- **Manque un champ localisation géographique** : usine, port, entrepôt client.
- **Manque un champ coût de non-qualité** : reprise, remplacement, expédition, pénalités.
- **Pas de procédure d'escalade** : à quel moment une NC déclenche un déclassement fournisseur ?
- **Champ « Preuves »** insuffisant : une seule ligne pour documenter des défauts sur des produits manufacturés.
- **Placeholder FM-P04-NC-XXXX** : non résolu.

### DOC_Objectifs_Qualite.md

- **Objectif #6 = 100%** : irréaliste. La pratique est 90-95%.
- **Colonne « Statut »** avec une seule case sans libellé : faut « Atteint / Non atteint / En cours ».
- **Pas d'objectifs S1 ni M1** : ISO exige des objectifs « pour les fonctions, niveaux et processus pertinents ».
- **Pas de méthode de mesure** : qui collecte, comment, à partir de quelle source ?
- **Pas de baseline** : impossible de juger la pertinence des cibles sans état initial.
- **Placeholder 20____** : non résolu.

### DOC_Revue_Direction.md

- **Bon template, conforme §9.3** : couvre les éléments d'entrée et de sortie requis.
- **Incohérence KPI** : §2.4 mentionne « Taux transformation ≥ 30% » pour P01, absent de DOC_Objectifs_Qualite.
- **Pas de revue du contexte externe** : conditions de marché, changements réglementaires, paysage manufacturier chinois — exigé par §9.3.2.
- **Section Ressources (§2.7) trop succincte** : une seule ligne pour une entreprise opérant sur 3 continents.
- **Pas de référence aux documents d'entrée** : FM-P04-AUD, FM-P01-SAT, FM-M1-OBJ devraient être listés.
- **Placeholder FM-M1-RD-XXXX** : non résolu.

### DOC_Satisfaction_Client.md

- **Erreur méthodologique NPS** : question 14 utilise une échelle 1-5, le NPS standard est 0-10. Soit corriger l'échelle, soit retirer l'appellation NPS.
- **Pas de formule de conversion** : comment passer de notes /5 à un « Score satisfaction (%) » ?
- **Questionnaire trop générique** : pas de questions sur la visibilité de la chaîne d'approvisionnement, la qualité des inspections en usine, la gestion douanière.
- **Pas de version multilingue** : un questionnaire français-only n'est pas utilisable avec des clients allemands, italiens ou anglais.
- **Cible de 85% absente** du document lui-même (seulement dans DOC_Revue_Direction).
- **Placeholder FM-P01-SAT-XXX** : non résolu.

---

## 5. CHAÎNES PROCESSUS

### 21 liens cassés (CRITIQUE)

CHAIN-02, CHAIN-03 et CHAIN-04 contiennent chacun **7 liens cassés** vers des fichiers BLOC qui n'existent pas :

| Lien dans le fichier | Fichier réel |
|---------------------|-------------|
| CH-BLOC-002_Revue_Planification.md | CH-BLOC-002_Fiche_Commande.md |
| CH-BLOC-003_Lancement_Production.md | CH-BLOC-003_Fiche_Transport.md |
| CH-BLOC-004_Suivi_Production.md | CH-BLOC-004_Etude_Technique.md |
| CH-BLOC-005_Preparation_Expedition.md | CH-BLOC-005_Validation_Commande.md |
| CH-BLOC-006_Suivi_Livraison.md | CH-BLOC-006_Production_Qualite.md |
| CH-BLOC-007_Controle_Qualite.md | CH-BLOC-007_Livraison_Douane.md |
| CH-BLOC-008_Cloture_Feedback.md | CH-BLOC-008_Acceptation_Marchandise.md |

Seul le lien vers CH-BLOC-001_Reception_Commande.md est correct.

### Contradiction structurelle entre CHAIN-01 et CHAIN-02/03/04

Les 8 fichiers BLOC sont écrits pour le flux CHAIN-01 (produit existant). Les CHAIN-02/03/04 définissent un flux **complètement différent** avec des noms de blocs, des rôles et une séquence différents :

| Bloc | CHAIN-01 / Fichiers BLOC | CHAIN-02/03/04 |
|------|--------------------------|----------------|
| BLOC 2 | Fiche de Commande (SALES) | Revue & Planification |
| BLOC 3 | Fiche de Transport (DELIVERY) | Lancement Production |
| BLOC 4 | Étude Technique (MANUFACTURE) | Suivi Production |
| BLOC 5 | Validation Commande (SALES) | Préparation Expédition |
| BLOC 6 | Production & Qualité (MANUF+QUAL) | Suivi Livraison |
| BLOC 7 | Livraison & Douane (DELIV+SALES) | Contrôle Qualité |
| BLOC 8 | Acceptation Marchandise (QUAL+SALES) | Clôture & Feedback |

C'est une **incohérence fondamentale** : les fichiers BLOC prétendent être « applicables » aux 4 types de commande mais sont écrits exclusivement pour CHAIN-01.

### CHAIN-02, CHAIN-03, CHAIN-04 — Incomplets

- Les 3 fichiers ont le statut « À compléter ».
- Phrase placeholder : « Les fiches détaillées spécifiques à ce type de commande seront complétées ultérieurement. »
- Pas de KPI, pas de source documentaire, pas d'auteur du document source.

### CHAIN-01 et les 8 BLOCS — Cohérents entre eux

CHAIN-01 est complet et tous les liens fonctionnent. Les 8 BLOCS sont cohérents entre eux avec des interactions correctes : BLOC 1 → 2 → 3+4 → 5+6 → 7 → 8.

### Autres problèmes dans les BLOCS

- **Pas de gestion des exceptions** : fournisseur échoue au contrôle qualité (BLOC 6), client refuse l'AR (BLOC 5), blocage douanier (BLOC 7), non-paiement (BLOC 8) — non documentés.
- **Pas de références documentaires** : « Fiche de commande », « Bulletin de livraison », « Facture commerciale » sans codes de document ni emplacements de template.
- **Anglicismes** : « RFQ » (BLOC 1, non développé), « tracking » (BLOC 7), « samples » (CHAIN-03, devrait être « échantillons »).
- **PSI** : mentionné comme KPI dans CHAIN-01 mais jamais détaillé dans aucun BLOC.

---

## 6. PROBLÈMES TRANSVERSAUX

### A. Contexte Plus Sàrl systématiquement dilué

Aucun fichier ne mentionne :
- Le nom « Plus Sàrl » ou sa forme juridique (Sàrl au sens du CO suisse)
- La Chine comme zone géographique principale de sourcing
- FileMaker comme outil central (remplacé par « ERP » générique)
- WeChat comme canal de communication (remplacé par « messagerie »)
- Les Incoterms, le droit suisse applicable, les réglementations EU (CE, REACH, RoHS)
- Les compétences linguistiques requises (FR, EN, CN)

### B. Aucun formulaire pour P03 (Logistique)

Le registre DOC_Gestion_Documentaire ne liste **aucun template pour P03**, alors que c'est un processus cœur de métier.

### C. Placeholders non résolus dans tous les documents

Tous les formulaires utilisent des codes avec XXX/XXXX (FM-P02-AQF-XXX, FM-P04-NC-XXXX, etc.). Il n'existe **aucune convention de numérotation** documentée.

### D. Incohérence de version

- Manuel Qualité = v0.5 (brouillon)
- Formulaires = v1.0 (publié)
- Si le SMQ est en v0.5, les formulaires ne devraient pas être en v1.0.

### E. « si applicable » — à résoudre

Apparaît dans MQ_02 (portail client) et MQ_08 (propriété client). Doit être remplacé par une affirmation ou négation claire.

### F. Processus manquants dans la cartographie

Le SMQ n'a que 6 processus (M1, P01-P04, S1). Il manque :
- S2 — Ressources Humaines / Compétences (§7.2)
- S3 — Infrastructure et Environnement de travail (§7.1.3, §7.1.4)

---

## 7. ACTIONS CORRECTIVES PAR FICHIER

### Priorité 1 — Critique (bloquant certification)

| Fichier | Action |
|---------|--------|
| **Créer MQ_01** | Domaine d'application (§4.3), exclusion §8.3 justifiée, carte des processus (§4.4), termes/définitions |
| **MQ_08** | Ajouter §8.3 (exclusion formelle), §8.5.2, §8.5.3 (complet), §8.5.4, §8.5.5 |
| **MQ_07** | Ajouter §7.1.5 (étalonnage), §7.1.6 (connaissances), remplacer termes génériques par outils réels |
| **MQ_06** | Harmoniser les délais avec MQ_10, définir méthodologie de scoring des risques, ajouter baselines |
| **CHAIN-02/03/04** | Corriger les 21 liens cassés, résoudre la contradiction structurelle avec les BLOCS |
| **DOC_Gestion_Documentaire** | Ajouter une procédure de maîtrise documentaire (pas juste un registre) |

### Priorité 2 — Haute (attendu par l'auditeur)

| Fichier | Action |
|---------|--------|
| **MQ_04** | Ajouter parties intéressées manquantes (banques, assureurs, douanes), mentionner la Chine |
| **MQ_05** | Compléter la politique qualité (engagement §5.2.1c, spécificité métier) |
| **MQ_09** | Harmoniser KPI avec MQ_06, expliciter règle d'indépendance audit P04 |
| **P01** | Ajouter revue de contrat (§8.2.3), documents associés aux activités 1 et 2 |
| **P03** | Refonte complète : douanes, Incoterms, assurance, documents d'expédition, panel transporteurs |
| **P04** | Définir qui inspecte (interne/tiers), développer IPC/DUPRO/PSI, ajouter §7.1.5, §8.5.2 |
| **DOC_Accord_QF** | Ajouter clause PI, force majeure, droit applicable, signataire Direction |
| **DOC_Satisfaction** | Corriger échelle NPS (0-10), ajouter formule de conversion, version multilingue |
| **Tous les templates** | Résoudre les placeholders XXX/XXXX, créer convention de numérotation |

### Priorité 3 — Moyenne (qualité du SMQ)

| Fichier | Action |
|---------|--------|
| **MQ_02** | Préciser la géographie (Chine), supprimer « si applicable », compléter le tableau des processus |
| **MQ_03** | Corriger le diagramme ASCII, ajouter suppléance, cumul de rôles, Responsable SMQ |
| **MQ_10** | Contextualiser le PDCA, lier au registre des risques, corriger l'ambiguïté linguistique |
| **P02** | Traiter la sous-traitance, corriger séquence AQF, critères A/B/C, délai qualification réaliste |
| **S1** | Vérifier conformité durées de conservation avec CO suisse, ajouter gestion numérique/accès |
| **DOC_Audit** | Enrichir la checklist (6 questions insuffisant), ajouter statuts « En cours/Clôturé » |
| **DOC_Evaluation** | Ajouter barème de conversion, critères spécifiques Chine, données IPC/DUPRO/PSI |
| **DOC_Objectifs** | Réduire objectif #6 à 95%, ajouter objectifs S1/M1, ajouter méthode de mesure |
| **Tous les MQ** | Ajouter cartouche d'approbation (date, version, approbateur, historique de révision) |
| **Tous les BLOCS** | Ajouter gestion des exceptions, références documentaires, développer acronymes |

---

*Revue réalisée le 2026-03-04*
*35 fichiers .md analysés — Dossier v0.5 — Plus Sàrl*
