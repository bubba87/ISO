# Process Chain - CHAIN-02: Tooling Modification Order

| **Document**       | CHAIN-02_Commande_Modification_Outillage    |
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

This document describes the process chain for handling an **order requiring modification of existing tooling**. This chain follows the 8-block structure of CHAIN-01 (Existing Product) with specific adaptations related to the technical tooling modification phase.

---

## 2. Scope

This chain applies to any customer order involving the modification of tooling already existing at a qualified supplier, regardless of the geographic location of the customer or supplier.

---

## 3. Specifics of the "Tooling Modification" Chain

| Characteristic                   | Description                                                              |
|----------------------------------|--------------------------------------------------------------------------|
| Development phase                | Partial — technical modification of existing tooling                     |
| Supplier evaluation              | Already completed — supplier qualified and referenced                    |
| Tooling                          | Existing but requiring modification per new requirements                 |
| Lead time                        | Intermediate — includes modification and validation phase                |
| Inspection                       | Enhanced quality control — validation of modifications made              |
| Samples                          | Possible validation of post-modification samples                         |

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

| Block  | Title                           | Adaptations Compared to CHAIN-01                                                                  |
|--------|---------------------------------|---------------------------------------------------------------------------------------------------|
| BLOCK 1| Order reception                 | Identification of order type: tooling modification                                                |
| BLOCK 2| Order sheet                     | Mention of required modification, reference to existing tooling                                   |
| BLOCK 3| Transport sheet                 | Adjusted lead times for tooling modification (+2-4 weeks vs. standard), coordination of post-modification sample transport if necessary, final transport planning once modification is validated |
| BLOCK 4| Technical study with suppliers  | Feasibility study of the modification, tooling modification quote, technical validation            |
| BLOCK 5| Order validation                | AR including modification details, potential additional costs                                      |
| BLOCK 6| Production and quality          | Tooling modification phase, post-modification sample validation, then series production            |
| BLOCK 7| Delivery & Customs              | Standard delivery procedure with adjusted lead times (+1-2 weeks), possible shipment of post-modification samples to the customer before series delivery, specific documentation mentioning tooling modification |
| BLOCK 8| Goods acceptance                | Enhanced control on parts produced from the modified tooling                                       |

---

## 6. Overview of the Blocks

```
BLOCK 1         BLOCK 2         BLOCK 3         BLOCK 4
Order           Order           Transport       Technical Study
Reception       Sheet           Sheet           + Modification
[01 SALES]      [01 SALES]      [03 DELIVERY]   [02 MANUFACTURE]
    |               |               |               |
    v               v               v               v
BLOCK 5         BLOCK 6         BLOCK 7         BLOCK 8
Order           Production      Delivery        Goods
Validation      & Quality       & Customs       Acceptance
[01 SALES]      [02 MANUF.      [03 DELIVERY    [04 QUALITY
                 04 QUALITY]     01 SALES]        01 SALES]
```

---

## 7. Responsibility Matrix (RACI)

| Block  | SALES           | MANUFACTURE | DELIVERY        | QUALITY      |
|--------|-----------------|-------------|-----------------|--------------|
| BLOCK 1| R/A             | I           | I               | I            |
| BLOCK 2| R/A             | C           | I               | I            |
| BLOCK 3| I               | C           | R/A             | I            |
| BLOCK 4| I               | R/A         | I               | C            |
| BLOCK 5| R/A             | C           | C               | C            |
| BLOCK 6| I               | R/A         | I               | R/A          |
| BLOCK 7| R               | I           | R/A             | I            |
| BLOCK 8| R               | I           | I               | R/A          |

**Legend**: R = Responsible, A = Approver, C = Consulted, I = Informed

---

## 8. Key Performance Indicators (KPI)

| KPI                                          | Target                    | Measurement Frequency | Owner              |
|----------------------------------------------|---------------------------|----------------------|--------------------|
| Tooling modification lead time               | ≤ contractual deadline    | Per order            | MANUFACTURE        |
| Post-modification sample conformity rate     | ≥ 95%                    | Per order            | QUALITY            |
| Customer complaint rate                      | ≤ 3%                     | Monthly              | SALES              |
| Supplier deadline compliance                 | ≥ 90%                    | Monthly              | MANUFACTURE        |

---

## 9. Associated Documents

| Reference   | Document                                          |
|-------------|---------------------------------------------------|
| CHAIN-01    | Process Chain — Existing Product Order             |
| CH-BLOC-001 to CH-BLOC-008 | Block detail sheets (CHAIN-01 reference) |

---

## 10. Document Completeness

> All sections of this document have been completed in v0.7.

---

## Normative References

| ISO 9001:2015 Clause | Requirement                                                     |
|-----------------------|-----------------------------------------------------------------|
| 8.1                   | Operational planning and control                                 |
| 8.3                   | Design and development of products and services                  |
| 8.4                   | Control of externally provided processes, products and services  |
| 8.5.1                 | Control of production and service provision                      |

---

*Controlled document - Any printed copy is considered uncontrolled.*
*Plus Sàrl - Quality Management System ISO 9001:2015 - v0.7*
