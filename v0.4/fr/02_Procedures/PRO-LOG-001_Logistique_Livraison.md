# Procédure Logistique et Livraison

| | |
|---|---|
| **Référence** | PRO-LOG-001 |
| **Version** | 0.4 |
| **Date de création** | 18/02/2026 |
| **Date de revision** | 18/02/2026 |
| **Rédigé par** | Roxane Wicky |
| **Approuve par** | Roxane Wicky |

> **Légende :** :red_circle: [À REMPLIR] = obligatoire, manquant | :yellow_circle: [RECOMMANDE] = recommandé | :green_circle: = déjà rempli | :blue_circle: [À VÉRIFIER] = a confirmer

---

## 1. Objet

Définir les règles d'organisation, de suivi et de maîtrise de la logistique internationale et des livraisons, depuis la notification de produits prêts par le partenaire chinois jusqu'a la confirmation de reception par le client européen, en passant par la création des documents douaniers conformes à la législation européenne et suisse.

> **Cette procédure est essentielle pour Plus Sarl.** La coordination logistique entre la Chine et l'Europe
> constitue un maillon critique de la chaîne de valeur. La maîtrise des délais, du transport et des
> formalités douanières impacte directement la satisfaction des clients et sera examinée par l'auditeur
> de certification (SQS).

## 2. Domaine d'application

Toutes les expéditions de produits depuis la Chine vers les clients européens de Plus Sarl (~10 clients actifs, 50-100 expéditions par an) :
- Expeditions de pièces plastiques injectees (depuis Yuyao Mould Factory)
- Expeditions de vis (depuis Whang, Yuyao)
- Expeditions combinees ou multi-références
- Tous les modes de transport : aérien, maritime, ferroviaire
- Gestion des documents douaniers associés

## 3. Responsabilités

| Responsabilité | Qui |
|---|---|
| Création de la fiche de livraison dans FileMaker | :green_circle: Roxane Wicky, gérante |
| Choix du mode de transport | :green_circle: Roxane Wicky, gérante |
| Sélection et contact du transporteur | :green_circle: Roxane Wicky, gérante |
| Préparation des documents douaniers | :green_circle: Roxane Wicky, gérante |
| Suivi d'expédition et tracking | :green_circle: Roxane Wicky, gérante |
| Gestion des formalités douanières (EU et CH) | :green_circle: Roxane Wicky, gérante |
| Confirmation de livraison auprès du client | :green_circle: Roxane Wicky, gérante |
| Clôture de la fiche livraison dans FileMaker | :green_circle: Roxane Wicky, gérante |

## 4. Modes de transport

Le choix du mode de transport est détermine par l'urgence de la livraison et le volume des marchandises :

| Mode | Usage | Délai indicatif Chine-Europe | Tolerance | Critères de choix |
|---|---|---|---|---|
| **Aérien** | Urgent, petits volumes | :green_circle: 5-10 jours | :green_circle: +/- 3 jours | Urgence client, échantillons, petites series |
| **Maritime** | Standard, grands volumes | :green_circle: 30-45 jours | :green_circle: +/- 10 jours | Volumes importants, coût optimise, délai non critique |
| **Ferroviaire** | Intermédiaire | :green_circle: 15-25 jours | :green_circle: +/- 7 jours | Compromis entre délai et coût, volumes moyens |

> **Note :** Le mode de transport est choisi au cas par cas en fonction des exigences du client
> (délai, coût) et du volume de la commande. Le transport maritime est privilegie quand le délai
> le permet afin d'optimiser les coûts.

### 4.1 Transporteurs et transitaires

