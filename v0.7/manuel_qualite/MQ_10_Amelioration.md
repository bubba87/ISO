# Quality Manual - Chapter 10: Improvement

| **Document**       | MQ_10_Amelioration                       |
|--------------------|------------------------------------------|
| **Version**        | v0.7                                     |
| **Date**           | 2026-03-04                               |
| **Classification** | Internal                                 |
| **Process**        | PS03 - Continuous improvement            |
| **Drafted by**     | Quality Role                             |
| **Approved by**    | Management                               |

---

## 10.1 General

Plus Sàrl determines and selects opportunities for improvement and undertakes the necessary actions to meet customer requirements and enhance their satisfaction. Improvement encompasses:

- Improving products and services to meet requirements and address future needs and expectations
- Correcting, preventing, or reducing undesirable effects
- Improving the performance and effectiveness of the Quality Management System

### Sources of improvement

| Source                               | Data type                                | Analysis responsible     |
|--------------------------------------|------------------------------------------|--------------------------|
| Internal audit results               | Findings, NCs, observations              | Quality Role             |
| Customer complaints                  | Complaint sheets                         | Commercial Role          |
| Product non-conformities             | NC reports                               | Quality Role             |
| Supplier evaluations                 | Scores and trends                        | Purchasing Role          |
| Performance indicators               | KPI dashboards                           | Quality Role             |
| Management reviews                   | Minutes, decisions                       | Management               |
| Staff feedback                       | Suggestions, lessons learned             | All roles                |
| Competitive and regulatory watch     | Watch reports                            | Quality Role             |

---

## 10.2 Nonconformity and corrective action

### 10.2.1 Six-step nonconformity treatment process

Nonconformity treatment follows a structured **six-step** process:

#### Step 1: Detection and recording

| Action                               | Description                                                      | Responsible        | Timeline    |
|--------------------------------------|------------------------------------------------------------------|--------------------|-------------|
| NC detection                         | Identification during an inspection, audit, complaint, or internal control | Any role   | Immediate   |
| Recording                            | Opening of a nonconformity sheet with factual description        | Quality Role       | 24 hours    |
| Unique number assignment             | Sequential reference NC-2026-001            | Quality Role       | 24 hours    |
| Initial classification               | Categorization according to the severity grid                    | Quality Role       | 24 hours    |

#### Step 2: Immediate action (containment)

| Action                               | Description                                                      | Responsible        | Timeline    |
|--------------------------------------|------------------------------------------------------------------|--------------------|-------------|
| Isolation of NC product              | Physical separation or marking of nonconforming products         | Quality Role       | Immediate   |
| Notification of concerned parties    | Information to the customer, supplier, and internal roles        | Commercial Role / Purchasing Role | 24 hours |
| Safeguarding                         | Prevention of use or shipment of the NC product                  | Quality Role / Logistics Role | Immediate |

#### Step 3: Root cause analysis

| Analysis method                      | Description                                                      | Application                     |
|--------------------------------------|------------------------------------------------------------------|---------------------------------|
| 5 Whys                              | Iterative questioning to trace back to the root cause            | Simple NCs, linear causes       |
| Ishikawa diagram                     | Cause analysis by category (5M: Material, Method, Manpower, Environment, Machine) | Complex NCs, multiple causes |
| Fault tree                           | Graphical representation of causal chains                        | Severe or recurring NCs         |

| Element to analyze                   | Key questions                                                    |
|--------------------------------------|------------------------------------------------------------------|
| Material                             | Was the product/material compliant with specifications?          |
| Method                               | Was the procedure followed? Was it adequate?                     |
| Manpower                             | Was the personnel competent and trained?                         |
| Environment                          | Was the production environment adequate?                         |
| Machine                              | Were the equipment suitable and in good condition?               |

#### Step 4: Definition and implementation of corrective actions

| Action                               | Description                                                      | Responsible        | Timeline    |
|--------------------------------------|------------------------------------------------------------------|--------------------|-------------|
| Corrective action definition         | Precise description of the action aimed at eliminating the root cause | Quality Role  | 5 days      |
| Action validation                    | Approval by the competent responsible party                      | Management / Quality Role | 2 days |
| Implementation                       | Execution of the corrective action                               | Relevant role      | 15 days     |
| Documentation                        | Update of the NC sheet with the actions taken                    | Quality Role       | Ongoing     |

#### Step 5: Effectiveness verification

| Action                               | Description                                                      | Responsible        | Timeline    |
|--------------------------------------|------------------------------------------------------------------|--------------------|-------------|
| Implementation check                 | Verification that the action was implemented as planned          | Quality Role       | Post-implementation |
| Effectiveness assessment             | Verification that the root cause has been eliminated             | Quality Role       | 30-90 days  |
| Non-recurrence check                 | Monitoring to confirm the absence of recurrence                  | Quality Role       | 3 months    |
| Closure decision                     | Closure of the NC sheet if effectiveness is confirmed            | Quality Role       | After verification |

#### Step 6: Capitalization and lessons learned

| Action                               | Description                                                      | Responsible        |
|--------------------------------------|------------------------------------------------------------------|--------------------|
| Document update                      | Revision of procedures or instructions if necessary              | Document Management Role |
| Internal communication               | Sharing of lessons learned with relevant roles                   | Quality Role       |
| Risk register update                 | Adjustment of the risk analysis if necessary (see MQ_06)        | Quality Role       |
| Integration into management review   | Presentation of significant NCs and trends                       | Quality Role       |

---

### 10.2.2 Nonconformity classification (4 levels)

