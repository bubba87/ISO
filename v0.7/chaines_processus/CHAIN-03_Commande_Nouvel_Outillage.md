# Process Chain - CHAIN-03: New Tooling Order

| **Document**       | CHAIN-03_Commande_Nouvel_Outillage           |
|--------------------|----------------------------------------------|
| **Version**        | v0.7                                         |
| **Date**           | 2026-03-04                                   |
| **Classification** | Internal                                     |
| **Status**         | **Active**                                   |
| **Process**        | Process Chain - Realization                  |
| **Drafted by**     | QUALITY                                      |
| **Approved by**    | Management                                   |

---

## 1. Purpose

This document describes the process chain for handling an **order requiring the creation of new tooling**. This chain follows the 8-block structure of CHAIN-01 (Existing Product) with specific adaptations related to the design, tooling manufacture, and sample validation (T0/T1) phases.

---

## 2. Scope

This chain applies to any customer order involving the design and manufacture of new tooling at a qualified supplier, regardless of the geographic location of the customer or supplier.

---

## 3. Specifics of the "New Tooling" Chain

| Characteristic                   | Description                                                                    |
|----------------------------------|--------------------------------------------------------------------------------|
| Development phase                | Complete — design and manufacture of new tooling                               |
| Supplier evaluation              | Already completed — supplier qualified and referenced                          |
| Tooling                          | New — design, manufacture, setup, and validation required                      |
| Lead time                        | Long — includes design, tooling manufacture, T0/T1 samples, validation         |
| Inspection                       | Enhanced quality control — validation of T0 and T1 samples                     |
| Samples                          | Mandatory — T0 series (initial trials) then T1 (pre-production validation)     |
| Design phase                     | Design review, tooling drawings, technical validation before manufacture       |

---

## 4. Process Lines

| Code | Line              | Lead Role            | Main Function                                    |
|------|-------------------|----------------------|--------------------------------------------------|
| 01   | SALES             | SALES                | Commercial management, customer relations, invoicing |
| 02   | MANUFACTURE       | MANUFACTURE          | Supplier coordination, production monitoring      |
| 03   | DELIVERY          | DELIVERY             | Transport, delivery, customs                      |
| 04   | QUALITY           | QUALITY              | Compliance control, quality validation            |

---

## 5. Adaptations per Block Compared to CHAIN-01

| Block  | Title                           | Adaptations Compared to CHAIN-01                                                                          |
|--------|---------------------------------|-------------------------------------------------------------------------------------------------------------|
| BLOCK 1| Order reception                 | Identification of order type: new tooling, collection of technical specifications                            |
| BLOCK 2| Order sheet                     | Mention of new tooling required, technical specifications, drawings, and tolerances                           |
| BLOCK 3| Transport sheet                 | Adjusted lead times for new tooling (+6-12 weeks vs. standard), possible transport of T0/T1 samples to the customer for validation, series transport planning once T1 is validated |
| BLOCK 4| Technical study with suppliers  | Feasibility study, tooling design, tooling quote, validation plan, T0/T1 schedule                            |
| BLOCK 5| Order validation                | AR including tooling details, tooling costs, provisional T0/T1 schedule                                      |
| BLOCK 6| Production and quality          | Tooling manufacture, T0 trials, adjustments, T1 validation, then series production launch                     |
| BLOCK 7| Delivery & Customs              | Possible delivery of T1 samples to the customer before series delivery, standard procedure for series delivery, documentation including T0/T1 validation reports, mention of tooling intellectual property in transport documents |
| BLOCK 8| Goods acceptance                | Enhanced control, full dimensional report, validation of parts produced from the new tooling                  |

---

## 6. Overview of the Blocks

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

| Step                 | Description                                                          | Owner           |
|----------------------|----------------------------------------------------------------------|-----------------|
| Design review        | Requirements analysis, technical feasibility                          | MANUFACTURE     |
| Tooling design       | Tooling drawings, material selection, technical validation            | MANUFACTURE     |
| Tooling manufacture  | Tooling production by the supplier                                    | MANUFACTURE     |
| T0 trials            | Initial trials, dimensional analysis, adjustments                     | QUALITY         |
| T1 validation        | Pre-production validation, full conformity report                     | QUALITY         |
| Customer approval    | T1 sample shipment to the customer for final validation               | SALES           |

---

## 8. Tooling Intellectual Property

| Aspect                                    | Provision                                                                                       |
|-------------------------------------------|-------------------------------------------------------------------------------------------------|
| Tooling ownership                         | The tooling remains the property of the customer unless otherwise agreed                        |
| Confidentiality                           | Confidentiality clause on tooling drawings and specifications                                   |
| Storage and maintenance                   | Tooling storage and maintenance conditions at the supplier's premises defined contractually     |

Intellectual property provisions must be formalized in the contract or purchase order before tooling design is initiated. The supplier commits not to use the tooling for third parties without written authorization from the tooling owner.

---

## 9. Responsibility Matrix (RACI)

| Block  | SALES           | MANUFACTURE | DELIVERY        | QUALITY      |
|--------|-----------------|-------------|-----------------|--------------|
| BLOCK 1| R/A             | I           | I               | I            |
| BLOCK 2| R/A             | C           | I               | C            |
| BLOCK 3| I               | C           | R/A             | I            |
| BLOCK 4| I               | R/A         | I               | C            |
| BLOCK 5| R/A             | C           | C               | C            |
| BLOCK 6| I               | R/A         | I               | R/A          |
| BLOCK 7| R               | I           | R/A             | I            |
| BLOCK 8| R               | I           | I               | R/A          |

**Legend**: R = Responsible, A = Approver, C = Consulted, I = Informed

---

## 10. Key Performance Indicators (KPI)

| KPI                                           | Target                    | Measurement Frequency | Owner              |
|-----------------------------------------------|---------------------------|----------------------|--------------------|
| Tooling design and manufacture lead time       | ≤ contractual deadline    | Per order            | MANUFACTURE        |
| T0 sample conformity rate                      | ≥ 80%                    | Per order            | QUALITY            |
| T1 sample conformity rate                      | ≥ 95%                    | Per order            | QUALITY            |
| Customer validation rate at first submission    | ≥ 85%                    | Per order            | SALES              |
| Customer complaint rate                        | ≤ 3%                     | Monthly              | SALES              |
| Supplier deadline compliance                   | ≥ 90%                    | Monthly              | MANUFACTURE        |

---

## 11. Associated Documents

| Reference   | Document                                          |
|-------------|---------------------------------------------------|
| CHAIN-01    | Process Chain — Existing Product Order             |
| CHAIN-02    | Process Chain — Tooling Modification               |
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
*Plus Sàrl - Quality Management System ISO 9001:2015 - v0.7*