| Élément | Détail |
|---|---|
| **Modes disponibles** | :green_circle: Aérien, maritime, ferroviaire |
| **Critères de sélection** | :green_circle: Fiabilité, respect des délais, couverture géographique, coût |
| **Noms des transporteurs** | :yellow_circle: [RECOMMANDE -- il est recommandé de documenter les noms des transporteurs et transitaires utilisés pour assurer la traçabilité et l'évaluation] |

## 5. Procédure de livraison

### 5.1 Logigramme

```
    Notification produits prêts
    (depuis processus O2)
            |
            v
    +---------------------------+
    | 1. Recevoir la            |---> Le partenaire chinois notifie
    |    notification produits  |     que les produits sont prêts
    |    prêts                  |     à l\'expédition (email/WeChat)
    +---------------------------+
            |
            v
    +---------------------------+
    | 2. Créer la fiche         |---> Enregistrement dans FileMaker :
    |    livraison dans         |     references, quantités, client,
    |    FileMaker              |     délai souhaité
    +---------------------------+
            |
            v
    +---------------------------+
    | 3. Choisir le mode de     |---> Aerien / Maritime / Ferroviaire
    |    transport              |     selon urgence, volume et
    |                           |     exigences client
    +---------------------------+
            |
            v
    +---------------------------+
    | 4. Selectionner et        |---> Contact transporteur/transitaire
    |    contacter le           |     Demande de devis si nécessaire
    |    transporteur           |     Confirmation de la réservation
    +---------------------------+
            |
            v
    +---------------------------+
    | 5. Preparer les documents |---> Facture douaniere
    |    douaniers              |     Certificat d'origine
    |                           |     Packing list
    |                           |     Autres documents requis
    +---------------------------+
            |
            v
    +---------------------------+
    | 6. Verifier la conformité |---> Conformite à la législation
    |    des documents          |     europeenne (UE) et suisse (CH)
    |    douaniers              |     Coherence avec la commande client
    +---------------------------+
            |
            v
    +---------------------------+
    | 7. Lancer l'expédition    |---> Remise des marchandises et
    |                           |     documents au transporteur
    +---------------------------+
            |
            v
    +---------------------------+
    | 8. Suivre l'expédition    |---> Tracking en ligne
    |                           |     Contact transporteur si besoin
    |                           |     Mise à jour FileMaker
    +---------------------------+
            |
            v
    +---------------------------+
    | 9. Gérer le dédouanement  |---> Suivi des formalités douanières
    |                           |     à l\'import (EU/CH)
    |                           |     Résolution des blocages
    +---------------------------+
            |
            v
    +---------------------------+
    | 10. Confirmer la          |---> Contact client pour confirmation
    |     livraison au client   |     de bonne réception
    +---------------------------+
            |
            v
       Problème signalé ?
       /                \
     NON                OUI
      |                   |
      v                   v
    +---------------------------+
    | 11. Clôturer la fiche     |   PRO-NCF-001
    |     dans FileMaker        |   (non-conformité)
    +---------------------------+
```

### 5.2 Détail des étapes

| # | Étape | Description | Outil | Sortie |
|---|---|---|---|---|
| 1 | Reception notification produits prêts | Le partenaire chinois informe que les produits sont prêts à l\'expédition après CQ pre-expédition (cf. PRO-ACH-001, section 8) | Email / WeChat | Notification reçue |
| 2 | Création fiche livraison | Enregistrement de toutes les informations de livraison dans FileMaker (références, quantités, client, délai) | FileMaker | Fiche livraison créée |
| 3 | Choix du mode de transport | Sélection du mode de transport (aérien, maritime, ferroviaire) en fonction de l'urgence, du volume et des exigences client | -- | Mode de transport défini |
| 4 | Sélection transporteur | Contact du transporteur ou transitaire, demande de devis si nécessaire, confirmation de réservation | Email | Réservation confirmée |
| 5 | Préparation documents douaniers | Création de la facture douanière, du certificat d'origine, de la packing list et de tout autre document requis | FileMaker / Email | Documents douaniers prêts |
| 6 | Vérification conformité documents | Vérification de la cohérence des documents avec la commande client et la législation douanière EU et CH | -- | Documents valides |
| 7 | Lancement expédition | Remise des marchandises et des documents au transporteur | -- | Expédition lancée |
| 8 | Suivi expédition | Suivi du transport via tracking en ligne, contact transporteur si nécessaire, mise à jour du statut dans FileMaker | FileMaker / Email | Statut a jour |
| 9 | Gestion dédouanement | Suivi des formalités douanières à l\'import, résolution des éventuels blocages | Email | Dédouanement effectué |
| 10 | Confirmation livraison client | Contact avec le client pour confirmer la bonne reception des marchandises | Email | Confirmation reçue |
| 11 | Clôture dans FileMaker | Clôture de la fiche livraison, archivage des documents associés | FileMaker | Fiche clôturée |

## 6. Documents douaniers

Les documents suivants sont requis pour chaque expédition :

| Document | Description | Obligatoire | Responsable |
|---|---|---|---|
| **Facture douanière** | Facture commerciale détaillant les marchandises, quantités, valeurs, incoterms | Oui | :green_circle: Roxane Wicky |
| **Certificat d'origine** | Document attestant l'origine des marchandises (Chine) | Oui | :green_circle: Roxane Wicky / Partenaire chinois |
| **Packing list** | Liste de colisage détaillant le contenu de chaque colis (poids, dimensions, références) | Oui | :green_circle: Roxane Wicky / Partenaire chinois |
| **Bon de livraison** | Document accompagnant les marchandises pour le client | Oui | :green_circle: Roxane Wicky |
| **Documents de transport** | AWB (aérien), B/L (maritime), CIM/SMGS (ferroviaire) | Oui | :green_circle: Transporteur |
| **Déclaration en douane** | Déclaration d'importation pour la Suisse ou l'UE | Oui | :green_circle: Transitaire / Roxane Wicky |
| **Certificats spécifiques** | Certificats de conformité, rapports de test, si requis par le client ou la réglementation | Selon commande | :blue_circle: [À VÉRIFIER -- au cas par cas selon les exigences client et réglementaires] |

> **Note :** Les documents douaniers doivent être conformes à la fois à la législation européenne
> (pour les livraisons directes aux clients UE) et à la législation suisse (pour les expéditions
> transitant par la Suisse). La cohérence entre les documents douaniers et les commandes clients
> est vérifiée systématiquement avant chaque expédition.

## 7. Indicateurs de performance

| Indicateur | Objectif | Statut | Méthode de mesure |
|---|---|---|---|
| Taux de livraisons dans les délais | >= 95% | :green_circle: | Comparaison délai annonce vs. délai reel dans FileMaker |
| Respect tolérance transport maritime/ferroviaire | +/- 10 jours | :green_circle: | Suivi des écarts dans FileMaker |
| Respect tolérance transport aérien | +/- 3 jours | :green_circle: | Suivi des écarts dans FileMaker |
| Taux d'erreurs documents douaniers | < 5% | :green_circle: | Nombre de rejets ou corrections par rapport au nombre total d'expéditions |
| Réclamations clients liées à la livraison | 0 réclamation majeure par an | :green_circle: | Suivi des réclamations dans FileMaker |

> **Frequence de revue :** Les indicateurs sont revus lors de la revue de direction annuelle
> et en continu par la gérante dans le cadre du suivi opérationnel quotidien.

## 8. Risques et actions

| Risque | Impact | Probabilite | Action preventive | Action corrective |
|---|---|---|---|---|
| Retard de transport (intemperies, congestion portuaire, perturbations logistiques) | Livraison en retard chez le client | Moyenne | Integrer des marges de sécurité dans les délais annoncés au client ; diversifier les modes de transport | Informer le client immédiatement ; rechercher une solution alternative (changement de mode de transport) |
| Blocage en douane (documents incomplets ou non conformes) | Retard de livraison, coûts supplementaires | Faible | Vérifier systématiquement la conformité des documents avant expédition (étape 6) ; se tenir informe des évolutions réglementaires | Corriger les documents et les soumettre a nouveau ; contacter le transitaire pour debloquer la situation |
| Perte ou dommage de marchandises pendant le transport | Perte financière, insatisfaction client | Faible | Selectionner des transporteurs fiables ; vérifier l'emballage avant expédition | Declarer le sinistre au transporteur ; organiser un remplacement si possible ; enregistrer une NC (PRO-NCF-001) |
| Erreur dans les documents douaniers (montants, références, quantités) | Blocage en douane, pénalités | Faible | Double vérification des documents avant envoi (étape 6) | Corriger immédiatement ; informer le transitaire et le client |
| Changement de réglementation douanière (EU ou CH) | Non-conformité des documents | Faible | Veille réglementaire ; contact régulier avec le transitaire | Adapter les documents et les processus ; former si nécessaire |

## 9. Interfaces avec les autres processus

| Processus | Interface | Description |
|---|---|---|
| **O1 -- Relation client** | Entrée / Sortie | Reception des exigences client (délais, adresse, incoterms) ; confirmation de livraison au client ; traitement des réclamations liées à la livraison |
| **O2 -- Production et suivi de fabrication** | Entrée | Reception de la notification de produits prêts à l\'expédition après CQ pre-expédition |
| **O4 -- Facturation** | Sortie | Transmission des informations de livraison pour facturation (références, quantités, date de livraison) |
| **S1 -- Maîtrise documentaire** | Support | Archivage des documents douaniers, fiches de livraison et preuves de suivi conformément a PRO-DOC-001 |
| **PRO-ACH-001** | Lien | Les transporteurs et transitaires sont des fournisseurs de classe B évalués selon PRO-ACH-001 |
| **PRO-NCF-001** | Lien | En cas de problème de livraison (retard majeur, perte, dommage), une non-conformité est enregistrée selon PRO-NCF-001 |

---

> **Instructions de remplissage :**
> 1. Enregistrez TOUTES les expéditions dans FileMaker avec les références, les délais, le mode de transport et le statut
> 2. Conservez TOUS les documents douaniers (factures, certificats d'origine, packing lists) -- ce sont des preuves de maîtrise du processus
> 3. Conservez les preuves de suivi de transport (tracking, emails transporteur) -- l'auditeur (SQS) voudra les voir
> 4. En cas de retard significatif, informez le client immédiatement et documentez l'incident
> 5. Verifiez systématiquement la cohérence entre les documents douaniers et les commandes clients avant chaque expédition
> 6. Les tolérances de délai (+/- 3 jours aérien, +/- 10 jours maritime) doivent être communiquees aux clients lors de la confirmation de commande

---

## Historique des revisions

| Version | Date | Description de la modification | Auteur |
|---|---|---|---|
| 0.4 | 18/02/2026 | Création initiale. Procédure de logistique et livraison couvrant les modes de transport, les documents douaniers, le suivi d'expédition et les indicateurs de performance. Intégration du système de légende des champs. | Roxane Wicky |
