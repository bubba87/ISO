# Fiche Processus O3 - Logistique et Livraison

| | |
|---|---|
| **Reference** | FIC-PRO-002 |
| **Version** | 0.4 |
| **Date de creation** | 18/02/2026 |
| **Date de revision** | 18/02/2026 |
| **Redige par** | Roxane Wicky |
| **Approuve par** | Roxane Wicky |

> **Legende :** 🔴 [A REMPLIR] = obligatoire, manquant | 🟡 [RECOMMANDE] = recommande | 🟢 = deja rempli | 🔵 [A VERIFIER] = a confirmer

---

## Identification du processus

| Element | Description |
|---|---|
| **Nom du processus** | Logistique et Livraison |
| **Code** | O3 |
| **Type** | Operationnel |
| **Pilote** | Roxane Wicky (Gerante) |
| **Finalite** | Organiser le transport international des pieces depuis la Chine vers les clients europeens, gerer les documents douaniers, assurer le suivi des expeditions et la livraison dans les delais. |

---

## Donnees d'entree et de sortie

| Donnees d'entree (inputs) | Provenance |
|---|---|
| Produits fabriques prets a l'expedition | Processus O2 - Achats et Sous-traitance |
| Documents d'exportation (facture douaniere, packing list) | Processus O2 - Achats et Sous-traitance |
| Delais de livraison convenus avec le client | Processus O1 - Commercial |
| Commande client et informations de livraison | S1 - Gestion documentaire (FileMaker) |

