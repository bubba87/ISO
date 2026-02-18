# Procedure Logistique et Livraison

| | |
|---|---|
| **Reference** | PRO-LOG-001 |
| **Version** | 0.4 |
| **Date de creation** | 18/02/2026 |
| **Date de revision** | 18/02/2026 |
| **Redige par** | Roxane Wicky |
| **Approuve par** | Roxane Wicky |

> **Legende :** :red_circle: [A REMPLIR] = obligatoire, manquant | :yellow_circle: [RECOMMANDE] = recommande | :green_circle: = deja rempli | :blue_circle: [A VERIFIER] = a confirmer

---

## 1. Objet

Definir les regles d'organisation, de suivi et de maitrise de la logistique internationale et des livraisons, depuis la notification de produits prets par le partenaire chinois jusqu'a la confirmation de reception par le client europeen, en passant par la creation des documents douaniers conformes a la legislation europeenne et suisse.

> **Cette procedure est essentielle pour Plus Sarl.** La coordination logistique entre la Chine et l'Europe
> constitue un maillon critique de la chaine de valeur. La maitrise des delais, du transport et des
> formalites douanieres impacte directement la satisfaction des clients et sera examinee par l'auditeur
> de certification (SQS).

## 2. Domaine d'application

Toutes les expeditions de produits depuis la Chine vers les clients europeens de Plus Sarl (~10 clients actifs, 50-100 expeditions par an) :
- Expeditions de pieces plastiques injectees (depuis Yuyao Mould Factory)
- Expeditions de vis (depuis Whang, Yuyao)
- Expeditions combinees ou multi-references
- Tous les modes de transport : aerien, maritime, ferroviaire
- Gestion des documents douaniers associes

## 3. Responsabilites

| Responsabilite | Qui |
|---|---|
| Creation de la fiche de livraison dans FileMaker | :green_circle: Roxane Wicky, gerante |
| Choix du mode de transport | :green_circle: Roxane Wicky, gerante |
| Selection et contact du transporteur | :green_circle: Roxane Wicky, gerante |
| Preparation des documents douaniers | :green_circle: Roxane Wicky, gerante |
| Suivi d'expedition et tracking | :green_circle: Roxane Wicky, gerante |
| Gestion des formalites douanieres (EU et CH) | :green_circle: Roxane Wicky, gerante |
| Confirmation de livraison aupres du client | :green_circle: Roxane Wicky, gerante |
| Cloture de la fiche livraison dans FileMaker | :green_circle: Roxane Wicky, gerante |

## 4. Modes de transport

Le choix du mode de transport est determine par l'urgence de la livraison et le volume des marchandises :

| Mode | Usage | Delai indicatif Chine-Europe | Tolerance | Criteres de choix |
|---|---|---|---|---|
| **Aerien** | Urgent, petits volumes | :green_circle: 5-10 jours | :green_circle: +/- 3 jours | Urgence client, echantillons, petites series |
| **Maritime** | Standard, grands volumes | :green_circle: 30-45 jours | :green_circle: +/- 10 jours | Volumes importants, cout optimise, delai non critique |
| **Ferroviaire** | Intermediaire | :green_circle: 15-25 jours | :green_circle: +/- 7 jours | Compromis entre delai et cout, volumes moyens |

> **Note :** Le mode de transport est choisi au cas par cas en fonction des exigences du client
> (delai, cout) et du volume de la commande. Le transport maritime est privilegie quand le delai
> le permet afin d'optimiser les couts.

### 4.1 Transporteurs et transitaires

