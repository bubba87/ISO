# Procedure d'Actions Correctives

| | |
|---|---|
| **Reference** | PRO-ACR-001 |
| **Version** | 0.4 |
| **Date de creation** | 10/02/2026 |
| **Date de revision** | 18/02/2026 |
| **Redige par** | Roxane Wicky |
| **Approuve par** | Roxane Wicky |

> **Legende :** :red_circle: [A REMPLIR] = obligatoire, manquant | :yellow_circle: [RECOMMANDE] = recommande | :green_circle: = deja rempli | :blue_circle: [A VERIFIER] = a confirmer

---

## 1. Objet

Definir les regles d'analyse des causes, de mise en oeuvre et de verification de l'efficacite des actions correctives afin d'eliminer les causes des non-conformites et d'empecher leur recurrence au sein du SMQ de Plus Sarl.

> **Lien Processus 04 (cf. CTX-QUA-001, section 1.1) :** En cas de non-conformite identifiee, une fiche NC est creee (PRO-NCF-001), une decision de traitement est prise (acceptation, remplacement ou correction), puis une analyse de la cause et investigation est menee. La present procedure definit la mise en oeuvre des actions correctives afin d'eviter la repetition. 🟢

## 2. Domaine d'application

Toute non-conformite necessitant une action corrective :
- NC majeures (systematiquement)
- NC mineures recurrentes
- NC d'audit interne ou externe (y compris audit de certification SQS)
- Reclamations clients significatives ou repetitives
- Toute situation ou la gerante juge necessaire d'agir sur les causes

## 3. Definitions

| Terme | Definition |
|---|---|
| **Correction** | Action pour eliminer une NC detectee (traitement immediat du symptome) |
| **Action corrective** | Action pour eliminer la **cause** d'une NC et empecher sa recurrence |
| **Cause racine** | La cause fondamentale a l'origine de la NC |
| **Verification d'efficacite** | Controle que l'action corrective a bien empeche la recurrence de la NC |

> **Difference cle :**
> - Correction = "J'ai remplace les pieces defectueuses aupres du client" (symptome)
> - Action corrective = "J'ai demande a l'usine de mettre en place un controle renforce sur cette reference" (cause)

## 4. Responsabilites

| Responsabilite | Qui |
|---|---|
| Decider de l'ouverture d'une AC | :green_circle: Roxane Wicky, gerante |
| Analyser les causes (dans la mesure des competences de la gerante) | :green_circle: Roxane Wicky, gerante (avec les partenaires chinois si NC de fabrication) |
| Definir l'action corrective | :green_circle: Roxane Wicky, gerante |
| Mettre en oeuvre ou coordonner la mise en oeuvre | :green_circle: Roxane Wicky, gerante (ou partenaire chinois) |
| Verifier l'efficacite | :green_circle: Roxane Wicky, gerante |

## 5. Procedure

### 5.1 Logigramme

```
    NC necessitant une action corrective
    (voir criteres en section 2)
            |
            v
    +------------------------+
    | 1. Ouvrir la fiche AC  |---> AC_[AAAA]_[NNN]
    +------------------------+
            |
            v
    +------------------------+
    | 2. Analyser les causes |---> Methode des 5 Pourquoi
    |    (dans la mesure des |     (adaptee a une micro-entreprise)
    |     competences)       |
    +------------------------+
            |
            v
    +------------------------+
    | 3. Identifier la cause  |---> Cause racine documentee
    |    racine               |
    +------------------------+
            |
            v
    +------------------------+
    | 4. Definir l'action     |---> Quoi, qui, quand
    |    corrective           |
    +------------------------+
            |
            v
    +------------------------+
    | 5. Mettre en oeuvre     |---> Application de l'action
    |    (gerante et/ou       |     (coordination partenaires)
    |     partenaires)        |
    +------------------------+
            |
            v
    +------------------------+
    | 6. Verifier l'efficacite|---> NC recurrente ? OUI/NON
    +------------------------+
            |
       NC eliminee ?
       /          \
     OUI          NON
      |             |
      v             v
  +--------+   +-----------------+
  | Cloturer|  | Nouvelle analyse|
  | la fiche|  | des causes      |
  +--------+   +-----------------+
```

### 5.2 Detail des etapes

**Etape 1 - Ouvrir la fiche AC**

- Attribuer un numero : AC_[AAAA]_[NNN]
- Lier a la NC d'origine (NC_[AAAA]_[NNNN])
- Decrire le probleme

**Etape 2 - Analyser les causes**

