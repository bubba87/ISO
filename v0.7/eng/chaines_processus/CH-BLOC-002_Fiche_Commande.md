# Block Detail Sheet - CH-BLOC-002: Order Sheet Creation

| **Document**       | CH-BLOC-002_Fiche_Commande                    |
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

This sheet describes the detailed actions of **BLOCK 2 -- Order Sheet Creation** within the existing product order process chain.

---

## 2. Process Line

| Line Code  | Line      | Lead Role       |
|------------|-----------|-----------------|
| 01         | SALES     | Sales Role      |

---

## 3. Block Inputs

| Element                            | Source                         |
|------------------------------------|--------------------------------|
| Registered customer order          | BLOCK 1 -- Order Reception     |
| File stored in ORDER_20XX          | BLOCK 1 -- Order Reception     |
| Product library                    | Internal system                |

---

## 4. Detailed Actions

| No. | Action                                                                                        | Responsible     | Tool / Medium                    |
|-----|-----------------------------------------------------------------------------------------------|-----------------|----------------------------------|
| 1   | Create a new order sheet                                                                      | Sales Role      | Order management system          |
| 2   | Add the order as PDF under the PDF tab                                                        | Sales Role      | Order management system          |
| 3   | Download the order under the file                                                             | Sales Role      | Order management system          |
| 4   | Add the customer name, date, and deadline if applicable                                       | Sales Role      | Order management system          |
| 5   | Select the product name from the dropdown library                                             | Sales Role      | Product library                  |
| 6   | Add the ordered quantity and final quantity (identical)                                        | Sales Role      | Order management system          |
| 7   | Add the order reference, identical to the customer's reference                                | Sales Role      | Order management system          |

---

## 5. Order Sheet Fields

| Field                    | Description                                          | Mandatory   |
|--------------------------|------------------------------------------------------|-------------|
| Customer name            | Customer's company name                              | Yes         |
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
| Completed order sheet            | BLOCK 3 -- Transport Sheet       |
| Completed order sheet            | BLOCK 4 -- Technical Study       |
| Completed order sheet            | BLOCK 5 -- Order Validation      |

---

## 7. Control Points

| Control                                        | Acceptance Criterion                                 | Responsible     |
|------------------------------------------------|------------------------------------------------------|-----------------|
| All mandatory fields completed                 | No mandatory field left empty                         | Sales Role      |
| Order PDF attached                             | Document legible and complete                         | Sales Role      |
| Product correctly selected                     | Matches the customer order                            | Sales Role      |
| Order reference compliant                      | Identical to the customer's reference                 | Sales Role      |
| Quantities consistent                          | Ordered quantity = final quantity                      | Sales Role      |

---

## 8. Associated Documents

| Reference   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Process Chain -- Existing Product Order        |
| CH-BLOC-001 | Detail Sheet -- Order Reception               |
| CH-BLOC-003 | Detail Sheet -- Transport Sheet               |

---

## Normative References

| ISO 9001:2015 Clause | Requirement                                           |
|-----------------------|-------------------------------------------------------|
| 8.2.2                 | Determining the requirements for products              |
| 8.2.3                 | Review of the requirements for products                |
| 7.5                   | Documented information                                 |

---

*Controlled document - Any printed copy is considered uncontrolled.*
*Plus Sarl - Quality Management System ISO 9001:2015 - v0.7*
