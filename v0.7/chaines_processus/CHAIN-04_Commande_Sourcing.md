# Chaîne Processus - CHAIN-04 : Commande Sourcing

| **Document**       | CHAIN-04_Commande_Sourcing                   |
|--------------------|----------------------------------------------|
| **Version**        | v0.7                                         |
| **Date**           | 2026-03-04                                   |
| **Classification** | Interne                                      |
| **Statut**         | **Active**                                   |
| **Processus**      | Chaîne Processus - Réalisation               |
| **Rédaction**      | Rôle Qualité                                 |
| **Approbation**    | Direction                                    |

---

## 1. Objet

Ce document décrit la chaîne processus pour le traitement d'une **commande nécessitant une phase de sourcing**. Cette chaîne reprend la structure en 8 blocs de la CHAIN-01 (Produit Existant) avec des adaptations spécifiques liées à la recherche, l'évaluation et la qualification d'un nouveau fournisseur.

---

## 2. Domaine d'application

Cette chaîne s'applique à toute commande client pour laquelle aucun fournisseur qualifié n'est encore référencé pour le produit demandé. La recherche de fournisseurs s'effectue à l'échelle mondiale, indépendamment de la localisation géographique.

---

## 3. Spécificités de la chaîne « Sourcing »

| Caractéristique                  | Description                                                                          |
|----------------------------------|--------------------------------------------------------------------------------------|
| Phase de développement           | Variable — selon que le produit existe ou nécessite un développement                  |
| Évaluation fournisseur           | À réaliser — recherche, évaluation et qualification d'un nouveau fournisseur          |
| Outillage                        | Variable — selon le fournisseur identifié (existant, à modifier ou à créer)           |
| Délai de réalisation             | Le plus long — inclut la phase de sourcing, qualification et validation               |
| Inspection                       | Contrôle qualité renforcé — première production avec un nouveau fournisseur           |
| Qualification fournisseur        | Audit fournisseur, évaluation capacités, échantillons de validation                   |

---

## 4. Lignes processus

| Code | Ligne             | Rôle pilote          | Fonction principale                              |
|------|-------------------|----------------------|--------------------------------------------------|
| 01   | SALES             | Rôle Commercial      | Gestion commerciale, relation client, facturation |
| 02   | MANUFACTURE       | Rôle Achats          | Coordination fournisseurs, suivi de production    |
| 03   | DELIVERY          | Rôle Logistique      | Transport, livraison, douane                      |
| 04   | QUALITY           | Rôle Qualité         | Contrôle conformité, validation qualité           |

---

## 5. Phase de sourcing et qualification fournisseur

| Étape                          | Description                                                            | Responsable       |
|--------------------------------|------------------------------------------------------------------------|--------------------|
| Analyse du besoin              | Définition des exigences techniques, volumes, délais                   | Rôle Commercial    |
| Recherche fournisseurs         | Identification de fournisseurs potentiels à l'échelle mondiale         | Rôle Achats        |
| Demande de devis               | Envoi du cahier des charges, collecte des offres                       | Rôle Achats        |
| Évaluation comparative         | Analyse qualité, coût, délai, capacité de production                   | Rôle Achats        |
| Audit fournisseur              | Visite sur site, évaluation du système qualité fournisseur             | Rôle Qualité       |
| Échantillons de validation     | Demande et contrôle d'échantillons initiaux                            | Rôle Qualité       |
| Qualification fournisseur      | Décision de référencement, mise à jour du panel fournisseurs           | Rôle Achats        |
| Validation direction           | Approbation finale du nouveau fournisseur par la direction             | Direction          |

---

## 6. Critères de sélection fournisseur et processus d'audit

### 6.1 Grille de critères de sélection

| Critère                  | Pondération | Description                                                                 |
|--------------------------|-------------|-----------------------------------------------------------------------------|
| Qualité                  | 25 %        | Système qualité, certifications (ISO 9001, IATF, etc.), historique qualité  |
| Coût                     | 20 %        | Compétitivité des prix, transparence de la structure de coûts               |
| Délai                    | 20 %        | Capacité à respecter les délais demandés, réactivité                        |
| Capacité de production   | 15 %        | Moyens de production, capacité à absorber les volumes demandés              |
| Certifications           | 10 %        | Certifications spécifiques au secteur, normes environnementales             |
| RSE                      | 10 %        | Responsabilité sociétale, conditions de travail, impact environnemental     |

### 6.2 Qualification

- **Score minimum pour qualification** : 70/100
- Le score est calculé sur la base de la grille de critères ci-dessus, chaque critère étant noté sur 100 puis pondéré.
- Un fournisseur n'atteignant pas le score minimum ne peut pas être référencé sauf dérogation validée par la Direction.

### 6.3 Processus d'audit

- **Audit sur site obligatoire** pour toute commande dont le montant dépasse le seuil défini par la Direction.
- L'audit couvre : système qualité, moyens de production, gestion des non-conformités, traçabilité, conditions de travail.
- Un rapport d'audit est formalisé et archivé. Les écarts identifiés font l'objet d'un plan d'actions correctives avec suivi.
- Pour les commandes en dessous du seuil, un audit documentaire à distance peut être accepté sous validation du Rôle Qualité.

---

## 7. Adaptations par bloc par rapport à CHAIN-01

