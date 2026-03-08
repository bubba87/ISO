# P02 - Purchasing and Subcontracting Process

| **Process**         | P02 - Purchasing and Subcontracting                  |
|----------------------|------------------------------------------------------|
| **Type**            | Core                                                  |
| **Owner**           | Purchasing Role                                       |
| **Version**         | v0.7                                                  |
| **Date**            | 2026-03-04                                            |
| **Reference**       | PR-P02-ACH                                            |
| **ISO 9001 Standard** | Clauses 8.4, 8.6                                   |

---

## 1. Purpose and Scope

This process describes the purchasing and subcontracting activities of **Plus Sàrl** for its international industrial follow-up and sourcing operations. It covers the selection, qualification, and evaluation of suppliers worldwide, as well as order management and product/service receipt.

---

## 2. Normative References

- ISO 9001:2015, Clauses 8.4 (Control of Externally Provided Processes, Products and Services), 8.6 (Release of Products and Services)
- Plus Sàrl Quality Manual (MQ-001)

---

## 3. Roles and Responsibilities

| Role                        | Key Responsibilities                                                 |
|-----------------------------|----------------------------------------------------------------------|
| **Purchasing**              | Sourcing, negotiation, orders, supplier monitoring                   |
| **Quality**                 | Supplier qualification, audits, non-conformity monitoring            |
| **Executive Management**    | Validation of strategic suppliers, budgets                           |
| **Logistics**               | Coordination of receipts and international transport                 |
| **Supplier**                | Compliant delivery, adherence to SQA, communication                  |

---

## 4. Input and Output Data

### Input Data
- Purchasing needs from process P01 (Commercial)
- Specifications / technical requirements
- Existing supplier panel
- Supplier performance history
- Applicable regulatory requirements by country

### Output Data
- Approved purchase orders
- Signed Supplier Quality Agreement (SQA)
- Supplier evaluation (FM-P02-EVAL)
- Updated supplier panel
- Compliant products/services received

---

## 5. Activity Description

### A1 - Identification of Purchasing Need

The Purchasing Role receives the purchasing need from process P01 or from an internal requirement. It verifies the completeness of specifications and identifies potential international sourcing options.

### A2 - Supplier Search and Shortlisting

The Purchasing Role identifies potential suppliers in international markets, analyzes their capabilities, and proceeds with shortlisting based on defined criteria (capacity, certifications, location, references).

### A3 - Supplier Qualification

The Purchasing Role, in coordination with the Quality Role, proceeds with the qualification of shortlisted suppliers: on-site or remote audit, certification verification, production capacity assessment, and signature of the Supplier Quality Agreement (FM-P02-AQF).

### A4 - Solicitation and Negotiation

The Purchasing Role issues requests for quotation to qualified suppliers, compares offers (price, lead times, conditions, Incoterms), and conducts negotiations.

### A5 - Order Placement

The Purchasing Role issues the purchase order with complete specifications, quality requirements, delivery timelines, and logistics conditions (Incoterms, mode of transport).

### A6 - Order Tracking and Follow-up

The Purchasing Role monitors order execution with the supplier, verifies compliance with deadlines, and initiates follow-up actions as necessary.

### A7 - Receipt and Inspection

The Purchasing Role coordinates with the Logistics Role and the Quality Role for product/service receipt. Inspections defined by process P04 are initiated (IPC, DUPRO, PSI, Loading Check as applicable).

### A8 - Periodic Supplier Evaluation

The Purchasing Role, in coordination with the Quality Role, conducts periodic supplier evaluations based on weighted criteria defined in FM-P02-EVAL. Suppliers are classified A/B/C and the panel is updated.

---

## 6. Swimlane Diagram

```
 PROCESS P02 - PURCHASING AND SUBCONTRACTING
 ============================================================================

 Role                 | Activity Flow
 ============================================================================
                      |
 PURCHASING           |  [A1 Identify]     [A2 Search]        [A4 Solicit]
                      |  the purchasing --> and shortlist  --> and negotiate
                      |  need               suppliers          offers
                      |      |              fournisseurs           |
                      |      |                   |                 v
                      |      |                   v           [A5 Place]
                      |      |              [A3 Qualify]     the order
                      |      |              suppliers        (PO + specs)
                      |      |              (with Quality)        |
                      |      |                   |                 v
                      |      |                   v           [A6 Track]
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
 QUALITY              |  Participate in --> Audit          --> Inspect at
                      |  qualification      suppliers          receipt
                      |  (criteria)         (on-site or        (P04)
                      |                     remote)
                      |
 ============================================================================
                      |
 EXECUTIVE            |  Validate strategic suppliers
 MANAGEMENT           |  Approve purchasing budgets
                      |
 ============================================================================
                      |
 LOGISTICS            |  Coordinate    --> Organize       --> Confirm
                      |  international     product            receipt
                      |  transport         receipt
                      |
 ============================================================================
                      |
 SUPPLIER             |  Respond to    --> Sign         --> Deliver      --> Handle
                      |  solicitations     SQA              in compliance    NCs
                      |
 ============================================================================
```

---

## 7. Interactions with Other Processes

| Process                | Nature of Interaction                                  |
|------------------------|--------------------------------------------------------|
| PM01 - Leadership      | Purchasing strategy validation, budgets                |
| P01 - Commercial       | Receipt of customer needs, feasibility feedback        |
| P04 - Logistics        | International transport and receipt coordination       |
| P03 - Quality Control  | Source inspections, receipt inspection                  |
| PS01 - Document Management | Archiving of SQAs, evaluations, orders              |

---

## 8. Key Performance Indicators (KPI)

| Indicator                                 | Formula / Method                                   | Target         | Frequency    |
|-------------------------------------------|---------------------------------------------------|----------------|--------------|
| Delivery conformity rate                  | Compliant deliveries / Total deliveries x 100      | >= 95%         | Monthly      |
| Supplier on-time delivery rate            | On-time deliveries / Total deliveries x 100        | >= 90%         | Monthly      |
| Number of qualified suppliers             | Count of suppliers classified A or B               | Upward trend   | Semi-annual  |
| Supplier non-conformity rate              | Supplier NCs / Total receipts x 100                | < 5%           | Monthly      |
| Average order processing time             | Sum of lead times / Number of orders               | < 5 days       | Monthly      |
| Evaluation completion rate                | Evaluations completed / Evaluations planned        | 100%           | Annual       |

---

## 9. Associated Documents and Records

| Code         | Title                                 | Type          |
|--------------|---------------------------------------|---------------|
| PR-P02-ACH   | Purchasing and Subcontracting Procedure | Procedure   |
| FM-P02-AQF   | Supplier Quality Agreement            | Form          |
| FM-P02-EVAL  | Supplier Evaluation                   | Form          |
| FM-P02-BC    | Purchase Order                        | Form          |
| EN-P02-PAN   | Supplier Panel                        | Record        |

---

## 10. Continual Improvement

Improvement of the purchasing process is based on:
- Analysis of supplier evaluations and trends
- Monitoring of supplier-related non-conformities
- Optimization of lead times and procurement costs
- Geographic diversification of the supplier panel
- Feedback from inspections (P04)

---

*Controlled document - Plus Sàrl - ISO 9001:2015 Quality Management System*
*Version v0.7 - 2026-03-04*
