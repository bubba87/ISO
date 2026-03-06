# Process Chain - CHAIN-02: Tooling Modification Order

| **Document**       | CHAIN-02_Commande_Modification_Outillage    |
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

This document describes the process chain for handling an **order requiring modification of existing tooling**. This chain follows the 8-block structure of CHAIN-01 (Existing Product) with specific adaptations related to the technical tooling modification phase.

---

## 2. Scope

This chain applies to any customer order involving the modification of tooling already existing at a qualified supplier, regardless of the geographical location of the customer or the supplier.

---

## 3. Specificities of the "Tooling Modification" Chain

| Characteristic                   | Description                                                              |
|----------------------------------|--------------------------------------------------------------------------|
| Development phase                | Partial -- technical modification of existing tooling                    |
| Supplier evaluation              | Already completed -- supplier qualified and referenced                   |
| Tooling                          | Existing but requiring modification according to new requirements        |
| Lead time                        | Intermediate -- includes modification and validation phase               |
| Inspection                       | Enhanced quality control -- validation of modifications made             |
| Samples                          | Possible validation of post-modification samples                         |

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

| Block  | Title                           | Adaptations Compared to CHAIN-01                                                                  |
|--------|---------------------------------|---------------------------------------------------------------------------------------------------|
| BLOCK 1| Order reception                 | Identification of order type: tooling modification                                                |
| BLOCK 2| Order sheet                     | Mention of required modification, reference to existing tooling                                   |
| BLOCK 3| Transport sheet                 | Adjusted lead times for tooling modification (+2-4 weeks vs. standard), coordination of post-modification sample transport if necessary, final transport planning once modification validated |
| BLOCK 4| Technical study with suppliers  | Feasibility study of the modification, tooling modification quotation, technical validation        |
| BLOCK 5| Order validation                | AR including modification details, potential additional costs                                      |
| BLOCK 6| Production and quality          | Tooling modification phase, post-modification sample validation, then series production            |
| BLOCK 7| Delivery & Customs              | Standard delivery procedure with adjusted lead times (+1-2 weeks), possible shipment of post-modification samples to customer before series delivery, specific documentation mentioning tooling modification |
| BLOCK 8| Goods acceptance                | Enhanced control on parts produced from modified tooling                                           |

---

## 6. Block Overview

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

| Block  | Sales Role      | Purchasing Role | Logistics Role  | Quality Role |
|--------|-----------------|-----------------|-----------------|--------------|
| BLOCK 1| R/A             | I               | I               | I            |
| BLOCK 2| R/A             | C               | I               | I            |
| BLOCK 3| I               | C               | R/A             | I            |
| BLOCK 4| I               | R/A             | I               | C            |
| BLOCK 5| R/A             | C               | C               | C            |
| BLOCK 6| I               | R/A             | I               | R/A          |
| BLOCK 7| R               | I               | R/A             | I            |
| BLOCK 8| R               | I               | I               | R/A          |

**Legend**: R = Responsible, A = Accountable, C = Consulted, I = Informed

---

## 8. Key Performance Indicators (KPI)

| KPI                                          | Target                    | Measurement Frequency | Responsible        |
|----------------------------------------------|---------------------------|-----------------------|--------------------|
| Tooling modification lead time               | <= contractual deadline   | Per order             | Purchasing Role    |
| Post-modification sample conformity rate     | >= 95%                    | Per order             | Quality Role       |
| Customer complaint rate                      | <= 3%                     | Monthly               | Sales Role         |
| Supplier deadline compliance                 | >= 90%                    | Monthly               | Purchasing Role    |

---

## 9. Associated Documents

| Reference   | Document                                          |
|-------------|---------------------------------------------------|
| CHAIN-01    | Process Chain -- Existing Product Order            |
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
*Plus Sarl - Quality Management System ISO 9001:2015 - v0.7*
