# Block Detail Sheet - CH-BLOC-005: Order Validation

| **Document**       | CH-BLOC-005_Validation_Commande               |
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

This sheet describes the detailed actions of **BLOCK 5 — Order Validation** within the existing product order process chain.

---

## 2. Process Line

| Line Code  | Line      | Lead Role       |
|------------|-----------|-----------------|
| 01         | SALES     | SALES           |

---

## 3. Block Inputs

| Element                            | Source                            |
|------------------------------------|-----------------------------------|
| Completed order sheet              | BLOCK 2 — Order Sheet             |
| Validated delivery deadlines       | BLOCK 3 — Transport Sheet         |
| Validated production lead times    | BLOCK 4 — Technical Study         |
| Price per product                  | Commercial management system      |

---

## 4. Detailed Actions

| No.| Action                                                                                          | Owner           | Tool / Support                   |
|----|-------------------------------------------------------------------------------------------------|-----------------|----------------------------------|
| 1  | Print the acknowledgment of receipt (AR) to prepare for sending and validate with the customer  | SALES           | Order management system          |
| 2  | Send the AR to the customer with delivery details and price per product                         | SALES           | Email                            |
| 3  | Customer feedback if necessary: acceptance or rejection                                         | SALES           | Email / phone                    |

---

## 5. Acknowledgment of Receipt (AR) Content

| Element                        | Description                                         |
|--------------------------------|-----------------------------------------------------|
| Order reference                | Identical to the customer's reference                |
| Product details                | Description, ordered quantities                      |
| Price per product              | Unit price and total amount                          |
| Delivery deadlines             | Validated estimated delivery date                    |
| Delivery conditions            | Transport type, incoterms                            |
| Payment terms                  | Agreed payment conditions                            |

---

## 6. Customer Response Scenarios

| Customer Response | Next Action                                                        |
|-------------------|--------------------------------------------------------------------|
| Acceptance        | Proceed to BLOCK 6 — Production Confirmation                      |
| Rejection         | Analysis of reasons, offer adjustment or file closure              |
| Modification      | Update of the order sheet, new AR if necessary                     |

---

## 7. Block Outputs

| Element                               | Destination                      |
|---------------------------------------|----------------------------------|
| AR sent and validated by the customer | BLOCK 6 — Production and Quality |
| Order confirmed                       | BLOCK 6 — Production and Quality |
| File closed (in case of rejection)    | Archiving                        |

---

## 8. Control Points

| Control                                    | Acceptance Criterion                                  | Owner           |
|--------------------------------------------|-------------------------------------------------------|-----------------|
| AR complete and compliant                  | All required elements present                          | SALES           |
| Prices and deadlines consistent            | Consistent with BLOCK 3 and BLOCK 4 validations        | SALES           |
| Customer response recorded                 | Formal customer response (acceptance/rejection/modification) | SALES      |

---

## 9. Associated Documents

| Reference   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Process Chain — Existing Product Order         |
| CH-BLOC-003 | Detail Sheet — Transport Sheet                |
| CH-BLOC-004 | Detail Sheet — Technical Study                |
| CH-BLOC-006 | Detail Sheet — Production and Quality         |

---

## Normative References

| ISO 9001:2015 Clause | Requirement                                           |
|-----------------------|-------------------------------------------------------|
| 8.2.3                 | Review of requirements for products                    |
| 8.2.1                 | Customer communication                                 |

---

*Controlled document - Any printed copy is considered uncontrolled.*
*Plus Sàrl - Quality Management System ISO 9001:2015 - v0.7*
