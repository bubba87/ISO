# Manuel Qualité - Chapitre 2 : Activités, Organisation et Relations Clients

| **Document**       | MQ_02_Activites                          |
|--------------------|------------------------------------------|
| **Version**        | v0.7                                     |
| **Date**           | 2026-03-04                               |
| **Classification** | Interne                                  |
| **Processus**      | Tous processus                           |
| **Rédaction**      | Rôle Qualité                             |
| **Approbation**    | Direction                                |

---

## 2.1 Présentation de Plus Sàrl

Plus Sàrl est une société de **monitoring industriel et de sourcing à l'échelle mondiale**. L'entreprise intervient en tant qu'intermédiaire qualifié entre ses clients et un réseau international de fournisseurs industriels, en assurant la conformité, la qualité et la traçabilité des produits sourcés.

### Domaines d'activité

| Domaine                        | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| Sourcing industriel mondial    | Identification et qualification de fournisseurs internationaux              |
| Monitoring de production       | Suivi et contrôle qualité des productions externalisées                     |
| Inspection et contrôle qualité | Réalisation d'inspections à différentes étapes de la production             |
| Conseil et accompagnement      | Assistance technique et logistique pour les opérations d'approvisionnement  |

---

## 2.2 Modèle de production externalisée

Plus Sàrl opère selon un **modèle de production entièrement externalisé**. L'entreprise ne possède pas d'unités de fabrication propres. Son rôle consiste à :

1. **Sélectionner** les fournisseurs les plus adaptés aux exigences des clients
2. **Qualifier** les capacités de production des partenaires industriels
3. **Superviser** les étapes critiques de fabrication
4. **Contrôler** la qualité des produits avant expédition
5. **Coordonner** la logistique internationale

Ce modèle implique une maîtrise rigoureuse des processus externalisés conformément aux exigences de la norme ISO 9001:2015, clause 8.4.

---

## 2.3 Cartographie des processus principaux

### Processus de management

| Code | Processus               | Pilote     | Objectif principal                              |
|------|-------------------------|------------|-------------------------------------------------|
| PM01 | Pilotage stratégique    | Direction  | Définir les orientations et assurer le pilotage |

### Processus de réalisation

| Code | Processus                      | Pilote            | Objectif principal                                          |
|------|--------------------------------|--------------------|-------------------------------------------------------------|
| P01  | Gestion commerciale            | Rôle Commercial    | Gérer la relation client et analyser les demandes           |
| P02  | Achats et sourcing             | Rôle Achats        | Sélectionner et qualifier les fournisseurs internationaux   |
| P03  | Monitoring et contrôle qualité | Rôle Qualité       | Assurer la conformité des produits par des inspections       |
| P04  | Logistique et expédition       | Rôle Logistique    | Coordonner le transport et la livraison internationale      |

### Processus de support

| Code | Processus                | Pilote                      | Objectif principal                           |
|------|--------------------------|-----------------------------|----------------------------------------------|
| PS01 | Gestion documentaire     | Rôle Gestion Documentaire   | Maîtriser la documentation du SMQ            |
| PS02 | Gestion des compétences  | Direction                    | Assurer l'adéquation des compétences         |
| PS03 | Amélioration continue    | Rôle Qualité                 | Piloter l'amélioration continue du SMQ       |

---

## 2.4 Interactions entre processus

```
┌─────────────────────────────────────────────────────────┐
│                  PM01 - Pilotage stratégique             │
│                       (Direction)                        │
└──────────┬──────────────────────────────────┬────────────┘
           │                                  │
           ▼                                  ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│  P01 - Gestion   │───▶│  P02 - Achats &  │───▶│  P03 - Monitoring│
│  commerciale     │    │  Sourcing        │    │  & Contrôle QC   │
└──────────────────┘    └──────────────────┘    └────────┬─────────┘
                                                         │
                                                         ▼
                                                ┌──────────────────┐
                                                │  P04 - Logistique│
                                                │  & Expédition    │
                                                └──────────────────┘
           ▲                                  ▲
           │                                  │
┌──────────┴──────────────────────────────────┴────────────┐
│        PS01 / PS02 / PS03 - Processus de support           │
└──────────────────────────────────────────────────────────┘
```

