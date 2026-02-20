# Formulaire de Contrôle a Reception (adapte)

| | |
|---|---|
| **Référence** | FOR-CTR-001 |
| **Version** | 0.4 |
| **Date** | 18/02/2026 |
| **Société** | Plus Sarl |

> **Légende :** :red_circle: [À REMPLIR] = obligatoire, manquant | :yellow_circle: [RECOMMANDE] = recommandé | :green_circle: = déjà rempli | :blue_circle: [À VÉRIFIER] = a confirmer

| Version | Date | Modification | Auteur |
|---|---|---|---|
| 0.1 | 10/02/2026 | Création initiale | Roxane Wicky |
| 0.2 | 10/02/2026 | Ajout checklist CQ, fiche contrôle détaillée, registre, lien NC_2026_1001 | Roxane Wicky |
| 0.3 | 12/02/2026 | Intégration des réponses (Whang, Paradiso, SQS, cloud, ~10 clients, echantillonnage CQ). Ajout du système de légende des champs. | Roxane Wicky |
| 0.4 | 18/02/2026 | Intégration UPDATE 2.1 Processus 04 : référence au contrôle qualité formalisé (CTX-QUA-001 section 1.1). Fiche de contrôle a formaliser avec YAN. | Roxane Wicky |

---

> **[POINT D'ATTENTION]** : Plus Sarl ne réceptionne pas physiquement les produits. Les marchandises
> sont expédiées directement de Chine vers les clients européens. Le contrôle se fait via la
> confirmation client et l'absence de réclamation. Une visite chez les partenaires en Chine est
> planifiée pour mars 2026 pour renforcer le suivi de production (cf. section 8.5 du manuel qualité).

> :green_circle: **CQ pre-expédition (v0.3)** : Le partenaire realisera un CQ avant expédition et enverra un echantillonnage chez Plus Sarl en parallèle du transport chez le client. Ce dispositif permet a Plus Sarl de vérifier la conformité des produits meme en l'absence de reception physique des lots complets.

---

## Contexte et adaptation

Dans le cadre de l'activité de coordination industrielle de Plus Sarl, les produits fabriques en Chine sont expédiés directement aux clients européens. Plus Sarl n'effectué donc pas de contrôle physique a reception. Le "contrôle a reception" est adapte comme suit :

| Contrôle classique | Adaptation Plus Sarl |
|---|---|
| Inspection physique à la reception | Vérification des documents de transport et d'expédition |
| Contrôle visuel des produits | Suivi de l'expédition (outils en ligne, contact transporteur) |
| Contrôle dimensionnel | Confirmation de reception par le client |
| Vérification sur échantillon | :green_circle: **CQ pre-expédition par le partenaire + echantillonnage envoye chez Plus Sarl en parallèle du transport** |
| Decision d'acceptation/refus | Absence de réclamation = conformité implicite (cf. section 8.6 du manuel qualité) |
| Ouverture NC si defaut | Si réclamation client : declenchement du processus NC (PRO-NCF-001) |

---

## Checklist de contrôle qualité

> **Contexte :** Cette checklist a été créée suite à l\'action corrective issue de la NC_2026_1001
> (erreur d'étiquetage sur la commande SHIP_25058 / CFM00057428 / 90.60.05710, 1000 pièces
> avec mauvaise etiquette). Elle visé à systematiser les vérifications cles avant expédition
> ou a reception des documents, afin de prevenir la recurrence de ce type de non-conformité.
>
> **Note :** Cette checklist sera finalisée et validée lors du voyage en Chine en mars 2026,
> en concertation avec les partenaires de fabrication (Yuyao Mould Factory et Whang).
>
> **Mise à jour v0.3 (NC_2026_1001) :** Suivi en cours : oui. Photos non disponibles. Cause pas encore identifiée.

### Points de vérification

| # | Point de contrôle | Conforme | Non conforme | N/A | Commentaire |
|---|---|---|---|---|---|
| 1 | **Etiquetage correct** (référence produit, quantité, numéro de lot) | [ ] | [ ] | [ ] | Vérifier la correspondance avec le bon de commande |
| 2 | **Correspondance entre l'etiquette et le contenu** | [ ] | [ ] | [ ] | S'assurer que le produit emballe correspond à l\'etiquette apposee |
| 3 | **Emballage conforme** (protection, calage) | [ ] | [ ] | [ ] | Vérifier que l'emballage protégé le produit pour le transport international |
| 4 | **Documents de transport présents et conformes** | [ ] | [ ] | [ ] | Bon de livraison, facture douanière, certificat d'origine si applicable |
| 5 | **Quantités conformes à la commande** | [ ] | [ ] | [ ] | Comparer les quantités expédiées avec le bon de commande |
| 6 | **Références produit conformes au bon de commande** | [ ] | [ ] | [ ] | Vérifier que les références correspondent exactement au bon de commande |
| 7 | **Vérification de l'échantillon reçu chez Plus Sarl** | [ ] | [ ] | [ ] | :green_circle: Comparer l'échantillon reçu en parallèle avec les spécifications de la commande. Vérifier conformité visuelle, étiquetage, qualité générale |

### Résultat de la checklist

| | |
|---|---|
| **Résultat global** | [ ] CONFORME — tous les points vérifiés sont conformes |
| | [ ] NON CONFORME — écart(s) identifié(s), action requise |
| **Si non conforme, action prise** | :red_circle: [À REMPLIR] |
| **NC ouverte ?** | [ ] Oui — Ref : NC-[AAAA]-[NNN] [ ] Non |
| **Vérifié par** | :red_circle: [À REMPLIR] |
| **Date** | :red_circle: [À REMPLIR — JJ/MM/AAAA] |

---

## Fiche de Contrôle a Reception (Suivi de Livraison)

### Identification de la livraison

| Élément | Détail |
|---|---|
| **N de contrôle** | :red_circle: [À REMPLIR — CTR-[AAAA]-[NNN]] |
| **Date d'expédition** | :red_circle: [À REMPLIR — JJ/MM/AAAA] |
| **Date de livraison prévue** | :red_circle: [À REMPLIR — JJ/MM/AAAA] |
| **Date de livraison effective** | :red_circle: [À REMPLIR — JJ/MM/AAAA] |
| **Fournisseur** | [ ] Yuyao Mould Factory [ ] Whang |
| **N de commande Plus Sarl** | :red_circle: [À REMPLIR — Référence FileMaker] |
| **Client final** | :red_circle: [À REMPLIR — Nom du client européen] |
| **Transporteur** | :red_circle: [À REMPLIR — Nom du transporteur / transitaire] |
| **Mode de transport** | [ ] Aérien [ ] Maritime [ ] Ferroviaire |
| **N de suivi (tracking)** | :red_circle: [À REMPLIR — Numéro de suivi du transporteur] |

### Description des produits expédiés

| # | Designation | Référence/Plan | Quantité commandee | Quantité expédiée | Écart |
|---|---|---|---|---|---|
| 1 | :red_circle: [À REMPLIR — Description] | :red_circle: [À REMPLIR — Ref plan] | :red_circle: [À REMPLIR — Qte] | :red_circle: [À REMPLIR — Qte] | :red_circle: [À REMPLIR — +/- ou OK] |
| 2 | :red_circle: [À REMPLIR — Description] | :red_circle: [À REMPLIR — Ref plan] | :red_circle: [À REMPLIR — Qte] | :red_circle: [À REMPLIR — Qte] | :red_circle: [À REMPLIR — +/- ou OK] |
| 3 | :red_circle: [À REMPLIR — Description] | :red_circle: [À REMPLIR — Ref plan] | :red_circle: [À REMPLIR — Qte] | :red_circle: [À REMPLIR — Qte] | :red_circle: [À REMPLIR — +/- ou OK] |

---

### Étape 1 : Vérification des documents de transport

| Document | Présent | Conforme | Commentaire |
|---|---|---|---|
| Facture douanière | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |
| Bon de livraison | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |
| Documents de douane / export | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |
| Certificat d'origine (si applicable) | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |
| Accusé de reception de commande | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |
| Rapport d'inspection fournisseur (si fourni) | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |

**Résultat vérification documentaire :** [ ] Conforme [ ] Documents manquants — relance nécessaire

---

### Étape 2 : Suivi de l'expédition

| Élément | Détail |
|---|---|
| **Outil de suivi utilisé** | [ ] Plateforme en ligne du transporteur [ ] Contact direct avec le transporteur [ ] Autre : :red_circle: [À REMPLIR — preciser] |
| **Expédition en cours selon le planning ?** | [ ] Oui [ ] Non — retard signalé |
| **Si retard, cause identifiée** | :red_circle: [À REMPLIR — Description du retard et cause] |
| **Client informe du retard ?** | [ ] Oui [ ] Non [ ] Non applicable (pas de retard) |
| **Date de livraison effective** | :red_circle: [À REMPLIR — JJ/MM/AAAA] |
| **Respect du délai** | [ ] Oui [ ] Non — écart de :red_circle: [À REMPLIR] jours |

---

### Étape 3 : Vérification de l'échantillon (CQ pre-expédition)

> :green_circle: **Nouveau v0.3 :** Le partenaire realisera un CQ avant expédition et enverra un echantillonnage chez Plus Sarl en parallèle du transport chez le client.

| Élément | Détail |
|---|---|
| **Échantillon reçu chez Plus Sarl ?** | [ ] Oui [ ] Non [ ] N/A (pas d'echantillonnage pour cette commande) |
| **Date de reception de l'échantillon** | :red_circle: [À REMPLIR — JJ/MM/AAAA] |
| **Conformité visuelle de l'échantillon** | [ ] Conforme [ ] Non conforme — détail : :red_circle: [À REMPLIR] |
| **Etiquetage de l'échantillon correct** | [ ] Conforme [ ] Non conforme |
| **Qualité générale de l'échantillon** | [ ] Conforme [ ] Non conforme — détail : :red_circle: [À REMPLIR] |
| **Correspondance avec les spécifications** | [ ] Conforme [ ] Non conforme |
| **Decision suite à la vérification** | [ ] Échantillon conforme — lot valide [ ] Échantillon non conforme — alerte au partenaire et au client |
| **Rapport CQ du partenaire reçu ?** | [ ] Oui [ ] Non |

---

### Étape 4 : Confirmation de reception par le client

| Élément | Détail |
|---|---|
| **Confirmation de reception reçue ?** | [ ] Oui [ ] Non — relance le :red_circle: [À REMPLIR — JJ/MM/AAAA] |
| **Date de confirmation** | :red_circle: [À REMPLIR — JJ/MM/AAAA] |
| **Mode de confirmation** | [ ] Email [ ] Téléphone [ ] Autre : :red_circle: [À REMPLIR — preciser] |
| **Commentaires du client** | :red_circle: [À REMPLIR — Observations du client à la reception, le cas echeant] |

---

### Étape 5 : Évaluation de la conformité

| Élément | Détail |
|---|---|
| **Réclamation client ?** | [ ] Non — conformité implicite [ ] Oui — réclamation reçue |
| **Si réclamation, nature** | [ ] Defaut produit [ ] Quantité incorrecte [ ] Dommage transport [ ] Retard [ ] Autre : :red_circle: [À REMPLIR — preciser] |
| **Description de la réclamation** | :red_circle: [À REMPLIR — Description détaillée] |
| **Fiche NC ouverte ?** | [ ] Oui — Ref : NC-[AAAA]-[NNN] [ ] Non applicable |

> **Rappel :** Conformement à la section 8.6 du manuel qualité, l'absence de réclamation client
> dans un délai raisonnable après la livraison vaut conformité implicite des produits livrés.

---

### Étape 6 : Decision et clôture

| | |
|---|---|
| **Résultat global** | [ ] CONFORME (livraison confirmée, pas de réclamation) |
| | [ ] CONFORME AVEC REMARQUES (livraison confirmée, remarques mineures du client) |
| | [ ] NON CONFORME (réclamation client — NC ouverte) |
| **Decision** | [ ] Livraison validée — commande soldée |
| | [ ] Livraison validée avec points de suivi (remarques a integrer pour prochaines commandes) |
| | [ ] NC ouverte — traitement selon PRO-NCF-001 |
| **Commentaire** | :red_circle: [À REMPLIR — Détail de la decision, points d'attention pour la suite] |

---

### Validation

| | Nom | Date |
|---|---|---|
| **Contrôle effectué par** | :green_circle: Roxane Wicky | :red_circle: [À REMPLIR — JJ/MM/AAAA] |
| **Decision prise par** | :green_circle: Roxane Wicky | :red_circle: [À REMPLIR — JJ/MM/AAAA] |

---

## Suivi NC_2026_1001

> **Mise à jour v0.3 :** Suivi de la NC_2026_1001 (erreur d'étiquetage sur la commande SHIP_25058 / CFM00057428 / 90.60.05710, 1000 pièces avec mauvaise etiquette).

| Élément | Détail |
|---|---|
| **Suivi en cours** | :green_circle: Oui |
| **Photos disponibles** | :red_circle: Non disponibles |
| **Cause identifiée** | :red_circle: Pas encore identifiée |
| **Action corrective** | :green_circle: Checklist de contrôle qualité mise en place (FOR-CTR-001) |
| **Prochaine étape** | :yellow_circle: [RECOMMANDE — identifier la cause racine lors du voyage en Chine en mars 2026, en concertation avec Yuyao Mould Factory et/ou Whang] |

---

## Registre des Contrôles a Reception (Suivi des Livraisons)

| N CTR | Date exp. | Date livr. | Fournisseur | Commande | Client | Produit | Délai respecte | Échantillon conforme | Réclamation | NC ? | Statut |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CTR-[AAAA]-001 | :red_circle: [À REMPLIR] | :red_circle: [À REMPLIR] | :red_circle: [À REMPLIR] | :red_circle: [À REMPLIR] | :red_circle: [À REMPLIR] | :red_circle: [À REMPLIR] | :red_circle: [À REMPLIR — O/N] | :red_circle: [À REMPLIR — O/N/N/A] | :red_circle: [À REMPLIR — O/N] | :red_circle: [À REMPLIR — ref NC] | :red_circle: [À REMPLIR — Solde/Ouvert] |
| CTR-[AAAA]-002 | | | | | | | | | | | |
| CTR-[AAAA]-003 | | | | | | | | | | | |

---

> **Instructions de remplissage :**
> 1. Remplissez une fiche pour CHAQUE livraison expédiée depuis la Chine vers un client
> 2. Utilisez la **checklist de contrôle qualité** pour chaque expédition — elle sera obligatoire après validation lors du voyage en Chine (mars 2026)
> 3. Verifiez les documents de transport des la reception des documents d'export
> 4. Suivez l'acheminement et relancez le transporteur en cas de retard
> 5. **Nouveau v0.3 :** Verifiez l'échantillon reçu chez Plus Sarl en parallèle de la livraison (CQ pre-expédition par le partenaire)
> 6. Obtenez la confirmation de reception du client (email, téléphone)
> 7. En l'absence de réclamation dans un délai raisonnable, la conformité est implicite
> 8. Si le client signalé un problème, ouvrez immédiatement une fiche NC (PRO-NCF-001)
> 9. Ces fiches sont des preuves cles pour l'auditeur SQS — elles demontrent le suivi malgre l'absence de reception physique
> 10. La visite planifiée en Chine en mars 2026 permettra de finaliser la checklist de contrôle qualité et de renforcer le contrôle qualité en amont avec Yuyao Mould Factory et Whang (cf. section 8.5 du manuel qualité)
> 11. NC_2026_1001 : suivi en cours, photos non disponibles, cause pas encore identifiée — a investiguer lors du voyage en Chine
