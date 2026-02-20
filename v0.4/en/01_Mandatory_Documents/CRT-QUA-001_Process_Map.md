# Process Map

| | |
|---|---|
| **Reference** | CRT-QUA-001 |
| **Version** | 0.4 |
| **Creation date** | 10/02/2026 |
| **Revision date** | 20/02/2026 |
| **Written by** | Roxane Wicky |
| **Approved by** | Roxane Wicky |

> **Legend:** 🔴 [TO BE COMPLETED] = mandatory, missing | 🟡 [RECOMMENDED] = recommended | 🟢 = already filled | 🔵 [TO BE VERIFIED] = to be confirmed

---

## 1. Process overview

### Context

Plus Sarl specialises in industrial coordination between European clients and Chinese manufacturing partners. The company does not carry out any design activities (clause 8.3 of the ISO 9001:2015 standard excluded from the scope of application). Designs and intellectual property belong to the clients. The activity covers commercial coordination, purchasing and subcontracting with Chinese partners (Yuyao Mould Factory and **Whang**, Yuyao), international logistics organisation and quality control.

ISO 9001:2015 certification is pursued through the certification body **SQS**. 🟢

### Process map representation

```
+=========================================================================+
|                    MANAGEMENT PROCESSES                                   |
|  +-------------------+  +-------------------+  +---------------------+  |
|  | M1 - Leadership   |  | M2 - Continuous   |  | M3 - Management     |  |
|  | and strategy      |  | improvement       |  | review              |  |
|  +-------------------+  +-------------------+  +---------------------+  |
+=========================================================================+
                                    |
  CLIENT                            v                           CLIENT
  REQUIREMENTS +====================================================+  SATISFACTION
  -----------> |              OPERATIONAL PROCESSES                  | -------->
               |                                                      |
               |  +----------+  +----------+  +----------+  +------+  |
               |  | O1       |  | O2       |  | O3       |  | O4   |  |
               |  | Commer-  |->| Purcha-  |->| Logis-   |->| Qual.|  |
               |  | cial     |  | sing &   |  | tics &   |  | Con- |  |
               |  |          |  | Subcon.  |  | Delivery |  | trol |  |
               |  +----------+  +----------+  +----------+  +------+  |
               +====================================================+
                                    |
+=========================================================================+
|                    SUPPORT PROCESSES                                      |
|  +-------------------+  +-------------------+  +---------------------+  |
|  | S1 - Document     |  | S2 - Competency   |  | S3 - Resource and   |  |
|  | management         |  | and training      |  | infrastructure      |  |
|  | (FileMaker, emails)|  | management        |  | management          |  |
|  +-------------------+  +-------------------+  +---------------------+  |
+=========================================================================+
```

**Note:** Clause 8.3 (Design and development) is excluded from the scope of application. Designs are the property of the clients. Plus Sarl acts as an industrial coordinator and does not carry out any design activities.

---

## 2. List of processes

### Management processes

| Code | Process | Process owner | Purpose | Associated document(s) |
|---|---|---|---|---|
| M1 | Leadership and strategy | Roxane Wicky (Managing Director) | Define the quality policy, strategic objectives, assign responsibilities, guide the company and **plan changes** (clause 6.3 — impact analysis, validation, controlled implementation) | **M1-DIR-001**, POL-QUA-001, CTX-QUA-001 (section 6) 🟢 |
| M2 | Continual improvement | Roxane Wicky (Managing Director) | Drive QMS improvement (nonconformities, corrective actions, indicators). **Review of change effectiveness** during management review | PRO-NCF-001, PRO-ACR-001 |
| M3 | Management review | Roxane Wicky (Managing Director) | Evaluate QMS performance and decide on improvement actions | FOR-RDR-001 |

### Operational processes

| Code | Process | Process owner | Purpose | Associated document(s) |
|---|---|---|---|---|
| O1 | Commercial | Roxane Wicky (Managing Director) | Manage client relationships (~10 active clients), analyse needs, carry out order review, track orders in FileMaker | CTX-QUA-001 (sections 1.2, 1.3) 🟢 |
| O2 | Purchasing and subcontracting | Roxane Wicky (Managing Director) | Coordinate Chinese partners (Yuyao Mould Factory and **Whang**), create FileMaker production sheets, monitor production 🟢 | PRO-ACH-001, FIC-PRO-001 |
| O3 | Logistics and delivery | Roxane Wicky (Managing Director) | Create FileMaker delivery sheets, organise international transport, manage customs documents, ensure tracking until delivery 🟢 | **PRO-LOG-001**, **FIC-PRO-002** 🟢 |
| O4 | Quality control | Roxane Wicky (Managing Director) | Verify part conformity before shipment, manage NCs and corrective actions, analyse client returns | PRO-NCF-001, PRO-ACR-001, FOR-CTR-001 |