| Level  | Category       | Description                                                                   | Treatment timeline  | Approval required   |
|--------|----------------|-------------------------------------------------------------------------------|---------------------|---------------------|
| 1      | **Minor**      | Isolated deviation with no significant impact on product conformity or customer satisfaction | 30 days            | Quality Role        |
| 2      | **Significant** | Deviation partially affecting conformity or requiring a structured corrective action | 15 days            | Quality Role        |
| 3      | **Major**      | Systematic deviation or one significantly impacting product conformity, customer satisfaction, or QMS effectiveness | 5 days             | Management          |
| 4      | **Critical**   | Deviation compromising product safety, regulatory compliance, or potentially causing severe consequences for the customer | Immediate          | Management          |

### 10.2.3 Escalation matrix

| NC level        | Notification                          | Treatment decision   | Follow-up            |
|-----------------|---------------------------------------|----------------------|----------------------|
| Minor           | Quality Role                          | Quality Role         | Quality Role         |
| Significant     | Quality Role, Relevant role           | Quality Role         | Quality Role         |
| Major           | Management, Quality Role, Customer    | Management           | Quality Role         |
| Critical        | Management, Customer, Supplier        | Management           | Management / Quality Role |

---

## 10.3 Continuous improvement

### 10.3.1 PDCA cycle (Plan-Do-Check-Act)

Plus Sàrl applies the PDCA cycle (Deming wheel) as the fundamental continuous improvement method at all levels of the QMS.

```
        +---------------------------------------------+
        |            PLAN (Plan)                       |
        |  - Identify opportunities                    |
        |  - Define objectives                         |
        |  - Plan actions                              |
        +----------------------+-----------------------+
                               |
                               v
+--------------------------------------------------+
|                DO (Do)                            |
|  - Implement planned actions                     |
|  - Collect data                                  |
|  - Document results                              |
+----------------------+---------------------------+
                       |
                       v
        +---------------------------------------------+
        |           CHECK (Check)                      |
        |  - Measure results                           |
        |  - Compare to objectives                     |
        |  - Analyze deviations                        |
        +----------------------+-----------------------+
                               |
                               v
+--------------------------------------------------+
|                ACT (Act)                          |
|  - Standardize if objective achieved             |
|  - Correct if deviation                          |
|  - Launch a new cycle                            |
+--------------------------------------------------+
```

### 10.3.2 PDCA application by process

| Process | PLAN                                    | DO                                     | CHECK                                  | ACT                                    |
|-----------|-----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|
| P01       | Commercial objectives, action plan      | Prospecting, offers, customer follow-up | Commercial KPIs, customer satisfaction | Commercial strategy adjustment         |
| P02       | Selection criteria, target panel        | Qualification, orders, evaluations     | Supplier scores, NC rate               | Panel revision, corrective actions     |
| P03       | Inspection plan, checklists             | Inspections, reports, decisions        | Acceptance rate, inspection effectiveness | Method adjustment, training          |
| P04       | Logistics planning, delivery targets   | Shipments, tracking, documentation     | On-time delivery rate, complaints      | Flow optimization, new partners        |
| PS01      | Document plan, objectives               | Creation, update, distribution         | Up-to-date document rate, doc audits   | Procedure revision, training           |
| PM01      | Policy, quality objectives              | Management, resource allocation        | Management review, overall KPIs        | Strategy revision, new objectives      |

### 10.3.3 Continuous improvement tools

| Tool                                 | Application                                                      | Usage frequency         |
|--------------------------------------|------------------------------------------------------------------|-------------------------|
| Trend analysis                       | Tracking of KPI evolution over time                              | Monthly                 |
| Benchmarking                         | Comparison with industry best practices                          | Annual                  |
| Brainstorming                        | Team-based generation of improvement ideas                       | As needed               |
| Pareto analysis                      | Identification of main NC causes (80/20 rule)                    | Quarterly               |
| Lessons learned (REX)               | Capitalization of lessons learned after each significant project  | At each project closure |

### 10.3.4 Annual improvement program

| Element                              | Description                                                      | Responsible        |
|--------------------------------------|------------------------------------------------------------------|--------------------|
| Performance review                   | Analysis of the previous year's results                          | Management / Quality Role |
| Identification of improvement areas  | Priority selection based on data                                 | Management         |
| Improvement action plan              | Actions defined with owners, resources, and deadlines            | Quality Role       |
| Quarterly follow-up                  | Review of improvement action progress                            | Quality Role       |
| Annual review                        | Assessment of improvement program effectiveness                  | Management         |

### 10.3.5 Continuous improvement indicators

| Indicator                            | Formula / Method                         | Target        | Frequency     |
|--------------------------------------|------------------------------------------|---------------|---------------|
| Number of improvement actions launched | Count                                  | >= 6/year     | Annual        |
| Improvement action completion rate   | Actions completed / planned (%)          | >= 80%        | Semi-annual   |
| Corrective action effectiveness rate | Effective CAs / Closed CAs (%)          | >= 90%        | Annual        |
| Overall NC rate evolution            | Trend over rolling 12 months             | Continuous decrease | Quarterly |
| Number of NC recurrences             | Identical NCs over 12 months             | 0 recurrence  | Annual        |

---

## Normative references

| ISO 9001:2015 Clause | Requirement                                                  |
|-----------------------|--------------------------------------------------------------|
| 10.1                  | General                                                       |
| 10.2                  | Nonconformity and corrective action                           |
| 10.2.1                | Reaction to nonconformity                                     |
| 10.2.2                | Retention of documented information                           |
| 10.3                  | Continuous improvement                                        |

---

*Controlled document - Any printed copy is considered uncontrolled.*
*Plus Sàrl - Quality Management System ISO 9001:2015 - v0.7*
