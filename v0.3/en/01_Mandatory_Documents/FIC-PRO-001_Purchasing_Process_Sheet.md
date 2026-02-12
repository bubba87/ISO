# Process Sheet O2 - Purchasing and Subcontracting

| | |
|---|---|
| **Reference** | FIC-PRO-001 |
| **Version** | 0.3 |
| **Creation date** | 10/02/2026 |
| **Revision date** | 12/02/2026 |
| **Written by** | Roxane Wicky |
| **Approved by** | Roxane Wicky |

> **Legend:** 🔴 [TO BE COMPLETED] = mandatory, missing | 🟡 [RECOMMENDED] = recommended | 🟢 = already filled | 🔵 [TO BE VERIFIED] = to be confirmed

---

## Process identification

| Element | Description |
|---|---|
| **Process name** | Purchasing and Subcontracting |
| **Code** | O2 |
| **Type** | Operational |
| **Process owner** | Roxane Wicky (Managing Director) |
| **Purpose** | Coordinate Chinese partners (Yuyao Mould Factory and **Whang**, Yuyao) to ensure the manufacturing of parts, moulds and screws in accordance with the specifications of European clients, in compliance with deadlines, prices and quality requirements. |

---

## Input and output data

| Input data (inputs) | Source |
|---|---|
| Client technical specifications (drawings, requirements, tolerances, materials) | Client via process O1 - Commercial |
| Delivery deadlines agreed with the client | Process O1 - Commercial |
| Quotation accepted by the client, order confirmation | Process O1 - Commercial |
| Order and price history | S1 - Document management (FileMaker) |
| Feedback on previous non-conformities | Process O4 - Quality control |

| Output data (outputs) | Recipient |
|---|---|
| Manufacturing order transmitted to the Chinese partner | Yuyao Mould Factory / Whang |
| Feasibility and manufacturing lead time confirmation | Process O1 - Commercial (for client information) |
| Production monitoring reports (photos, progress reports) | Internal / Client if requested |
| Manufactured products ready for shipment | Process O3 - Logistics and delivery |
| Export documents (customs invoice, packing list) | Process O3 - Logistics and delivery |
| Supplier inspection reports | Process O4 - Quality control |
| Samples sent in parallel with the shipment | Plus Sarl (conformity check) 🟢 |
| Supplier performance evaluation | Process M2 - Continuous improvement |

---

## Activity description

| # | Activity | Description | Responsible | Document/Record |
|---|---|---|---|---|
| 1 | Receipt of client specifications | Receive from the commercial process the technical specifications, drawings, requirements and client needs. Verify the completeness of the file. | Roxane Wicky | Client requirements, technical drawings, transmission email |
| 2 | Consultation of Chinese partner(s) | Transmit the specifications to Yuyao Mould Factory (main partner) or to **Whang** (Yuyao — specialised in screw manufacturing) depending on the nature of the project. Request a feasibility analysis, quotation and lead time. Communication by email and WeChat. | Roxane Wicky | Emails, WeChat messages, supplier quotation |
| 3 | Iterative technical exchanges | Coordinate back-and-forth between the client and the Chinese partner until a validated technical solution is reached (materials, tolerances, manufacturing process, price). Translate and adapt requirements if necessary. | Roxane Wicky | Emails, WeChat messages, exchange summaries |
| 4 | Validation and order placement | Once the technical solution and price are validated by the client, issue the manufacturing order to the Chinese partner. Prepare the order documents (customs invoice, purchase order). | Roxane Wicky | Purchase order, customs invoice, order confirmation |
| 5 | Production monitoring | Monitor production progress with the Chinese partner. Receive and analyse photos, progress reports, inspection reports. Intervene in case of deviation. | Roxane Wicky | Production photos, progress reports, supplier inspection reports, WeChat messages |
| 6 | Pre-shipment quality control | The partner will carry out a quality control before shipment as well as send samples to Plus Sarl in parallel with transport to the client. 🟢 | Roxane Wicky / Chinese partner | Final inspection report, samples, shipment approval |
| 7 | Handover to logistics process | Confirm that the products are ready and transmit the necessary information to process O3 (Logistics/Delivery) for transport organisation. Provide export documents. | Roxane Wicky | Export documents, packing list, ready-for-shipment notification |
| 8 | Partner evaluation | Periodically evaluate the performance of Chinese partners (conformity, deadline compliance, communication quality, responsiveness). | Roxane Wicky | Supplier evaluation form (simplified form created by the Managing Director) |

