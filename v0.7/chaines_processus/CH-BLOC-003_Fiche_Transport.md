# Block Detail Sheet - CH-BLOC-003: Transport Sheet Creation

| **Document**       | CH-BLOC-003_Fiche_Transport                   |
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

This sheet describes the detailed actions of **BLOCK 3 — Transport Sheet Creation** within the existing product order process chain.

---

## 2. Process Line

| Line Code  | Line        | Lead Role       |
|------------|-------------|-----------------|
| 03         | DELIVERY    | DELIVERY        |

---

## 3. Block Inputs

| Element                            | Source                         |
|------------------------------------|--------------------------------|
| Completed order sheet              | BLOCK 2 — Order Sheet          |
| Customer delivery information      | BLOCK 2 — Order Sheet          |
| Customer requested deadlines       | BLOCK 2 — Order Sheet          |

---

## 4. Detailed Actions

| No.| Action                                                                         | Owner             | Tool / Support                   |
|----|--------------------------------------------------------------------------------|--------------------|----------------------------------|
| 1  | Create a transport sheet or add to an existing transport                        | DELIVERY           | Transport management system      |
| 2  | Validation of delivery deadlines by the carrier                                | DELIVERY           | Carrier communication            |
| 3  | Definition of the delivery type                                                | DELIVERY           | Transport management system      |

---

## 5. Delivery Types

| Delivery Type           | Description                                              |
|-------------------------|----------------------------------------------------------|
| Sea freight             | For bulky shipments, longer lead times                   |
| Air freight             | For urgent or low-volume shipments                       |
| Road transport          | For regional or continental deliveries                   |
| Rail transport          | For intermediate volume/lead time shipments              |
| Express transport       | For highly urgent shipments (express courier)            |

---

## 6. Block Outputs

| Element                             | Destination                         |
|-------------------------------------|-------------------------------------|
| Completed transport sheet           | BLOCK 5 — Order Validation          |
| Validated delivery deadlines        | BLOCK 5 — Order Validation          |
| Defined delivery type               | BLOCK 7 — Delivery & Customs        |

---

## 7. Control Points

| Control                                     | Acceptance Criterion                               | Owner             |
|---------------------------------------------|----------------------------------------------------|--------------------|
| Transport sheet created or updated          | All required information completed                  | DELIVERY           |
| Deadlines validated by the carrier          | Deadlines compatible with the customer deadline     | DELIVERY           |
| Appropriate delivery type                   | Consistent with volume, urgency, and destination    | DELIVERY           |

---

## 8. Associated Documents

| Reference   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Process Chain — Existing Product Order         |
| CH-BLOC-002 | Detail Sheet — Order Sheet                    |
| CH-BLOC-007 | Detail Sheet — Delivery and Customs           |

---

## Normative References

| ISO 9001:2015 Clause | Requirement                                           |
|-----------------------|-------------------------------------------------------|
| 8.5.4                 | Preservation                                           |
| 8.1                   | Operational planning and control                       |

---

*Controlled document - Any printed copy is considered uncontrolled.*
*Plus Sàrl - Quality Management System ISO 9001:2015 - v0.7*
