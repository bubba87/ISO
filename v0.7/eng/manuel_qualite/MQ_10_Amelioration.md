# Quality Manual - Chapter 10: Improvement

| **Document**       | MQ_10_Amelioration                       |
|--------------------|------------------------------------------|
| **Version**        | v0.7                                     |
| **Date**           | 2026-03-04                               |
| **Classification** | Internal                                 |
| **Process**        | PS03 - Continual improvement             |
| **Drafted by**     | Quality Role                             |
| **Approved by**    | Management                               |

---

## 10.1 General

Plus Sarl determines and selects opportunities for improvement and undertakes the necessary actions to meet customer requirements and enhance customer satisfaction. Improvement covers:

- Improving products and services to meet requirements and to address future needs and expectations
- Correcting, preventing or reducing undesired effects
- Improving the performance and effectiveness of the Quality Management System

### Sources of Improvement

| Source                               | Data Type                                | Analysis Responsibility |
|--------------------------------------|------------------------------------------|--------------------------|
| Internal audit results               | Findings, NCs, observations              | Quality Role             |
| Customer complaints                  | Complaint forms                          | Commercial Role          |
| Product nonconformities              | NC reports                               | Quality Role             |
| Supplier evaluations                 | Scores and trends                        | Purchasing Role          |
| Performance indicators               | KPI dashboards                           | Quality Role             |
| Management reviews                   | Minutes, decisions                       | Management               |
| Employee feedback                    | Suggestions, lessons learned             | All roles                |
| Competitive and standards watch      | Watch reports                            | Quality Role             |

---

## 10.2 Nonconformity and Corrective Action

### 10.2.1 Nonconformity Treatment Process in 6 Steps

The treatment of nonconformities follows a structured process in **six steps**:

#### Step 1: Detection and Recording

| Action                               | Description                                                      | Responsible       | Deadline    |
|--------------------------------------|------------------------------------------------------------------|--------------------|-------------|
| NC detection                         | Identification during an inspection, audit, complaint or internal check | Any role    | Immediate   |
| Recording                            | Opening of a nonconformity form with factual description         | Quality Role       | 24 hours    |
| Unique number assignment             | Sequential reference NC-YYYY-NNN (e.g.: NC-2026-001)            | Quality Role       | 24 hours    |
| Initial classification               | Categorization according to the severity grid                    | Quality Role       | 24 hours    |

#### Step 2: Immediate Action (Containment)

| Action                               | Description                                                      | Responsible       | Deadline    |
|--------------------------------------|------------------------------------------------------------------|--------------------|-------------|
| NC product isolation                 | Physical separation or marking of nonconforming products         | Quality Role       | Immediate   |
| Notification of concerned parties    | Informing the customer, supplier and internal roles              | Commercial Role / Purchasing Role | 24 hours |
| Securing                             | Prevention of use or shipment of the NC product                  | Quality Role / Logistics Role | Immediate |

#### Step 3: Root Cause Analysis

| Analysis Method                      | Description                                                      | Application                     |
|--------------------------------------|------------------------------------------------------------------|---------------------------------|
| 5 Whys                              | Iterative questioning to trace back to the root cause            | Simple NCs, linear causes       |
| Ishikawa Diagram                     | Cause analysis by category (5M: Material, Method, Manpower, Environment, Machine) | Complex NCs, multiple causes |
| Cause Tree                           | Graphical representation of causal chains                        | Serious or recurring NCs        |

| Element to Analyze                   | Key Questions                                                    |
|--------------------------------------|------------------------------------------------------------------|
| Material                             | Was the product/material compliant with specifications?          |
| Method                               | Was the procedure followed? Was it adequate?                     |
| Manpower                             | Was the personnel competent and trained?                         |
| Environment                          | Was the production environment adequate?                         |
| Machine                              | Were the equipment suitable and in good condition?               |

#### Step 4: Definition and Implementation of Corrective Actions

| Action                               | Description                                                      | Responsible       | Deadline    |
|--------------------------------------|------------------------------------------------------------------|--------------------|-------------|
| Corrective action definition         | Precise description of the action aimed at eliminating the root cause | Quality Role  | 5 days      |
| Action validation                    | Approval by the competent responsible party                      | Management / Quality Role | 2 days |
| Implementation                       | Implementation of the corrective action                          | Relevant role      | 15 days     |
| Documentation                        | NC form update with actions taken                                | Quality Role       | Ongoing     |

#### Step 5: Effectiveness Verification

| Action                               | Description                                                      | Responsible       | Deadline    |
|--------------------------------------|------------------------------------------------------------------|--------------------|-------------|
| Implementation check                 | Verification that the action was implemented as planned          | Quality Role       | Post-implementation |
| Effectiveness evaluation             | Verification that the root cause has been eliminated             | Quality Role       | 30-90 days  |
| Non-recurrence check                 | Monitoring to confirm absence of recurrence                      | Quality Role       | 3 months    |
| Closure decision                     | NC form closure if effectiveness is confirmed                    | Quality Role       | After verification |

#### Step 6: Capitalization and Lessons Learned

| Action                               | Description                                                      | Responsible       |
|--------------------------------------|------------------------------------------------------------------|--------------------|
| Document update                      | Revision of procedures or instructions if necessary              | Document Mgmt Role |
| Internal communication               | Sharing of lessons learned with relevant roles                   | Quality Role       |
| Risk register update                 | Adjustment of risk analysis if necessary (cf. MQ_06)             | Quality Role       |
| Integration in management review     | Presentation of significant NCs and trends                       | Quality Role       |

---

### 10.2.2 Nonconformity Classification (4 Levels)

