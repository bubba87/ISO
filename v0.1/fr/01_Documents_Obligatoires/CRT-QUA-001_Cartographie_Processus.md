# Cartographie des Processus

| | |
|---|---|
| **Reference** | CRT-QUA-001 |
| **Version** | 1.0 |
| **Date de creation** | 10/02/2026 |
| **Date de revision** | 10/02/2026 |
| **Redige par** | Roxane Wicky |
| **Approuve par** | Roxane Wicky |

---

## 1. Vue d'ensemble des processus

### Contexte

Plus Sarl est specialisee dans la coordination industrielle entre des clients europeens et des partenaires de fabrication chinois. L'entreprise n'exerce aucune activite de conception (clause 8.3 de la norme ISO 9001:2015 exclue du domaine d'application). Les conceptions et la propriete intellectuelle appartiennent aux clients. L'activite couvre la coordination commerciale, les achats et la sous-traitance aupres de partenaires chinois, l'organisation logistique internationale et le controle qualite.

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

| Code | Processus | Pilote | Objectif |
|---|---|---|---|
| M1 | Leadership et strategie | Roxane Wicky (Gerante) | Definir la politique qualite, les objectifs strategiques et orienter l'entreprise |
| M2 | Amelioration continue | Roxane Wicky (Gerante) | Piloter l'amelioration du SMQ (non-conformites, actions correctives, indicateurs) |
| M3 | Revue de direction | Roxane Wicky (Gerante) | Evaluer les performances du SMQ et decider des actions d'amelioration |

### Processus operationnels

| Code | Processus | Pilote | Objectif |
|---|---|---|---|
| O1 | Commercial | Roxane Wicky (Gerante) | Gerer les relations clients, analyser les besoins, etablir les offres, suivre les commandes |
| O2 | Achats et sous-traitance | Roxane Wicky (Gerante) | Coordonner les partenaires chinois (Yuyao Mould Factory et second partenaire), suivre la production |
| O3 | Logistique et livraison | Roxane Wicky (Gerante) | Organiser le transport international (aerien, maritime, ferroviaire), gerer les douanes, assurer la livraison |
| O4 | Controle qualite | Roxane Wicky (Gerante) | Gerer les non-conformites, mettre en oeuvre les actions correctives, suivre les reclamations |

### Processus support

| Code | Processus | Pilote | Objectif |
|---|---|---|---|
| S1 | Gestion documentaire | Roxane Wicky (Gerante) | Maitriser les documents et enregistrements du SMQ (FileMaker, emails, fichiers) |
| S2 | Competences et formations | Roxane Wicky (Gerante) | Maintenir et developper les competences necessaires a la coordination industrielle |
| S3 | Ressources et infrastructure | Roxane Wicky (Gerante) | Gerer les ressources materielles, informatiques et financieres |

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
 1. RECEPTION DE LA DEMANDE CLIENT
    Le client envoie sa demande par email (plans, specifications, besoin)
            |
            v
 2. ANALYSE DES BESOINS (O1 - Commercial)
    Analyse des besoins, des specifications techniques et des delais
            |
            v
 3. ENREGISTREMENT ADMINISTRATIF (S1 - Gestion documentaire)
    Les informations administratives sont enregistrees dans FileMaker
            |
            v
 4. COORDINATION TECHNIQUE AVEC LES PARTENAIRES CHINOIS (O2 - Achats)
    Echanges par email et WeChat avec Yuyao Mould Factory
    (et/ou second partenaire selon le projet)
            |
            v
 5. ECHANGES ITERATIFS (O2 - Achats)
    Allers-retours techniques jusqu'a validation de la solution
    (faisabilite, materiaux, tolerances, prix)
            |
            v
 6. ETABLISSEMENT DES DOCUMENTS DE COMMANDE (O1/O2)
    Facture douaniere, facture client, bon de livraison,
    accusé de reception de commande
            |
            v
 7. LANCEMENT DE LA PRODUCTION (O2 - Achats)
    Confirmation de commande aupres du/des partenaire(s) chinois
    Suivi de fabrication (photos, rapports d'etape, echanges WeChat)
            |
            v
 8. PREPARATION DES DOCUMENTS D'EXPORTATION (O3 - Logistique)
    Documents douaniers, organisation du transport
    (aerien, maritime ou ferroviaire selon urgence et volume)
            |
            v
 9. SUIVI DU TRANSPORT (O3 - Logistique)
    Suivi de l'acheminement jusqu'a destination
            |
            v
10. CONFIRMATION DE RECEPTION PAR LE CLIENT (O3/O1)
    Le client confirme la bonne reception des marchandises
            |
            +---> Si NON CONFORME : Processus NC (O4 - Controle qualite)
            |     Gestion de la reclamation, action corrective,
            |     coordination remplacement avec partenaire chinois
            |
            v
11. FACTURATION ET SUIVI (O1 - Commercial)
    Facturation finale, suivi de la satisfaction client
```

---

## 4. Objectifs qualite par processus

Les objectifs qualite de Plus Sarl sont alignes sur les quatre axes definis dans le document OBJ-QUA-001 :

| Processus | Indicateur | Objectif | Frequence de mesure |
|---|---|---|---|
| O1 Commercial | Delai moyen de reponse aux demandes clients | [A CONFIRMER] | Par demande |
| O1 Commercial | Niveau de satisfaction client | [A CONFIRMER] | Annuel |
| O2 Achats/Sous-traitance | Nombre de non-conformites par commande | Minimiser les NC | Par livraison |
| O2 Achats/Sous-traitance | Delai de remplacement en cas de NC | Selon besoin client | Par NC |
| O3 Logistique/Livraison | Respect des delais - Transport maritime/ferroviaire | +/- 10 jours par rapport a la cible | Par livraison |
| O3 Logistique/Livraison | Respect des delais - Transport aerien | +/- 3 jours par rapport a la cible | Par livraison |
| O4 Controle qualite | Nombre de NC et actions correctives soldees | 100% de traitement | Trimestriel |
| M2 Amelioration | Nombre d'actions correctives realisees dans les delais | 100% | Trimestriel |
| M3 Revue de direction | Tenue effective de la revue de direction | 1 fois par an minimum | Annuel |
| S1 Gestion documentaire | Documents a jour dans FileMaker | 100% | Annuel |
| S2 Competences | Maintien des competences (formations, veille) | [A CONFIRMER] | Annuel |

---

## 5. Outils et logiciels utilises

| Outil | Utilisation dans le SMQ |
|---|---|
| **FileMaker** | Base de donnees principale : enregistrement des informations administratives, suivi des commandes, gestion documentaire |
| **Email** | Communication principale avec les clients europeens et les partenaires chinois, tracabilite des echanges |
| **WeChat** | Communication technique quotidienne avec les partenaires chinois (echanges rapides, photos, suivi de production) |

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
| | | | |