L'analyse des causes est realisee par la gerante dans la mesure de ses competences, en coordination avec les partenaires chinois lorsque la NC est liee a la fabrication.

Utiliser la methode des 5 Pourquoi (recommandee pour Plus Sarl) :

| # | Pourquoi ? | Reponse |
|---|---|---|
| 1 | Pourquoi la NC est-elle survenue ? | [Reponse 1] |
| 2 | Pourquoi [Reponse 1] ? | [Reponse 2] |
| 3 | Pourquoi [Reponse 2] ? | [Reponse 3] |
| 4 | Pourquoi [Reponse 3] ? | [Reponse 4] |
| 5 | Pourquoi [Reponse 4] ? | [Reponse 5 = cause racine probable] |

### 5.3 Actions correctives types pour Plus Sarl

L'objectif des actions correctives est de prevenir la recurrence des NC et de reduire l'impact sur les clients. Voici les scenarios les plus frequents et les actions correctives associees :

#### Scenario 1 : Retard de transport

| Element | Detail |
|---|---|
| **Probleme** | Retard de livraison lie au transporteur ou au transitaire |
| **Cause racine typique** | Transporteur/transitaire non fiable, problemes logistiques |
| **Actions correctives** | - Reevaluer le transporteur/transitaire concerne |
| | - Informer les partenaires chinois pour eviter ce prestataire a l'avenir |
| | - Adapter le choix logistique (changement de mode : aerien/maritime/ferroviaire) |
| | - Anticiper les delais dans les communications aux clients |

#### Scenario 2 : Retard de production

