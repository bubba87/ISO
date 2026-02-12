# Registre et Formulaire de Reclamations Client

| | |
|---|---|
| **Reference** | FOR-RCL-001 |
| **Version** | 0.3 |
| **Date** | 12/02/2026 |
| **Societe** | Plus Sarl |

> **Legende :** :red_circle: [A REMPLIR] = obligatoire, manquant | :yellow_circle: [RECOMMANDE] = recommande | :green_circle: = deja rempli | :blue_circle: [A VERIFIER] = a confirmer

| Version | Date | Modification | Auteur |
|---|---|---|---|
| 0.1 | 10/02/2026 | Creation initiale | Roxane Wicky |
| 0.2 | 10/02/2026 | Ajout registre, indicateurs, lien NC_2026_1001 | Roxane Wicky |
| 0.3 | 12/02/2026 | Integration des reponses (Whang, Paradiso, SQS, cloud, ~10 clients, echantillonnage CQ). Ajout du systeme de legende des champs. | Roxane Wicky |

---

> **Note v0.2 :** La premiere non-conformite documentee dans le cadre du SMQ (NC_2026_1001 — erreur
> d'etiquetage sur la commande SHIP_25058 / CFM00057428 / 90.60.05710, 1000 pieces avec mauvaise
> etiquette) a ete detectee en interne par la gerante, et non via une reclamation client.
> Ce cas demontre l'efficacite du controle interne mis en place et confirme que les non-conformites
> ne proviennent pas uniquement des reclamations clients. Le processus NC (PRO-NCF-001) peut etre
> declenche independamment d'une reclamation.

---

## Principes de traitement des reclamations chez Plus Sarl

| Element | Regle applicable |
|---|---|
| **Delai de prise en compte** | :green_circle: Toute reclamation est traitee quelle que soit sa date de signalement par le client |
| **Processus de traitement** | :green_circle: Identifier la cause, mettre en oeuvre des actions correctives, assurer la satisfaction du client |
| **Remplacement de produits** | :green_circle: Les produits sont remplaces lorsque la non-conformite est imputable a Plus Sarl ou a ses fournisseurs |
| **Conditions financieres** | :green_circle: Discutees avec le fournisseur (Yuyao Mould Factory ou Whang) en fonction de l'origine du probleme |
| **Responsable** | :green_circle: Roxane Wicky (gerante — seule collaboratrice) |

---

## Fiche de Reclamation Client

### Identification

| Element | Detail |
|---|---|
| **N de reclamation** | :red_circle: [A REMPLIR — RCL-[AAAA]-[NNN]] |
| **Date de reception** | :red_circle: [A REMPLIR — JJ/MM/AAAA] |
| **Client** | :red_circle: [A REMPLIR — Nom du client] |
| **Contact** | :red_circle: [A REMPLIR — Nom de la personne] |
| **Canal** | [ ] Email [ ] Telephone [ ] WeChat [ ] Courrier [ ] Autre : :red_circle: [A REMPLIR] |
| **Commande/Projet concerne** | :red_circle: [A REMPLIR — Reference] |
| **Produit concerne** | :red_circle: [A REMPLIR — Description] |

### Description de la reclamation

| Element | Detail |
|---|---|
| **Objet de la reclamation** | [ ] Qualite produit [ ] Retard livraison [ ] Erreur commande [ ] Documentation [ ] Emballage/Transport [ ] Autre : :red_circle: [A REMPLIR] |
| **Description detaillee** | :red_circle: [A REMPLIR — Description factuelle telle que rapportee par le client] |
| **Impact pour le client** | :red_circle: [A REMPLIR — Consequences : arret production, perte financiere, retard projet, etc.] |
| **Gravite** | [ ] Critique [ ] Majeure [ ] Mineure |
| **Pieces jointes** | [ ] Photos [ ] Rapport [ ] Email [ ] Autre : :red_circle: [A REMPLIR] |

### Accuse de reception

| Element | Detail |
|---|---|
| **Date d'accuse de reception au client** | :red_circle: [A REMPLIR — JJ/MM/AAAA] |
| **Mode** | [ ] Email [ ] Telephone [ ] Autre |
| **Delai de reponse promis** | :red_circle: [A REMPLIR — X jours ouvrables] |

### Analyse et traitement

