# Process Chain - CHAIN-04: Sourcing Order

| **Document**       | CHAIN-04_Commande_Sourcing                   |
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

This document describes the process chain for handling an **order requiring a sourcing phase**. This chain follows the 8-block structure of CHAIN-01 (Existing Product) with specific adaptations related to the search, evaluation, and qualification of a new supplier.

---

## 2. Scope

This chain applies to any customer order for which no qualified supplier is yet referenced for the requested product. The supplier search is conducted on a global scale, regardless of geographical location.

---

## 3. Specificities of the "Sourcing" Chain

| Characteristic                   | Description                                                                          |
|----------------------------------|--------------------------------------------------------------------------------------|
| Development phase                | Variable -- depending on whether the product exists or requires development           |
| Supplier evaluation              | To be performed -- search, evaluation, and qualification of a new supplier            |
| Tooling                          | Variable -- depending on the identified supplier (existing, to be modified, or to be created) |
| Lead time                        | Longest -- includes sourcing, qualification, and validation phase                     |
| Inspection                       | Enhanced quality control -- first production with a new supplier                      |
| Supplier qualification           | Supplier audit, capability assessment, validation samples                             |

---

## 4. Process Lines

| Code | Line              | Lead Role            | Main Function                                    |
|------|-------------------|----------------------|--------------------------------------------------|
| 01   | SALES             | Sales Role           | Sales management, customer relations, invoicing   |
| 02   | MANUFACTURE       | Purchasing Role      | Supplier coordination, production monitoring      |
| 03   | DELIVERY          | Logistics Role       | Transport, delivery, customs                      |
| 04   | QUALITY           | Quality Role         | Conformity control, quality validation            |

---

## 5. Sourcing and Supplier Qualification Phase

| Step                             | Description                                                            | Responsible        |
|----------------------------------|------------------------------------------------------------------------|--------------------|
| Needs analysis                   | Definition of technical requirements, volumes, deadlines               | Sales Role         |
| Supplier search                  | Identification of potential suppliers on a global scale                 | Purchasing Role    |
| Request for quotation            | Sending of technical specifications, collection of offers              | Purchasing Role    |
| Comparative evaluation           | Analysis of quality, cost, lead time, production capacity              | Purchasing Role    |
| Supplier audit                   | On-site visit, evaluation of the supplier's quality system             | Quality Role       |
| Validation samples               | Request and control of initial samples                                  | Quality Role       |
| Supplier qualification           | Referencing decision, update of the supplier panel                     | Purchasing Role    |
| Management approval              | Final approval of the new supplier by management                       | Management         |

---

## 6. Supplier Selection Criteria and Audit Process

### 6.1 Selection Criteria Grid

| Criterion                | Weighting   | Description                                                                 |
|--------------------------|-------------|-----------------------------------------------------------------------------|
| Quality                  | 25%         | Quality system, certifications (ISO 9001, IATF, etc.), quality history      |
| Cost                     | 20%         | Price competitiveness, transparency of cost structure                        |
| Lead time                | 20%         | Ability to meet required deadlines, responsiveness                           |
| Production capacity      | 15%         | Production resources, ability to absorb requested volumes                    |
| Certifications           | 10%         | Sector-specific certifications, environmental standards                      |
| CSR                      | 10%         | Corporate social responsibility, working conditions, environmental impact    |

### 6.2 Qualification

- **Minimum score for qualification**: 70/100
- The score is calculated based on the criteria grid above, with each criterion rated out of 100 then weighted.
- A supplier not reaching the minimum score cannot be referenced unless a derogation is approved by Management.

### 6.3 Audit Process

- **Mandatory on-site audit** for any order exceeding the threshold defined by Management.
- The audit covers: quality system, production resources, nonconformity management, traceability, working conditions.
- An audit report is formalized and archived. Identified deviations are subject to a corrective action plan with follow-up.
- For orders below the threshold, a remote documentary audit may be accepted subject to Quality Role approval.

---

## 7. Adaptations by Block Compared to CHAIN-01

| Block  | Title                           | Adaptations Compared to CHAIN-01                                                                          |
|--------|---------------------------------|-------------------------------------------------------------------------------------------------------------|
| BLOCK 1| Order reception                 | Identification of order type: sourcing required, preliminary needs analysis                                  |
| BLOCK 2| Order sheet                     | Mention "sourcing in progress," complete technical specifications                                            |
| BLOCK 3| Transport sheet                 | Provisional lead times to be adjusted based on sourcing results, establishment of new logistics routes with selected supplier, verification of customs constraints specific to the country of origin |
| BLOCK 4| Technical study with suppliers  | Complete sourcing phase: search, evaluation, audit, qualification, then standard technical study              |
| BLOCK 5| Order validation                | AR including sourcing results, presentation of selected supplier, provisional schedule                       |
| BLOCK 6| Production and quality          | First production with new supplier, enhanced quality control, PPAP if applicable                             |
| BLOCK 7| Delivery & Customs              | Establishment of logistics routes with the new supplier, logistics route testing on first shipment, complete documentation for new supply corridor, verification of specific customs procedures |
| BLOCK 8| Goods acceptance                | Enhanced control on first delivery, lessons learned, supplier evaluation update                               |

---

## 8. Block Overview

```
           +------------------------------+
           |  PRELIMINARY PHASE: SOURCING |
           |  Supplier Search &           |
           |  Qualification               |
           +--------------+---------------+
                          v
BLOCK 1         BLOCK 2         BLOCK 3         BLOCK 4
Order           Order           Transport       Technical Study
Reception       Sheet           Sheet           with Suppliers
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

| KPI                                            | Target                    | Measurement Frequency | Responsible        |
|------------------------------------------------|---------------------------|-----------------------|--------------------|
| Average sourcing and qualification lead time    | <= contractual deadline   | Per order             | Purchasing Role    |
| Number of suppliers evaluated per sourcing       | >= 3                      | Per order             | Purchasing Role    |
| Initial sample conformity rate                  | >= 90%                    | Per order             | Quality Role       |
| First audit qualification rate                  | >= 70%                    | Semi-annual           | Quality Role       |
| Customer complaint rate                         | <= 3%                     | Monthly               | Sales Role         |
| Supplier deadline compliance                    | >= 90%                    | Monthly               | Purchasing Role    |

---

## 11. Associated Documents

| Reference   | Document                                          |
|-------------|---------------------------------------------------|
| CHAIN-01    | Process Chain -- Existing Product Order            |
| CHAIN-02    | Process Chain -- Tooling Modification              |
| CHAIN-03    | Process Chain -- New Tooling                       |
| CH-BLOC-001 to CH-BLOC-008 | Block detail sheets (CHAIN-01 reference) |

---

## 12. Document Completeness

> All sections of this document have been completed in v0.7.

---

## Normative References

| ISO 9001:2015 Clause | Requirement                                                     |
|-----------------------|-----------------------------------------------------------------|
| 8.1                   | Operational planning and control                                 |
| 8.4                   | Control of externally provided processes, products and services  |
| 8.4.1                 | General -- type and extent of control                            |
| 8.4.2                 | Type and extent of control                                       |
| 8.4.3                 | Information for external providers                               |

---

*Controlled document - Any printed copy is considered uncontrolled.*
*Plus Sarl - Quality Management System ISO 9001:2015 - v0.7*
