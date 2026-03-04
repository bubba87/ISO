# Manuel Qualite - Chapitre 10 : Amelioration

| **Document**       | MQ_10_Amelioration                       |
|--------------------|------------------------------------------|
| **Version**        | v0.6                                     |
| **Date**           | 2026-03-04                               |
| **Classification** | Interne                                  |
| **Processus**      | PS03 - Amelioration continue             |
| **Redaction**      | Role Qualite                             |
| **Approbation**    | Direction                                |

---

## 10.1 Generalites

Plus Sarl determine et selectionne les opportunites d'amelioration et entreprend les actions necessaires pour satisfaire aux exigences des clients et accroitre leur satisfaction. L'amelioration porte sur :

- L'amelioration des produits et services pour satisfaire aux exigences et prendre en compte les besoins et attentes futurs
- La correction, la prevention ou la reduction des effets indesirables
- L'amelioration de la performance et de l'efficacite du Systeme de Management de la Qualite

### Sources d'amelioration

| Source                               | Type de donnee                           | Responsable de l'analyse |
|--------------------------------------|------------------------------------------|--------------------------|
| Resultats d'audits internes          | Constats, NC, observations               | Role Qualite             |
| Reclamations clients                 | Fiches de reclamation                    | Role Commercial          |
| Non-conformites produits             | Rapports de NC                           | Role Qualite             |
| Evaluations fournisseurs             | Scores et tendances                      | Role Achats              |
| Indicateurs de performance           | Tableaux de bord KPIs                    | Role Qualite             |
| Revues de direction                  | Comptes-rendus, decisions                | Direction                |
| Retours des collaborateurs           | Suggestions, retours d'experience        | Tous les roles           |
| Veille concurrentielle et normative  | Rapports de veille                       | Role Qualite             |

---

## 10.2 Non-conformite et action corrective

### 10.2.1 Processus de traitement des non-conformites en 6 etapes

Le traitement des non-conformites suit un processus structure en **six etapes** :

#### Etape 1 : Detection et enregistrement

| Action                               | Description                                                      | Responsable       | Delai       |
|--------------------------------------|------------------------------------------------------------------|--------------------|-------------|
| Detection de la NC                   | Identification lors d'une inspection, audit, reclamation ou controle interne | Tout role  | Immediat    |
| Enregistrement                       | Ouverture d'une fiche de non-conformite avec description factuelle | Role Qualite     | 24 heures   |
| Attribution d'un numero unique       | Reference sequentielle NC-AAAA-XXX                               | Role Qualite       | 24 heures   |
| Classification initiale              | Categorisation selon la grille de severite                       | Role Qualite       | 24 heures   |

#### Etape 2 : Action immediate (containment)

| Action                               | Description                                                      | Responsable       | Delai       |
|--------------------------------------|------------------------------------------------------------------|--------------------|-------------|
| Isolement du produit NC              | Separation physique ou marquage des produits non conformes       | Role Qualite       | Immediat    |
| Notification des parties concernees  | Information du client, du fournisseur et des roles internes      | Role Commercial / Role Achats | 24 heures |
| Securisation                         | Prevention de l'utilisation ou de l'expedition du produit NC     | Role Qualite / Role Logistique | Immediat |

#### Etape 3 : Analyse des causes racines

| Methode d'analyse                    | Description                                                      | Application                     |
|--------------------------------------|------------------------------------------------------------------|---------------------------------|
| 5 Pourquoi                           | Questionnement iteratif pour remonter a la cause racine          | NC simples, causes lineaires    |
| Diagramme d'Ishikawa                 | Analyse des causes par categorie (5M : Matiere, Methode, Main-d'oeuvre, Milieu, Materiel) | NC complexes, causes multiples |
| Arbre des causes                     | Representation graphique des enchainements causaux               | NC graves ou recurrentes        |

| Element a analyser                   | Questions cles                                                   |
|--------------------------------------|------------------------------------------------------------------|
| Matiere                              | Le produit/materiau etait-il conforme aux specifications ?       |
| Methode                              | La procedure etait-elle respectee ? Etait-elle adequate ?        |
| Main-d'oeuvre                        | Le personnel etait-il competent et forme ?                       |
| Milieu                               | L'environnement de production etait-il adequat ?                 |
| Materiel                             | Les equipements etaient-ils adaptes et en bon etat ?             |

