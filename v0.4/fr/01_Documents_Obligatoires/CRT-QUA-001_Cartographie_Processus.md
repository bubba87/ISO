# Cartographie des Processus

| | |
|---|---|
| **Reference** | CRT-QUA-001 |
| **Version** | 0.4 |
| **Date de creation** | 10/02/2026 |
| **Date de revision** | 20/02/2026 |
| **Redige par** | Roxane Wicky |
| **Approuve par** | Roxane Wicky |

> **Legende :** 🔴 [A REMPLIR] = obligatoire, manquant | 🟡 [RECOMMANDE] = recommande | 🟢 = deja rempli | 🔵 [A VERIFIER] = a confirmer

---

## 1. Vue d'ensemble des processus

### Contexte

Plus Sarl est specialisee dans la coordination industrielle entre des clients europeens et des partenaires de fabrication chinois. L'entreprise n'exerce aucune activite de conception (clause 8.3 de la norme ISO 9001:2015 exclue du domaine d'application). Les conceptions et la propriete intellectuelle appartiennent aux clients. L'activite couvre la coordination commerciale, les achats et la sous-traitance aupres de partenaires chinois (Yuyao Mould Factory et **Whang**, Yuyao), l'organisation logistique internationale et le controle qualite.

La certification ISO 9001:2015 est visee aupres de l'organisme **SQS**. 🟢

### Representation de la cartographie

```
+=========================================================================+
|                    PROCESSUS DE MANAGEMENT                               |
|  +-------------------+  +-------------------+  +---------------------+  |
|  | M1 - Leadership   |  | M2 - Amelioration |  | M3 - Revue de      |  |
|  | et strategie      |  | continue          |  | direction           |  |
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
|  | documentaire       |  | competences et    |  | ressources et       |  |
|  | (FileMaker, emails)|  | formations        |  | infrastructure      |  |
|  +-------------------+  +-------------------+  +---------------------+  |
+=========================================================================+
```

**Note :** La clause 8.3 (Conception et developpement) est exclue du domaine d'application. Les conceptions sont la propriete des clients. Plus Sarl intervient en tant que coordinateur industriel et n'exerce aucune activite de conception.

---

## 2. Liste des processus

### Processus de management

| Code | Processus | Pilote | Objectif | Document(s) associe(s) |
|---|---|---|---|---|
| M1 | Leadership et strategie | Roxane Wicky (Gerante) | Definir la politique qualite, les objectifs strategiques, attribuer les responsabilites, orienter l'entreprise et **planifier les modifications** (clause 6.3 — analyse d'impact, validation, mise en oeuvre controlee) | **M1-DIR-001**, POL-QUA-001, CTX-QUA-001 (section 6) 🟢 |
| M2 | Amelioration continue | Roxane Wicky (Gerante) | Piloter l'amelioration du SMQ (non-conformites, actions correctives, indicateurs). **Revue de l'efficacite des modifications** lors de la revue de direction | PRO-NCF-001, PRO-ACR-001 |
| M3 | Revue de direction | Roxane Wicky (Gerante) | Evaluer les performances du SMQ et decider des actions d'amelioration | FOR-RDR-001 |

### Processus operationnels

| Code | Processus | Pilote | Objectif | Document(s) associe(s) |
|---|---|---|---|---|
| O1 | Commercial | Roxane Wicky (Gerante) | Gerer les relations clients (~10 clients actifs), analyser les besoins, realiser la revue de commande, suivre les commandes dans FileMaker | CTX-QUA-001 (sections 1.2, 1.3) 🟢 |
| O2 | Achats et sous-traitance | Roxane Wicky (Gerante) | Coordonner les partenaires chinois (Yuyao Mould Factory et **Whang**), creer les fiches de production FileMaker, suivre la fabrication 🟢 | PRO-ACH-001, FIC-PRO-001 |
| O3 | Logistique et livraison | Roxane Wicky (Gerante) | Creer les fiches de livraison FileMaker, organiser le transport international, gerer les documents douaniers, assurer le suivi jusqu'a livraison 🟢 | **PRO-LOG-001**, **FIC-PRO-002** 🟢 |
| O4 | Controle qualite | Roxane Wicky (Gerante) | Verifier la conformite des pieces avant expedition, gerer les NC et actions correctives, analyser les retours clients | PRO-NCF-001, PRO-ACR-001, FOR-CTR-001 |

### Processus support

| Code | Processus | Pilote | Objectif | Document(s) associe(s) |
|---|---|---|---|---|
| S1 | Gestion documentaire | Roxane Wicky (Gerante) | Maitriser les documents et enregistrements du SMQ (FileMaker, emails, WeChat). Assurer la tracabilite et alimenter l'amelioration continue. Sauvegarde cloud chez le fournisseur 🟢 | PRO-DOC-001 |
| S2 | Competences et formations | Roxane Wicky (Gerante) | Maintenir et developper les competences necessaires a la coordination industrielle | FOR-CMP-001 |
| S3 | Ressources et infrastructure | Roxane Wicky (Gerante) | Gerer les ressources materielles, informatiques et financieres. Comptabilite via fiduciaire Paradiso 🟢 | — |