| Element | Detail |
|---|---|
| **Probleme** | Retard de fabrication chez le partenaire chinois |
| **Cause racine typique** | Planification insuffisante, surcharge de l'usine, probleme technique |
| **Actions correctives** | - Suivi renforce avec les partenaires chinois (points d'etape plus frequents) |
| | - Pousser pour de meilleurs delais et une meilleure planification |
| | - Anticiper les communications vers les clients en cas de risque de retard |
| | - Ajustements commerciaux si necessaire (geste commercial, echelonnement) |

#### Scenario 3 : Defaut de production

| Element | Detail |
|---|---|
| **Probleme** | Pieces non conformes aux specifications (dimensions, aspect, matiere) |
| **Cause racine typique** | Probleme de reglage machine, usure du moule, erreur de matiere, controle insuffisant |
| **Actions correctives** | - Demander a l'usine de conserver les informations sur la NC |
| | - Demander la mise en place de controles renforces sur les prochaines productions de cette reference |
| | - Remplacement des pieces non conformes pour le client |
| | - Adaptation logistique si necessaire (reexpedition urgente) |
| | - Suivi renforce du partenaire (monitoring continu de la qualite) |
| | - Renforcer le CQ pre-expedition et l'echantillonnage (cf. PRO-ACH-001, section 8) |
| | - Ajustements commerciaux si necessaire |

#### Scenario 4 : Erreur d'etiquetage ou d'emballage

| Element | Detail |
|---|---|
| **Probleme** | Erreur d'etiquetage ou d'emballage (reference incorrecte sur l'etiquette, confusion entre references similaires) |
| **Cause racine typique** | Confusion entre references similaires, absence de checklist de controle, verification insuffisante avant expedition |
| **Actions correctives** | - Creer une checklist de controle qualite complete couvrant l'etiquetage et l'emballage |
| | - Renforcer la verification des etiquettes avant expedition |
| | - Clarifier les references avec le fournisseur (notamment les references proches pouvant preter a confusion) |
| | - Demander au fournisseur de mettre en place un double controle sur l'etiquetage |
| | - Integrer le controle d'etiquetage dans le CQ pre-expedition |

> **Principe directeur :** Les actions correctives de Plus Sarl visent a prevenir la recurrence et a reduire l'impact sur le client. La gerante agit dans la mesure de ses competences et s'appuie sur ses partenaires chinois (Yuyao Mould Factory et Whang) pour les aspects techniques de la fabrication.

**Etape 3 - Identifier la cause racine**

- Selectionner la cause la plus probable
- Verifier par des donnees/preuves si possible (photos, rapports, echanges email/WeChat)

**Etape 4 - Definir l'action corrective**

L'action corrective doit :
- Agir sur la cause racine (pas sur le symptome)
- Etre realiste et proportionnee aux moyens de Plus Sarl
- Avoir un responsable et un delai
- Etre communiquee au partenaire chinois concerne si necessaire

**Etape 5 - Mettre en oeuvre**

- Realiser l'action ou coordonner sa mise en oeuvre par le partenaire chinois
- Documenter ce qui a ete fait
- Communiquer les actions aux parties concernees (partenaire chinois, client, transporteur)

**Etape 6 - Verifier l'efficacite**

- Attendre un delai suffisant (generalement 1 a 3 mois ou les prochaines commandes de meme type)
- Verifier que la NC ne s'est pas reproduite lors des productions/livraisons suivantes
- Si la NC se reproduit : reprendre l'analyse des causes, envisager des mesures plus fortes

## 6. Fiche d'Action Corrective (modele)

### Identification

| Element | Detail |
|---|---|
| **N. d'AC** | AC_[AAAA]_[NNN] |
| **Date d'ouverture** | [JJ/MM/AAAA] |
| **NC d'origine** | NC_[AAAA]_[NNNN] |
| **Source** | [ ] Reclamation client [ ] Retard transport [ ] Retard production [ ] Defaut production [ ] Etiquetage/Emballage [ ] CQ pre-expedition [ ] Audit interne [ ] Audit externe (SQS) [ ] Autre |

### Description du probleme

| Element | Detail |
|---|---|
| **Description** | [Description factuelle du probleme] |
| **Impact sur le client** | [Consequences de la NC pour le client] |
| **Frequence/Recurrence** | [Premiere occurrence / Recurrente (combien de fois)] |

### Analyse des causes

| Element | Detail |
|---|---|
| **Methode utilisee** | [ ] 5 Pourquoi [ ] Autre |
| **Detail de l'analyse** | [Voir tableau des 5 Pourquoi] |
| **Cause racine identifiee** | [Description de la cause racine] |
| **Partenaire implique dans l'analyse** | [ ] Yuyao Mould Factory [ ] Whang [ ] Transporteur [ ] Analyse interne uniquement |

### Plan d'action

| # | Action corrective | Responsable | Delai | Statut |
|---|---|---|---|---|
| 1 | [Description de l'action] | [Gerante / Partenaire] | [Date] | [ ] Planifie [ ] En cours [ ] Realise |
| 2 | [Description de l'action] | [Gerante / Partenaire] | [Date] | [ ] Planifie [ ] En cours [ ] Realise |
| 3 | [Description de l'action] | [Gerante / Partenaire] | [Date] | [ ] Planifie [ ] En cours [ ] Realise |

### Verification de l'efficacite

| Element | Detail |
|---|---|
| **Date de verification** | [JJ/MM/AAAA] (au moins 1-3 mois apres mise en oeuvre ou prochaines commandes) |
| **Methode de verification** | [Suivi des prochaines livraisons, absence de reclamation client, retour partenaire] |
| **Resultat** | [ ] Efficace (NC non recurrente) [ ] Non efficace (NC recurrente) |
| **Commentaire** | [Observations] |

### Cloture

| Element | Detail |
|---|---|
| **Date de cloture** | [JJ/MM/AAAA] |
| **Cloturee par** | Roxane Wicky |
| **Statut final** | [ ] Soldee [ ] En cours [ ] Reouverture necessaire |

---

### Exemple de fiche remplie : AC_2026_001

#### Identification

| Element | Detail |
|---|---|
| **N. d'AC** | :green_circle: AC_2026_001 |
| **Date d'ouverture** | :green_circle: 10/02/2026 |
| **NC d'origine** | :green_circle: NC_2026_1001 |
| **Source** | :green_circle: [X] Etiquetage/Emballage |

#### Description du probleme

| Element | Detail |
|---|---|
| **Description** | :green_circle: Livraison d'un carton de 1000 pieces avec etiquetage incorrect (90.60.05710L au lieu de 90.60.05710) - SHIP_25058/CFM00057428 |
| **Impact sur le client** | :green_circle: Impact limite -- le produit physique est conforme, seule l'etiquette est erronee. Le client a accepte le produit en l'etat (derogation). |
| **Frequence/Recurrence** | :green_circle: Premiere occurrence |

#### Analyse des causes

| Element | Detail |
|---|---|
| **Methode utilisee** | :green_circle: [X] 5 Pourquoi |
| **Detail de l'analyse** | :red_circle: [A REMPLIR -- cause pas encore identifiee. L'analyse sera approfondie lors du voyage en Chine en mars 2026] |
| **Cause racine identifiee** | :red_circle: [A REMPLIR -- cause exacte pas encore identifiee] |
| **Partenaire implique dans l'analyse** | :green_circle: [X] Yuyao Mould Factory |

#### Plan d'action

| # | Action corrective | Responsable | Delai | Statut |
|---|---|---|---|---|
| 1 | Informer le fournisseur de la NC | :green_circle: Roxane Wicky | :green_circle: 10/02/2026 | :green_circle: [X] Realise |
| 2 | Creer une checklist de controle qualite complete | Roxane Wicky + Yuyao Mould Factory | Mars 2026 (voyage Chine) | [ ] En cours |
| 3 | Renforcer le CQ pre-expedition pour l'etiquetage | Yuyao Mould Factory | Mars 2026 (voyage Chine) | [ ] Planifie |

#### Verification de l'efficacite

| Element | Detail |
|---|---|
| **Date de verification** | :red_circle: [A REMPLIR -- apres mise en oeuvre des actions, prochaines commandes de la reference 90.60.05710] |
| **Methode de verification** | Suivi des prochaines livraisons de cette reference, verification de l'etiquetage |
| **Resultat** | :red_circle: [A REMPLIR -- en attente] |
| **Commentaire** | Suivi en cours. Cause exacte pas encore identifiee. Photos non disponibles. Le traitement sera renforce lors du voyage en Chine prevu en mars 2026. |

#### Cloture

| Element | Detail |
|---|---|
| **Date de cloture** | :red_circle: [A REMPLIR -- en attente] |
| **Cloturee par** | Roxane Wicky |
| **Statut final** | :green_circle: [X] En cours |

---

## 7. Registre des actions correctives

| N. AC | Date ouv. | NC liee | Cause racine | Action | Delai | Efficace ? | Statut |
|---|---|---|---|---|---|---|---|
| :green_circle: AC_2026_001 | 10/02/2026 | NC_2026_1001 | :red_circle: Cause pas encore identifiee | 1. Informer le fournisseur (realise) 2. Creer une checklist de controle qualite complete 3. Renforcer le CQ pre-expedition pour l'etiquetage | Mars 2026 (voyage Chine) | En cours | En cours |
| AC_[AAAA]_[NNN] | [date] | NC_xxx | [resume] | [resume] | [date] | [O/N/En cours] | [Ouvert/Solde] |

---

## 8. Indicateurs

| Indicateur | Cible | Frequence |
|---|---|---|
| Nombre d'AC ouvertes | Information | Trimestriel |
| Repartition par type (transport, production, retard, etiquetage, CQ pre-expedition) | Information | Trimestriel |
| Taux de cloture dans les delais | > 80% | Trimestriel |
| Taux d'efficacite des AC | > 90% | Annuel |

---

> **Instructions de remplissage :**
> 1. N'ouvrez une AC que si c'est justifie (NC majeure, recurrente, ou d'audit)
> 2. Prenez le temps de bien analyser la cause racine -- c'est l'etape cle
> 3. La methode des 5 Pourquoi est simple et efficace pour une micro-entreprise comme Plus Sarl
> 4. Impliquez les partenaires chinois (Yuyao Mould Factory ou Whang) dans l'analyse quand la NC vient de la fabrication
> 5. Documentez les echanges (emails, WeChat) comme preuves des actions correctives
> 6. L'auditeur (SQS) verifiera que vos AC sont efficaces (pas juste sur papier)
> 7. L'analyse des causes se fait dans la mesure des competences de la gerante -- c'est une demarche d'amelioration continue
> 8. Le CQ pre-expedition avec echantillonnage peut etre une source d'AC si des NC sont detectees avant livraison

---

## Historique des revisions

| Version | Date | Description de la modification | Auteur |
|---|---|---|---|
| 0.1 | 10/02/2026 | Creation initiale | Roxane Wicky |
| 0.2 | 10/02/2026 | Ajout de la premiere action corrective reelle (AC_2026_001 liee a NC_2026_1001 - erreur d'etiquetage). Ajout du Scenario 4 (erreur d'etiquetage/emballage). Mise a jour du format de numerotation (underscores). Ajout de la categorie "Etiquetage/Emballage" dans les indicateurs. | Roxane Wicky |
| 0.3 | 12/02/2026 | Integration des reponses (Whang, Paradiso, SQS, cloud, echantillonnage CQ). Ajout du systeme de legende des champs. | Roxane Wicky |
| 0.4 | 18/02/2026 | Integration UPDATE 2.1 Processus 04 : ajout reference au lien avec le controle qualite formalise (CTX-QUA-001, section 1.1). | Roxane Wicky |
