# Fiche Processus O2 - Achats et Sous-traitance

| | |
|---|---|
| **Reference** | FIC-PRO-001 |
| **Version** | 0.4 |
| **Date de creation** | 10/02/2026 |
| **Date de revision** | 18/02/2026 |
| **Redige par** | Roxane Wicky |
| **Approuve par** | Roxane Wicky |

> **Legende :** 🔴 [A REMPLIR] = obligatoire, manquant | 🟡 [RECOMMANDE] = recommande | 🟢 = deja rempli | 🔵 [A VERIFIER] = a confirmer

---

## Identification du processus

| Element | Description |
|---|---|
| **Nom du processus** | Achats et Sous-traitance |
| **Code** | O2 |
| **Type** | Operationnel |
| **Pilote** | Roxane Wicky (Gerante) |
| **Finalite** | Coordonner les partenaires chinois (Yuyao Mould Factory et **Whang**, Yuyao) pour assurer la fabrication des pieces, moules et vis conformement aux specifications des clients europeens, dans le respect des delais, des prix et des exigences qualite. |

---

## Donnees d'entree et de sortie

| Donnees d'entree (inputs) | Provenance |
|---|---|
| Specifications techniques du client (plans, cahier des charges, tolerances, materiaux) | Client via processus O1 - Commercial |
| Delais de livraison convenus avec le client | Processus O1 - Commercial |
| Offre validee par le client, confirmation de commande | Processus O1 - Commercial |
| Historique des commandes et des prix | S1 - Gestion documentaire (FileMaker) |
| Retour sur les non-conformites precedentes | Processus O4 - Controle qualite |

