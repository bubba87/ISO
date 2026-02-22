# Manuel Qualité — Plus Sarl

| | |
|---|---|
| **Référence** | MQ-001 |
| **Version** | 0.4 — Version de travail |
| **Date** | 20/02/2026 |
| **Rédigé par** | Roxane Wicky |
| **Approuve par** | Roxane Wicky |
| **Organisme de certification** | SQS |

---

## Table des matières

1. [Introduction](#1-introduction)
2. [Présentation de l'entreprise](#2-présentation-de-lentreprise)
3. [Chapitre 4 — Contexte de l'organisme](#chapitre-4--contexte-de-lorganisme)
4. [Chapitre 5 — Leadership](#chapitre-5--leadership)
5. [Chapitre 6 — Planification](#chapitre-6--planification)
6. [Chapitre 7 — Support](#chapitre-7--support)
7. [Chapitre 8 — Realisation des activités opérationnelles](#chapitre-8--realisation-des-activités-opérationnelles)
8. [Chapitre 9 — Évaluation des performances](#chapitre-9--évaluation-des-performances)
9. [Chapitre 10 — Amélioration](#chapitre-10--amélioration)
10. [Annexes](#annexes)

---

## 1. Introduction

### 1.1 Objet du manuel qualité

Ce manuel qualité constitue le document de synthèse du Système de Management de la Qualité (SMQ) de Plus Sarl, conforme à la norme ISO 9001:2015.

Il présente :
- l'organisation de l'entreprise et son contexte
- la politique et les objectifs qualité
- la cartographie des processus
- les dispositions prises pour satisfaire chaque exigence de la norme

Ce document est destiné à :
- servir de référence interne pour la gérante
- presenter le SMQ à l\'organisme de certification SQS
- communiquer l'organisation qualité aux parties intéressées

### 1.2 Référence normative

- **ISO 9001:2015** — Systemes de management de la qualité — Exigences
- **ISO 9000:2015** — Systemes de management de la qualité — Principes essentiels et vocabulaire

### 1.3 Convention du document

> **Légende :** 🔴 [À REMPLIR] = obligatoire, manquant | 🟡 [RECOMMANDE] = recommandé | 🟢 = déjà rempli | 🔵 [À VÉRIFIER] = a confirmer

Les références entre parentheses (ex. *cf. CTX-QUA-001 §5*) renvoient aux documents détaillés du SMQ.

---

## 2. Présentation de l'entreprise

| Élément | Détail |
|---|---|
| **Raison sociale** | Plus Sarl |
| **Adresse** | Route de Montet 11, 1588 Cudrefin, Suisse |
| **Canton** | Fribourg (district de la Broye) |
| **Forme juridique** | Société à responsabilité limitée (Sarl) |
| **N. IDE** | CH-645.4.101.228-7 🟢 |
| **Annee de fondation** | 2007 |
| **Gérante** | Roxane Wicky |
| **Nombre d'employés** | 1 (la gérante) |
| **Associes** | Roxane Wicky, Olav Wicky, Capucine Wicky |
| **Fiduciaire** | Paradiso 🟢 |
| **Organisme de certification** | SQS 🟢 |
| **Clients** | ~10 clients actifs, principalement européens 🟢 |

### Activité principale

Plus Sarl est spécialisée dans la **coordination industrielle entre des clients européens et des partenaires de fabrication chinois**. L'activité couvre :

- la conception, le développement et la production de pièces industrielles
- le sourcing et l'approvisionnement de pièces existantes
- la gestion de la chaîne logistique internationale

Plus Sarl ne réalise pas directement la production. Celle-ci est effectuée par des partenaires industriels situés en Chine. L'entreprise coordonné cette production afin de garantir la conformité des pièces aux exigences techniques et qualitatives des clients.

*(cf. CTX-QUA-001 §1.1)*

### Partenaires industriels

| Partenaire | Activité | Relation |
|---|---|---|
| **Yuyao Mould Factory** | Fabrication moules et injection | Partenaire principal et historique (depuis 2007) 🟢 |
| **Oukailuo** (Yuyao, Chine) | Fabrication de vis | Second partenaire de production 🟢 |

### Chaîne de valeur

```
Client europeen --> Plus Sarl --> Partenaires chinois --> Plus Sarl --> Client europeen
(besoin,            (coordination, (fabrication         (controle,   (livraison)
 specification)     suivi,         moules et            suivi
                    controle)      pièces)              qualité)
```

### Outils et systèmes

| Outil | Utilisation |
|---|---|
| **FileMaker** | Gestion des données, suivi des commandes, prix, transport |
| **Email** | Communication avec les clients et les partenaires |
| **WeChat** | Communication avec les partenaires chinois |
| **Cloud** | Sauvegarde des données, hebergement chez le fournisseur 🟢 |

---

## Chapitre 4 — Contexte de l'organisme

### 4.1 Compréhension de l'organisme et de son contexte

Plus Sarl a identifié les enjeux internes et externes pertinents pour son orientation stratégique et susceptibles d'influencer sa capacité a atteindre les résultats attendus de son SMQ.

#### Enjeux externes

- Dependance envers les partenaires industriels chinois pour l'outillage et la production
- Délais et contraintes logistiques du transport international
- Exigences douanières et réglementaires à l\'importation/exportation
- Variations des coûts de production, de transport et des matières premières
- Attentes élevées des clients en termes de qualité, conformité technique et respect des délais

#### Enjeux internes

- Organisation unipersonnelle necessitant une forte gestion des priorités et de la planification
- Besoin d'une communication fluide et continue avec les clients, fournisseurs et partenaires logistiques
- Maintien d'un haut niveau de maîtrise documentaire, technique et organisationnelle
- Capacité a garantir réactivité, confidentialité et satisfaction durable des clients

#### Analyse SWOT

L'analyse SWOT complète (forces, faiblesses, opportunités, menaces) est documentée dans **CTX-QUA-001 §2** et est revue au minimum une fois par an lors de la revue de direction.

**Principaux points :**

| Forces | Faiblesses |
|---|---|
| Expertise technique en développement de moules a injection | Organisation unipersonnelle : ressources humaines limitées |
| Flexibilite et réactivité (micro-entreprise) | Dependance envers deux partenaires chinois |
| Relation de confiance historique avec Yuyao Mould Factory (depuis 2007) | Distance géographique de la production |
| Connaissance approfondie du marche européen | Pas de capacité de production en interne |

| Opportunités | Menaces |
|---|---|
| Certification ISO 9001 via SQS = accès a de nouveaux marches | Défaillance ou indisponibilité d'un partenaire chinois |
| Amélioration continue de la satisfaction client | Retards significatifs du transport international |
| Diversification fournisseurs en Asie (Oukailuo en place) | Defauts qualité majeurs sur produits fabriques |

*(cf. CTX-QUA-001 §2 pour la matrice complète)*

### 4.2 Compréhension des besoins et attentes des parties intéressées

Les parties intéressées pertinentes et leurs exigences sont identifiées :

| Partie intéressée | Exigences principales |
|---|---|
| **Clients européens** (~10 actifs) | Conformité technique, respect des délais, communication réactive, confidentialité |
| **Partenaires chinois** (Yuyao Mould Factory, Oukailuo) | Transmission claire des exigences, coordination efficace |
| **Transporteurs et transitaires** | Fiabilité des délais, intégrité des marchandises |
| **Autorites douanières** | Conformité réglementaire importation/exportation |
| **Fiduciaire Paradiso** | Conformité administrative, comptable et fiscale |
| **Associes** (Roxane, Olav, Capucine Wicky) | Rentabilité, pérennité de l'entreprise |
| **SQS** (organisme de certification) | Conformité ISO 9001:2015 |

*(cf. CTX-QUA-001 §3)*

### 4.3 Détermination du domaine d'application

**Domaine d'application du SMQ :**

> Coordination industrielle entre des clients européens et des partenaires de fabrication chinois. Conception, développement et production de pièces industrielles. Sourcing et approvisionnement de pièces existantes. Gestion de la chaîne logistique internationale.

**Site couvert :** Route de Montet 11, 1588 Cudrefin, Suisse

**Exclusion :**

| Clause exclue | Justification |
|---|---|
| **8.3 — Conception et développement** | Plus Sarl ne conçoit pas les produits. Les designs, spécifications et propriété intellectuelle appartiennent aux clients. Plus Sarl intervient uniquement en tant que coordinateur industriel. Cette exclusion n'affecte pas la capacité a fournir des produits conformes. |

*(cf. DOM-QUA-001)*

### 4.4 Système de management de la qualité et ses processus

Le SMQ de Plus Sarl est structure autour de **10 processus** :

| Type | Code | Processus | Document associé |
|---|---|---|---|
| **Management** | M1 | Leadership et stratégie | M1-DIR-001 |
| | M2 | Amélioration continue | PRO-NCF-001, PRO-ACR-001 |
| | M3 | Revue de direction | FOR-RDR-001 |
| **Opérationnel** | O1 | Commercial | CTX-QUA-001 (§1.2, 1.3) |
| | O2 | Achats et sous-traitance | PRO-ACH-001, FIC-PRO-001 |
| | O3 | Logistique et livraison | PRO-LOG-001, FIC-PRO-002 |
| | O4 | Contrôle qualité | PRO-NCF-001, FOR-CTR-001 |
| **Support** | S1 | Gestion documentaire | PRO-DOC-001 |
| | S2 | Compétences, formations et sensibilisation | FOR-CMP-001 |
| | S3 | Ressources et infrastructure | CTX-QUA-001 (§7) |

#### Representation de la cartographie

```
+=========================================================================+
|                    PROCESSUS DE MANAGEMENT                               |
|  M1 - Leadership    M2 - Amelioration     M3 - Revue de direction      |
+=========================================================================+
                                |
  EXIGENCES                     v                           SATISFACTION
  CLIENTS    ====================================================  CLIENTS
  -------->  | O1 Commercial -> O2 Achats -> O3 Logistique -> O4 Qualite |
             ====================================================
                                |
+=========================================================================+
|                    PROCESSUS SUPPORT                                     |
|  S1 - Gestion doc.   S2 - Compétences    S3 - Ressources              |
+=========================================================================+
```

Les interactions entre processus, la matrice d'interaction et le flux principal sont documentés dans **CRT-QUA-001** (sections 2 et 3).

Le fichier visuel de la cartographie est disponible : **CRT-QUA-001.drawio**.

---

## Chapitre 5 — Leadership

### 5.1 Leadership et engagement

En tant que gérante et unique employée de Plus Sarl, Roxane Wicky s'engage personnellement a :

1. Assumer la responsabilité de l'efficacité du SMQ et rendre compte de sa performance
2. Établir la politique qualité et les objectifs qualité compatibles avec l'orientation stratégique
3. Integrer les exigences du SMQ dans les processus opérationnels
4. Promouvoir l'approche par les risques et l'approche processus
5. Assurer la disponibilité des ressources nécessaires
6. Communiquer sur l'importance du management de la qualité
7. Veiller à ce que le SMQ atteigne les résultats attendus
8. Orienter et soutenir les personnes (gérante + partenaires externes)
9. Promouvoir l'amélioration continue
10. Soutenir les autres rôles de management pertinents

#### Orientation client (clause 5.1.2)

La gérante s'engage à ce que :
- les exigences des clients soient déterminées, comprises et satisfaites
- les risques et opportunités susceptibles d'affecter la conformité soient pris en compte
- l'accroissement de la satisfaction des clients soit un objectif permanent

#### Engagement opérationnel

La direction s'impliqué activement par :
- la supervision de la gestion des demandes clients et des offres commerciales
- l'analyse des conditions tarifaires
- le suivi des transports et le respect des délais
- la coordination en cas de problematique qualité
- la mise en œuvre d'actions correctives en cas de dysfonctionnement

**Gestion des situations de crise :**
- Retard logistique : reevaluation des partenaires, adaptation des modalites de transport
- Retard de production : renforcement du suivi, ajustement de la planification
- NC produit : analyse des causes, actions correctives, suivi contrôles ulterieurs

*(cf. M1-DIR-001 §2)*

### 5.2 Politique qualité

La politique qualité de Plus Sarl est etablie, communiquee et maintenue.

**Mission :** Plus Sarl est spécialisée dans la coordination industrielle entre des clients européens et des partenaires de fabrication chinois.

**Engagements de la direction :**

1. Traiter les demandes clients avec réactivité et rigueur
2. Assurer la cohérence des offres commerciales et la maîtrise des conditions tarifaires
3. Coordonner efficacement les partenaires industriels pour garantir la qualité et la conformité
4. Surveiller les opérations de production, de transport et de livraison
5. Gérer les non-conformites et mettre en œuvre des actions pour eviter leur réapparition
6. Proteger la confidentialité des informations techniques et de la propriété intellectuelle
7. Ameliorer en continu l'organisation et la performance du SMQ

**Axes stratégiques qualité :**
- Respect des délais de livraison a plus de 95%
- Maximum 3 NC par client et par an
- Délai moyen de réponse aux clients inférieur a 24h
- Renforcement du partenariat qualité avec Yuyao Mould Factory et Oukailuo
- Maîtrise de la chaîne logistique internationale

**Signature :** Direction Plus Sarl — 19/02/2026 — Cudrefin 🟢

*(cf. POL-QUA-001)*

### 5.3 Roles, responsabilités et autorites

#### Organigramme fonctionnel

```
                    +=================================+
                    |       DIRECTION GENERALE        |
                    |        Roxane Wicky             |
                    |    Gerante / Directrice         |
                    +=================================+
                                  |
        +------------+------------+------------+------------+
        |            |            |            |            |
   Responsable  Responsable   Achats &    Coordina-  Responsable
   Qualite      Commercial   Sous-trait.  tion Log.  Administratif
```

> Toutes les fonctions sont assumees par Roxane Wicky, gérante unique.

#### Responsabilités par fonction

| Fonction | Périmètre |
|---|---|
| **Direction** | Stratégie, politique qualité, objectifs, revue de direction, amélioration continue |
| **Commercial** | Analyse des besoins clients, offres, commandes, réclamations |
| **Achats** | Sélection et évaluation fournisseurs, coordination production, exigences qualité |
| **Logistique** | Transport international, documents d'expédition, suivi livraisons |
| **Qualité** | Gestion SMQ, maîtrise documentaire, NC, actions correctives, audits internes |

#### Audit interne

La gérante peut réaliser l'audit interne elle-meme. Cependant, il est **fortement recommandé** de mandater un auditeur externe indépendant pour respecter l'exigence d'indépendance de la clause 9.2.2 c). 🟡

*(cf. M1-DIR-001 §3, 4, 5, 6)*

---

## Chapitre 6 — Planification

### 6.1 Actions a mettre en œuvre face aux risques et opportunités

Plus Sarl identifié et analyse les risques et opportunités susceptibles d'influencer sa capacité a fournir des produits conformes et a améliorer la satisfaction de ses clients.

#### Principaux risques identifiés

| # | Risque | Probabilite | Impact | Niveau | Action principale |
|---|---|---|---|---|---|
| R1 | Perte d'un client important | Faible | Élevé | Moyen | Maintien relation de confiance, diversification |
| R2 | Défaillance d'un partenaire chinois | Faible | Tres élevé | Élevé | Communication renforcee, Oukailuo en second partenaire |
| R3 | Defauts qualité majeurs | Moyen | Élevé | Élevé | Gestion rapide NC, remplacement, contrôles renforces |
| R4 | Retards transport international | Moyen | Élevé | Élevé | Sélection transporteurs, marges de sécurité |
| R5 | Risques douaniers | Faible | Moyen | Faible | Niveau controlable, suivi documentaire rigoureux |

#### Opportunités principales

- Optimisation des délais de livraison
- Renforcement de la qualité de production
- Amélioration continue de la satisfaction client
- Acces a de nouveaux marches grâce à la certification ISO 9001

L'efficacité des actions est évaluée lors du suivi des indicateurs, des audits internes et de la revue de direction.

*(cf. CTX-QUA-001 §5)*

### 6.2 Objectifs qualité et planification des actions

Cinq objectifs qualité sont définis pour l'année 2026 :

| # | Objectif | Indicateur | Cible |
|---|---|---|---|
| 1 | Respect des délais de livraison | % commandes livrées dans les délais | >= 95% |
| 2 | Conformité des produits livrés | Nb de NC par client et par an | Max 3 NC/client/an |
| 3 | Maîtrise des conditions tarifaires | Taux de validation des offres | Offres validées sans reneg. majeure |
| 4 | Réactivité de réponse aux clients | Délai moyen de réponse email | 24-48H |
| 5 | Satisfaction globale des clients | Absence de réclamation majeure | Satisfaction confirmée (~10 clients) |

Le suivi est trimestriel (objectifs 1-4) ou semestriel (objectif 5). Les résultats sont présentés lors de la revue de direction.

*(cf. OBJ-QUA-001)*

### 6.3 Planification des modifications

Plus Sarl assure que toute modification susceptible d'impacter la conformité, les délais, les conditions commerciales ou l'organisation est analysée, planifiée et contrôlée avant mise en œuvre.

**Types de modifications :** introduction d'un nouveau partenaire, changement de fournisseur ou transporteur, modification produit ou outillage, évolution logistique ou organisationnelle.

**Processus :**
1. Analyse d'impact par processus concerné (O1-O4)
2. Information et validation client si nécessaire
3. Mise en œuvre contrôlée (essais ou première implementation)
4. Mise à jour des documents et integration des risques
5. Revue lors de la revue de direction

*(cf. CTX-QUA-001 §6)*

---

## Chapitre 7 — Support

### 7.1 Ressources

#### Généralités

Plus Sarl détermine et met a disposition les ressources nécessaires pour établir, maintenir et améliorer son SMQ, incluant :
- les ressources humaines
- les infrastructures numeriques et materielles
- les ressources externes liées aux processus externalisés

#### Ressources humaines

Les compétences requises pour les fonctions de direction, commercial, coordination industrielle, logistique et qualité sont définies au chapitre 5.3. La gérante assure l'ensemble de ces fonctions depuis 2007.

#### Infrastructure

| Infrastructure | Utilisation |
|---|---|
| Ordinateur equipe de logiciels | Gestion administrative et technique |
| Système FileMaker | Suivi produits, commandes, prix, transport 🟢 |
| Email | Échanges formels avec partenaires et clients 🟢 |
| Acces internet | Communication, suivi logistique 🟢 |
| Application WeChat | Échanges opérationnels avec partenaires chinois 🟢 |
| Téléphone mobile | Disponibilité et réactivité 🟢 |
| Sauvegarde cloud | Sauvegarde des données, chez le fournisseur 🟢 |

#### Environnement de travail

L'environnement de travail assure la confidentialité des données, la fiabilité des communications et la réactivité dans la gestion des commandes.

#### Ressources externes — Processus externalisés

| Partenaire | Activité | Suivi |
|---|---|---|
| **Yuyao Mould Factory** | Moules et injection | Accord qualité, évaluation annuelle (FOR-EVF-001) 🟢 |
| **Oukailuo** (Yuyao) | Vis | Accord qualité, évaluation annuelle 🟢 |
| **Paradiso** | Fiduciaire | Contrat de mandat 🟢 |
| Transitaires | Transport international | Suivi par expédition 🟡 |

*(cf. CTX-QUA-001 §7)*

### 7.2 Compétences

Les compétences de la gérante sont documentées dans le registre FOR-CMP-001 :

- **7 compétences cles identifiées** : disponibilité, priorités, évaluation des limites, relationnel, résolution de problèmes, communication anglais, deplacements critiques
- **Maintien des compétences** : expérience quotidienne, communication continue avec partenaires, retours clients, pratique terrain, veille technique, analyse des performances

**Extension aux fournisseurs :** Plus Sarl veille à ce que les partenaires industriels disposent des compétences techniques nécessaires. Évaluation continue via respect des délais, conformité des pièces, stabilité de la relation.

**Informations en attente :** Diplomes et formations initiales de la gérante non divulgues à ce stade. 🔴

*(cf. FOR-CMP-001 §1-4)*

### 7.3 Sensibilisation

La gérante est directement impliquée dans la compréhension, l'application et l'amélioration du SMQ. La sensibilisation porte sur :

- la politique qualité (cf. POL-QUA-001)
- les objectifs qualité (cf. OBJ-QUA-001)
- l'importance de la satisfaction client
- les exigences de conformité des produits et services
- les consequences d'un écart par rapport aux exigences du SMQ

**Moyens de sensibilisation :** integration dans les activités quotidiennes, communication des priorités et objectifs, analyse des NC et retours clients, revue de direction.

*(cf. FOR-CMP-001 §5)*

### 7.4 Communication

#### Communication externe

| Partie intéressée | Canal principal | Canal secondaire |
|---|---|---|
| **Clients européens** | Email | Téléphone (urgences) |
| **Partenaires chinois** | WeChat | Email |
| **Transporteurs** | Email | WeChat |
| **Fiduciaire Paradiso** | Email | Téléphone |
| **Autorites douanières** | Email / portail officiel | Téléphone |

#### Maîtrise de la confidentialité

Plus Sarl veille à la protection des informations techniques, commerciales et contractuelles :
- données clients traitées comme confidentielles
- accès aux systèmes sécurisé
- informations transmises uniquement aux parties concernées
- partenaires informes du caractere confidentiel

*(cf. CTX-QUA-001 §7.6-7.7, M1-DIR-001 §7)*

### 7.5 Informations documentées

Le SMQ comprend **24 documents** gérés selon la procédure PRO-DOC-001 :

**Gestion documentaire :**
- Création, approbation, diffusion, mise à jour et archivage par la gérante
- Codification systématique (POL, DOM, CTX, CRT, OBJ, M1, FIC, PRO, FOR, CHK, LST)
- Stockage : FileMaker, fichiers locaux, archivés email, WeChat, partenaires chinois, fiduciaire
- Sauvegarde cloud automatique 🟢
- Conservation : 3 ans (enregistrements SMQ), 5 ans (commandes), 10 ans (factures)

La liste maitresse des documents et la liste de gestion documentaire sont tenues a jour dans PRO-DOC-001 §8-9.

*(cf. PRO-DOC-001)*

---

## Chapitre 8 — Realisation des activités opérationnelles

### 8.1 Planification et maîtrise opérationnelles

Les activités opérationnelles sont planifiées et maitrisees a travers les 4 processus opérationnels (O1 a O4) et le flux principal decrit dans la cartographie des processus.

**Flux principal (12 étapes) :**

1. Reception de la demande client (O1)
2. Analyse préalable et revue de commande (O1/O2/O4) — incluant analyse d'impact si modification (clause 6.3)
3. Consultation des partenaires industriels (O1/O2/O3)
4. Validation et enregistrement dans FileMaker (O1/S1)
5. Coordination technique (O2)
6. Lancement de la fabrication (O2)
7. Contrôle qualité pre-expédition (O4)
8. Préparation logistique (O3)
9. Suivi du transport (O3)
10. Confirmation de reception par le client (O3/O1)
11. Facturation et suivi (O1)
12. Traçabilité et amélioration (S1)

*(cf. CRT-QUA-001 §3)*

### 8.2 Exigences relatives aux produits et services

#### Revue de commande

Chaque demande client (commande, devis, modification, réclamation) fait l'objet d'une analyse préalable :

| Aspect | Processus |
|---|---|
| Compréhension des besoins | O1 — Commercial |
| Références, quantités, délais | O1 — Commercial |
| Faisabilité technique et logistique | O2 — Achats & sous-traitance |
| Exigences qualité | O4 — Contrôle qualité |

Apres validation : enregistrement dans FileMaker, accusé de reception au client.

Toute modification est soumise a analyse, validation partenaire si nécessaire, confirmation client par email et mise à jour FileMaker.

*(cf. CTX-QUA-001 §1.3, M1-DIR-001 §6)*

### 8.3 Conception et développement — EXCLU

Plus Sarl ne conçoit pas les produits. Les conceptions, cahiers des charges, brevets et spécifications appartiennent aux clients ou sont définis par les partenaires industriels. Cette exclusion est justifiée dans DOM-QUA-001 §3.

### 8.4 Maîtrise des processus, produits et services fournis par des prestataires externes

La production est entièrement externalisée chez les partenaires chinois. La maîtrise repose sur :

- **Sélection** : partenaires experimentes, capacité technique évaluée
- **Suivi** : communication régulière (email, WeChat), échanges documentés, rapports de production
- **Évaluation** : évaluation annuelle des fournisseurs (FOR-EVF-001), suivi des indicateurs (délais, conformité)
- **Contrôle** : contrôle qualité pre-expédition par le partenaire, échantillons valides

Les critères d'évaluation continue incluent :
- Respect des délais (continu, par commande)
- Conformité des pièces livrées (a chaque reception)
- Stabilité de la relation industrielle (annuel)

*(cf. PRO-ACH-001, FIC-PRO-001, FOR-EVF-001)*

### 8.5 Production et prestation de service

La coordination de la production et la prestation logistique suivent les processus O2 et O3 :

**Processus O2 — Achats et sous-traitance :**
- Transmission des commandes et exigences techniques aux partenaires
- Vérification de la faisabilité, délais et conditions de fabrication
- Suivi de production par échanges documentés
- Envoi et validation d'échantillons

**Processus O3 — Logistique et livraison :**
- Organisation du transport adapte (avion, bateau, train)
- Documents d'expédition et douaniers conformes
- Suivi du transport jusqu'a livraison finale
- Information client en cas de retard ou incident

*(cf. PRO-LOG-001, FIC-PRO-002)*

### 8.5.3 Propriété des clients

Les moules sont développés et stockés en Chine chez les partenaires. Les moules sont la **propriété des clients**. Un inventaire des moules existe. 🟢

Les données techniques (designs, spécifications) appartiennent aux clients et sont traitées comme confidentielles.

*(cf. CTX-QUA-001 §9, PRO-DOC-001 §7)*

### 8.6 Liberation des produits et services

Avant expédition, Plus Sarl s'assure de la conformité des pièces :
- vérification de la conformité aux exigences techniques
- contrôle qualité réalisé par le fabricant 🔵 [À VÉRIFIER — fiche de contrôle a formaliser]
- suivi documentaire conserve sur FileMaker
- analyse des retours clients après livraison

*(cf. FOR-CTR-001)*

### 8.7 Maîtrise des éléments de sortie non conformes

En cas de non-conformité identifiée :
1. Création d'une fiche de non-conformité
2. Decision : acceptation, remplacement ou correction
3. Analyse de la cause et investigation
4. Mise en œuvre d'actions correctives pour eviter la répétition

*(cf. PRO-NCF-001)*

---

## Chapitre 9 — Évaluation des performances

### 9.1 Surveillance, mesure, analyse et évaluation

Le suivi de la performance du SMQ s'appuie sur :

**Indicateurs de performance (tableau de bord) :**

| Indicateur | Cible | Frequence |
|---|---|---|
| % livraisons dans les délais | >= 95% | Trimestriel |
| Nb de NC par client/an | Max 3 | Trimestriel |
| Validation des offres sans reneg. majeure | Oui | Trimestriel |
| Délai moyen de réponse email | 24-48H | Trimestriel |
| Satisfaction globale clients | Absence réclamation majeure | Semestriel |

*(cf. OBJ-QUA-001 §2)*

### 9.1.2 Satisfaction du client

La satisfaction des clients est évaluée par :
- suivi des réclamations majeures
- collecte de retours clients (formulaire de satisfaction)
- bilan annuel

*(cf. FOR-SAT-001)*

### 9.2 Audit interne

L'audit interne est réalisé au minimum 1 fois par an, conformément à la procédure PRO-AUD-001.

| Élément | Détail |
|---|---|
| **Frequence** | Minimum 1 fois par an |
| **Responsable** | Gérante ou auditeur externe indépendant 🟡 |
| **Référence** | PRO-AUD-001, CHK-AUD-001 |

> **Recommandation forte :** dans une organisation unipersonnelle, il est recommandé de mandater un auditeur externe indépendant pour respecter l'exigence d'indépendance (clause 9.2.2 c). 🟡

*(cf. PRO-AUD-001, CHK-AUD-001)*

### 9.3 Revue de direction

La revue de direction est réalisée au minimum **1 fois par an** par Roxane Wicky.

**Éléments examines :**
- État des actions des revues précédentes
- Modifications du contexte interne et externe
- Performance des processus et conformité des produits
- Satisfaction des clients européens
- Résultats des audits
- Performance des fournisseurs (Yuyao Mould Factory, Oukailuo)
- Adéquation des ressources
- Efficacité des actions face aux risques et opportunités
- Opportunités d'amélioration

Les données de sortie comprennent les decisions relatives à l'amélioration du SMQ, aux besoins en ressources et aux actions a mener.

*(cf. FOR-RDR-001, M1-DIR-001 §8)*

---

## Chapitre 10 — Amélioration

### 10.1 Généralités

Plus Sarl détermine et sélectionné les opportunités d'amélioration et entreprend les actions nécessaires pour satisfaire les exigences des clients et accroitre leur satisfaction.

Le processus **M2 — Amélioration continue** pilote l'amélioration du SMQ a travers :
- le suivi des indicateurs de performance
- la gestion des actions correctives
- l'analyse des tendances
- la revue de l'efficacité des modifications

### 10.2 Non-conformité et action corrective

**Identification des NC :**
- lors de contrôles par le partenaire industriel
- a reception de marchandises par le client
- à la suite d'une réclamation

**Processus de traitement :**
1. Enregistrement dans une fiche de NC
2. Analyse de la situation et des causes
3. Decision de traitement : acceptation, correction ou remplacement
4. Mise en place d'actions correctives
5. Vérification de leur efficacité
6. Intégration au suivi qualité, audit interne et revue de direction

**NC enregistrée en 2026 :** NC_2026_1001 — erreur d'étiquetage sur expédition SHIP_25058 / article CFM00057428 / référence 90.60.05710 (1000 pièces avec mauvaise etiquette). Action : renforcement contrôle étiquetage. 🟢

*(cf. PRO-NCF-001, PRO-ACR-001, FOR-RCL-001)*

### 10.3 Amélioration continue

L'amélioration continue est alimentee par :
- les résultats des audits internes
- l'analyse des indicateurs de performance
- les retours clients et les réclamations
- les résultats de la revue de direction
- les actions correctives mises en œuvre

Les decisions d'amélioration sont prises lors de la revue de direction et intégrées dans la planification des objectifs qualité.

---

## Annexes

### A. Liste des documents du SMQ

| # | Référence | Titre |
|---|---|---|
| 1 | POL-QUA-001 | Politique Qualité |
| 2 | DOM-QUA-001 | Domaine d'Application du SMQ |
| 3 | CTX-QUA-001 | Contexte de l'Organisation |
| 4 | CRT-QUA-001 | Cartographie des Processus |
| 5 | OBJ-QUA-001 | Objectifs Qualité |
| 6 | M1-DIR-001 | Leadership et Attribution des Responsabilités |
| 7 | FIC-PRO-001 | Fiche Processus O2 — Achats et Sous-traitance |
| 8 | FIC-PRO-002 | Fiche Processus O3 — Logistique et Livraison |
| 9 | PRO-DOC-001 | Maîtrise des Documents et Enregistrements |
| 10 | PRO-AUD-001 | Audit Interne |
| 11 | PRO-NCF-001 | Non-Conformites |
| 12 | PRO-ACR-001 | Actions Correctives |
| 13 | PRO-ACH-001 | Achats et Sous-traitance |
| 14 | PRO-LOG-001 | Logistique et Livraison |
| 15 | FOR-EVF-001 | Évaluation Fournisseurs |
| 16 | FOR-SAT-001 | Satisfaction Client |
| 17 | FOR-RDR-001 | Revue de Direction |
| 18 | FOR-CMP-001 | Compétences et Formation |
| 19 | FOR-RCL-001 | Réclamations Client |
| 20 | FOR-CTR-001 | Contrôle Reception |
| 21 | CHK-AUD-001 | Checklist Audit ISO 9001 |

### B. Correspondance ISO 9001:2015 — Documents SMQ

Voir **INDEX_DOSSIER_AUDIT.md** pour la table de correspondance complète clause par clause.

### C. Cartographie des processus (format visuel)

Voir **CRT-QUA-001.drawio**.

---

## Historique des revisions

| Version | Date | Modification | Auteur |
|---|---|---|---|
| 0.4 | 20/02/2026 | Création initiale du Manuel Qualité (version de travail). Compilation de l'ensemble des documents SMQ v0.4 incluant 16 UPDATEs intégrés (U1-U16). | Roxane Wicky |

---

*Manuel Qualité rédigé conformément aux exigences de la norme ISO 9001:2015.*
*Document de travail — Version 0.4 — Plus Sarl, Cudrefin, Suisse.*
