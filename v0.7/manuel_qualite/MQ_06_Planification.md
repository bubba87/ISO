# Manuel Qualité - Chapitre 6 : Planification

| **Document**       | MQ_06_Planification                      |
|--------------------|------------------------------------------|
| **Version**        | v0.7                                     |
| **Date**           | 2026-03-04                               |
| **Classification** | Interne                                  |
| **Processus**      | PM01 - Pilotage stratégique              |
| **Rédaction**      | Rôle Qualité                             |
| **Approbation**    | Direction                                |

---

## 6.1 Actions à mettre en œuvre face aux risques et opportunités

### 6.1.1 Méthodologie d'identification des risques

Plus Sàrl applique une démarche structurée d'identification et de traitement des risques et opportunités :

1. **Identification** : recensement des risques et opportunités liés au contexte (cf. MQ_04)
2. **Analyse** : évaluation de la probabilité d'occurrence et de la gravité de l'impact
3. **Hiérarchisation** : classement par niveau de criticité
4. **Traitement** : définition des actions pour maîtriser les risques ou exploiter les opportunités
5. **Suivi** : surveillance de l'efficacité des actions mises en œuvre

### 6.1.2 Échelle d'évaluation

**Probabilité d'occurrence :**

| Niveau | Libellé      | Description                               |
|--------|-------------|-------------------------------------------|
| 1      | Rare         | Moins d'une fois par an                   |
| 2      | Occasionnel  | Une à deux fois par an                    |
| 3      | Probable     | Plusieurs fois par an                     |
| 4      | Fréquent     | Plusieurs fois par trimestre              |

**Gravité de l'impact :**

| Niveau | Libellé      | Description                               |
|--------|-------------|-------------------------------------------|
| 1      | Mineur       | Impact négligeable sur les opérations      |
| 2      | Modéré       | Impact limité, gérable sans difficulté     |
| 3      | Majeur       | Impact significatif sur la qualité ou les délais |
| 4      | Critique     | Impact grave sur la satisfaction client ou la pérennité |

**Criticité = Probabilité x Gravité**

| Niveau de criticité | Plage | Action requise                              |
|---------------------|-------|---------------------------------------------|
| Faible              | 1-4   | Surveillance, aucune action immédiate requise|
| Moyen               | 5-8   | Actions de réduction à planifier             |
| Élevé               | 9-12  | Actions prioritaires à mettre en œuvre      |
| Critique            | 13-16 | Actions immédiates obligatoires              |

---

### 6.1.3 Registre des risques et opportunités

#### Risques identifiés

| Réf.  | Risque                                                    | Processus | Prob. | Grav. | Crit. | Action de maîtrise                                          | Responsable       |
|-------|-----------------------------------------------------------|-----------|-------|-------|-------|--------------------------------------------------------------|-------------------|
| R-01  | Non-conformité produit détectée tardivement                | P03       | 3     | 4     | 12    | Renforcement des inspections intermédiaires (IPC, DUPRO)     | Rôle Qualité      |
| R-02  | Défaillance d'un fournisseur stratégique                   | P02       | 2     | 4     | 8     | Diversification du panel fournisseurs, fournisseurs de secours| Rôle Achats       |
| R-03  | Retard de livraison impactant la satisfaction client       | P04       | 3     | 3     | 9     | Suivi proactif des expéditions, marges de sécurité sur les délais | Rôle Logistique|
| R-04  | Perte de compétences clés liée au départ de personnel      | PS02      | 2     | 3     | 6     | Documentation des savoir-faire, plans de formation croisée   | Direction         |
| R-05  | Non-respect des exigences réglementaires internationales   | P02/P04   | 2     | 4     | 8     | Veille réglementaire systématique, mise à jour des procédures| Rôle Qualité      |
| R-06  | Erreur de communication avec le client sur les spécifications | P01    | 2     | 3     | 6     | Revue des exigences formalisée, confirmation écrite          | Rôle Commercial   |
| R-07  | Perte de données ou de documents critiques du SMQ          | PS01      | 1     | 4     | 4     | Sauvegardes régulières, système documentaire sécurisé        | Rôle Gestion Doc. |
| R-08  | Fluctuation des taux de change impactant les marges        | P01/P02   | 3     | 2     | 6     | Clauses contractuelles de révision, couverture de change     | Direction         |

#### Opportunités identifiées

| Réf.  | Opportunité                                               | Processus | Impact | Action d'exploitation                                        | Responsable       |
|-------|-----------------------------------------------------------|-----------|--------|---------------------------------------------------------------|-------------------|
| O-01  | Certification ISO 9001 comme levier commercial            | P01       | Élevé  | Communication active auprès des prospects et clients          | Rôle Commercial   |
| O-02  | Digitalisation des rapports d'inspection                  | P03       | Élevé  | Déploiement d'outils numériques de reporting en temps réel    | Rôle Qualité      |
| O-03  | Expansion vers de nouveaux marchés géographiques          | P01/P02   | Élevé  | Prospection de fournisseurs et clients dans de nouvelles régions | Rôle Commercial |
| O-04  | Partenariats avec des laboratoires d'essais internationaux| P03       | Moyen  | Établissement de conventions avec des laboratoires accrédités | Rôle Qualité      |

---

## 6.2 Objectifs qualité et planification des actions

