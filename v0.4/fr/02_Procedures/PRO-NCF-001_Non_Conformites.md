# Procedure de Gestion des Non-Conformites

| | |
|---|---|
| **Reference** | PRO-NCF-001 |
| **Version** | 0.4 |
| **Date de creation** | 10/02/2026 |
| **Date de revision** | 18/02/2026 |
| **Redige par** | Roxane Wicky |
| **Approuve par** | Roxane Wicky |

> **Legende :** :red_circle: [A REMPLIR] = obligatoire, manquant | :yellow_circle: [RECOMMANDE] = recommande | :green_circle: = deja rempli | :blue_circle: [A VERIFIER] = a confirmer

---

## 1. Objet

Definir les regles de detection, d'enregistrement, de traitement et de suivi des non-conformites (NC) liees aux produits (moules, pieces plastiques, vis), aux processus et au SMQ de Plus Sarl.

> **Processus 04 — Controle qualite (cf. CTX-QUA-001, section 1.1) :** Avant l'expedition de la marchandise, Plus Sarl s'assure que les pieces produites sont conformes aux exigences techniques definies par le client et a la commande enregistree et validee. Cette verification repose sur le controle qualite realise par le fabricant, le suivi documentaire conserve sur FileMaker, l'analyse des retours clients par e-mail et la reception et traitement de toute information de non-conformite. En cas de NC : creation d'une fiche, decision de traitement, analyse des causes et mise en oeuvre d'actions correctives (cf. PRO-ACR-001). 🟢

## 2. Domaine d'application

