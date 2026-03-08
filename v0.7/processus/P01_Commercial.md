# P01 - Commercial Process

| **Process**         | P01 - Commercial                                      |
|----------------------|------------------------------------------------------|
| **Type**            | Core                                                  |
| **Owner**           | Commercial Role                                       |
| **Version**         | v0.7                                                  |
| **Date**            | 2026-03-04                                            |
| **Reference**       | PR-P01-COM                                            |
| **ISO 9001 Standard** | Clauses 8.2, 8.5, 9.1.2                            |

---

## 1. Purpose and Scope

This process describes the commercial activities of **Plus Sàrl** from the receipt of a customer request to the measurement of satisfaction. It covers the entire commercial cycle for industrial follow-up and sourcing activities on a global scale.

---

## 2. Normative References

- ISO 9001:2015, Clauses 8.2 (Requirements for Products and Services), 8.5 (Production and Service Provision), 9.1.2 (Customer Satisfaction)
- Plus Sàrl Quality Manual (MQ-001)

---

## 3. Roles and Responsibilities

| Role                        | Key Responsibilities                                                 |
|-----------------------------|----------------------------------------------------------------------|
| **Commercial**              | Management of inquiries, proposals, contracts, customer follow-up    |
| **Executive Management**    | Validation of strategic proposals, approval of major contracts       |
| **Quality**                 | Support for quality requirements, complaint handling                  |
| **Customer**                | Expression of needs, proposal validation, satisfaction feedback      |

---

## 4. Input and Output Data

### Input Data
- Customer request (specifications, requirements, RFQ)
- Applicable regulatory and normative requirements
- Customer history and commercial terms
- Plus Sàrl service catalogue

### Output Data
- Approved commercial proposal
- Signed contract / purchase order
- Internal execution order
- Customer satisfaction report
- Commercial performance indicators

---

## 5. Activity Description

### A1 - Receipt and Registration of Customer Request

The Commercial Role receives the customer request (email, telephone, online platform), registers it in the tracking system, and assigns a unique reference number.

### A2 - Analysis and Review of Customer Requirements

The Commercial Role analyzes the request to verify technical, logistical, and commercial feasibility. Requirements are reviewed with processes P02 (Purchasing), P03 (Logistics), and P04 (Quality Control) as necessary.

### A3 - Preparation of the Commercial Proposal

The Commercial Role prepares the proposal including: service description, pricing conditions, lead times, delivery conditions (Incoterms), payment terms, and quality requirements.

### A4 - Validation and Submission of the Proposal

The proposal is validated according to defined approval thresholds (Executive Management for strategic proposals) and then transmitted to the customer.

### A5 - Negotiation and Adjustment

The Commercial Role conducts negotiations with the customer, adjusts the proposal as necessary, and documents the modifications made.

### A6 - Contract Finalization

Upon agreement, the Commercial Role formalizes the contract or purchase order, ensures signature by both parties, and triggers the internal execution order.

### A7 - Handover to Operational Processes

The Commercial Role transmits the necessary information to processes P02 (Purchasing/Sourcing), P03 (Logistics), and P04 (Quality Control) for order execution.

### A8 - Execution Monitoring and Customer Communication

The Commercial Role monitors progress with the operational processes and regularly communicates with the customer on the status of their order.

### A9 - Customer Satisfaction Measurement

The Commercial Role manages the measurement of customer satisfaction through surveys (FM-P01-SAT), analysis of feedback, and complaint handling.

---

## 6. Swimlane Diagram

```
 PROCESS P01 - COMMERCIAL
 ============================================================================

 Role                 | Activity Flow
 ============================================================================
                      |
 CUSTOMER             |  Express the     Validate      Negotiate /    Confirm
                      |  need      ----> the proposal  adjust   ----> the order
                      |  (RFQ, specs)    received      conditions     (signature)
                      |      |               ^             ^               |
                      |      v               |             |               v
 ============================================================================
                      |
 COMMERCIAL           |  [A1 Receive]       [A3 Prepare]   [A5 Negotiate]
                      |  and register        the commercial  and adjust
                      |  the request         proposal        the proposal
                      |      |                   ^               |
                      |      v                   |               v
                      |  [A2 Analyze]       [A4 Validate]   [A6 Finalize
                      |  customer            and submit      contract]
                      |  requirements        the proposal    (contract/PO)
                      |      |                                   |
                      |      |    +------------------------------+
                      |      |    |
                      |      v    v
                      |  [A7 Hand over to operational processes]
                      |      |
                      |      v
                      |  [A8 Monitor execution]
                      |  Regular customer communication
                      |      |
                      |      v
                      |  [A9 Measure customer satisfaction]
                      |  (FM-P01-SAT)
                      |
 ============================================================================
                      |
 EXECUTIVE            |  Validate strategic proposals
 MANAGEMENT           |  Approve major contracts
                      |
 ============================================================================
                      |
 QUALITY              |  Quality requirements support
                      |  Complaint handling
                      |
 ============================================================================
                      |
 P02 PURCHASING       |  <--- Receipt of purchasing / sourcing order
 P03 LOGISTICS        |  <--- Receipt of logistics instructions
 P04 QUALITY CONTROL  |  <--- Receipt of quality / inspection requirements
                      |
 ============================================================================
```

---

## 7. Interactions with Other Processes

| Process                | Nature of Interaction                                  |
|------------------------|--------------------------------------------------------|
| PM01 - Leadership      | Commercial reporting, strategic validation             |
| P02 - Purchasing       | Transmission of sourcing needs, feasibility feedback   |
| P04 - Logistics        | Delivery coordination, shipment tracking               |
| P03 - Quality Control  | Definition of required inspections, quality feedback   |
| PS01 - Document Management | Archiving of proposals, contracts, records           |

---

## 8. Key Performance Indicators (KPI)

| Indicator                                 | Formula / Method                                   | Target         | Frequency    |
|-------------------------------------------|---------------------------------------------------|----------------|--------------|
| Proposal conversion rate                  | Proposals accepted / Proposals issued x 100        | >= 30%         | Monthly      |
| Average response time to inquiries        | Sum of response times / Number of inquiries        | < 48 hours     | Monthly      |
| Customer satisfaction rate                | Average score from FM-P01-SAT survey               | >= 4/5         | Quarterly    |
| Number of customer complaints             | Count of complaints received                       | Downward trend | Monthly      |
| Revenue per period                        | Total invoiced orders                              | Per budget     | Monthly      |
| Customer retention rate                   | Recurring customers / Total customers x 100        | >= 60%         | Annual       |
| Average contract finalization time        | Contract date - Initial request date               | < 15 days      | Monthly      |

---

## 9. Associated Documents and Records

| Code         | Title                             | Type          |
|--------------|-----------------------------------|---------------|
| PR-P01-COM   | Commercial Procedure              | Procedure     |
| FM-P01-SAT   | Customer Satisfaction Survey      | Form          |
| FM-P01-OFF   | Commercial Proposal Template      | Form          |
| FM-P01-BC    | Purchase Order                    | Form          |
| EN-P01-REC   | Complaint Register                | Record        |

---

## 10. Continual Improvement

Improvement of the commercial process is based on:
- Analysis of customer satisfaction surveys
- Monitoring of conversion rates and lead times
- Analysis of complaints and their root causes
- Feedback from operational teams
- Benchmarking of industry commercial practices

---

*Controlled document - Plus Sàrl - ISO 9001:2015 Quality Management System*
*Version v0.7 - 2026-03-04*
