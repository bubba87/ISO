# Block Detail Sheet - CH-BLOC-007: Delivery & Customs

| **Document**       | CH-BLOC-007_Livraison_Douane                  |
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

This sheet describes the detailed actions of **BLOCK 7 — Delivery & Customs** within the existing product order process chain. This block involves two process lines: DELIVERY and SALES.

---

## 2. Process Lines

| Line Code  | Line        | Lead Role       |
|------------|-------------|-----------------|
| 03         | DELIVERY    | DELIVERY        |
| 01         | SALES       | SALES           |

---

## 3. Block Inputs

| Element                            | Source                            |
|------------------------------------|-----------------------------------|
| Parts conformity validated         | BLOCK 6 — Production and Quality  |
| Transport sheet                    | BLOCK 3 — Transport Sheet         |
| Commercial information             | BLOCK 2 — Order Sheet             |

---

## 4. Detailed Actions

| No.| Action                                                                                             | Line        | Owner             | Tool / Support                     |
|----|----------------------------------------------------------------------------------------------------|-------------|--------------------|------------------------------------|
| 1  | Create a delivery note                                                                             | 03 DELIVERY | DELIVERY           | Transport management system        |
| 2  | Send the commercial invoice to the carrier                                                         | 01 SALES    | SALES              | Email                              |
| 3  | Define any specific requirements to the supplier (deadline, delivery day, etc.)                     | 03 DELIVERY | DELIVERY           | Email / messaging                  |
| 4  | Track the shipment until delivery with the carrier                                                  | 03 DELIVERY | DELIVERY           | Tracking system                    |
| 5  | Customs follow-up until delivery with the carrier and customs agent                                 | 03 DELIVERY | DELIVERY           | Customs agent communication        |
| 6  | Inform the customer of the delivery date validated by the carrier                                   | 01 SALES    | SALES              | Email                              |

---

## 5. Delivery Note Elements

| Element                     | Description                                         |
|-----------------------------|-----------------------------------------------------|
| Order reference             | Identical to the customer's reference                |
| Product description         | Description of delivered products                    |
| Quantities                  | Number of units shipped                              |
| Weight and dimensions       | Physical characteristics of the package              |
| Delivery address            | Full address of the recipient                        |
| Transport mode              | Delivery type defined in BLOCK 3                     |
| Shipment date               | Actual departure date                                |
| Expected delivery date      | Estimated arrival date                               |

---

## 6. Customs Follow-up

| Step                           | Description                                                    | Owner             |
|--------------------------------|----------------------------------------------------------------|--------------------|
| Export documents               | Preparation of documents required for export                    | DELIVERY           |
| Customs declaration            | Customs declaration at departure                                | Customs agent      |
| Transit tracking               | International customs transit tracking                          | DELIVERY           |
| Customs clearance at destination| Coordination of customs clearance upon arrival                  | Customs agent      |
| Delivery confirmation          | Validation of receipt by the recipient                          | DELIVERY           |

---

## 7. Block Outputs

| Element                                | Destination                          |
|----------------------------------------|--------------------------------------|
| Delivery note                          | BLOCK 8 — Goods Acceptance           |
| Commercial invoice transmitted         | Carrier / Customs agent              |
| Delivery date communicated             | Customer                             |
| Proof of delivery                      | BLOCK 8 — Goods Acceptance           |

---

## 8. Control Points

| Control                                         | Acceptance Criterion                                | Owner             |
|-------------------------------------------------|------------------------------------------------------|--------------------|
| Delivery note complete                          | All required elements completed                       | DELIVERY           |
| Commercial invoice sent to the carrier          | Compliant document transmitted before shipment        | SALES              |
| Active shipment tracking                        | Tracking number available and functional              | DELIVERY           |
| Customs clearance completed                     | No customs hold                                       | DELIVERY           |
| Customer informed of delivery date              | Communication sent with validated date                | SALES              |

---

## 9. Associated Documents

| Reference   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Process Chain — Existing Product Order         |
| CH-BLOC-003 | Detail Sheet — Transport Sheet                |
| CH-BLOC-006 | Detail Sheet — Production and Quality         |
| CH-BLOC-008 | Detail Sheet — Goods Acceptance               |
| PR-P04-LOG  | Logistics and Delivery Process                |
| FM-P04-EXP  | Shipment Sheet                                |
| FM-P04-SUI  | Shipment Tracking Table                       |

---

## Normative References

| ISO 9001:2015 Clause | Requirement                                           |
|-----------------------|-------------------------------------------------------|
| 8.5.4                 | Preservation                                           |
| 8.5.2                 | Identification and traceability                        |
| 8.1                   | Operational planning and control                       |

---

*Controlled document - Any printed copy is considered uncontrolled.*
*Plus Sàrl - Quality Management System ISO 9001:2015 - v0.7*
