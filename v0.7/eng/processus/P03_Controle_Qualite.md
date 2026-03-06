# P03 - Quality Control Process

| **Process**         | P03 - Quality Control                                |
|----------------------|------------------------------------------------------|
| **Type**            | Operational                                           |
| **Owner**           | Quality Role                                          |
| **Version**         | v0.7                                                  |
| **Date**            | 2026-03-04                                            |
| **Reference**       | PR-P03-CQ                                             |
| **ISO 9001 Standard** | Clauses 8.6, 9.1, 10.2                             |

---

## 1. Purpose and scope

This process describes the quality control activities of **Plus Sarl** for its international industrial monitoring and sourcing operations. It covers the four types of inspection (IPC, DUPRO, PSI, Loading Check), nonconformity management, supplier audits and quality data analysis.

---

## 2. Normative references

- ISO 9001:2015, Clauses 8.6 (Release of products and services), 9.1 (Monitoring, measurement, analysis and evaluation), 10.2 (Nonconformity and corrective action)
- Plus Sarl Quality Manual (MQ-001)
- Applicable product standards and regulations

---

## 3. Roles and responsibilities

| Role                        | Key responsibilities                                                 |
|-----------------------------|----------------------------------------------------------------------|
| **Quality**                 | Inspection planning, execution of controls, NC management, reporting |
| **Purchasing**              | Communication of supplier requirements, follow-up of corrective actions |
| **Sales**                   | Transmission of customer requirements, validation of criteria        |
| **Management**              | Arbitration on critical NCs, approval of major actions               |
| **Supplier**                | Making available for inspection, handling of NCs                     |

---

## 4. Types of inspection

| Type            | Full name                            | Timing                           | Objective                                   |
|-----------------|--------------------------------------|----------------------------------|---------------------------------------------|
| **IPC**         | Initial Production Check             | Start of production              | Verify raw materials, components and production parameters |
| **DUPRO**       | During Production Check              | During production (30-50 %)      | Monitor in-process quality, detect deviations |
| **PSI**         | Pre-Shipment Inspection              | Production completed (100 %)     | Final verification before shipment          |
| **Loading Check** | Loading Check                      | At the time of loading           | Verify packaging, labelling and loading     |

---

## 5. Input and output data

### Input data
- Specifications and customer requirements (P01)
- Purchase order and quality requirements (P02)
- Supplier production schedule
- Applicable standards and regulations
- Defined acceptance criteria (AQL, tolerances)

### Output data
- Inspection reports (IPC, DUPRO, PSI, Loading Check)
- Nonconformity reports (FM-P03-NC)
- Release / rejection / sorting decision
- Supplier audit reports (FM-P03-AUD)
- Quality statistics and trends

---

## 6. Description of activities

### A1 - Inspection planning

The Quality Role defines the inspection plan based on the order, the supplier (history, classification) and customer requirements. It determines the type, timing and inspection criteria.

### A2 - Inspection preparation

The Quality Role prepares the inspection documents: checklist based on specifications, sampling plan (AQL), required measuring instruments, acceptance/rejection criteria.

### A3 - Inspection execution (IPC)

The Quality Role carries out the Initial Production Check at the start of production to verify raw materials, components, production parameters and the supplier's understanding of specifications.

### A4 - Inspection execution (DUPRO)

The Quality Role carries out the During Production Check at 30-50 % progress to monitor the quality of products in process, detect deviations and take early corrective measures.

### A5 - Inspection execution (PSI)

The Quality Role carries out the Pre-Shipment Inspection at 100 % production completion. Final inspection according to the AQL sampling plan. Release, rejection or sorting decision.

### A6 - Inspection execution (Loading Check)

The Quality Role carries out the Loading Check at the time of loading to verify packaging, marking, labelling, quantity and loading conditions.

### A7 - Nonconformity management

The Quality Role identifies, records and classifies nonconformities according to 4 levels (see FM-P03-NC). It conducts root cause analysis, defines corrective actions and ensures follow-up.

### A8 - Supplier audits

The Quality Role plans and carries out supplier audits (on-site or remote) according to the annual programme. Results feed into the supplier evaluation (FM-P02-EVAL).

### A9 - Data analysis and quality reporting

The Quality Role compiles and analyses quality data (conformity rates, NC trends, supplier performance), produces dashboards and presents results at the management review.

---

## 7. Swimlane diagram