---

## 2.5 Relations clients à l'international

### Typologie des clients

| Catégorie               | Description                                                    |
|-------------------------|----------------------------------------------------------------|
| Industriels             | Entreprises manufacturières nécessitant du sourcing de composants |
| Distributeurs           | Sociétés de distribution recherchant des produits finis         |
| Donneurs d'ordres       | Entreprises externalisant tout ou partie de leur production     |
| Bureaux d'études        | Structures nécessitant un accompagnement technique au sourcing  |

### Couverture géographique

Plus Sàrl intervient à l'échelle mondiale, avec des clients et fournisseurs répartis sur tous les continents. L'entreprise assure ses services indépendamment de la localisation géographique des parties prenantes.

### Canaux de communication client

| Canal                | Utilisation                                      | Fréquence          |
|----------------------|--------------------------------------------------|---------------------|
| E-mail professionnel | Communication courante, envoi de rapports        | Quotidienne         |
| Visioconférence      | Réunions de projet, revues qualité               | Hebdomadaire        |
| Plateforme en ligne  | Suivi des commandes, partage documentaire         | Continue            |
| Visites sur site     | Audits, inspections, réunions stratégiques        | Selon besoin        |

---

## 2.6 Workflow d'analyse de la demande

Le processus d'analyse de la demande client se déroule selon les étapes suivantes :

### Étape 1 : Réception de la demande
- Le **Rôle Commercial** réceptionne la demande du client
- Enregistrement dans le système de gestion
- Attribution d'un numéro de référence unique

### Étape 2 : Analyse de faisabilité
- Évaluation des spécifications techniques
- Vérification de la disponibilité des fournisseurs qualifiés
- Analyse des contraintes logistiques et de délai
- Consultation du **Rôle Achats** et du **Rôle Qualité** si nécessaire

### Étape 3 : Revue des exigences

| Élément de revue               | Responsable        | Critère de validation                     |
|--------------------------------|--------------------|-------------------------------------------|
| Spécifications techniques      | Rôle Qualité       | Conformité aux normes applicables          |
| Capacité fournisseur           | Rôle Achats        | Fournisseur qualifié disponible            |
| Délais de réalisation          | Rôle Logistique    | Cohérence avec les attentes client         |
| Conditions commerciales        | Rôle Commercial    | Rentabilité et conditions acceptables      |
| Exigences réglementaires       | Rôle Qualité       | Conformité aux réglementations applicables |

### Étape 4 : Offre et validation
- Émission de l'offre commerciale par le **Rôle Commercial**
- Négociation éventuelle avec le client
- Validation finale et acceptation de la commande

### Étape 5 : Lancement opérationnel
- Transmission du dossier au **Rôle Achats** pour lancement de la commande fournisseur
- Planification des inspections par le **Rôle Qualité**
- Organisation logistique par le **Rôle Logistique**

---

## 2.7 Engagements envers les clients

Plus Sàrl s'engage auprès de ses clients sur les points suivants :

1. **Transparence** : communication claire et régulière sur l'avancement des commandes
2. **Qualité** : contrôle rigoureux de la conformité des produits aux spécifications
3. **Réactivité** : traitement rapide des demandes et des réclamations
4. **Traçabilité** : documentation complète de chaque étape du processus
5. **Amélioration continue** : prise en compte systématique des retours clients

---

## Références normatives

| Clause ISO 9001:2015 | Exigence                                              |
|-----------------------|-------------------------------------------------------|
| 4.3                   | Détermination du domaine d'application du SMQ          |
| 4.4                   | Système de management de la qualité et ses processus   |
| 8.2                   | Exigences relatives aux produits et services           |
| 8.2.1                 | Communication avec les clients                         |
| 8.2.2                 | Détermination des exigences relatives aux produits      |
| 8.2.3                 | Revue des exigences relatives aux produits              |
| 8.4                   | Maîtrise des processus, produits et services externalisés |

---

*Document contrôlé - Toute copie imprimée est considérée comme non contrôlée.*
*Plus Sàrl - Système de Management de la Qualité ISO 9001:2015 - v0.7*
