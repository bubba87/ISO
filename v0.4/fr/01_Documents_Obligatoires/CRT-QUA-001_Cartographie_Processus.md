# Cartographie des Processus

| | |
|---|---|
| **Référence** | CRT-QUA-001 |
| **Version** | 0.4 |
| **Date de création** | 10/02/2026 |
| **Date de révision** | 21/02/2026 |
| **Rédigé par** | Roxane Wicky |
| **Approuvé par** | Roxane Wicky |

> **Légende :** 🔴 [À REMPLIR] = obligatoire, manquant | 🟡 [RECOMMANDÉ] = recommandé | 🟢 = déjà rempli | 🔵 [À VÉRIFIER] = à confirmer

---

## 1. Vue d'ensemble des processus

### Contexte

Plus Sarl est spécialisée dans la coordination industrielle entre des clients européens et des partenaires de fabrication chinois. L'entreprise n'exerce aucune activité de conception (clause 8.3 de la norme ISO 9001:2015 exclue du domaine d'application). Les conceptions et la propriété intellectuelle appartiennent aux clients. L'activité couvre la coordination commerciale, les achats et la sous-traitance auprès de partenaires chinois (Yuyao Mould Factory et **Whang**, Yuyao), l'organisation logistique internationale et le contrôle qualité.

La certification ISO 9001:2015 est visée auprès de l'organisme **SQS**. 🟢

### Représentation de la cartographie

```
+=========================================================================+
|                    PROCESSUS DE MANAGEMENT                               |
|  +-------------------+  +-------------------+  +---------------------+  |
|  | M1 - Leadership   |  | M2 - Amélioration |  | M3 - Revue de      |  |
|  | et stratégie      |  | continue          |  | direction           |  |
|  +-------------------+  +-------------------+  +---------------------+  |
+=========================================================================+
                                    |
  EXIGENCES                         v                           SATISFACTION
  CLIENTS    +====================================================+  CLIENTS
  ---------> |              PROCESSUS OPERATIONNELS                | -------->
             |                                                      |
             |  +----------+  +----------+  +----------+  +------+  |
             |  | O1       |  | O2       |  | O3       |  | O4   |  |
             |  | Commer-  |->| Achats & |->| Logis-   |->| Con- |  |
             |  | cial     |  | Sous-    |  | tique &  |  | trole|  |
             |  |          |  | traitance|  | Livraison|  | Qual.|  |
             |  +----------+  +----------+  +----------+  +------+  |
             +====================================================+
                                    |
+=========================================================================+
|                    PROCESSUS SUPPORT                                      |
|  +-------------------+  +-------------------+  +---------------------+  |
|  | S1 - Gestion      |  | S2 - Gestion des  |  | S3 - Gestion des   |  |
|  | documentaire       |  | compétences et    |  | ressources et       |  |
|  | (FileMaker, emails)|  | formations        |  | infrastructure      |  |
|  +-------------------+  +-------------------+  +---------------------+  |
+=========================================================================+
```

**Note :** La clause 8.3 (Conception et développement) est exclue du domaine d'application. Les conceptions sont la propriété des clients. Plus Sarl intervient en tant que coordinateur industriel et n'exerce aucune activité de conception.

---

## 2. Liste des processus

### Processus de management

| Code | Processus | Pilote | Objectif | Document(s) associé(s) |
|---|---|---|---|---|
| M1 | Leadership et stratégie | Roxane Wicky (Gérante) | Définir la politique qualité, les objectifs stratégiques, attribuer les responsabilités, orienter l'entreprise et **planifier les modifications** (clause 6.3 — analyse d'impact, validation, mise en œuvre contrôlée) | **M1-DIR-001**, POL-QUA-001, CTX-QUA-001 (section 6) 🟢 |
| M2 | Amélioration continue | Roxane Wicky (Gérante) | Piloter l'amélioration du SMQ (non-conformités, actions correctives, indicateurs). **Revue de l'efficacité des modifications** lors de la revue de direction | PRO-NCF-001, PRO-ACR-001 |
| M3 | Revue de direction | Roxane Wicky (Gérante) | Évaluer les performances du SMQ et décider des actions d'amélioration | FOR-RDR-001 |

### Processus opérationnels

