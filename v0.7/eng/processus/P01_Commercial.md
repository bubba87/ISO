# P01 - Sales Process

| **Process**         | P01 - Sales                                           |
|----------------------|------------------------------------------------------|
| **Type**            | Operational                                           |
| **Owner**           | Sales Role                                            |
| **Version**         | v0.7                                                  |
| **Date**            | 2026-03-04                                            |
| **Reference**       | PR-P01-COM                                            |
| **ISO 9001 Standard** | Clauses 8.2, 8.5, 9.1.2                            |

---

## 1. Purpose and scope

This process describes the sales activities of **Plus Sarl** from the receipt of a customer request to the measurement of satisfaction. It covers the entire sales cycle for industrial monitoring and worldwide sourcing activities.

---

## 2. Normative references

- ISO 9001:2015, Clauses 8.2 (Requirements for products and services), 8.5 (Production and service provision), 9.1.2 (Customer satisfaction)
- Plus Sarl Quality Manual (MQ-001)

---

## 3. Roles and responsibilities

| Role                        | Key responsibilities                                                 |
|-----------------------------|----------------------------------------------------------------------|
| **Sales**                   | Management of enquiries, quotations, contracts, customer follow-up   |
| **Management**              | Approval of strategic quotations, approval of major contracts        |
| **Quality**                 | Support for quality requirements, handling of complaints             |
| **Customer**                | Expression of needs, validation of quotations, satisfaction feedback |

---

## 4. Input and output data

### Input data
- Customer request (specifications, requirements, RFQ)
- Applicable regulatory and normative requirements
- Customer history and commercial terms
- Plus Sarl service catalogue

### Output data
- Approved sales quotation
- Signed contract / purchase order
- Internal work order
- Customer satisfaction report
- Sales performance indicators

---

## 5. Description of activities

### A1 - Receipt and registration of customer request

The Sales Role receives the customer request (e-mail, telephone, online platform), registers it in the tracking system and assigns a unique reference number.

### A2 - Analysis and review of customer requirements

The Sales Role analyses the request to verify technical, logistical and commercial feasibility. Requirements are reviewed with processes P02 (Purchasing), P03 (Logistics) and P04 (Quality Control) as needed.

### A3 - Preparation of the sales quotation

The Sales Role prepares the quotation including: service description, pricing conditions, lead times, delivery terms (Incoterms), payment terms and quality requirements.

### A4 - Approval and submission of the quotation

The quotation is approved according to defined approval thresholds (Management for strategic quotations) and then submitted to the customer.

### A5 - Negotiation and adjustment

The Sales Role conducts negotiations with the customer, adjusts the quotation if necessary and documents the changes made.

### A6 - Contracting

Once agreed, the Sales Role formalises the contract or purchase order, ensures both parties have signed and triggers the internal work order.

### A7 - Transmission to operational processes

The Sales Role transmits the necessary information to processes P02 (Purchasing/Sourcing), P03 (Logistics) and P04 (Quality Control) for order execution.

### A8 - Monitoring of execution and customer communication

The Sales Role monitors progress with the operational processes and communicates regularly with the customer on the status of their order.

### A9 - Customer satisfaction measurement

The Sales Role manages customer satisfaction measurement through surveys (FM-P01-SAT), analysis of feedback and handling of complaints.

---

## 6. Swimlane diagram

```
 PROCESS P01 - SALES
 ============================================================================

 Role                 | Activity flow
 ============================================================================
                      |
 CUSTOMER             |  Express the     Validate      Negotiate /    Confirm
                      |  need      ----> the received  adjust   ----> the order
                      |  (RFQ, specs)    quotation     terms          (signature)
                      |      |               ^             ^               |
                      |      v               |             |               v
 ============================================================================
                      |
 SALES                |  [A1 Receive]       [A3 Prepare]   [A5 Negotiate]
                      |  and register        the sales      and adjust
                      |  the request         quotation      the quotation
                      |      |                   ^               |
                      |      v                   |               v
                      |  [A2 Analyse]        [A4 Approve]   [A6 Contract]
                      |  customer             and submit     (contract/PO)
                      |  requirements         the quotation
                      |      |                                   |
                      |      |    +------------------------------+
                      |      |    |
                      |      v    v
                      |  [A7 Transmit to operational processes]
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
 MANAGEMENT           |  Approve strategic quotations
                      |  Approve major contracts
                      |
 ============================================================================
                      |
 QUALITY              |  Support for quality requirements
                      |  Handling of complaints
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

## 7. Interactions with other processes

| Process                | Nature of interaction                                  |
|------------------------|--------------------------------------------------------|
| PM01 - Leadership        | Sales reporting, strategic approval                   |
| P02 - Purchasing       | Transmission of sourcing needs, feasibility feedback   |
| P04 - Logistics        | Delivery coordination, shipment tracking               |
| P03 - Quality Control  | Definition of required inspections, quality feedback   |
| PS01 - Document Management | Archiving of quotations, contracts, records          |

---

## 8. Key Performance Indicators (KPI)

| Indicator                                 | Formula / Method                                | Target         | Frequency    |
|-------------------------------------------|------------------------------------------------|----------------|--------------|
| Quotation conversion rate                 | Accepted quotations / Issued quotations x 100  | >= 30 %        | Monthly      |
| Average response time to enquiries        | Sum of response times / Number of enquiries    | < 48 hours     | Monthly      |
| Customer satisfaction rate                | Average score from FM-P01-SAT survey           | >= 4/5         | Quarterly    |
| Number of customer complaints             | Count of complaints received                   | Downward trend | Monthly      |
| Revenue per period                        | Total invoiced orders                          | Per budget     | Monthly      |
| Customer retention rate                   | Recurring customers / Total customers x 100    | >= 60 %        | Annual       |
| Average contracting lead time             | Contract date - Initial request date           | < 15 days      | Monthly      |

---

## 9. Associated documents and records

| Code         | Title                             | Type          |
|--------------|-----------------------------------|---------------|
| PR-P01-COM   | Sales Procedure                   | Procedure     |
| FM-P01-SAT   | Customer Satisfaction Survey      | Form          |
| FM-P01-OFF   | Sales Quotation Template          | Form          |
| FM-P01-BC    | Purchase Order                    | Form          |
| EN-P01-REC   | Complaints Register               | Record        |

---

## 10. Continual improvement

Improvement of the sales process is based on:
- Analysis of customer satisfaction surveys
- Monitoring of conversion rates and lead times
- Analysis of complaints and their root causes
- Feedback from operational teams
- Benchmarking of industry sales practices

---

*Controlled document - Plus Sarl - ISO 9001:2015 Quality Management System*
*Version v0.7 - 2026-03-04*