| Level | Category       | Description                                                                   | Treatment Deadline | Approval Required |
|-------|----------------|-------------------------------------------------------------------------------|--------------------|---------------------|
| 1     | **Minor**      | Isolated deviation with no significant impact on product conformity or customer satisfaction | 30 days           | Quality Role        |
| 2     | **Significant**| Deviation partially affecting conformity or requiring a structured corrective action | 15 days           | Quality Role        |
| 3     | **Major**      | Systematic deviation or significantly impacting product conformity, customer satisfaction or QMS effectiveness | 5 days            | Management          |
| 4     | **Critical**   | Deviation compromising product safety, regulatory compliance or potentially causing serious consequences for the customer | Immediate         | Management          |

### 10.2.3 Escalation Matrix

| NC Level        | Notification                          | Treatment Decision | Follow-up            |
|-----------------|---------------------------------------|------------------------|----------------------|
| Minor           | Quality Role                          | Quality Role           | Quality Role         |
| Significant     | Quality Role, Relevant role           | Quality Role           | Quality Role         |
| Major           | Management, Quality Role, Customer    | Management             | Quality Role         |
| Critical        | Management, Customer, Supplier        | Management             | Management / Quality Role |

---

## 10.3 Continual Improvement

### 10.3.1 PDCA Cycle (Plan-Do-Check-Act)

Plus Sarl applies the PDCA cycle (Deming wheel) as the fundamental method of continual improvement at all levels of the QMS.

```
        +-------------------------------------------+
        |            PLAN                            |
        |  - Identify opportunities                  |
        |  - Define objectives                       |
        |  - Plan actions                            |
        +-------------------+-----------------------+
                            |
                            v
+------------------------------------------------+
|                DO                                |
|  - Implement planned actions                     |
|  - Collect data                                  |
|  - Document results                              |
+-------------------+------------------------------+
                    |
                    v
        +-------------------------------------------+
        |           CHECK                            |
        |  - Measure results                         |
        |  - Compare to objectives                   |
        |  - Analyze deviations                      |
        +-------------------+-----------------------+
                            |
                            v
+------------------------------------------------+
|                ACT                               |
|  - Standardize if objective achieved             |
|  - Correct if deviation                          |
|  - Launch a new cycle                            |
+------------------------------------------------+
```

### 10.3.2 PDCA Application by Process

| Process | PLAN                                    | DO                                     | CHECK                                  | ACT                                    |
|---------|-----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|
| P01     | Sales objectives, action plan           | Prospecting, quotations, customer follow-up | Sales KPIs, customer satisfaction  | Sales strategy adjustment              |
| P02     | Selection criteria, target panel        | Qualification, orders, evaluations     | Supplier scores, NC rate               | Panel revision, corrective actions     |
| P03     | Inspection plan, checklists             | Inspections, reports, decisions        | Acceptance rate, inspection effectiveness | Method adjustment, training          |
| P04     | Logistics schedule, lead time objectives| Shipments, tracking, documentation     | On-time delivery rate, complaints      | Flow optimization, new partners        |
| PS01    | Document plan, objectives               | Creation, updating, distribution       | Up-to-date document rate, document audits | Procedure revision, training        |
| PM01    | Policy, quality objectives              | Oversight, resource allocation         | Management review, overall KPIs        | Strategy revision, new objectives      |

### 10.3.3 Continual Improvement Tools

| Tool                                 | Application                                                      | Frequency of Use    |
|--------------------------------------|------------------------------------------------------------------|-------------------------|
| Trend analysis                       | Monitoring KPI evolution over time                               | Monthly                 |
| Benchmarking                         | Comparison with industry best practices                          | Annual                  |
| Brainstorming                        | Team generation of improvement ideas                             | As needed               |
| Pareto analysis                      | Identification of main NC causes (80/20 rule)                    | Quarterly               |
| Lessons learned (REX)               | Capitalization of lessons learned after each significant project  | At each project closure  |

### 10.3.4 Annual Improvement Program

| Element                              | Description                                                      | Responsible       |
|--------------------------------------|------------------------------------------------------------------|--------------------|
| Performance review                   | Analysis of the past year's results                              | Management / Quality Role |
| Identification of improvement areas  | Priority selection based on data                                 | Management         |
| Improvement action plan              | Actions defined with responsible parties, resources and deadlines| Quality Role       |
| Quarterly follow-up                  | Progress review of improvement actions                           | Quality Role       |
| Annual assessment                    | Evaluation of the improvement program effectiveness              | Management         |

### 10.3.5 Continual Improvement Indicators

| Indicator                           | Formula / Method                         | Target        | Frequency     |
|--------------------------------------|------------------------------------------|---------------|---------------|
| Number of improvement actions launched | Count                                  | >= 6/year     | Annual        |
| Improvement action completion rate   | Actions completed / planned (%)          | >= 80%        | Semi-annual   |
| Corrective action effectiveness rate | Effective CAs / Closed CAs (%)          | >= 90%        | Annual        |
| Overall NC rate trend                | Trend over rolling 12 months             | Continuous decrease | Quarterly |
| Number of NC recurrences             | Identical NCs over 12 months             | 0 recurrence  | Annual        |

---

## Normative References

| ISO 9001:2015 Clause | Requirement                                                  |
|-----------------------|--------------------------------------------------------------|
| 10.1                  | General                                                       |
| 10.2                  | Nonconformity and corrective action                           |
| 10.2.1                | Reaction to nonconformity                                     |
| 10.2.2                | Retention of documented information                           |
| 10.3                  | Continual improvement                                         |

---

*Controlled document - Any printed copy is considered uncontrolled.*
*Plus Sarl - Quality Management System ISO 9001:2015 - v0.7*