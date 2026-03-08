# Block Detail Sheet - CH-BLOC-001: Customer Order Reception

| **Document**       | CH-BLOC-001_Reception_Commande                |
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

This sheet describes the detailed actions of **BLOCK 1 — Customer Order Reception** within the existing product order process chain.

---

## 2. Process Line

| Line Code  | Line      | Lead Role       |
|------------|-----------|-----------------|
| 01         | SALES     | SALES           |

---

## 3. Block Inputs

| Element                                | Source                    |
|----------------------------------------|---------------------------|
| Customer order (email, EDI, mail)      | Customer                  |
| Purchase order or formal request       | Customer                  |

---

## 4. Detailed Actions

| No.| Action                                                                                                       | Owner           | Tool / Support                   |
|----|--------------------------------------------------------------------------------------------------------------|-----------------|----------------------------------|
| 1  | Download and save the order on the desktop and in the ORDER_20XX folder using the same naming convention as the customer | SALES           | File system / ORDER_20XX         |

---

## 5. Naming Convention Rules

| Element               | Rule                                                               |
|-----------------------|--------------------------------------------------------------------|
| Storage folder        | ORDER_20XX (XX = current year)                                     |
| File name             | Identical to the naming convention used by the customer            |
| Local backup          | Copy on the desktop for immediate processing                       |

---

## 6. Block Outputs

| Element                          | Destination            |
|----------------------------------|------------------------|
| Order recorded and filed         | BLOCK 2 — Order Sheet  |
| File saved in ORDER_20XX         | Archiving              |

---

## 7. Control Points

| Control                                    | Acceptance Criterion                          | Owner           |
|--------------------------------------------|-----------------------------------------------|-----------------|
| Order complete and legible                 | All required information is present            | SALES           |
| File naming convention compliant           | Identical to the customer's convention         | SALES           |
| Saved in the correct folder               | Present in ORDER_20XX                          | SALES           |

---

## 8. Associated Documents

| Reference   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Process Chain — Existing Product Order         |
| CH-BLOC-002 | Detail Sheet — Order Sheet                    |
| PR-P01-COM  | Commercial Process                            |
| FM-P01-OFF  | Commercial Offer Template                     |
| FM-P01-BC   | Purchase Order                                |

---

## Normative References

| ISO 9001:2015 Clause | Requirement                                           |
|-----------------------|-------------------------------------------------------|
| 8.2.1                 | Customer communication                                 |
| 8.2.2                 | Determination of requirements for products             |
| 7.5                   | Documented information                                 |

---

*Controlled document - Any printed copy is considered uncontrolled.*
*Plus Sàrl - Quality Management System ISO 9001:2015 - v0.7*
