# Process Chain - CHAIN-03: New Tooling Order

| **Document**       | CHAIN-03_Commande_Nouvel_Outillage           |
|--------------------|----------------------------------------------|
| **Version**        | v0.7                                         |
| **Date**           | 2026-03-04                                   |
| **Classification** | Internal                                     |
| **Status**         | **Active**                                   |
| **Process**        | Process Chain - Realization                  |
| **Drafted by**     | Quality Role                                 |
| **Approved by**    | Management                                   |

---

## 1. Purpose

This document describes the process chain for handling an **order requiring the creation of new tooling**. This chain follows the 8-block structure of CHAIN-01 (Existing Product) with specific adaptations related to the design phase, tooling manufacture, and validation through samples (T0/T1).

---

## 2. Scope

This chain applies to any customer order involving the design and manufacture of new tooling at a qualified supplier, regardless of the geographical location of the customer or the supplier.

---

## 3. Specificities of the "New Tooling" Chain

| Characteristic                   | Description                                                                    |
|----------------------------------|--------------------------------------------------------------------------------|
| Development phase                | Complete -- design and manufacture of new tooling                              |
| Supplier evaluation              | Already completed -- supplier qualified and referenced                         |
| Tooling                          | New -- design, manufacture, commissioning, and validation required             |
| Lead time                        | Long -- includes design, tooling manufacture, T0/T1 samples, validation        |
| Inspection                       | Enhanced quality control -- validation of T0 and T1 samples                    |
| Samples                          | Mandatory -- T0 series (initial trials) then T1 (pre-production validation)    |
| Design phase                     | Design review, tooling drawings, technical validation before manufacture       |

---

## 4. Process Lines

| Code | Line              | Lead Role            | Main Function                                    |
|------|-------------------|----------------------|--------------------------------------------------|
| 01   | SALES             | Sales Role           | Sales management, customer relations, invoicing   |
| 02   | MANUFACTURE       | Purchasing Role      | Supplier coordination, production monitoring      |
| 03   | DELIVERY          | Logistics Role       | Transport, delivery, customs                      |
| 04   | QUALITY           | Quality Role         | Conformity control, quality validation            |

---

## 5. Adaptations by Block Compared to CHAIN-01

| Block  | Title                           | Adaptations Compared to CHAIN-01                                                                          |
|--------|---------------------------------|-------------------------------------------------------------------------------------------------------------|
| BLOCK 1| Order reception                 | Identification of order type: new tooling, collection of technical specifications                            |
| BLOCK 2| Order sheet                     | Mention of required new tooling, technical specifications, drawings, and tolerances                          |
| BLOCK 3| Transport sheet                 | Adjusted lead times for new tooling (+6-12 weeks vs. standard), possible transport of T0/T1 samples to customer for validation, series transport planning once T1 validated |
| BLOCK 4| Technical study with suppliers  | Feasibility study, tooling design, tooling quotation, validation plan, T0/T1 schedule                        |
| BLOCK 5| Order validation                | AR including tooling details, tooling costs, provisional T0/T1 schedule                                     |
| BLOCK 6| Production and quality          | Tooling manufacture, T0 trials, adjustments, T1 validation, then series production launch                    |
| BLOCK 7| Delivery & Customs              | Possible delivery of T1 samples to customer before series delivery, standard procedure for series delivery, documentation including T0/T1 validation reports, mention of tooling intellectual property in transport documents |
| BLOCK 8| Goods acceptance                | Enhanced control, complete dimensional report, validation of parts produced from new tooling                  |

---

## 6. Block Overview

```
BLOCK 1         BLOCK 2         BLOCK 3         BLOCK 4
Order           Order           Transport       Technical Study
Reception       Sheet           Sheet           + Tooling Design
[01 SALES]      [01 SALES]      [03 DELIVERY]   [02 MANUFACTURE]
    |               |               |               |
    v               v               v               v
BLOCK 5         BLOCK 6         BLOCK 7         BLOCK 8
Order           Production      Delivery        Goods
Validation      T0/T1 + Series  & Customs       Acceptance
[01 SALES]      [02 MANUF.      [03 DELIVERY    [04 QUALITY
                 04 QUALITY]     01 SALES]        01 SALES]
```