| Bloc   | Intitulé                        | Adaptations par rapport à CHAIN-01                                                                          |
|--------|---------------------------------|-------------------------------------------------------------------------------------------------------------|
| BLOC 1 | Réception commande              | Identification du type de commande : sourcing requis, analyse préliminaire du besoin                         |
| BLOC 2 | Fiche de commande               | Mention « sourcing en cours », cahier des charges technique complet                                          |
| BLOC 3 | Fiche de transport              | Délais prévisionnels à ajuster selon résultat du sourcing, mise en place des nouveaux circuits logistiques avec le fournisseur retenu, vérification des contraintes douanières spécifiques au pays d'origine |
| BLOC 4 | Étude technique fournisseurs    | Phase de sourcing complète : recherche, évaluation, audit, qualification, puis étude technique standard      |
| BLOC 5 | Validation de commande          | AR incluant le résultat du sourcing, présentation du fournisseur retenu, planning prévisionnel               |
| BLOC 6 | Production et qualité           | Première production avec nouveau fournisseur, contrôle qualité renforcé, PPAP si applicable                  |
| BLOC 7 | Livraison & Douane              | Mise en place des circuits logistiques avec le nouveau fournisseur, test du circuit logistique sur première expédition, documentation complète pour nouveau corridor d'approvisionnement, vérification des procédures douanières spécifiques |
| BLOC 8 | Acceptation marchandise         | Contrôle renforcé première livraison, retour d'expérience, mise à jour évaluation fournisseur                |

---

## 8. Vue d'ensemble des blocs

```
           ┌──────────────────────────────┐
           │  PHASE PRÉALABLE : SOURCING  │
           │  Recherche & Qualification   │
           │  fournisseur                 │
           └──────────────┬───────────────┘
                          ▼
BLOC 1          BLOC 2          BLOC 3          BLOC 4
Réception       Fiche de        Fiche de        Étude technique
commande        commande        transport       fournisseurs
[01 SALES]      [01 SALES]      [03 DELIVERY]   [02 MANUFACTURE]
    │               │               │               │
    ▼               ▼               ▼               ▼
BLOC 5          BLOC 6          BLOC 7          BLOC 8
Validation      Production      Livraison       Acceptation
commande        & Qualité       & Douane        marchandise
[01 SALES]      [02 MANUF.      [03 DELIVERY    [04 QUALITY
                 04 QUALITY]     01 SALES]        01 SALES]
```

---

## 9. Matrice de responsabilité (RACI)

| Bloc   | Rôle Commercial | Rôle Achats | Rôle Logistique | Rôle Qualité |
|--------|-----------------|-------------|-----------------|--------------|
| BLOC 1 | R/A             | I           | I               | I            |
| BLOC 2 | R/A             | C           | I               | C            |
| BLOC 3 | I               | C           | R/A             | I            |
| BLOC 4 | I               | R/A         | I               | C            |
| BLOC 5 | R/A             | C           | C               | C            |
| BLOC 6 | I               | R/A         | I               | R/A          |
| BLOC 7 | R               | I           | R/A             | I            |
| BLOC 8 | R               | I           | I               | R/A          |

**Légende** : R = Réalise, A = Approuve, C = Consulté, I = Informé

---

## 10. Indicateurs de performance (KPI)

| KPI                                            | Objectif                  | Fréquence de mesure | Responsable       |
|------------------------------------------------|---------------------------|---------------------|--------------------|
| Délai moyen de sourcing et qualification        | ≤ délai contractuel       | Par commande        | Rôle Achats        |
| Nombre de fournisseurs évalués par sourcing     | ≥ 3                       | Par commande        | Rôle Achats        |
| Taux de conformité échantillons initiaux        | ≥ 90 %                   | Par commande        | Rôle Qualité       |
| Taux de qualification au premier audit          | ≥ 70 %                   | Semestrielle        | Rôle Qualité       |
| Taux de réclamations clients                    | ≤ 3 %                    | Mensuelle           | Rôle Commercial    |
| Respect des délais fournisseurs                 | ≥ 90 %                   | Mensuelle           | Rôle Achats        |

---

## 11. Documents associés

| Référence   | Document                                          |
|-------------|---------------------------------------------------|
| CHAIN-01    | Chaîne Processus — Commande Produit Existant      |
| CHAIN-02    | Chaîne Processus — Modification d'Outillage       |
| CHAIN-03    | Chaîne Processus — Nouvel Outillage               |
| CH-BLOC-001 à CH-BLOC-008 | Fiches détail des blocs (référence CHAIN-01) |

---

## 12. Complétude du document

> Toutes les sections de ce document ont été complétées en v0.7.

---

## Références normatives

| Clause ISO 9001:2015 | Exigence                                                        |
|-----------------------|-----------------------------------------------------------------|
| 8.1                   | Planification et maîtrise opérationnelles                        |
| 8.4                   | Maîtrise des processus, produits et services externalisés        |
| 8.4.1                 | Généralités — type et étendue de la maîtrise                    |
| 8.4.2                 | Type et étendue de la maîtrise                                   |
| 8.4.3                 | Informations à l'attention des prestataires externes             |

---

*Document contrôlé - Toute copie imprimée est considérée comme non contrôlée.*
*Plus Sàrl - Système de Management de la Qualité ISO 9001:2015 - v0.7*
