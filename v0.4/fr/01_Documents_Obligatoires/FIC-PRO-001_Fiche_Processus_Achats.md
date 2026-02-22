# Fiche Processus O2 - Achats et Sous-traitance

| | |
|---|---|
| **Référence** | FIC-PRO-001 |
| **Version** | 0.4 |
| **Date de création** | 10/02/2026 |
| **Date de revision** | 18/02/2026 |
| **Rédigé par** | Roxane Wicky |
| **Approuve par** | Roxane Wicky |

> **Légende :** 🔴 [À REMPLIR] = obligatoire, manquant | 🟡 [RECOMMANDE] = recommandé | 🟢 = déjà rempli | 🔵 [À VÉRIFIER] = a confirmer

---

## Identification du processus

| Élément | Description |
|---|---|
| **Nom du processus** | Achats et Sous-traitance |
| **Code** | O2 |
| **Type** | Opérationnel |
| **Pilote** | Roxane Wicky (Gérante) |
| **Finalite** | Coordonner les partenaires chinois (Yuyao Mould Factory et **Oukailuo**, Yuyao) pour assurer la fabrication des pièces, moules et vis conformément aux spécifications des clients européens, dans le respect des délais, des prix et des exigences qualité. |

---

## Données d'entrée et de sortie

| Données d'entrée (inputs) | Provenance |
|---|---|
| Specifications techniques du client (plans, cahier des charges, tolérances, materiaux) | Client via processus O1 - Commercial |
| Délais de livraison convenus avec le client | Processus O1 - Commercial |
| Offre validée par le client, confirmation de commande | Processus O1 - Commercial |
| Historique des commandes et des prix | S1 - Gestion documentaire (FileMaker) |
| Retour sur les non-conformites précédentes | Processus O4 - Contrôle qualité |

