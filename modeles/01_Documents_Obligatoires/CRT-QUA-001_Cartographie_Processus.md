# Cartographie des Processus

| | |
|---|---|
| **Reference** | CRT-QUA-001 |
| **Version** | 1.0 |
| **Date de creation** | [JJ/MM/AAAA] |
| **Date de revision** | [JJ/MM/AAAA] |
| **Redige par** | [Nom de la gerante] |
| **Approuve par** | [Nom de la gerante] |

---

## 1. Vue d'ensemble des processus

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
             |  | Commer-  |->| Concep-  |->| Achats & |->| Con- |  |
             |  | cial     |  | tion     |  | Sous-    |  | trole|  |
             |  |          |  | moules   |  | traitance|  | &    |  |
             |  |          |  |          |  |          |  | Livr.|  |
             |  +----------+  +----------+  +----------+  +------+  |
             +====================================================+
                                    |
+=========================================================================+
|                    PROCESSUS SUPPORT                                      |
|  +-------------------+  +-------------------+  +---------------------+  |
|  | S1 - Gestion des  |  | S2 - Gestion des  |  | S3 - Gestion des   |  |
|  | documents et       |  | competences et    |  | ressources et       |  |
|  | enregistrements    |  | formations        |  | infrastructure      |  |
|  +-------------------+  +-------------------+  +---------------------+  |
+=========================================================================+
```

---

## 2. Liste des processus

### Processus de management

| Code | Processus | Pilote | Objectif |
|---|---|---|---|
| M1 | Leadership et strategie | Gerante | Definir la politique, les objectifs et la strategie de l'entreprise |
| M2 | Amelioration continue | Gerante | Piloter l'amelioration du SMQ (NC, actions correctives, KPI) |
| M3 | Revue de direction | Gerante | Evaluer les performances du SMQ et decider des actions |

### Processus operationnels

| Code | Processus | Pilote | Objectif |
|---|---|---|---|
| O1 | Commercial | Gerante | Comprendre les besoins clients, etablir les offres, gerer les commandes |
| O2 | Conception et developpement | Gerante | Concevoir les moules selon les exigences clients |
| O3 | Achats et sous-traitance | Gerante | Gerer le partenaire chinois, commander, suivre la fabrication |
| O4 | Controle et livraison | Gerante | Controler la conformite et livrer les produits aux clients |

### Processus support

| Code | Processus | Pilote | Objectif |
|---|---|---|---|
| S1 | Gestion documentaire | Gerante | Maitriser les documents et enregistrements du SMQ |
| S2 | Competences et formations | Gerante | Maintenir et developper les competences |
| S3 | Ressources et infrastructure | Gerante | Gerer les ressources materielles et financieres |

---

## 3. Interactions entre processus

### Matrice d'interaction

| De / Vers | O1 Commercial | O2 Conception | O3 Achats | O4 Controle |
|---|---|---|---|---|
| **O1 Commercial** | - | Exigences client, cahier des charges | - | Delai de livraison promis |
| **O2 Conception** | Offre technique | - | Specifications moule, plans | Criteres de controle |
| **O3 Achats** | Delai de fabrication | Retour faisabilite | - | Produits a controler |
| **O4 Controle** | Confirmation livraison | Retour NC conception | Retour NC fabrication | - |

### Flux principal (de la demande client a la livraison)

```
1. CLIENT : Envoie une demande (plan, specifications, ou besoin)
       |
       v
2. O1 - COMMERCIAL : Analyse la demande, prepare l'offre
       |
       v
3. CLIENT : Confirme la commande
       |
       v
4. O1 - COMMERCIAL : Revue de commande (verification des exigences)
       |
       v
5. O2 - CONCEPTION : Developpe le moule (specifications, plans, choix materiaux)
       |
       v
6. O2 - CONCEPTION : Revue de conception (validation interne avant envoi)
       |
       v
7. O3 - ACHATS : Transmet le cahier des charges au partenaire chinois
       |
       v
8. O3 - ACHATS : Suit la fabrication (echanges, etapes, photos, rapports)
       |
       v
9. O3 - ACHATS : Reception des moules/pieces en Suisse
       |
       v
10. O4 - CONTROLE : Controle a reception (dimensionnel, visuel, fonctionnel)
       |
       +---> Si NON CONFORME : Processus NC (PRO-NCF-001)
       |
       v
11. O4 - LIVRAISON : Preparation et expedition au client
       |
       v
12. CLIENT : Reception et acceptation
       |
       v
13. O1 - COMMERCIAL : Suivi satisfaction, facturation
```

---

## 4. Indicateurs par processus

| Processus | Indicateur | Objectif | Frequence de mesure |
|---|---|---|---|
| O1 Commercial | Taux de transformation des offres | [> XX%] | Trimestriel |
| O1 Commercial | Nombre de reclamations clients | [< X par an] | Mensuel |
| O2 Conception | Nombre de modifications apres validation | [< X par projet] | Par projet |
| O3 Achats | Taux de conformite des livraisons fournisseur | [> 95%] | Par livraison |
| O3 Achats | Respect des delais fournisseur | [> 90%] | Par livraison |
| O4 Controle | Taux de conformite a reception | [> 95%] | Par reception |
| O4 Livraison | Taux de livraison a temps aux clients | [> 90%] | Par livraison |
| M2 Amelioration | Nombre d'actions correctives soldees | [100% dans les delais] | Trimestriel |
| S2 Competences | Heures de formation annuelles | [> X heures] | Annuel |

---

> **Instructions de remplissage :**
> 1. Adaptez les processus a VOTRE realite (ajoutez ou supprimez si necessaire)
> 2. Definissez des objectifs realistes pour chaque indicateur
> 3. Completez les interactions entre processus
> 4. Ce document est le "plan" de votre SMQ - l'auditeur s'en servira comme fil conducteur
> 5. Si vous ne faites PAS de conception, supprimez le processus O2
