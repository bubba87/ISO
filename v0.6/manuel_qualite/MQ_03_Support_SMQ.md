# Manuel Qualité - Chapitre 3 : Support du Système de Management de la Qualité

| **Document**       | MQ_03_Support_SMQ                        |
|--------------------|------------------------------------------|
| **Version**        | v0.6                                     |
| **Date**           | 2026-03-04                               |
| **Classification** | Interne                                  |
| **Processus**      | Tous processus                           |
| **Rédaction**      | Rôle Qualité                             |
| **Approbation**    | Direction                                |

---

## 3.1 Structure organisationnelle du SMQ

Le Système de Management de la Qualité de Plus Sàrl repose sur une organisation par rôles fonctionnels. Chaque rôle est défini par ses responsabilités, ses autorités et ses interactions avec les autres rôles. Une matrice de compétences sera présentée ultérieurement pour détailler les aptitudes requises par rôle.

---

## 3.2 Cartographie des rôles

### 3.2.1 Direction

| Attribut              | Description                                                         |
|-----------------------|---------------------------------------------------------------------|
| **Mission**           | Piloter la stratégie de l'entreprise et garantir l'efficacité du SMQ |
| **Responsabilités**   | Définition de la politique qualité, allocation des ressources, revue de direction, engagement envers la satisfaction client |
| **Autorité**          | Décisions stratégiques, approbation des documents du SMQ, validation des objectifs qualité |
| **Processus pilotés** | PM01 - Pilotage stratégique, PS02 - Gestion des compétences          |

### 3.2.2 Rôle Commercial

| Attribut              | Description                                                         |
|-----------------------|---------------------------------------------------------------------|
| **Mission**           | Gérer la relation client et assurer le développement commercial      |
| **Responsabilités**   | Analyse des demandes clients, émission des offres, suivi des commandes, gestion des réclamations clients |
| **Autorité**          | Validation des offres commerciales, acceptation des commandes dans le cadre défini |
| **Processus pilotés** | P01 - Gestion commerciale                                           |

### 3.2.3 Rôle Achats

| Attribut              | Description                                                         |
|-----------------------|---------------------------------------------------------------------|
| **Mission**           | Sélectionner, qualifier et gérer les fournisseurs internationaux     |
| **Responsabilités**   | Prospection fournisseurs, qualification initiale, négociation, passation de commandes, évaluation périodique des fournisseurs |
| **Autorité**          | Sélection des fournisseurs, suspension d'un fournisseur non conforme |
| **Processus pilotés** | P02 - Achats et sourcing                                            |

### 3.2.4 Rôle Logistique

| Attribut              | Description                                                         |
|-----------------------|---------------------------------------------------------------------|
| **Mission**           | Coordonner les opérations logistiques et les expéditions internationales |
| **Responsabilités**   | Planification des transports, suivi des expéditions, gestion documentaire douanière, coordination avec les transitaires |
| **Autorité**          | Choix des modes de transport, validation des documents d'expédition   |
| **Processus pilotés** | P04 - Logistique et expédition                                       |

### 3.2.5 Rôle Qualité

| Attribut              | Description                                                         |
|-----------------------|---------------------------------------------------------------------|
| **Mission**           | Assurer la conformité des produits et l'efficacité du SMQ            |
| **Responsabilités**   | Planification et réalisation des inspections, gestion des non-conformités, audits internes, suivi des indicateurs qualité, amélioration continue |
| **Autorité**          | Blocage de produits non conformes, déclenchement d'actions correctives, décision de libération des produits |
| **Processus pilotés** | P03 - Monitoring et contrôle qualité                                 |

### 3.2.6 Rôle Gestion Documentaire

| Attribut              | Description                                                         |
|-----------------------|---------------------------------------------------------------------|
| **Mission**           | Garantir la maîtrise documentaire du SMQ                             |
| **Responsabilités**   | Création, révision et diffusion des documents, gestion des enregistrements, archivage, contrôle des versions |
| **Autorité**          | Validation de la conformité documentaire, retrait des documents obsolètes |
| **Processus pilotés** | PS01 - Gestion documentaire                                         |

---

## 3.3 Matrice des interactions entre rôles

| Rôle émetteur ↓ / Rôle récepteur → | Direction | Rôle Commercial | Rôle Achats | Rôle Logistique | Rôle Qualité | Rôle Gestion Doc. |
|--------------------------------------|-----------|-----------------|-------------|-----------------|--------------|---------------------|
| **Direction**                        | -         | Orientations stratégiques | Budgets achats | Objectifs logistiques | Politique qualité | Exigences documentaires |
| **Rôle Commercial**                  | Rapports commerciaux | - | Cahier des charges client | Besoins expédition | Exigences qualité client | Demandes de documents |
| **Rôle Achats**                      | Reporting achats | Confirmations fournisseur | - | Informations fournisseur | Dossiers qualification | Fiches fournisseurs |
| **Rôle Logistique**                  | Reporting logistique | Confirmations expédition | Coordination transport | - | Documents transport | Documents douaniers |
| **Rôle Qualité**                     | Indicateurs qualité | Rapports d'inspection | Évaluation fournisseurs | Autorisation d'expédition | - | Rapports et enregistrements |
| **Rôle Gestion Doc.**               | Tableau de bord documentaire | Documents applicables | Documents applicables | Documents applicables | Documents applicables | - |