#### Etape 4 : Definition et mise en oeuvre des actions correctives

| Action                               | Description                                                      | Responsable       | Delai       |
|--------------------------------------|------------------------------------------------------------------|--------------------|-------------|
| Definition de l'action corrective    | Description precise de l'action visant a eliminer la cause racine| Role Qualite       | 5 jours     |
| Validation de l'action               | Approbation par le responsable competent                         | Direction / Role Qualite | 2 jours |
| Mise en oeuvre                        | Implementation de l'action corrective                            | Role concerne      | 15 jours    |
| Documentation                        | Mise a jour de la fiche NC avec les actions entreprises          | Role Qualite       | Continue    |

#### Etape 5 : Verification de l'efficacite

| Action                               | Description                                                      | Responsable       | Delai       |
|--------------------------------------|------------------------------------------------------------------|--------------------|-------------|
| Controle de mise en oeuvre           | Verification que l'action a ete implementee comme prevu          | Role Qualite       | Post-implementation |
| Evaluation de l'efficacite           | Verification que la cause racine a ete eliminee                  | Role Qualite       | 30-90 jours |
| Controle de non-recurrence           | Surveillance pour confirmer l'absence de recurrence              | Role Qualite       | 3 mois      |
| Decision de cloture                  | Cloture de la fiche NC si l'efficacite est confirmee             | Role Qualite       | Apres verification |

#### Etape 6 : Capitalisation et retour d'experience

| Action                               | Description                                                      | Responsable       |
|--------------------------------------|------------------------------------------------------------------|--------------------|
| Mise a jour des documents            | Revision des procedures ou instructions si necessaire            | Role Gestion Documentaire |
| Communication interne                | Partage des lecons apprises avec les roles concernes             | Role Qualite       |
| Mise a jour du registre des risques  | Ajustement de l'analyse de risques si necessaire (cf. MQ_06)    | Role Qualite       |
| Integration en revue de direction    | Presentation des NC significatives et tendances                  | Role Qualite       |

---

### 10.2.2 Classification des non-conformites (4 niveaux)

| Niveau | Categorie      | Description                                                                   | Delai de traitement | Approbation requise |
|--------|----------------|-------------------------------------------------------------------------------|---------------------|---------------------|
| 1      | **Mineure**    | Ecart ponctuel sans impact significatif sur la conformite du produit ou la satisfaction client | 30 jours           | Role Qualite        |
| 2      | **Significative** | Ecart affectant partiellement la conformite ou necessitant une action corrective structuree | 15 jours           | Role Qualite        |
| 3      | **Majeure**    | Ecart systematique ou impactant significativement la conformite du produit, la satisfaction client ou l'efficacite du SMQ | 5 jours            | Direction           |
| 4      | **Critique**   | Ecart mettant en cause la securite du produit, la conformite reglementaire ou pouvant entrainer des consequences graves pour le client | Immediat           | Direction           |

### 10.2.3 Matrice d'escalade

| Niveau de NC    | Notification                          | Decision de traitement | Suivi                |
|-----------------|---------------------------------------|------------------------|----------------------|
| Mineure         | Role Qualite                          | Role Qualite           | Role Qualite         |
| Significative   | Role Qualite, Role concerne           | Role Qualite           | Role Qualite         |
| Majeure         | Direction, Role Qualite, Client       | Direction              | Role Qualite         |
| Critique        | Direction, Client, Fournisseur        | Direction              | Direction / Role Qualite |

---

## 10.3 Amelioration continue

### 10.3.1 Cycle PDCA (Plan-Do-Check-Act)

Plus Sarl applique le cycle PDCA (roue de Deming) comme methode fondamentale d'amelioration continue a tous les niveaux du SMQ.

```
        ┌─────────────────────────────────────────┐
        │            PLAN (Planifier)              │
        │  - Identifier les opportunites           │
        │  - Definir les objectifs                 │
        │  - Planifier les actions                 │
        └──────────────────┬──────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────┐
│                DO (Realiser)                      │
│  - Mettre en oeuvre les actions planifiees        │
│  - Collecter les donnees                         │
│  - Documenter les resultats                      │
└──────────────────┬───────────────────────────────┘
                   │
                   ▼
        ┌─────────────────────────────────────────┐
        │           CHECK (Verifier)               │
        │  - Mesurer les resultats                 │
        │  - Comparer aux objectifs                │
        │  - Analyser les ecarts                   │
        └──────────────────┬──────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────┐
│                ACT (Agir)                         │
│  - Standardiser si objectif atteint              │
│  - Corriger si ecart                             │
│  - Relancer un nouveau cycle                     │
└──────────────────────────────────────────────────┘
```

