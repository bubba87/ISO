# Review of Version v0.6 — QMS ISO 9001:2015 Plus Sarl

**Review date**: 2026-03-04
**Version analyzed**: v0.6
**Files analyzed**: 37 files (9 QM + 6 processes + 12 chains + 8 documents + 2 drawio)

---

## Summary

Version v0.6 represents the **first formally structured version** of the ISO 9001 dossier. Compared to v0.5, the main changes are:

- Addition of **standardized metadata headers** (version, date, approval, normative references)
- Restructuring with **numbered sections** and explicit ISO references
- Content enrichment and better formalization
- Removal of 3 review files from v0.5

The structure (37 files) remains identical. No files were added or removed (excluding review files).

**Overall verdict: 75-80% ready for ISO 9001:2015 audit** — with critical gaps to address.

---

## 1. Critical Non-Conformities (to be corrected BEFORE audit)

### 1.1 Process PS02 — Competence Management: MISSING

- **ISO Clause**: 7.2 (Competence)
- **Finding**: PS02 is referenced in MQ_02, MQ_03, MQ_04, MQ_06, MQ_07 but **no process file exists**
- **Impact**: Major non-conformity almost certain during audit
- **Action**: Create `processus/PS02_Gestion_Competences.md`
- **Required content**: Needs identification, training plan, evaluation, competence matrix

### 1.2 Competence Matrix: MISSING

- **ISO Clause**: 7.2 (Competence)
- **Finding**: Three identical references in MQ_03 and MQ_07 indicate "to be presented later"
- **Impact**: The auditor will require proof of competence demonstration
- **Action**: Create the detailed matrix (roles x competencies, levels E/S/B)

### 1.3 Process PS03 — Continuous Improvement: MISSING

- **ISO Clause**: 10.3 (Continual improvement)
- **Finding**: MQ_10 references PS03 in its header but this process does not exist anywhere in the process map (MQ_02)
- **Impact**: Documentary inconsistency + missing process
- **Action**: Create `processus/PS03_Amelioration_Continue.md` or integrate into M1

### 1.4 Non-Conformity Classification: INCONSISTENT

- **ISO Clause**: 8.7, 10.2
- **Finding**:
  - MQ_10 defines 4 levels: Minor / Significant / Major / Critical
  - DOC_Non_Conformite defines: Minor / Major / Critical / Blocking
- **Impact**: Two classification systems within the same QMS = non-conformity
- **Action**: Harmonize on a single scale across all documents

---

## 2. Coding Inconsistencies (minor non-conformities)

### 2.1 PM01 vs M1

- MQ_02, MQ_04, MQ_06 use **PM01** (Strategic management)
- The process file is named **M1_Leadership.md**
- **Action**: Choose a single coding and apply it everywhere

### 2.2 P03/P04 potentially swapped

- MQ_02 section 2.3 defines: P03 = Monitoring/QC, P04 = Logistics
- Files: P03_Logistique_Livraison.md, P04_Controle_Qualite.md
- **Action**: Verify and align numbering between manual and files

### 2.3 PS01 vs S1

- The manual references **PS01** (Document management)
- The file is named **S1_Gestion_Documentaire.md**
- **Action**: Harmonize naming convention

### 2.4 PS03 not mapped

- PS03 appears in the MQ_10 header but is cited neither in MQ_02 nor in MQ_04
- **Action**: Add PS03 to the official process map or remove the reference

---

## 3. Missing Documents and Forms

### 3.1 Referenced forms not provided

| Code | Title | Referenced in |
|------|-------|---------------|
| FM-P01-SAT | Customer Satisfaction Survey (template) | P01_Commercial |
| FM-P02-AQF | Supplier Quality Agreement (template) | P02_Achats |
| FM-P02-EVAL | Supplier Evaluation (template) | P02_Achats |
| IT-P04-ECH | AQL Sampling Instruction | P04_Controle_Qualite |

