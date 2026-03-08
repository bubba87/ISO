# Block Detail Sheet - CH-BLOC-008: Goods Acceptance

| **Document**       | CH-BLOC-008_Acceptation_Marchandise           |
|--------------------|-----------------------------------------------|
| **Version**        | v0.7                                          |
| **Date**           | 2026-03-04                                    |
| **Classification** | Internal                                      |
| **Process**        | Process Chain - Realization                   |
| **Chain ref.**     | CHAIN-01 — Existing Product Order             |
| **Drafted by**     | QUALITY                                       |
| **Approved by**    | Management                                    |

---

## 1. Purpose

This sheet describes the detailed actions of **BLOCK 8 — Goods Acceptance** within the existing product order process chain. This block involves two process lines: QUALITY and SALES.

---

## 2. Process Lines

| Line Code  | Line      | Lead Role       |
|------------|-----------|-----------------|
| 04         | QUALITY   | QUALITY         |
| 01         | SALES     | SALES           |

---

## 3. Block Inputs

| Element                            | Source                           |
|------------------------------------|----------------------------------|
| Delivered goods                    | BLOCK 7 — Delivery & Customs     |
| Delivery note                      | BLOCK 7 — Delivery & Customs     |
| Proof of delivery                  | BLOCK 7 — Delivery & Customs     |
| Quality control report             | BLOCK 6 — Production and Quality |

---

## 4. Detailed Actions

| No.| Action                                                                          | Line       | Owner           | Tool / Support                   |
|----|---------------------------------------------------------------------------------|------------|-----------------|----------------------------------|
| 1  | Confirmation email to the customer regarding goods conformity                    | 04 QUALITY | QUALITY         | Email                            |
| 2  | Send the invoice to the customer                                                | 01 SALES   | SALES           | Email / invoicing system         |
| 3  | Send the customs declaration to the customer if applicable                       | 01 SALES   | SALES           | Email                            |
| 4  | Customer payment                                                                | 01 SALES   | SALES           | Accounting system                |
| 5  | Close the file                                                                  | 01 SALES   | SALES           | Order management system          |

---

## 5. Documents Transmitted to the Customer

| Document                         | Sending Condition             | Owner           |
|----------------------------------|-------------------------------|-----------------|
| Conformity email                 | Systematic                    | QUALITY         |
| Invoice                          | Systematic                    | SALES           |
| Customs declaration              | If applicable (import/export) | SALES           |

---

## 6. File Closure Process

| Step                         | Description                                                  | Owner           |
|------------------------------|--------------------------------------------------------------|-----------------|
| Conformity confirmation      | Validation that the goods are compliant                       | QUALITY         |
| Invoicing                    | Issuance and sending of the invoice to the customer           | SALES           |
| Customs documents            | Sending of customs declaration if applicable                  | SALES           |
| Payment collection           | Follow-up and confirmation of customer payment                | SALES           |
| Closure                      | Administrative closure of the order file                      | SALES           |

---

## 7. Block Outputs

| Element                               | Destination            |
|---------------------------------------|------------------------|
| Conformity confirmation sent          | Customer               |
| Invoice sent                          | Customer               |
| Customs declaration sent              | Customer (if applicable)|
| Payment received                      | Accounting             |
| File closed                           | Archiving              |

---

## 8. Control Points

| Control                                      | Acceptance Criterion                               | Owner           |
|----------------------------------------------|-----------------------------------------------------|-----------------|
| Conformity confirmed to the customer         | Confirmation email sent                              | QUALITY         |
| Invoice sent                                 | Invoice compliant with the order and agreed prices   | SALES           |
| Customs declaration transmitted              | Complete and compliant document (if applicable)      | SALES           |
| Payment received                             | Amount compliant with the invoice, within deadlines  | SALES           |
| File complete and closed                     | All documents archived, status "closed"              | SALES           |

---

## 9. Associated Documents

| Reference   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Process Chain — Existing Product Order         |
| CH-BLOC-006 | Detail Sheet — Production and Quality         |
| CH-BLOC-007 | Detail Sheet — Delivery and Customs           |
| PR-P03-CQ   | Quality Control Process                       |
| FM-P03-NC   | Non-Conformity Report                         |
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
*Plus Sàrl - Quality Management System ISO 9001:2015 - v0.7*