Toutes les non-conformites detectees :
- Par les clients (~10 clients actifs) apres livraison (reclamations) -- source principale de detection
- Lors du suivi des expeditions (dommages transport, retards)
- Lors du suivi interne (erreurs d'etiquetage, de documentation, de quantite)
- Lors du controle qualite pre-expedition par les partenaires chinois
- Lors de la verification des echantillons recus chez Plus Sarl
- Lors des audits internes
- Lors des audits de certification (SQS)
- Lors du fonctionnement courant du SMQ

> **Note :** Plus Sarl ne receptionne pas physiquement les produits. Les marchandises sont expedites directement de Chine vers les clients europeens. Les non-conformites sont donc principalement detectees par les clients eux-memes apres reception des produits, ou par la gerante lors du suivi operationnel. Un processus de CQ pre-expedition avec envoi d'echantillons chez Plus Sarl en parallele du transport est en place (cf. PRO-ACH-001, section 8).

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
| Detecter et signaler les NC | :green_circle: Roxane Wicky, gerante (et clients, partenaires chinois) |
| Enregistrer les NC | :green_circle: Roxane Wicky, gerante |
| Analyser la situation et decider du traitement | :green_circle: Roxane Wicky, gerante |
| Mettre en oeuvre les corrections | :green_circle: Roxane Wicky, gerante |
| Coordonner avec les partenaires chinois | :green_circle: Roxane Wicky, gerante |
| Declencher les actions correctives | :green_circle: Roxane Wicky, gerante |
| Suivre la cloture | :green_circle: Roxane Wicky, gerante |

## 5. Sources de detection des NC

| Source | Exemples |
|---|---|
| **Reclamation client** | Client signale un defaut, un retard, une erreur de quantite, un probleme d'aspect |
| **Dommage transport** | Produits endommages pendant le transport (aerien, maritime, ferroviaire) |
| **Defaut de production** | Pieces non conformes aux specifications (dimensions, aspect, matiere) detectees par le client |
| **Erreur d'etiquetage/emballage** | Etiquettes incorrectes, confusion de references, erreur de conditionnement |
| **Retard de livraison** | Delai de production ou de transport non respecte |
| **CQ pre-expedition** | :green_circle: NC detectee lors du controle qualite avant expedition par le partenaire chinois |
| **Verification echantillons** | :green_circle: NC detectee lors de la verification des echantillons recus chez Plus Sarl en parallele de la livraison |
| **Suivi interne** | Detection par la gerante lors du suivi operationnel (verification documents, photos, echanges) |
| **Audit interne** | Constat d'audit (NC majeure ou mineure) |
| **Audit de certification** | Constat de l'organisme de certification (SQS) |
| **Retour du partenaire chinois** | Probleme signale pendant la fabrication par Yuyao Mould Factory ou Whang |
| **Fonctionnement courant** | Erreur de commande, oubli, document manquant |

> **Important :** Toutes les reclamations sont traitees independamment de la date a laquelle elles sont signalees par le client.

## 6. Procedure de traitement

### 6.1 Logigramme

```
    NC detectee (principalement par reclamation client,
    CQ pre-expedition ou verification echantillons)
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
    |    le fournisseur  |     (Yuyao Mould Factory ou Whang)
    |                    |     Discuter conditions financieres
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
- Numero unique : NC_[AAAA]_[NNNN] (ex : NC_2026_1001)
- Date de detection (date de la reclamation client ou du constat)
- Source de detection (reclamation client, dommage transport, suivi interne, CQ pre-expedition, verification echantillons, etc.)
- Description precise de la NC
- Produit/processus concerne
- Reference de la commande/projet (reference FileMaker)

**Format de numerotation :** NC_AAAA_NNNN
- AAAA = annee
- NNNN = numero sequentiel a 4 chiffres (1001, 1002, 1003, ...)
- Separateur : underscore (_)

**Etape 2 - Analyser la situation**

La gerante analyse la situation en evaluant :
- La gravite : Majeure / Mineure
- L'impact sur le client et sa satisfaction
- L'origine probable du probleme (defaut de production, transport, erreur de commande, etiquetage)
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

- Informer le partenaire chinois (Yuyao Mould Factory ou Whang) de la NC
- Discuter les conditions financieres en fonction de l'origine du probleme :
  - Si defaut de production : prise en charge par le partenaire chinois
  - Si dommage transport : reclamation aupres du transporteur
  - Si erreur d'etiquetage/emballage : correction par le partenaire chinois
  - Autres cas : negociation au cas par cas
- Demander au partenaire de conserver les informations de la NC pour les productions futures
- Demander un renforcement du CQ pre-expedition si la NC aurait pu etre detectee avant envoi

**Etape 6 - Verifier**

- Confirmer que le traitement est effectif (remplacement livre, client satisfait)
- S'assurer que le partenaire chinois a bien pris en compte la NC pour les prochaines productions
- Verifier que le CQ pre-expedition a ete ajuste si necessaire

## 7. Fiche de Non-Conformite (modele)

### En-tete

| Element | Detail |
|---|---|
| **N. de NC** | NC_[AAAA]_[NNNN] |
| **Date de detection** | [JJ/MM/AAAA] |
| **Detectee par** | [Nom du client / Source] |
| **Commande/Projet concerne** | [Reference FileMaker] |
| **Client concerne** | [Nom du client] |

### Description

| Element | Detail |
|---|---|
| **Produit concerne** | [Description du produit (moule, pieces plastiques, vis)] |
| **Description de la NC** | [Description factuelle et precise] |
| **Origine probable** | [ ] Defaut de production [ ] Dommage transport [ ] Retard [ ] Erreur de commande [ ] Emballage/Etiquetage [ ] CQ pre-expedition [ ] Verification echantillons [ ] Autre |
| **Exigence non satisfaite** | [Reference au plan, aux specifications, au contrat] |
| **Gravite** | [ ] Majeure [ ] Mineure |
| **Quantite concernee** | [Nombre de pieces / lots] |
| **Preuves** | [Photos, rapports du client, documents de transport, rapport CQ] |

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
| **Partenaire informe** | [ ] Yuyao Mould Factory [ ] Whang [ ] Transporteur |
| **Date d'information** | [JJ/MM/AAAA] |
| **Moyen de communication** | [ ] Email [ ] WeChat [ ] Autre |
| **Conditions financieres** | [Prise en charge fournisseur / partage / autre] |
| **Actions demandees au partenaire** | [Description : controles renforces, conservation des informations, ajustement CQ pre-expedition, etc.] |

### Action corrective associee

| Element | Detail |
|---|---|
| **Action corrective necessaire ?** | [ ] Oui - Ref : AC_[AAAA]_[NNN] [ ] Non (NC ponctuelle, non recurrente) |
| **Justification si non** | [Pourquoi pas d'action corrective] |

### Cloture

| Element | Detail |
|---|---|
| **Date de cloture** | [JJ/MM/AAAA] |
| **Cloturee par** | Roxane Wicky |
| **Statut** | [ ] Soldee [ ] En cours |

---

### Exemple de fiche remplie : NC_2026_1001

#### En-tete

| Element | Detail |
|---|---|
| **N. de NC** | :green_circle: NC_2026_1001 |
| **Date de detection** | :green_circle: 10/02/2026 |
| **Detectee par** | :green_circle: Suivi interne (Plus Sarl) |
| **Commande/Projet concerne** | :green_circle: SHIP_25058 / CFM00057428 / 90.60.05710 |
| **Client concerne** | :green_circle: [Client concerne par la commande CFM00057428] |

#### Description

| Element | Detail |
|---|---|
| **Produit concerne** | :green_circle: Pieces plastiques - reference 90.60.05710 |
| **Description de la NC** | :green_circle: Livraison d'un carton de 1000 pieces avec etiquetage incorrect (90.60.05710L au lieu de 90.60.05710) |
| **Origine probable** | :green_circle: [X] Emballage/Etiquetage |
| **Exigence non satisfaite** | :green_circle: Etiquetage conforme a la reference commandee |
| **Gravite** | :green_circle: [X] Mineure |
| **Quantite concernee** | :green_circle: 1000 pieces (1 carton) |
| **Preuves** | Photos non disponibles. :red_circle: [A REMPLIR -- photos demandees mais non encore recues] |

#### Analyse

| Element | Detail |
|---|---|
| **Analyse** | :green_circle: Erreur sur l'etiquetage uniquement, produit conforme. La reference imprimee sur l'etiquette est 90.60.05710L au lieu de 90.60.05710. Le produit physique est correct. |
| **Cause exacte** | :red_circle: [A REMPLIR -- cause pas encore identifiee] |
| **Suivi** | :green_circle: Suivi en cours |

#### Traitement immediat (correction)

| Element | Detail |
|---|---|
| **Decision** | :green_circle: [X] Derogation (acceptation client) |
| **Description de la correction** | :green_circle: Demande de photo de l'etiquetage pour validation. Le client accepte la marchandise en l'etat car le produit est conforme, seule l'etiquette est erronee. |
| **Accord client (si derogation)** | :green_circle: [X] Oui - Client accepte le produit en l'etat |
| **Date de mise en oeuvre** | :green_circle: 10/02/2026 |
| **Verification** | :green_circle: En cours - client en vacances, suivi a la reprise |

#### Coordination fournisseur

| Element | Detail |
|---|---|
| **Partenaire informe** | :green_circle: [X] Yuyao Mould Factory |
| **Date d'information** | :green_circle: 10/02/2026 |
| **Moyen de communication** | :green_circle: [X] WeChat |
| **Conditions financieres** | :red_circle: [A REMPLIR -- a determiner] |
| **Actions demandees au partenaire** | :green_circle: Corriger l'etiquetage pour les prochaines productions de cette reference. Verifier les etiquettes avant expedition. Renforcer le CQ pre-expedition. |

#### Action corrective associee

| Element | Detail |
|---|---|
| **Action corrective necessaire ?** | :green_circle: [X] Oui - Ref : AC_2026_001 |
| **Actions prevues** | :green_circle: 1. Informer le fournisseur (fait le 10/02/2026 via WeChat). 2. Creer une checklist de controle qualite complete. |
| **Delai** | :green_circle: Correction lors du voyage en Chine en mars 2026 |

#### Cloture

| Element | Detail |
|---|---|
| **Date de cloture** | :red_circle: [A REMPLIR -- en attente] |
| **Cloturee par** | Roxane Wicky |
| **Statut** | :green_circle: [X] En cours |

#### Commentaire

:green_circle: Le fournisseur confirme via WeChat que l'erreur concerne l'etiquetage et non le produit. Le produit livre est bien conforme a la reference 90.60.05710. Client en vacances, suivi a la reprise.

**Mise a jour 12/02/2026 :** Suivi en cours, photos non disponibles, cause exacte pas encore identifiee. L'action corrective AC_2026_001 reste ouverte. Le traitement sera renforce lors du voyage en Chine prevu en mars 2026.

---

## 8. Registre des non-conformites

| N. NC | Date | Source | Description resumee | Origine | Gravite | Traitement | Statut | AC associee |
|---|---|---|---|---|---|---|---|---|
| :green_circle: NC_2026_1001 | 10/02/2026 | Suivi interne | 1000 pieces livrees avec mauvaise etiquette (90.60.05710L au lieu de 90.60.05710) - SHIP_25058/CFM00057428. Suivi en cours, photos non disponibles, cause pas encore identifiee. | Emballage/Etiquetage | Mineure | Derogation (client accepte en l'etat). Informer fournisseur. Creer checklist controle qualite. | En cours | AC_2026_001 (En cours) |
| NC_[AAAA]_[NNNN] | [date] | [source] | [resume] | [production/transport/retard/etiquetage/CQ pre-expedition/autre] | [Maj/Min] | [decision] | [Ouvert/Solde] | [AC_xxx ou N/A] |

---

## 9. Indicateurs

| Indicateur | Formule | Cible | Frequence |
|---|---|---|---|
| Nombre de NC par trimestre | Comptage | Tendance a la baisse | Trimestriel |
| Repartition par origine | Comptage par categorie (production, transport, retard, etiquetage, CQ pre-expedition, autre) | Information | Trimestriel |
| Delai moyen de traitement | Moyenne (date cloture - date detection) | < 30 jours :blue_circle: [A VERIFIER] | Trimestriel |
| Taux de NC recurrentes | NC recurrentes / Total NC x 100 | < 10% | Annuel |
| Taux de remplacement | Remplacements / Total NC x 100 | Information | Annuel |
| NC detectees par CQ pre-expedition | Comptage | Information | Trimestriel |

---

> **Instructions de remplissage :**
> 1. Enregistrez TOUTE non-conformite signalee par un client ou detectee en interne, quelle que soit la date de signalement
> 2. Utilisez le format de numerotation NC_AAAA_NNNN (ex : NC_2026_1001)
> 3. Photographiez ou demandez au client de photographier les defauts quand c'est possible
> 4. Communiquez chaque NC produit au partenaire chinois concerne (Yuyao Mould Factory ou Whang)
> 5. Documentez les echanges par email ou WeChat avec les partenaires chinois
> 6. Analysez les tendances lors de la revue de direction
> 7. En cas de doute sur l'origine, privilegiez la satisfaction client (remplacement)
> 8. Verifiez si la NC aurait pu etre detectee lors du CQ pre-expedition et ajustez le processus si necessaire

---

## Historique des revisions

| Version | Date | Description de la modification | Auteur |
|---|---|---|---|
| 0.1 | 10/02/2026 | Creation initiale | Roxane Wicky |
| 0.2 | 10/02/2026 | Ajout de la premiere NC reelle (NC_2026_1001 - erreur d'etiquetage SHIP_25058/CFM00057428/90.60.05710). Ajout d'un exemple de fiche NC remplie en section 7. Mise a jour du format de numerotation (NC_AAAA_NNNN avec underscores). Ajout de la source de detection "Suivi interne" et de l'origine "Emballage/Etiquetage". | Roxane Wicky |
| 0.3 | 12/02/2026 | Integration des reponses (Whang, Paradiso, SQS, cloud, echantillonnage CQ). Ajout du systeme de legende des champs. | Roxane Wicky |
| 0.4 | 18/02/2026 | Integration UPDATE 2.1 Processus 04 : ajout reference au controle qualite pre-expedition formalise (CTX-QUA-001, section 1.1). | Roxane Wicky |
