# Procedure de Gestion des Non-Conformites

| | |
|---|---|
| **Reference** | PRO-NCF-001 |
| **Version** | 1.0 |
| **Date de creation** | [JJ/MM/AAAA] |
| **Date de revision** | [JJ/MM/AAAA] |
| **Redige par** | [Nom de la gerante] |
| **Approuve par** | [Nom de la gerante] |

---

## 1. Objet

Definir les regles de detection, d'enregistrement, de traitement et de suivi des non-conformites (NC) liees aux produits (moules et pieces plastiques), aux processus et au SMQ de DUMMY Sarl.

## 2. Domaine d'application

Toutes les non-conformites detectees :
- A la reception des produits du partenaire chinois
- Par les clients (reclamations)
- Lors des audits internes
- Lors du fonctionnement courant du SMQ

## 3. Definitions

| Terme | Definition |
|---|---|
| **Non-conformite (NC)** | Non-satisfaction d'une exigence (client, norme, reglementaire, interne) |
| **NC Majeure** | NC ayant un impact significatif sur la qualite du produit ou la satisfaction client |
| **NC Mineure** | NC ponctuelle, impact limite |
| **Correction** | Action immediate pour eliminer la NC detectee (traitement du symptome) |
| **Action corrective** | Action pour eliminer la cause de la NC et empecher sa recurrence (voir PRO-ACR-001) |
| **Derogation** | Autorisation d'utiliser un produit non conforme sous conditions |

## 4. Responsabilites

| Responsabilite | Qui |
|---|---|
| Detecter et signaler les NC | Gerante (et clients, partenaire chinois) |
| Enregistrer les NC | Gerante |
| Decider du traitement | Gerante |
| Mettre en oeuvre les corrections | Gerante |
| Declencher les actions correctives | Gerante |
| Suivre la cloture | Gerante |

## 5. Sources de detection des NC

| Source | Exemples |
|---|---|
| Controle a reception | Pieces non conformes aux specifications (dimensions, aspect, matiere) |
| Reclamation client | Client signale un defaut, un retard, une erreur |
| Audit interne | Constat d'audit (NC majeure ou mineure) |
| Audit de certification | Constat de l'organisme de certification |
| Retour du partenaire chinois | Probleme signale pendant la fabrication |
| Fonctionnement courant | Erreur de commande, oubli, document manquant |

## 6. Procedure de traitement

### 6.1 Logigramme

```
    NC detectee
        |
        v
    +-------------------+
    | 1. Enregistrer     |---> Fiche NC (numero, date, description)
    +-------------------+
        |
        v
    +-------------------+
    | 2. Isoler /        |---> Produit NC isole, identifie, mis a l'ecart
    |    Securiser       |
    +-------------------+
        |
        v
    +-------------------+
    | 3. Analyser        |---> Determiner la gravite et l'impact
    +-------------------+
        |
        v
    +-------------------+
    | 4. Decider du      |---> Voir 6.3 (options de traitement)
    |    traitement      |
    +-------------------+
        |
        v
    +-------------------+
    | 5. Mettre en       |---> Appliquer la decision
    |    oeuvre           |
    +-------------------+
        |
        v
    +-------------------+
    | 6. Verifier        |---> Confirmer que la NC est resolue
    +-------------------+
        |
        v
    NC Majeure ou recurrente ?
       /            \
     OUI            NON
      |               |
      v               v
    +----------+   +---------+
    | Ouvrir   |   | Cloturer|
    | Action   |   | la fiche|
    | Corrective|   | NC      |
    | PRO-ACR  |   +---------+
    +----------+
```

### 6.2 Detail des etapes

**Etape 1 - Enregistrer la NC**

Remplir la fiche de non-conformite avec :
- Numero unique (NC-[ANNEE]-[NNN], ex: NC-2026-001)
- Date de detection
- Source de detection
- Description precise de la NC
- Produit/processus concerne
- Reference de la commande/projet

**Etape 2 - Isoler / Securiser**

Pour les NC produit :
- Isoler physiquement le produit non conforme
- L'identifier clairement (etiquette "NON CONFORME")
- Empecher son utilisation ou sa livraison involontaire

**Etape 3 - Analyser**

