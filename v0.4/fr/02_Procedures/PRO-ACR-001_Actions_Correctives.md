# Procédure d'Actions Correctives

| | |
|---|---|
| **Référence** | PRO-ACR-001 |
| **Version** | 0.4 |
| **Date de création** | 10/02/2026 |
| **Date de revision** | 18/02/2026 |
| **Rédigé par** | Roxane Wicky |
| **Approuve par** | Roxane Wicky |

> **Légende :** :red_circle: [À REMPLIR] = obligatoire, manquant | :yellow_circle: [RECOMMANDE] = recommandé | :green_circle: = déjà rempli | :blue_circle: [À VÉRIFIER] = a confirmer

---

## 1. Objet

Définir les règles d'analyse des causes, de mise en œuvre et de vérification de l'efficacité des actions correctives afin d'eliminer les causes des non-conformites et d'empecher leur recurrence au sein du SMQ de Plus Sarl.

> **Lien Processus 04 (cf. CTX-QUA-001, section 1.1) :** En cas de non-conformité identifiée, une fiche NC est créée (PRO-NCF-001), une decision de traitement est prise (acceptation, remplacement ou correction), puis une analyse de la cause et investigation est menee. La présent procédure définit la mise en œuvre des actions correctives afin d'eviter la répétition. 🟢

## 2. Domaine d'application

Toute non-conformité necessitant une action corrective :
- NC majeures (systématiquement)
- NC mineures recurrentes
- NC d'audit interne ou externe (y compris audit de certification SQS)
- Réclamations clients significatives ou repetitives
- Toute situation ou la gérante juge nécessaire d'agir sur les causes

## 3. Definitions

| Terme | Definition |
|---|---|
| **Correction** | Action pour eliminer une NC détectée (traitement immédiat du symptome) |
| **Action corrective** | Action pour eliminer la **cause** d'une NC et empecher sa recurrence |
| **Cause racine** | La cause fondamentale à l\'origine de la NC |
| **Vérification d'efficacité** | Contrôle que l'action corrective a bien empeche la recurrence de la NC |

> **Difference cle :**
> - Correction = "J'ai remplacé les pièces defectueuses auprès du client" (symptome)
> - Action corrective = "J'ai demande à l\'usine de mettre en place un contrôle renforce sur cette référence" (cause)

## 4. Responsabilités

| Responsabilité | Qui |
|---|---|
| Decider de l'ouverture d'une AC | :green_circle: Roxane Wicky, gérante |
| Analyser les causes (dans la mesure des compétences de la gérante) | :green_circle: Roxane Wicky, gérante (avec les partenaires chinois si NC de fabrication) |
| Définir l'action corrective | :green_circle: Roxane Wicky, gérante |
| Mettre en œuvre ou coordonner la mise en œuvre | :green_circle: Roxane Wicky, gérante (ou partenaire chinois) |
| Vérifier l'efficacité | :green_circle: Roxane Wicky, gérante |

## 5. Procédure

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
    | 2. Analyser les causes |---> Méthode des 5 Pourquoi
    |    (dans la mesure des |     (adaptée à une micro-entreprise)
    |     compétences)       |
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
    | 5. Mettre en œuvre     |---> Application de l'action
    |    (gerante et/ou       |     (coordination partenaires)
    |     partenaires)        |
    +------------------------+
            |
            v
    +------------------------+
    | 6. Verifier l'efficacité|---> NC recurrente ? OUI/NON
    +------------------------+
            |
       NC eliminee ?
       /          \
     OUI          NON
      |             |
      v             v
  +--------+   +-----------------+
  | Clôturer|  | Nouvelle analyse|
  | la fiche|  | des causes      |
  +--------+   +-----------------+
