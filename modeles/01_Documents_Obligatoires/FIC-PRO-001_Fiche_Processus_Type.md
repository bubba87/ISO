# Fiche Processus Type

> Ce modele est a dupliquer et a adapter pour chaque processus identifie
> dans la cartographie (CRT-QUA-001).

| | |
|---|---|
| **Reference** | FIC-PRO-[XXX] |
| **Version** | 1.0 |
| **Date de creation** | [JJ/MM/AAAA] |
| **Date de revision** | [JJ/MM/AAAA] |
| **Redige par** | [Nom de la gerante] |
| **Approuve par** | [Nom de la gerante] |

---

## Identification du processus

| Element | Description |
|---|---|
| **Nom du processus** | [Ex : Commercial / Conception / Achats & Sous-traitance / Controle & Livraison] |
| **Code** | [Ex : O1 / O2 / O3 / O4 / M1 / S1] |
| **Type** | [Management / Operationnel / Support] |
| **Pilote** | [Gerante] |
| **Finalite** | [Objectif principal du processus en 1-2 phrases] |

---

## Donnees d'entree et de sortie

| Donnees d'entree (inputs) | Provenance |
|---|---|
| [Ex : Demande client, cahier des charges] | [Ex : Client, processus commercial] |
| [Ex : Plans techniques] | [Ex : Client, processus conception] |
| [A completer] | [A completer] |

| Donnees de sortie (outputs) | Destinataire |
|---|---|
| [Ex : Offre technique et commerciale] | [Ex : Client] |
| [Ex : Bon de commande fournisseur] | [Ex : Partenaire chinois] |
| [A completer] | [A completer] |

---

## Description des activites

| # | Activite | Description | Responsable | Document/Enregistrement |
|---|---|---|---|---|
| 1 | [Nom de l'activite] | [Description de ce qui est fait] | [Qui] | [Document utilise ou cree] |
| 2 | [Nom de l'activite] | [Description de ce qui est fait] | [Qui] | [Document utilise ou cree] |
| 3 | [Nom de l'activite] | [Description de ce qui est fait] | [Qui] | [Document utilise ou cree] |
| 4 | [Nom de l'activite] | [Description de ce qui est fait] | [Qui] | [Document utilise ou cree] |
| 5 | [Nom de l'activite] | [Description de ce qui est fait] | [Qui] | [Document utilise ou cree] |

---

## Logigramme (flux d'activites)

```
    [Evenement declencheur]
            |
            v
    +------------------+
    | Activite 1       |----> [Document/Enregistrement]
    +------------------+
            |
            v
    +------------------+
    | Activite 2       |----> [Document/Enregistrement]
    +------------------+
            |
            v
      /  Decision  \
     /   conforme ? \
    /                \
   OUI              NON
    |                 |
    v                 v
+----------+  +------------------+
| Activite |  | Traitement NC    |
| suivante |  | (PRO-NCF-001)    |
+----------+  +------------------+
    |
    v
    [Sortie / Livrable]
```

> Adaptez ce logigramme a votre processus reel.

---

## Ressources necessaires

| Type de ressource | Description |
|---|---|
| **Humaines** | [Ex : Gerante - X heures/semaine sur ce processus] |
| **Materielles** | [Ex : Ordinateur, logiciel CAO, instruments de mesure] |
| **Informatiques** | [Ex : Email, ERP, logiciel de conception] |
| **Documentaires** | [Ex : Normes, catalogues fournisseurs, plans] |
| **Financieres** | [Ex : Budget annuel prevu pour ce processus] |

---

## Indicateurs de performance

| Indicateur | Formule de calcul | Objectif | Frequence | Source de donnees |
|---|---|---|---|---|
| [Nom de l'indicateur] | [Comment le calculer] | [Cible] | [Mensuel/Trimestriel/Annuel] | [Ou trouver les donnees] |
| [Nom de l'indicateur] | [Comment le calculer] | [Cible] | [Mensuel/Trimestriel/Annuel] | [Ou trouver les donnees] |

---

## Risques et opportunites associes

Voir CTX-QUA-001 pour le detail. Resume :

| # | Risque / Opportunite | Niveau | Action |
|---|---|---|---|
| [Rxx] | [Description] | [Faible/Moyen/Eleve] | [Action prevue] |
| [Oxx] | [Description] | [Faible/Moyen/Eleve] | [Action prevue] |

---

## Interfaces avec les autres processus

| Processus en interface | Nature de l'interaction |
|---|---|
| [Code et nom du processus] | [Ce qui est echange : donnees, documents, produits] |
| [Code et nom du processus] | [Ce qui est echange] |

---

## Exigences applicables

| Type | Exigence | Reference |
|---|---|---|
| ISO 9001:2015 | [Chapitre(s) applicable(s)] | [Ex : 8.2, 8.4] |
| Reglementaire | [Si applicable] | [Reference du texte] |
| Client | [Exigences specifiques] | [Reference] |

---

## Historique des revisions

| Version | Date | Modification | Auteur |
|---|---|---|---|
| 1.0 | [JJ/MM/AAAA] | Creation initiale | [Nom] |
| | | | |

---

> **Instructions :**
> 1. Dupliquez ce modele pour chaque processus : O1, O2, O3, O4, M1, M2, M3, S1, S2, S3
> 2. Nommez le fichier : FIC-PRO-O1, FIC-PRO-O2, etc.
> 3. Completez toutes les sections
> 4. Les processus critiques pour votre activite sont O3 (Achats/Sous-traitance) et O4 (Controle)
> 5. Gardez les fiches simples et concretes - decrivez ce que vous faites reellement

---

# Exemples pre-remplis

## Exemple : Fiche Processus O3 - Achats et Sous-traitance

| Element | Description |
|---|---|
| **Nom** | Achats et Sous-traitance |
| **Code** | O3 |
| **Pilote** | Gerante |
| **Finalite** | Assurer que les moules et pieces fabriques par le partenaire chinois sont conformes aux specifications |

**Activites :**

| # | Activite | Description | Document |
|---|---|---|---|
| 1 | Reception du cahier des charges interne | Recevoir les specifications du processus conception | Cahier des charges |
| 2 | Transmission au partenaire chinois | Envoyer les specifications, plans et exigences | Email + accusé de reception |
| 3 | Suivi de fabrication | Suivre l'avancement (echanges, photos, rapports d'etape) | Emails, rapports fournisseur |
| 4 | Validation pre-expedition | Verifier les rapports d'inspection du partenaire avant expedition | Rapport d'inspection fournisseur |
| 5 | Evaluation du partenaire | Evaluer les performances (conformite, delais) | FOR-EVF-001 |

**Indicateurs :**

| Indicateur | Cible |
|---|---|
| Taux de conformite des livraisons fournisseur | >= 95% |
| Taux de respect des delais fournisseur | >= 90% |
| Note d'evaluation annuelle fournisseur | >= [X/10] |
