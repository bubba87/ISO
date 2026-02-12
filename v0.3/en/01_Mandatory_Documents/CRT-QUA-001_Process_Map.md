# Process Map

| | |
|---|---|
| **Reference** | CRT-QUA-001 |
| **Version** | 0.3 |
| **Creation date** | 10/02/2026 |
| **Revision date** | 12/02/2026 |
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

| Code | Process | Process owner | Purpose |
|---|---|---|---|
| M1 | Leadership and strategy | Roxane Wicky (Managing Director) | Define the quality policy, strategic objectives and guide the company |
| M2 | Continuous improvement | Roxane Wicky (Managing Director) | Drive QMS improvement (non-conformities, corrective actions, indicators) |
| M3 | Management review | Roxane Wicky (Managing Director) | Evaluate QMS performance and decide on improvement actions |

### Operational processes

| Code | Process | Process owner | Purpose |
|---|---|---|---|
| O1 | Commercial | Roxane Wicky (Managing Director) | Manage client relationships (~10 active clients), analyse needs, prepare quotations, track orders |
| O2 | Purchasing and subcontracting | Roxane Wicky (Managing Director) | Coordinate Chinese partners (Yuyao Mould Factory and **Whang**), monitor production 🟢 |
| O3 | Logistics and delivery | Roxane Wicky (Managing Director) | Organise international transport (air, sea, rail), manage customs, ensure delivery |
| O4 | Quality control | Roxane Wicky (Managing Director) | Manage non-conformities, implement corrective actions, track complaints |

### Support processes

| Code | Process | Process owner | Purpose |
|---|---|---|---|
| S1 | Document management | Roxane Wicky (Managing Director) | Control QMS documents and records (FileMaker, emails, files). Cloud backup at the provider 🟢 |
| S2 | Competencies and training | Roxane Wicky (Managing Director) | Maintain and develop the competencies necessary for industrial coordination |
| S3 | Resources and infrastructure | Roxane Wicky (Managing Director) | Manage material, IT and financial resources. Accounting via fiduciary Paradiso 🟢 |

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
 1. CLIENT REQUEST RECEIVED
    The client sends their request by email (drawings, specifications, needs)
            |
            v
 2. NEEDS ANALYSIS (O1 - Commercial)
    Analysis of needs, technical specifications and deadlines
            |
            v
 3. ADMINISTRATIVE REGISTRATION (S1 - Document management)
    Administrative information is recorded in FileMaker
            |
            v
 4. TECHNICAL COORDINATION WITH CHINESE PARTNERS (O2 - Purchasing)
    Exchanges by email and WeChat with Yuyao Mould Factory
    and/or Whang depending on the project (moulds/parts or screws)
            |
            v
 5. ITERATIVE TECHNICAL EXCHANGES (O2 - Purchasing)
    Back-and-forth until validation of the solution
    (feasibility, materials, tolerances, price)
            |
            v
 6. PREPARATION OF ORDER DOCUMENTS (O1/O2)
    Customs invoice, client invoice, delivery note,
    order acknowledgement
            |
            v
 7. PRODUCTION LAUNCH (O2 - Purchasing)
    Order confirmation to the Chinese partner(s)
    Production monitoring (photos, progress reports, WeChat exchanges)
            |
            v
 8. PRE-SHIPMENT QUALITY CONTROL (O2/O4)
    The partner carries out a quality control before shipment
    + sending of samples to Plus Sarl in parallel with transport
    to the client
            |
            v
 9. PREPARATION OF EXPORT DOCUMENTS (O3 - Logistics)
    Customs documents, transport organisation
    (air, sea or rail depending on urgency and volume)
            |
            v
10. TRANSPORT MONITORING (O3 - Logistics)
    Monitoring of shipment to destination
            |
            v
11. CONFIRMATION OF RECEIPT BY CLIENT (O3/O1)
    The client confirms proper receipt of goods
            |
            +---> If NON-CONFORMING: NC Process (O4 - Quality control)
            |     Complaint management, corrective action,
            |     replacement coordination with Chinese partner
            |
            v
12. INVOICING AND FOLLOW-UP (O1 - Commercial)
    Final invoicing, client satisfaction monitoring
```

---

## 4. Quality objectives by process

The quality objectives of Plus Sarl are aligned with the four axes defined in document OBJ-QUA-001:

| Process | Indicator | Objective | Measurement frequency |
|---|---|---|---|
| O1 Commercial | Average response time to client requests | Target: 24h 🟢 | Per request |
| O1 Commercial | Client satisfaction | Absence of major complaints and positive feedback 🟢 | Annual |
| O2 Purchasing/Subcontracting | Number of non-conformities per client | Maximum 3 NC per client per year 🟢 | Per delivery |
| O2 Purchasing/Subcontracting | Replacement time in case of NC | According to client need 🟢 | Per NC |
| O3 Logistics/Delivery | On-time delivery compliance | 95% of deliveries on time 🟢 | Per delivery |
| O3 Logistics/Delivery | Delivery compliance - Sea/rail transport | +/- 10 days from the target 🟢 | Per delivery |
| O3 Logistics/Delivery | Delivery compliance - Air transport | +/- 3 days from the target 🟢 | Per delivery |
| O4 Quality control | Number of NCs and closed corrective actions | 100% processed 🟢 | Quarterly |
| M2 Continuous improvement | Number of corrective actions completed on time | 100% 🟢 | Quarterly |
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
