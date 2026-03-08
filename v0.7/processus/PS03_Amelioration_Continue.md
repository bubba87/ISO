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

## 1. Purpose and Scope

This process defines the activities related to the management of continual improvement within the QMS of **Plus Sàrl**. It covers the collection and analysis of improvement data, management of non-conformities and corrective actions, PDCA cycle management, and the annual improvement program.

This process interacts with all QMS processes and directly feeds the management review (PM01).

---

## 2. Normative References

- ISO 9001:2015, Clause 10.1 (General), 10.2 (Nonconformity and Corrective Action), 10.3 (Continual Improvement)
- Plus Sàrl Quality Manual (MQ_10_Amelioration)
- Non-Conformity Report (FM-P03-NC)

---

## 3. Roles and Responsibilities

| Role                        | Responsibilities                                                    |
|-----------------------------|---------------------------------------------------------------------|
| **Executive Management**    | Validation of the improvement program, priority arbitration, resource allocation |
| **Quality Role**            | Process management, facilitation of improvement reviews, corrective action monitoring |
| **Process Owners**          | Identification of opportunities within their scope, implementation of actions |
| **All Roles**               | Submission of suggestions, reporting of non-conformities, participation in lessons learned |

---

## 4. Input and Output Data

### Input Data
- Internal and external audit results (MQ_09)
- Customer complaints and satisfaction surveys (P01)
- Product and supplier non-conformities (P03, P02)
- Key performance indicators (KPI) from all processes
- Supplier evaluation results (P02)
- Management review minutes (PM01)
- Employee suggestions
- Normative and competitive intelligence

### Output Data
- Up-to-date non-conformity register
- Closed and evaluated corrective actions
- Annual improvement program
- Trend reports and analyses
- Input data for management review
- QMS update proposals

---

## 5. Activity Description

### A1 - Collection of Improvement Data

| Source                              | Data Collected                                   | Frequency          | Responsible        |
|-------------------------------------|--------------------------------------------------|--------------------|-------------------|
| Internal audits                     | Findings, NCs, observations, strengths           | Per program        | Quality Role       |
| Customer complaints                 | Complaint forms, analyses                        | Ongoing            | Commercial Role    |
| Product non-conformities            | NC reports, inspection reports                   | Ongoing            | Quality Role       |
| Supplier evaluations                | Scores, trends, alerts                           | Semi-annual        | Purchasing Role    |
| Performance indicators              | KPI dashboards per process                       | Monthly            | Quality Role       |
| Management reviews                  | Decisions, actions to be taken                   | Semi-annual        | Executive Management |
| Employee suggestions                | Improvement ideas, field feedback                | Ongoing            | All Roles          |
| Normative and competitive intelligence | Standards developments, market practices       | Quarterly          | Quality Role       |

### A2 - Non-Conformity Treatment

Non-conformity treatment follows the 6-step process defined in MQ_10:

1. **Detection and registration** -- NC report opening (NC-YYYY-NNN)
2. **Immediate action** -- Isolation, notification, containment
3. **Root cause analysis** -- 5 Whys, Ishikawa, cause tree
4. **Corrective actions** -- Definition, validation, implementation
5. **Effectiveness verification** -- Control, evaluation, non-recurrence
6. **Capitalization** -- Document updates, lessons learned, management review

### Non-Conformity Classification

| Level | Category          | Treatment Deadline | Approval Required    |
|-------|-------------------|--------------------|----------------------|
| 1     | **Minor**         | 30 days            | Quality Role         |
| 2     | **Significant**   | 15 days            | Quality Role         |
| 3     | **Major**         | 5 days             | Executive Management |
| 4     | **Critical**      | Immediate          | Executive Management |

### A3 - PDCA Cycle Management

The Quality Role facilitates the PDCA (Plan-Do-Check-Act) cycle for each process:

| Phase   | Actions                                          | Responsible                    | Frequency      |
|---------|--------------------------------------------------|--------------------------------|----------------|
| PLAN    | Analyze data, define improvement objectives, plan actions | Quality Role + Process Owners | Quarterly      |
| DO      | Implement planned actions, collect data          | Process Owners                 | Ongoing        |
| CHECK   | Measure results, compare to objectives, analyze gaps | Quality Role                | Quarterly      |
| ACT     | Standardize if successful, correct if gap exists, launch new cycle | Executive Management + Quality Role | Quarterly |

### A4 - Annual Improvement Program