| Données de sortie (outputs) | Destinataire |
|---|---|
| Commande de fabrication transmise au partenaire chinois | Yuyao Mould Factory / Oukailuo |
| Confirmation de faisabilité et de délai de fabrication | Processus O1 - Commercial (pour information au client) |
| Rapports de suivi de fabrication (photos, rapports d'étape) | Interne / Client si demande |
| Produits fabriques prêts à l\'expédition | Processus O3 - Logistique et livraison |
| Documents d'exportation (facture douanière, packing list) | Processus O3 - Logistique et livraison |
| Rapports d'inspection fournisseur | Processus O4 - Contrôle qualité |
| Échantillons envoyés en parallèle de l'expédition | Plus Sarl (contrôle de conformité) 🟢 |
| Évaluation des performances fournisseur | Processus M2 - Amélioration continue |

---

## Description des activités

| # | Activité | Description | Responsable | Document/Enregistrement |
|---|---|---|---|---|
| 1 | Revue de commande et reception des spécifications | Recevoir du processus commercial les spécifications techniques, plans, cahier des charges et exigences du client. Vérifier la completude du dossier. Réaliser l'analyse préalable selon M1-DIR-001 (cf. CTX-QUA-001 section 1.3). | Roxane Wicky | Cahier des charges client, plans techniques, email de transmission, fiche commande FileMaker |
| 1b | Création de la fiche de production FileMaker | Créer la fiche de production dans le système FileMaker : caracteristiques attendues du produit, délai de fabrication, suivi de production. Cette fiche est mise à jour tout au long de la fabrication (cf. PRO-ACH-001, section 9). 🟢 | Roxane Wicky | Fiche de production FileMaker |
| 2 | Consultation du/des partenaire(s) chinois | Transmettre les spécifications a Yuyao Mould Factory (partenaire principal) ou a **Oukailuo** (Yuyao — spécialisé dans la fabrication de vis) selon la nature du projet. Demander une analyse de faisabilité, un devis et un délai. Communication par email et WeChat. | Roxane Wicky | Emails, messages WeChat, devis fournisseur |
| 3 | Échanges techniques iteratifs | Coordonner les allers-retours entre le client et le partenaire chinois jusqu'a obtenir une solution technique validée (materiaux, tolérances, procede de fabrication, prix). Traduire et adapter les exigences si nécessaire. | Roxane Wicky | Emails, messages WeChat, comptes-rendus d'échanges |
| 4 | Validation et passation de commande | Une fois la solution technique et le prix valides par le client, emettre la commande de fabrication au partenaire chinois. Établir les documents de commande (facture douanière, bon de commande). | Roxane Wicky | Bon de commande, facture douanière, confirmation de commande |
| 5 | Suivi de fabrication | Suivre l'avancement de la production auprès du partenaire chinois. Recevoir et analyser les photos, rapports d'étape, rapports d'inspection. Intervenir en cas d'écart constate. | Roxane Wicky | Photos de production, rapports d'étape, rapports d'inspection fournisseur, messages WeChat |
| 6 | Contrôle qualité pre-expédition | Le partenaire realisera un contrôle qualité avant expédition ainsi qu'un envoi d'echantillonnage chez Plus Sarl en parallèle du transport chez le client. 🟢 | Roxane Wicky / Partenaire chinois | Rapport d'inspection final, échantillons, accord d'expédition |
| 7 | Transmission au processus logistique | Confirmer que les produits sont prêts et transmettre les informations nécessaires au processus O3 (Logistique/Livraison) pour organisation du transport. Fournir les documents d'exportation. | Roxane Wicky | Documents d'exportation, packing list, notification de pret à l\'expédition |
| 8 | Évaluation du partenaire | Évaluer periodiquement les performances des partenaires chinois (conformité, respect des délais, qualité de communication, réactivité). | Roxane Wicky | Formulaire d'évaluation fournisseur (formulaire simplifié créé par la gérante) |

---

## Logigramme (flux d'activités)

```
    [Specifications client reçues du processus O1 - Commercial]
            |
            v
    +-------------------------------+
    | 1. Reception et vérification  |----> Cahier des charges, plans
    |    des specifications client  |
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 2. Consultation du partenaire |----> Email/WeChat vers Yuyao Mould Factory
    |    chinois (faisabilité,      |      ou Oukailuo (Yuyao - vis)
    |    devis, délai)              |
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 3. Échanges techniques        |----> Emails, WeChat
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
    |                   | pour ajustement  |---> Retour à l\'étape 3
    |                   +------------------+
    v
    +-------------------------------+
    | 4. Passation de commande      |----> Bon de commande, facture
    |    au partenaire chinois      |      douaniere
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 5. Suivi de fabrication       |----> Photos, rapports d'étape,
    |    (échanges reguliers        |      rapports d'inspection
    |    email/WeChat)              |
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 6. Controle qualité           |----> Rapport d'inspection final
    |    pre-expédition             |      + envoi échantillons chez
    |    (par le partenaire)        |      Plus Sarl en parallèle
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
    |                   | (O4 - Controle qualité)   |
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
    [Produits prêts pour expédition]
```

---

## Ressources nécessaires

| Type de ressource | Description |
|---|---|
| **Humaines** | Roxane Wicky (Gérante) - pilotage complet du processus de coordination avec les partenaires chinois |
| **Materielles** | Bureau a Cudrefin (Route de Montet 11, 1588 Cudrefin), ordinateur, téléphone |
| **Informatiques** | Email (communication formelle avec clients et partenaires), WeChat (communication quotidienne avec les partenaires chinois), FileMaker (suivi des commandes, enregistrement des informations). Sauvegarde cloud chez le fournisseur 🟢 |
| **Documentaires** | Specifications clients, plans techniques, catalogues fournisseurs, normes applicables, historique des commandes |
| **Financières** | 🟡 [RECOMMANDE — définir le budget annuel achats et sous-traitance] |

---

## Indicateurs de performance

| Indicateur | Formule de calcul | Objectif | Frequence | Source de données |
|---|---|---|---|---|
| Respect des délais fournisseur | Nombre de livraisons fournisseur dans les délais / Nombre total de livraisons x 100 | >= 95% 🟢 | Par livraison | Suivi des commandes FileMaker |
| Taux de conformité (NC par client) | Nombre de NC par client et par an | Maximum 3 NC par client et par an 🟢 | Par livraison | Fiches NC, registre NC, FileMaker |
| Nombre de non-conformites (NC) | Comptage des NC enregistrées par période | Reduction d'une année sur l'autre (1ere année : référence) | Trimestriel | Fiches NC, FileMaker |
| Délai de remplacement en cas de NC | Date de remplacement effectif - Date de signalement NC | Conforme au besoin exprime par le client 🟢 | Par NC | Fiches NC, emails |
| Stabilité des prix | Évolution des prix par rapport à l\'année précédente | Prix stables sur plusieurs années | Annuel | Historique devis et commandes FileMaker |

---

## Actions d'amélioration planifiées

| # | Action | Description | Échéance | Statut |
|---|---|---|---|---|
| A01 | Voyage en Chine - mars 2026 | Deplacement prévu en Chine en mars 2026 pour renforcer les contrôles qualité en production, visiter les partenaires (Yuyao Mould Factory et **Oukailuo**), et consolider les exigences qualité sur site. | Mars 2026 | Planifié |
| A02 | Renforcement des contrôles d'étiquetage | Suite à la NC_2026_1001 (erreur d'étiquetage sur 1000 pièces SHIP_25058/CFM00057428/90.60.05710), renforcement des contrôles d'étiquetage avant expédition. | T2 2026 | En cours |
| A03 | Accord qualité avec Yuyao Mould Factory | Formaliser un accord qualité avec Yuyao des que le dossier de certification est pret. 🟢 | Des que dossier certification pret | Planifié |
| A04 | Accord qualité avec Oukailuo | Formaliser un accord qualité avec Oukailuo des que le dossier de certification est pret. 🟢 | Des que dossier certification pret | Planifié |

