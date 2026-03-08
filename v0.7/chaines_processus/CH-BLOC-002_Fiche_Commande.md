# Block Detail Sheet - CH-BLOC-002: Order Sheet Creation

| **Document**       | CH-BLOC-002_Fiche_Commande                    |
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

This sheet describes the detailed actions of **BLOCK 2 — Order Sheet Creation** within the existing product order process chain.

---

## 2. Process Line

| Line Code  | Line      | Lead Role       |
|------------|-----------|-----------------|
| 01         | SALES     | SALES           |

---

## 3. Block Inputs

| Element                            | Source                         |
|------------------------------------|--------------------------------|
| Registered customer order          | BLOCK 1 — Order Reception      |
| File stored in ORDER_20XX          | BLOCK 1 — Order Reception      |
| Product library                    | Internal system                 |

---

## 4. Detailed Actions

| No.| Action                                                                                        | Owner           | Tool / Support                   |
|----|-----------------------------------------------------------------------------------------------|-----------------|----------------------------------|
| 1  | Create a new order sheet                                                                      | SALES           | Order management system          |
| 2  | Add the order as PDF under the PDF tab                                                        | SALES           | Order management system          |
| 3  | Download the order into the file                                                              | SALES           | Order management system          |
| 4  | Add the customer name, date, and deadline if applicable                                       | SALES           | Order management system          |
| 5  | Select the product name from the dropdown library                                             | SALES           | Product library                  |
| 6  | Add the ordered quantity and final quantity (identical)                                        | SALES           | Order management system          |
| 7  | Add the order reference, identical to the customer's reference                                | SALES           | Order management system          |

---

## 5. Order Sheet Fields

| Field                    | Description                                          | Mandatory   |
|--------------------------|------------------------------------------------------|-------------|
| Customer name            | Customer company name                                | Yes         |
| Order date               | Date the order was received                          | Yes         |
| Deadline                 | Delivery date requested by the customer              | If applicable|
| Product                  | Selection from the dropdown library                  | Yes         |
| Ordered quantity         | Number of units ordered                              | Yes         |
| Final quantity           | Identical to the ordered quantity                    | Yes         |
| Order reference          | Identical to the customer's reference                | Yes         |
| Order PDF                | Original customer order document                     | Yes         |

---

## 6. Block Outputs

| Element                          | Destination                      |
|----------------------------------|----------------------------------|
| Completed order sheet            | BLOCK 3 — Transport Sheet        |
| Completed order sheet            | BLOCK 4 — Technical Study        |
| Completed order sheet            | BLOCK 5 — Order Validation       |

---

## 7. Control Points

| Control                                        | Acceptance Criterion                                 | Owner           |
|------------------------------------------------|------------------------------------------------------|-----------------|
| All mandatory fields completed                 | No mandatory field left empty                         | SALES           |
| Order PDF attached                             | Document legible and complete                         | SALES           |
| Product correctly selected                     | Matches the customer order                            | SALES           |
| Order reference compliant                      | Identical to the customer's reference                 | SALES           |
| Quantities consistent                          | Ordered quantity = final quantity                      | SALES           |

---

## 8. Associated Documents

| Reference   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Process Chain — Existing Product Order         |
| CH-BLOC-001 | Detail Sheet — Order Reception                |
| CH-BLOC-003 | Detail Sheet — Transport Sheet                |

---

## Normative References

| ISO 9001:2015 Clause | Requirement                                           |
|-----------------------|-------------------------------------------------------|
| 8.2.2                 | Determination of requirements for products             |
| 8.2.3                 | Review of requirements for products                    |
| 7.5                   | Documented information                                 |

---

*Controlled document - Any printed copy is considered uncontrolled.*
*Plus Sàrl - Quality Management System ISO 9001:2015 - v0.7*