| Step                                | Description                                              | Responsible        | Period     |
|--------------------------------------|----------------------------------------------------------|--------------------|------------|
| Previous year review                 | Analysis of results, trends, action effectiveness        | Quality Role       | Q4         |
| Identification of priority areas     | Selection of priorities based on data                    | Executive Management | Q4       |
| Program definition                   | Actions, responsible parties, resources, deadlines       | Quality Role       | Q4/Q1      |
| Validation                           | Approval by Executive Management at management review    | Executive Management | Q1       |
| Quarterly monitoring                 | Progress review, adjustments                             | Quality Role       | Q1-Q4      |
| Annual review                        | Evaluation of program effectiveness                      | Executive Management | Q4       |

### A5 - Continual Improvement Tools

| Tool                     | Application                                              | Frequency              |
|--------------------------|----------------------------------------------------------|------------------------|
| Trend analysis           | Monitoring of KPI evolution over time                    | Monthly                |
| Pareto analysis          | Identification of main causes (80/20 rule)               | Quarterly              |
| Brainstorming            | Team idea generation for improvement                     | As needed              |
| Benchmarking             | Comparison with industry best practices                  | Annual                 |
| Lessons learned          | Capitalization after each significant project            | At each closure        |
| 5 Whys                   | Root cause investigation                                 | At each NC             |
| Ishikawa diagram         | Multi-causal analysis                                    | Complex NCs            |

---

## 6. Swimlane Diagram

```
 PROCESS PS03 - CONTINUAL IMPROVEMENT
 ============================================================================

 Role                 | Activity Flow
 ============================================================================
                      |
 EXECUTIVE            |  Validate the       Arbitrate            Approve the
 MANAGEMENT           |  improvement  --->  action          ---> annual review
                      |  program            priorities            and
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
                      |  Analyze             Monitor              Measure
                      |  trends and          actions and          results
                      |  identify            verify               and propose
                      |  opportunities       effectiveness        adjustments
                      |      |                   |                   |
                      |      v                   v                   v
                      |  [A4 Define the annual improvement program]
                      |      |
                      |      v
                      |  [A5 Facilitate continual improvement tools]
                      |      |
                      |      v
                      |  Prepare input data for management review
                      |
 ============================================================================
                      |
 PROCESS              |  Identify       -->  Implement     --->  Report
 OWNERS               |  opportunities in    actions in          results
                      |  their scope         their process       and lessons
                      |                                          learned
 ============================================================================
                      |
 ALL                  |  Report         --->  Propose       ---> Participate
 ROLES                |  NCs and gaps         improvement        in lessons
                      |                       suggestions        learned
 ============================================================================
```

---

## 7. Interactions with Other Processes

| Process                | Nature of Interaction                                          |
|------------------------|----------------------------------------------------------------|
| PM01 - Leadership      | Management review, improvement program validation              |
| P01 - Commercial       | Customer complaints, customer satisfaction                     |
| P02 - Purchasing       | Supplier evaluations, supplier NCs                             |
| P03 - Quality Control  | Product NCs, inspection results                                |
| P04 - Logistics        | Logistics NCs, delivery performance                            |
| PS01 - Document Mgmt   | Document updates following improvement actions                 |
| PS02 - Competency Mgmt | Training needs identified through NC analysis                  |

---

## 8. Key Performance Indicators (KPI)

| Indicator                                    | Formula / Method                                   | Target         | Frequency    |
|----------------------------------------------|---------------------------------------------------|----------------|--------------|
| Number of improvement actions launched       | Count                                              | >= 6/year      | Annual       |
| Action completion rate                       | Actions completed / Actions planned x 100          | >= 80%         | Semi-annual  |
| Corrective action effectiveness rate         | Effective CAs / Closed CAs x 100                  | >= 90%         | Annual       |
| Overall NC rate trend                        | Trend over rolling 12 months                       | Continuous decrease | Quarterly |
| Number of NC recurrences                     | Identical NCs over 12 months                       | 0 recurrence   | Annual       |
| Average NC closure time                      | Average treatment duration                         | <= 20 days     | Quarterly    |

---

## 9. Associated Documents and Records

| Code          | Title                             | Type           |
|---------------|-----------------------------------|----------------|
| MQ_10         | Quality Manual -- Improvement     | Manual         |
| FM-P03-NC     | Non-Conformity Report             | Form           |
| FM-PS03-PAA   | Annual Improvement Program        | Form           |
| EN-PS03-REG   | Non-Conformity Register           | Record         |
| EN-PS03-REX   | Lessons Learned Reports           | Record         |

---

## Normative References

| ISO 9001:2015 Clause | Requirement                                                  |
|-----------------------|--------------------------------------------------------------|
| 10.1                  | General -- Improvement                                       |
| 10.2                  | Nonconformity and Corrective Action                          |
| 10.3                  | Continual Improvement                                        |

---

*Controlled document - Plus Sàrl - ISO 9001:2015 Quality Management System*
*Version v0.7 - 2026-03-04*