---

## Risques et opportunités associés

Voir CTX-QUA-001 pour le détail. Résumé :

| # | Risque / Opportunité | Niveau | Action |
|---|---|---|---|
| R01 | Retard de fabrication chez le partenaire chinois | Élevé | Suivi régulier de la production (WeChat/email), anticipation des délais, marge de sécurité dans les plannings |
| R02 | Non-conformité des pièces fabriquees | Élevé | Contrôle qualité pre-expédition par le partenaire, envoi d'échantillons en parallèle, rapports d'inspection, historique des NC pour identification des causes recurrentes 🟢 |
| R03 | Problème de communication (barriere linguistique, decalage horaire) | Moyen | Utilisation de WeChat pour échanges rapides, spécifications ecrites détaillées, photos et échantillons |
| R04 | Dependance envers un nombre limité de partenaires | Moyen | Maintien de deux partenaires chinois actifs (Yuyao Mould Factory et Oukailuo), évaluation régulière, veille sur d'éventuels partenaires complémentaires 🟢 |
| R05 | Fluctuation des prix matières premières ou taux de change | Moyen | Suivi des prix sur plusieurs années, offres validées par le client, communication proactive en cas de variation |
| R06 | Certifications des partenaires non confirmees | Moyen | 🔵 [À VÉRIFIER — certifications de Oukailuo incertaines, a clarifier lors du voyage en Chine mars 2026] |
| O01 | Renforcement du partenariat avec Yuyao Mould Factory | Élevé | Relation de confiance construite depuis la création de Plus Sarl (2007), communication régulière, voyage prévu en Chine mars 2026, accord qualité en préparation |
| O02 | Diversification des capacités via Oukailuo (vis) | Moyen | Developper les commandes auprès de Oukailuo pour elargir les capacités de production (vis et autres) 🟢 |

---

## Interfaces avec les autres processus

| Processus en interface | Nature de l'interaction |
|---|---|
| **O1 - Commercial** | Recoit : spécifications client, confirmation de commande, délais convenus. Fournit : retour faisabilité, délai de fabrication, prix partenaire |
| **O3 - Logistique et livraison** | Fournit : produits prêts a expédier, documents d'exportation (facture douanière, packing list). Recoit : confirmation d'expédition |
| **O4 - Contrôle qualité** | Fournit : rapports d'inspection fournisseur, produits a contrôler, échantillons reçus en parallèle. Recoit : retour NC fabrication, demandes d'actions correctives, demandes de remplacement |
| **M2 - Amélioration continue** | Fournit : données de performance fournisseur, indicateurs. Recoit : objectifs d'amélioration, actions correctives a mettre en œuvre |
| **S1 - Gestion documentaire** | Fournit : enregistrements (bons de commande, rapports, correspondances). Recoit : accès aux historiques et données dans FileMaker |
| **S2 - Compétences** | Recoit : formations ou mises a jour sur les normes, les techniques de fabrication, les exigences réglementaires |

