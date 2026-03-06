# PS03 - Continual Improvement Process

| **Process**         | PS03 - Continual Improvement                         |
|----------------------|------------------------------------------------------|
| **Type**            | Support                                               |
| **Owner**           | Quality Role                                          |
| **Version**         | v0.7                                                  |
| **Date**            | 2026-03-04                                            |
| **Reference**       | PR-PS03-AMC                                           |
| **ISO 9001 Standard** | Clause 10 (Improvement)                             |

---

## 1. Purpose and scope

This process defines the activities related to the management of continual improvement within the QMS of **Plus Sarl**. It covers the collection and analysis of improvement data, nonconformity and corrective action management, PDCA cycle management, and the annual improvement programme.

This process interacts with all QMS processes and directly feeds the management review (PM01).

---

## 2. Normative references

- ISO 9001:2015, Clause 10.1 (General), 10.2 (Nonconformity and corrective action), 10.3 (Continual improvement)
- Plus Sarl Quality Manual (MQ_10_Improvement)
- Nonconformity Report (FM-P03-NC)

---

## 3. Roles and responsibilities

| Role                        | Responsibilities                                                     |
|-----------------------------|---------------------------------------------------------------------|
| **Management**              | Approval of the improvement programme, prioritisation, resource allocation |
| **Quality Role**            | Process management, facilitation of improvement reviews, corrective action follow-up |
| **Process owners**          | Identification of opportunities within their scope, implementation of actions |
| **All roles**               | Submission of suggestions, reporting of nonconformities, participation in lessons learned |

---

## 4. Input and output data

### Input data
- Results of internal and external audits (MQ_09)
- Customer complaints and satisfaction surveys (P01)
- Product and supplier nonconformities (P03, P02)
- Key performance indicators (KPI) from all processes
- Results of supplier evaluations (P02)
- Management review minutes (PM01)
- Staff suggestions
- Normative and competitive intelligence

### Output data
- Up-to-date nonconformity register
- Closed and evaluated corrective actions
- Annual improvement programme
- Trend reports and analyses
- Input data for management review
- Proposals for QMS updates

---

## 5. Description of activities

### A1 - Collection of improvement data

| Source                              | Data collected                                    | Frequency          | Responsible       |
|-------------------------------------|--------------------------------------------------|--------------------|-------------------|
| Internal audits                     | Findings, NCs, observations, strengths           | Per programme      | Quality Role      |
| Customer complaints                 | Complaint forms, analyses                        | Ongoing            | Sales Role        |
| Product nonconformities             | NC reports, inspection reports                   | Ongoing            | Quality Role      |
| Supplier evaluations                | Scores, trends, alerts                           | Semi-annual        | Purchasing Role   |
| Performance indicators              | KPI dashboards per process                       | Monthly            | Quality Role      |
| Management reviews                  | Decisions, actions to be taken                   | Semi-annual        | Management        |
| Staff suggestions                   | Improvement ideas, field feedback                | Ongoing            | All roles         |
| Normative and competitive intelligence | Standard developments, market practices        | Quarterly          | Quality Role      |

### A2 - Nonconformity handling

Nonconformity handling follows the 6-step process defined in MQ_10:

1. **Detection and registration** -- Opening of NC report (NC-YYYY-NNN)
2. **Immediate action** -- Isolation, notification, containment
3. **Root cause analysis** -- 5 Whys, Ishikawa, fault tree analysis
4. **Corrective actions** -- Definition, approval, implementation
5. **Effectiveness verification** -- Monitoring, evaluation, non-recurrence
6. **Capitalisation** -- Document update, lessons learned, management review

### Nonconformity classification

| Level | Category          | Handling time       | Approval required   |
|-------|-------------------|---------------------|---------------------|
| 1     | **Minor**         | 30 days             | Quality Role        |
| 2     | **Significant**   | 15 days             | Quality Role        |
| 3     | **Major**         | 5 days              | Management          |
| 4     | **Critical**      | Immediate           | Management          |

### A3 - PDCA cycle management

The Quality Role facilitates the PDCA (Plan-Do-Check-Act) cycle for each process:

| Phase   | Actions                                          | Responsible              | Frequency      |
|---------|--------------------------------------------------|--------------------------|----------------|
| PLAN    | Analyse data, define improvement objectives, plan actions | Quality Role + Owners | Quarterly      |
| DO      | Implement planned actions, collect data          | Process owners           | Ongoing        |
| CHECK   | Measure results, compare to objectives, analyse gaps | Quality Role           | Quarterly      |
| ACT     | Standardise if successful, correct if gap, launch new cycle | Management + Quality Role | Quarterly |

### A4 - Annual improvement programme