```

### 5.2 Détail des étapes

**Étape 1 - Ouvrir la fiche AC**

- Attribuer un numéro : AC_[AAAA]_[NNN]
- Lier à la NC d'origine (NC_[AAAA]_[NNNN])
- Decrire le problème

**Étape 2 - Analyser les causes**

L'analyse des causes est réalisée par la gérante dans la mesure de ses compétences, en coordination avec les partenaires chinois lorsque la NC est liée à la fabrication.

Utiliser la méthode des 5 Pourquoi (recommandée pour Plus Sarl) :

| # | Pourquoi ? | Réponse |
|---|---|---|
| 1 | Pourquoi la NC est-elle survenue ? | [Réponse 1] |
| 2 | Pourquoi [Réponse 1] ? | [Réponse 2] |
| 3 | Pourquoi [Réponse 2] ? | [Réponse 3] |
| 4 | Pourquoi [Réponse 3] ? | [Réponse 4] |
| 5 | Pourquoi [Réponse 4] ? | [Réponse 5 = cause racine probable] |

### 5.3 Actions correctives types pour Plus Sarl

L'objectif des actions correctives est de prevenir la recurrence des NC et de reduire l'impact sur les clients. Voici les scenarios les plus frequents et les actions correctives associées :

#### Scenario 1 : Retard de transport

| Élément | Détail |
|---|---|
| **Problème** | Retard de livraison lié au transporteur ou au transitaire |
| **Cause racine typique** | Transporteur/transitaire non fiable, problèmes logistiques |
| **Actions correctives** | - Reevaluer le transporteur/transitaire concerné |
| | - Informer les partenaires chinois pour eviter ce prestataire à l\'avenir |
| | - Adapter le choix logistique (changement de mode : aérien/maritime/ferroviaire) |
| | - Anticiper les délais dans les communications aux clients |

#### Scenario 2 : Retard de production

| Élément | Détail |
|---|---|
| **Problème** | Retard de fabrication chez le partenaire chinois |
| **Cause racine typique** | Planification insuffisante, surcharge de l'usine, problème technique |
| **Actions correctives** | - Suivi renforce avec les partenaires chinois (points d'étape plus frequents) |
| | - Pousser pour de meilleurs délais et une meilleure planification |
| | - Anticiper les communications vers les clients en cas de risque de retard |
| | - Ajustements commerciaux si nécessaire (geste commercial, echelonnement) |

#### Scenario 3 : Defaut de production

| Élément | Détail |
|---|---|
| **Problème** | Pièces non conformes aux spécifications (dimensions, aspect, matière) |
| **Cause racine typique** | Problème de reglage machine, usure du moule, erreur de matière, contrôle insuffisant |
| **Actions correctives** | - Demander à l\'usine de conserver les informations sur la NC |
| | - Demander la mise en place de contrôles renforces sur les prochaines productions de cette référence |
| | - Remplacement des pièces non conformes pour le client |
| | - Adaptation logistique si nécessaire (reexpedition urgente) |
| | - Suivi renforce du partenaire (monitoring continu de la qualité) |
| | - Renforcer le CQ pre-expédition et l'echantillonnage (cf. PRO-ACH-001, section 8) |
| | - Ajustements commerciaux si nécessaire |

#### Scenario 4 : Erreur d'étiquetage ou d'emballage

| Élément | Détail |
|---|---|
| **Problème** | Erreur d'étiquetage ou d'emballage (référence incorrecte sur l'etiquette, confusion entre références similaires) |
| **Cause racine typique** | Confusion entre références similaires, absence de checklist de contrôle, vérification insuffisante avant expédition |
| **Actions correctives** | - Créer une checklist de contrôle qualité complète couvrant l'étiquetage et l'emballage |
| | - Renforcer la vérification des etiquettes avant expédition |
| | - Clarifier les références avec le fournisseur (notamment les références proches pouvant preter a confusion) |
| | - Demander au fournisseur de mettre en place un double contrôle sur l'étiquetage |
| | - Integrer le contrôle d'étiquetage dans le CQ pre-expédition |

> **Principe directeur :** Les actions correctives de Plus Sarl visent a prevenir la recurrence et a reduire l'impact sur le client. La gérante agit dans la mesure de ses compétences et s'appuie sur ses partenaires chinois (Yuyao Mould Factory et Whang) pour les aspects techniques de la fabrication.

**Étape 3 - Identifier la cause racine**

- Selectionner la cause la plus probable
- Vérifier par des données/preuves si possible (photos, rapports, échanges email/WeChat)

**Étape 4 - Définir l'action corrective**

L'action corrective doit :
- Agir sur la cause racine (pas sur le symptome)
- Être realiste et proportionnee aux moyens de Plus Sarl
- Avoir un responsable et un délai
- Être communiquee au partenaire chinois concerné si nécessaire

**Étape 5 - Mettre en œuvre**

- Réaliser l'action ou coordonner sa mise en œuvre par le partenaire chinois
- Documenter ce qui a été fait
- Communiquer les actions aux parties concernées (partenaire chinois, client, transporteur)

**Étape 6 - Vérifier l'efficacité**

- Attendre un délai suffisant (generalement 1 a 3 mois ou les prochaines commandes de meme type)
- Vérifier que la NC ne s'est pas reproduite lors des productions/livraisons suivantes
- Si la NC se reproduit : reprendre l'analyse des causes, envisager des mesurés plus fortes

## 6. Fiche d'Action Corrective (modèle)

### Identification

| Élément | Détail |
|---|---|
| **N. d'AC** | AC_[AAAA]_[NNN] |
| **Date d'ouverture** | [JJ/MM/AAAA] |
| **NC d'origine** | NC_[AAAA]_[NNNN] |
| **Source** | [ ] Réclamation client [ ] Retard transport [ ] Retard production [ ] Defaut production [ ] Etiquetage/Emballage [ ] CQ pre-expédition [ ] Audit interne [ ] Audit externe (SQS) [ ] Autre |

### Description du problème

| Élément | Détail |
|---|---|
| **Description** | [Description factuelle du problème] |
| **Impact sur le client** | [Consequences de la NC pour le client] |
| **Frequence/Recurrence** | [Première occurrence / Recurrente (combien de fois)] |

### Analyse des causes

| Élément | Détail |
|---|---|
| **Méthode utilisée** | [ ] 5 Pourquoi [ ] Autre |
| **Détail de l'analyse** | [Voir tableau des 5 Pourquoi] |
| **Cause racine identifiée** | [Description de la cause racine] |
| **Partenaire impliqué dans l'analyse** | [ ] Yuyao Mould Factory [ ] Whang [ ] Transporteur [ ] Analyse interne uniquement |

### Plan d'action

| # | Action corrective | Responsable | Délai | Statut |
|---|---|---|---|---|
| 1 | [Description de l'action] | [Gérante / Partenaire] | [Date] | [ ] Planifié [ ] En cours [ ] Réalisé |
| 2 | [Description de l'action] | [Gérante / Partenaire] | [Date] | [ ] Planifié [ ] En cours [ ] Réalisé |
| 3 | [Description de l'action] | [Gérante / Partenaire] | [Date] | [ ] Planifié [ ] En cours [ ] Réalisé |

### Vérification de l'efficacité

| Élément | Détail |
|---|---|
| **Date de vérification** | [JJ/MM/AAAA] (au moins 1-3 mois après mise en œuvre ou prochaines commandes) |
| **Méthode de vérification** | [Suivi des prochaines livraisons, absence de réclamation client, retour partenaire] |
| **Résultat** | [ ] Efficace (NC non recurrente) [ ] Non efficace (NC recurrente) |
| **Commentaire** | [Observations] |

### Clôture

| Élément | Détail |
|---|---|
| **Date de clôture** | [JJ/MM/AAAA] |
| **Clôturée par** | Roxane Wicky |
| **Statut final** | [ ] Soldée [ ] En cours [ ] Reouverture nécessaire |

---

### Exemple de fiche remplie : AC_2026_001

#### Identification

| Élément | Détail |
|---|---|
| **N. d'AC** | :green_circle: AC_2026_001 |
| **Date d'ouverture** | :green_circle: 10/02/2026 |
| **NC d'origine** | :green_circle: NC_2026_1001 |
| **Source** | :green_circle: [X] Etiquetage/Emballage |

#### Description du problème

| Élément | Détail |
|---|---|
| **Description** | :green_circle: Livraison d'un carton de 1000 pièces avec étiquetage incorrect (90.60.05710L au lieu de 90.60.05710) - SHIP_25058/CFM00057428 |
| **Impact sur le client** | :green_circle: Impact limité -- le produit physique est conforme, seule l'etiquette est erronee. Le client a accepte le produit en l'état (dérogation). |
| **Frequence/Recurrence** | :green_circle: Première occurrence |

#### Analyse des causes

| Élément | Détail |
|---|---|
| **Méthode utilisée** | :green_circle: [X] 5 Pourquoi |
| **Détail de l'analyse** | :red_circle: [À REMPLIR -- cause pas encore identifiée. L'analyse sera approfondie lors du voyage en Chine en mars 2026] |
| **Cause racine identifiée** | :red_circle: [À REMPLIR -- cause exacte pas encore identifiée] |
| **Partenaire impliqué dans l'analyse** | :green_circle: [X] Yuyao Mould Factory |

#### Plan d'action

| # | Action corrective | Responsable | Délai | Statut |
|---|---|---|---|---|
| 1 | Informer le fournisseur de la NC | :green_circle: Roxane Wicky | :green_circle: 10/02/2026 | :green_circle: [X] Réalisé |
| 2 | Créer une checklist de contrôle qualité complète | Roxane Wicky + Yuyao Mould Factory | Mars 2026 (voyage Chine) | [ ] En cours |
| 3 | Renforcer le CQ pre-expédition pour l'étiquetage | Yuyao Mould Factory | Mars 2026 (voyage Chine) | [ ] Planifié |

#### Vérification de l'efficacité

| Élément | Détail |
|---|---|
| **Date de vérification** | :red_circle: [À REMPLIR -- après mise en œuvre des actions, prochaines commandes de la référence 90.60.05710] |
| **Méthode de vérification** | Suivi des prochaines livraisons de cette référence, vérification de l'étiquetage |
| **Résultat** | :red_circle: [À REMPLIR -- en attente] |
| **Commentaire** | Suivi en cours. Cause exacte pas encore identifiée. Photos non disponibles. Le traitement sera renforce lors du voyage en Chine prévu en mars 2026. |

#### Clôture

| Élément | Détail |
|---|---|
| **Date de clôture** | :red_circle: [À REMPLIR -- en attente] |
| **Clôturée par** | Roxane Wicky |
| **Statut final** | :green_circle: [X] En cours |

---

## 7. Registre des actions correctives

| N. AC | Date ouv. | NC liée | Cause racine | Action | Délai | Efficace ? | Statut |
|---|---|---|---|---|---|---|---|
| :green_circle: AC_2026_001 | 10/02/2026 | NC_2026_1001 | :red_circle: Cause pas encore identifiée | 1. Informer le fournisseur (réalisé) 2. Créer une checklist de contrôle qualité complète 3. Renforcer le CQ pre-expédition pour l'étiquetage | Mars 2026 (voyage Chine) | En cours | En cours |
| AC_[AAAA]_[NNN] | [date] | NC_xxx | [résumé] | [résumé] | [date] | [O/N/En cours] | [Ouvert/Solde] |

---

## 8. Indicateurs

| Indicateur | Cible | Frequence |
|---|---|---|
| Nombre d'AC ouvertes | Information | Trimestriel |
| Repartition par type (transport, production, retard, étiquetage, CQ pre-expédition) | Information | Trimestriel |
| Taux de clôture dans les délais | > 80% | Trimestriel |
| Taux d'efficacité des AC | > 90% | Annuel |

---

> **Instructions de remplissage :**
> 1. N'ouvrez une AC que si c'est justifié (NC majeure, recurrente, ou d'audit)
> 2. Prenez le temps de bien analyser la cause racine -- c'est l'étape cle
> 3. La méthode des 5 Pourquoi est simple et efficace pour une micro-entreprise comme Plus Sarl
> 4. Impliquez les partenaires chinois (Yuyao Mould Factory ou Whang) dans l'analyse quand la NC vient de la fabrication
> 5. Documentez les échanges (emails, WeChat) comme preuves des actions correctives
> 6. L'auditeur (SQS) verifiera que vos AC sont efficaces (pas juste sur papier)
> 7. L'analyse des causes se fait dans la mesure des compétences de la gérante -- c'est une demarche d'amélioration continue
> 8. Le CQ pre-expédition avec echantillonnage peut être une source d'AC si des NC sont détectées avant livraison

---

## Historique des revisions

| Version | Date | Description de la modification | Auteur |
|---|---|---|---|
| 0.1 | 10/02/2026 | Création initiale | Roxane Wicky |
| 0.2 | 10/02/2026 | Ajout de la première action corrective reelle (AC_2026_001 liée à NC_2026_1001 - erreur d'étiquetage). Ajout du Scenario 4 (erreur d'étiquetage/emballage). Mise à jour du format de numérotation (underscores). Ajout de la categorie "Etiquetage/Emballage" dans les indicateurs. | Roxane Wicky |
| 0.3 | 12/02/2026 | Intégration des réponses (Whang, Paradiso, SQS, cloud, echantillonnage CQ). Ajout du système de légende des champs. | Roxane Wicky |
| 0.4 | 18/02/2026 | Intégration UPDATE 2.1 Processus 04 : ajout référence au lien avec le contrôle qualité formalisé (CTX-QUA-001, section 1.1). | Roxane Wicky |