---

## Exigences applicables

| Type | Exigence | Référence |
|---|---|---|
| ISO 9001:2015 | Maîtrise des processus, produits et services fournis par des prestataires externes | 8.4 |
| ISO 9001:2015 | Type et etendue de la maîtrise (des prestataires externes) | 8.4.2 |
| ISO 9001:2015 | Informations à l\'attention des prestataires externes | 8.4.3 |
| ISO 9001:2015 | Production et prestation de service - Maîtrise de la production | 8.5.1 |
| ISO 9001:2015 | Identification et traçabilité | 8.5.2 |
| ISO 9001:2015 | Propriété des clients ou des prestataires externes | 8.5.3 |
| ISO 9001:2015 | Maîtrise des éléments de sortie non conformes | 8.7 |
| Réglementaire | Réglementation douanière suisse (importation depuis la Chine) | 🔵 [À VÉRIFIER — références spécifiques] |
| Réglementaire | Reglementations applicables selon la nature des produits (marquage CE, etc.) | 🔵 [À VÉRIFIER — selon les produits] |
| Client | Specifications techniques, plans, tolérances, materiaux définis par chaque client | Cahier des charges client (par projet) |

---

## Particularites du processus

### Partenaires chinois

| Partenaire | Rôle | Localisation | Produits | Certifications | Mode de communication |
|---|---|---|---|---|---|
| **Yuyao Mould Factory** | Partenaire principal - fabrication de moules et pièces | Yuyao, Chine | Moules d'injection, pièces plastiques | 🔵 [À VÉRIFIER] | Email, WeChat |
| **Oukailuo** | Second partenaire - fabrication de vis | Yuyao, Chine | Vis (screws) 🟢 | 🔵 [À VÉRIFIER — certifications incertaines] | Email, WeChat |

### Contrôle qualité pre-expédition

Le partenaire realisera un contrôle qualité avant expédition ainsi qu'un envoi d'echantillonnage chez Plus Sarl en parallèle du transport chez le client. Ce processus permet a Plus Sarl de vérifier la conformité des produits tout en maintenant les délais de livraison. 🟢

### Gestion des moules

Les moules sont développés et stockés en Chine, chez les partenaires. Les moules sont la **propriété des clients**. Un **inventaire des moules existe**. 🟢

### Planification et maîtrise opérationnelle (clause 8.1)

> **Source :** UPDATE 7.5-8.7 — Planification opérationnelle (21/02/2026) 🟢

Lors de la réception d'une commande ou d'une demande :
- la demande est analysée afin de vérifier sa faisabilité technique, logistique ou commerciale
- si nécessaire, les éléments techniques sont transmis au partenaire industriel pour étude de faisabilité et confirmation des délais
- les délais de production sont confirmés avant validation définitive auprès du client
- la commande est enregistrée dans le système FileMaker, assurant sa traçabilité
- un accusé de réception est transmis au client, confirmant les quantités, prix et délais

> **Note :** Dans le cas où l'entreprise n'est pas en mesure de répondre à une demande (par exemple pour un nouveau produit hors champ de compétence), la demande peut être refusée afin de garantir la conformité et la maîtrise des engagements. Seules les commandes réalisables et maîtrisées sont acceptées.

### Exigences relatives aux produits et services (clause 8.2)

> **Source :** UPDATE 7.5-8.7 — Exigences produits (21/02/2026) 🟢

Les demandes des clients sont reçues sous forme de bon de commande ou par courrier électronique. Elles peuvent inclure :
- quantités commandées
- délais souhaités
- références produit ou version spécifique
- spécifications techniques (dimensions, coloris, modifications particulières)
- exigences emballages
- exigences logistiques ou lieu de livraison

En cas de nouveau produit ou de modification technique, un plan ou des spécifications peuvent être transmis.

