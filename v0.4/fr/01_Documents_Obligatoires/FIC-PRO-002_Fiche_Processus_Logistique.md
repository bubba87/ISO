# Fiche Processus O3 - Logistique et Livraison

| | |
|---|---|
| **Référence** | FIC-PRO-002 |
| **Version** | 0.4 |
| **Date de création** | 18/02/2026 |
| **Date de revision** | 18/02/2026 |
| **Rédigé par** | Roxane Wicky |
| **Approuve par** | Roxane Wicky |

> **Légende :** 🔴 [À REMPLIR] = obligatoire, manquant | 🟡 [RECOMMANDE] = recommandé | 🟢 = déjà rempli | 🔵 [À VÉRIFIER] = a confirmer

---

## Identification du processus

| Élément | Description |
|---|---|
| **Nom du processus** | Logistique et Livraison |
| **Code** | O3 |
| **Type** | Opérationnel |
| **Pilote** | Roxane Wicky (Gérante) |
| **Finalite** | Organiser le transport international des pièces depuis la Chine vers les clients européens, gérer les documents douaniers, assurer le suivi des expéditions et la livraison dans les délais. |

---

## Données d'entrée et de sortie

| Données d'entrée (inputs) | Provenance |
|---|---|
| Produits fabriques prêts à l\'expédition | Processus O2 - Achats et Sous-traitance |
| Documents d'exportation (facture douanière, packing list) | Processus O2 - Achats et Sous-traitance |
| Délais de livraison convenus avec le client | Processus O1 - Commercial |
| Commande client et informations de livraison | S1 - Gestion documentaire (FileMaker) |