| Code | Processus | Pilote | Objectif | Document(s) associé(s) |
|---|---|---|---|---|
| O1 | Commercial | Roxane Wicky (Gérante) | Gérer les relations clients (~10 clients actifs), analyser les besoins, déterminer les exigences applicables (6 types, clause 8.2), réaliser la revue de commande, possibilité de refuser une commande hors domaine (clause 8.1), suivre les commandes dans FileMaker | CTX-QUA-001 (sections 1.2, 1.3), FIC-PRO-001 🟢 |
| O2 | Achats et sous-traitance | Roxane Wicky (Gérante) | Coordonner les partenaires chinois (Yuyao Mould Factory et **Whang**), sélection sur 7 critères et évaluation sur 4 indicateurs (clause 8.4), valider les nouveaux outillages avant série, créer les fiches de production FileMaker, suivre la fabrication externalisée (4 moyens de conformité, clause 8.5), assurer la confidentialité de la propriété intellectuelle 🟢 | PRO-ACH-001, FIC-PRO-001 |
| O3 | Logistique et livraison | Roxane Wicky (Gérante) | Créer les fiches de livraison FileMaker, organiser le transport international, gérer les documents douaniers, assurer le suivi jusqu'à livraison 🟢 | **PRO-LOG-001**, **FIC-PRO-002** 🟢 |
| O4 | Contrôle qualité | Roxane Wicky (Gérante) | Vérifier la conformité des pièces avant expédition, libération formalisée sur 3 critères (CQ fabricant, confirmation commande, photos — clause 8.6), gérer les NC et actions correctives selon processus en 4 étapes (clause 8.7), registre NC dans FileMaker 🔵 [À VÉRIFIER — registre à mettre en place], analyser les retours clients | PRO-NCF-001, PRO-ACR-001, FOR-CTR-001 |

### Processus support

| Code | Processus | Pilote | Objectif | Document(s) associé(s) |
|---|---|---|---|---|
| S1 | Gestion documentaire | Roxane Wicky (Gérante) | Maîtriser les documents et enregistrements du SMQ (FileMaker, emails, WeChat). Maîtrise des informations documentées selon clause 7.5 (accessibilité, lisibilité, conservation, protection). Mesures de confidentialité des données. Assurer la traçabilité et alimenter l'amélioration continue. Sauvegarde cloud chez le fournisseur 🟢 | PRO-DOC-001 |
| S2 | Compétences, formations et sensibilisation | Roxane Wicky (Gérante) | Maintenir et développer les compétences nécessaires à la coordination industrielle. Compétences gérante (7 domaines), extension aux fournisseurs (évaluation continue). Sensibilisation au SMQ (politique, objectifs, satisfaction client). Communication en anglais 🟢 | FOR-CMP-001 🟢 |
| S3 | Ressources et infrastructure | Roxane Wicky (Gérante) | Gérer les ressources humaines, matérielles, numériques et externes. Infrastructures (FileMaker, email, WeChat, cloud). Environnement de travail (confidentialité, fiabilité, réactivité). Ressources externes (Yuyao, Whang, transitaires). Comptabilité via fiduciaire Paradiso 🟢 | CTX-QUA-001 (section 7) 🟢 |

---

## 3. Interactions entre processus

### Matrice d'interaction

| De / Vers | O1 Commercial | O2 Achats/Sous-traitance | O3 Logistique/Livraison | O4 Contrôle qualité |
|---|---|---|---|---|
| **O1 Commercial** | - | Spécifications client, cahier des charges, plans, délais | Délai de livraison promis au client | Exigences qualité client |
| **O2 Achats/Sous-traitance** | Délai de fabrication, retour faisabilité, prix | - | Produits prêts à expédier, documents d'exportation | Rapports d'inspection, produits à contrôler |
| **O3 Logistique/Livraison** | Confirmation de livraison, suivi transport | Coordination dates d'expédition | - | Documents de transport, avis de réception |
| **O4 Contrôle qualité** | Information sur NC, retour satisfaction | Retour NC fabrication, demande de remplacement | Retour NC transport/livraison | - |

### Flux principal (de la demande client à la livraison)

