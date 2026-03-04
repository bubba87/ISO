# P04 - Processus Logistique et Livraison

| **Processus**       | P04 - Logistique et Livraison                        |
|----------------------|------------------------------------------------------|
| **Type**            | Réalisation                                           |
| **Pilote**          | Rôle Logistique                                       |
| **Version**         | v0.7                                                  |
| **Date**            | 2026-03-04                                            |
| **Référence**       | PR-P04-LOG                                            |
| **Norme ISO 9001**  | Chapitres 8.5.4, 8.6                                 |

---

## 1. Objet et domaine d'application

Ce processus décrit les activités logistiques de **Plus Sàrl** couvrant la planification des expéditions, la coordination du transport international, le suivi des livraisons et la confirmation de bonne réception. Il s'applique à l'ensemble des flux logistiques liés aux opérations mondiales de monitoring industriel et de sourcing.

---

## 2. Références normatives

- ISO 9001:2015, Chapitres 8.5.4 (Préservation), 8.6 (Libération des produits et services)
- Manuel Qualité Plus Sàrl (MQ-001)
- Réglementations douanières et de transport internationales applicables

---

## 3. Rôles et responsabilités

| Rôle                        | Responsabilités principales                                          |
|-----------------------------|----------------------------------------------------------------------|
| **Logistique**              | Planification, coordination transport, suivi, documentation          |
| **Achats**                  | Transmission des informations fournisseur, conditions Incoterms      |
| **Commercial**              | Communication client sur les délais et le suivi                      |
| **Qualité**                 | Libération des marchandises après inspection                         |
| **Transitaire / Transporteur** | Exécution du transport, dédouanement                              |

---

## 4. Données d'entrée et de sortie

### Données d'entrée
- Bon de commande validé et confirmé (P01/P02)
- Confirmation de libération qualité (P04)
- Informations fournisseur (adresse, contact, conditions)
- Exigences client (délai, lieu, Incoterms)
- Réglementations douanières applicables

### Données de sortie
- Plan d'expédition
- Documents de transport (BL, AWB, CMR, packing list)
- Déclarations douanières
- Preuve de livraison (POD)
- Confirmation de réception client

---

## 5. Description des activités

### A1 - Planification de l'expédition

Le Rôle Logistique reçoit les informations de commande validée et planifie l'expédition : mode de transport (maritime, aérien, routier, ferroviaire), délais, volumes, exigences spéciales d'emballage et de manutention.

### A2 - Sélection du transitaire / transporteur

Le Rôle Logistique sélectionne le transitaire ou transporteur approprié parmi les prestataires qualifiés, en tenant compte du coût, des délais, de la fiabilité et de la destination.

### A3 - Préparation de la documentation

Le Rôle Logistique prépare ou coordonne la préparation des documents nécessaires : facture commerciale, packing list, certificat d'origine, documents douaniers, connaissement (BL) ou lettre de transport aérien (AWB).

### A4 - Coordination de l'enlèvement et du chargement

Le Rôle Logistique coordonne l'enlèvement des marchandises chez le fournisseur, s'assure de la bonne exécution du Loading Check (P04) le cas échéant, et confirme le chargement.

### A5 - Suivi du transport en cours

Le Rôle Logistique assure le suivi en temps réel du transport, gère les aléas (retards, avaries, blocages douaniers) et communique proactivement les mises à jour au Rôle Commercial pour information du client.

### A6 - Dédouanement et livraison finale

Le Rôle Logistique coordonne les opérations de dédouanement à destination, organise la livraison finale au client et s'assure du respect des conditions convenues.

### A7 - Confirmation de livraison et clôture

Le Rôle Logistique obtient la preuve de livraison (POD), confirme la bonne réception au Rôle Commercial et au client, archive les documents et clôture le dossier logistique.

---

## 6. Diagramme swimlane

