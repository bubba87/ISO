# Chaîne Processus - CHAIN-03 : Commande Nouvel Outillage

| **Document**       | CHAIN-03_Commande_Nouvel_Outillage           |
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

Ce document décrit la chaîne processus pour le traitement d'une **commande nécessitant la création d'un nouvel outillage**. Cette chaîne reprend la structure en 8 blocs de la CHAIN-01 (Produit Existant) avec des adaptations spécifiques liées à la phase de conception, fabrication d'outillage et validation par échantillons (T0/T1).

---

## 2. Domaine d'application

Cette chaîne s'applique à toute commande client impliquant la conception et la fabrication d'un nouvel outillage chez un fournisseur qualifié, indépendamment de la localisation géographique du client ou du fournisseur.

---

## 3. Spécificités de la chaîne « Nouvel Outillage »

| Caractéristique                  | Description                                                                    |
|----------------------------------|--------------------------------------------------------------------------------|
| Phase de développement           | Complète — conception et fabrication d'un nouvel outillage                      |
| Évaluation fournisseur           | Déjà réalisée — fournisseur qualifié et référencé                              |
| Outillage                        | Nouveau — conception, fabrication, mise au point et validation nécessaires      |
| Délai de réalisation             | Long — inclut conception, fabrication outillage, échantillons T0/T1, validation|
| Inspection                       | Contrôle qualité renforcé — validation des échantillons T0 et T1               |
| Échantillons                     | Obligatoire — série T0 (premiers essais) puis T1 (pré-série de validation)     |
| Phase de design                  | Revue de conception, plans d'outillage, validation technique avant fabrication  |

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

| Bloc   | Intitulé                        | Adaptations par rapport à CHAIN-01                                                                          |
|--------|---------------------------------|-------------------------------------------------------------------------------------------------------------|
| BLOC 1 | Réception commande              | Identification du type de commande : nouvel outillage, collecte du cahier des charges technique              |
| BLOC 2 | Fiche de commande               | Mention du nouvel outillage requis, spécifications techniques, plans et tolérances                           |
| BLOC 3 | Fiche de transport              | *À compléter* — Délais ajustés en fonction des phases de conception et validation                           |
| BLOC 4 | Étude technique fournisseurs    | Étude de faisabilité, conception outillage, devis outillage, plan de validation, planning T0/T1              |
| BLOC 5 | Validation de commande          | AR incluant le détail de l'outillage, coûts outillage, planning prévisionnel T0/T1                          |
| BLOC 6 | Production et qualité           | Fabrication outillage, essais T0, ajustements, validation T1, puis lancement production série                |
| BLOC 7 | Livraison & Douane              | *À compléter* — Procédure standard avec délais ajustés, livraison éventuelle d'échantillons T1 au client    |
| BLOC 8 | Acceptation marchandise         | Contrôle renforcé, rapport dimensionnel complet, validation des pièces issues du nouvel outillage            |

---

## 6. Vue d'ensemble des blocs

```
BLOC 1          BLOC 2          BLOC 3          BLOC 4
Réception       Fiche de        Fiche de        Étude technique
commande        commande        transport       + Design outillage
[01 SALES]      [01 SALES]      [03 DELIVERY]   [02 MANUFACTURE]
    │               │               │               │
    ▼               ▼               ▼               ▼
BLOC 5          BLOC 6          BLOC 7          BLOC 8
Validation      Production      Livraison       Acceptation
commande        T0/T1 + Série   & Douane        marchandise
[01 SALES]      [02 MANUF.      [03 DELIVERY    [04 QUALITY
                 04 QUALITY]     01 SALES]        01 SALES]
```

---

## 7. Phase de conception et validation outillage

| Étape              | Description                                                          | Responsable     |
|--------------------|----------------------------------------------------------------------|-----------------|
| Revue de conception| Analyse du cahier des charges, faisabilité technique                  | Rôle Achats     |
| Conception outillage| Plans d'outillage, choix matériaux, validation technique             | Rôle Achats     |
| Fabrication outillage| Réalisation de l'outillage par le fournisseur                       | Rôle Achats     |
| Essais T0          | Premiers essais, analyse dimensionnelle, ajustements                 | Rôle Qualité    |
| Validation T1      | Pré-série de validation, rapport de conformité complet               | Rôle Qualité    |
| Approbation client | Envoi échantillons T1 au client pour validation finale               | Rôle Commercial |

---

## 8. Indicateurs de performance (KPI)

| KPI                                           | Objectif                  | Fréquence de mesure | Responsable       |
|-----------------------------------------------|---------------------------|---------------------|--------------------|
| Délai de conception et fabrication outillage   | ≤ délai contractuel       | Par commande        | Rôle Achats        |
| Taux de conformité échantillons T0             | ≥ 80 %                   | Par commande        | Rôle Qualité       |
| Taux de conformité échantillons T1             | ≥ 95 %                   | Par commande        | Rôle Qualité       |
| Taux de validation client au premier envoi     | ≥ 85 %                   | Par commande        | Rôle Commercial    |
| Taux de réclamations clients                   | ≤ 3 %                    | Mensuelle           | Rôle Commercial    |
| Respect des délais fournisseurs                | ≥ 90 %                   | Mensuelle           | Rôle Achats        |

---

## 9. Documents associés

| Référence   | Document                                          |
|-------------|---------------------------------------------------|
| CHAIN-01    | Chaîne Processus — Commande Produit Existant      |
| CHAIN-02    | Chaîne Processus — Modification d'Outillage       |
| CH-BLOC-001 à CH-BLOC-008 | Fiches détail des blocs (référence CHAIN-01) |

---

## 10. Actions restantes

- [ ] Compléter les adaptations détaillées pour chaque bloc
- [ ] Définir le processus complet de conception outillage
- [ ] Documenter les critères d'acceptation T0 et T1
- [ ] Définir les livrables attendus à chaque phase de validation
- [ ] Valider les délais standards pour la création d'un nouvel outillage
- [ ] Définir le processus de propriété intellectuelle de l'outillage

---

## Références normatives

| Clause ISO 9001:2015 | Exigence                                                        |
|-----------------------|-----------------------------------------------------------------|
| 8.1                   | Planification et maîtrise opérationnelles                        |
| 8.3                   | Conception et développement de produits et services              |
| 8.3.2                 | Planification de la conception et du développement               |
| 8.3.4                 | Maîtrise de la conception et du développement                    |
| 8.4                   | Maîtrise des processus, produits et services externalisés        |
| 8.5.1                 | Maîtrise de la production et de la prestation de service         |

---

*Document contrôlé - Toute copie imprimée est considérée comme non contrôlée.*
*Plus Sàrl - Système de Management de la Qualité ISO 9001:2015 - v0.6*
