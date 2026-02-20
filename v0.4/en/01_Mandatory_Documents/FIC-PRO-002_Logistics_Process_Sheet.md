# Process Sheet O3 - Logistics and Delivery

| | |
|---|---|
| **Reference** | FIC-PRO-002 |
| **Version** | 0.4 |
| **Creation date** | 18/02/2026 |
| **Revision date** | 18/02/2026 |
| **Written by** | Roxane Wicky |
| **Approved by** | Roxane Wicky |

> **Legend:** 🔴 [TO BE COMPLETED] = mandatory, missing | 🟡 [RECOMMENDED] = recommended | 🟢 = already filled | 🔵 [TO BE VERIFIED] = to be confirmed

---

## Process identification

| Element | Description |
|---|---|
| **Process name** | Logistics and Delivery |
| **Code** | O3 |
| **Type** | Operational |
| **Owner** | Roxane Wicky (Managing Director) |
| **Purpose** | Organise the international transport of parts from China to European customers, manage customs documents, ensure shipment tracking and on-time delivery. |

---

## Input and output data

| Input data (inputs) | Source |
|---|---|
| Manufactured products ready for shipment | Process O2 - Purchasing and Subcontracting |
| Export documents (customs invoice, packing list) | Process O2 - Purchasing and Subcontracting |
| Delivery deadlines agreed with the customer | Process O1 - Sales |
| Customer order and delivery information | S1 - Document management (FileMaker) |

| Output data (outputs) | Recipient |
|---|---|
| Delivery confirmed to the customer | End customer |
| Customs documents (import/export declaration, certificates) | CH and EU customs authorities / Customer |
| Shipment tracking (tracking, progress notifications) | Internal / Customer |
| Customer reception confirmation | Process O1 - Sales / FileMaker |
| Logistics performance data (actual lead times, incidents) | Process M2 - Continual improvement |

---

## Description of activities

| # | Activity | Description | Responsible | Document/Record |
|---|---|---|---|---|
| 1 | Receipt of ready-for-shipment notification | Receive from process O2 the confirmation that the products have been manufactured, inspected and are ready for shipment. Verify the completeness of the export documents provided by O2. | Roxane Wicky | Ready-for-shipment notification, packing list, customs invoice |
| 2 | Creation of delivery record in FileMaker | Create or update the delivery record in FileMaker with the following information: agreed deadlines, shipping conditions, transport mode, customer delivery address, order references. | Roxane Wicky | FileMaker delivery record |
| 3 | Preparation of customs documents | Prepare all customs documents required for export from China and import into Switzerland/EU, in compliance with applicable legislation. Verify the compliance of each document. | Roxane Wicky | Customs declaration, certificate of origin, commercial invoice, packing list |
| 4 | Organisation of transport | Select the appropriate transport mode (air, sea or rail) based on urgency, volume and cost. Coordinate with the carrier for the collection of the goods. | Roxane Wicky | Transport order, booking confirmation, carrier emails |
| 5 | Shipment tracking | Track the movement of goods via the carrier's tracking tools. Proactively communicate with the customer on progress. Intervene in case of delay or incident. | Roxane Wicky | Carrier tracking, follow-up emails, WeChat messages |
| 6 | Customs management | Coordinate customs clearance on arrival (CH or EU import). Ensure that documents comply with regulatory requirements. Handle any additional requests from customs authorities. | Roxane Wicky | Clearance documents, customs clearance confirmation |
| 7 | Customer reception confirmation | Obtain confirmation of receipt of goods from the customer. Verify that the delivery matches the order (quantity, condition, deadline). Record any remarks or complaints. | Roxane Wicky | Customer reception confirmation, confirmation email/message |
| 8 | Closure in FileMaker | Update the delivery record in FileMaker: actual delivery date, order status, any remarks. Close the delivery dossier. | Roxane Wicky | FileMaker delivery record (updated), closure record |

---

## Flowchart (activity flow)

