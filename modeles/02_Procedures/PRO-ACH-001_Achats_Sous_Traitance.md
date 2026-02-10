# Procedure Achats et Sous-Traitance

| | |
|---|---|
| **Reference** | PRO-ACH-001 |
| **Version** | 1.0 |
| **Date de creation** | [JJ/MM/AAAA] |
| **Date de revision** | [JJ/MM/AAAA] |
| **Redige par** | [Nom de la gerante] |
| **Approuve par** | [Nom de la gerante] |

---

## 1. Objet

Definir les regles de selection, d'evaluation et de maitrise des fournisseurs et sous-traitants, en particulier le partenaire chinois qui fabrique les moules et les pieces plastiques injectees.

> **Cette procedure est CRITIQUE pour DUMMY Sarl.** La fabrication etant entierement
> externalisee, la maitrise de ce processus est essentielle et sera examinee en
> detail par l'auditeur de certification.

## 2. Domaine d'application

Tous les achats et prestations externalisees ayant un impact sur la qualite des produits livres aux clients :
- Fabrication de moules (partenaire chinois)
- Injection de pieces plastiques (partenaire chinois)
- Transport international (transitaire)
- Tout autre fournisseur ayant un impact qualite

## 3. Responsabilites

| Responsabilite | Qui |
|---|---|
| Selection des fournisseurs | Gerante |
| Evaluation periodique | Gerante |
| Emission des commandes | Gerante |
| Definition des exigences techniques | Gerante |
| Suivi de fabrication | Gerante |
| Controle a reception | Gerante |

## 4. Classification des fournisseurs

| Classe | Critere | Exemples | Niveau de maitrise |
|---|---|---|---|
| **A - Critique** | Impact direct sur la qualite du produit | Partenaire chinois (moules + injection) | Evaluation annuelle formelle, accord qualite, suivi continu |
| **B - Important** | Impact indirect sur la qualite ou les delais | Transporteur, transitaire | Evaluation annuelle simplifiee |
| **C - Standard** | Impact faible sur la qualite | Fournitures de bureau, fiduciaire | Pas d'evaluation formelle |

## 5. Selection d'un nouveau fournisseur

### 5.1 Criteres de selection

| Critere | Poids | Evaluation |
|---|---|---|
| Capacite technique (equipements, savoir-faire) | [Eleve] | [/10] |
| Qualite (certifications, references, echantillons) | [Eleve] | [/10] |
| Delais de fabrication et de livraison | [Eleve] | [/10] |
| Prix et conditions commerciales | [Moyen] | [/10] |
| Communication et reactivite | [Moyen] | [/10] |
| Stabilite financiere | [Faible] | [/10] |
| Localisation geographique | [Faible] | [/10] |

### 5.2 Etapes de selection

| # | Etape | Description | Document |
|---|---|---|---|
| 1 | Identification | Rechercher des fournisseurs potentiels | Liste de fournisseurs |
| 2 | Demande d'information | Envoyer un questionnaire de pre-qualification | Questionnaire fournisseur |
| 3 | Evaluation initiale | Evaluer selon les criteres ci-dessus | Grille d'evaluation |
| 4 | Essai / Echantillon | Commander un echantillon ou un premier lot test | Bon de commande essai |
| 5 | Validation | Valider le fournisseur sur la base des resultats | FOR-EVF-001 |
| 6 | Accord qualite | Signer un accord qualite (fournisseur classe A) | Accord qualite |

## 6. Accord qualite avec le partenaire chinois

> **Document essentiel** : L'accord qualite formalise les exigences et les engagements
> reciproques entre DUMMY Sarl et le partenaire de fabrication.

### Contenu minimum de l'accord qualite

| Clause | Description | Statut |
|---|---|---|
| 1. Objet | Description des produits/services concernes | [ ] Inclus |
| 2. Exigences qualite | Specifications generales (tolerances, materiaux, finitions) | [ ] Inclus |
| 3. Documentation technique | Le partenaire doit recevoir les plans/CDC avant fabrication | [ ] Inclus |
| 4. Controle en cours de fabrication | Le partenaire effectue des controles et fournit des rapports | [ ] Inclus |
| 5. Controle final | Le partenaire effectue un controle final avant expedition | [ ] Inclus |
| 6. Rapport d'inspection | Le partenaire fournit un rapport d'inspection avec chaque livraison | [ ] Inclus |
| 7. Droit d'audit / visite | DUMMY Sarl peut auditer ou visiter l'usine | [ ] Inclus |
| 8. Gestion des NC | Processus de traitement des NC (delais, responsabilites) | [ ] Inclus |
| 9. Tracabilite | Le partenaire assure la tracabilite des lots (matiere, machine, date) | [ ] Inclus |
| 10. Modifications | Toute modification doit etre soumise et approuvee par DUMMY Sarl | [ ] Inclus |
| 11. Confidentialite | Protection des plans, specifications et donnees clients | [ ] Inclus |
| 12. Penalites / Litiges | Conditions en cas de non-respect | [ ] Inclus |
| 13. Duree et reconduction | Duree de l'accord et conditions de resiliation | [ ] Inclus |

