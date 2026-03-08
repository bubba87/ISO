# P03 - Quality Control Process

| **Process**         | P03 - Quality Control                                |
|----------------------|------------------------------------------------------|
| **Type**            | Core                                                  |
| **Owner**           | Quality Role                                          |
| **Version**         | v0.7                                                  |
| **Date**            | 2026-03-04                                            |
| **Reference**       | PR-P03-CQ                                             |
| **ISO 9001 Standard** | Clauses 8.6, 9.1, 10.2                             |

---

## 1. Purpose and Scope

This process describes the quality control activities of **Plus Sàrl** for its international industrial follow-up and sourcing operations. It covers the four types of inspection (IPC, DUPRO, PSI, Loading Check), non-conformity management, supplier audits, and quality data analysis.

---

## 2. Normative References

- ISO 9001:2015, Clauses 8.6 (Release of Products and Services), 9.1 (Monitoring, Measurement, Analysis and Evaluation), 10.2 (Nonconformity and Corrective Action)
- Plus Sàrl Quality Manual (MQ-001)
- Applicable product standards and regulations

---

## 3. Roles and Responsibilities

| Role                        | Key Responsibilities                                                 |
|-----------------------------|----------------------------------------------------------------------|
| **Quality**                 | Inspection planning, control execution, NC management, reporting     |
| **Purchasing**              | Communication of supplier requirements, corrective action follow-up  |
| **Commercial**              | Transmission of customer requirements, validation of criteria        |
| **Executive Management**    | Arbitration on critical NCs, validation of major actions             |
| **Supplier**                | Availability for inspection, NC resolution                           |

---

## 4. Inspection Types

| Type            | Full Name                            | Timing                           | Objective                                   |
|-----------------|--------------------------------------|----------------------------------|---------------------------------------------|
| **IPC**         | Initial Production Check             | Start of production              | Verify raw materials, components, and production parameters |
| **DUPRO**       | During Production Check              | During production (30-50%)       | Monitor in-process quality, detect deviations |
| **PSI**         | Pre-Shipment Inspection              | Production completed (100%)      | Final verification before shipment          |
| **Loading Check** | Loading Check                      | At time of loading               | Verify packaging, labeling, and loading     |

---

## 5. Input and Output Data

### Input Data
- Customer specifications and requirements (P01)
- Purchase order and quality requirements (P02)
- Supplier production schedule
- Applicable standards and regulations
- Defined acceptance criteria (AQL, tolerances)

### Output Data
- Inspection reports (IPC, DUPRO, PSI, Loading Check)
- Non-conformity reports (FM-P03-NC)
- Release / rejection / sorting decision
- Supplier audit reports (FM-P03-AUD)
- Quality statistics and trends

---

## 6. Activity Description

### A1 - Inspection Planning

The Quality Role defines the inspection plan based on the order, the supplier (history, classification), and customer requirements. It determines the type, timing, and inspection criteria.

### A2 - Inspection Preparation

The Quality Role prepares the inspection documents: checklist based on specifications, sampling plan (AQL), required measurement tools, acceptance/rejection criteria.

### A3 - Inspection Execution (IPC)

The Quality Role performs the Initial Production Check at the start of production to verify raw materials, components, production parameters, and the supplier's understanding of specifications.

### A4 - Inspection Execution (DUPRO)

The Quality Role performs the During Production Check at 30-50% completion to monitor the quality of products in progress, detect deviations, and take early corrective measures.

### A5 - Inspection Execution (PSI)

The Quality Role performs the Pre-Shipment Inspection at 100% production completion. Final inspection according to the AQL sampling plan. Release, rejection, or sorting decision.

### A6 - Inspection Execution (Loading Check)

The Quality Role performs the Loading Check at the time of loading to verify packaging, marking, labeling, quantity, and loading conditions.

### A7 - Non-Conformity Management

The Quality Role identifies, records, and classifies non-conformities according to 4 levels (ref. FM-P03-NC). It conducts root cause analysis, defines corrective actions, and ensures their follow-up.

### A8 - Supplier Audits

The Quality Role plans and conducts supplier audits (on-site or remote) according to the annual program. Results feed into the supplier evaluation (FM-P02-EVAL).

### A9 - Data Analysis and Quality Reporting

The Quality Role compiles and analyzes quality data (conformity rates, NC trends, supplier performance), produces dashboards, and presents results at the management review.

---

## 7. Swimlane Diagram

