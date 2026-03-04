# P01 - Processus Commercial

| **Processus**       | P01 - Commercial                                      |
|----------------------|------------------------------------------------------|
| **Type**            | Réalisation                                           |
| **Pilote**          | Rôle Commercial                                       |
| **Version**         | v0.6                                                  |
| **Date**            | 2026-03-04                                            |
| **Référence**       | PR-P01-COM                                            |
| **Norme ISO 9001**  | Chapitres 8.2, 8.5, 9.1.2                            |

---

## 1. Objet et domaine d'application

Ce processus décrit les activités commerciales de **Plus Sàrl** depuis la réception d'une demande client jusqu'à la mesure de la satisfaction. Il couvre l'ensemble du cycle commercial pour les activités de monitoring industriel et de sourcing à l'échelle mondiale.

---

## 2. Références normatives

- ISO 9001:2015, Chapitres 8.2 (Exigences relatives aux produits et services), 8.5 (Production et prestation de service), 9.1.2 (Satisfaction du client)
- Manuel Qualité Plus Sàrl (MQ-001)

---

## 3. Rôles et responsabilités

| Rôle                        | Responsabilités principales                                          |
|-----------------------------|----------------------------------------------------------------------|
| **Commercial**              | Gestion des demandes, offres, contrats, suivi client                 |
| **Direction**               | Validation des offres stratégiques, approbation des contrats majeurs |
| **Qualité**                 | Support pour les exigences qualité, traitement des réclamations      |
| **Client**                  | Expression du besoin, validation des offres, retour de satisfaction  |

---

## 4. Données d'entrée et de sortie

### Données d'entrée
- Demande client (cahier des charges, spécifications, RFQ)
- Exigences réglementaires et normatives applicables
- Historique client et conditions commerciales
- Catalogue de services Plus Sàrl

### Données de sortie
- Offre commerciale validée
- Contrat / bon de commande signé
- Ordre interne de réalisation
- Rapport de satisfaction client
- Indicateurs de performance commerciale

---

## 5. Description des activités

### A1 - Réception et enregistrement de la demande client

Le Rôle Commercial réceptionne la demande client (e-mail, téléphone, plateforme en ligne), l'enregistre dans le système de suivi et attribue un numéro de référence unique.

### A2 - Analyse et revue des exigences client

Le Rôle Commercial analyse la demande pour vérifier la faisabilité technique, logistique et commerciale. Les exigences sont revues avec les processus P02 (Achats), P03 (Logistique) et P04 (Contrôle Qualité) si nécessaire.

### A3 - Élaboration de l'offre commerciale

Le Rôle Commercial prépare l'offre incluant : description des services, conditions tarifaires, délais, conditions de livraison (Incoterms), conditions de paiement et exigences qualité.

### A4 - Validation et envoi de l'offre

L'offre est validée selon les seuils d'approbation définis (Direction pour les offres stratégiques) puis transmise au client.

### A5 - Négociation et ajustement

Le Rôle Commercial conduit les négociations avec le client, ajuste l'offre si nécessaire et documente les modifications apportées.

### A6 - Contractualisation

Après accord, le Rôle Commercial formalise le contrat ou le bon de commande, s'assure de la signature des deux parties et déclenche l'ordre interne de réalisation.

### A7 - Transmission aux processus opérationnels

Le Rôle Commercial transmet les informations nécessaires aux processus P02 (Achats/Sourcing), P03 (Logistique) et P04 (Contrôle Qualité) pour exécution de la commande.

### A8 - Suivi de la réalisation et communication client

Le Rôle Commercial assure le suivi de l'avancement auprès des processus opérationnels et communique régulièrement avec le client sur l'état de sa commande.

### A9 - Mesure de la satisfaction client

Le Rôle Commercial pilote la mesure de la satisfaction client via des enquêtes (FM-P01-SAT), l'analyse des retours et le traitement des réclamations.

---

## 6. Diagramme swimlane