## 7. Processus de commande

### 7.1 Logigramme

```
    Besoin identifie (commande client validee)
            |
            v
    +---------------------------+
    | 1. Preparer le cahier     |
    |    des charges (CDC)      |---> Plans, specifications, quantites, delais
    +---------------------------+
            |
            v
    +---------------------------+
    | 2. Revue du CDC           |---> Verification completude et clarte
    +---------------------------+
            |
            v
    +---------------------------+
    | 3. Envoyer au partenaire  |---> Email + pieces jointes
    |    chinois                |---> Demander un accuse de reception
    +---------------------------+
            |
            v
    +---------------------------+
    | 4. Confirmation et        |---> Le partenaire confirme faisabilite,
    |    planification          |     delai et prix
    +---------------------------+
            |
            v
    +---------------------------+
    | 5. Bon de commande        |---> Emission du bon de commande formel
    +---------------------------+
            |
            v
    +---------------------------+
    | 6. Suivi de fabrication   |---> Points d'etape (photos, rapports)
    +---------------------------+
            |
            v
    +---------------------------+
    | 7. Controle pre-expedition|---> Rapport d'inspection du partenaire
    |    (par le partenaire)    |
    +---------------------------+
            |
            v
    +---------------------------+
    | 8. Expedition             |---> Documents de transport, douane
    +---------------------------+
            |
            v
    +---------------------------+
    | 9. Controle a reception   |---> FOR-CTR-001 (voir formulaire)
    |    (par DUMMY Sarl)       |
    +---------------------------+
            |
       Conforme ?
       /        \
     OUI        NON
      |           |
      v           v
  Livraison    PRO-NCF-001
  au client
```

### 7.2 Contenu du cahier des charges (CDC)

Le CDC transmis au partenaire chinois doit contenir au minimum :

| Element | Detail | Obligatoire |
|---|---|---|
| Reference du projet/commande | Numero unique | OUI |
| Client final (si autorise) | Nom ou reference anonyme | Selon confidentialite |
| Plans techniques | Plans cotes au format [PDF/DWG/STEP] | OUI |
| Specifications matieres | Type de plastique, grade, couleur, fournisseur matiere | OUI |
| Tolerances dimensionnelles | Tolerances acceptables | OUI |
| Finition et aspect | Etat de surface, couleur, marquages | OUI |
| Quantites | Nombre de pieces / nombre d'empreintes (moule) | OUI |
| Delai souhaite | Date de livraison souhaitee | OUI |
| Criteres d'acceptation | Comment le produit sera controle a reception | OUI |
| Exigences d'emballage | Type d'emballage pour le transport | OUI |
| Exigences reglementaires | REACH, RoHS, alimentaire, etc. | Si applicable |
| Documents attendus | Rapport dimensionnel, certificat matiere, etc. | OUI |

## 8. Evaluation periodique des fournisseurs

### 8.1 Frequence

| Classe | Frequence d'evaluation |
|---|---|
| A - Critique | Annuelle (formelle) + suivi continu |
| B - Important | Annuelle (simplifiee) |
| C - Standard | Pas d'evaluation formelle |

### 8.2 Criteres d'evaluation (classe A)

Voir formulaire FOR-EVF-001 pour le detail.

| Critere | Poids | Mode de calcul |
|---|---|---|
| Qualite des livraisons | 40% | Taux de conformite (lots conformes / total lots) |
| Respect des delais | 30% | Taux de livraison a temps |
| Reactivite / Communication | 15% | Appreciation subjective (1 a 5) |
| Gestion des NC | 15% | Delai et efficacite de traitement des NC |

### 8.3 Actions selon le resultat

| Note globale | Appreciation | Action |
|---|---|---|
| >= 80% | Fournisseur performant | Maintien, eventuellement augmenter les volumes |
| 60-79% | Fournisseur acceptable | Plan d'amelioration a demander |
| < 60% | Fournisseur insuffisant | Plan d'amelioration urgent ou recherche d'alternative |

## 9. Liste des fournisseurs approuves

| Fournisseur | Classe | Produit/Service | Pays | Accord qualite | Derniere evaluation | Note | Statut |
|---|---|---|---|---|---|---|---|
| [Partenaire chinois] | A | Moules + injection | Chine | [ ] Oui [ ] Non | [Date] | [__/100] | Approuve |
| [Transporteur] | B | Transport international | [Pays] | [ ] N/A | [Date] | [__/100] | Approuve |
| [Autre fournisseur] | [A/B/C] | [Produit/Service] | [Pays] | [ ] | [Date] | [__/100] | [Statut] |

---

> **Instructions de remplissage :**
> 1. L'accord qualite avec le partenaire chinois est PRIORITAIRE - faites-le signer
> 2. Creez un modele de cahier des charges (CDC) standard pour vos commandes
> 3. Conservez TOUS les emails/echanges avec le partenaire chinois
> 4. L'auditeur voudra voir : accord qualite signe, CDC transmis, rapports d'inspection, evaluations
> 5. Si votre partenaire est certifie ISO 9001, conservez une copie du certificat
