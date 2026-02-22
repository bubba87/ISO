# Corrective Actions Procedure

| | |
|---|---|
| **Reference** | PRO-ACR-001 |
| **Version** | 0.4 |
| **Creation date** | 10/02/2026 |
| **Revision date** | 22/02/2026 |
| **Prepared by** | Roxane Wicky |
| **Approved by** | Roxane Wicky |

> **Legend:** :red_circle: [TO BE COMPLETED] = mandatory, missing | :yellow_circle: [RECOMMENDED] = recommended | :green_circle: = already completed | :blue_circle: [TO BE VERIFIED] = to be confirmed

---

## 1. Purpose

To define the rules for root cause analysis, implementation and effectiveness verification of corrective actions in order to eliminate the causes of nonconformities and prevent their recurrence within the QMS of Plus Sarl.

> **Link to Process 04 (cf. CTX-QUA-001, section 1.1):** In case of identified nonconformity, an NC form is created (PRO-NCF-001), a treatment decision is made (acceptance, replacement or correction), then a root cause analysis and investigation is conducted. This procedure defines the implementation of corrective actions in order to prevent recurrence. 🟢

## 2. Scope

Any nonconformity requiring corrective action:
- Major NCs (systematically)
- Recurring minor NCs
- Internal or external audit NCs (including SQS certification audit)
- Significant or repetitive customer complaints
- Any situation where the managing director deems it necessary to act on the causes

## 3. Definitions

| Term | Definition |
|---|---|
| **Correction** | Action to eliminate a detected NC (immediate treatment of the symptom) |
| **Corrective action** | Action to eliminate the **cause** of an NC and prevent its recurrence |
| **Root cause** | The fundamental cause at the origin of the NC |
| **Effectiveness verification** | Control that the corrective action has indeed prevented the recurrence of the NC |

> **Key difference:**
> - Correction = "I replaced the defective parts at the customer's" (symptom)
> - Corrective action = "I asked the factory to implement enhanced control on this reference" (cause)

## 4. Responsibilities