```
    [Ready-for-shipment notification received from process O2 - Purchasing]
            |
            v
    +-------------------------------+
    | 1. Receipt of ready-for-      |----> Packing list, customs invoice
    |    shipment notification (O2) |      received
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 2. Creation of delivery       |----> FileMaker delivery record
    |    record in FileMaker        |      (references, address,
    |    (deadlines, shipping       |       transport mode)
    |    conditions)                |
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 3. Preparation of customs     |----> Customs declaration,
    |    documents (compliant with  |      certificate of origin,
    |    EU and CH legislation)     |      commercial invoice
    +-------------------------------+
            |
            v
      /  Customs documents   \
     /   complete and          \
    /    compliant?              \
   YES                          NO
    |                             |
    |                             v
    |                   +------------------+
    |                   | Document         |
    |                   | correction       |---> Back to step 3
    |                   +------------------+
    v
    +-------------------------------+
    | 4. Transport organisation     |----> Air / Sea /
    |    (mode selection based on   |      Rail
    |    urgency and volume)        |      Booking confirmation
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 5. Shipment tracking          |----> Carrier tracking,
    |    (tracking through to       |      customer notifications,
    |    final delivery)            |      emails/WeChat
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 6. Customs management         |----> Import clearance,
    |    (import/export compliance) |      clearance documents
    +-------------------------------+
            |
            v
      /  Customs clearance   \
     /   completed without     \
    /    issues?                \
   YES                          NO
    |                             |
    |                             v
    |                   +---------------------------+
    |                   | Resolution of customs     |
    |                   | issue (additional         |
    |                   | documents, authority      |
    |                   | coordination)             |
    |                   +---------------------------+
    v
    +-------------------------------+
    | 7. Customer reception         |----> Confirmation email/message
    |    confirmation               |      from customer
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 8. Closure in FileMaker       |----> Delivery record updated,
    |    (actual date, status,      |      dossier closed
    |    remarks)                   |
    +-------------------------------+
            |
            v
    [Delivery completed - dossier closed]
```

---

## Required resources

| Resource type | Description |
|---|---|
| **Human** | Roxane Wicky (Managing Director) - full management of the logistics process, coordination with carriers and customs authorities |
| **Material** | Office in Cudrefin (Route de Montet 11, 1588 Cudrefin), computer, telephone |
| **IT** | Email (formal communication with customers, carriers and customs authorities), WeChat (coordination with Chinese partners for shipment), FileMaker (delivery tracking, information recording). Cloud backup at the provider's 🟢 |
| **Documentary** | Export documents, CH and EU customs regulations, carrier rates, delivery history |
| **Financial** | 🟡 [RECOMMENDED — define the annual transport and logistics budget] |

---

## Performance indicators

| Indicator | Calculation formula | Target | Frequency | Data source |
|---|---|---|---|---|
| On-time delivery rate | Number of on-time deliveries / Total number of deliveries x 100 | >= 95% 🟢 | Per delivery | FileMaker delivery tracking |
| Sea/rail delivery accuracy | Variance between actual delivery date and planned date (sea or rail transport) | +/- 10 days 🟢 | Per delivery | FileMaker delivery tracking |
| Air delivery accuracy | Variance between actual delivery date and planned date (air transport) | +/- 3 days 🟢 | Per delivery | FileMaker delivery tracking |
| Customs document compliance rate | Number of customs files conforming on first submission / Total number of files x 100 | 100% | Per delivery | Customs files, FileMaker |
| Transport incident rate | Number of deliveries with an incident (loss, damage, major delay) / Total number of deliveries x 100 | 🟡 [RECOMMENDED — define a target after the first reference year] | Quarterly | FileMaker delivery tracking |

---

## Planned improvement actions

| # | Action | Description | Deadline | Status |
|---|---|---|---|---|
| A05 | Carrier benchmarking | Establish a benchmark of the carriers used (lead times, reliability, cost) to optimise the choice of transport mode according to the situation. | Q2 2026 | Planned |
| A06 | Formalised customs procedure | Formalise a checklist of customs documents required by type of shipment (CH, EU) to reduce the risk of error. | Q2 2026 | Planned |