| Element | Detail |
|---|---|
| **Modes disponibles** | :green_circle: Aerien, maritime, ferroviaire |
| **Criteres de selection** | :green_circle: Fiabilite, respect des delais, couverture geographique, cout |
| **Noms des transporteurs** | :yellow_circle: [RECOMMANDE -- il est recommande de documenter les noms des transporteurs et transitaires utilises pour assurer la tracabilite et l'evaluation] |

## 5. Procedure de livraison

### 5.1 Logigramme

```
    Notification produits prets
    (depuis processus O2)
            |
            v
    +---------------------------+
    | 1. Recevoir la            |---> Le partenaire chinois notifie
    |    notification produits  |     que les produits sont prets
    |    prets                  |     a l'expedition (email/WeChat)
    +---------------------------+
            |
            v
    +---------------------------+
    | 2. Creer la fiche         |---> Enregistrement dans FileMaker :
    |    livraison dans         |     references, quantites, client,
    |    FileMaker              |     delai souhaite
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
    |    contacter le           |     Demande de devis si necessaire
    |    transporteur           |     Confirmation de la reservation
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
    | 6. Verifier la conformite |---> Conformite a la legislation
    |    des documents          |     europeenne (UE) et suisse (CH)
    |    douaniers              |     Coherence avec la commande client
    +---------------------------+
            |
            v
    +---------------------------+
    | 7. Lancer l'expedition    |---> Remise des marchandises et
    |                           |     documents au transporteur
    +---------------------------+
            |
            v
    +---------------------------+
    | 8. Suivre l'expedition    |---> Tracking en ligne
    |                           |     Contact transporteur si besoin
    |                           |     Mise a jour FileMaker
    +---------------------------+
            |
            v
    +---------------------------+
    | 9. Gerer le dedouanement  |---> Suivi des formalites douanieres
    |                           |     a l'import (EU/CH)
    |                           |     Resolution des blocages
    +---------------------------+
            |
            v
    +---------------------------+
    | 10. Confirmer la          |---> Contact client pour confirmation
    |     livraison au client   |     de bonne reception
    +---------------------------+
            |
            v
       Probleme signale ?
       /                \
     NON                OUI
      |                   |
      v                   v
    +---------------------------+
    | 11. Cloturer la fiche     |   PRO-NCF-001
    |     dans FileMaker        |   (non-conformite)
    +---------------------------+
```

### 5.2 Detail des etapes

| # | Etape | Description | Outil | Sortie |
|---|---|---|---|---|
| 1 | Reception notification produits prets | Le partenaire chinois informe que les produits sont prets a l'expedition apres CQ pre-expedition (cf. PRO-ACH-001, section 8) | Email / WeChat | Notification recue |
| 2 | Creation fiche livraison | Enregistrement de toutes les informations de livraison dans FileMaker (references, quantites, client, delai) | FileMaker | Fiche livraison creee |
| 3 | Choix du mode de transport | Selection du mode de transport (aerien, maritime, ferroviaire) en fonction de l'urgence, du volume et des exigences client | -- | Mode de transport defini |
| 4 | Selection transporteur | Contact du transporteur ou transitaire, demande de devis si necessaire, confirmation de reservation | Email | Reservation confirmee |
| 5 | Preparation documents douaniers | Creation de la facture douaniere, du certificat d'origine, de la packing list et de tout autre document requis | FileMaker / Email | Documents douaniers prets |
| 6 | Verification conformite documents | Verification de la coherence des documents avec la commande client et la legislation douaniere EU et CH | -- | Documents valides |
| 7 | Lancement expedition | Remise des marchandises et des documents au transporteur | -- | Expedition lancee |
| 8 | Suivi expedition | Suivi du transport via tracking en ligne, contact transporteur si necessaire, mise a jour du statut dans FileMaker | FileMaker / Email | Statut a jour |
| 9 | Gestion dedouanement | Suivi des formalites douanieres a l'import, resolution des eventuels blocages | Email | Dedouanement effectue |
| 10 | Confirmation livraison client | Contact avec le client pour confirmer la bonne reception des marchandises | Email | Confirmation recue |
| 11 | Cloture dans FileMaker | Cloture de la fiche livraison, archivage des documents associes | FileMaker | Fiche cloturee |

## 6. Documents douaniers

Les documents suivants sont requis pour chaque expedition :

| Document | Description | Obligatoire | Responsable |
|---|---|---|---|
| **Facture douaniere** | Facture commerciale detaillant les marchandises, quantites, valeurs, incoterms | Oui | :green_circle: Roxane Wicky |
| **Certificat d'origine** | Document attestant l'origine des marchandises (Chine) | Oui | :green_circle: Roxane Wicky / Partenaire chinois |
| **Packing list** | Liste de colisage detaillant le contenu de chaque colis (poids, dimensions, references) | Oui | :green_circle: Roxane Wicky / Partenaire chinois |
| **Bon de livraison** | Document accompagnant les marchandises pour le client | Oui | :green_circle: Roxane Wicky |
| **Documents de transport** | AWB (aerien), B/L (maritime), CIM/SMGS (ferroviaire) | Oui | :green_circle: Transporteur |
| **Declaration en douane** | Declaration d'importation pour la Suisse ou l'UE | Oui | :green_circle: Transitaire / Roxane Wicky |
| **Certificats specifiques** | Certificats de conformite, rapports de test, si requis par le client ou la reglementation | Selon commande | :blue_circle: [A VERIFIER -- au cas par cas selon les exigences client et reglementaires] |

> **Note :** Les documents douaniers doivent etre conformes a la fois a la legislation europeenne
> (pour les livraisons directes aux clients UE) et a la legislation suisse (pour les expeditions
> transitant par la Suisse). La coherence entre les documents douaniers et les commandes clients
> est verifiee systematiquement avant chaque expedition.

## 7. Indicateurs de performance

| Indicateur | Objectif | Statut | Methode de mesure |
|---|---|---|---|
| Taux de livraisons dans les delais | >= 95% | :green_circle: | Comparaison delai annonce vs. delai reel dans FileMaker |
| Respect tolerance transport maritime/ferroviaire | +/- 10 jours | :green_circle: | Suivi des ecarts dans FileMaker |
| Respect tolerance transport aerien | +/- 3 jours | :green_circle: | Suivi des ecarts dans FileMaker |
| Taux d'erreurs documents douaniers | < 5% | :green_circle: | Nombre de rejets ou corrections par rapport au nombre total d'expeditions |
| Reclamations clients liees a la livraison | 0 reclamation majeure par an | :green_circle: | Suivi des reclamations dans FileMaker |

> **Frequence de revue :** Les indicateurs sont revus lors de la revue de direction annuelle
> et en continu par la gerante dans le cadre du suivi operationnel quotidien.

## 8. Risques et actions

| Risque | Impact | Probabilite | Action preventive | Action corrective |
|---|---|---|---|---|
| Retard de transport (intemperies, congestion portuaire, perturbations logistiques) | Livraison en retard chez le client | Moyenne | Integrer des marges de securite dans les delais annonces au client ; diversifier les modes de transport | Informer le client immediatement ; rechercher une solution alternative (changement de mode de transport) |
| Blocage en douane (documents incomplets ou non conformes) | Retard de livraison, couts supplementaires | Faible | Verifier systematiquement la conformite des documents avant expedition (etape 6) ; se tenir informe des evolutions reglementaires | Corriger les documents et les soumettre a nouveau ; contacter le transitaire pour debloquer la situation |
| Perte ou dommage de marchandises pendant le transport | Perte financiere, insatisfaction client | Faible | Selectionner des transporteurs fiables ; verifier l'emballage avant expedition | Declarer le sinistre au transporteur ; organiser un remplacement si possible ; enregistrer une NC (PRO-NCF-001) |
| Erreur dans les documents douaniers (montants, references, quantites) | Blocage en douane, penalites | Faible | Double verification des documents avant envoi (etape 6) | Corriger immediatement ; informer le transitaire et le client |
| Changement de reglementation douaniere (EU ou CH) | Non-conformite des documents | Faible | Veille reglementaire ; contact regulier avec le transitaire | Adapter les documents et les processus ; former si necessaire |

## 9. Interfaces avec les autres processus

| Processus | Interface | Description |
|---|---|---|
| **O1 -- Relation client** | Entree / Sortie | Reception des exigences client (delais, adresse, incoterms) ; confirmation de livraison au client ; traitement des reclamations liees a la livraison |
| **O2 -- Production et suivi de fabrication** | Entree | Reception de la notification de produits prets a l'expedition apres CQ pre-expedition |
| **O4 -- Facturation** | Sortie | Transmission des informations de livraison pour facturation (references, quantites, date de livraison) |
| **S1 -- Maitrise documentaire** | Support | Archivage des documents douaniers, fiches de livraison et preuves de suivi conformement a PRO-DOC-001 |
| **PRO-ACH-001** | Lien | Les transporteurs et transitaires sont des fournisseurs de classe B evalues selon PRO-ACH-001 |
| **PRO-NCF-001** | Lien | En cas de probleme de livraison (retard majeur, perte, dommage), une non-conformite est enregistree selon PRO-NCF-001 |

---

> **Instructions de remplissage :**
> 1. Enregistrez TOUTES les expeditions dans FileMaker avec les references, les delais, le mode de transport et le statut
> 2. Conservez TOUS les documents douaniers (factures, certificats d'origine, packing lists) -- ce sont des preuves de maitrise du processus
> 3. Conservez les preuves de suivi de transport (tracking, emails transporteur) -- l'auditeur (SQS) voudra les voir
> 4. En cas de retard significatif, informez le client immediatement et documentez l'incident
> 5. Verifiez systematiquement la coherence entre les documents douaniers et les commandes clients avant chaque expedition
> 6. Les tolerances de delai (+/- 3 jours aerien, +/- 10 jours maritime) doivent etre communiquees aux clients lors de la confirmation de commande

---

## Historique des revisions

| Version | Date | Description de la modification | Auteur |
|---|---|---|---|
| 0.4 | 18/02/2026 | Creation initiale. Procedure de logistique et livraison couvrant les modes de transport, les documents douaniers, le suivi d'expedition et les indicateurs de performance. Integration du systeme de legende des champs. | Roxane Wicky |
