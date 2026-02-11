# Process Sheet O2 - Purchasing and Subcontracting

| | |
|---|---|
| **Reference** | FIC-PRO-001 |
| **Version** | 1.0 |
| **Date created** | 10/02/2026 |
| **Date revised** | 10/02/2026 |
| **Written by** | Roxane Wicky |
| **Approved by** | Roxane Wicky |

---

## Process identification

| Element | Description |
|---|---|
| **Process name** | Purchasing and Subcontracting |
| **Code** | O2 |
| **Type** | Operational |
| **Owner** | Roxane Wicky (Managing Director) |
| **Purpose** | Coordinate Chinese partners (Yuyao Mould Factory and second partner) to ensure the manufacture of parts and moulds in accordance with European clients' specifications, within the required deadlines, prices and quality requirements. |

---

## Inputs and outputs

| Inputs | Source |
|---|---|
| Client technical specifications (drawings, specifications, tolerances, materials) | Client via process O1 - Sales |
| Delivery deadlines agreed with the client | Process O1 - Sales |
| Offer validated by the client, order confirmation | Process O1 - Sales |
| Order and price history | S1 - Document management (FileMaker) |
| Feedback on previous non-conformities | Process O4 - Quality control |

| Outputs | Recipient |
|---|---|
| Manufacturing order transmitted to the Chinese partner | Yuyao Mould Factory / Second partner |
| Feasibility and manufacturing lead time confirmation | Process O1 - Sales (for client information) |
| Production monitoring reports (photos, progress reports) | Internal / Client if requested |
| Manufactured products ready for shipment | Process O3 - Logistics and delivery |
| Export documents (customs invoice, packing list) | Process O3 - Logistics and delivery |
| Supplier inspection reports | Process O4 - Quality control |
| Supplier performance evaluation | Process M2 - Continuous improvement |

---

## Activity description

| # | Activity | Description | Responsible | Document/Record |
|---|---|---|---|---|
| 1 | Receipt of client specifications | Receive technical specifications, drawings, requirements and client requirements from the sales process. Verify completeness of the file. | Roxane Wicky | Client specifications, technical drawings, transmission email |
| 2 | Consultation of the Chinese partner(s) | Transmit specifications to Yuyao Mould Factory (main partner) or to the second partner depending on the nature of the project. Request a feasibility analysis, quotation and lead time. Communication by email and WeChat. | Roxane Wicky | Emails, WeChat messages, supplier quotation |
| 3 | Iterative technical exchanges | Coordinate back-and-forth between the client and the Chinese partner until a validated technical solution is reached (materials, tolerances, manufacturing process, price). Translate and adapt requirements if necessary. | Roxane Wicky | Emails, WeChat messages, exchange summaries |
| 4 | Validation and order placement | Once the technical solution and price are validated by the client, issue the manufacturing order to the Chinese partner. Prepare order documents (customs invoice, purchase order). | Roxane Wicky | Purchase order, customs invoice, order confirmation |
| 5 | Production monitoring | Monitor production progress with the Chinese partner. Receive and analyze photos, progress reports, inspection reports. Intervene in case of any deviation observed. | Roxane Wicky | Production photos, progress reports, supplier inspection reports, WeChat messages |
| 6 | Pre-shipment validation | Review the Chinese partner's final inspection reports before authorizing shipment. Ensure that the product conforms to the initial specifications. | Roxane Wicky | Final inspection report, shipment authorization |
| 7 | Handover to logistics process | Confirm that products are ready and transmit the necessary information to process O3 (Logistics/Delivery) for transport organization. Provide export documents. | Roxane Wicky | Export documents, packing list, ready-for-shipment notification |
| 8 | Partner evaluation | Periodically evaluate the performance of Chinese partners (conformity, on-time delivery, communication quality, responsiveness). | Roxane Wicky | [TO BE CONFIRMED - Supplier evaluation form] |

---

## Flowchart (activity flow)

```
    [Client specifications received from process O1 - Sales]
            |
            v
    +-------------------------------+
    | 1. Receipt and verification   |----> Specifications, drawings
    |    of client specifications   |
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 2. Consultation of the        |----> Email/WeChat to Yuyao Mould Factory
    |    Chinese partner            |      or second partner
    |    (feasibility, quotation,   |
    |    lead time)                 |
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 3. Iterative technical        |----> Emails, WeChat
    |    exchanges (client <-->     |      (back-and-forth until
    |    Chinese partner)           |       validation)
    +-------------------------------+
            |
            v
      /  Technical solution   \
     /   and price validated   \
    /    by the client?         \
   YES                         NO
    |                           |
    |                           v
    |                   +------------------+
    |                   | Return to client |
    |                   | for adjustment   |---> Return to step 3
    |                   +------------------+
    v
    +-------------------------------+
    | 4. Order placement            |----> Purchase order, customs
    |    to Chinese partner         |      invoice
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 5. Production monitoring      |----> Photos, progress reports,
    |    (regular exchanges         |      inspection reports
    |    email/WeChat)              |
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 6. Pre-shipment validation    |----> Final inspection report
    +-------------------------------+
            |
            v
      /  Product conforming    \
     /   to specifications?     \
    /                            \
   YES                          NO
    |                           |
    |                           v
    |                   +---------------------------+
    |                   | NC handling               |
    |                   | (O4 - Quality control)    |
    |                   | Replacement coordination  |
    |                   | with Chinese partner      |
    |                   +---------------------------+
    v
    +-------------------------------+
    | 7. Handover to process        |----> Export documents,
    |    O3 - Logistics/Delivery    |      packing list
    +-------------------------------+
            |
            v
    [Products ready for shipment]
```

---

## Required resources

