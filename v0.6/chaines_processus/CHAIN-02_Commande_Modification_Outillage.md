# Chaîne Processus - CHAIN-02 : Commande Modification d'Outillage

| **Document**       | CHAIN-02_Commande_Modification_Outillage    |
|--------------------|----------------------------------------------|
| **Version**        | v0.6                                         |
| **Date**           | 2026-03-04                                   |
| **Classification** | Interne                                      |
| **Statut**         | **À compléter**                              |
| **Processus**      | Chaîne Processus - Réalisation               |
| **Rédaction**      | Rôle Qualité                                 |
| **Approbation**    | Direction                                    |

---

## 1. Objet

Ce document décrit la chaîne processus pour le traitement d'une **commande nécessitant une modification d'outillage existant**. Cette chaîne reprend la structure en 8 blocs de la CHAIN-01 (Produit Existant) avec des adaptations spécifiques liées à la phase de modification technique de l'outillage.

---

## 2. Domaine d'application

Cette chaîne s'applique à toute commande client impliquant la modification d'un outillage déjà existant chez un fournisseur qualifié, indépendamment de la localisation géographique du client ou du fournisseur.

---

## 3. Spécificités de la chaîne « Modification d'Outillage »

| Caractéristique                  | Description                                                              |
|----------------------------------|--------------------------------------------------------------------------|
| Phase de développement           | Partielle — modification technique de l'outillage existant               |
| Évaluation fournisseur           | Déjà réalisée — fournisseur qualifié et référencé                        |
| Outillage                        | Existant mais nécessitant une modification selon les nouvelles exigences |
| Délai de réalisation             | Intermédiaire — inclut la phase de modification et validation            |
| Inspection                       | Contrôle qualité renforcé — validation des modifications apportées       |
| Échantillons                     | Possible validation d'échantillons post-modification                     |

---

## 4. Lignes processus

| Code | Ligne             | Rôle pilote          | Fonction principale                              |
|------|-------------------|----------------------|--------------------------------------------------|
| 01   | SALES             | Rôle Commercial      | Gestion commerciale, relation client, facturation |
| 02   | MANUFACTURE       | Rôle Achats          | Coordination fournisseurs, suivi de production    |
| 03   | DELIVERY          | Rôle Logistique      | Transport, livraison, douane                      |
| 04   | QUALITY           | Rôle Qualité         | Contrôle conformité, validation qualité           |

---

## 5. Adaptations par bloc par rapport à CHAIN-01

| Bloc   | Intitulé                        | Adaptations par rapport à CHAIN-01                                                                |
|--------|---------------------------------|---------------------------------------------------------------------------------------------------|
| BLOC 1 | Réception commande              | Identification du type de commande : modification d'outillage                                     |
| BLOC 2 | Fiche de commande               | Mention de la modification requise, référence à l'outillage existant                              |
| BLOC 3 | Fiche de transport              | *À compléter* — Délais ajustés en fonction de la phase de modification                           |
| BLOC 4 | Étude technique fournisseurs    | Étude de faisabilité de la modification, devis modification outillage, validation technique        |
| BLOC 5 | Validation de commande          | AR incluant le détail de la modification, coûts supplémentaires éventuels                         |
| BLOC 6 | Production et qualité           | Phase de modification outillage, validation échantillons post-modification, puis production série  |
| BLOC 7 | Livraison & Douane              | *À compléter* — Procédure standard avec délais ajustés                                           |
| BLOC 8 | Acceptation marchandise         | Contrôle renforcé sur les pièces issues de l'outillage modifié                                    |

---

## 6. Vue d'ensemble des blocs

```
BLOC 1          BLOC 2          BLOC 3          BLOC 4
Réception       Fiche de        Fiche de        Étude technique
commande        commande        transport       + Modification
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

## 7. Indicateurs de performance (KPI)

| KPI                                          | Objectif                  | Fréquence de mesure | Responsable       |
|----------------------------------------------|---------------------------|---------------------|--------------------|
| Délai de modification d'outillage            | ≤ délai contractuel       | Par commande        | Rôle Achats        |
| Taux de conformité échantillons post-modif.  | ≥ 95 %                   | Par commande        | Rôle Qualité       |
| Taux de réclamations clients                 | ≤ 3 %                    | Mensuelle           | Rôle Commercial    |
| Respect des délais fournisseurs              | ≥ 90 %                   | Mensuelle           | Rôle Achats        |

---

## 8. Documents associés

| Référence   | Document                                          |
|-------------|---------------------------------------------------|
| CHAIN-01    | Chaîne Processus — Commande Produit Existant      |
| CH-BLOC-001 à CH-BLOC-008 | Fiches détail des blocs (référence CHAIN-01) |

---

## 9. Actions restantes

- [ ] Compléter les adaptations détaillées pour chaque bloc
- [ ] Définir les critères spécifiques de validation post-modification
- [ ] Documenter le processus d'approbation des échantillons modifiés
- [ ] Valider les délais standards pour les modifications d'outillage

---

## Références normatives

| Clause ISO 9001:2015 | Exigence                                                        |
|-----------------------|-----------------------------------------------------------------|
| 8.1                   | Planification et maîtrise opérationnelles                        |
| 8.3                   | Conception et développement de produits et services              |
| 8.4                   | Maîtrise des processus, produits et services externalisés        |
| 8.5.1                 | Maîtrise de la production et de la prestation de service         |

---

*Document contrôlé - Toute copie imprimée est considérée comme non contrôlée.*
*Plus Sàrl - Système de Management de la Qualité ISO 9001:2015 - v0.6*