### Support processes

| Code | Process | Process owner | Purpose | Associated document(s) |
|---|---|---|---|---|
| S1 | Document management | Roxane Wicky (Managing Director) | Control QMS documents and records (FileMaker, emails, WeChat). Ensure traceability and feed continual improvement. Cloud backup at the provider 🟢 | PRO-DOC-001 |
| S2 | Competencies and training | Roxane Wicky (Managing Director) | Maintain and develop the competencies necessary for industrial coordination | FOR-CMP-001 |
| S3 | Resources and infrastructure | Roxane Wicky (Managing Director) | Manage human, material, digital and external resources. Infrastructure (FileMaker, email, WeChat, cloud). Work environment (confidentiality, reliability, responsiveness). External resources (Yuyao, Whang, freight forwarders). Accounting via fiduciary Paradiso 🟢 | CTX-QUA-001 (section 7) 🟢 |

---

## 3. Process interactions

### Interaction matrix

| From / To | O1 Commercial | O2 Purchasing/Subcontracting | O3 Logistics/Delivery | O4 Quality control |
|---|---|---|---|---|
| **O1 Commercial** | - | Client specifications, requirements, drawings, deadlines | Delivery deadline promised to the client | Client quality requirements |
| **O2 Purchasing/Subcontracting** | Manufacturing lead time, feasibility feedback, price | - | Products ready for shipment, export documents | Inspection reports, products to be checked |
| **O3 Logistics/Delivery** | Delivery confirmation, transport tracking | Coordination of shipment dates | - | Transport documents, receipt notifications |
| **O4 Quality control** | NC information, satisfaction feedback | Manufacturing NC feedback, replacement request | Transport/delivery NC feedback | - |

### Main flow (from client request to delivery)

```
 1. RECEIPT OF CLIENT REQUEST (O1 - Commercial)
    Request received by email (order, quotation, modification, complaint)
    or by telephone in case of emergency
            |
            v
 2. PRELIMINARY ANALYSIS AND ORDER REVIEW (O1/O2/O4 - cf. M1-DIR-001)
    Analysis according to responsibilities defined in M1 Leadership:
    - Understanding of needs: O1 Commercial
    - References, quantities, deadlines: O1 Commercial
    - Technical and logistical feasibility: O2 Purchasing & Subcontracting
    - Applicable quality requirements: O4 Quality control
    - If change: impact analysis by process (clause 6.3)
      and client validation before implementation
            |
            v
 3. CONSULTATION OF INDUSTRIAL PARTNERS (O1/O2/O3)
    Confirmation with Chinese partners:
    - Feasibility and production conditions: O1
    - Manufacturing deadlines and conditions: O2
    - Delivery deadlines and conditions: O3
            |
            v
 4. VALIDATION AND REGISTRATION (O1/S1)
    - Registration in FileMaker (order + production sheet)
    - Order acknowledgement sent to the client (quantities, price, deadline)
            |
            v
 5. TECHNICAL COORDINATION (O2 - Purchasing)
    Exchanges by email and WeChat with Yuyao Mould Factory
    and/or Whang depending on the project (moulds/parts or screws)
    Technical back-and-forth until validation
            |
            v
 6. PRODUCTION LAUNCH (O2 - Purchasing)
    Order confirmation to the Chinese partner(s)
    Production monitoring (photos, progress reports, WeChat exchanges)
    Sending of samples to clients and to Plus Sarl if necessary
            |
            v
 7. PRE-SHIPMENT QUALITY CONTROL (O4)
    Conformity check: technical requirements + order
    The partner carries out a QC before shipment
    + sending of samples to Plus Sarl in parallel with transport
            |
            v
 8. LOGISTICS PREPARATION (O3 - Logistics)
    Creation of delivery sheet in FileMaker
    Compliant customs documents (EU and CH legislation)
    Transport organisation (air/sea/rail)
            |
            v
 9. TRANSPORT MONITORING (O3 - Logistics)
    Monitoring of shipment to final delivery
            |
            v
10. CONFIRMATION OF RECEIPT BY CLIENT (O3/O1)
    The client confirms proper receipt of goods
            |
            +---> If NON-CONFORMING: NC Process (O4 - Quality control)
            |     Creation of NC sheet, analysis, decision on treatment,
            |     corrective actions (cf. PRO-NCF-001, PRO-ACR-001)
            |
            v
11. INVOICING AND FOLLOW-UP (O1 - Commercial)
    Final invoicing, client satisfaction monitoring
            |
            v
12. TRACEABILITY AND IMPROVEMENT (S1 - Document management)
    Retention of information in FileMaker and emails/WeChat
    Feed into: NC monitoring, internal audit, management review
```