| Step                                 | Description                                              | Responsible        | Period     |
|--------------------------------------|----------------------------------------------------------|--------------------|------------|
| Previous year review                 | Analysis of results, trends, action effectiveness        | Quality Role       | Q4         |
| Identification of priority areas     | Priority selection based on data                         | Management         | Q4         |
| Programme definition                 | Actions, owners, resources, deadlines                    | Quality Role       | Q4/Q1      |
| Approval                            | Approval by Management at management review              | Management         | Q1         |
| Quarterly monitoring                 | Progress review, adjustments                             | Quality Role       | Q1-Q4      |
| Annual review                        | Evaluation of programme effectiveness                    | Management         | Q4         |

### A5 - Continual improvement tools

| Tool                     | Application                                              | Frequency              |
|--------------------------|----------------------------------------------------------|------------------------|
| Trend analysis           | Monitoring of KPI evolution over time                    | Monthly                |
| Pareto analysis          | Identification of main causes (80/20 rule)               | Quarterly              |
| Brainstorming            | Team-based generation of improvement ideas               | As needed              |
| Benchmarking             | Comparison with industry best practices                  | Annual                 |
| Lessons learned          | Capitalisation after each significant project            | At each closure        |
| 5 Whys                   | Root cause investigation                                 | For each NC            |
| Ishikawa diagram         | Multi-cause analysis                                     | Complex NCs            |

---

## 6. Swimlane diagram

```
 PROCESS PS03 - CONTINUAL IMPROVEMENT
 ============================================================================

 Role                 | Activity flow
 ============================================================================
                      |
 MANAGEMENT           |  Approve the        Arbitrate            Approve the
                      |  improvement  --->  action          ---> annual review
                      |  programme          priorities            and
                      |                                          adjustments
                      |                         |
                      |                         v
 ============================================================================
                      |
 QUALITY ROLE         |  [A1 Collect]       [A2 Handle]         [A3 Manage]
                      |  improvement   ---> NCs and CAs    ---> the PDCA
                      |  data                                    cycle
                      |      |                   |                   |
                      |      v                   v                   v
                      |  Analyse             Follow up on       Measure
                      |  trends and          actions and        results
                      |  identify            verify             and propose
                      |  opportunities       effectiveness      adjustments
                      |      |                   |                   |
                      |      v                   v                   v
                      |  [A4 Define the annual improvement programme]
                      |      |
                      |      v
                      |  [A5 Facilitate continual improvement tools]
                      |      |
                      |      v
                      |  Prepare input data for management review
                      |
 ============================================================================
                      |
 PROCESS              |  Identify        -->  Implement    --->  Report
 OWNERS               |  opportunities in     actions in         results
                      |  their scope          their process      and lessons
                      |                                          learned
 ============================================================================
                      |
 ALL                  |  Report          --->  Propose       ---> Participate
 ROLES                |  NCs and gaps          improvement        in lessons
                      |                        suggestions        learned
 ============================================================================
```

---

## 7. Interactions with other processes

| Process                | Nature of interaction                                          |
|------------------------|----------------------------------------------------------------|
| PM01 - Leadership      | Management review, improvement programme approval              |
| P01 - Sales            | Customer complaints, customer satisfaction                     |
| P02 - Purchasing       | Supplier evaluations, supplier NCs                             |
| P03 - Quality Control  | Product NCs, inspection results                                |
| P04 - Logistics        | Logistics NCs, delivery performance                            |
| PS01 - Document Mgmt   | Document updates following improvement actions                 |
| PS02 - Competence Mgmt | Training needs identified through NC analysis                  |

---

## 8. Key Performance Indicators (KPI)

| Indicator                                    | Formula / Method                                | Target         | Frequency    |
|----------------------------------------------|------------------------------------------------|----------------|--------------|
| Number of improvement actions launched       | Count                                          | >= 6/year      | Annual       |
| Action completion rate                       | Actions completed / Actions planned x 100      | >= 80 %        | Semi-annual  |
| Corrective action effectiveness rate         | Effective CAs / Closed CAs x 100              | >= 90 %        | Annual       |
| Overall NC rate trend                        | Trend over rolling 12 months                   | Continuous decline | Quarterly |
| Number of NC recurrences                     | Identical NCs over 12 months                   | 0 recurrence   | Annual       |
| Average NC closure time                      | Average handling duration                      | <= 20 days     | Quarterly    |

---

## 9. Associated documents and records

| Code          | Title                             | Type           |
|---------------|-----------------------------------|----------------|
| MQ_10         | Quality Manual -- Improvement     | Manual         |
| FM-P03-NC     | Nonconformity Report              | Form           |
| FM-PS03-PAA   | Annual Improvement Programme      | Form           |
| EN-PS03-REG   | Nonconformity Register            | Record         |
| EN-PS03-REX   | Lessons Learned Reports           | Record         |

---

## Normative references

| ISO 9001:2015 Clause | Requirement                                                  |
|-----------------------|--------------------------------------------------------------|
| 10.1                  | General -- Improvement                                       |
| 10.2                  | Nonconformity and corrective action                          |
| 10.3                  | Continual improvement                                        |

---

*Controlled document - Plus Sarl - ISO 9001:2015 Quality Management System*
*Version v0.7 - 2026-03-04*
