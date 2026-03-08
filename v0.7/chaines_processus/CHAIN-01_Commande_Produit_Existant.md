# Process Chain - CHAIN-01: Existing Product Order

| **Document**       | CHAIN-01_Commande_Produit_Existant         |
|--------------------|---------------------------------------------|
| **Version**        | v0.7                                        |
| **Date**           | 2026-03-04                                  |
| **Classification** | Internal                                    |
| **Process**        | Process Chain - Realization                 |
| **Drafted by**     | QUALITY                                     |
| **Approved by**    | Management                                  |

---

## 1. Purpose

This document describes the complete process chain for handling an **existing product order** at Plus Sàrl. It covers the standard flow applicable when a customer orders a product already referenced, with a supplier already evaluated and existing tooling.

---

## 2. Scope

This chain applies to any customer order for an existing product in the Plus Sàrl catalog, regardless of the geographic location of the customer or supplier.

---

## 3. Specifics of the "Existing Product" Chain

| Characteristic                   | Description                                                        |
|----------------------------------|--------------------------------------------------------------------|
| Development phase                | None — product already developed and validated                     |
| Supplier evaluation              | Already completed — supplier qualified and referenced              |
| Tooling                          | Existing — no tooling creation or modification required             |
| Lead time                        | Shortest among the 4 order types                                   |
| Inspection                       | Standard quality control per existing specifications               |

---

## 4. Process Lines

The chain is built around **4 process lines**:

| Code | Line              | Lead Role            | Main Function                                    |
|------|-------------------|----------------------|--------------------------------------------------|
| 01   | SALES             | SALES                | Commercial management, customer relations, invoicing |
| 02   | MANUFACTURE       | MANUFACTURE          | Supplier coordination, production monitoring      |
| 03   | DELIVERY          | DELIVERY             | Transport, delivery, customs                      |
| 04   | QUALITY           | QUALITY              | Compliance control, quality validation            |

---

## 5. Overview of the 8 Blocks

```
BLOCK 1         BLOCK 2         BLOCK 3         BLOCK 4
Order           Order           Transport       Technical
Reception       Sheet           Sheet           Study
[01 SALES]      [01 SALES]      [03 DELIVERY]   [02 MANUFACTURE]
    |               |               |               |
    v               v               v               v
BLOCK 5         BLOCK 6         BLOCK 7         BLOCK 8
Order           Production      Delivery        Goods
Validation      & Quality       & Customs       Acceptance
[01 SALES]      [02 MANUF.      [03 DELIVERY    [04 QUALITY
                 04 QUALITY]     01 SALES]        01 SALES]
```

---

## 6. Block Details by Process Line

### BLOCK 1 — Customer Order Reception

| Detail Ref. | Line     | Actions                                                                                      |
|-------------|----------|----------------------------------------------------------------------------------------------|
| CH-BLOC-001 | 01 SALES | Download and save the order on the desktop and in the ORDER_20XX folder using the same naming convention as the customer |

### BLOCK 2 — Order Sheet Creation

| Detail Ref. | Line     | Actions                                                                                              |
|-------------|----------|------------------------------------------------------------------------------------------------------|
| CH-BLOC-002 | 01 SALES | 1. Create a new order sheet                                                                          |
|             |          | 2. Add the order as PDF under the PDF tab                                                            |
|             |          | 3. Download the order into the file                                                                  |
|             |          | 4. Add the customer name, date, and deadline if applicable                                           |
|             |          | 5. Select the product name from the dropdown library                                                 |
|             |          | 6. Add the ordered quantity and final quantity (identical)                                            |
|             |          | 7. Add the order reference, identical to the customer's reference                                    |

### BLOCK 3 — Transport Sheet Creation

| Detail Ref. | Line        | Actions                                                                              |
|-------------|-------------|--------------------------------------------------------------------------------------|
| CH-BLOC-003 | 03 DELIVERY | 1. Create a transport sheet or add to an existing transport                           |
|             |             | 2. Validation of delivery deadlines by the carrier                                   |
|             |             | 3. Definition of the delivery type                                                   |

### BLOCK 4 — Technical Study with Suppliers

| Detail Ref. | Line           | Actions                                                                         |
|-------------|----------------|---------------------------------------------------------------------------------|
| CH-BLOC-004 | 02 MANUFACTURE | 1. Define the order status (dropdown list)                                       |
|             |                | 2. Send information to the required suppliers                                    |
|             |                | 3. Validation of production lead times by the suppliers                          |

### BLOCK 5 — Order Validation

| Detail Ref. | Line     | Actions                                                                                      |
|-------------|----------|----------------------------------------------------------------------------------------------|
| CH-BLOC-005 | 01 SALES | 1. Print the acknowledgment of receipt (AR) to prepare for sending and validate with the customer |
|             |          | 2. Send the AR to the customer with delivery details and price per product                   |
|             |          | 3. Customer feedback if necessary, or acceptance or rejection                                |