### 10.3.2 Application du PDCA par processus

| Processus | PLAN                                    | DO                                     | CHECK                                  | ACT                                    |
|-----------|-----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|
| P01       | Objectifs commerciaux, plan d'action    | Prospection, offres, suivi client      | KPIs commerciaux, satisfaction client  | Ajustement strategie commerciale       |
| P02       | Criteres de selection, panel cible      | Qualification, commandes, evaluations  | Scores fournisseurs, taux NC           | Revision panel, actions correctives    |
| P03       | Plan d'inspection, checklists           | Inspections, rapports, decisions       | Taux acceptation, efficacite inspections | Ajustement methodes, formation        |
| P04       | Planning logistique, objectifs delais   | Expeditions, suivi, documentation      | Taux livraison a temps, reclamations   | Optimisation flux, nouveaux partenaires|
| PS01      | Plan documentaire, objectifs            | Creation, mise a jour, diffusion       | Taux documents a jour, audits doc      | Revision procedures, formation         |
| PM01      | Politique, objectifs qualite            | Pilotage, allocation ressources        | Revue de direction, KPIs globaux       | Revision strategie, nouveaux objectifs |

### 10.3.3 Outils d'amelioration continue

| Outil                                | Application                                                      | Frequence d'utilisation |
|--------------------------------------|------------------------------------------------------------------|-------------------------|
| Analyse de tendances                 | Suivi de l'evolution des KPIs dans le temps                      | Mensuelle               |
| Benchmarking                         | Comparaison avec les meilleures pratiques du secteur             | Annuelle                |
| Brainstorming                        | Generation d'idees d'amelioration en equipe                      | Selon besoin            |
| Analyse Pareto                       | Identification des causes principales de NC (regle 80/20)       | Trimestrielle           |
| Retour d'experience (REX)           | Capitalisation des lecons apprises apres chaque projet significatif | A chaque cloture de projet |

### 10.3.4 Programme d'amelioration annuel

| Element                              | Description                                                      | Responsable       |
|--------------------------------------|------------------------------------------------------------------|--------------------|
| Revue des performances               | Analyse des resultats de l'annee ecoulee                        | Direction / Role Qualite |
| Identification des axes d'amelioration | Selection des priorites basee sur les donnees                  | Direction          |
| Plan d'actions d'amelioration        | Actions definies avec responsables, ressources et echeances     | Role Qualite       |
| Suivi trimestriel                    | Revue de l'avancement des actions d'amelioration                | Role Qualite       |
| Bilan annuel                         | Evaluation de l'efficacite du programme d'amelioration          | Direction          |

### 10.3.5 Indicateurs d'amelioration continue

| Indicateur                          | Formule / Methode                        | Cible         | Frequence     |
|--------------------------------------|------------------------------------------|---------------|---------------|
| Nombre d'actions d'amelioration lancees | Comptage                              | >= 6/an       | Annuelle      |
| Taux de realisation des actions d'amelioration | Actions realisees / planifiees (%) | >= 80%     | Semestrielle  |
| Taux d'efficacite des actions correctives | AC efficaces / AC cloturees (%)     | >= 90%        | Annuelle      |
| Evolution du taux de NC global       | Tendance sur 12 mois glissants           | Baisse continue | Trimestrielle |
| Nombre de recurrences de NC          | NC identiques sur 12 mois               | 0 recurrence  | Annuelle      |

---

## References normatives

| Clause ISO 9001:2015 | Exigence                                                     |
|-----------------------|--------------------------------------------------------------|
| 10.1                  | Generalites                                                   |
| 10.2                  | Non-conformite et action corrective                           |
| 10.2.1                | Reaction a la non-conformite                                  |
| 10.2.2                | Conservation des informations documentees                     |
| 10.3                  | Amelioration continue                                         |

---

*Document controle - Toute copie imprimee est consideree comme non controlee.*
*Plus Sarl - Systeme de Management de la Qualite ISO 9001:2015 - v0.6*
