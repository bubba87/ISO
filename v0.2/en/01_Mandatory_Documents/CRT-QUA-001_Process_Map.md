# Process Map

| | |
|---|---|
| **Reference** | CRT-QUA-001 |
| **Version** | 0.2 |
| **Creation date** | 10/02/2026 |
| **Revision date** | 10/02/2026 |
| **Written by** | Roxane Wicky |
| **Approved by** | Roxane Wicky |

---

## 1. Process overview

### Context

Plus Sarl specializes in industrial coordination between European clients and Chinese manufacturing partners. The company does not carry out any design activity (clause 8.3 of the ISO 9001:2015 standard excluded from the scope). Designs and intellectual property belong to the clients. The business covers commercial coordination, purchasing and subcontracting with Chinese partners, international logistics organization and quality control.

### Process map representation

```
+=========================================================================+
|                    MANAGEMENT PROCESSES                                   |
|  +-------------------+  +-------------------+  +---------------------+  |
|  | M1 - Leadership   |  | M2 - Continuous   |  | M3 - Management    |  |
|  | and strategy      |  | improvement       |  | review             |  |
|  +-------------------+  +-------------------+  +---------------------+  |
+=========================================================================+
                                    |
  CUSTOMER                          v                           CUSTOMER
  REQUIREMENTS +====================================================+ SATISFACTION
  -----------> |              OPERATIONAL PROCESSES                  | -------->
               |                                                      |
               |  +----------+  +----------+  +----------+  +------+  |
               |  | O1       |  | O2       |  | O3       |  | O4   |  |
               |  | Sales    |->| Purchasing|->| Logis-  |->| Qual.|  |
               |  |          |  | & Sub-   |  | tics &  |  | Con- |  |
               |  |          |  | contract.|  | Delivery|  | trol |  |
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

**Note:** Clause 8.3 (Design and development) is excluded from the scope. Designs are the property of the clients. Plus Sarl acts as an industrial coordinator and does not carry out any design activity.

---

## 2. Process list

### Management processes

| Code | Process | Owner | Objective |
|---|---|---|---|
| M1 | Leadership and strategy | Roxane Wicky (Managing Director) | Define the quality policy, strategic objectives and guide the company |
| M2 | Continuous improvement | Roxane Wicky (Managing Director) | Drive QMS improvement (non-conformities, corrective actions, indicators) |
| M3 | Management review | Roxane Wicky (Managing Director) | Evaluate QMS performance and decide on improvement actions |

### Operational processes

| Code | Process | Owner | Objective |
|---|---|---|---|
| O1 | Sales | Roxane Wicky (Managing Director) | Manage customer relationships, analyze needs, prepare offers, monitor orders |
| O2 | Purchasing and subcontracting | Roxane Wicky (Managing Director) | Coordinate Chinese partners (Yuyao Mould Factory and second partner), monitor production |
| O3 | Logistics and delivery | Roxane Wicky (Managing Director) | Organize international transport (air, sea, rail), manage customs, ensure delivery |
| O4 | Quality control | Roxane Wicky (Managing Director) | Manage non-conformities, implement corrective actions, monitor complaints |

### Support processes

| Code | Process | Owner | Objective |
|---|---|---|---|
| S1 | Document management | Roxane Wicky (Managing Director) | Control QMS documents and records (FileMaker, emails, files) |
| S2 | Competencies and training | Roxane Wicky (Managing Director) | Maintain and develop competencies required for industrial coordination |
| S3 | Resources and infrastructure | Roxane Wicky (Managing Director) | Manage material, IT and financial resources |

---

## 3. Process interactions

### Interaction matrix

| From / To | O1 Sales | O2 Purchasing/Subcontracting | O3 Logistics/Delivery | O4 Quality control |
|---|---|---|---|---|
| **O1 Sales** | - | Customer specifications, technical requirements, drawings, deadlines | Delivery deadline promised to the customer | Customer quality requirements |
| **O2 Purchasing/Subcontracting** | Manufacturing lead time, feasibility feedback, price | - | Products ready for shipment, export documents | Inspection reports, products to be inspected |
| **O3 Logistics/Delivery** | Delivery confirmation, transport tracking | Shipment date coordination | - | Transport documents, receipt notices |
| **O4 Quality control** | NC information, satisfaction feedback | Manufacturing NC feedback, replacement request | Transport/delivery NC feedback | - |

### Main flow (from customer request to delivery)

```
 1. RECEIPT OF CUSTOMER REQUEST
    The customer sends their request by email (drawings, specifications, requirements)
            |
            v
 2. REQUIREMENTS ANALYSIS (O1 - Sales)
    Analysis of needs, technical specifications and deadlines
            |
            v
 3. ADMINISTRATIVE REGISTRATION (S1 - Document management)
    Administrative information is recorded in FileMaker
            |
            v
 4. TECHNICAL COORDINATION WITH CHINESE PARTNERS (O2 - Purchasing)
    Exchanges by email and WeChat with Yuyao Mould Factory
    (and/or second partner depending on the project)
            |
            v
 5. ITERATIVE EXCHANGES (O2 - Purchasing)
    Technical back-and-forth until solution validation
    (feasibility, materials, tolerances, price)
            |
            v
 6. PREPARATION OF ORDER DOCUMENTS (O1/O2)
    Customs invoice, customer invoice, delivery note,
    order acknowledgment
            |
            v
 7. PRODUCTION LAUNCH (O2 - Purchasing)
    Order confirmation with the Chinese partner(s)
    Production monitoring (photos, progress reports, WeChat exchanges)
            |
            v
 8. PREPARATION OF EXPORT DOCUMENTS (O3 - Logistics)
    Customs documents, transport organization
    (air, sea or rail depending on urgency and volume)
            |
            v
 9. TRANSPORT MONITORING (O3 - Logistics)
    Tracking of shipment to destination
            |
            v
