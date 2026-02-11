# Formulaire de Controle a Reception (adapte)

| | |
|---|---|
| **Reference** | FOR-CTR-001 |
| **Version** | 0.1 |
| **Date** | 10/02/2026 |

---

> **[POINT D'ATTENTION]** : Plus Sarl ne receptionne pas physiquement les produits. Les marchandises
> sont expediees directement de Chine vers les clients europeens. Le controle se fait via la
> confirmation client et l'absence de reclamation. Une visite chez les partenaires en Chine est
> planifiee pour renforcer le suivi de production (cf. section 8.5 du manuel qualite).

---

## Contexte et adaptation

Dans le cadre de l'activite de coordination industrielle de Plus Sarl, les produits fabriques en Chine sont expedies directement aux clients europeens. Plus Sarl n'effectue donc pas de controle physique a reception. Le "controle a reception" est adapte comme suit :

| Controle classique | Adaptation Plus Sarl |
|---|---|
| Inspection physique a la reception | Verification des documents de transport et d'expedition |
| Controle visuel des produits | Suivi de l'expedition (outils en ligne, contact transporteur) |
| Controle dimensionnel | Confirmation de reception par le client |
| Decision d'acceptation/refus | Absence de reclamation = conformite implicite (cf. section 8.6 du manuel qualite) |
| Ouverture NC si defaut | Si reclamation client : declenchement du processus NC (PRO-NCF-001) |

---

## Fiche de Controle a Reception (Suivi de Livraison)

### Identification de la livraison

| Element | Detail |
|---|---|
| **N. de controle** | CTR-[AAAA]-[NNN] |
| **Date d'expedition** | [JJ/MM/AAAA] |
| **Date de livraison prevue** | [JJ/MM/AAAA] |
| **Date de livraison effective** | [JJ/MM/AAAA] |
| **Fournisseur** | [ ] Yuyao Mould Factory [ ] Second partenaire [nom A CONFIRMER] |
| **N. de commande Plus Sarl** | [Reference FileMaker] |
| **Client final** | [Nom du client europeen] |
| **Transporteur** | [Nom du transporteur / transitaire] |
| **Mode de transport** | [ ] Aerien [ ] Maritime [ ] Ferroviaire |
| **N. de suivi (tracking)** | [Numero de suivi du transporteur] |

### Description des produits expedies

| # | Designation | Reference/Plan | Quantite commandee | Quantite expediee | Ecart |
|---|---|---|---|---|---|
| 1 | [Description] | [Ref plan] | [Qte] | [Qte] | [+/- ou OK] |
| 2 | [Description] | [Ref plan] | [Qte] | [Qte] | [+/- ou OK] |
| 3 | [Description] | [Ref plan] | [Qte] | [Qte] | [+/- ou OK] |

---

### Etape 1 : Verification des documents de transport

| Document | Present | Conforme | Commentaire |
|---|---|---|---|
| Facture douaniere | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |
| Bon de livraison | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |
| Documents de douane / export | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |
| Certificat d'origine (si applicable) | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |
| Accusé de reception de commande | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |
| Rapport d'inspection fournisseur (si fourni) | [ ] Oui [ ] Non | [ ] Oui [ ] Non | |

**Resultat verification documentaire :** [ ] Conforme [ ] Documents manquants -- relance necessaire

---

### Etape 2 : Suivi de l'expedition

| Element | Detail |
|---|---|
| **Outil de suivi utilise** | [ ] Plateforme en ligne du transporteur [ ] Contact direct avec le transporteur [ ] Autre : [preciser] |
| **Expedition en cours selon le planning ?** | [ ] Oui [ ] Non -- retard signale |
| **Si retard, cause identifiee** | [Description du retard et cause] |
| **Client informe du retard ?** | [ ] Oui [ ] Non [ ] Non applicable (pas de retard) |
| **Date de livraison effective** | [JJ/MM/AAAA] |
| **Respect du delai** | [ ] Oui [ ] Non -- ecart de [___] jours |

---

### Etape 3 : Confirmation de reception par le client

| Element | Detail |
|---|---|
| **Confirmation de reception recue ?** | [ ] Oui [ ] Non -- relance le [JJ/MM/AAAA] |
| **Date de confirmation** | [JJ/MM/AAAA] |
| **Mode de confirmation** | [ ] Email [ ] Telephone [ ] Autre : [preciser] |
| **Commentaires du client** | [Observations du client a la reception, le cas echeant] |

---

### Etape 4 : Evaluation de la conformite

| Element | Detail |
|---|---|
| **Reclamation client ?** | [ ] Non -- conformite implicite [ ] Oui -- reclamation recue |
| **Si reclamation, nature** | [ ] Defaut produit [ ] Quantite incorrecte [ ] Dommage transport [ ] Retard [ ] Autre : [preciser] |
| **Description de la reclamation** | [Description detaillee] |
| **Fiche NC ouverte ?** | [ ] Oui -- Ref : NC-[AAAA]-[NNN] [ ] Non applicable |

> **Rappel :** Conformement a la section 8.6 du manuel qualite, l'absence de reclamation client
> dans un delai raisonnable apres la livraison vaut conformite implicite des produits livres.

---

### Etape 5 : Decision et cloture

| | |
|---|---|
| **Resultat global** | [ ] CONFORME (livraison confirmee, pas de reclamation) |
| | [ ] CONFORME AVEC REMARQUES (livraison confirmee, remarques mineures du client) |
| | [ ] NON CONFORME (reclamation client -- NC ouverte) |
| **Decision** | [ ] Livraison validee -- commande soldee |
| | [ ] Livraison validee avec points de suivi (remarques a integrer pour prochaines commandes) |
| | [ ] NC ouverte -- traitement selon PRO-NCF-001 |
| **Commentaire** | [Detail de la decision, points d'attention pour la suite] |

---

### Validation

| | Nom | Date |
|---|---|---|
| **Controle effectue par** | Roxane Wicky | [JJ/MM/AAAA] |
| **Decision prise par** | Roxane Wicky | [JJ/MM/AAAA] |

---

## Registre des Controles a Reception (Suivi des Livraisons)

| N. CTR | Date exp. | Date livr. | Fournisseur | Commande | Client | Produit | Delai respecte | Reclamation | NC ? | Statut |
|---|---|---|---|---|---|---|---|---|---|---|
| CTR-[AAAA]-001 | [date] | [date] | [fournisseur] | [ref] | [client] | [produit] | [O/N] | [O/N] | [ref NC] | [Solde/Ouvert] |
| CTR-[AAAA]-002 | | | | | | | | | | |
| CTR-[AAAA]-003 | | | | | | | | | | |

---

> **Instructions de remplissage :**
> 1. Remplissez une fiche pour CHAQUE livraison expediee depuis la Chine vers un client
> 2. Verifiez les documents de transport des la reception des documents d'export
> 3. Suivez l'acheminement et relancez le transporteur en cas de retard
> 4. Obtenez la confirmation de reception du client (email, telephone)
> 5. En l'absence de reclamation dans un delai raisonnable, la conformite est implicite
> 6. Si le client signale un probleme, ouvrez immediatement une fiche NC (PRO-NCF-001)
> 7. Ces fiches sont des preuves cles pour l'auditeur -- elles demontrent le suivi malgre l'absence de reception physique
> 8. La visite planifiee en Chine permettra de renforcer le controle qualite en amont (cf. section 8.5 du manuel qualite)
