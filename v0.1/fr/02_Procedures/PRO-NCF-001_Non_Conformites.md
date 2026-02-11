# Procedure de Gestion des Non-Conformites

| | |
|---|---|
| **Reference** | PRO-NCF-001 |
| **Version** | 0.1 |
| **Date de creation** | 10/02/2026 |
| **Date de revision** | 10/02/2026 |
| **Redige par** | Roxane Wicky |
| **Approuve par** | Roxane Wicky |

---

## 1. Objet

Definir les regles de detection, d'enregistrement, de traitement et de suivi des non-conformites (NC) liees aux produits (moules et pieces plastiques), aux processus et au SMQ de Plus Sarl.

## 2. Domaine d'application

Toutes les non-conformites detectees :
- Par les clients apres livraison (reclamations) -- source principale de detection
- Lors du suivi des expeditions (dommages transport, retards)
- Lors des audits internes
- Lors du fonctionnement courant du SMQ

> **Note :** Plus Sarl ne receptionne pas physiquement les produits. Les marchandises sont expedites directement de Chine vers les clients europeens. Les non-conformites sont donc principalement detectees par les clients eux-memes apres reception des produits.

## 3. Definitions

| Terme | Definition |
|---|---|
| **Non-conformite (NC)** | Non-satisfaction d'une exigence (client, norme, reglementaire, interne) |
| **NC Majeure** | NC ayant un impact significatif sur la qualite du produit ou la satisfaction client |
| **NC Mineure** | NC ponctuelle, impact limite |
| **Correction** | Action immediate pour eliminer la NC detectee (traitement du symptome) |
| **Action corrective** | Action pour eliminer la cause de la NC et empecher sa recurrence (voir PRO-ACR-001) |
| **Derogation** | Autorisation d'utiliser un produit non conforme sous conditions (accord client) |

## 4. Responsabilites

| Responsabilite | Qui |
|---|---|
| Detecter et signaler les NC | Roxane Wicky, gerante (et clients, partenaires chinois) |
| Enregistrer les NC | Roxane Wicky, gerante |
| Analyser la situation et decider du traitement | Roxane Wicky, gerante |
| Mettre en oeuvre les corrections | Roxane Wicky, gerante |
| Coordonner avec les partenaires chinois | Roxane Wicky, gerante |
| Declencher les actions correctives | Roxane Wicky, gerante |
| Suivre la cloture | Roxane Wicky, gerante |

## 5. Sources de detection des NC

| Source | Exemples |
|---|---|
| **Reclamation client** | Client signale un defaut, un retard, une erreur de quantite, un probleme d'aspect |
| **Dommage transport** | Produits endommages pendant le transport (aerien, maritime, ferroviaire) |
| **Defaut de production** | Pieces non conformes aux specifications (dimensions, aspect, matiere) detectees par le client |
| **Retard de livraison** | Delai de production ou de transport non respecte |
| **Audit interne** | Constat d'audit (NC majeure ou mineure) |
| **Audit de certification** | Constat de l'organisme de certification |
| **Retour du partenaire chinois** | Probleme signale pendant la fabrication par Yuyao Mould Factory ou le second partenaire [nom A CONFIRMER] |
| **Fonctionnement courant** | Erreur de commande, oubli, document manquant |

> **Important :** Toutes les reclamations sont traitees independamment de la date a laquelle elles sont signalees par le client.

## 6. Procedure de traitement

### 6.1 Logigramme

