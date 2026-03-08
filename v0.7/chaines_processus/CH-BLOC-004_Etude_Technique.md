# Block Detail Sheet - CH-BLOC-004: Technical Study with Suppliers

| **Document**       | CH-BLOC-004_Etude_Technique                   |
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

This sheet describes the detailed actions of **BLOCK 4 — Technical Study with Suppliers** within the existing product order process chain.

---

## 2. Process Line

| Line Code  | Line           | Lead Role     |
|------------|----------------|---------------|
| 02         | MANUFACTURE    | MANUFACTURE   |

---

## 3. Block Inputs

| Element                            | Source                         |
|------------------------------------|--------------------------------|
| Completed order sheet              | BLOCK 2 — Order Sheet          |
| Product specifications             | Product library                |
| Qualified supplier information     | Supplier panel                 |

---

## 4. Detailed Actions

| No.| Action                                                                  | Owner         | Tool / Support                   |
|----|-------------------------------------------------------------------------|---------------|----------------------------------|
| 1  | Define the order status (dropdown list)                                 | MANUFACTURE   | Order management system          |
| 2  | Send information to the required suppliers                              | MANUFACTURE   | Email / messaging                |
| 3  | Validation of production lead times by the suppliers                    | MANUFACTURE   | Email / messaging                |

---

## 5. Order Statuses

| Status                  | Description                                                  |
|-------------------------|--------------------------------------------------------------|
| Pending                 | Order received, awaiting supplier processing                  |
| In progress             | Information sent to supplier, awaiting response               |
| Deadlines validated     | Supplier has confirmed production lead times                  |
| In production           | Production launched at the supplier                           |

---

## 6. Block Outputs

| Element                              | Destination                      |
|--------------------------------------|----------------------------------|
| Updated order status                 | BLOCK 5 — Order Validation       |
| Validated production lead times      | BLOCK 5 — Order Validation       |
| Supplier confirmation                | BLOCK 6 — Production and Quality |

---

## 7. Control Points

| Control                                      | Acceptance Criterion                               | Owner         |
|----------------------------------------------|-----------------------------------------------------|---------------|
| Order status correctly defined               | Status consistent with actual progress               | MANUFACTURE   |
| Information sent to the correct suppliers    | Suppliers matching the ordered product               | MANUFACTURE   |
| Production lead times confirmed              | Lead times compatible with the customer deadline     | MANUFACTURE   |

---

## 8. Associated Documents

| Reference   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Process Chain — Existing Product Order         |
| CH-BLOC-002 | Detail Sheet — Order Sheet                    |
| CH-BLOC-005 | Detail Sheet — Order Validation               |
| CH-BLOC-006 | Detail Sheet — Production and Quality         |
| PR-P02-ACH  | Purchasing and Subcontracting Process         |
| FM-P02-AQF  | Supplier Quality Agreement                    |
| FM-P02-EVAL | Supplier Evaluation                           |

---

## Normative References

| ISO 9001:2015 Clause | Requirement                                               |
|-----------------------|-----------------------------------------------------------|
| 8.4                   | Control of externally provided processes, products and services |
| 8.4.3                 | Information for external providers                         |
| 8.1                   | Operational planning and control                           |

---

*Controlled document - Any printed copy is considered uncontrolled.*
*Plus Sàrl - Quality Management System ISO 9001:2015 - v0.7*