```
 PROCESS P03 - QUALITY CONTROL
 ============================================================================

 Role                 | Activity flow
 ============================================================================
                      |
 QUALITY              |  [A1 Plan]         [A2 Prepare]
                      |  inspections   --> documents and
                      |  (type, timing,    checklists
                      |   criteria)             |
                      |                         v
                      |      +------------------+------------------+
                      |      |                  |                  |
                      |      v                  v                  v
                      |  [A3 IPC]          [A4 DUPRO]        [A5 PSI]
                      |  Initial           During             Pre-Shipment
                      |  Production        Production         Inspection
                      |  Check             Check              (AQL)
                      |      |                  |                  |
                      |      v                  v                  v
                      |  IPC Report        DUPRO Report     PSI Report
                      |  OK / NC           OK / NC           PASS/FAIL/PENDING
                      |      |                  |                  |
                      |      +------------------+------------------+
                      |                         |
                      |                         v
                      |                    [A6 Loading Check]
                      |                    Packaging, marking,
                      |                    loading
                      |                         |
                      |          +--------------+---------------+
                      |          |              |               |
                      |          v              v               v
                      |     COMPLIANT     NONCOMPLIANT     [A8 Audits]
                      |     Release       [A7 NC Mgmt]     suppliers
                      |     (P03)         (FM-P03-NC)      (FM-P03-AUD)
                      |                        |               |
                      |                        v               v
                      |                   Root cause       Results -->
                      |                   analysis -->     FM-P02-EVAL
                      |                   Corrective action
                      |                        |
                      |                        v
                      |              [A9 Analyse and report]
                      |              Quality dashboards
                      |              Management review (PM01)
                      |
 ============================================================================
                      |
 PURCHASING           |  Transmit       --> Follow up on --> Update
                      |  supplier           supplier         the supplier
                      |  requirements       corrective       panel
                      |                     actions
                      |
 ============================================================================
                      |
 SALES                |  Transmit customer requirements
                      |  Validate acceptance criteria
                      |  Communicate results to customer
                      |
 ============================================================================
                      |
 MANAGEMENT           |  Arbitrate critical NCs (Level 4)
                      |  Approve major actions
                      |
 ============================================================================
                      |
 SUPPLIER             |  Make available  --> Handle     --> Demonstrate
                      |  for inspection      NCs           effectiveness
                      |                                    of corrections
                      |
 ============================================================================
```

---

## 8. Nonconformity management flow

```
  NC Detection
       |
       v
  Registration (FM-P03-NC)
       |
       v
  Classification (4 levels)
  +--------------------------------------------------+
  | Level 1: Minor         - Minor cosmetic defect       |
  | Level 2: Significant   - Specification non-compliance |
  | Level 3: Major         - Impact on conformity/QMS     |
  | Level 4: Critical      - Immediate shipment stop      |
  +--------------------------------------------------+
       |
       v
  Immediate decision
  (Accept / Sort / Reject / Immediate stop)
       |
       v
  Root cause analysis
  (5 Whys, Ishikawa)
       |
       v
  Corrective action
       |
       v
  Effectiveness verification
       |
       v
  NC Closure
```

---

## 9. Interactions with other processes

| Process                | Nature of interaction                                  |
|------------------------|--------------------------------------------------------|
| PM01 - Leadership        | Quality reporting, management review, NC arbitration  |
| P01 - Sales            | Customer requirements, acceptance criteria, quality feedback |
| P02 - Purchasing       | Supplier requirements, evaluation, corrective actions  |
| P04 - Logistics        | Loading Check, release for shipment                    |
| PS01 - Document Management | Archiving of reports, NCs, audits                    |

---

## 10. Key Performance Indicators (KPI)

| Indicator                                 | Formula / Method                                | Target         | Frequency    |
|-------------------------------------------|------------------------------------------------|----------------|--------------|
| PSI conformity rate (PASS)                | PSI PASS / Total PSI x 100                    | >= 90 %        | Monthly      |
| Nonconformity detection rate              | NCs detected / Total inspections x 100         | Downward trend | Monthly      |
| Average NC closure time                   | Sum of NC closure times / Number of NCs        | < 15 days      | Monthly      |
| Corrective action effectiveness rate      | Effective CAs / Verified CAs x 100            | >= 85 %        | Quarterly    |
| Inspection plan completion rate           | Inspections completed / Inspections planned    | >= 95 %        | Monthly      |
| Supplier audit completion rate            | Audits completed / Audits planned x 100        | 100 %          | Annual       |
| Cost of non-quality                       | Total NC costs / Revenue x 100                 | < 2 %          | Quarterly    |

---

## 11. Associated documents and records

| Code         | Title                                 | Type          |
|--------------|---------------------------------------|---------------|
| PR-P03-CQ    | Quality Control Procedure             | Procedure     |
| FM-P03-NC    | Nonconformity Report                  | Form          |
| FM-P03-AUD   | Internal Audit Report                 | Form          |
| FM-P03-IPC   | IPC Report                            | Form          |
| FM-P03-DUPRO | DUPRO Report                          | Form          |
| FM-P03-PSI   | PSI Report                            | Form          |
| FM-P03-LC    | Loading Check Report                  | Form          |
| IT-P03-ECH   | AQL Sampling Instruction              | Instruction   |

---

## 12. Continual improvement

Improvement of the quality control process is based on:
- Statistical analysis of nonconformities and trends
- Evaluation of the effectiveness of corrective actions
- Optimisation of inspection plans based on supplier performance
- Ongoing training of inspectors
- Benchmarking of industry best practices

---

*Controlled document - Plus Sarl - ISO 9001:2015 Quality Management System*
*Version v0.7 - 2026-03-04*