---

## 7. Tooling Design and Validation Phase

| Step                 | Description                                                          | Responsible     |
|----------------------|----------------------------------------------------------------------|-----------------|
| Design review        | Analysis of technical specifications, technical feasibility           | Purchasing Role |
| Tooling design       | Tooling drawings, material selection, technical validation            | Purchasing Role |
| Tooling manufacture  | Tooling production by the supplier                                    | Purchasing Role |
| T0 trials            | Initial trials, dimensional analysis, adjustments                     | Quality Role    |
| T1 validation        | Pre-production validation, complete conformity report                 | Quality Role    |
| Customer approval    | Sending T1 samples to customer for final validation                   | Sales Role      |

---

## 8. Tooling Intellectual Property

| Aspect                                    | Provision                                                                                       |
|-------------------------------------------|-------------------------------------------------------------------------------------------------|
| Tooling ownership                         | Tooling remains the property of the customer unless otherwise agreed                            |
| Confidentiality                           | Confidentiality clause on tooling drawings and specifications                                   |
| Storage and maintenance                   | Tooling storage and maintenance conditions at the supplier defined contractually                 |

Provisions relating to intellectual property must be formalized in the contract or purchase order before launching tooling design. The supplier commits not to use the tooling for third parties without written authorization from the customer owner.

---

## 9. Responsibility Matrix (RACI)

| Block  | Sales Role      | Purchasing Role | Logistics Role  | Quality Role |
|--------|-----------------|-----------------|-----------------|--------------|
| BLOCK 1| R/A             | I               | I               | I            |
| BLOCK 2| R/A             | C               | I               | C            |
| BLOCK 3| I               | C               | R/A             | I            |
| BLOCK 4| I               | R/A             | I               | C            |
| BLOCK 5| R/A             | C               | C               | C            |
| BLOCK 6| I               | R/A             | I               | R/A          |
| BLOCK 7| R               | I               | R/A             | I            |
| BLOCK 8| R               | I               | I               | R/A          |

**Legend**: R = Responsible, A = Accountable, C = Consulted, I = Informed

---

## 10. Key Performance Indicators (KPI)

| KPI                                           | Target                    | Measurement Frequency | Responsible        |
|-----------------------------------------------|---------------------------|-----------------------|--------------------|
| Tooling design and manufacture lead time       | <= contractual deadline   | Per order             | Purchasing Role    |
| T0 sample conformity rate                      | >= 80%                    | Per order             | Quality Role       |
| T1 sample conformity rate                      | >= 95%                    | Per order             | Quality Role       |
| Customer validation rate at first submission   | >= 85%                    | Per order             | Sales Role         |
| Customer complaint rate                        | <= 3%                     | Monthly               | Sales Role         |
| Supplier deadline compliance                   | >= 90%                    | Monthly               | Purchasing Role    |

---

## 11. Associated Documents

| Reference   | Document                                          |
|-------------|---------------------------------------------------|
| CHAIN-01    | Process Chain -- Existing Product Order            |
| CHAIN-02    | Process Chain -- Tooling Modification              |
| CH-BLOC-001 to CH-BLOC-008 | Block detail sheets (CHAIN-01 reference) |

---

## 12. Document Completeness

> All sections of this document have been completed in v0.7.

---

## Normative References

| ISO 9001:2015 Clause | Requirement                                                     |
|-----------------------|-----------------------------------------------------------------|
| 8.1                   | Operational planning and control                                 |
| 8.3                   | Design and development of products and services                  |
| 8.3.2                 | Design and development planning                                  |
| 8.3.4                 | Design and development controls                                  |
| 8.4                   | Control of externally provided processes, products and services  |
| 8.5.1                 | Control of production and service provision                      |

---

*Controlled document - Any printed copy is considered uncontrolled.*
*Plus Sarl - Quality Management System ISO 9001:2015 - v0.7*