### BLOCK 6 — Production and Quality

| Detail Ref. | Line           | Actions                                                                                         |
|-------------|----------------|-------------------------------------------------------------------------------------------------|
| CH-BLOC-006 | 02 MANUFACTURE | Send production confirmation to the supplier (email or messaging)                                |
|             | 04 QUALITY     | Validation of parts conformity by the supplier following quality control                         |

### BLOCK 7 — Delivery & Customs

| Detail Ref. | Line        | Actions                                                                                          |
|-------------|-------------|--------------------------------------------------------------------------------------------------|
| CH-BLOC-007 | 03 DELIVERY | 1. Create a delivery note                                                                        |
|             | 01 SALES    | 2. Send the commercial invoice to the carrier                                                    |
|             | 03 DELIVERY | 3. Define any specific requirements to the supplier (deadline, delivery day, etc.)                |
|             | 03 DELIVERY | 4. Track the shipment until delivery with the carrier                                            |
|             | 03 DELIVERY | 5. Customs follow-up until delivery with the carrier and customs agent                           |
|             | 01 SALES    | 6. Inform the customer of the delivery date validated by the carrier                             |

### BLOCK 8 — Goods Acceptance

| Detail Ref. | Line       | Actions                                                                                    |
|-------------|------------|--------------------------------------------------------------------------------------------|
| CH-BLOC-008 | 04 QUALITY | 1. Confirmation email to the customer regarding goods conformity                            |
|             | 01 SALES   | 2. Send the invoice to the customer                                                        |
|             | 01 SALES   | 3. Send the customs declaration to the customer if applicable                              |
|             | 01 SALES   | 4. Customer payment                                                                       |
|             | 01 SALES   | 5. Close the file                                                                         |

---

## 7. Responsibility Matrix (RACI)

| Block  | SALES           | MANUFACTURE | DELIVERY        | QUALITY      |
|--------|-----------------|-------------|-----------------|--------------|
| BLOCK 1| R/A             | I           | I               | I            |
| BLOCK 2| R/A             | I           | I               | I            |
| BLOCK 3| I               | I           | R/A             | I            |
| BLOCK 4| I               | R/A         | I               | C            |
| BLOCK 5| R/A             | C           | C               | I            |
| BLOCK 6| I               | R/A         | I               | R/A          |
| BLOCK 7| R               | I           | R/A             | I            |
| BLOCK 8| R               | I           | I               | R/A          |

**Legend**: R = Responsible, A = Approver, C = Consulted, I = Informed

---

## 8. Key Performance Indicators (KPI)

| KPI                                    | Target                    | Measurement Frequency | Owner              |
|----------------------------------------|---------------------------|----------------------|--------------------|
| Average order processing time          | ≤ contractual deadline    | Monthly              | SALES              |
| Delivery conformity rate               | ≥ 95%                    | Monthly              | QUALITY            |
| Customer complaint rate                | ≤ 3%                     | Monthly              | SALES              |
| Supplier deadline compliance           | ≥ 90%                    | Monthly              | MANUFACTURE        |
| Rate of files closed on time           | ≥ 90%                    | Monthly              | SALES              |
| Quality control conformity rate        | ≥ 97%                    | Per order            | QUALITY            |
| Average delivery time                  | ≤ time announced to customer | Monthly           | DELIVERY           |

---

## 9. Associated Documents

| Reference    | Document                                  |
|--------------|-------------------------------------------|
| CH-BLOC-001  | Detail Sheet — Order Reception            |
| CH-BLOC-002  | Detail Sheet — Order Sheet                |
| CH-BLOC-003  | Detail Sheet — Transport Sheet            |
| CH-BLOC-004  | Detail Sheet — Technical Study            |
| CH-BLOC-005  | Detail Sheet — Order Validation           |
| CH-BLOC-006  | Detail Sheet — Production and Quality     |
| CH-BLOC-007  | Detail Sheet — Delivery and Customs       |
| CH-BLOC-008  | Detail Sheet — Goods Acceptance           |

---

## Normative References

| ISO 9001:2015 Clause | Requirement                                                     |
|-----------------------|-----------------------------------------------------------------|
| 8.1                   | Operational planning and control                                 |
| 8.2                   | Requirements for products and services                           |
| 8.4                   | Control of externally provided processes, products and services  |
| 8.5                   | Production and service provision                                 |
| 8.5.2                 | Identification and traceability                                  |
| 8.6                   | Release of products and services                                 |

---

*Controlled document - Any printed copy is considered uncontrolled.*
*Plus Sàrl - Quality Management System ISO 9001:2015 - v0.7*
