# Fiche Détail Bloc - CH-BLOC-001 : Réception d'une Commande Client

| **Document**       | CH-BLOC-001_Reception_Commande                |
|--------------------|-----------------------------------------------|
| **Version**        | v0.7                                          |
| **Date**           | 2026-03-04                                    |
| **Classification** | Interne                                       |
| **Processus**      | Chaîne Processus - Réalisation                |
| **Chaîne réf.**    | CHAIN-01 — Commande Produit Existant          |
| **Rédaction**      | Rôle Qualité                                  |
| **Approbation**    | Direction                                     |

---

## 1. Objet

Cette fiche décrit les actions détaillées du **BLOC 1 — Réception d'une commande client** dans le cadre de la chaîne processus de commande produit existant.

---

## 2. Ligne processus

| Code ligne | Ligne     | Rôle pilote     |
|------------|-----------|-----------------|
| 01         | SALES     | Rôle Commercial |

---

## 3. Entrées du bloc

| Élément                        | Provenance                |
|--------------------------------|---------------------------|
| Commande client (e-mail, EDI, courrier) | Client                |
| Bon de commande ou demande formelle     | Client                |

---

## 4. Actions détaillées

| N° | Action                                                                                                       | Responsable     | Outil / Support                  |
|----|--------------------------------------------------------------------------------------------------------------|-----------------|----------------------------------|
| 1  | Télécharger et enregistrer la commande sur le bureau et dans le dossier ORDER_20XX sous la même nomenclature que le client | Rôle Commercial | Système de fichiers / ORDER_20XX |

---

## 5. Règles de nomenclature

| Élément               | Règle                                                              |
|-----------------------|--------------------------------------------------------------------|
| Dossier de rangement  | ORDER_20XX (XX = année en cours)                                   |
| Nom du fichier        | Identique à la nomenclature utilisée par le client                 |
| Sauvegarde locale     | Copie sur le bureau pour traitement immédiat                       |

---

## 6. Sorties du bloc

| Élément                          | Destination          |
|----------------------------------|----------------------|
| Commande enregistrée et classée  | BLOC 2 — Fiche de commande |
| Fichier sauvegardé dans ORDER_20XX | Archivage           |

---

## 7. Points de contrôle

| Contrôle                                   | Critère d'acceptation                         | Responsable     |
|--------------------------------------------|-----------------------------------------------|-----------------|
| Commande complète et lisible               | Toutes les informations requises sont présentes| Rôle Commercial |
| Nomenclature du fichier conforme           | Identique à celle du client                    | Rôle Commercial |
| Enregistrement dans le bon dossier         | Présence dans ORDER_20XX                       | Rôle Commercial |

---

## 8. Documents associés

| Référence | Document                                      |
|-----------|-----------------------------------------------|
| CHAIN-01  | Chaîne Processus — Commande Produit Existant  |
| CH-BLOC-002 | Fiche détail — Fiche de commande            |
| PR-P01-COM  | Processus Commercial                        |
| FM-P01-OFF  | Modèle d'offre commerciale                  |
| FM-P01-BC   | Bon de commande                             |

---

## Références normatives

| Clause ISO 9001:2015 | Exigence                                              |
|-----------------------|-------------------------------------------------------|
| 8.2.1                 | Communication avec les clients                         |
| 8.2.2                 | Détermination des exigences relatives aux produits     |
| 7.5                   | Informations documentées                               |

---

*Document contrôlé - Toute copie imprimée est considérée comme non contrôlée.*
*Plus Sàrl - Système de Management de la Qualité ISO 9001:2015 - v0.7*
