# Block Detail Sheet - CH-BLOC-006: Production and Quality

| **Document**       | CH-BLOC-006_Production_Qualite                |
|--------------------|-----------------------------------------------|
| **Version**        | v0.7                                          |
| **Date**           | 2026-03-04                                    |
| **Classification** | Internal                                      |
| **Process**        | Process Chain - Realization                   |
| **Chain ref.**     | CHAIN-01 -- Existing Product Order            |
| **Drafted by**     | Quality Role                                  |
| **Approved by**    | Management                                    |

---

## 1. Purpose

This sheet describes the detailed actions of **BLOCK 6 -- Production and Quality** within the existing product order process chain. This block involves two process lines: MANUFACTURE and QUALITY.

---

## 2. Process Lines

| Line Code  | Line           | Lead Role        |
|------------|----------------|------------------|
| 02         | MANUFACTURE    | Purchasing Role  |
| 04         | QUALITY        | Quality Role     |

---

## 3. Block Inputs

| Element                            | Source                          |
|------------------------------------|---------------------------------|
| Order validated by the customer    | BLOCK 5 -- Order Validation     |
| Product specifications             | Product library                 |
| Supplier information               | BLOCK 4 -- Technical Study      |

---

## 4. Detailed Actions

| No. | Action                                                                                                      | Line           | Responsible      | Tool / Medium         |
|-----|-------------------------------------------------------------------------------------------------------------|----------------|------------------|-----------------------|
| 1   | Send the production confirmation to the supplier (e-mail or messaging)                                       | 02 MANUFACTURE | Purchasing Role  | E-mail / messaging    |
| 2   | Validation of parts conformity by the supplier following quality control                                     | 04 QUALITY     | Quality Role     | Control report        |

---

## 5. Quality Control Process

| Step                         | Description                                                  | Responsible      |
|------------------------------|--------------------------------------------------------------|------------------|
| Supplier control             | The supplier performs quality control according to specifications | Supplier      |
| Control report               | The supplier transmits the quality control report             | Supplier         |
| Conformity validation        | Review of the report and conformity validation                | Quality Role     |
| Production release           | Authorization to ship if conformity is validated              | Quality Role     |

---

## 6. Block Outputs

| Element                                | Destination                    |
|----------------------------------------|--------------------------------|
| Production confirmation sent           | Supplier                       |
| Parts conformity validated             | BLOCK 7 -- Delivery & Customs  |
| Quality control report                 | Quality archiving              |

---

## 7. Control Points

| Control                                           | Acceptance Criterion                             | Responsible      |
|---------------------------------------------------|--------------------------------------------------|------------------|
| Production confirmation sent                      | Acknowledgment of receipt from the supplier       | Purchasing Role  |
| Quality control report received                   | Report complete and compliant with specifications | Quality Role     |
| Parts conformity validated                        | All parts compliant with requirements             | Quality Role     |

---

## 8. Associated Documents

| Reference   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Process Chain -- Existing Product Order        |
| CH-BLOC-005 | Detail Sheet -- Order Validation              |
| CH-BLOC-007 | Detail Sheet -- Delivery and Customs          |
| PR-P03-CQ   | Quality Control Process                       |
| FM-P03-IPC  | IPC Report                                    |
| FM-P03-DUPRO| DUPRO Report                                  |
| FM-P03-PSI  | PSI Report                                    |
| FM-P03-LC   | Loading Check Report                          |
| FM-P03-NC   | Nonconformity Report                          |
| IT-P03-ECH  | AQL Sampling Instruction                      |

---

## Normative References

| ISO 9001:2015 Clause | Requirement                                              |
|-----------------------|----------------------------------------------------------|
| 8.4                   | Control of externally provided processes, products and services |
| 8.5.1                 | Control of production and service provision                |
| 8.6                   | Release of products and services                          |

---

*Controlled document - Any printed copy is considered uncontrolled.*
*Plus Sarl - Quality Management System ISO 9001:2015 - v0.7*