- Determiner la gravite : Majeure / Mineure
- Evaluer l'impact sur le client
- Verifier si d'autres produits/lots sont concernes

**Etape 4 - Decider du traitement**

### 6.3 Options de traitement des produits non conformes

| Option | Description | Quand l'utiliser | Accord client |
|---|---|---|---|
| **Rebut** | Detruire ou retourner le produit | Produit inutilisable | Non necessaire |
| **Retouche** | Reparer pour rendre conforme | Defaut corrigeable | Non necessaire |
| **Reclassement** | Utiliser pour un autre usage | Produit utilisable autrement | A evaluer |
| **Derogation** | Accepter en l'etat malgre la NC | NC mineure, impact nul | **Obligatoire** |
| **Retour fournisseur** | Renvoyer au partenaire chinois | NC de fabrication | Non necessaire |

**Etape 5 - Mettre en oeuvre**

- Appliquer la decision
- Documenter les actions prises
- Si retour fournisseur : communiquer au partenaire chinois (email, rapport)

**Etape 6 - Verifier**

- Confirmer que le traitement est effectif
- S'assurer que le produit/processus est de nouveau conforme

## 7. Fiche de Non-Conformite (modele)

### En-tete

| Element | Detail |
|---|---|
| **N. de NC** | NC-[AAAA]-[NNN] |
| **Date de detection** | [JJ/MM/AAAA] |
| **Detectee par** | [Nom / Source] |
| **Commande/Projet concerne** | [Reference] |
| **Client concerne** | [Nom du client] |

### Description

| Element | Detail |
|---|---|
| **Produit/processus concerne** | [Description du produit ou du processus] |
| **Description de la NC** | [Description factuelle et precise] |
| **Exigence non satisfaite** | [Reference a la specification, au plan, a la norme, au contrat] |
| **Gravite** | [ ] Majeure [ ] Mineure |
| **Quantite concernee** | [Nombre de pieces / lots] |
| **Preuves** | [Photos, rapports de mesure, etc.] |

### Traitement immediat (correction)

| Element | Detail |
|---|---|
| **Decision** | [ ] Rebut [ ] Retouche [ ] Reclassement [ ] Derogation [ ] Retour fournisseur |
| **Description de la correction** | [Ce qui est fait immediatement] |
| **Accord client (si derogation)** | [ ] Oui - Ref : [___] [ ] Non applicable |
| **Date de mise en oeuvre** | [JJ/MM/AAAA] |
| **Verification** | [Resultat de la verification] |

### Action corrective associee

| Element | Detail |
|---|---|
| **Action corrective necessaire ?** | [ ] Oui - Ref : AC-[AAAA]-[NNN] [ ] Non (NC ponctuelle, non recurrente) |
| **Justification si non** | [Pourquoi pas d'action corrective] |

### Cloture

| Element | Detail |
|---|---|
| **Date de cloture** | [JJ/MM/AAAA] |
| **Cloturee par** | [Nom] |
| **Statut** | [ ] Soldee [ ] En cours |

---

## 8. Registre des non-conformites

| N. NC | Date | Source | Description resumee | Gravite | Traitement | Statut | AC associee |
|---|---|---|---|---|---|---|---|
| NC-[AAAA]-001 | [date] | [source] | [resume] | [Maj/Min] | [decision] | [Ouvert/Solde] | [AC-xxx ou N/A] |
| NC-[AAAA]-002 | | | | | | | |
| NC-[AAAA]-003 | | | | | | | |

---

## 9. Indicateurs

| Indicateur | Formule | Cible | Frequence |
|---|---|---|---|
| Nombre de NC par trimestre | Comptage | Tendance a la baisse | Trimestriel |
| Delai moyen de traitement | Moyenne (date cloture - date detection) | [< XX jours] | Trimestriel |
| Taux de NC recurrentes | NC recurrentes / Total NC x 100 | [< 10%] | Annuel |

---

> **Instructions de remplissage :**
> 1. Imprimez quelques fiches NC vierges et gardez-les a portee de main
> 2. Enregistrez TOUTE non-conformite, meme mineure (c'est une preuve pour l'auditeur)
> 3. Photographiez les defauts quand c'est possible
> 4. Communiquez chaque NC produit au partenaire chinois
> 5. Analysez les tendances lors de la revue de direction