10. RECEIPT CONFIRMATION BY THE CUSTOMER (O3/O1)
    The customer confirms proper receipt of goods
            |
            +---> If NON-CONFORMING: NC process (O4 - Quality control)
            |     Complaint handling, corrective action,
            |     replacement coordination with Chinese partner
            |
            v
11. INVOICING AND FOLLOW-UP (O1 - Sales)
    Final invoicing, customer satisfaction monitoring
```

---

## 4. Quality objectives by process

The quality objectives of Plus Sarl are aligned with the four strategic areas defined in document OBJ-QUA-001:

| Process | Indicator | Objective | Measurement frequency |
|---|---|---|---|
| O1 Sales | Average response time to customer requests | Target: 24h | Per request |
| O1 Sales | Customer satisfaction | No major complaints and positive feedback | Annual |
| O2 Purchasing/Subcontracting | Number of non-conformities per customer | Maximum 3 NCs per customer per year | Per delivery |
| O2 Purchasing/Subcontracting | Replacement lead time in case of NC | According to customer needs | Per NC |
| O3 Logistics/Delivery | On-time delivery compliance | 95% of deliveries on time | Per delivery |
| O3 Logistics/Delivery | On-time delivery - Sea/rail transport | +/- 10 days from target | Per delivery |
| O3 Logistics/Delivery | On-time delivery - Air transport | +/- 3 days from target | Per delivery |
| O4 Quality control | Number of NCs and corrective actions closed out | 100% processing | Quarterly |
| M2 Improvement | Number of corrective actions completed on time | 100% | Quarterly |
| M3 Management review | Management review effectively held | At least once a year | Annual |
| S1 Document management | Documents up to date in FileMaker | 100% | Annual |
| S2 Competencies | Competency maintenance (training, watch) | [TO BE CONFIRMED] | Annual |

---

## 5. Tools and software used

| Tool | Use in the QMS |
|---|---|
| **FileMaker** | Main database: recording of administrative information, order tracking, document management |
| **Email** | Main communication with European clients and Chinese partners, exchange traceability |
| **WeChat** | Daily technical communication with Chinese partners (quick exchanges, photos, production monitoring) |

---

## 6. Scope exclusion

| Excluded clause | Justification |
|---|---|
| **8.3 - Design and development** | Plus Sarl does not carry out any design activity. Designs (drawings, technical specifications, intellectual property) are provided by the clients and belong exclusively to them. Plus Sarl acts as an industrial coordinator for putting these designs into production with the Chinese partners. |

---

## Revision history

| Version | Date | Modification | Author |
|---|---|---|---|
| 1.0 | 10/02/2026 | Initial creation | Roxane Wicky |
| 0.2 | 10/02/2026 | Update of quality objectives by process with confirmed targets: 24h response, max 3 NCs/customer/year, 95% on-time deliveries, no major complaints | Roxane Wicky |