| Resource type | Description |
|---|---|
| **Human** | Roxane Wicky (Managing Director) - full management of the coordination process with Chinese partners |
| **Material** | Office in Cudrefin (Route de Montet 11, 1588 Cudrefin), computer, telephone |
| **IT** | Email (formal communication with clients and partners), WeChat (daily communication with Chinese partners), FileMaker (order tracking, information recording) |
| **Documentary** | Client specifications, technical drawings, supplier catalogues, applicable standards, order history |
| **Financial** | [TO BE CONFIRMED - Annual purchasing and subcontracting budget] |

---

## Performance indicators

| Indicator | Calculation method | Objective | Frequency | Data source |
|---|---|---|---|---|
| Number of non-conformities (NCs) | Count of NCs recorded per period | Reduction year over year (1st year: baseline) | Quarterly | NC reports, FileMaker |
| Replacement lead time in case of NC | Actual replacement date - NC reporting date | Consistent with the need expressed by the client | Per NC | NC reports, emails |
| Supplier on-time delivery | Number of on-time supplier deliveries / Total number of deliveries x 100 | [TO BE CONFIRMED - e.g.: >= 90%] | Per delivery | Order tracking FileMaker |
| Supplier delivery conformity rate | Number of conforming lots / Total number of lots received x 100 | [TO BE CONFIRMED - e.g.: >= 95%] | Per delivery | Inspection reports, NC reports |
| Price stability | Price evolution compared to the previous year | Prices stable over several years | Annual | Quotation and order history FileMaker |

---

## Associated risks and opportunities

See CTX-QUA-001 for details. Summary:

| # | Risk / Opportunity | Level | Action |
|---|---|---|---|
| R01 | Manufacturing delay at the Chinese partner | High | Regular production monitoring (WeChat/email), lead time anticipation, safety margin in schedules |
| R02 | Non-conformity of manufactured parts | High | Pre-shipment validation, inspection reports, NC history for identification of recurring causes |
| R03 | Communication issue (language barrier, time zone difference) | Medium | Use of WeChat for quick exchanges, detailed written specifications, photos and samples |
| R04 | Dependence on a limited number of partners | Medium | Maintaining two active Chinese partners, regular evaluation, monitoring of potential additional partners |
| R05 | Raw material price or exchange rate fluctuation | Medium | Multi-year price monitoring, offers validated by the client, proactive communication in case of variation |
| O01 | Strengthening of the partnership with Yuyao Mould Factory | High | Relationship of trust built since the creation of Plus Sarl (2007), regular communication, visits [TO BE CONFIRMED] |
| O02 | Capacity diversification through the second partner | Medium | Develop orders with the second partner to expand production capacity |

---

## Interfaces with other processes

| Interfacing process | Nature of interaction |
|---|---|
| **O1 - Sales** | Receives: client specifications, order confirmation, agreed deadlines. Provides: feasibility feedback, manufacturing lead time, partner price |
| **O3 - Logistics and delivery** | Provides: products ready for shipment, export documents (customs invoice, packing list). Receives: shipment confirmation |
| **O4 - Quality control** | Provides: supplier inspection reports, products to be inspected. Receives: manufacturing NC feedback, corrective action requests, replacement requests |
| **M2 - Continuous improvement** | Provides: supplier performance data, indicators. Receives: improvement objectives, corrective actions to be implemented |
| **S1 - Document management** | Provides: records (purchase orders, reports, correspondence). Receives: access to history and data in FileMaker |
| **S2 - Competencies** | Receives: training or updates on standards, manufacturing techniques, regulatory requirements |

---

## Applicable requirements

| Type | Requirement | Reference |
|---|---|---|
| ISO 9001:2015 | Control of externally provided processes, products and services | 8.4 |
| ISO 9001:2015 | Type and extent of control (of external providers) | 8.4.2 |
| ISO 9001:2015 | Information for external providers | 8.4.3 |
| ISO 9001:2015 | Production and service provision - Control of production | 8.5.1 |
| ISO 9001:2015 | Identification and traceability | 8.5.2 |
| ISO 9001:2015 | Property belonging to customers or external providers | 8.5.3 |
| ISO 9001:2015 | Control of nonconforming outputs | 8.7 |
| Regulatory | Swiss customs regulations (import from China) | [TO BE CONFIRMED - specific references] |
| Regulatory | Applicable regulations depending on product nature (CE marking, etc.) | [TO BE CONFIRMED - depending on products] |
| Client | Technical specifications, drawings, tolerances, materials defined by each client | Client specifications (per project) |

---

## Process specifics

### Chinese partners

| Partner | Role | Location | Communication method |
|---|---|---|---|
| **Yuyao Mould Factory** | Main partner - mould and parts manufacturing | Yuyao, China | Email, WeChat |
| **Second partner** | Complementary partner | [TO BE CONFIRMED] | Email, WeChat |

### Key notes

- **Intellectual property**: designs and drawings belong exclusively to the clients. Plus Sarl ensures the confidentiality of technical information transmitted to the Chinese partners (cf. Quality policy, commitment no. 6).
- **Mould storage**: moulds are developed and stored in China, at the partner's premises. An inventory and mould condition monitoring system is [TO BE CONFIRMED].
- **Time zone difference**: coordination with China involves a time difference of 6 to 7 hours. The use of WeChat allows for quick exchanges despite this difference.
- **No design activity**: Plus Sarl does not design products (clause 8.3 excluded). The role is that of an industrial coordinator between the client (design owner) and the Chinese manufacturer.

---

## Revision history

| Version | Date | Modification | Author |
|---|---|---|---|
| 1.0 | 10/02/2026 | Initial creation | Roxane Wicky |
| | | | |