| Donnees de sortie (outputs) | Destinataire |
|---|---|
| Commande de fabrication transmise au partenaire chinois | Yuyao Mould Factory / Whang |
| Confirmation de faisabilite et de delai de fabrication | Processus O1 - Commercial (pour information au client) |
| Rapports de suivi de fabrication (photos, rapports d'etape) | Interne / Client si demande |
| Produits fabriques prets a l'expedition | Processus O3 - Logistique et livraison |
| Documents d'exportation (facture douaniere, packing list) | Processus O3 - Logistique et livraison |
| Rapports d'inspection fournisseur | Processus O4 - Controle qualite |
| Echantillons envoyes en parallele de l'expedition | Plus Sarl (controle de conformite) 🟢 |
| Evaluation des performances fournisseur | Processus M2 - Amelioration continue |

---

## Description des activites

| # | Activite | Description | Responsable | Document/Enregistrement |
|---|---|---|---|---|
| 1 | Revue de commande et reception des specifications | Recevoir du processus commercial les specifications techniques, plans, cahier des charges et exigences du client. Verifier la completude du dossier. Realiser l'analyse prealable selon M1-DIR-001 (cf. CTX-QUA-001 section 1.3). | Roxane Wicky | Cahier des charges client, plans techniques, email de transmission, fiche commande FileMaker |
| 1b | Creation de la fiche de production FileMaker | Creer la fiche de production dans le systeme FileMaker : caracteristiques attendues du produit, delai de fabrication, suivi de production. Cette fiche est mise a jour tout au long de la fabrication (cf. PRO-ACH-001, section 9). 🟢 | Roxane Wicky | Fiche de production FileMaker |
| 2 | Consultation du/des partenaire(s) chinois | Transmettre les specifications a Yuyao Mould Factory (partenaire principal) ou a **Whang** (Yuyao — specialise dans la fabrication de vis) selon la nature du projet. Demander une analyse de faisabilite, un devis et un delai. Communication par email et WeChat. | Roxane Wicky | Emails, messages WeChat, devis fournisseur |
| 3 | Echanges techniques iteratifs | Coordonner les allers-retours entre le client et le partenaire chinois jusqu'a obtenir une solution technique validee (materiaux, tolerances, procede de fabrication, prix). Traduire et adapter les exigences si necessaire. | Roxane Wicky | Emails, messages WeChat, comptes-rendus d'echanges |
| 4 | Validation et passation de commande | Une fois la solution technique et le prix valides par le client, emettre la commande de fabrication au partenaire chinois. Etablir les documents de commande (facture douaniere, bon de commande). | Roxane Wicky | Bon de commande, facture douaniere, confirmation de commande |
| 5 | Suivi de fabrication | Suivre l'avancement de la production aupres du partenaire chinois. Recevoir et analyser les photos, rapports d'etape, rapports d'inspection. Intervenir en cas d'ecart constate. | Roxane Wicky | Photos de production, rapports d'etape, rapports d'inspection fournisseur, messages WeChat |
| 6 | Controle qualite pre-expedition | Le partenaire realisera un controle qualite avant expedition ainsi qu'un envoi d'echantillonnage chez Plus Sarl en parallele du transport chez le client. 🟢 | Roxane Wicky / Partenaire chinois | Rapport d'inspection final, echantillons, accord d'expedition |
| 7 | Transmission au processus logistique | Confirmer que les produits sont prets et transmettre les informations necessaires au processus O3 (Logistique/Livraison) pour organisation du transport. Fournir les documents d'exportation. | Roxane Wicky | Documents d'exportation, packing list, notification de pret a l'expedition |
| 8 | Evaluation du partenaire | Evaluer periodiquement les performances des partenaires chinois (conformite, respect des delais, qualite de communication, reactivite). | Roxane Wicky | Formulaire d'evaluation fournisseur (formulaire simplifie cree par la gerante) |

---

## Logigramme (flux d'activites)

```
    [Specifications client recues du processus O1 - Commercial]
            |
            v
    +-------------------------------+
    | 1. Reception et verification  |----> Cahier des charges, plans
    |    des specifications client  |
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 2. Consultation du partenaire |----> Email/WeChat vers Yuyao Mould Factory
    |    chinois (faisabilite,      |      ou Whang (Yuyao - vis)
    |    devis, delai)              |
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 3. Echanges techniques        |----> Emails, WeChat
    |    iteratifs (client <-->     |      (allers-retours jusqu'a
    |    partenaire chinois)        |       validation)
    +-------------------------------+
            |
            v
      /  Solution technique  \
     /   et prix valides      \
    /    par le client ?       \
   OUI                        NON
    |                           |
    |                           v
    |                   +------------------+
    |                   | Retour au client |
    |                   | pour ajustement  |---> Retour a l'etape 3
    |                   +------------------+
    v
    +-------------------------------+
    | 4. Passation de commande      |----> Bon de commande, facture
    |    au partenaire chinois      |      douaniere
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 5. Suivi de fabrication       |----> Photos, rapports d'etape,
    |    (echanges reguliers        |      rapports d'inspection
    |    email/WeChat)              |
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 6. Controle qualite           |----> Rapport d'inspection final
    |    pre-expedition             |      + envoi echantillons chez
    |    (par le partenaire)        |      Plus Sarl en parallele
    |    + echantillonnage          |      du transport client
    +-------------------------------+
            |
            v
      /  Produit conforme   \
     /   aux specifications ? \
    /                          \
   OUI                        NON
    |                           |
    |                           v
    |                   +---------------------------+
    |                   | Traitement NC             |
    |                   | (O4 - Controle qualite)   |
    |                   | Coordination remplacement |
    |                   | avec partenaire chinois   |
    |                   +---------------------------+
    v
    +-------------------------------+
    | 7. Transmission au processus  |----> Documents d'exportation,
    |    O3 - Logistique/Livraison  |      packing list
    +-------------------------------+
            |
            v
    [Produits prets pour expedition]
```

---

## Ressources necessaires

| Type de ressource | Description |
|---|---|
| **Humaines** | Roxane Wicky (Gerante) - pilotage complet du processus de coordination avec les partenaires chinois |
| **Materielles** | Bureau a Cudrefin (Route de Montet 11, 1588 Cudrefin), ordinateur, telephone |
| **Informatiques** | Email (communication formelle avec clients et partenaires), WeChat (communication quotidienne avec les partenaires chinois), FileMaker (suivi des commandes, enregistrement des informations). Sauvegarde cloud chez le fournisseur 🟢 |
| **Documentaires** | Specifications clients, plans techniques, catalogues fournisseurs, normes applicables, historique des commandes |
| **Financieres** | 🟡 [RECOMMANDE — definir le budget annuel achats et sous-traitance] |

---

## Indicateurs de performance

| Indicateur | Formule de calcul | Objectif | Frequence | Source de donnees |
|---|---|---|---|---|
| Respect des delais fournisseur | Nombre de livraisons fournisseur dans les delais / Nombre total de livraisons x 100 | >= 95% 🟢 | Par livraison | Suivi des commandes FileMaker |
| Taux de conformite (NC par client) | Nombre de NC par client et par an | Maximum 3 NC par client et par an 🟢 | Par livraison | Fiches NC, registre NC, FileMaker |
| Nombre de non-conformites (NC) | Comptage des NC enregistrees par periode | Reduction d'une annee sur l'autre (1ere annee : reference) | Trimestriel | Fiches NC, FileMaker |
| Delai de remplacement en cas de NC | Date de remplacement effectif - Date de signalement NC | Conforme au besoin exprime par le client 🟢 | Par NC | Fiches NC, emails |
| Stabilite des prix | Evolution des prix par rapport a l'annee precedente | Prix stables sur plusieurs annees | Annuel | Historique devis et commandes FileMaker |

---

## Actions d'amelioration planifiees

| # | Action | Description | Echeance | Statut |
|---|---|---|---|---|
| A01 | Voyage en Chine - mars 2026 | Deplacement prevu en Chine en mars 2026 pour renforcer les controles qualite en production, visiter les partenaires (Yuyao Mould Factory et **Whang**), et consolider les exigences qualite sur site. | Mars 2026 | Planifie |
| A02 | Renforcement des controles d'etiquetage | Suite a la NC_2026_1001 (erreur d'etiquetage sur 1000 pieces SHIP_25058/CFM00057428/90.60.05710), renforcement des controles d'etiquetage avant expedition. | T2 2026 | En cours |
| A03 | Accord qualite avec Yuyao Mould Factory | Formaliser un accord qualite avec Yuyao des que le dossier de certification est pret. 🟢 | Des que dossier certification pret | Planifie |
| A04 | Accord qualite avec Whang | Formaliser un accord qualite avec Whang des que le dossier de certification est pret. 🟢 | Des que dossier certification pret | Planifie |

