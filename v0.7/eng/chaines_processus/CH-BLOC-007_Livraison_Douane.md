# Block Detail Sheet - CH-BLOC-007: Delivery & Customs

| **Document**       | CH-BLOC-007_Livraison_Douane                  |
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

This sheet describes the detailed actions of **BLOCK 7 -- Delivery & Customs** within the existing product order process chain. This block involves two process lines: DELIVERY and SALES.

---

## 2. Process Lines

| Line Code  | Line        | Lead Role         |
|------------|-------------|-------------------|
| 03         | DELIVERY    | Logistics Role    |
| 01         | SALES       | Sales Role        |

---

## 3. Block Inputs

| Element                            | Source                            |
|------------------------------------|-----------------------------------|
| Parts conformity validated         | BLOCK 6 -- Production and Quality |
| Transport sheet                    | BLOCK 3 -- Transport Sheet        |
| Commercial information             | BLOCK 2 -- Order Sheet            |

---

## 4. Detailed Actions

| No. | Action                                                                                             | Line        | Responsible        | Tool / Medium                      |
|-----|-----------------------------------------------------------------------------------------------------|-------------|--------------------|------------------------------------|
| 1   | Creation of a delivery note                                                                         | 03 DELIVERY | Logistics Role     | Transport management system        |
| 2   | Sending the commercial invoice to the carrier                                                       | 01 SALES    | Sales Role         | E-mail                             |
| 3   | Definition of specific requirements to the supplier if any (deadline, delivery day, etc.)            | 03 DELIVERY | Logistics Role     | E-mail / messaging                 |
| 4   | Shipment tracking until delivery with the carrier                                                   | 03 DELIVERY | Logistics Role     | Tracking system                    |
| 5   | Customs tracking until delivery with the carrier and customs agent                                  | 03 DELIVERY | Logistics Role     | Customs agent communication        |
| 6   | Inform the customer of the delivery date validated by the carrier                                   | 01 SALES    | Sales Role         | E-mail                             |

---

## 5. Delivery Note Elements

| Element                     | Description                                         |
|-----------------------------|-----------------------------------------------------|
| Order reference             | Identical to customer reference                      |
| Product description         | Description of delivered products                    |
| Quantities                  | Number of units shipped                              |
| Weight and dimensions       | Physical characteristics of the package              |
| Delivery address            | Complete recipient address                           |
| Transport mode              | Delivery type defined in BLOCK 3                     |
| Shipment date               | Actual departure date                                |
| Expected delivery date      | Estimated arrival date                               |

---

## 6. Customs Tracking

| Step                           | Description                                                    | Responsible        |
|--------------------------------|----------------------------------------------------------------|--------------------|
| Export documents               | Preparation of required export documents                        | Logistics Role     |
| Customs declaration            | Customs declaration at departure                                | Customs agent      |
| Transit tracking               | International customs transit tracking                          | Logistics Role     |
| Customs clearance at destination | Coordination of customs clearance at arrival                  | Customs agent      |
| Delivery confirmation          | Validation of receipt by the consignee                          | Logistics Role     |

---

## 7. Block Outputs

| Element                                | Destination                          |
|----------------------------------------|--------------------------------------|
| Delivery note                          | BLOCK 8 -- Goods Acceptance          |
| Commercial invoice transmitted         | Carrier / Customs agent              |
| Delivery date communicated             | Customer                             |
| Proof of delivery                      | BLOCK 8 -- Goods Acceptance          |

---

## 8. Control Points

| Control                                         | Acceptance Criterion                                | Responsible        |
|-------------------------------------------------|-----------------------------------------------------|--------------------|
| Delivery note complete                          | All required elements completed                      | Logistics Role     |
| Commercial invoice sent to the carrier          | Compliant document transmitted before shipment        | Sales Role         |
| Active shipment tracking                        | Tracking number available and functional              | Logistics Role     |
| Customs clearance completed                     | No customs hold-up                                   | Logistics Role     |
| Customer informed of delivery date              | Communication sent with validated date                | Sales Role         |

---

## 9. Associated Documents

| Reference   | Document                                      |
|-------------|-----------------------------------------------|
| CHAIN-01    | Process Chain -- Existing Product Order        |
| CH-BLOC-003 | Detail Sheet -- Transport Sheet               |
| CH-BLOC-006 | Detail Sheet -- Production and Quality        |
| CH-BLOC-008 | Detail Sheet -- Goods Acceptance              |
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
*Plus Sarl - Quality Management System ISO 9001:2015 - v0.7*