> **Note**: DOC_Satisfaction_Client, DOC_Accord_Qualite_Fournisseur and DOC_Evaluation_Fournisseur exist and could cover these needs. References should be aligned (FM-xxx vs DOC_xxx).

### 3.2 Missing Work Instructions

Work instructions (WI) are not documented:
- WI IPC Inspection
- WI DUPRO Inspection
- WI PSI Inspection
- WI Loading Check
- WI Supplier Audit

### 3.3 Chapter MQ_01 missing

- The manual starts directly at MQ_02
- An introductory chapter (purpose, scope, reading guide, history) would be recommended
- **Severity**: Low (no direct normative requirement)

---

## 4. Incomplete Process Chains

### 4.1 CHAIN-01: Existing Product Order
- **Status**: 100% complete
- KPIs, RACI, ISO references: all present

### 4.2 CHAIN-02: Tooling Modification Order
- **Status**: ~70% complete (marked "To be completed")
- **Missing**: BLOC 3 and BLOC 7 not detailed, RACI matrix absent
- Post-modification validation criteria not documented

### 4.3 CHAIN-03: New Tooling Order
- **Status**: ~75% complete (marked "To be completed")
- **Missing**: BLOC 3 and BLOC 7, RACI matrix, T0/T1 deliverables, tooling intellectual property

### 4.4 CHAIN-04: Sourcing Order
- **Status**: ~70% complete (marked "To be completed")
- **Missing**: BLOC 3 and BLOC 7, RACI matrix, supplier selection criteria, supplier audit process

### 4.5 BLOC Sheets (001-008)
- **Status**: 100% complete (inputs/outputs/control points/responsibilities)

---

## 5. Formatting Issues

### 5.1 Inconsistent UTF-8 Encoding

| File | Accents | Status |
|------|---------|--------|
| MQ_02, MQ_03 | Preserved (Qualite, Activites) | OK |
| MQ_04 | Mixed (titles without accents, content with) | To be corrected |
| MQ_05, MQ_06, MQ_08, MQ_09, MQ_10 | Missing (Qualite, Realisation, Evaluation) | To be corrected |

- **Impact**: Less professional documents for a French-speaking auditor
- **Action**: Standardize all files in UTF-8 with French accents

### 5.2 Normative Numbering Error

- MQ_09 titles "9.1.3 Customer satisfaction"
- ISO 9001:2015 places customer satisfaction at **9.1.2**
- **Action**: Correct the numbering

### 5.3 Unresolved Placeholder

- MQ_10, line 49: "Sequential reference NC-YYYY-XXX"
- "XXX" is a placeholder
- **Action**: Replace with actual format (e.g.: NC-2026-001)

---

## 6. KPIs: Points of Attention

### 6.1 Excellent Coverage
- **37 KPIs** defined in total (6-7 per process)
- Targets generally realistic and measurable

### 6.2 KPIs to Adjust

| KPI | Process | Issue | Action |
|-----|---------|-------|--------|
| Customer retention rate | P01 | Reference period not defined | Specify (rolling 12 months?) |
| Average transit time | P03 | Target "Depending on destination" = not measurable | Define target by region/corridor |
| Up-to-date document rate | S1 | Target 100% = unrealistic | Lower to 98% |

---

## 7. Operational Documents: Analysis

All 8 documents in the `/documents/` directory are **complete and usable**:

| Document | Code | Completeness |
|----------|------|-------------|
| Supplier Quality Agreement | FM-P02-AQF | 95% (form to be filled) |
| Internal Audit | FM-P04-AUD | 100% |
| Supplier Evaluation | FM-P02-EVAL | 100% |
| Document Management | FM-PS01-GD | 100% |
| Non-Conformity | FM-P04-NC | 100% |
| Quality Objectives | FM-PM01-OBJ | 100% |
| Management Review | FM-PM01-RD | 100% |
| Customer Satisfaction | FM-P01-SAT | 100% |