| Donnees de sortie (outputs) | Destinataire |
|---|---|
| Livraison confirmee au client | Client final |
| Documents douaniers (declaration import/export, certificats) | Autorites douanieres CH et EU / Client |
| Suivi de transport (tracking, notifications d'avancement) | Interne / Client |
| Confirmation de reception par le client | Processus O1 - Commercial / FileMaker |
| Donnees de performance logistique (delais effectifs, incidents) | Processus M2 - Amelioration continue |

---

## Description des activites

| # | Activite | Description | Responsable | Document/Enregistrement |
|---|---|---|---|---|
| 1 | Reception notification produits prets | Recevoir du processus O2 la confirmation que les produits sont fabriques, controles et prets a l'expedition. Verifier la completude des documents d'exportation fournis par O2. | Roxane Wicky | Notification de pret a l'expedition, packing list, facture douaniere |
| 2 | Creation fiche livraison FileMaker | Creer ou mettre a jour la fiche de livraison dans FileMaker avec les informations : delais convenus, conditions d'expedition, mode de transport, adresse de livraison client, references commande. | Roxane Wicky | Fiche livraison FileMaker |
| 3 | Preparation documents douaniers | Preparer l'ensemble des documents douaniers necessaires a l'exportation depuis la Chine et a l'importation en Suisse/UE, conformement a la legislation applicable. Verifier la conformite de chaque document. | Roxane Wicky | Declaration douaniere, certificat d'origine, facture commerciale, packing list |
| 4 | Organisation du transport | Selectionner le mode de transport adapte (aerien, maritime ou ferroviaire) selon l'urgence, le volume et le cout. Coordonner avec le transporteur pour la prise en charge des marchandises. | Roxane Wicky | Bon de transport, booking confirmation, emails transporteur |
| 5 | Suivi de l'expedition | Suivre l'acheminement des marchandises via les outils de tracking du transporteur. Communiquer proactivement avec le client sur l'avancement. Intervenir en cas de retard ou d'incident. | Roxane Wicky | Tracking transporteur, emails de suivi, messages WeChat |
| 6 | Gestion des douanes | Coordonner le dedouanement a l'arrivee (importation CH ou EU). S'assurer de la conformite des documents avec les exigences reglementaires. Gerer les eventuelles demandes complementaires des autorites douanieres. | Roxane Wicky | Documents de dedouanement, confirmation de passage en douane |
| 7 | Confirmation reception client | Obtenir la confirmation de reception de la marchandise par le client. Verifier que la livraison correspond a la commande (quantite, etat, delai). Enregistrer toute remarque ou reclamation. | Roxane Wicky | Confirmation de reception client, email/message de confirmation |
| 8 | Cloture dans FileMaker | Mettre a jour la fiche de livraison dans FileMaker : date de livraison effective, statut de la commande, eventuelles remarques. Cloturer le dossier de livraison. | Roxane Wicky | Fiche livraison FileMaker (mise a jour), enregistrement de cloture |

---

## Logigramme (flux d'activites)

```
    [Notification produits prets recue du processus O2 - Achats]
            |
            v
    +-------------------------------+
    | 1. Reception notification     |----> Packing list, facture
    |    produits prets (O2)        |      douaniere recus
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 2. Creation fiche livraison   |----> Fiche livraison FileMaker
    |    dans FileMaker (delais,    |      (references, adresse,
    |    conditions expedition)     |       mode de transport)
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 3. Preparation documents      |----> Declaration douaniere,
    |    douaniers (conformes       |      certificat d'origine,
    |    legislation EU et CH)      |      facture commerciale
    +-------------------------------+
            |
            v
      /  Documents douaniers  \
     /   complets et conformes ?\
    /                            \
   OUI                          NON
    |                             |
    |                             v
    |                   +------------------+
    |                   | Correction des   |
    |                   | documents        |---> Retour a l'etape 3
    |                   +------------------+
    v
    +-------------------------------+
    | 4. Organisation transport     |----> Aerien / Maritime /
    |    (selection mode selon      |      Ferroviaire
    |    urgence et volume)         |      Booking confirmation
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 5. Suivi expedition           |----> Tracking transporteur,
    |    (tracking jusqu'a          |      notifications client,
    |    livraison finale)          |      emails/WeChat
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 6. Gestion douanes            |----> Dedouanement import,
    |    (conformite import/export) |      documents de passage
    +-------------------------------+
            |
            v
      /  Dedouanement        \
     /   effectue sans         \
    /    probleme ?              \
   OUI                          NON
    |                             |
    |                             v
    |                   +---------------------------+
    |                   | Resolution probleme       |
    |                   | douanier (documents       |
    |                   | complementaires,          |
    |                   | coordination autorites)   |
    |                   +---------------------------+
    v
    +-------------------------------+
    | 7. Confirmation reception     |----> Email/message de
    |    client                     |      confirmation client
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 8. Cloture dans FileMaker     |----> Fiche livraison mise a
    |    (date effective, statut,   |      jour, dossier cloture
    |    remarques)                 |
    +-------------------------------+
            |
            v
    [Livraison terminee - dossier cloture]
```

---

## Ressources necessaires

| Type de ressource | Description |
|---|---|
| **Humaines** | Roxane Wicky (Gerante) - pilotage complet du processus logistique, coordination avec transporteurs et autorites douanieres |
| **Materielles** | Bureau a Cudrefin (Route de Montet 11, 1588 Cudrefin), ordinateur, telephone |
| **Informatiques** | Email (communication formelle avec clients, transporteurs et douanes), WeChat (coordination avec partenaires chinois pour l'expedition), FileMaker (suivi des livraisons, enregistrement des informations). Sauvegarde cloud chez le fournisseur 🟢 |
| **Documentaires** | Documents d'exportation, reglementations douanieres CH et EU, tarifs transporteurs, historique des livraisons |
| **Financieres** | 🟡 [RECOMMANDE — definir le budget annuel transport et logistique] |

---

## Indicateurs de performance

| Indicateur | Formule de calcul | Objectif | Frequence | Source de donnees |
|---|---|---|---|---|
| Respect des delais de livraison | Nombre de livraisons dans les delais / Nombre total de livraisons x 100 | >= 95% 🟢 | Par livraison | Suivi des livraisons FileMaker |
| Precision delai maritime/ferroviaire | Ecart entre date de livraison effective et date prevue (transport maritime ou ferroviaire) | +/- 10 jours 🟢 | Par livraison | Suivi des livraisons FileMaker |
| Precision delai aerien | Ecart entre date de livraison effective et date prevue (transport aerien) | +/- 3 jours 🟢 | Par livraison | Suivi des livraisons FileMaker |
| Conformite des documents douaniers | Nombre de dossiers douaniers conformes du premier coup / Nombre total de dossiers x 100 | 100% | Par livraison | Dossiers douaniers, FileMaker |
| Taux d'incidents transport | Nombre de livraisons avec incident (perte, dommage, retard majeur) / Nombre total de livraisons x 100 | 🟡 [RECOMMANDE — definir un objectif apres 1ere annee de reference] | Trimestriel | Suivi des livraisons FileMaker |

---

## Actions d'amelioration planifiees

| # | Action | Description | Echeance | Statut |
|---|---|---|---|---|
| A05 | Comparatif transporteurs | Etablir un comparatif des transporteurs utilises (delais, fiabilite, cout) pour optimiser le choix du mode de transport selon les situations. | T2 2026 | Planifie |
| A06 | Procedure douaniere formalisee | Formaliser une check-list des documents douaniers requis par type d'expedition (CH, UE) pour reduire le risque d'erreur. | T2 2026 | Planifie |

---

## Risques et opportunites associes

Voir CTX-QUA-001 pour le detail. Resume :

| # | Risque / Opportunite | Niveau | Action |
|---|---|---|---|
| R04 | Retards de transport (aleas maritimes, aeriens, ferroviaires, conditions meteorologiques, congestionnement portuaire) | Eleve | Anticipation des delais avec marge de securite, suivi en temps reel des expeditions, communication proactive avec le client en cas de retard, choix du mode de transport adapte a l'urgence |
| R05 | Formalites douanieres (erreur documentaire, changement reglementaire, blocage en douane) | Faible | Preparation rigoureuse des documents, veille reglementaire, check-list des documents requis, relation avec les autorites douanieres |
| O04 | Optimisation des delais de livraison (amelioration continue des circuits logistiques) | Moyen | Comparatif regulier des transporteurs et des modes de transport, consolidation des envois lorsque possible, retour d'experience sur chaque livraison |

---

## Interfaces avec les autres processus

| Processus en interface | Nature de l'interaction |
|---|---|
| **O1 - Commercial** | Recoit : delais de livraison convenus avec le client, adresse de livraison, conditions particulieres. Fournit : confirmation de livraison, date effective, suivi transport |
| **O2 - Achats et Sous-traitance** | Recoit : produits prets a expedier, documents d'exportation (facture douaniere, packing list). Fournit : confirmation de prise en charge par le transporteur |
| **O4 - Controle qualite** | Recoit : signalement de NC detectee a reception chez le client. Fournit : information sur l'etat des marchandises a la livraison, reclamations liees au transport |
| **S1 - Gestion documentaire** | Fournit : enregistrements (fiches livraison, documents douaniers, confirmations de transport). Recoit : acces aux historiques et donnees dans FileMaker |
| **M2 - Amelioration continue** | Fournit : donnees de performance logistique (delais, incidents, conformite douaniere). Recoit : objectifs d'amelioration, actions correctives a mettre en oeuvre |

---

## Exigences applicables

| Type | Exigence | Reference |
|---|---|---|
| ISO 9001:2015 | Preservation (des elements de sortie au cours de la production et de la prestation de service) | 8.5.4 |
| ISO 9001:2015 | Activites apres livraison | 8.5.5 |
| ISO 9001:2015 | Identification et tracabilite | 8.5.2 |
| ISO 9001:2015 | Propriete des clients ou des prestataires externes | 8.5.3 |
| Reglementaire | Reglementation douaniere suisse (importation depuis la Chine) | 🔵 [A VERIFIER — references specifiques] |
| Reglementaire | Reglementation douaniere europeenne (importation dans l'UE) | 🔵 [A VERIFIER — references specifiques selon pays client] |
| Reglementaire | Reglementations applicables au transport international de marchandises (aerien, maritime, ferroviaire) | 🔵 [A VERIFIER — selon les modes de transport utilises] |
| Client | Delais de livraison, conditions de livraison (Incoterms), adresse et instructions specifiques | Confirmation de commande client (par projet) |

---

## Particularites du processus

### Modes de transport

| Mode | Usage | Delai typique Chine-Europe | Critere de selection |
|---|---|---|---|
| **Aerien** | Commandes urgentes, petits volumes, echantillons | 5-10 jours | Urgence elevee, faible volume |
| **Maritime** | Volumes importants, commandes planifiees | 30-45 jours | Volume important, cout optimise |
| **Ferroviaire** | Compromis delai/cout, volumes moyens | 18-25 jours | Delai intermediaire, bon rapport cout/delai |

### Coordination avec les partenaires chinois

L'organisation du transport implique une coordination etroite avec les partenaires chinois (Yuyao Mould Factory et **Whang**) pour la mise a disposition des marchandises au point de depart. La communication se fait principalement par email et WeChat.

### Points d'attention specifiques

- **Douanes** : les formalites douanieres dependent du type de marchandise, du pays de destination et de la valeur declaree. Une attention particuliere est portee a la conformite de chaque dossier.
- **Incoterms** : les conditions de livraison (repartition des responsabilites entre Plus Sarl et le client) sont definies pour chaque commande.
- **Decalage horaire** : la coordination avec la Chine pour l'expedition implique un decalage horaire de 6 a 7 heures. WeChat permet des echanges rapides malgre ce decalage.
- **Fiduciaire Paradiso** : la fiduciaire intervient dans la gestion comptable et fiscale des operations d'import/export.
- **Sauvegarde** : tous les documents logistiques et douaniers sont sauvegardes dans le cloud. 🟢

---

## Historique des revisions

| Version | Date | Modification | Auteur |
|---|---|---|---|
| 0.4 | 18/02/2026 | Creation initiale de la fiche processus O3 - Logistique et Livraison. | Roxane Wicky |
