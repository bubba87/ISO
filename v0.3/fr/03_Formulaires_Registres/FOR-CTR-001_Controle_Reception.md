# Formulaire de Controle a Reception (adapte)

| | |
|---|---|
| **Reference** | FOR-CTR-001 |
| **Version** | 0.3 |
| **Date** | 12/02/2026 |
| **Societe** | Plus Sarl |

> **Legende :** :red_circle: [A REMPLIR] = obligatoire, manquant | :yellow_circle: [RECOMMANDE] = recommande | :green_circle: = deja rempli | :blue_circle: [A VERIFIER] = a confirmer

| Version | Date | Modification | Auteur |
|---|---|---|---|
| 0.1 | 10/02/2026 | Creation initiale | Roxane Wicky |
| 0.2 | 10/02/2026 | Ajout checklist CQ, fiche controle detaillee, registre, lien NC_2026_1001 | Roxane Wicky |
| 0.3 | 12/02/2026 | Integration des reponses (Whang, Paradiso, SQS, cloud, ~10 clients, echantillonnage CQ). Ajout du systeme de legende des champs. | Roxane Wicky |

---

> **[POINT D'ATTENTION]** : Plus Sarl ne receptionne pas physiquement les produits. Les marchandises
> sont expediees directement de Chine vers les clients europeens. Le controle se fait via la
> confirmation client et l'absence de reclamation. Une visite chez les partenaires en Chine est
> planifiee pour mars 2026 pour renforcer le suivi de production (cf. section 8.5 du manuel qualite).

> :green_circle: **CQ pre-expedition (v0.3)** : Le partenaire realisera un CQ avant expedition et enverra un echantillonnage chez Plus Sarl en parallele du transport chez le client. Ce dispositif permet a Plus Sarl de verifier la conformite des produits meme en l'absence de reception physique des lots complets.

---

## Contexte et adaptation

Dans le cadre de l'activite de coordination industrielle de Plus Sarl, les produits fabriques en Chine sont expedies directement aux clients europeens. Plus Sarl n'effectue donc pas de controle physique a reception. Le "controle a reception" est adapte comme suit :

| Controle classique | Adaptation Plus Sarl |
|---|---|
| Inspection physique a la reception | Verification des documents de transport et d'expedition |
| Controle visuel des produits | Suivi de l'expedition (outils en ligne, contact transporteur) |
| Controle dimensionnel | Confirmation de reception par le client |
| Verification sur echantillon | :green_circle: **CQ pre-expedition par le partenaire + echantillonnage envoye chez Plus Sarl en parallele du transport** |
| Decision d'acceptation/refus | Absence de reclamation = conformite implicite (cf. section 8.6 du manuel qualite) |
| Ouverture NC si defaut | Si reclamation client : declenchement du processus NC (PRO-NCF-001) |

---

## Checklist de controle qualite

> **Contexte :** Cette checklist a ete creee suite a l'action corrective issue de la NC_2026_1001
> (erreur d'etiquetage sur la commande SHIP_25058 / CFM00057428 / 90.60.05710, 1000 pieces
> avec mauvaise etiquette). Elle vise a systematiser les verifications cles avant expedition
> ou a reception des documents, afin de prevenir la recurrence de ce type de non-conformite.
>
> **Note :** Cette checklist sera finalisee et validee lors du voyage en Chine en mars 2026,
> en concertation avec les partenaires de fabrication (Yuyao Mould Factory et Whang).
>
> **Mise a jour v0.3 (NC_2026_1001) :** Suivi en cours : oui. Photos non disponibles. Cause pas encore identifiee.

### Points de verification

| # | Point de controle | Conforme | Non conforme | N/A | Commentaire |
|---|---|---|---|---|---|
| 1 | **Etiquetage correct** (reference produit, quantite, numero de lot) | [ ] | [ ] | [ ] | Verifier la correspondance avec le bon de commande |
| 2 | **Correspondance entre l'etiquette et le contenu** | [ ] | [ ] | [ ] | S'assurer que le produit emballe correspond a l'etiquette apposee |
| 3 | **Emballage conforme** (protection, calage) | [ ] | [ ] | [ ] | Verifier que l'emballage protege le produit pour le transport international |
| 4 | **Documents de transport presents et conformes** | [ ] | [ ] | [ ] | Bon de livraison, facture douaniere, certificat d'origine si applicable |
| 5 | **Quantites conformes a la commande** | [ ] | [ ] | [ ] | Comparer les quantites expediees avec le bon de commande |
| 6 | **References produit conformes au bon de commande** | [ ] | [ ] | [ ] | Verifier que les references correspondent exactement au bon de commande |
| 7 | **Verification de l'echantillon recu chez Plus Sarl** | [ ] | [ ] | [ ] | :green_circle: Comparer l'echantillon recu en parallele avec les specifications de la commande. Verifier conformite visuelle, etiquetage, qualite generale |

### Resultat de la checklist

| | |
|---|---|
| **Resultat global** | [ ] CONFORME — tous les points verifies sont conformes |
| | [ ] NON CONFORME — ecart(s) identifie(s), action requise |
| **Si non conforme, action prise** | :red_circle: [A REMPLIR] |
| **NC ouverte ?** | [ ] Oui — Ref : NC-[AAAA]-[NNN] [ ] Non |
| **Verifie par** | :red_circle: [A REMPLIR] |
| **Date** | :red_circle: [A REMPLIR — JJ/MM/AAAA] |

---

## Fiche de Controle a Reception (Suivi de Livraison)

### Identification de la livraison

| Element | Detail |
|---|---|
| **N de controle** | :red_circle: [A REMPLIR — CTR-[AAAA]-[NNN]] |
| **Date d'expedition** | :red_circle: [A REMPLIR — JJ/MM/AAAA] |
| **Date de livraison prevue** | :red_circle: [A REMPLIR — JJ/MM/AAAA] |
| **Date de livraison effective** | :red_circle: [A REMPLIR — JJ/MM/AAAA] |
| **Fournisseur** | [ ] Yuyao Mould Factory [ ] Whang |
| **N de commande Plus Sarl** | :red_circle: [A REMPLIR — Reference FileMaker] |
| **Client final** | :red_circle: [A REMPLIR — Nom du client europeen] |
| **Transporteur** | :red_circle: [A REMPLIR — Nom du transporteur / transitaire] |
| **Mode de transport** | [ ] Aerien [ ] Maritime [ ] Ferroviaire |
| **N de suivi (tracking)** | :red_circle: [A REMPLIR — Numero de suivi du transporteur] |

### Description des produits expedies

| # | Designation | Reference/Plan | Quantite commandee | Quantite expediee | Ecart |
|---|---|---|---|---|---|
| 1 | :red_circle: [A REMPLIR — Description] | :red_circle: [A REMPLIR — Ref plan] | :red_circle: [A REMPLIR — Qte] | :red_circle: [A REMPLIR — Qte] | :red_circle: [A REMPLIR — +/- ou OK] |
| 2 | :red_circle: [A REMPLIR — Description] | :red_circle: [A REMPLIR — Ref plan] | :red_circle: [A REMPLIR — Qte] | :red_circle: [A REMPLIR — Qte] | :red_circle: [A REMPLIR — +/- ou OK] |
| 3 | :red_circle: [A REMPLIR — Description] | :red_circle: [A REMPLIR — Ref plan] | :red_circle: [A REMPLIR — Qte] | :red_circle: [A REMPLIR — Qte] | :red_circle: [A REMPLIR — +/- ou OK] |

---

### Etape 1 : Verification des documents de transport

| Document | Present | Conforme | Commentaire |
|---|---|---|---|
| Facture douaniere | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |
| Bon de livraison | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |
| Documents de douane / export | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |
| Certificat d'origine (si applicable) | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |
| Accuse de reception de commande | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |
| Rapport d'inspection fournisseur (si fourni) | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |

**Resultat verification documentaire :** [ ] Conforme [ ] Documents manquants — relance necessaire

---

### Etape 2 : Suivi de l'expedition

| Element | Detail |
|---|---|
| **Outil de suivi utilise** | [ ] Plateforme en ligne du transporteur [ ] Contact direct avec le transporteur [ ] Autre : :red_circle: [A REMPLIR — preciser] |
| **Expedition en cours selon le planning ?** | [ ] Oui [ ] Non — retard signale |
| **Si retard, cause identifiee** | :red_circle: [A REMPLIR — Description du retard et cause] |
| **Client informe du retard ?** | [ ] Oui [ ] Non [ ] Non applicable (pas de retard) |
| **Date de livraison effective** | :red_circle: [A REMPLIR — JJ/MM/AAAA] |
| **Respect du delai** | [ ] Oui [ ] Non — ecart de :red_circle: [A REMPLIR] jours |

---

### Etape 3 : Verification de l'echantillon (CQ pre-expedition)

> :green_circle: **Nouveau v0.3 :** Le partenaire realisera un CQ avant expedition et enverra un echantillonnage chez Plus Sarl en parallele du transport chez le client.

| Element | Detail |
|---|---|
| **Echantillon recu chez Plus Sarl ?** | [ ] Oui [ ] Non [ ] N/A (pas d'echantillonnage pour cette commande) |
| **Date de reception de l'echantillon** | :red_circle: [A REMPLIR — JJ/MM/AAAA] |
| **Conformite visuelle de l'echantillon** | [ ] Conforme [ ] Non conforme — detail : :red_circle: [A REMPLIR] |
| **Etiquetage de l'echantillon correct** | [ ] Conforme [ ] Non conforme |
| **Qualite generale de l'echantillon** | [ ] Conforme [ ] Non conforme — detail : :red_circle: [A REMPLIR] |
| **Correspondance avec les specifications** | [ ] Conforme [ ] Non conforme |
| **Decision suite a la verification** | [ ] Echantillon conforme — lot valide [ ] Echantillon non conforme — alerte au partenaire et au client |
| **Rapport CQ du partenaire recu ?** | [ ] Oui [ ] Non |

---

### Etape 4 : Confirmation de reception par le client

| Element | Detail |
|---|---|
| **Confirmation de reception recue ?** | [ ] Oui [ ] Non — relance le :red_circle: [A REMPLIR — JJ/MM/AAAA] |
| **Date de confirmation** | :red_circle: [A REMPLIR — JJ/MM/AAAA] |
| **Mode de confirmation** | [ ] Email [ ] Telephone [ ] Autre : :red_circle: [A REMPLIR — preciser] |
| **Commentaires du client** | :red_circle: [A REMPLIR — Observations du client a la reception, le cas echeant] |

---

### Etape 5 : Evaluation de la conformite

| Element | Detail |
|---|---|
| **Reclamation client ?** | [ ] Non — conformite implicite [ ] Oui — reclamation recue |
| **Si reclamation, nature** | [ ] Defaut produit [ ] Quantite incorrecte [ ] Dommage transport [ ] Retard [ ] Autre : :red_circle: [A REMPLIR — preciser] |
| **Description de la reclamation** | :red_circle: [A REMPLIR — Description detaillee] |
| **Fiche NC ouverte ?** | [ ] Oui — Ref : NC-[AAAA]-[NNN] [ ] Non applicable |

> **Rappel :** Conformement a la section 8.6 du manuel qualite, l'absence de reclamation client
> dans un delai raisonnable apres la livraison vaut conformite implicite des produits livres.

---

### Etape 6 : Decision et cloture

| | |
|---|---|
| **Resultat global** | [ ] CONFORME (livraison confirmee, pas de reclamation) |
| | [ ] CONFORME AVEC REMARQUES (livraison confirmee, remarques mineures du client) |
| | [ ] NON CONFORME (reclamation client — NC ouverte) |
| **Decision** | [ ] Livraison validee — commande soldee |
| | [ ] Livraison validee avec points de suivi (remarques a integrer pour prochaines commandes) |
| | [ ] NC ouverte — traitement selon PRO-NCF-001 |
| **Commentaire** | :red_circle: [A REMPLIR — Detail de la decision, points d'attention pour la suite] |

---

### Validation

| | Nom | Date |
|---|---|---|
| **Controle effectue par** | :green_circle: Roxane Wicky | :red_circle: [A REMPLIR — JJ/MM/AAAA] |
| **Decision prise par** | :green_circle: Roxane Wicky | :red_circle: [A REMPLIR — JJ/MM/AAAA] |

---

## Suivi NC_2026_1001

> **Mise a jour v0.3 :** Suivi de la NC_2026_1001 (erreur d'etiquetage sur la commande SHIP_25058 / CFM00057428 / 90.60.05710, 1000 pieces avec mauvaise etiquette).

| Element | Detail |
|---|---|
| **Suivi en cours** | :green_circle: Oui |
| **Photos disponibles** | :red_circle: Non disponibles |
| **Cause identifiee** | :red_circle: Pas encore identifiee |
| **Action corrective** | :green_circle: Checklist de controle qualite mise en place (FOR-CTR-001) |
| **Prochaine etape** | :yellow_circle: [RECOMMANDE — identifier la cause racine lors du voyage en Chine en mars 2026, en concertation avec Yuyao Mould Factory et/ou Whang] |

---

## Registre des Controles a Reception (Suivi des Livraisons)

| N CTR | Date exp. | Date livr. | Fournisseur | Commande | Client | Produit | Delai respecte | Echantillon conforme | Reclamation | NC ? | Statut |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CTR-[AAAA]-001 | :red_circle: [A REMPLIR] | :red_circle: [A REMPLIR] | :red_circle: [A REMPLIR] | :red_circle: [A REMPLIR] | :red_circle: [A REMPLIR] | :red_circle: [A REMPLIR] | :red_circle: [A REMPLIR — O/N] | :red_circle: [A REMPLIR — O/N/N/A] | :red_circle: [A REMPLIR — O/N] | :red_circle: [A REMPLIR — ref NC] | :red_circle: [A REMPLIR — Solde/Ouvert] |
| CTR-[AAAA]-002 | | | | | | | | | | | |
| CTR-[AAAA]-003 | | | | | | | | | | | |

---

> **Instructions de remplissage :**
> 1. Remplissez une fiche pour CHAQUE livraison expediee depuis la Chine vers un client
> 2. Utilisez la **checklist de controle qualite** pour chaque expedition — elle sera obligatoire apres validation lors du voyage en Chine (mars 2026)
> 3. Verifiez les documents de transport des la reception des documents d'export
> 4. Suivez l'acheminement et relancez le transporteur en cas de retard
> 5. **Nouveau v0.3 :** Verifiez l'echantillon recu chez Plus Sarl en parallele de la livraison (CQ pre-expedition par le partenaire)
> 6. Obtenez la confirmation de reception du client (email, telephone)
> 7. En l'absence de reclamation dans un delai raisonnable, la conformite est implicite
> 8. Si le client signale un probleme, ouvrez immediatement une fiche NC (PRO-NCF-001)
> 9. Ces fiches sont des preuves cles pour l'auditeur SQS — elles demontrent le suivi malgre l'absence de reception physique
> 10. La visite planifiee en Chine en mars 2026 permettra de finaliser la checklist de controle qualite et de renforcer le controle qualite en amont avec Yuyao Mould Factory et Whang (cf. section 8.5 du manuel qualite)
> 11. NC_2026_1001 : suivi en cours, photos non disponibles, cause pas encore identifiee — a investiguer lors du voyage en Chine
