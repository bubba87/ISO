# CHAIN-01 — Commande Produit Existant

## Chaîne Processus Complète

| Élément | Détail |
|---------|--------|
| **Code** | CHAIN-01 |
| **Type de commande** | Produit existant (référence catalogue) |
| **Statut** | Active — Fiche détaillée |
| **Source** | PROCESS_CHAIN_PRODUIT_EXISTANT_260304.doc |
| **Diagramme** | [chaine_processus_general.drawio](../diagrammes/chaine_processus_general.drawio) |

---

## Description

Cette chaîne processus couvre le flux complet d'une **commande de produit existant** — c'est-à-dire un produit dont les références, les spécifications et les fournisseurs sont déjà connus et validés. Il s'agit du cas le plus fréquent et le plus direct.

**Auteur du document source** : Roxane Wicky

---

## Flux des 8 Blocs

```
CLIENT  ──→  [BLOC 1] ──→ [BLOC 2] ──→ [BLOC 3] ──→ [BLOC 4] ──→ [BLOC 5] ──→ [BLOC 6] ──→ [BLOC 7] ──→ [BLOC 8] ──→  CLIENT
              Réception    Fiche de     Fiche de     Étude        Validation   Production    Livraison    Acceptation    Dossier
              Commande     Commande     Transport    Technique    Commande     & Qualité     & Douane     Marchandise    Clôturé
              (SALES)      (SALES)      (DELIVERY)   (MANUF.)     (SALES)      (MANUF+QUAL)  (DELIV+SALES)(QUAL+SALES)
```

---

## Détail par Ligne

### 01 SALES (Blocs 1, 2, 5)

| Bloc | Fiche | Actions clés |
|------|-------|-------------|
| **BLOC 1** — Réception Commande | [CH-BLOC-001](CH-BLOC-001_Reception_Commande.md) | Charger et enregistrer la commande dans ORDER_20XX, identifier le type de commande |
| **BLOC 2** — Création Fiche de Commande | [CH-BLOC-002](CH-BLOC-002_Fiche_Commande.md) | Créer fiche de commande, ajouter PDF, sélectionner produit, quantité, référence |
| **BLOC 5** — Validation de Commande | [CH-BLOC-005](CH-BLOC-005_Validation_Commande.md) | Imprimer et envoyer l'AR au client avec détails livraison & prix, retour client |

### 02 MANUFACTURE (Blocs 4, 6)

| Bloc | Fiche | Actions clés |
|------|-------|-------------|
| **BLOC 4** — Étude Technique Fournisseurs | [CH-BLOC-004](CH-BLOC-004_Etude_Technique.md) | Définir statut commande, envoyer infos aux fournisseurs, valider délais production |
| **BLOC 6** — Production & Qualité | [CH-BLOC-006](CH-BLOC-006_Production_Qualite.md) | Confirmer production au fournisseur (WeChat/email), validation conformité pièces |

### 03 DELIVERY (Blocs 3, 7)

| Bloc | Fiche | Actions clés |
|------|-------|-------------|
| **BLOC 3** — Création Fiche de Transport | [CH-BLOC-003](CH-BLOC-003_Fiche_Transport.md) | Créer fiche transport, valider délais livraison, définir type de livraison |
| **BLOC 7** — Livraison & Douane | [CH-BLOC-007](CH-BLOC-007_Livraison_Douane.md) | Bulletin de livraison, facture commerciale, suivi envoi & douane, informer client |

### 04 QUALITY (Blocs 6, 8)

| Bloc | Fiche | Actions clés |
|------|-------|-------------|
| **BLOC 6** — Production & Qualité | [CH-BLOC-006](CH-BLOC-006_Production_Qualite.md) | Validation de la conformité des pièces par le fournisseur suite au contrôle qualité |
| **BLOC 8** — Acceptation Marchandise | [CH-BLOC-008](CH-BLOC-008_Acceptation_Marchandise.md) | Confirmation conformité au client, facture, déclaration douanière, paiement, clôture |

---

## Spécificités « Produit Existant »

- **Pas de phase de développement** : le produit est déjà qualifié
- **Fournisseur déjà évalué** : pas besoin de processus de qualification
- **Outillage existant** : pas de création ou modification d'outillage
- **Délai plus court** : le flux est le plus rapide des 4 types de commande
- **Inspection standard** : plan d'inspection basé sur l'historique

---

## Indicateurs de performance

| Indicateur | Cible | Fréquence |
|-----------|-------|-----------|
| Délai global commande → livraison | Selon produit | Par commande |
| Taux de conformité PSI | ≥ 95% | Trimestriel |
| Taux de livraison à temps | ≥ 90% | Trimestriel |
| Réclamations client | Tendance à la baisse | Trimestriel |

---

*Réf. ISO 9001:2015 — §8.1, §8.2, §8.4, §8.5, §8.6*
*Source : PROCESS_CHAIN_PRODUIT_EXISTANT_260304.doc*