---

## 3. Interactions entre processus

### Matrice d'interaction

| De / Vers | O1 Commercial | O2 Achats/Sous-traitance | O3 Logistique/Livraison | O4 Controle qualite |
|---|---|---|---|---|
| **O1 Commercial** | - | Specifications client, cahier des charges, plans, delais | Delai de livraison promis au client | Exigences qualite client |
| **O2 Achats/Sous-traitance** | Delai de fabrication, retour faisabilite, prix | - | Produits prets a expedier, documents d'exportation | Rapports d'inspection, produits a controler |
| **O3 Logistique/Livraison** | Confirmation de livraison, suivi transport | Coordination dates d'expedition | - | Documents de transport, avis de reception |
| **O4 Controle qualite** | Information sur NC, retour satisfaction | Retour NC fabrication, demande de remplacement | Retour NC transport/livraison | - |

### Flux principal (de la demande client a la livraison)

```
 1. RECEPTION DE LA DEMANDE CLIENT (O1 - Commercial)
    Demande recue par e-mail (commande, devis, modification, reclamation)
    ou par telephone en cas d'urgence
            |
            v
 2. ANALYSE PREALABLE ET REVUE DE COMMANDE (O1/O2/O4 - cf. M1-DIR-001)
    Analyse selon les responsabilites definies dans M1 Leadership :
    - Comprehension des besoins : O1 Commercial
    - References, quantites, delais : O1 Commercial
    - Faisabilite technique et logistique : O2 Achats & Sous-traitance
    - Exigences qualite applicables : O4 Controle qualite
    - Si modification : analyse d'impact par processus (clause 6.3)
      et validation client avant mise en oeuvre
            |
            v
 3. CONSULTATION PARTENAIRES INDUSTRIELS (O1/O2/O3)
    Confirmation aupres des partenaires chinois :
    - Faisabilite et conditions de production : O1
    - Delais et conditions de fabrication : O2
    - Delais et conditions de livraison : O3
            |
            v
 4. VALIDATION ET ENREGISTREMENT (O1/S1)
    - Enregistrement dans FileMaker (commande + fiche production)
    - Accuse de reception transmis au client (quantites, prix, delai)
            |
            v
 5. COORDINATION TECHNIQUE (O2 - Achats)
    Echanges par email et WeChat avec Yuyao Mould Factory
    et/ou Whang selon le projet (moules/pieces ou vis)
    Allers-retours techniques jusqu'a validation
            |
            v
 6. LANCEMENT DE LA PRODUCTION (O2 - Achats)
    Confirmation de commande aupres du/des partenaire(s) chinois
    Suivi de fabrication (photos, rapports d'etape, echanges WeChat)
    Envoi d'echantillons aux clients et a Plus Sarl si necessaire
            |
            v
 7. CONTROLE QUALITE PRE-EXPEDITION (O4)
    Verification de conformite : exigences techniques + commande
    Le partenaire realise un CQ avant expedition
    + envoi d'echantillons chez Plus Sarl en parallele du transport
            |
            v
 8. PREPARATION LOGISTIQUE (O3 - Logistique)
    Creation fiche de livraison dans FileMaker
    Documents douaniers conformes (legislation EU et CH)
    Organisation du transport (aerien/maritime/ferroviaire)
            |
            v
 9. SUIVI DU TRANSPORT (O3 - Logistique)
    Suivi de l'acheminement jusqu'a la livraison finale
            |
            v
10. CONFIRMATION DE RECEPTION PAR LE CLIENT (O3/O1)
    Le client confirme la bonne reception des marchandises
            |
            +---> Si NON CONFORME : Processus NC (O4 - Controle qualite)
            |     Creation fiche NC, analyse, decision de traitement,
            |     actions correctives (cf. PRO-NCF-001, PRO-ACR-001)
            |
            v
11. FACTURATION ET SUIVI (O1 - Commercial)
    Facturation finale, suivi de la satisfaction client
            |
            v
12. TRACABILITE ET AMELIORATION (S1 - Gestion documentaire)
    Conservation des informations dans FileMaker et emails/WeChat
    Alimentation : suivi NC, audit interne, revue de direction
```

