# Block Detail Sheet - CH-BLOC-008: Goods Acceptance

| **Document**       | CH-BLOC-008_Acceptation_Marchandise           |
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

This sheet describes the detailed actions of **BLOCK 8 -- Goods Acceptance** within the existing product order process chain. This block involves two process lines: QUALITY and SALES.

---

## 2. Process Lines

| Line Code  | Line      | Lead Role       |
|------------|-----------|-----------------|
| 04         | QUALITY   | Quality Role    |
| 01         | SALES     | Sales Role      |

---

## 3. Block Inputs

| Element                            | Source                           |
|------------------------------------|----------------------------------|
| Delivered goods                    | BLOCK 7 -- Delivery & Customs    |
| Delivery note                      | BLOCK 7 -- Delivery & Customs    |
| Proof of delivery                  | BLOCK 7 -- Delivery & Customs    |
| Quality control report             | BLOCK 6 -- Production and Quality|

---

## 4. Detailed Actions

| No. | Action                                                                          | Line       | Responsible     | Tool / Medium                    |
|-----|---------------------------------------------------------------------------------|------------|-----------------|----------------------------------|
| 1   | Confirmation e-mail to the customer regarding goods conformity                  | 04 QUALITY | Quality Role    | E-mail                           |
| 2   | Sending the invoice to the customer                                             | 01 SALES   | Sales Role      | E-mail / invoicing system        |
| 3   | Sending the customs declaration to the customer if applicable                   | 01 SALES   | Sales Role      | E-mail                           |
| 4   | Customer payment                                                                | 01 SALES   | Sales Role      | Accounting system                |
| 5   | File closure                                                                    | 01 SALES   | Sales Role      | Order management system          |

---

## 5. Documents Transmitted to the Customer

| Document                         | Sending Condition             | Responsible     |
|----------------------------------|-------------------------------|-----------------|
| Conformity e-mail                | Systematic                    | Quality Role    |
| Invoice                          | Systematic                    | Sales Role      |
| Customs declaration              | If applicable (import/export) | Sales Role      |

---

## 6. File Closure Process

| Step                         | Description                                                  | Responsible     |
|------------------------------|--------------------------------------------------------------|-----------------|
| Conformity confirmation      | Validation that goods are compliant                           | Quality Role    |
| Invoicing                    | Issuance and sending of the invoice to the customer           | Sales Role      |
| Customs documents            | Sending the customs declaration if applicable                 | Sales Role      |
| Collection                   | Follow-up and confirmation of customer payment                | Sales Role      |
| Closure                      | Administrative closure of the order file                      | Sales Role      |

---

## 7. Block Outputs

| Element                               | Destination           |
|---------------------------------------|-----------------------|
| Conformity confirmation sent          | Customer              |
| Invoice sent                          | Customer              |
| Customs declaration sent              | Customer (if applicable)|
| Payment received                      | Accounting            |
| File closed                           | Archiving             |

---

## 8. Control Points

| Control                                      | Acceptance Criterion                               | Responsible     |
|----------------------------------------------|----------------------------------------------------|-----------------|
| Conformity confirmed to the customer         | Confirmation e-mail sent                            | Quality Role    |
| Invoice sent                                 | Invoice compliant with the order and agreed prices   | Sales Role      |
| Customs declaration transmitted              | Document complete and compliant (if applicable)      | Sales Role      |
| Payment received                             | Amount compliant with the invoice, within deadlines   | Sales Role      |
| File complete and closed                     | All documents archived, status "closed"              | Sales Role      |

---

## 9. Associated Documents

| Reference   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Process Chain -- Existing Product Order        |
| CH-BLOC-006 | Detail Sheet -- Production and Quality        |
| CH-BLOC-007 | Detail Sheet -- Delivery and Customs          |
| PR-P03-CQ   | Quality Control Process                       |
| FM-P03-NC   | Nonconformity Report                          |
| FM-P01-SAT  | Customer Satisfaction Survey                  |

---

## Normative References

| ISO 9001:2015 Clause | Requirement                                           |
|-----------------------|-------------------------------------------------------|
| 8.6                   | Release of products and services                       |
| 8.2.1                 | Customer communication                                 |
| 7.5                   | Documented information                                 |
| 9.1.2                 | Customer satisfaction                                  |

---

*Controlled document - Any printed copy is considered uncontrolled.*
*Plus Sarl - Quality Management System ISO 9001:2015 - v0.7*