```
 1. RÉCEPTION DE LA DEMANDE CLIENT (O1 - Commercial)
    Demande reçue par e-mail (commande, devis, modification, réclamation)
    ou par téléphone en cas d'urgence
            |
            v
 2. ANALYSE PRÉALABLE ET REVUE DE COMMANDE (O1/O2/O4 - cf. M1-DIR-001)
    Analyse selon les responsabilités définies dans M1 Leadership :
    - Compréhension des besoins : O1 Commercial
    - Détermination des exigences (6 types, clause 8.2) :
      spécifications techniques, quantités/délais, exigences
      légales/réglementaires, normes, conditions de livraison,
      exigences implicites (emballage, marquage, certificats)
    - Faisabilité technique et logistique : O2 Achats & Sous-traitance
    - Exigences qualité applicables : O4 Contrôle qualité
    - Possibilité de refuser une commande hors domaine de
      compétence (clause 8.1)
    - Si modification : analyse d'impact par processus (clause 6.3)
      et validation client avant mise en œuvre
            |
            v
 3. CONSULTATION PARTENAIRES INDUSTRIELS (O1/O2/O3)
    Confirmation auprès des partenaires chinois :
    - Faisabilité et conditions de production : O1
    - Délais et conditions de fabrication : O2
    - Délais et conditions de livraison : O3
            |
            v
 4. VALIDATION ET ENREGISTREMENT (O1/S1)
    - Enregistrement dans FileMaker (commande + fiche production)
    - Accusé de réception transmis au client (quantités, prix, délai)
            |
            v
 5. COORDINATION TECHNIQUE (O2 - Achats)
    Échanges par email et WeChat avec Yuyao Mould Factory
    et/ou Whang selon le projet (moules/pièces ou vis)
    Allers-retours techniques jusqu'à validation
            |
            v
 6. LANCEMENT DE LA PRODUCTION (O2 - Achats)
    Si nouveau moule/outillage : validation sur échantillon avant
    lancement en série (clause 8.4)
    Confirmation de commande auprès du/des partenaire(s) chinois
    Suivi de fabrication (photos, rapports d'étape, échanges WeChat)
    4 moyens de conformité : spécifications transmises, suivi
    production, CQ pré-expédition, échantillons (clause 8.5)
    Envoi d'échantillons aux clients et à Plus Sarl si nécessaire
            |
            v
 7. CONTRÔLE QUALITÉ ET LIBÉRATION (O4) (clauses 8.5/8.6)
    Vérification de conformité : exigences techniques + commande
    Le partenaire réalise un CQ avant expédition
    Libération sur 3 critères :
    - CQ fabricant conforme
    - Confirmation correspondance avec la commande
    - Photos des pièces et de l'emballage
    + envoi d'échantillons chez Plus Sarl en parallèle du transport
            |
            v
 8. PRÉPARATION LOGISTIQUE (O3 - Logistique)
    Création fiche de livraison dans FileMaker
    Documents douaniers conformes (législation EU et CH)
    Organisation du transport (aérien/maritime/ferroviaire)
            |
            v
 9. SUIVI DU TRANSPORT (O3 - Logistique)
    Suivi de l'acheminement jusqu'à la livraison finale
            |
            v
10. CONFIRMATION DE RÉCEPTION PAR LE CLIENT (O3/O1)
    Le client confirme la bonne réception des marchandises
            |
            +---> Si NON CONFORME : Processus NC en 4 étapes (clause 8.7)
            |     1. Identification et isolement du lot
            |     2. Analyse de la NC et décision de traitement
            |     3. Actions correctives (cf. PRO-NCF-001, PRO-ACR-001)
            |     4. Enregistrement dans le registre NC FileMaker
            |
            v
11. FACTURATION ET SUIVI (O1 - Commercial)
    Facturation finale, suivi de la satisfaction client
            |
            v
12. TRAÇABILITÉ ET AMÉLIORATION (S1 - Gestion documentaire)
    Conservation des informations dans FileMaker et emails/WeChat
    Alimentation : suivi NC, audit interne, revue de direction
```

> **v0.4 :** Le flux intègre désormais la **revue de commande** (étape 2) formalisée selon le chapitre 2.2.1 du manuel qualité, avec attribution des responsabilités par processus selon M1-DIR-001. Toute modification ultérieure demandée par le client fait l'objet d'une analyse, d'une validation partenaire si nécessaire, d'une confirmation client par e-mail et d'une mise à jour FileMaker.
>
> **v0.4 (UPDATE 6.3) :** L'étape 2 intègre désormais la **planification des modifications** (clause 6.3 ISO 9001). Toute modification susceptible d'impacter la conformité, les délais, les conditions commerciales ou l'organisation fait l'objet d'une analyse d'impact par processus (O1-O4), d'une information/validation client et d'une mise en œuvre contrôlée. Les modifications sont revues en revue de direction (M3). Voir CTX-QUA-001 section 6.
>
> **v0.4 (UPDATE 7.5-8.7) :** Enrichissement du flux principal : étape 2 — détermination des 6 types d'exigences (clause 8.2) et possibilité de refus hors domaine (clause 8.1) ; étape 6 — validation outillages avant série et 4 moyens de conformité production externalisée (clauses 8.4/8.5) ; étape 7 — libération formalisée sur 3 critères (clause 8.6) ; étape 10 — processus NC en 4 étapes avec registre FileMaker (clause 8.7). Enrichissement S1 (maîtrise informations documentées, confidentialité, clause 7.5). Enrichissement O1, O2, O4 (clauses 8.1-8.7).

---

## 4. Objectifs qualité par processus

Les objectifs qualité de Plus Sarl sont alignés sur les quatre axes définis dans le document OBJ-QUA-001 :