```
 PROCESS P03 - QUALITY CONTROL
 ============================================================================

 Role                 | Activity Flow
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
                      |     COMPLIANT     NON-COMPLIANT    [A8 Audits]
                      |     Release       [A7 NC Mgmt]     Supplier
                      |     (P03)         (FM-P03-NC)      (FM-P03-AUD)
                      |                        |               |
                      |                        v               v
                      |                   Root cause        Results -->
                      |                   analysis -->      FM-P02-EVAL
                      |                   Corrective action
                      |                        |
                      |                        v
                      |              [A9 Analyze and report]
                      |              Quality dashboards
                      |              Management review (PM01)
                      |
 ============================================================================
                      |
 PURCHASING           |  Transmit       ---> Monitor       ---> Update
                      |  supplier            supplier            supplier
                      |  requirements        corrective          panel
                      |                      actions
                      |
 ============================================================================
                      |
 COMMERCIAL           |  Transmit customer requirements
                      |  Validate acceptance criteria
                      |  Communicate results to customer
                      |
 ============================================================================
                      |
 EXECUTIVE            |  Arbitrate critical NCs (Level 4)
 MANAGEMENT           |  Validate major actions
                      |
 ============================================================================
                      |
 SUPPLIER             |  Make available  ---> Resolve    ---> Demonstrate
                      |  for inspection       NCs             correction
                      |                                       effectiveness
                      |
 ============================================================================
```

---

## 8. Non-Conformity Management Flow

```
  NC Detection
       |
       v
  Registration (FM-P03-NC)
       |
       v
  Classification (4 levels)
  +--------------------------------------------------+
  | Level 1: Minor          - Minor aesthetic defect      |
  | Level 2: Significant    - Specification non-compliance |
  | Level 3: Major          - Impact on conformity/QMS     |
  | Level 4: Critical       - Immediate shipment stop      |
  +--------------------------------------------------+
       |
       v
  Immediate Decision
  (Accept / Sort / Reject / Immediate Stop)
       |
       v
  Root Cause Analysis
  (5 Whys, Ishikawa)
       |
       v
  Corrective Action
       |
       v
  Effectiveness Verification
       |
       v
  NC Closure
```

---

## 9. Interactions with Other Processes

| Process                | Nature of Interaction                                  |
|------------------------|--------------------------------------------------------|
| PM01 - Leadership      | Quality reporting, management review, NC arbitration   |
| P01 - Commercial       | Customer requirements, acceptance criteria, quality feedback |
| P02 - Purchasing       | Supplier requirements, evaluation, corrective actions  |
| P04 - Logistics        | Loading Check, release for shipment                    |
| PS01 - Document Management | Archiving of reports, NCs, audits                   |

---

## 10. Key Performance Indicators (KPI)

| Indicator                                 | Formula / Method                                   | Target         | Frequency    |
|-------------------------------------------|---------------------------------------------------|----------------|--------------|
| PSI conformity rate (PASS)                | PSI PASS / Total PSI x 100                        | >= 90%         | Monthly      |
| Non-conformity detection rate             | NCs detected / Total inspections x 100             | Downward trend | Monthly      |
| Average NC closure time                   | Sum of NC closure times / Number of NCs            | < 15 days      | Monthly      |
| Corrective action effectiveness rate      | Effective CAs / Verified CAs x 100                | >= 85%         | Quarterly    |
| Inspection plan completion rate           | Inspections performed / Inspections planned        | >= 95%         | Monthly      |
| Supplier audit completion rate            | Audits performed / Audits planned x 100            | 100%           | Annual       |
| Cost of non-quality                       | Total NC costs / Revenue x 100                     | < 2%           | Quarterly    |

---

## 11. Associated Documents and Records

| Code         | Title                                 | Type          |
|--------------|---------------------------------------|---------------|
| PR-P03-CQ    | Quality Control Procedure             | Procedure     |
| FM-P03-NC    | Non-Conformity Report                 | Form          |
| FM-P03-AUD   | Internal Audit Report                 | Form          |
| FM-P03-IPC   | IPC Report                            | Form          |
| FM-P03-DUPRO | DUPRO Report                          | Form          |
| FM-P03-PSI   | PSI Report                            | Form          |
| FM-P03-LC    | Loading Check Report                  | Form          |
| IT-P03-ECH   | AQL Sampling Instruction              | Instruction   |

---

## 12. Continual Improvement

Improvement of the quality control process is based on:
- Statistical analysis of non-conformities and trends
- Evaluation of corrective action effectiveness
- Optimization of inspection plans based on supplier performance
- Ongoing training of inspectors
- Benchmarking of industry best practices

---

*Controlled document - Plus Sàrl - ISO 9001:2015 Quality Management System*
*Version v0.7 - 2026-03-04*