---

## Flowchart (activity flow)

```
    [Client specifications received from process O1 - Commercial]
            |
            v
    +-------------------------------+
    | 1. Receipt and verification   |----> Requirements, drawings
    |    of client specifications   |
    +-------------------------------+
            |
            v
    +-------------------------------+
    | 2. Consultation of Chinese    |----> Email/WeChat to Yuyao Mould Factory
    |    partner (feasibility,      |      or Whang (Yuyao - screws)
    |    quotation, lead time)      |
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
      /  Technical solution    \
     /   and price validated    \
    /    by the client ?         \
   YES                          NO
    |                           |
    |                           v
    |                   +------------------+
    |                   | Return to client |
    |                   | for adjustment   |---> Return to step 3
    |                   +------------------+
    v
    +-------------------------------+
    | 4. Order placement to         |----> Purchase order, customs
    |    Chinese partner            |      invoice
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
    | 6. Pre-shipment quality       |----> Final inspection report
    |    control                    |      + sending samples to
    |    (by the partner)           |      Plus Sarl in parallel
    |    + sampling                 |      with client transport
    +-------------------------------+
            |
            v
      /  Product conforming    \
     /   to specifications ?    \
    /                            \
   YES                          NO
    |                           |
    |                           v
    |                   +---------------------------+
    |                   | NC processing             |
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
| **IT** | Email (formal communication with clients and partners), WeChat (daily communication with Chinese partners), FileMaker (order tracking, information recording). Cloud backup at the provider 🟢 |
| **Documentary** | Client specifications, technical drawings, supplier catalogues, applicable standards, order history |
| **Financial** | 🟡 [RECOMMENDED — define the annual purchasing and subcontracting budget] |

---

## Performance indicators

| Indicator | Calculation formula | Objective | Frequency | Data source |
|---|---|---|---|---|
| Supplier on-time delivery | Number of supplier deliveries on time / Total number of deliveries x 100 | >= 95% 🟢 | Per delivery | Order tracking FileMaker |
| Conformity rate (NC per client) | Number of NCs per client per year | Maximum 3 NC per client per year 🟢 | Per delivery | NC sheets, NC register, FileMaker |
| Number of non-conformities (NC) | Count of NCs recorded per period | Reduction year on year (1st year: baseline) | Quarterly | NC sheets, FileMaker |
| Replacement time in case of NC | Actual replacement date - NC reporting date | Consistent with the need expressed by the client 🟢 | Per NC | NC sheets, emails |
| Price stability | Price evolution compared to the previous year | Stable prices over several years | Annual | Quotation and order history FileMaker |

---

## Planned improvement actions

| # | Action | Description | Deadline | Status |
|---|---|---|---|---|
| A01 | Trip to China - March 2026 | Planned trip to China in March 2026 to strengthen production quality controls, visit partners (Yuyao Mould Factory and **Whang**), and consolidate quality requirements on site. | March 2026 | Planned |
| A02 | Strengthening of labelling controls | Following NC_2026_1001 (labelling error on 1000 pieces SHIP_25058/CFM00057428/90.60.05710), strengthening of labelling controls before shipment. | Q2 2026 | In progress |
| A03 | Quality agreement with Yuyao Mould Factory | Formalise a quality agreement with Yuyao as soon as the certification file is ready. 🟢 | As soon as certification file ready | Planned |
| A04 | Quality agreement with Whang | Formalise a quality agreement with Whang as soon as the certification file is ready. 🟢 | As soon as certification file ready | Planned |

---

## Associated risks and opportunities

See CTX-QUA-001 for details. Summary:

| # | Risk / Opportunity | Level | Action |
|---|---|---|---|
| R01 | Manufacturing delay at the Chinese partner | High | Regular production monitoring (WeChat/email), deadline anticipation, safety margin in schedules |
| R02 | Non-conformity of manufactured parts | High | Pre-shipment quality control by the partner, sending of samples in parallel, inspection reports, NC history for identification of recurring causes 🟢 |
| R03 | Communication issue (language barrier, time zone difference) | Medium | Use of WeChat for quick exchanges, detailed written specifications, photos and samples |
| R04 | Dependence on a limited number of partners | Medium | Maintaining two active Chinese partners (Yuyao Mould Factory and Whang), regular evaluation, monitoring for potential additional partners 🟢 |
| R05 | Raw material price or exchange rate fluctuation | Medium | Price monitoring over several years, quotations validated by the client, proactive communication in case of variation |
| R06 | Partner certifications not confirmed | Medium | 🔵 [TO BE VERIFIED — Whang certifications uncertain, to be clarified during China trip March 2026] |
| O01 | Strengthening of partnership with Yuyao Mould Factory | High | Trust relationship built since the creation of Plus Sarl (2007), regular communication, trip to China planned March 2026, quality agreement in preparation |
| O02 | Capacity diversification via Whang (screws) | Medium | Develop orders with Whang to expand production capacity (screws and other) 🟢 |

---

## Interfaces with other processes

| Interfacing process | Nature of interaction |
|---|---|
| **O1 - Commercial** | Receives: client specifications, order confirmation, agreed deadlines. Provides: feasibility feedback, manufacturing lead time, partner price |
| **O3 - Logistics and delivery** | Provides: products ready for shipment, export documents (customs invoice, packing list). Receives: shipment confirmation |
| **O4 - Quality control** | Provides: supplier inspection reports, products to be checked, samples received in parallel. Receives: manufacturing NC feedback, corrective action requests, replacement requests |
| **M2 - Continuous improvement** | Provides: supplier performance data, indicators. Receives: improvement objectives, corrective actions to implement |
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
| Regulatory | Swiss customs regulations (import from China) | 🔵 [TO BE VERIFIED — specific references] |
| Regulatory | Applicable regulations depending on the nature of products (CE marking, etc.) | 🔵 [TO BE VERIFIED — depending on products] |
| Client | Technical specifications, drawings, tolerances, materials defined by each client | Client requirements (per project) |

---

## Process specifics

### Chinese partners

| Partner | Role | Location | Products | Certifications | Communication method |
|---|---|---|---|---|---|
| **Yuyao Mould Factory** | Main partner - mould and part manufacturing | Yuyao, China | Injection moulds, plastic parts | 🔵 [TO BE VERIFIED] | Email, WeChat |
| **Whang** | Second partner - screw manufacturing | Yuyao, China | Screws 🟢 | 🔵 [TO BE VERIFIED — certifications uncertain] | Email, WeChat |

### Pre-shipment quality control

The partner will carry out a quality control before shipment as well as send samples to Plus Sarl in parallel with transport to the client. This process allows Plus Sarl to verify product conformity while maintaining delivery deadlines. 🟢

### Mould management

The moulds are developed and stored in China, at the partners' premises. The moulds are the **property of the clients**. A **mould inventory exists**. 🟢

### Specific points of attention

- **Intellectual property**: designs and drawings belong exclusively to the clients. Plus Sarl ensures the confidentiality of technical information transmitted to Chinese partners (cf. Quality policy, commitment no.6).
- **Mould storage**: moulds are developed and stored in China, at the partner's premises. Property of the clients. Existing inventory. 🟢
- **Time zone difference**: coordination with China involves a time zone difference of 6 to 7 hours. The use of WeChat enables quick exchanges despite this difference.
- **No design activity**: Plus Sarl does not design products (clause 8.3 excluded). The role is that of industrial coordinator between the client (design owner) and the Chinese manufacturer.
- **Trip to China March 2026**: an on-site visit is planned to strengthen production quality controls and consolidate requirements with the partners.
- **Quality agreement**: a quality agreement will be formalised with Yuyao Mould Factory and Whang as soon as the certification file is ready. 🟢

---

## Revision History

| Version | Date | Modification | Author |
|---|---|---|---|
| 1.0 | 10/02/2026 | Initial creation | Roxane Wicky |
| 0.2 | 10/02/2026 | Update of performance indicators (supplier on-time delivery >= 95%, max 3 NC/client/year). Addition of improvement actions: China trip March 2026, strengthened labelling control following NC_2026_1001. | Roxane Wicky |
| 0.3 | 12/02/2026 | Integration of responses (Whang, Paradiso, SQS, cloud backup). Addition of field legend system. | Roxane Wicky |