| Processus | Indicateur | Objectif | Fréquence de mesure |
|---|---|---|---|
| O1 Commercial | Délai moyen de réponse aux demandes clients | Cible : 24h 🟢 | Par demande |
| O1 Commercial | Satisfaction client | Absence de réclamation majeure et retours positifs 🟢 | Annuel |
| O2 Achats/Sous-traitance | Nombre de non-conformités par client | Maximum 3 NC par client et par an 🟢 | Par livraison |
| O2 Achats/Sous-traitance | Délai de remplacement en cas de NC | Selon besoin client 🟢 | Par NC |
| O3 Logistique/Livraison | Respect des délais de livraison | 95% de livraisons dans les délais 🟢 | Par livraison |
| O3 Logistique/Livraison | Respect des délais - Transport maritime/ferroviaire | +/- 10 jours par rapport à la cible 🟢 | Par livraison |
| O3 Logistique/Livraison | Respect des délais - Transport aérien | +/- 3 jours par rapport à la cible 🟢 | Par livraison |
| O4 Contrôle qualité | Nombre de NC et actions correctives soldées | 100% de traitement 🟢 | Trimestriel |
| M2 Amélioration | Nombre d'actions correctives réalisées dans les délais | 100% 🟢 | Trimestriel |
| M3 Revue de direction | Tenue effective de la revue de direction | 1 fois par an minimum 🟢 | Annuel |
| S1 Gestion documentaire | Documents à jour dans FileMaker | 100% 🟢 | Annuel |
| S2 Compétences | Maintien des compétences (formations, veille) | 🔴 [À REMPLIR — diplômes et formations non divulgués] | Annuel |

---

## 5. Outils et logiciels utilisés

| Outil | Utilisation dans le SMQ |
|---|---|
| **FileMaker** | Base de données principale : enregistrement des informations administratives, suivi des commandes, gestion documentaire |
| **Email** | Communication principale avec les clients européens et les partenaires chinois, traçabilité des échanges |
| **WeChat** | Communication technique quotidienne avec les partenaires chinois (échanges rapides, photos, suivi de production) |

### Sauvegarde des données

Les données sont sauvegardées dans le **cloud, hébergement chez le fournisseur**. 🟢

---

## 6. Exclusion du domaine d'application

| Clause exclue | Justification |
|---|---|
| **8.3 - Conception et développement** | Plus Sarl n'exerce aucune activité de conception. Les conceptions (plans, spécifications techniques, propriété intellectuelle) sont fournies par les clients et appartiennent exclusivement à ces derniers. Plus Sarl intervient en tant que coordinateur industriel pour la mise en production de ces conceptions auprès des partenaires chinois. |

---

## Historique des révisions

| Version | Date | Modification | Auteur |
|---|---|---|---|
| 1.0 | 10/02/2026 | Création initiale | Roxane Wicky |
| 0.2 | 10/02/2026 | Mise à jour des objectifs qualité par processus avec cibles confirmées : 24h réponse, max 3 NC/client/an, 95% livraisons dans les délais, absence de réclamation majeure | Roxane Wicky |
| 0.3 | 12/02/2026 | Intégration des réponses (Whang, Paradiso, SQS, sauvegarde cloud). Ajout du système de légende des champs. | Roxane Wicky |
| 0.4 | 18/02/2026 | Intégration des chapitres 2.1, 2.2, 2.2.1 du manuel qualité. Ajout de la colonne Documents associés. Révision du flux principal avec revue de commande (étape 2), consultation partenaires (étape 3), référence à M1-DIR-001. Ajout de l'étape 12 (traçabilité et amélioration, S1). Ajout des nouveaux documents PRO-LOG-001, FIC-PRO-002, M1-DIR-001. | Roxane Wicky |
| 0.4 | 20/02/2026 | Intégration UPDATE 6.3 : enrichissement M1 (planification des modifications, clause 6.3), enrichissement M2 (revue efficacité modifications), ajout analyse d'impact clause 6.3 dans le flux principal (étape 2). | Roxane Wicky |
| 0.4 | 20/02/2026 | Intégration UPDATEs 7, 7.2, 7.3 : enrichissement S3 (ressources, clause 7.1, ref. CTX-QUA-001 §7), enrichissement S2 (compétences, sensibilisation, clauses 7.2-7.3, ref. FOR-CMP-001). | Roxane Wicky |
| 0.4 | 21/02/2026 | Intégration UPDATE 7.5-8.7 : enrichissement S1 (maîtrise informations documentées, confidentialité, clause 7.5), enrichissement O1 (exigences 8.2, refus 8.1), enrichissement O2 (critères sélection 8.4, validation outillages, confidentialité PI, production externalisée 8.5), enrichissement O4 (libération 8.6, processus NC 8.7, registre NC FileMaker). Mise à jour du flux principal (étapes 2, 6, 7, 10). | Roxane Wicky |