```
 PROCESSUS P01 - COMMERCIAL
 ============================================================================

 Rôle                 | Flux des activités
 ============================================================================
                      |
 CLIENT               |  Exprimer le     Valider       Négocier /     Confirmer
                      |  besoin    ----> l'offre  ---> ajuster  ----> la commande
                      |  (RFQ, CdC)      reçue        conditions     (signature)
                      |      |               ^             ^               |
                      |      v               |             |               v
 ============================================================================
                      |
 COMMERCIAL           |  [A1 Réceptionner]  [A3 Élaborer]  [A5 Négocier]
                      |  et enregistrer      l'offre         et ajuster
                      |  la demande          commerciale     l'offre
                      |      |                   ^               |
                      |      v                   |               v
                      |  [A2 Analyser]      [A4 Valider]   [A6 Contractua-
                      |  les exigences       et envoyer     liser]
                      |  client              l'offre        (contrat/BC)
                      |      |                                   |
                      |      |    +------------------------------+
                      |      |    |
                      |      v    v
                      |  [A7 Transmettre aux processus opérationnels]
                      |      |
                      |      v
                      |  [A8 Suivre la réalisation]
                      |  Communication client régulière
                      |      |
                      |      v
                      |  [A9 Mesurer la satisfaction client]
                      |  (FM-P01-SAT)
                      |
 ============================================================================
                      |
 DIRECTION            |  Valider les offres stratégiques
                      |  Approuver les contrats majeurs
                      |
 ============================================================================
                      |
 QUALITÉ              |  Support exigences qualité
                      |  Traitement des réclamations
                      |
 ============================================================================
                      |
 P02 ACHATS           |  <--- Réception ordre d'achat / sourcing
 P03 LOGISTIQUE       |  <--- Réception instructions logistiques
 P04 CONTRÔLE         |  <--- Réception exigences qualité / inspections
                      |
 ============================================================================
```

---

## 7. Interactions avec les autres processus

| Processus              | Nature de l'interaction                                |
|------------------------|--------------------------------------------------------|
| M1 - Leadership        | Reporting commercial, validation stratégique           |
| P02 - Achats           | Transmission des besoins de sourcing, retour faisabilité |
| P03 - Logistique       | Coordination des livraisons, suivi expéditions         |
| P04 - Contrôle Qualité | Définition des inspections requises, retour qualité    |
| S1 - Gestion Documentaire | Archivage des offres, contrats, enregistrements     |

---

## 8. Indicateurs de performance (KPI)

| Indicateur                                | Formule / Méthode                              | Objectif       | Fréquence    |
|-------------------------------------------|------------------------------------------------|----------------|--------------|
| Taux de conversion des offres             | Offres acceptées / Offres émises x 100         | >= 30 %        | Mensuelle    |
| Délai moyen de réponse aux demandes       | Somme des délais / Nombre de demandes          | < 48 heures    | Mensuelle    |
| Taux de satisfaction client               | Score moyen enquête FM-P01-SAT                 | >= 4/5         | Trimestrielle |
| Nombre de réclamations clients            | Comptage des réclamations reçues               | Tendance baisse | Mensuelle   |
| Chiffre d'affaires par période            | Total des commandes facturées                  | Selon budget   | Mensuelle    |
| Taux de fidélisation client               | Clients récurrents / Clients totaux x 100      | >= 60 %        | Annuelle     |
| Délai moyen de contractualisation         | Date contrat - Date demande initiale           | < 15 jours     | Mensuelle    |

---

## 9. Documents et enregistrements associés

| Code         | Intitulé                          | Type          |
|--------------|-----------------------------------|---------------|
| PR-P01-COM   | Procédure Commerciale             | Procédure     |
| FM-P01-SAT   | Enquête Satisfaction Client       | Formulaire    |
| FM-P01-OFF   | Modèle d'offre commerciale       | Formulaire    |
| FM-P01-BC    | Bon de commande                   | Formulaire    |
| EN-P01-REC   | Registre des réclamations         | Enregistrement|

---

## 10. Amélioration continue

L'amélioration du processus commercial s'appuie sur :
- L'analyse des enquêtes de satisfaction client
- Le suivi des taux de conversion et des délais
- L'analyse des réclamations et de leurs causes racines
- Les retours d'expérience des équipes opérationnelles
- Le benchmarking des pratiques commerciales du secteur

---

*Document contrôlé - Plus Sàrl - Système de Management de la Qualité ISO 9001:2015*
*Version v0.6 - 2026-03-04*
