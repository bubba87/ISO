# P02 - Purchasing and Subcontracting Process

| **Process**         | P02 - Purchasing and Subcontracting                  |
|----------------------|------------------------------------------------------|
| **Type**            | Operational                                           |
| **Owner**           | Purchasing Role                                       |
| **Version**         | v0.7                                                  |
| **Date**            | 2026-03-04                                            |
| **Reference**       | PR-P02-ACH                                            |
| **ISO 9001 Standard** | Clauses 8.4, 8.6                                   |

---

## 1. Purpose and scope

This process describes the purchasing and subcontracting activities of **Plus Sarl** for its international industrial monitoring and sourcing operations. It covers the selection, qualification and evaluation of suppliers worldwide, as well as order management and receipt of products/services.

---

## 2. Normative references

- ISO 9001:2015, Clauses 8.4 (Control of externally provided processes, products and services), 8.6 (Release of products and services)
- Plus Sarl Quality Manual (MQ-001)

---

## 3. Roles and responsibilities

| Role                        | Key responsibilities                                                 |
|-----------------------------|----------------------------------------------------------------------|
| **Purchasing**              | Sourcing, negotiation, orders, supplier follow-up                    |
| **Quality**                 | Supplier qualification, audits, monitoring of nonconformities        |
| **Management**              | Approval of strategic suppliers, budgets                             |
| **Logistics**               | Coordination of receipts and international transport                 |
| **Supplier**                | Compliant delivery, adherence to SQA, communication                  |

---

## 4. Input and output data

### Input data
- Purchasing needs from process P01 (Sales)
- Specifications / technical requirements
- Existing supplier panel
- Supplier performance history
- Applicable regulatory requirements by country

### Output data
- Approved purchase orders
- Signed Supplier Quality Agreement (SQA)
- Supplier evaluation (FM-P02-EVAL)
- Updated supplier panel
- Compliant products/services received

---

## 5. Description of activities

### A1 - Identification of purchasing need

The Purchasing Role receives the purchasing need from process P01 or from an internal requirement. It verifies the completeness of specifications and identifies potential international sourcing options.

### A2 - Supplier search and pre-selection

The Purchasing Role identifies potential suppliers in international markets, analyses their capabilities and carries out a pre-selection based on defined criteria (capacity, certifications, location, references).

### A3 - Supplier qualification

The Purchasing Role, in coordination with the Quality Role, carries out the qualification of pre-selected suppliers: on-site or remote audit, verification of certifications, assessment of production capabilities, signing of the Supplier Quality Agreement (FM-P02-AQF).

### A4 - Consultation and negotiation

The Purchasing Role issues requests for quotation to qualified suppliers, compares offers (price, lead times, terms, Incoterms) and conducts negotiations.

### A5 - Order placement

The Purchasing Role issues the purchase order with complete specifications, quality requirements, delivery deadlines and logistics conditions (Incoterms, transport mode).

### A6 - Order follow-up and reminders

The Purchasing Role monitors the execution of the order with the supplier, verifies compliance with deadlines and issues reminders as needed.

### A7 - Receipt and inspection

The Purchasing Role coordinates with the Logistics Role and the Quality Role for the receipt of products/services. The inspections defined by process P04 are triggered (IPC, DUPRO, PSI, Loading Check as applicable).

### A8 - Periodic supplier evaluation

The Purchasing Role, in coordination with the Quality Role, carries out periodic supplier evaluation according to the weighted criteria defined in FM-P02-EVAL. Suppliers are classified A/B/C and the panel is updated.

---

## 6. Swimlane diagram

```
 PROCESS P02 - PURCHASING AND SUBCONTRACTING
 ============================================================================

 Role                 | Activity flow
 ============================================================================
                      |
 PURCHASING           |  [A1 Identify]     [A2 Search]        [A4 Consult]
                      |  the purchasing --> and pre-       --> and negotiate
                      |  need               select             offers
                      |      |              suppliers              |
                      |      |                   |                 v
                      |      |                   v           [A5 Place]
                      |      |              [A3 Qualify]     the order
                      |      |              suppliers        (PO + specs)
                      |      |              (with Quality)        |
                      |      |                   |                 v
                      |      |                   v           [A6 Monitor]
                      |      |              Sign SQA         the order
                      |      |              (FM-P02-AQF)     and follow up
                      |      |                                    |
                      |      |                                    v
                      |      |                              [A7 Receive]
                      |      |                              and inspect
                      |      |                                    |
                      |      |                                    v
                      |      +----------------------------->[A8 Evaluate]
                      |                                     suppliers
                      |                                     (FM-P02-EVAL)
                      |                                     Classification A/B/C
                      |
 ============================================================================
                      |
 QUALITY              |  Participate in --> Audit         --> Inspect at
                      |  qualification      suppliers         receipt
                      |  (criteria)         (on-site or       (P04)
                      |                     remote)
                      |
 ============================================================================
                      |
 MANAGEMENT           |  Approve strategic suppliers
                      |  Approve purchasing budgets
                      |
 ============================================================================
                      |
 LOGISTICS            |  Coordinate    --> Organise      --> Confirm
                      |  international     receipt of        receipt
                      |  transport         products
                      |
 ============================================================================
                      |
 SUPPLIER             |  Respond to    --> Sign         --> Deliver       --> Handle
                      |  consultations     the SQA         in compliance      NCs
                      |
 ============================================================================
```

---

## 7. Interactions with other processes

| Process                | Nature of interaction                                  |
|------------------------|--------------------------------------------------------|
| PM01 - Leadership        | Purchasing strategy approval, budgets                 |
| P01 - Sales            | Receipt of customer needs, feasibility feedback        |
| P04 - Logistics        | International transport and receipt coordination       |
| P03 - Quality Control  | Source inspections, incoming inspection                 |
| PS01 - Document Management | Archiving of SQAs, evaluations, orders              |

---

## 8. Key Performance Indicators (KPI)

| Indicator                                 | Formula / Method                                | Target         | Frequency    |
|-------------------------------------------|------------------------------------------------|----------------|--------------|
| Delivery conformity rate                  | Compliant deliveries / Total deliveries x 100  | >= 95 %        | Monthly      |
| Supplier on-time delivery rate            | On-time deliveries / Total deliveries x 100    | >= 90 %        | Monthly      |
| Number of qualified suppliers             | Count of suppliers classified A or B           | Upward trend   | Semi-annual  |
| Supplier nonconformity rate               | Supplier NCs / Total receipts x 100            | < 5 %          | Monthly      |
| Average order processing time             | Sum of lead times / Number of orders           | < 5 days       | Monthly      |
| Evaluation completion rate                | Evaluations completed / Evaluations planned    | 100 %          | Annual       |

---

## 9. Associated documents and records

| Code         | Title                                 | Type          |
|--------------|---------------------------------------|---------------|
| PR-P02-ACH   | Purchasing and Subcontracting Procedure | Procedure   |
| FM-P02-AQF   | Supplier Quality Agreement            | Form          |
| FM-P02-EVAL  | Supplier Evaluation                   | Form          |
| FM-P02-BC    | Purchase Order                        | Form          |
| EN-P02-PAN   | Supplier Panel                        | Record        |

---

## 10. Continual improvement

Improvement of the purchasing process is based on:
- Analysis of supplier evaluations and trends
- Monitoring of supplier-related nonconformities
- Optimisation of procurement lead times and costs
- Geographical diversification of the supplier panel
- Feedback from inspections (P04)

---

*Controlled document - Plus Sarl - ISO 9001:2015 Quality Management System*
*Version v0.7 - 2026-03-04*