---

## Risques et opportunites associes

Voir CTX-QUA-001 pour le detail. Resume :

| # | Risque / Opportunite | Niveau | Action |
|---|---|---|---|
| R01 | Retard de fabrication chez le partenaire chinois | Eleve | Suivi regulier de la production (WeChat/email), anticipation des delais, marge de securite dans les plannings |
| R02 | Non-conformite des pieces fabriquees | Eleve | Controle qualite pre-expedition par le partenaire, envoi d'echantillons en parallele, rapports d'inspection, historique des NC pour identification des causes recurrentes 🟢 |
| R03 | Probleme de communication (barriere linguistique, decalage horaire) | Moyen | Utilisation de WeChat pour echanges rapides, specifications ecrites detaillees, photos et echantillons |
| R04 | Dependance envers un nombre limite de partenaires | Moyen | Maintien de deux partenaires chinois actifs (Yuyao Mould Factory et Whang), evaluation reguliere, veille sur d'eventuels partenaires complementaires 🟢 |
| R05 | Fluctuation des prix matieres premieres ou taux de change | Moyen | Suivi des prix sur plusieurs annees, offres validees par le client, communication proactive en cas de variation |
| R06 | Certifications des partenaires non confirmees | Moyen | 🔵 [A VERIFIER — certifications de Whang incertaines, a clarifier lors du voyage en Chine mars 2026] |
| O01 | Renforcement du partenariat avec Yuyao Mould Factory | Eleve | Relation de confiance construite depuis la creation de Plus Sarl (2007), communication reguliere, voyage prevu en Chine mars 2026, accord qualite en preparation |
| O02 | Diversification des capacites via Whang (vis) | Moyen | Developper les commandes aupres de Whang pour elargir les capacites de production (vis et autres) 🟢 |

---

## Interfaces avec les autres processus

| Processus en interface | Nature de l'interaction |
|---|---|
| **O1 - Commercial** | Recoit : specifications client, confirmation de commande, delais convenus. Fournit : retour faisabilite, delai de fabrication, prix partenaire |
| **O3 - Logistique et livraison** | Fournit : produits prets a expedier, documents d'exportation (facture douaniere, packing list). Recoit : confirmation d'expedition |
| **O4 - Controle qualite** | Fournit : rapports d'inspection fournisseur, produits a controler, echantillons recus en parallele. Recoit : retour NC fabrication, demandes d'actions correctives, demandes de remplacement |
| **M2 - Amelioration continue** | Fournit : donnees de performance fournisseur, indicateurs. Recoit : objectifs d'amelioration, actions correctives a mettre en oeuvre |
| **S1 - Gestion documentaire** | Fournit : enregistrements (bons de commande, rapports, correspondances). Recoit : acces aux historiques et donnees dans FileMaker |
| **S2 - Competences** | Recoit : formations ou mises a jour sur les normes, les techniques de fabrication, les exigences reglementaires |