---

## 8. Cross-references: Analysis

### 8.1 Verified Consistencies
- All 4 CHAINs correctly reference the 8 BLOCs
- Quality Manual <-> Support Documents: generally consistent
- DOC_Objectifs_Qualite includes the 6 objectives from MQ_06
- DOC_Audit_Interne includes the ISO checklist from MQ_09
- DOC_Revue_Direction includes the inputs/outputs from MQ_09

### 8.2 Missing Links
- No cross-references between CHAIN/BLOC and operational documents
- Example: BLOC 6 should reference FM-P04-NC; BLOC 8 should reference FM-P01-SAT

---

## 9. Strengths of v0.6

- Generally good ISO 9001:2015 coverage (clauses 4 to 10)
- Clause 8.3 exclusion (Design) correctly justified and documented
- 4 well-defined operational processes with swimlanes
- 37 ambitious and measurable KPIs
- Formalized risk management (risk/opportunity register in MQ_06)
- Complete RACI matrix in MQ_03
- 8 consistent and usable support documents
- 8 complete BLOC sheets with inputs/outputs/control points
- Drawio process map and general chain diagram

---

## 10. Priority Action Plan

### Priority 1 — CRITICAL (before any audit)

| # | Action | Effort | ISO Clause |
|---|--------|--------|-----------|
| 1 | Create process PS02 (Competence Management) | 1 day | 7.2 |
| 2 | Create detailed competence matrix | 1 day | 7.2 |
| 3 | Create process PS03 (Continuous Improvement) or integrate into M1 | 0.5 day | 10.3 |
| 4 | Harmonize NC classification (MQ_10 vs DOC_Non_Conformite) | 0.5 day | 8.7, 10.2 |
| 5 | Unify process naming convention (PM01/M1, PS01/S1, P03/P04) | 0.5 day | 4.4 |

### Priority 2 — IMPORTANT (before audit)

| # | Action | Effort |
|---|--------|--------|
| 6 | Finalize CHAIN-02, CHAIN-03, CHAIN-04 (BLOC 3, 7, RACI) | 2 days |
| 7 | Align form references (FM-xxx vs DOC_xxx) | 0.5 day |
| 8 | Correct numbering 9.1.3 -> 9.1.2 in MQ_09 | 5 min |
| 9 | Fix UTF-8 encoding (MQ_05, MQ_06, MQ_08, MQ_09, MQ_10) | 1 day |
| 10 | Add cross-references CHAIN/BLOC -> operational documents | 0.5 day |

### Priority 3 — DESIRABLE

| # | Action | Effort |
|---|--------|--------|
| 11 | Create MQ_01 (Manual Introduction) | 0.5 day |
| 12 | Create work instructions (WI for IPC, DUPRO, PSI inspections) | 2 days |
| 13 | Refine KPIs (retention, transit, up-to-date documents) | 0.5 day |
| 14 | Add revision history to each document | 0.5 day |
| 15 | Document tooling intellectual property (CHAIN-03) | 0.5 day |

---

## 11. Certification Risks

| Risk | Probability | Severity | Clause |
|------|------------|----------|--------|
| Major NC: missing competence matrix | Very high | Major | 7.2 |
| Major NC: missing PS02 process | High | Major | 7.1.2 |
| Major NC: inconsistent NC classification | Medium | Significant | 10.2 |
| Minor NC: inconsistent process coding | Medium | Minor | 4.4 |
| Minor NC: incomplete process chains | Medium | Minor | 8.1 |
| Minor NC: poorly defined KPIs | Low | Minor | 9.1 |

**Recommendation**: Do not present for audit before resolving Priority 1 actions.

---

## 12. README Compliance Note

The README.md still indicates "Current version: v0.4" and a structure based on v0.4.
- **Action**: Update the README to reflect the v0.6 structure

---

*Review performed on 2026-03-04 — Version 0.6 of the QMS Plus Sarl*