> **v0.4:** The flow now integrates the **order review** (step 2) formalised in accordance with section 2.2.1 of the quality manual, with assignment of responsibilities by process according to M1-DIR-001. Any subsequent modification requested by the client is subject to analysis, partner validation if necessary, client confirmation by email and a FileMaker update.
>
> **v0.4 (UPDATE 6.3):** Step 2 now integrates **planning of changes** (clause 6.3 ISO 9001). Any change likely to impact conformity, delivery times, commercial conditions or organization is subject to an impact analysis by process (O1-O4), client information/validation and controlled implementation. Changes are reviewed during the management review (M3). See CTX-QUA-001 section 6.

---

## 4. Quality objectives by process

The quality objectives of Plus Sarl are aligned with the four axes defined in document OBJ-QUA-001:

| Process | Indicator | Objective | Measurement frequency |
|---|---|---|---|
| O1 Commercial | Average response time to client requests | Target: 24h 🟢 | Per request |
| O1 Commercial | Client satisfaction | Absence of major complaints and positive feedback 🟢 | Annual |
| O2 Purchasing/Subcontracting | Number of nonconformities per client | Maximum 3 NC per client per year 🟢 | Per delivery |
| O2 Purchasing/Subcontracting | Replacement time in case of NC | According to client need 🟢 | Per NC |
| O3 Logistics/Delivery | On-time delivery compliance | 95% of deliveries on time 🟢 | Per delivery |
| O3 Logistics/Delivery | Delivery compliance - Sea/rail transport | +/- 10 days from the target 🟢 | Per delivery |
| O3 Logistics/Delivery | Delivery compliance - Air transport | +/- 3 days from the target 🟢 | Per delivery |
| O4 Quality control | Number of NCs and closed corrective actions | 100% processed 🟢 | Quarterly |
| M2 Continual improvement | Number of corrective actions completed on time | 100% 🟢 | Quarterly |
| M3 Management review | Effective holding of management review | At least once per year 🟢 | Annual |
| S1 Document management | Documents up to date in FileMaker | 100% 🟢 | Annual |
| S2 Competencies | Competency maintenance (training, monitoring) | 🔴 [TO BE COMPLETED — diplomas and training not disclosed] | Annual |

---

## 5. Tools and software used

| Tool | Use in the QMS |
|---|---|
| **FileMaker** | Main database: recording of administrative information, order tracking, document management |
| **Email** | Primary communication with European clients and Chinese partners, exchange traceability |
| **WeChat** | Daily technical communication with Chinese partners (quick exchanges, photos, production monitoring) |

### Data backup

Data is backed up in the **cloud, hosted at the provider**. 🟢

---

## 6. Scope exclusion

| Excluded clause | Justification |
|---|---|
| **8.3 - Design and development** | Plus Sarl does not carry out any design activities. Designs (drawings, technical specifications, intellectual property) are provided by the clients and belong exclusively to them. Plus Sarl acts as an industrial coordinator for the production of these designs with Chinese partners. |

---

## Revision History

| Version | Date | Modification | Author |
|---|---|---|---|
| 1.0 | 10/02/2026 | Initial creation | Roxane Wicky |
| 0.2 | 10/02/2026 | Update of quality objectives by process with confirmed targets: 24h response, max 3 NC/client/year, 95% on-time deliveries, absence of major complaints | Roxane Wicky |
| 0.3 | 12/02/2026 | Integration of responses (Whang, Paradiso, SQS, cloud backup). Addition of field legend system. | Roxane Wicky |
| 0.4 | 18/02/2026 | Integration of sections 2.1, 2.2, 2.2.1 of the quality manual. Addition of Associated Documents column. Revision of the main flow with order review (step 2), partner consultation (step 3), reference to M1-DIR-001. Addition of step 12 (traceability and improvement, S1). Addition of new documents PRO-LOG-001, FIC-PRO-002, M1-DIR-001. | Roxane Wicky |
| 0.4 | 20/02/2026 | Integration UPDATE 6.3: enrichment of M1 (planning of changes, clause 6.3), enrichment of M2 (review of change effectiveness), addition of clause 6.3 impact analysis in the main flow (step 2). | Roxane Wicky |