---

## Exigences applicables

| Type | Exigence | Reference |
|---|---|---|
| ISO 9001:2015 | Maitrise des processus, produits et services fournis par des prestataires externes | 8.4 |
| ISO 9001:2015 | Type et etendue de la maitrise (des prestataires externes) | 8.4.2 |
| ISO 9001:2015 | Informations a l'attention des prestataires externes | 8.4.3 |
| ISO 9001:2015 | Production et prestation de service - Maitrise de la production | 8.5.1 |
| ISO 9001:2015 | Identification et tracabilite | 8.5.2 |
| ISO 9001:2015 | Propriete des clients ou des prestataires externes | 8.5.3 |
| ISO 9001:2015 | Maitrise des elements de sortie non conformes | 8.7 |
| Reglementaire | Reglementation douaniere suisse (importation depuis la Chine) | 🔵 [A VERIFIER — references specifiques] |
| Reglementaire | Reglementations applicables selon la nature des produits (marquage CE, etc.) | 🔵 [A VERIFIER — selon les produits] |
| Client | Specifications techniques, plans, tolerances, materiaux definis par chaque client | Cahier des charges client (par projet) |

---

## Particularites du processus

### Partenaires chinois

| Partenaire | Role | Localisation | Produits | Certifications | Mode de communication |
|---|---|---|---|---|---|
| **Yuyao Mould Factory** | Partenaire principal - fabrication de moules et pieces | Yuyao, Chine | Moules d'injection, pieces plastiques | 🔵 [A VERIFIER] | Email, WeChat |
| **Whang** | Second partenaire - fabrication de vis | Yuyao, Chine | Vis (screws) 🟢 | 🔵 [A VERIFIER — certifications incertaines] | Email, WeChat |

### Controle qualite pre-expedition

Le partenaire realisera un controle qualite avant expedition ainsi qu'un envoi d'echantillonnage chez Plus Sarl en parallele du transport chez le client. Ce processus permet a Plus Sarl de verifier la conformite des produits tout en maintenant les delais de livraison. 🟢

### Gestion des moules

Les moules sont developpes et stockes en Chine, chez les partenaires. Les moules sont la **propriete des clients**. Un **inventaire des moules existe**. 🟢

### Points d'attention specifiques

- **Propriete intellectuelle** : les conceptions et plans appartiennent exclusivement aux clients. Plus Sarl veille a la confidentialite des informations techniques transmises aux partenaires chinois (cf. Politique qualite, engagement n.6).
- **Stockage des moules** : les moules sont developpes et stockes en Chine, chez le partenaire. Propriete des clients. Inventaire existant. 🟢
- **Decalage horaire** : la coordination avec la Chine implique un decalage horaire de 6 a 7 heures. L'utilisation de WeChat permet des echanges rapides malgre ce decalage.
- **Pas d'activite de conception** : Plus Sarl ne concoit pas les produits (clause 8.3 exclue). Le role est celui de coordinateur industriel entre le client (proprietaire de la conception) et le fabricant chinois.
- **Voyage en Chine mars 2026** : un deplacement sur site est planifie pour renforcer les controles qualite en production et consolider les exigences aupres des partenaires.
- **Accord qualite** : un accord qualite sera formalise avec Yuyao Mould Factory et Whang des que le dossier de certification sera pret. 🟢

---

## Historique des revisions

| Version | Date | Modification | Auteur |
|---|---|---|---|
| 1.0 | 10/02/2026 | Creation initiale | Roxane Wicky |
| 0.2 | 10/02/2026 | Mise a jour des indicateurs de performance (delais fournisseur >= 95%, max 3 NC/client/an). Ajout des actions d'amelioration : voyage Chine mars 2026, renforcement controle etiquetage suite NC_2026_1001. | Roxane Wicky |
| 0.3 | 12/02/2026 | Integration des reponses (Whang, Paradiso, SQS, sauvegarde cloud). Ajout du systeme de legende des champs. | Roxane Wicky |
| 0.4 | 18/02/2026 | Integration UPDATE 2.1 : ajout activite 1b (fiche de production FileMaker), reference a la revue de commande (M1-DIR-001, CTX-QUA-001 section 1.3). | Roxane Wicky |