**Revue des exigences :** Avant validation, Plus Sarl procède à une revue afin de vérifier :
- la compréhension complète des besoins
- la faisabilité technique auprès du partenaire industriel
- la capacité de production
- les conditions logistiques
- la cohérence des conditions commerciales

Toute exigence incomplète ou ambiguë fait l'objet d'une clarification auprès du client.

**Gestion des modifications :** Toute modification ultérieure fait l'objet :
- d'une nouvelle analyse
- d'une validation fournisseur si nécessaire
- d'une confirmation écrite au client
- d'une mise à jour dans le système de gestion

### Points d'attention spécifiques

- **Propriété intellectuelle** : les conceptions et plans appartiennent exclusivement aux clients. Plus Sarl veille à la confidentialité des informations techniques transmises aux partenaires chinois (cf. Politique qualité, engagement n.6).
- **Stockage des moules** : les moules sont développés et stockés en Chine, chez le partenaire. Propriété des clients. Inventaire existant. 🟢
- **Decalage horaire** : la coordination avec la Chine impliqué un decalage horaire de 6 a 7 heures. L'utilisation de WeChat permet des échanges rapides malgre ce decalage.
- **Pas d'activité de conception** : Plus Sarl ne conçoit pas les produits (clause 8.3 exclue). Le rôle est celui de coordinateur industriel entre le client (proprietaire de la conception) et le fabricant chinois.
- **Voyage en Chine mars 2026** : un deplacement sur site est planifié pour renforcer les contrôles qualité en production et consolider les exigences auprès des partenaires.
- **Accord qualité** : un accord qualité sera formalisé avec Yuyao Mould Factory et Oukailuo des que le dossier de certification sera pret. 🟢

### Maîtrise de la production externalisée (clause 8.5)

> **Source :** UPDATE 7.5-8.7 — Production externalisée et libération (21/02/2026) 🟢

La production des pièces est réalisée par des partenaires industriels en Chine. La conformité des produits est assurée par :
- la transmission des spécifications techniques aux partenaires industriels
- la validation de faisabilité avant lancement de production
- la réalisation d'un contrôle qualité interne par le fabricant avant expédition
- l'émission d'un rapport de contrôle qualité 🟡 [RECOMMANDÉ — à formaliser et standardiser lors du voyage en Chine]

En cas de non-conformité détectée avant expédition, une nouvelle production ou une correction est réalisée avant toute livraison client.

### Libération des produits et services (clause 8.6)

> **Source :** UPDATE 7.5-8.7 — Libération (21/02/2026) 🟢

La libération des produits est effectuée après confirmation par le partenaire industriel que les pièces sont conformes aux exigences définies.

La libération repose sur :
- le contrôle qualité réalisé par le fabricant
- la confirmation de conformité
- lorsque nécessaire, des photos ou éléments justificatifs transmis

> 🟡 [RECOMMANDÉ] Une amélioration du formalisme du processus de libération sera mise en place afin de renforcer la traçabilité documentaire des contrôles effectués.

---

## Historique des revisions

| Version | Date | Modification | Auteur |
|---|---|---|---|
| 1.0 | 10/02/2026 | Création initiale | Roxane Wicky |
| 0.2 | 10/02/2026 | Mise à jour des indicateurs de performance (délais fournisseur >= 95%, max 3 NC/client/an). Ajout des actions d'amélioration : voyage Chine mars 2026, renforcement contrôle étiquetage suite NC_2026_1001. | Roxane Wicky |
| 0.3 | 12/02/2026 | Intégration des réponses (Oukailuo, Paradiso, SQS, sauvegarde cloud). Ajout du système de légende des champs. | Roxane Wicky |
| 0.4 | 18/02/2026 | Intégration UPDATE 2.1 : ajout activité 1b (fiche de production FileMaker), référence à la revue de commande (M1-DIR-001, CTX-QUA-001 section 1.3). | Roxane Wicky |
| 0.4 | 21/02/2026 | Intégration UPDATE 7.5-8.7 : ajout sections 8.1 (planification opérationnelle, refus commande hors compétence), 8.2 (exigences produits, revue des exigences, gestion des modifications). | Roxane Wicky |