| Données de sortie (outputs) | Destinataire |
|---|---|
| Livraison confirmée au client | Client final |
| Documents douaniers (déclaration import/export, certificats) | Autorites douanières CH et EU / Client |
| Suivi de transport (tracking, notifications d'avancement) | Interne / Client |
| Confirmation de reception par le client | Processus O1 - Commercial / FileMaker |
| Données de performance logistique (délais effectifs, incidents) | Processus M2 - Amélioration continue |

---

## Description des activités

| # | Activité | Description | Responsable | Document/Enregistrement |
|---|---|---|---|---|
| 1 | Reception notification produits prêts | Recevoir du processus O2 la confirmation que les produits sont fabriques, contrôles et prêts à l\'expédition. Vérifier la completude des documents d'exportation fournis par O2. | Roxane Wicky | Notification de pret à l\'expédition, packing list, facture douanière |
| 2 | Création fiche livraison FileMaker | Créer ou mettre a jour la fiche de livraison dans FileMaker avec les informations : délais convenus, conditions d'expédition, mode de transport, adresse de livraison client, références commande. | Roxane Wicky | Fiche livraison FileMaker |
| 3 | Préparation documents douaniers | Preparer l'ensemble des documents douaniers nécessaires à l\'exportation depuis la Chine et à l\'importation en Suisse/UE, conformément à la législation applicable. Vérifier la conformité de chaque document. | Roxane Wicky | Déclaration douanière, certificat d'origine, facture commerciale, packing list |
| 4 | Organisation du transport | Selectionner le mode de transport adapte (aérien, maritime ou ferroviaire) selon l'urgence, le volume et le coût. Coordonner avec le transporteur pour la prise en charge des marchandises. | Roxane Wicky | Bon de transport, booking confirmation, emails transporteur |
| 5 | Suivi de l'expédition | Suivre l'acheminement des marchandises via les outils de tracking du transporteur. Communiquer proactivement avec le client sur l'avancement. Intervenir en cas de retard ou d'incident. | Roxane Wicky | Tracking transporteur, emails de suivi, messages WeChat |
| 6 | Gestion des douanes | Coordonner le dédouanement à l\'arrivee (importation CH ou EU). S'assurer de la conformité des documents avec les exigences réglementaires. Gérer les éventuelles demandes complémentaires des autorites douanières. | Roxane Wicky | Documents de dédouanement, confirmation de passage en douane |
| 7 | Confirmation reception client | Obtenir la confirmation de reception de la marchandise par le client. Vérifier que la livraison correspond à la commande (quantité, état, délai). Enregistrer toute remarque ou réclamation. | Roxane Wicky | Confirmation de reception client, email/message de confirmation |
| 8 | Clôture dans FileMaker | Mettre a jour la fiche de livraison dans FileMaker : date de livraison effective, statut de la commande, éventuelles remarques. Clôturer le dossier de livraison. | Roxane Wicky | Fiche livraison FileMaker (mise à jour), enregistrement de clôture |

---

## Logigramme (flux d'activités)

```
    [Notification produits prêts reçue du processus O2 - Achats]
            |
            v
    +-------------------------------+
    | 1. Reception notification     |----> Packing list, facture
    |    produits prêts (O2)        |      douaniere reçus
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 2. Création fiche livraison   |----> Fiche livraison FileMaker
    |    dans FileMaker (délais,    |      (references, adresse,
    |    conditions expédition)     |       mode de transport)
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 3. Préparation documents      |----> Declaration douaniere,
    |    douaniers (conformes       |      certificat d'origine,
    |    législation EU et CH)      |      facture commerciale
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
    |                   | documents        |---> Retour à l\'étape 3
    |                   +------------------+
    v
    +-------------------------------+
    | 4. Organisation transport     |----> Aerien / Maritime /
    |    (sélection mode selon      |      Ferroviaire
    |    urgence et volume)         |      Booking confirmation
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 5. Suivi expédition           |----> Tracking transporteur,
    |    (tracking jusqu'a          |      notifications client,
    |    livraison finale)          |      emails/WeChat
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 6. Gestion douanes            |----> Dédouanement import,
    |    (conformité import/export) |      documents de passage
    +-------------------------------+
            |
            v
      /  Dédouanement        \
     /   effectue sans         \
    /    problème ?              \
   OUI                          NON
    |                             |
    |                             v
    |                   +---------------------------+
    |                   | Résolution problème       |
    |                   | douanier (documents       |
    |                   | complementaires,          |
    |                   | coordination autorites)   |
    |                   +---------------------------+
    v
    +-------------------------------+
    | 7. Confirmation réception     |----> Email/message de
    |    client                     |      confirmation client
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 8. Cloture dans FileMaker     |----> Fiche livraison mise a
    |    (date effective, statut,   |      jour, dossier clôturé
    |    remarques)                 |
    +-------------------------------+
            |
            v
    [Livraison terminee - dossier clôturé]
```

---

## Ressources nécessaires

| Type de ressource | Description |
|---|---|
| **Humaines** | Roxane Wicky (Gérante) - pilotage complet du processus logistique, coordination avec transporteurs et autorites douanières |
| **Materielles** | Bureau a Cudrefin (Route de Montet 11, 1588 Cudrefin), ordinateur, téléphone |
| **Informatiques** | Email (communication formelle avec clients, transporteurs et douanes), WeChat (coordination avec partenaires chinois pour l'expédition), FileMaker (suivi des livraisons, enregistrement des informations). Sauvegarde cloud chez le fournisseur 🟢 |
| **Documentaires** | Documents d'exportation, reglementations douanières CH et EU, tarifs transporteurs, historique des livraisons |
| **Financières** | 🟡 [RECOMMANDE — définir le budget annuel transport et logistique] |

---

## Indicateurs de performance

| Indicateur | Formule de calcul | Objectif | Frequence | Source de données |
|---|---|---|---|---|
| Respect des délais de livraison | Nombre de livraisons dans les délais / Nombre total de livraisons x 100 | >= 95% 🟢 | Par livraison | Suivi des livraisons FileMaker |
| Precision délai maritime/ferroviaire | Écart entre date de livraison effective et date prévue (transport maritime ou ferroviaire) | +/- 10 jours 🟢 | Par livraison | Suivi des livraisons FileMaker |
| Precision délai aérien | Écart entre date de livraison effective et date prévue (transport aérien) | +/- 3 jours 🟢 | Par livraison | Suivi des livraisons FileMaker |
| Conformité des documents douaniers | Nombre de dossiers douaniers conformes du premier coup / Nombre total de dossiers x 100 | 100% | Par livraison | Dossiers douaniers, FileMaker |
| Taux d'incidents transport | Nombre de livraisons avec incident (perte, dommage, retard majeur) / Nombre total de livraisons x 100 | 🟡 [RECOMMANDE — définir un objectif après 1ere année de référence] | Trimestriel | Suivi des livraisons FileMaker |

---

## Actions d'amélioration planifiées

| # | Action | Description | Échéance | Statut |
|---|---|---|---|---|
| A05 | Comparatif transporteurs | Établir un comparatif des transporteurs utilisés (délais, fiabilité, coût) pour optimiser le choix du mode de transport selon les situations. | T2 2026 | Planifié |
| A06 | Procédure douanière formalisée | Formaliser une check-list des documents douaniers requis par type d'expédition (CH, UE) pour reduire le risque d'erreur. | T2 2026 | Planifié |

---

## Risques et opportunités associés

Voir CTX-QUA-001 pour le détail. Résumé :

| # | Risque / Opportunité | Niveau | Action |
|---|---|---|---|
| R04 | Retards de transport (aléas maritimes, aériens, ferroviaires, conditions meteorologiques, congestionnement portuaire) | Élevé | Anticipation des délais avec marge de sécurité, suivi en temps reel des expéditions, communication proactive avec le client en cas de retard, choix du mode de transport adapte à l\'urgence |
| R05 | Formalités douanières (erreur documentaire, changement réglementaire, blocage en douane) | Faible | Préparation rigoureuse des documents, veille réglementaire, check-list des documents requis, relation avec les autorites douanières |
| O04 | Optimisation des délais de livraison (amélioration continue des circuits logistiques) | Moyen | Comparatif régulier des transporteurs et des modes de transport, consolidation des envois lorsque possible, retour d'expérience sur chaque livraison |

---

## Interfaces avec les autres processus

| Processus en interface | Nature de l'interaction |
|---|---|
| **O1 - Commercial** | Recoit : délais de livraison convenus avec le client, adresse de livraison, conditions particulières. Fournit : confirmation de livraison, date effective, suivi transport |
| **O2 - Achats et Sous-traitance** | Recoit : produits prêts a expédier, documents d'exportation (facture douanière, packing list). Fournit : confirmation de prise en charge par le transporteur |
| **O4 - Contrôle qualité** | Recoit : signalement de NC détectée a reception chez le client. Fournit : information sur l'état des marchandises à la livraison, réclamations liées au transport |
| **S1 - Gestion documentaire** | Fournit : enregistrements (fiches livraison, documents douaniers, confirmations de transport). Recoit : accès aux historiques et données dans FileMaker |
| **M2 - Amélioration continue** | Fournit : données de performance logistique (délais, incidents, conformité douanière). Recoit : objectifs d'amélioration, actions correctives a mettre en œuvre |

---

## Exigences applicables

| Type | Exigence | Référence |
|---|---|---|
| ISO 9001:2015 | Preservation (des éléments de sortie au cours de la production et de la prestation de service) | 8.5.4 |
| ISO 9001:2015 | Activités après livraison | 8.5.5 |
| ISO 9001:2015 | Identification et traçabilité | 8.5.2 |
| ISO 9001:2015 | Propriété des clients ou des prestataires externes | 8.5.3 |
| Réglementaire | Réglementation douanière suisse (importation depuis la Chine) | 🔵 [À VÉRIFIER — références spécifiques] |
| Réglementaire | Réglementation douanière européenne (importation dans l'UE) | 🔵 [À VÉRIFIER — références spécifiques selon pays client] |
| Réglementaire | Reglementations applicables au transport international de marchandises (aérien, maritime, ferroviaire) | 🔵 [À VÉRIFIER — selon les modes de transport utilisés] |
| Client | Délais de livraison, conditions de livraison (Incoterms), adresse et instructions spécifiques | Confirmation de commande client (par projet) |

---

## Particularites du processus

### Modes de transport

| Mode | Usage | Délai typique Chine-Europe | Critère de sélection |
|---|---|---|---|
| **Aérien** | Commandes urgentes, petits volumes, échantillons | 5-10 jours | Urgence élevée, faible volume |
| **Maritime** | Volumes importants, commandes planifiées | 30-45 jours | Volume important, coût optimise |
| **Ferroviaire** | Compromis délai/coût, volumes moyens | 18-25 jours | Délai intermédiaire, bon rapport coût/délai |

### Coordination avec les partenaires chinois

L'organisation du transport impliqué une coordination etroite avec les partenaires chinois (Yuyao Mould Factory et **Oukailuo**) pour la mise à disposition des marchandises au point de depart. La communication se fait principalement par email et WeChat.

### Points d'attention spécifiques

- **Douanes** : les formalités douanières dependent du type de marchandise, du pays de destination et de la valeur déclarée. Une attention particulière est portee à la conformité de chaque dossier.
- **Incoterms** : les conditions de livraison (repartition des responsabilités entre Plus Sarl et le client) sont définies pour chaque commande.
- **Decalage horaire** : la coordination avec la Chine pour l'expédition impliqué un decalage horaire de 6 a 7 heures. WeChat permet des échanges rapides malgre ce decalage.
- **Fiduciaire Paradiso** : la fiduciaire intervient dans la gestion comptable et fiscale des opérations d'import/export.
- **Sauvegarde** : tous les documents logistiques et douaniers sont sauvegardes dans le cloud. 🟢

---

## Historique des revisions

| Version | Date | Modification | Auteur |
|---|---|---|---|
| 0.4 | 18/02/2026 | Création initiale de la fiche processus O3 - Logistique et Livraison. | Roxane Wicky |