| Element | Detail |
|---|---|
| **Reclamation justifiee ?** | [ ] Oui [ ] Partiellement [ ] Non |
| **Justification** | :red_circle: [A REMPLIR — Si non justifiee, expliquer pourquoi] |
| **Origine du probleme** | [ ] Fabrication (fournisseur chinois) [ ] Transport [ ] Specification client [ ] Coordination Plus Sarl [ ] Autre : :red_circle: [A REMPLIR] |
| **Fournisseur concerne** | [ ] Yuyao Mould Factory [ ] Whang [ ] Transporteur [ ] Autre : :red_circle: [A REMPLIR] |
| **NC associee ouverte ?** | [ ] Oui - Ref : NC-[AAAA]-[NNN] [ ] Non |
| **Cause identifiee** | :red_circle: [A REMPLIR — Cause racine de la reclamation] |
| **Correction immediate** | :red_circle: [A REMPLIR — Action corrective immediate pour le client] |
| **Action corrective** | [ ] Oui - Ref : AC-[AAAA]-[NNN] [ ] Non (cas isole) |

### Communication avec le fournisseur

| Element | Detail |
|---|---|
| **Fournisseur informe** | [ ] Oui [ ] Non [ ] N/A |
| **Date d'information** | :red_circle: [A REMPLIR — JJ/MM/AAAA] |
| **Mode de communication** | [ ] Email [ ] WeChat [ ] Autre |
| **Reponse du fournisseur** | :red_circle: [A REMPLIR — Resume de la reponse] |
| **Conditions financieres discutees** | [ ] Oui (detail : :red_circle: [A REMPLIR]) [ ] Non [ ] N/A |
| **Prise en charge financiere** | [ ] Fournisseur [ ] Plus Sarl [ ] Partagee [ ] N/A |

### Resolution

| Element | Detail |
|---|---|
| **Solution proposee au client** | [ ] Remplacement du produit [ ] Avoir/remboursement [ ] Retouche [ ] Explication/justification [ ] Ajustement commercial [ ] Autre : :red_circle: [A REMPLIR] |
| **Detail de la solution** | :red_circle: [A REMPLIR — Description] |
| **Date de la resolution** | :red_circle: [A REMPLIR — JJ/MM/AAAA] |
| **Client satisfait de la resolution ?** | [ ] Oui [ ] Non [ ] Pas de retour |

### Cloture

| Element | Detail |
|---|---|
| **Date de cloture** | :red_circle: [A REMPLIR — JJ/MM/AAAA] |
| **Delai de traitement** | :red_circle: [A REMPLIR — Nombre de jours] |
| **Cloturee par** | :green_circle: Roxane Wicky |

---

## Registre des Reclamations

| N | Date | Client | Objet | Gravite | Justifiee | Fournisseur concerne | NC/AC | Resolution | Delai | Statut |
|---|---|---|---|---|---|---|---|---|---|---|
| RCL-2026-001 | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] |
| RCL-2026-002 | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] |
| RCL-2026-003 | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] |
| RCL-2026-004 | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] |
| RCL-2026-005 | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] |

---

## Indicateurs reclamations

| Indicateur | T1 | T2 | T3 | T4 | Annuel |
|---|---|---|---|---|---|
| Nombre de reclamations | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] |
| Dont justifiees | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] |
| Dont liees a la fabrication (Yuyao Mould Factory / Whang) | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] |
| Dont liees au transport | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] |
| Dont liees a la coordination | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] |
| Delai moyen de traitement (jours) | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] |
| Taux de resolution satisfaisante | :red_circle: [A REMPLIR — au fur et a mesure — %] | :red_circle: [A REMPLIR — au fur et a mesure — %] | :red_circle: [A REMPLIR — au fur et a mesure — %] | :red_circle: [A REMPLIR — au fur et a mesure — %] | :red_circle: [A REMPLIR — au fur et a mesure — %] |
| Produits remplaces | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] | :red_circle: [A REMPLIR — au fur et a mesure] |

---

> **Instructions de remplissage :**
> 1. Enregistrez TOUTE reclamation, meme verbale (par telephone ou WeChat)
> 2. Accusez reception au client dans les 24-48h
> 3. Traitez les reclamations critiques en priorite
> 4. Communiquez au partenaire chinois concerne (Yuyao Mould Factory ou Whang) si la reclamation concerne la fabrication
> 5. Discutez les conditions financieres avec le fournisseur en fonction de l'origine du probleme
> 6. Les produits sont remplaces lorsque la NC est imputable a Plus Sarl ou ses fournisseurs
> 7. L'absence de reclamation est utilisee comme indicateur de satisfaction client (voir FOR-SAT-001)
> 8. Presentez les indicateurs reclamations lors de la revue de direction (FOR-RDR-001)
> 9. Toute reclamation est traitee quelle que soit sa date de signalement — pas de prescription
> 10. Les NC peuvent aussi etre detectees en interne (cf. NC_2026_1001) — elles ne dependent pas exclusivement des reclamations clients
> 11. L'auditeur SQS examinera ce registre — maintenez-le a jour rigoureusement