```
 PROCESSUS P03 - LOGISTIQUE ET LIVRAISON
 ============================================================================

 Rôle                 | Flux des activités
 ============================================================================
                      |
 LOGISTIQUE           |  [A1 Planifier]    [A2 Sélectionner]   [A3 Préparer]
                      |  l'expédition --->  transitaire/   ---> documentation
                      |  (mode, délai,      transporteur        (BL, AWB,
                      |   volumes)          qualifié             packing list)
                      |                                              |
                      |                                              v
                      |                                    [A4 Coordonner]
                      |                                    enlèvement et
                      |                                    chargement
                      |                                         |
                      |                                         v
                      |                                    [A5 Suivre]
                      |                                    le transport
                      |                                    en cours
                      |                                         |
                      |                                         v
                      |                                    [A6 Dédouaner]
                      |                                    et livrer
                      |                                         |
                      |                                         v
                      |                                    [A7 Confirmer]
                      |                                    livraison et
                      |                                    clôturer (POD)
                      |
 ============================================================================
                      |
 ACHATS               |  Transmettre les ---> Fournir les     Signaler
                      |  informations        conditions       les aléas
                      |  fournisseur         Incoterms        fournisseur
                      |
 ============================================================================
                      |
 COMMERCIAL           |  Communiquer   ---> Informer le  ---> Confirmer
                      |  les exigences      client sur le     au client la
                      |  client (délai,     suivi transport   bonne réception
                      |  destination)
                      |
 ============================================================================
                      |
 QUALITÉ              |  Libérer les marchandises après inspection (P04)
                      |  Valider le Loading Check avant chargement
                      |
 ============================================================================
                      |
 TRANSITAIRE /        |  Exécuter le  ---> Gérer le    ---> Livrer au
 TRANSPORTEUR         |  transport         dédouanement     destinataire
                      |                                     final
                      |
 ============================================================================
```

---

## 7. Interactions avec les autres processus

| Processus              | Nature de l'interaction                                |
|------------------------|--------------------------------------------------------|
| PM01 - Leadership        | Reporting performance logistique, budgets transport    |
| P01 - Commercial       | Exigences client, communication suivi, confirmation    |
| P02 - Achats           | Informations fournisseur, conditions d'enlèvement      |
| P03 - Contrôle Qualité | Loading Check, libération des marchandises             |
| PS01 - Gestion Documentaire | Archivage documents de transport                     |

---

## 8. Indicateurs de performance (KPI)

| Indicateur                                | Formule / Méthode                              | Objectif       | Fréquence    |
|-------------------------------------------|------------------------------------------------|----------------|--------------|
| Taux de livraison dans les délais         | Livraisons à temps / Total livraisons x 100    | >= 95 %        | Mensuelle    |
| Taux d'avaries transport                  | Livraisons avec avaries / Total livraisons x 100 | < 1 %        | Mensuelle    |
| Délai moyen de transit                    | Somme des délais de transit / Nombre d'expéditions | Selon destination | Mensuelle |
| Taux de complétude documentaire           | Dossiers complets / Total dossiers x 100       | 100 %          | Mensuelle    |
| Coût logistique moyen par expédition      | Total coûts logistiques / Nombre d'expéditions | Tendance baisse | Trimestrielle |
| Taux de réclamations liées au transport   | Réclamations transport / Total livraisons x 100 | < 2 %         | Mensuelle    |

---

## 9. Documents et enregistrements associés

| Code         | Intitulé                              | Type          |
|--------------|---------------------------------------|---------------|
| PR-P04-LOG   | Procédure Logistique et Livraison    | Procédure     |
| FM-P04-EXP   | Fiche d'expédition                    | Formulaire    |
| FM-P04-SUI   | Tableau de suivi des expéditions      | Formulaire    |
| EN-P04-POD   | Preuves de livraison                  | Enregistrement|
| EN-P04-DOC   | Dossiers documentaires transport      | Enregistrement|

---

## 10. Amélioration continue

L'amélioration du processus logistique s'appuie sur :
- L'analyse des retards et de leurs causes racines
- L'optimisation des routes et modes de transport
- L'évaluation régulière des transitaires et transporteurs
- La digitalisation du suivi des expéditions
- Le retour d'expérience sur les incidents de transport

---

*Document contrôlé - Plus Sàrl - Système de Management de la Qualité ISO 9001:2015*
*Version v0.7 - 2026-03-04*
