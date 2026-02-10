# Procedure d'Actions Correctives

| | |
|---|---|
| **Reference** | PRO-ACR-001 |
| **Version** | 1.0 |
| **Date de creation** | [JJ/MM/AAAA] |
| **Date de revision** | [JJ/MM/AAAA] |
| **Redige par** | [Nom de la gerante] |
| **Approuve par** | [Nom de la gerante] |

---

## 1. Objet

Definir les regles d'analyse des causes, de mise en oeuvre et de verification de l'efficacite des actions correctives afin d'eliminer les causes des non-conformites et d'empecher leur recurrence.

## 2. Domaine d'application

Toute non-conformite necessitant une action corrective :
- NC majeures (systematiquement)
- NC mineures recurrentes
- NC d'audit interne ou externe
- Reclamations clients significatives
- Toute situation ou la gerante juge necessaire d'agir sur les causes

## 3. Definitions

| Terme | Definition |
|---|---|
| **Correction** | Action pour eliminer une NC detectee (traitement immediat du symptome) |
| **Action corrective** | Action pour eliminer la **cause** d'une NC et empecher sa recurrence |
| **Cause racine** | La cause fondamentale a l'origine de la NC |
| **Verification d'efficacite** | Controle que l'action corrective a bien empeche la recurrence de la NC |

> **Difference cle :**
> - Correction = "J'ai remplace la piece defectueuse" (symptome)
> - Action corrective = "J'ai modifie le cahier des charges pour preciser la tolerance" (cause)

## 4. Responsabilites

| Responsabilite | Qui |
|---|---|
| Decider de l'ouverture d'une AC | Gerante |
| Analyser les causes | Gerante (avec le partenaire chinois si NC de fabrication) |
| Definir l'action corrective | Gerante |
| Mettre en oeuvre | Gerante (ou partenaire chinois) |
| Verifier l'efficacite | Gerante |

## 5. Procedure

### 5.1 Logigramme

```
    NC necessitant une action corrective
    (voir criteres en section 2)
            |
            v
    +------------------------+
    | 1. Ouvrir la fiche AC  |---> AC-[AAAA]-[NNN]
    +------------------------+
            |
            v
    +------------------------+
    | 2. Analyser les causes |---> Methode des 5 Pourquoi / Ishikawa
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

- Attribuer un numero : AC-[AAAA]-[NNN]
- Lier a la NC d'origine (NC-[AAAA]-[NNN])
- Decrire le probleme

**Etape 2 - Analyser les causes**

Utiliser l'une des methodes suivantes :

#### Methode des 5 Pourquoi (recommandee pour DUMMY Sarl)

| # | Pourquoi ? | Reponse |
|---|---|---|
| 1 | Pourquoi la NC est-elle survenue ? | [Reponse 1] |
| 2 | Pourquoi [Reponse 1] ? | [Reponse 2] |
| 3 | Pourquoi [Reponse 2] ? | [Reponse 3] |
| 4 | Pourquoi [Reponse 3] ? | [Reponse 4] |
| 5 | Pourquoi [Reponse 4] ? | [Reponse 5 = cause racine probable] |

**Exemple concret :**

| # | Pourquoi ? | Reponse |
|---|---|---|
| 1 | Pourquoi les pieces sont-elles non conformes ? | Les dimensions ne correspondent pas au plan |
| 2 | Pourquoi les dimensions ne correspondent pas ? | Le partenaire a utilise un mauvais reglage machine |
| 3 | Pourquoi un mauvais reglage ? | Le cahier des charges ne precisait pas les tolerances |
| 4 | Pourquoi les tolerances n'etaient pas precisees ? | Le modele de cahier des charges n'inclut pas cette rubrique |
| 5 | **Cause racine** | **Le modele de cahier des charges est incomplet** |

-> **Action corrective** : Mettre a jour le modele de cahier des charges pour inclure systematiquement les tolerances dimensionnelles.

#### Diagramme d'Ishikawa (causes et effets) - pour les cas complexes

```
    Main d'oeuvre    Methode         Matiere
         |              |              |
         v              v              v
    +----|--------------|--------------|----+
    |                                       |
    |           PROBLEME (NC)               |
    |                                       |
    +----|--------------|--------------|----+
         ^              ^              ^
         |              |              |
      Milieu        Machine         Mesure