| Responsibility | Who |
|---|---|
| Decide on opening a CA | :green_circle: Roxane Wicky, managing director |
| Analyze causes (to the extent of the managing director's competencies) | :green_circle: Roxane Wicky, managing director (with Chinese partners if manufacturing NC) |
| Define the corrective action | :green_circle: Roxane Wicky, managing director |
| Implement or coordinate implementation | :green_circle: Roxane Wicky, managing director (or Chinese partner) |
| Verify effectiveness | :green_circle: Roxane Wicky, managing director |

## 5. Procedure

### 5.1 Flowchart

```
    NC requiring corrective action
    (see criteria in section 2)
            |
            v
    +------------------------+
    | 1. Open CA form        |---> AC_[AAAA]_[NNN]
    +------------------------+
            |
            v
    +------------------------+
    | 2. Analyze causes      |---> 5 Whys Method
    |    (to the extent of   |     (adapted for a micro-company)
    |     competencies)      |
    +------------------------+
            |
            v
    +------------------------+
    | 3. Identify root cause |---> Documented root cause
    +------------------------+
            |
            v
    +------------------------+
    | 4. Define corrective   |---> What, who, when
    |    action              |
    +------------------------+
            |
            v
    +------------------------+
    | 5. Implement           |---> Action implementation
    |    (manager and/or     |     (partner coordination)
    |     partners)          |
    +------------------------+
            |
            v
    +------------------------+
    | 6. Verify effectiveness|---> Recurring NC? YES/NO
    +------------------------+
            |
       NC eliminated?
       /          \
     YES          NO
      |             |
      v             v
  +--------+   +-----------------+
  | Close  |   | New root cause  |
  | form   |   | analysis        |
  +--------+   +-----------------+
```

### 5.2 Detailed steps

**Step 1 - Open CA form**

- Assign a number: AC_[AAAA]_[NNN]
- Link to the original NC (NC_[AAAA]_[NNNN])
- Describe the problem

**Step 2 - Analyze causes**

Root cause analysis is performed by the managing director to the extent of her competencies, in coordination with Chinese partners when the NC is related to manufacturing.

Use the 5 Whys method (recommended for Plus Sarl):

| # | Why? | Answer |
|---|---|---|
| 1 | Why did the NC occur? | [Answer 1] |
| 2 | Why [Answer 1]? | [Answer 2] |
| 3 | Why [Answer 2]? | [Answer 3] |
| 4 | Why [Answer 3]? | [Answer 4] |
| 5 | Why [Answer 4]? | [Answer 5 = probable root cause] |

### 5.3 Typical corrective actions for Plus Sarl

The objective of corrective actions is to prevent recurrence of NCs and reduce impact on customers. Here are the most frequent scenarios and associated corrective actions:

#### Scenario 1: Transport delay

| Element | Detail |
|---|---|
| **Problem** | Delivery delay related to carrier or freight forwarder |
| **Typical root cause** | Unreliable carrier/freight forwarder, logistical problems |
| **Corrective actions** | - Reevaluate the carrier/freight forwarder concerned |
| | - Inform Chinese partners to avoid this service provider in the future |
| | - Adapt logistics choice (mode change: air/sea/rail) |
| | - Anticipate delays in communications to customers |

#### Scenario 2: Production delay

| Element | Detail |
|---|---|
| **Problem** | Manufacturing delay at Chinese partner |
| **Typical root cause** | Insufficient planning, factory overload, technical problem |
| **Corrective actions** | - Enhanced follow-up with Chinese partners (more frequent checkpoints) |
| | - Push for better lead times and improved planning |
| | - Anticipate communications to customers in case of delay risk |
| | - Commercial adjustments if necessary (commercial gesture, staggering) |

#### Scenario 3: Production defect

| Element | Detail |
|---|---|
| **Problem** | Parts not conforming to specifications (dimensions, appearance, material) |
| **Typical root cause** | Machine setting problem, mold wear, material error, insufficient control |
| **Corrective actions** | - Ask the factory to keep information about the NC |
| | - Request implementation of enhanced controls on future productions of this reference |
| | - Replacement of nonconforming parts for the customer |
| | - Logistics adaptation if necessary (urgent re-shipment) |
| | - Enhanced partner follow-up (continuous quality monitoring) |
| | - Strengthen pre-shipment QC and sampling (cf. PRO-ACH-001, section 8) |
| | - Commercial adjustments if necessary |

#### Scenario 4: Labeling or packaging error

| Element | Detail |
|---|---|
| **Problem** | Labeling or packaging error (incorrect reference on label, confusion between similar references) |
| **Typical root cause** | Confusion between similar references, absence of control checklist, insufficient verification before shipment |
| **Corrective actions** | - Create a complete quality control checklist covering labeling and packaging |
| | - Strengthen label verification before shipment |
| | - Clarify references with supplier (especially close references that may cause confusion) |
| | - Ask supplier to implement double control on labeling |
| | - Integrate labeling control into pre-shipment QC |

> **Guiding principle:** Plus Sarl's corrective actions aim to prevent recurrence and reduce impact on the customer. The managing director acts to the extent of her competencies and relies on her Chinese partners (Yuyao Mould Factory and Oukailuo) for technical aspects of manufacturing.

**Step 3 - Identify root cause**

- Select the most probable cause
- Verify with data/evidence if possible (photos, reports, email/WeChat exchanges)

**Step 4 - Define corrective action**

The corrective action must:
- Act on the root cause (not on the symptom)
- Be realistic and proportionate to Plus Sarl's means
- Have a responsible person and a deadline
- Be communicated to the concerned Chinese partner if necessary

**Step 5 - Implement**

- Perform the action or coordinate its implementation by the Chinese partner
- Document what has been done
- Communicate actions to concerned parties (Chinese partner, customer, carrier)

**Step 6 - Verify effectiveness**

- Wait for a sufficient period (generally 1 to 3 months or the next orders of the same type)
- Verify that the NC has not recurred during subsequent productions/deliveries
- If the NC recurs: resume root cause analysis, consider stronger measures

## 6. Corrective Action Form (template)

### Identification

| Element | Detail |
|---|---|
| **CA No.** | AC_[AAAA]_[NNN] |
| **Opening date** | [DD/MM/YYYY] |
| **Original NC** | NC_[AAAA]_[NNNN] |
| **Source** | [ ] Customer complaint [ ] Transport delay [ ] Production delay [ ] Production defect [ ] Labeling/Packaging [ ] Pre-shipment QC [ ] Internal audit [ ] External audit (SQS) [ ] Other |

### Problem description

| Element | Detail |
|---|---|
| **Description** | [Factual description of the problem] |
| **Customer impact** | [Consequences of the NC for the customer] |
| **Frequency/Recurrence** | [First occurrence / Recurring (how many times)] |

### Root cause analysis

| Element | Detail |
|---|---|
| **Method used** | [ ] 5 Whys [ ] Other |
| **Analysis detail** | [See 5 Whys table] |
| **Root cause identified** | [Root cause description] |
| **Partner involved in analysis** | [ ] Yuyao Mould Factory [ ] Oukailuo [ ] Carrier [ ] Internal analysis only |

### Action plan

| # | Corrective action | Responsible | Deadline | Status |
|---|---|---|---|---|
| 1 | [Action description] | [Manager / Partner] | [Date] | [ ] Planned [ ] In progress [ ] Completed |
| 2 | [Action description] | [Manager / Partner] | [Date] | [ ] Planned [ ] In progress [ ] Completed |
| 3 | [Action description] | [Manager / Partner] | [Date] | [ ] Planned [ ] In progress [ ] Completed |

### Effectiveness verification

| Element | Detail |
|---|---|
| **Verification date** | [DD/MM/YYYY] (at least 1-3 months after implementation or next orders) |
| **Verification method** | [Monitoring of next deliveries, absence of customer complaint, partner feedback] |
| **Result** | [ ] Effective (non-recurring NC) [ ] Not effective (recurring NC) |
| **Comment** | [Observations] |

### Closure

| Element | Detail |
|---|---|
| **Closure date** | [DD/MM/YYYY] |
| **Closed by** | Roxane Wicky |
| **Final status** | [ ] Closed [ ] In progress [ ] Reopening necessary |

---

### Example of completed form: AC_2026_001

#### Identification

| Element | Detail |
|---|---|
| **CA No.** | :green_circle: AC_2026_001 |
| **Opening date** | :green_circle: 10/02/2026 |
| **Original NC** | :green_circle: NC_2026_1001 |
| **Source** | :green_circle: [X] Labeling/Packaging |

#### Problem description

| Element | Detail |
|---|---|
| **Description** | :green_circle: Delivery of a carton of 1000 pieces with incorrect labeling (90.60.05710L instead of 90.60.05710) - SHIP_25058/CFM00057428 |
| **Customer impact** | :green_circle: Limited impact -- the physical product is conforming, only the label is erroneous. The customer accepted the product as-is (derogation). |
| **Frequency/Recurrence** | :green_circle: First occurrence |

#### Root cause analysis

| Element | Detail |
|---|---|
| **Method used** | :green_circle: [X] 5 Whys |
| **Analysis detail** | :red_circle: [TO BE COMPLETED -- cause not yet identified. Analysis will be deepened during the trip to China in March 2026] |
| **Root cause identified** | :red_circle: [TO BE COMPLETED -- exact cause not yet identified] |
| **Partner involved in analysis** | :green_circle: [X] Yuyao Mould Factory |

#### Action plan

| # | Corrective action | Responsible | Deadline | Status |
|---|---|---|---|---|
| 1 | Inform supplier of NC | :green_circle: Roxane Wicky | :green_circle: 10/02/2026 | :green_circle: [X] Completed |
| 2 | Create a complete quality control checklist | Roxane Wicky + Yuyao Mould Factory | March 2026 (China trip) | [ ] In progress |
| 3 | Strengthen pre-shipment QC for labeling | Yuyao Mould Factory | March 2026 (China trip) | [ ] Planned |

#### Effectiveness verification

| Element | Detail |
|---|---|
| **Verification date** | :red_circle: [TO BE COMPLETED -- after action implementation, next orders of reference 90.60.05710] |
| **Verification method** | Monitoring of next deliveries of this reference, labeling verification |
| **Result** | :red_circle: [TO BE COMPLETED -- pending] |
| **Comment** | Monitoring in progress. Exact cause not yet identified. Photos not available. Treatment will be strengthened during the trip to China planned for March 2026. |

#### Closure

| Element | Detail |
|---|---|
| **Closure date** | :red_circle: [TO BE COMPLETED -- pending] |
| **Closed by** | Roxane Wicky |
| **Final status** | :green_circle: [X] In progress |

---

## 7. Corrective actions register

| CA No. | Opening date | Linked NC | Root cause | Action | Deadline | Effective? | Status |
|---|---|---|---|---|---|---|---|
| :green_circle: AC_2026_001 | 10/02/2026 | NC_2026_1001 | :red_circle: Cause not yet identified | 1. Inform supplier (completed) 2. Create a complete quality control checklist 3. Strengthen pre-shipment QC for labeling | March 2026 (China trip) | In progress | In progress |
| AC_[AAAA]_[NNN] | [date] | NC_xxx | [summary] | [summary] | [date] | [Y/N/In progress] | [Open/Closed] |

---

## 8. Indicators

| Indicator | Target | Frequency |
|---|---|---|
| Number of CAs opened | Information | Quarterly |
| Distribution by type (transport, production, delay, labeling, pre-shipment QC) | Information | Quarterly |
| Closure rate within deadlines | > 80% | Quarterly |
| CA effectiveness rate | > 90% | Annual |

---

> **Completion instructions:**
> 1. Only open a CA if justified (major, recurring, or audit NC)
> 2. Take time to properly analyze the root cause -- this is the key step
> 3. The 5 Whys method is simple and effective for a micro-company like Plus Sarl
> 4. Involve Chinese partners (Yuyao Mould Factory or Oukailuo) in the analysis when the NC comes from manufacturing
> 5. Document exchanges (emails, WeChat) as evidence of corrective actions
> 6. The auditor (SQS) will verify that your CAs are effective (not just on paper)
> 7. Root cause analysis is done to the extent of the managing director's competencies -- it is a continuous improvement approach
> 8. Pre-shipment QC with sampling can be a source of CA if NCs are detected before delivery

---

## Revision history

| Version | Date | Modification description | Author |
|---|---|---|---|
| 0.1 | 10/02/2026 | Initial creation | Roxane Wicky |
| 0.2 | 10/02/2026 | Addition of first real corrective action (AC_2026_001 linked to NC_2026_1001 - labeling error). Addition of Scenario 4 (labeling/packaging error). Numbering format update (underscores). Addition of "Labeling/Packaging" category in indicators. | Roxane Wicky |
| 0.3 | 12/02/2026 | Integration of responses (Oukailuo, Paradiso, SQS, cloud, QC sampling). Addition of field legend system. | Roxane Wicky |
| 0.4 | 18/02/2026 | Integration UPDATE 2.1 Process 04: addition of reference to link with formalized quality control (CTX-QUA-001, section 1.1). | Roxane Wicky |
| 0.4 | 22/02/2026 | Oukailuo replaces Whang. | Roxane Wicky |