---

## Associated risks and opportunities

See CTX-QUA-001 for details. Summary:

| # | Risk / Opportunity | Level | Action |
|---|---|---|---|
| R04 | Transport delays (maritime, air, rail disruptions, weather conditions, port congestion) | High | Building in safety margins for deadlines, real-time shipment monitoring, proactive communication with the customer in case of delay, selection of the transport mode suited to urgency |
| R05 | Customs formalities (document error, regulatory change, customs hold) | Low | Rigorous document preparation, regulatory monitoring, checklist of required documents, relationship with customs authorities |
| O04 | Optimisation of delivery lead times (continual improvement of logistics circuits) | Medium | Regular benchmarking of carriers and transport modes, consolidation of shipments when possible, lessons learned from each delivery |

---

## Interfaces with other processes

| Interfacing process | Nature of the interaction |
|---|---|
| **O1 - Sales** | Receives: delivery deadlines agreed with the customer, delivery address, special conditions. Provides: delivery confirmation, actual date, shipment tracking |
| **O2 - Purchasing and Subcontracting** | Receives: products ready for shipment, export documents (customs invoice, packing list). Provides: confirmation of collection by the carrier |
| **O4 - Quality control** | Receives: notification of NC detected upon customer reception. Provides: information on the condition of goods at delivery, transport-related complaints |
| **S1 - Document management** | Provides: records (delivery records, customs documents, transport confirmations). Receives: access to history and data in FileMaker |
| **M2 - Continual improvement** | Provides: logistics performance data (lead times, incidents, customs compliance). Receives: improvement targets, corrective actions to implement |

---

## Applicable requirements

| Type | Requirement | Reference |
|---|---|---|
| ISO 9001:2015 | Preservation (of outputs during production and service provision) | 8.5.4 |
| ISO 9001:2015 | Post-delivery activities | 8.5.5 |
| ISO 9001:2015 | Identification and traceability | 8.5.2 |
| ISO 9001:2015 | Property belonging to customers or external providers | 8.5.3 |
| Regulatory | Swiss customs regulations (import from China) | 🔵 [TO BE VERIFIED — specific references] |
| Regulatory | European customs regulations (import into the EU) | 🔵 [TO BE VERIFIED — specific references depending on customer country] |
| Regulatory | Regulations applicable to the international transport of goods (air, sea, rail) | 🔵 [TO BE VERIFIED — depending on the transport modes used] |
| Customer | Delivery deadlines, delivery conditions (Incoterms), address and specific instructions | Customer order confirmation (per project) |

---

## Process-specific features

### Transport modes

| Mode | Use | Typical China-Europe transit time | Selection criterion |
|---|---|---|---|
| **Air** | Urgent orders, small volumes, samples | 5-10 days | High urgency, low volume |
| **Sea** | Large volumes, planned orders | 30-45 days | Large volume, optimised cost |
| **Rail** | Lead time/cost compromise, medium volumes | 18-25 days | Intermediate lead time, good cost/lead time ratio |

### Coordination with Chinese partners

The organisation of transport requires close coordination with the Chinese partners (Yuyao Mould Factory and **Whang**) for the availability of goods at the point of departure. Communication takes place primarily by email and WeChat.

### Specific attention points

- **Customs**: customs formalities depend on the type of goods, the country of destination and the declared value. Particular attention is paid to the compliance of each dossier.
- **Incoterms**: the delivery conditions (distribution of responsibilities between Plus Sarl and the customer) are defined for each order.
- **Time difference**: coordination with China for shipment involves a time difference of 6 to 7 hours. WeChat enables rapid exchanges despite this difference.
- **Paradiso**: the fiduciary is involved in the accounting and tax management of import/export operations.
- **Backup**: all logistics and customs documents are backed up in the cloud. 🟢

---

## Revision history

| Version | Date | Modification | Author |
|---|---|---|---|
| 0.4 | 18/02/2026 | Initial creation of the process sheet O3 - Logistics and Delivery. | Roxane Wicky |