---

## 3.4 Flux d'information et de décision

### 3.4.1 Flux ascendants (vers la Direction)

| Source             | Type d'information                        | Fréquence        |
|--------------------|-------------------------------------------|-------------------|
| Rôle Commercial    | Chiffre d'affaires, satisfaction client    | Mensuelle         |
| Rôle Achats        | Performance fournisseurs, coûts achats     | Mensuelle         |
| Rôle Logistique    | Taux de livraison à temps, incidents       | Mensuelle         |
| Rôle Qualité       | Taux de NC, résultats inspections, KPIs    | Mensuelle         |
| Rôle Gestion Doc.  | État de la documentation, audits doc.      | Trimestrielle     |

### 3.4.2 Flux descendants (depuis la Direction)

| Destinataire       | Type d'information                         | Fréquence        |
|--------------------|--------------------------------------------|-------------------|
| Tous les rôles     | Politique qualité, objectifs stratégiques   | Annuelle          |
| Tous les rôles     | Résultats de la revue de direction          | Semestrielle      |
| Rôle concerné      | Décisions d'allocation de ressources       | Selon besoin      |
| Rôle concerné      | Actions correctives stratégiques           | Selon besoin      |

### 3.4.3 Flux transversaux (entre rôles opérationnels)

| Émetteur           | Récepteur          | Information                              | Déclencheur           |
|--------------------|--------------------|------------------------------------------|-----------------------|
| Rôle Commercial    | Rôle Achats        | Nouvelle commande validée                | Acceptation commande  |
| Rôle Achats        | Rôle Qualité       | Commande fournisseur passée              | Confirmation commande |
| Rôle Qualité       | Rôle Logistique    | Autorisation de libération produit       | Inspection réussie    |
| Rôle Qualité       | Rôle Achats        | Non-conformité fournisseur               | Détection NC          |
| Rôle Logistique    | Rôle Commercial    | Confirmation d'expédition                | Départ marchandise    |

---

## 3.5 Matrice des autorités

| Décision                                      | Direction | Rôle Commercial | Rôle Achats | Rôle Qualité | Rôle Logistique | Rôle Gestion Doc. |
|-----------------------------------------------|-----------|-----------------|-------------|--------------|-----------------|---------------------|
| Approbation politique qualité                  | A         | I               | I           | C            | I               | I                   |
| Acceptation d'une commande client              | I         | A               | C           | C            | C               | -                   |
| Sélection d'un nouveau fournisseur             | I         | I               | A           | C            | -               | -                   |
| Suspension d'un fournisseur                    | C         | I               | A           | R            | -               | -                   |
| Libération d'un lot de produits                | -         | I               | I           | A            | I               | -                   |
| Blocage pour non-conformité                    | I         | I               | I           | A            | I               | -                   |
| Validation d'un document SMQ                   | A         | -               | -           | C            | -               | R                   |
| Lancement d'une action corrective              | I         | -               | -           | A            | -               | I                   |
| Allocation de ressources                       | A         | -               | -           | C            | -               | -                   |

**Légende** : A = Approuve / R = Réalise / C = Consulté / I = Informé

---

## 3.6 Compétences par rôle

Une matrice de compétences détaillée sera établie ultérieurement. Le tableau ci-dessous présente les domaines de compétences requis par rôle.

| Rôle                     | Domaines de compétences clés                                          |
|--------------------------|-----------------------------------------------------------------------|
| Direction                | Management stratégique, gestion financière, leadership, normes ISO    |
| Rôle Commercial          | Négociation commerciale, relation client, langues étrangères, commerce international |
| Rôle Achats              | Sourcing international, négociation fournisseurs, connaissance produits, évaluation fournisseurs |
| Rôle Logistique          | Logistique internationale, réglementation douanière, Incoterms, gestion transport |
| Rôle Qualité             | Normes qualité ISO 9001, techniques d'inspection, métrologie, audit, gestion NC |
| Rôle Gestion Documentaire| Gestion documentaire, outils numériques, archivage, maîtrise des enregistrements |

---

## Références normatives

| Clause ISO 9001:2015 | Exigence                                                |
|-----------------------|---------------------------------------------------------|
| 5.3                   | Rôles, responsabilités et autorités au sein de l'organisme |
| 7.1.2                 | Ressources humaines                                      |
| 7.2                   | Compétences                                              |
| 7.4                   | Communication                                            |
| 4.4.1                 | L'organisme doit établir les processus nécessaires       |

---

*Document contrôlé - Toute copie imprimée est considérée comme non contrôlée.*
*Plus Sàrl - Système de Management de la Qualité ISO 9001:2015 - v0.6*
