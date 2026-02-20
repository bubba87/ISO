# Procédure de Gestion des Non-Conformites

| | |
|---|---|
| **Référence** | PRO-NCF-001 |
| **Version** | 0.4 |
| **Date de création** | 10/02/2026 |
| **Date de revision** | 18/02/2026 |
| **Rédigé par** | Roxane Wicky |
| **Approuve par** | Roxane Wicky |

> **Légende :** :red_circle: [À REMPLIR] = obligatoire, manquant | :yellow_circle: [RECOMMANDE] = recommandé | :green_circle: = déjà rempli | :blue_circle: [À VÉRIFIER] = a confirmer

---

## 1. Objet

Définir les règles de detection, d'enregistrement, de traitement et de suivi des non-conformites (NC) liées aux produits (moules, pièces plastiques, vis), aux processus et au SMQ de Plus Sarl.

> **Processus 04 — Contrôle qualité (cf. CTX-QUA-001, section 1.1) :** Avant l'expédition de la marchandise, Plus Sarl s'assure que les pièces produites sont conformes aux exigences techniques définies par le client et à la commande enregistrée et validée. Cette vérification repose sur le contrôle qualité réalisé par le fabricant, le suivi documentaire conserve sur FileMaker, l'analyse des retours clients par e-mail et la reception et traitement de toute information de non-conformité. En cas de NC : création d'une fiche, decision de traitement, analyse des causes et mise en œuvre d'actions correctives (cf. PRO-ACR-001). 🟢

## 2. Domaine d'application

