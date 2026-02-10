# Process Map

| | |
|---|---|
| **Reference** | MAP-QUA-001 |
| **Version** | 1.0 |
| **Date created** | [DD/MM/YYYY] |
| **Date revised** | [DD/MM/YYYY] |
| **Drafted by** | [Name of the managing director] |
| **Approved by** | [Name of the managing director] |

---

## 1. Process Overview

### Process Map Representation

```
+=========================================================================+
|                      MANAGEMENT PROCESSES                                |
|  +-------------------+  +-------------------+  +---------------------+  |
|  | M1 - Leadership   |  | M2 - Continual   |  | M3 - Management     |  |
|  | and Strategy      |  | Improvement       |  | Review              |  |
|  +-------------------+  +-------------------+  +---------------------+  |
+=========================================================================+
                                    |
  CUSTOMER                          v                           CUSTOMER
  REQUIREMENTS +====================================================+ SATISFACTION
  -----------> |              OPERATIONAL PROCESSES                  | ----------->
               |                                                      |
               |  +----------+  +----------+  +----------+  +------+  |
               |  | O1       |  | O2       |  | O3       |  | O4   |  |
               |  | Sales    |->| Design   |->| Purchas- |->| In-  |  |
               |  |          |  | & Dev.   |  | ing &    |  | spec-|  |
               |  |          |  |          |  | Sub-     |  | tion |  |
               |  |          |  |          |  | contract.|  | &    |  |
               |  |          |  |          |  |          |  | Del. |  |
               |  +----------+  +----------+  +----------+  +------+  |
               +====================================================+
                                    |
+=========================================================================+
|                      SUPPORT PROCESSES                                    |
|  +-------------------+  +-------------------+  +---------------------+  |
|  | S1 - Document     |  | S2 - Competence   |  | S3 - Resource &     |  |
|  | and record        |  | and training       |  | infrastructure      |  |
|  | management        |  | management         |  | management          |  |
|  +-------------------+  +-------------------+  +---------------------+  |
+=========================================================================+
```

---

## 2. Process List

### Management Processes

| Code | Process | Owner | Objective |
|---|---|---|---|
| M1 | Leadership and Strategy | Director | Define the policy, objectives and strategy of the company |
| M2 | Continual Improvement | Director | Drive QMS improvement (NCs, corrective actions, KPIs) |
| M3 | Management Review | Director | Evaluate QMS performance and decide on actions |

### Operational Processes

| Code | Process | Owner | Objective |
|---|---|---|---|
| O1 | Sales | Director | Understand customer needs, prepare quotations, manage orders |
| O2 | Design and Development | Director | Design molds according to customer requirements |
| O3 | Purchasing and Subcontracting | Director | Manage Chinese partner, order, monitor manufacturing |
| O4 | Inspection and Delivery | Director | Verify conformity and deliver products to customers |

### Support Processes

| Code | Process | Owner | Objective |
|---|---|---|---|
| S1 | Document Management | Director | Control QMS documents and records |
| S2 | Competence and Training | Director | Maintain and develop competences |
| S3 | Resources and Infrastructure | Director | Manage material and financial resources |

---

## 3. Process Interactions

### Interaction Matrix

| From / To | O1 Sales | O2 Design | O3 Purchasing | O4 Inspection |
|---|---|---|---|---|
| **O1 Sales** | - | Customer requirements, specifications | - | Promised delivery date |
| **O2 Design** | Technical quotation | - | Mold specifications, drawings | Inspection criteria |
| **O3 Purchasing** | Manufacturing lead time | Feasibility feedback | - | Products to inspect |
| **O4 Inspection** | Delivery confirmation | Design NC feedback | Manufacturing NC feedback | - |

### Main Flow (from customer request to delivery)

```
1. CUSTOMER: Sends a request (drawing, specifications, or need)
       |
       v
2. O1 - SALES: Analyzes the request, prepares quotation
       |
       v
3. CUSTOMER: Confirms the order
       |
       v
4. O1 - SALES: Order review (requirement verification)
       |
       v
5. O2 - DESIGN: Develops the mold (specifications, drawings, material selection)
       |
       v
6. O2 - DESIGN: Design review (internal validation before sending)
       |
       v
7. O3 - PURCHASING: Transmits specifications to Chinese partner
       |
       v
8. O3 - PURCHASING: Monitors manufacturing (exchanges, milestones, photos, reports)
       |
       v
9. O3 - PURCHASING: Receipt of molds/parts in Switzerland
       |
       v
10. O4 - INSPECTION: Incoming inspection (dimensional, visual, functional)
       |
       +---> If NONCONFORMING: NC process (PRO-NCR-001)
       |
       v
11. O4 - DELIVERY: Preparation and shipping to customer
       |
       v
12. CUSTOMER: Receipt and acceptance
       |
       v
13. O1 - SALES: Satisfaction follow-up, invoicing
```

---

## 4. Indicators per Process

| Process | Indicator | Target | Measurement Frequency |
|---|---|---|---|
| O1 Sales | Quotation conversion rate | [> XX%] | Quarterly |
| O1 Sales | Number of customer complaints | [< X per year] | Monthly |
| O2 Design | Number of modifications after validation | [< X per project] | Per project |
| O3 Purchasing | Supplier delivery conformity rate | [> 95%] | Per delivery |
| O3 Purchasing | Supplier on-time delivery rate | [> 90%] | Per delivery |
| O4 Inspection | Incoming conformity rate | [> 95%] | Per receipt |
| O4 Delivery | Customer on-time delivery rate | [> 90%] | Per delivery |
| M2 Improvement | Number of closed corrective actions | [100% within deadlines] | Quarterly |
| S2 Competence | Annual training hours | [> X hours] | Annual |

---

> **Filling Instructions:**
> 1. Adapt the processes to YOUR reality (add or remove if necessary)
> 2. Define realistic targets for each indicator
> 3. Complete the process interactions
> 4. This document is the "map" of your QMS - the auditor will use it as a guide
> 5. If you do NOT do design, remove process O2