```

Categories a analyser :
- **Main d'oeuvre** : competences, formation, communication
- **Methode** : procedures, instructions, cahier des charges
- **Matiere** : matiere premiere, composants, fournisseur
- **Milieu** : environnement, conditions de transport/stockage
- **Machine** : equipement, outillage, moule
- **Mesure** : instruments, methode de controle, criteres

**Etape 3 - Identifier la cause racine**

- Selectionner la cause la plus probable
- Verifier par des donnees/preuves si possible

**Etape 4 - Definir l'action corrective**

L'action corrective doit :
- Agir sur la cause racine (pas sur le symptome)
- Etre realiste et proportionnee
- Avoir un responsable et un delai

**Etape 5 - Mettre en oeuvre**

- Realiser l'action
- Documenter ce qui a ete fait
- Communiquer si necessaire (partenaire chinois, client)

**Etape 6 - Verifier l'efficacite**

- Attendre un delai suffisant (generalement 1 a 3 mois)
- Verifier que la NC ne s'est pas reproduite
- Si la NC se reproduit : reprendre l'analyse des causes

## 6. Fiche d'Action Corrective (modele)

### Identification

| Element | Detail |
|---|---|
| **N. d'AC** | AC-[AAAA]-[NNN] |
| **Date d'ouverture** | [JJ/MM/AAAA] |
| **NC d'origine** | NC-[AAAA]-[NNN] |
| **Source** | [ ] Controle reception [ ] Reclamation client [ ] Audit interne [ ] Audit externe [ ] Autre |

### Description du probleme

| Element | Detail |
|---|---|
| **Description** | [Description factuelle du probleme] |
| **Impact** | [Consequences de la NC] |
| **Frequence/Recurrence** | [Premiere occurrence / Recurrente (combien de fois)] |

### Analyse des causes

| Element | Detail |
|---|---|
| **Methode utilisee** | [ ] 5 Pourquoi [ ] Ishikawa [ ] Autre |
| **Detail de l'analyse** | [Voir tableau des 5 Pourquoi ou diagramme] |
| **Cause racine identifiee** | [Description de la cause racine] |

### Plan d'action

| # | Action corrective | Responsable | Delai | Statut |
|---|---|---|---|---|
| 1 | [Description de l'action] | [Qui] | [Date] | [ ] Planifie [ ] En cours [ ] Realise |
| 2 | [Description de l'action] | [Qui] | [Date] | [ ] Planifie [ ] En cours [ ] Realise |
| 3 | [Description de l'action] | [Qui] | [Date] | [ ] Planifie [ ] En cours [ ] Realise |

### Verification de l'efficacite

| Element | Detail |
|---|---|
| **Date de verification** | [JJ/MM/AAAA] (au moins 1-3 mois apres mise en oeuvre) |
| **Methode de verification** | [Comment vous verifiez que la NC ne se reproduit pas] |
| **Resultat** | [ ] Efficace (NC non recurrente) [ ] Non efficace (NC recurrente) |
| **Commentaire** | [Observations] |

### Cloture

| Element | Detail |
|---|---|
| **Date de cloture** | [JJ/MM/AAAA] |
| **Cloturee par** | [Nom] |
| **Statut final** | [ ] Soldee [ ] En cours [ ] Reouverture necessaire |

---

## 7. Registre des actions correctives

| N. AC | Date ouv. | NC liee | Cause racine | Action | Delai | Efficace ? | Statut |
|---|---|---|---|---|---|---|---|
| AC-[AAAA]-001 | [date] | NC-xxx | [resume] | [resume] | [date] | [O/N/En cours] | [Ouvert/Solde] |
| AC-[AAAA]-002 | | | | | | | |
| AC-[AAAA]-003 | | | | | | | |

---

## 8. Indicateurs

| Indicateur | Cible | Frequence |
|---|---|---|
| Nombre d'AC ouvertes | Information | Trimestriel |
| Taux de cloture dans les delais | [> 80%] | Trimestriel |
| Taux d'efficacite des AC | [> 90%] | Annuel |

---

> **Instructions de remplissage :**
> 1. N'ouvrez une AC que si c'est justifie (NC majeure, recurrente, ou d'audit)
> 2. Prenez le temps de bien analyser la cause racine - c'est l'etape cle
> 3. La methode des 5 Pourquoi est simple et efficace pour une micro-entreprise
> 4. Impliquez le partenaire chinois dans l'analyse quand la NC vient de la fabrication
> 5. L'auditeur verifiera que vos AC sont efficaces (pas juste sur papier)