Toutes les non-conformites détectées :
- Par les clients (~10 clients actifs) après livraison (réclamations) -- source principale de detection
- Lors du suivi des expéditions (dommages transport, retards)
- Lors du suivi interne (erreurs d'étiquetage, de documentation, de quantité)
- Lors du contrôle qualité pre-expédition par les partenaires chinois
- Lors de la vérification des échantillons reçus chez Plus Sarl
- Lors des audits internes
- Lors des audits de certification (SQS)
- Lors du fonctionnement courant du SMQ

> **Note :** Plus Sarl ne réceptionne pas physiquement les produits. Les marchandises sont expédiées directement de Chine vers les clients européens. Les non-conformites sont donc principalement détectées par les clients eux-memes après reception des produits, ou par la gérante lors du suivi opérationnel. Un processus de CQ pre-expédition avec envoi d'échantillons chez Plus Sarl en parallèle du transport est en place (cf. PRO-ACH-001, section 8).

## 3. Definitions

| Terme | Definition |
|---|---|
| **Non-conformité (NC)** | Non-satisfaction d'une exigence (client, norme, réglementaire, interne) |
| **NC Majeure** | NC ayant un impact significatif sur la qualité du produit ou la satisfaction client |
| **NC Mineure** | NC ponctuelle, impact limité |
| **Correction** | Action immédiate pour eliminer la NC détectée (traitement du symptome) |
| **Action corrective** | Action pour eliminer la cause de la NC et empecher sa recurrence (voir PRO-ACR-001) |
| **Derogation** | Autorisation d'utiliser un produit non conforme sous conditions (accord client) |

## 4. Responsabilités

| Responsabilité | Qui |
|---|---|
| Detecter et signaler les NC | :green_circle: Roxane Wicky, gérante (et clients, partenaires chinois) |
| Enregistrer les NC | :green_circle: Roxane Wicky, gérante |
| Analyser la situation et decider du traitement | :green_circle: Roxane Wicky, gérante |
| Mettre en œuvre les corrections | :green_circle: Roxane Wicky, gérante |
| Coordonner avec les partenaires chinois | :green_circle: Roxane Wicky, gérante |
| Declencher les actions correctives | :green_circle: Roxane Wicky, gérante |
| Suivre la clôture | :green_circle: Roxane Wicky, gérante |

## 5. Sources de detection des NC

| Source | Exemples |
|---|---|
| **Réclamation client** | Client signalé un defaut, un retard, une erreur de quantité, un problème d'aspect |
| **Dommage transport** | Produits endommagés pendant le transport (aérien, maritime, ferroviaire) |
| **Defaut de production** | Pièces non conformes aux spécifications (dimensions, aspect, matière) détectées par le client |
| **Erreur d'étiquetage/emballage** | Etiquettes incorrectes, confusion de références, erreur de conditionnement |
| **Retard de livraison** | Délai de production ou de transport non respecte |
| **CQ pre-expédition** | :green_circle: NC détectée lors du contrôle qualité avant expédition par le partenaire chinois |
| **Vérification échantillons** | :green_circle: NC détectée lors de la vérification des échantillons reçus chez Plus Sarl en parallèle de la livraison |
| **Suivi interne** | Detection par la gérante lors du suivi opérationnel (vérification documents, photos, échanges) |
| **Audit interne** | Constat d'audit (NC majeure ou mineure) |
| **Audit de certification** | Constat de l'organisme de certification (SQS) |
| **Retour du partenaire chinois** | Problème signalé pendant la fabrication par Yuyao Mould Factory ou Whang |
| **Fonctionnement courant** | Erreur de commande, oubli, document manquant |

> **Important :** Toutes les réclamations sont traitées independamment de la date a laquelle elles sont signalees par le client.

## 6. Procédure de traitement

### 6.1 Logigramme

```
    NC détectée (principalement par reclamation client,
    CQ pre-expédition ou vérification échantillons)
        |
        v
    +-------------------+
    | 1. Enregistrer     |---> Fiche NC (numéro, date, description)
    +-------------------+
        |
        v
    +-------------------+
    | 2. Analyser la     |---> La gerante analyse la situation :
    |    situation       |     gravite, impact, origine du problème
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
    |    oeuvre           |     (remplacement, dérogation, etc.)
    +-------------------+
        |
        v
    +-------------------+
    | 5. Coordonner avec |---> Informer le partenaire chinois
    |    le fournisseur  |     (Yuyao Mould Factory ou Whang)
    |                    |     Discuter conditions financières
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
    | Ouvrir   |   | Clôturer|
    | Action   |   | la fiche|
    | Corrective|   | NC      |
    | PRO-ACR  |   +---------+
    +----------+
```

### 6.2 Détail des étapes

**Étape 1 - Enregistrer la NC**

Remplir la fiche de non-conformité avec :
- Numéro unique : NC_[AAAA]_[NNNN] (ex : NC_2026_1001)
- Date de detection (date de la réclamation client ou du constat)
- Source de detection (réclamation client, dommage transport, suivi interne, CQ pre-expédition, vérification échantillons, etc.)
- Description precise de la NC
- Produit/processus concerné
- Référence de la commande/projet (référence FileMaker)

**Format de numérotation :** NC_AAAA_NNNN
- AAAA = année
- NNNN = numéro sequentiel a 4 chiffrés (1001, 1002, 1003, ...)
- Separateur : underscore (_)

**Étape 2 - Analyser la situation**

La gérante analyse la situation en evaluant :
- La gravite : Majeure / Mineure
- L'impact sur le client et sa satisfaction
- L'origine probable du problème (defaut de production, transport, erreur de commande, étiquetage)
- Si d'autres commandes/clients sont potentiellement concernés

**Étape 3 - Decider du traitement**

### 6.3 Options de traitement des produits non conformes

| Option | Description | Quand l'utiliser | Accord client |
|---|---|---|---|
| **Remplacement** | Relancer une production et expédier de nouveaux produits conformes | Option privilegiee -- garantir la satisfaction client | Non nécessaire |
| **Derogation (acceptation par le client)** | Le client accepte le produit malgre la NC | NC mineure, client accepte en l'état | **Obligatoire** |
| **Modification / retouche** | Produit modifie si techniquement faisable | Defaut corrigeable | A évaluer avec le client |
| **Produit laisse chez le client** | Produit defectueux laisse chez le client (rebut ou usage secondaire) | Rapatriement non économique | Accord client |
| **Recuperation du produit** | Produit defectueux recupere auprès du client | Si nécessaire pour analyse ou retour | Non nécessaire |

> **Principe directeur :** L'objectif premier est de garantir la satisfaction du client. En règle générale, les produits non conformes sont remplacés.

**Étape 4 - Mettre en œuvre**

- Appliquer la decision (lancer le remplacement, organiser la modification, etc.)
- Documenter les actions prises
- Communiquer avec le client sur les délais et les solutions proposées

**Étape 5 - Coordonner avec le fournisseur**

- Informer le partenaire chinois (Yuyao Mould Factory ou Whang) de la NC
- Discuter les conditions financières en fonction de l'origine du problème :
  - Si defaut de production : prise en charge par le partenaire chinois
  - Si dommage transport : réclamation auprès du transporteur
  - Si erreur d'étiquetage/emballage : correction par le partenaire chinois
  - Autres cas : négociation au cas par cas
- Demander au partenaire de conserver les informations de la NC pour les productions futures
- Demander un renforcement du CQ pre-expédition si la NC aurait pu être détectée avant envoi

**Étape 6 - Vérifier**

- Confirmer que le traitement est effectif (remplacement livre, client satisfait)
- S'assurer que le partenaire chinois a bien pris en compte la NC pour les prochaines productions
- Vérifier que le CQ pre-expédition a été ajuste si nécessaire

## 7. Fiche de Non-Conformité (modèle)

### En-tete

| Élément | Détail |
|---|---|
| **N. de NC** | NC_[AAAA]_[NNNN] |
| **Date de detection** | [JJ/MM/AAAA] |
| **Détectée par** | [Nom du client / Source] |
| **Commande/Projet concerné** | [Référence FileMaker] |
| **Client concerné** | [Nom du client] |

### Description

| Élément | Détail |
|---|---|
| **Produit concerné** | [Description du produit (moule, pièces plastiques, vis)] |
| **Description de la NC** | [Description factuelle et precise] |
| **Origine probable** | [ ] Defaut de production [ ] Dommage transport [ ] Retard [ ] Erreur de commande [ ] Emballage/Etiquetage [ ] CQ pre-expédition [ ] Vérification échantillons [ ] Autre |
| **Exigence non satisfaite** | [Référence au plan, aux spécifications, au contrat] |
| **Gravite** | [ ] Majeure [ ] Mineure |
| **Quantité concernée** | [Nombre de pièces / lots] |
| **Preuves** | [Photos, rapports du client, documents de transport, rapport CQ] |

### Traitement immédiat (correction)

| Élément | Détail |
|---|---|
| **Decision** | [ ] Remplacement [ ] Derogation (acceptation client) [ ] Modification/retouche [ ] Produit laisse chez le client [ ] Recuperation du produit |
| **Description de la correction** | [Ce qui est fait immédiatement] |
| **Accord client (si dérogation)** | [ ] Oui - Ref : [___] [ ] Non applicable |
| **Date de mise en œuvre** | [JJ/MM/AAAA] |
| **Vérification** | [Résultat de la vérification -- confirmation client] |

### Coordination fournisseur

| Élément | Détail |
|---|---|
| **Partenaire informe** | [ ] Yuyao Mould Factory [ ] Whang [ ] Transporteur |
| **Date d'information** | [JJ/MM/AAAA] |
| **Moyen de communication** | [ ] Email [ ] WeChat [ ] Autre |
| **Conditions financières** | [Prise en charge fournisseur / partage / autre] |
| **Actions demandees au partenaire** | [Description : contrôles renforces, conservation des informations, ajustement CQ pre-expédition, etc.] |

### Action corrective associée

| Élément | Détail |
|---|---|
| **Action corrective nécessaire ?** | [ ] Oui - Ref : AC_[AAAA]_[NNN] [ ] Non (NC ponctuelle, non recurrente) |
| **Justification si non** | [Pourquoi pas d'action corrective] |

### Clôture

| Élément | Détail |
|---|---|
| **Date de clôture** | [JJ/MM/AAAA] |
| **Clôturée par** | Roxane Wicky |
| **Statut** | [ ] Soldée [ ] En cours |

---

### Exemple de fiche remplie : NC_2026_1001

#### En-tete

| Élément | Détail |
|---|---|
| **N. de NC** | :green_circle: NC_2026_1001 |
| **Date de detection** | :green_circle: 10/02/2026 |
| **Détectée par** | :green_circle: Suivi interne (Plus Sarl) |
| **Commande/Projet concerné** | :green_circle: SHIP_25058 / CFM00057428 / 90.60.05710 |
| **Client concerné** | :green_circle: [Client concerné par la commande CFM00057428] |

#### Description

| Élément | Détail |
|---|---|
| **Produit concerné** | :green_circle: Pièces plastiques - référence 90.60.05710 |
| **Description de la NC** | :green_circle: Livraison d'un carton de 1000 pièces avec étiquetage incorrect (90.60.05710L au lieu de 90.60.05710) |
| **Origine probable** | :green_circle: [X] Emballage/Etiquetage |
| **Exigence non satisfaite** | :green_circle: Etiquetage conforme à la référence commandee |
| **Gravite** | :green_circle: [X] Mineure |
| **Quantité concernée** | :green_circle: 1000 pièces (1 carton) |
| **Preuves** | Photos non disponibles. :red_circle: [À REMPLIR -- photos demandees mais non encore reçues] |

#### Analyse

| Élément | Détail |
|---|---|
| **Analyse** | :green_circle: Erreur sur l'étiquetage uniquement, produit conforme. La référence imprimée sur l'etiquette est 90.60.05710L au lieu de 90.60.05710. Le produit physique est correct. |
| **Cause exacte** | :red_circle: [À REMPLIR -- cause pas encore identifiée] |
| **Suivi** | :green_circle: Suivi en cours |

#### Traitement immédiat (correction)

| Élément | Détail |
|---|---|
| **Decision** | :green_circle: [X] Derogation (acceptation client) |
| **Description de la correction** | :green_circle: Demande de photo de l'étiquetage pour validation. Le client accepte la marchandise en l'état car le produit est conforme, seule l'etiquette est erronee. |
| **Accord client (si dérogation)** | :green_circle: [X] Oui - Client accepte le produit en l'état |
| **Date de mise en œuvre** | :green_circle: 10/02/2026 |
| **Vérification** | :green_circle: En cours - client en vacances, suivi à la reprise |

#### Coordination fournisseur

| Élément | Détail |
|---|---|
| **Partenaire informe** | :green_circle: [X] Yuyao Mould Factory |
| **Date d'information** | :green_circle: 10/02/2026 |
| **Moyen de communication** | :green_circle: [X] WeChat |
| **Conditions financières** | :red_circle: [À REMPLIR -- a determiner] |
| **Actions demandees au partenaire** | :green_circle: Corriger l'étiquetage pour les prochaines productions de cette référence. Vérifier les etiquettes avant expédition. Renforcer le CQ pre-expédition. |

#### Action corrective associée

| Élément | Détail |
|---|---|
| **Action corrective nécessaire ?** | :green_circle: [X] Oui - Ref : AC_2026_001 |
| **Actions prévues** | :green_circle: 1. Informer le fournisseur (fait le 10/02/2026 via WeChat). 2. Créer une checklist de contrôle qualité complète. |
| **Délai** | :green_circle: Correction lors du voyage en Chine en mars 2026 |

#### Clôture

| Élément | Détail |
|---|---|
| **Date de clôture** | :red_circle: [À REMPLIR -- en attente] |
| **Clôturée par** | Roxane Wicky |
| **Statut** | :green_circle: [X] En cours |

#### Commentaire

:green_circle: Le fournisseur confirmé via WeChat que l'erreur concerné l'étiquetage et non le produit. Le produit livre est bien conforme à la référence 90.60.05710. Client en vacances, suivi à la reprise.

**Mise à jour 12/02/2026 :** Suivi en cours, photos non disponibles, cause exacte pas encore identifiée. L'action corrective AC_2026_001 reste ouverte. Le traitement sera renforce lors du voyage en Chine prévu en mars 2026.

---

## 8. Registre des non-conformites

| N. NC | Date | Source | Description résumée | Origine | Gravite | Traitement | Statut | AC associée |
|---|---|---|---|---|---|---|---|---|
| :green_circle: NC_2026_1001 | 10/02/2026 | Suivi interne | 1000 pièces livrées avec mauvaise etiquette (90.60.05710L au lieu de 90.60.05710) - SHIP_25058/CFM00057428. Suivi en cours, photos non disponibles, cause pas encore identifiée. | Emballage/Etiquetage | Mineure | Derogation (client accepte en l'état). Informer fournisseur. Créer checklist contrôle qualité. | En cours | AC_2026_001 (En cours) |
| NC_[AAAA]_[NNNN] | [date] | [source] | [résumé] | [production/transport/retard/étiquetage/CQ pre-expédition/autre] | [Maj/Min] | [decision] | [Ouvert/Solde] | [AC_xxx ou N/A] |

---

## 9. Indicateurs

| Indicateur | Formule | Cible | Frequence |
|---|---|---|---|
| Nombre de NC par trimestre | Comptage | Tendance à la baisse | Trimestriel |
| Repartition par origine | Comptage par categorie (production, transport, retard, étiquetage, CQ pre-expédition, autre) | Information | Trimestriel |
| Délai moyen de traitement | Moyenne (date clôture - date detection) | < 30 jours :blue_circle: [À VÉRIFIER] | Trimestriel |
| Taux de NC recurrentes | NC recurrentes / Total NC x 100 | < 10% | Annuel |
| Taux de remplacement | Remplacements / Total NC x 100 | Information | Annuel |
| NC détectées par CQ pre-expédition | Comptage | Information | Trimestriel |

---

> **Instructions de remplissage :**
> 1. Enregistrez TOUTE non-conformité signalée par un client ou détectée en interne, quelle que soit la date de signalement
> 2. Utilisez le format de numérotation NC_AAAA_NNNN (ex : NC_2026_1001)
> 3. Photographiez ou demandez au client de photographier les defauts quand c'est possible
> 4. Communiquez chaque NC produit au partenaire chinois concerné (Yuyao Mould Factory ou Whang)
> 5. Documentez les échanges par email ou WeChat avec les partenaires chinois
> 6. Analysez les tendances lors de la revue de direction
> 7. En cas de doute sur l'origine, privilegiez la satisfaction client (remplacement)
> 8. Verifiez si la NC aurait pu être détectée lors du CQ pre-expédition et ajustez le processus si nécessaire

---

## Historique des revisions

| Version | Date | Description de la modification | Auteur |
|---|---|---|---|
| 0.1 | 10/02/2026 | Création initiale | Roxane Wicky |
| 0.2 | 10/02/2026 | Ajout de la première NC reelle (NC_2026_1001 - erreur d'étiquetage SHIP_25058/CFM00057428/90.60.05710). Ajout d'un exemple de fiche NC remplie en section 7. Mise à jour du format de numérotation (NC_AAAA_NNNN avec underscores). Ajout de la source de detection "Suivi interne" et de l'origine "Emballage/Etiquetage". | Roxane Wicky |
| 0.3 | 12/02/2026 | Intégration des réponses (Whang, Paradiso, SQS, cloud, echantillonnage CQ). Ajout du système de légende des champs. | Roxane Wicky |
| 0.4 | 18/02/2026 | Intégration UPDATE 2.1 Processus 04 : ajout référence au contrôle qualité pre-expédition formalisé (CTX-QUA-001, section 1.1). | Roxane Wicky |