### 6.2.1 Objectifs qualité

Les objectifs qualité de Plus Sàrl sont définis annuellement par la Direction, en cohérence avec la politique qualité et les résultats de la revue de direction.

| Réf.  | Objectif qualité                                         | Indicateur (KPI)                          | Cible          | Fréquence de mesure | Responsable       |
|-------|----------------------------------------------------------|-------------------------------------------|----------------|---------------------|-------------------|
| OQ-01 | Maintenir un taux de satisfaction client élevé           | Note moyenne de satisfaction client        | >= 8/10        | Semestrielle        | Rôle Commercial   |
| OQ-02 | Réduire le taux de non-conformités fournisseurs          | Nombre de NC / Nombre de commandes (%)    | <= 5%          | Trimestrielle       | Rôle Qualité      |
| OQ-03 | Assurer le respect des délais de livraison               | Taux de livraisons à temps (%)            | >= 90%         | Mensuelle           | Rôle Logistique   |
| OQ-04 | Garantir la réalisation des inspections planifiées       | Taux d'inspections réalisées / planifiées | >= 95%         | Mensuelle           | Rôle Qualité      |
| OQ-05 | Améliorer la maîtrise documentaire du SMQ                | Taux de documents à jour (%)              | >= 98%         | Trimestrielle       | Rôle Gestion Doc. |
| OQ-06 | Développer les compétences du personnel                  | Taux de réalisation du plan de formation  | >= 80%         | Annuelle            | Direction         |

### 6.2.2 Planification des actions pour atteindre les objectifs

| Réf.  | Actions planifiées                                        | Ressources nécessaires         | Échéance       | Responsable       |
|-------|-----------------------------------------------------------|--------------------------------|----------------|-------------------|
| OQ-01 | Mise en place d'enquêtes de satisfaction systématiques    | Outil de sondage en ligne      | T2 2026        | Rôle Commercial   |
| OQ-02 | Renforcement des critères de qualification fournisseurs   | Grille d'audit mise à jour     | T1 2026        | Rôle Achats       |
| OQ-03 | Mise en place d'un tableau de suivi logistique            | Outil de tracking              | T2 2026        | Rôle Logistique   |
| OQ-04 | Planification anticipée des inspections à 4 semaines      | Planning partagé               | Continu        | Rôle Qualité      |
| OQ-05 | Revue trimestrielle de l'état documentaire               | Checklist documentaire         | Trimestriel    | Rôle Gestion Doc. |
| OQ-06 | Élaboration du plan de formation annuel                   | Budget formation               | T1 2026        | Direction         |

---

## 6.3 Planification des modifications

### 6.3.1 Gestion des modifications du SMQ

Toute modification significative du SMQ fait l'objet d'une planification structurée selon la démarche suivante :

| Étape | Action                                    | Description                                                      | Responsable       |
|-------|-------------------------------------------|------------------------------------------------------------------|-------------------|
| 1     | Identification du besoin de modification  | Détection du besoin (audit, revue, retour client, évolution réglementaire) | Tout rôle     |
| 2     | Analyse d'impact                          | Évaluation des conséquences sur les processus, ressources et performances | Rôle Qualité  |
| 3     | Planification de la modification          | Définition des actions, ressources, responsabilités et échéances  | Rôle Qualité      |
| 4     | Approbation                               | Validation de la modification par la Direction                    | Direction         |
| 5     | Mise en œuvre                            | Implémentation de la modification selon le plan                   | Rôle concerné     |
| 6     | Vérification                              | Contrôle de l'efficacité de la modification                       | Rôle Qualité      |
| 7     | Mise à jour documentaire                  | Actualisation des documents impactés                              | Rôle Gestion Doc. |

### 6.3.2 Registre des modifications

Un registre des modifications est tenu à jour et contient :
- La description de la modification
- La justification
- L'analyse d'impact
- Les actions mises en œuvre
- Le résultat de la vérification d'efficacité

### 6.3.3 Critères déclenchant une revue de modification

| Critère                                          | Exemple                                                |
|--------------------------------------------------|--------------------------------------------------------|
| Changement organisationnel                       | Modification de la structure des rôles                 |
| Évolution réglementaire                          | Nouvelle réglementation d'importation                  |
| Retour d'expérience significatif                 | Non-conformité majeure récurrente                      |
| Demande client spécifique                        | Nouvelle exigence contractuelle                        |
| Résultat d'audit (interne ou externe)            | Non-conformité audit ISO 9001                          |
| Évolution technologique                          | Nouveau système d'information                          |

---

## Références normatives

| Clause ISO 9001:2015 | Exigence                                                     |
|-----------------------|--------------------------------------------------------------|
| 6.1                   | Actions à mettre en œuvre face aux risques et opportunités   |
| 6.1.1                 | Prise en compte des enjeux et des exigences                   |
| 6.1.2                 | Planification des actions                                     |
| 6.2                   | Objectifs qualité et planification des actions                |
| 6.2.1                 | Objectifs qualité                                             |
| 6.2.2                 | Planification des actions pour atteindre les objectifs        |
| 6.3                   | Planification des modifications                               |

---

*Document contrôlé - Toute copie imprimée est considérée comme non contrôlée.*
*Plus Sàrl - Système de Management de la Qualité ISO 9001:2015 - v0.7*