> **v0.4 :** Le flux integre desormais la **revue de commande** (etape 2) formalisee selon le chapitre 2.2.1 du manuel qualite, avec attribution des responsabilites par processus selon M1-DIR-001. Toute modification ulterieure demandee par le client fait l'objet d'une analyse, d'une validation partenaire si necessaire, d'une confirmation client par e-mail et d'une mise a jour FileMaker.
>
> **v0.4 (UPDATE 6.3) :** L'etape 2 integre desormais la **planification des modifications** (clause 6.3 ISO 9001). Toute modification susceptible d'impacter la conformite, les delais, les conditions commerciales ou l'organisation fait l'objet d'une analyse d'impact par processus (O1-O4), d'une information/validation client et d'une mise en oeuvre controlee. Les modifications sont revues en revue de direction (M3). Voir CTX-QUA-001 section 6.

---

## 4. Objectifs qualite par processus

Les objectifs qualite de Plus Sarl sont alignes sur les quatre axes definis dans le document OBJ-QUA-001 :

| Processus | Indicateur | Objectif | Frequence de mesure |
|---|---|---|---|
| O1 Commercial | Delai moyen de reponse aux demandes clients | Cible : 24h 🟢 | Par demande |
| O1 Commercial | Satisfaction client | Absence de reclamation majeure et retours positifs 🟢 | Annuel |
| O2 Achats/Sous-traitance | Nombre de non-conformites par client | Maximum 3 NC par client et par an 🟢 | Par livraison |
| O2 Achats/Sous-traitance | Delai de remplacement en cas de NC | Selon besoin client 🟢 | Par NC |
| O3 Logistique/Livraison | Respect des delais de livraison | 95% de livraisons dans les delais 🟢 | Par livraison |
| O3 Logistique/Livraison | Respect des delais - Transport maritime/ferroviaire | +/- 10 jours par rapport a la cible 🟢 | Par livraison |
| O3 Logistique/Livraison | Respect des delais - Transport aerien | +/- 3 jours par rapport a la cible 🟢 | Par livraison |
| O4 Controle qualite | Nombre de NC et actions correctives soldees | 100% de traitement 🟢 | Trimestriel |
| M2 Amelioration | Nombre d'actions correctives realisees dans les delais | 100% 🟢 | Trimestriel |
| M3 Revue de direction | Tenue effective de la revue de direction | 1 fois par an minimum 🟢 | Annuel |
| S1 Gestion documentaire | Documents a jour dans FileMaker | 100% 🟢 | Annuel |
| S2 Competences | Maintien des competences (formations, veille) | 🔴 [A REMPLIR — diplomes et formations non divulgues] | Annuel |

---

## 5. Outils et logiciels utilises

| Outil | Utilisation dans le SMQ |
|---|---|
| **FileMaker** | Base de donnees principale : enregistrement des informations administratives, suivi des commandes, gestion documentaire |
| **Email** | Communication principale avec les clients europeens et les partenaires chinois, tracabilite des echanges |
| **WeChat** | Communication technique quotidienne avec les partenaires chinois (echanges rapides, photos, suivi de production) |

### Sauvegarde des donnees

Les donnees sont sauvegardees dans le **cloud, hebergement chez le fournisseur**. 🟢

---

## 6. Exclusion du domaine d'application

| Clause exclue | Justification |
|---|---|
| **8.3 - Conception et developpement** | Plus Sarl n'exerce aucune activite de conception. Les conceptions (plans, specifications techniques, propriete intellectuelle) sont fournies par les clients et appartiennent exclusivement a ces derniers. Plus Sarl intervient en tant que coordinateur industriel pour la mise en production de ces conceptions aupres des partenaires chinois. |

---

## Historique des revisions

| Version | Date | Modification | Auteur |
|---|---|---|---|
| 1.0 | 10/02/2026 | Creation initiale | Roxane Wicky |
| 0.2 | 10/02/2026 | Mise a jour des objectifs qualite par processus avec cibles confirmees : 24h reponse, max 3 NC/client/an, 95% livraisons dans les delais, absence de reclamation majeure | Roxane Wicky |
| 0.3 | 12/02/2026 | Integration des reponses (Whang, Paradiso, SQS, sauvegarde cloud). Ajout du systeme de legende des champs. | Roxane Wicky |
| 0.4 | 18/02/2026 | Integration des chapitres 2.1, 2.2, 2.2.1 du manuel qualite. Ajout de la colonne Documents associes. Revision du flux principal avec revue de commande (etape 2), consultation partenaires (etape 3), reference a M1-DIR-001. Ajout de l'etape 12 (tracabilite et amelioration, S1). Ajout des nouveaux documents PRO-LOG-001, FIC-PRO-002, M1-DIR-001. | Roxane Wicky |
| 0.4 | 20/02/2026 | Integration UPDATE 6.3 : enrichissement M1 (planification des modifications, clause 6.3), enrichissement M2 (revue efficacite modifications), ajout analyse d'impact clause 6.3 dans le flux principal (etape 2). | Roxane Wicky |