```
    NC detectee (principalement par reclamation client)
        |
        v
    +-------------------+
    | 1. Enregistrer     |---> Fiche NC (numero, date, description)
    +-------------------+
        |
        v
    +-------------------+
    | 2. Analyser la     |---> La gerante analyse la situation :
    |    situation       |     gravite, impact, origine du probleme
    +-------------------+
        |
        v
    +-------------------+
    | 3. Decider du      |---> Voir 6.3 (options de traitement)
    |    traitement      |
    +-------------------+
        |
        v
    +-------------------+
    | 4. Mettre en       |---> Appliquer la decision
    |    oeuvre           |     (remplacement, derogation, etc.)
    +-------------------+
        |
        v
    +-------------------+
    | 5. Coordonner avec |---> Informer le partenaire chinois
    |    le fournisseur  |     Discuter conditions financieres
    +-------------------+
        |
        v
    +-------------------+
    | 6. Verifier        |---> Confirmer que la NC est resolue
    |                    |     et le client satisfait
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
- Numero unique (NC-[ANNEE]-[NNN], ex : NC-2026-001)
- Date de detection (date de la reclamation client ou du constat)
- Source de detection (reclamation client, dommage transport, etc.)
- Description precise de la NC
- Produit/processus concerne
- Reference de la commande/projet (reference FileMaker)

**Etape 2 - Analyser la situation**

La gerante analyse la situation en evaluant :
- La gravite : Majeure / Mineure
- L'impact sur le client et sa satisfaction
- L'origine probable du probleme (defaut de production, transport, erreur de commande)
- Si d'autres commandes/clients sont potentiellement concernes

**Etape 3 - Decider du traitement**

### 6.3 Options de traitement des produits non conformes

| Option | Description | Quand l'utiliser | Accord client |
|---|---|---|---|
| **Remplacement** | Relancer une production et expedier de nouveaux produits conformes | Option privilegiee -- garantir la satisfaction client | Non necessaire |
| **Derogation (acceptation par le client)** | Le client accepte le produit malgre la NC | NC mineure, client accepte en l'etat | **Obligatoire** |
| **Modification / retouche** | Produit modifie si techniquement faisable | Defaut corrigeable | A evaluer avec le client |
| **Produit laisse chez le client** | Produit defectueux laisse chez le client (rebut ou usage secondaire) | Rapatriement non economique | Accord client |
| **Recuperation du produit** | Produit defectueux recupere aupres du client | Si necessaire pour analyse ou retour | Non necessaire |

> **Principe directeur :** L'objectif premier est de garantir la satisfaction du client. En regle generale, les produits non conformes sont remplaces.

**Etape 4 - Mettre en oeuvre**

- Appliquer la decision (lancer le remplacement, organiser la modification, etc.)
- Documenter les actions prises
- Communiquer avec le client sur les delais et les solutions proposees

**Etape 5 - Coordonner avec le fournisseur**

- Informer le partenaire chinois (Yuyao Mould Factory ou le second partenaire [nom A CONFIRMER]) de la NC
- Discuter les conditions financieres en fonction de l'origine du probleme :
  - Si defaut de production : prise en charge par le partenaire chinois
  - Si dommage transport : reclamation aupres du transporteur
  - Autres cas : negociation au cas par cas
- Demander au partenaire de conserver les informations de la NC pour les productions futures

**Etape 6 - Verifier**

- Confirmer que le traitement est effectif (remplacement livre, client satisfait)
- S'assurer que le partenaire chinois a bien pris en compte la NC pour les prochaines productions

## 7. Fiche de Non-Conformite (modele)

### En-tete

| Element | Detail |
|---|---|
| **N. de NC** | NC-[AAAA]-[NNN] |
| **Date de detection** | [JJ/MM/AAAA] |
| **Detectee par** | [Nom du client / Source] |
| **Commande/Projet concerne** | [Reference FileMaker] |
| **Client concerne** | [Nom du client] |

### Description

| Element | Detail |
|---|---|
| **Produit concerne** | [Description du produit (moule, pieces plastiques)] |
| **Description de la NC** | [Description factuelle et precise] |
| **Origine probable** | [ ] Defaut de production [ ] Dommage transport [ ] Retard [ ] Erreur de commande [ ] Autre |
| **Exigence non satisfaite** | [Reference au plan, aux specifications, au contrat] |
| **Gravite** | [ ] Majeure [ ] Mineure |
| **Quantite concernee** | [Nombre de pieces / lots] |
| **Preuves** | [Photos, rapports du client, documents de transport] |

### Traitement immediat (correction)

| Element | Detail |
|---|---|
| **Decision** | [ ] Remplacement [ ] Derogation (acceptation client) [ ] Modification/retouche [ ] Produit laisse chez le client [ ] Recuperation du produit |
| **Description de la correction** | [Ce qui est fait immediatement] |
| **Accord client (si derogation)** | [ ] Oui - Ref : [___] [ ] Non applicable |
| **Date de mise en oeuvre** | [JJ/MM/AAAA] |
| **Verification** | [Resultat de la verification -- confirmation client] |

### Coordination fournisseur

| Element | Detail |
|---|---|
| **Partenaire informe** | [ ] Yuyao Mould Factory [ ] Second partenaire [nom A CONFIRMER] [ ] Transporteur |
| **Date d'information** | [JJ/MM/AAAA] |
| **Conditions financieres** | [Prise en charge fournisseur / partage / autre] |
| **Actions demandees au partenaire** | [Description : controles renforces, conservation des informations, etc.] |

### Action corrective associee

| Element | Detail |
|---|---|
| **Action corrective necessaire ?** | [ ] Oui - Ref : AC-[AAAA]-[NNN] [ ] Non (NC ponctuelle, non recurrente) |
| **Justification si non** | [Pourquoi pas d'action corrective] |

### Cloture

| Element | Detail |
|---|---|
| **Date de cloture** | [JJ/MM/AAAA] |
| **Cloturee par** | Roxane Wicky |
| **Statut** | [ ] Soldee [ ] En cours |

---

## 8. Registre des non-conformites

| N. NC | Date | Source | Description resumee | Origine | Gravite | Traitement | Statut | AC associee |
|---|---|---|---|---|---|---|---|---|
| NC-[AAAA]-001 | [date] | [source] | [resume] | [production/transport/retard/autre] | [Maj/Min] | [decision] | [Ouvert/Solde] | [AC-xxx ou N/A] |
| NC-[AAAA]-002 | | | | | | | | |
| NC-[AAAA]-003 | | | | | | | | |

---

## 9. Indicateurs

| Indicateur | Formule | Cible | Frequence |
|---|---|---|---|
| Nombre de NC par trimestre | Comptage | Tendance a la baisse | Trimestriel |
| Repartition par origine | Comptage par categorie (production, transport, retard, autre) | Information | Trimestriel |
| Delai moyen de traitement | Moyenne (date cloture - date detection) | < 30 jours [A CONFIRMER] | Trimestriel |
| Taux de NC recurrentes | NC recurrentes / Total NC x 100 | < 10% | Annuel |
| Taux de remplacement | Remplacements / Total NC x 100 | Information | Annuel |

---

> **Instructions de remplissage :**
> 1. Enregistrez TOUTE non-conformite signalee par un client, quelle que soit la date de signalement
> 2. Photographiez ou demandez au client de photographier les defauts quand c'est possible
> 3. Communiquez chaque NC produit au partenaire chinois concerne (Yuyao Mould Factory ou second partenaire)
> 4. Documentez les echanges par email ou WeChat avec les partenaires chinois
> 5. Analysez les tendances lors de la revue de direction
> 6. En cas de doute sur l'origine, privilegiez la satisfaction client (remplacement)
