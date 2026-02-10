# Corrective Actions Procedure

| | |
|---|---|
| **Reference** | PRO-CAR-001 |
| **Version** | 1.0 |
| **Creation date** | [DD/MM/YYYY] |
| **Revision date** | [DD/MM/YYYY] |
| **Written by** | [Name of the manager] |
| **Approved by** | [Name of the manager] |

---

## 1. Purpose

Define the rules for cause analysis, implementation, and verification of the effectiveness of corrective actions in order to eliminate the causes of nonconformities and prevent their recurrence.

## 2. Scope

Any nonconformity requiring a corrective action:
- Major NCs (systematically)
- Recurring minor NCs
- Internal or external audit NCs
- Significant customer complaints
- Any situation where the manager deems it necessary to act on the causes

## 3. Definitions

| Term | Definition |
|---|---|
| **Correction** | Action to eliminate a detected NC (immediate treatment of the symptom) |
| **Corrective action** | Action to eliminate the **cause** of an NC and prevent its recurrence |
| **Root cause** | The fundamental cause at the origin of the NC |
| **Effectiveness verification** | Check that the corrective action has effectively prevented the recurrence of the NC |

> **Key difference:**
> - Correction = "I replaced the defective part" (symptom)
> - Corrective action = "I modified the specifications to clarify the tolerance" (cause)

## 4. Responsibilities

| Responsibility | Who |
|---|---|
| Decide to open a CA | Manager |
| Analyze the causes | Manager (with the Chinese partner if manufacturing NC) |
| Define the corrective action | Manager |
| Implement | Manager (or Chinese partner) |
| Verify effectiveness | Manager |

## 5. Procedure

### 5.1 Flowchart

```
    NC requiring a corrective action
    (see criteria in section 2)
            |
            v
    +------------------------+
    | 1. Open the CA form    |---> CA-[YYYY]-[NNN]
    +------------------------+
            |
            v
    +------------------------+
    | 2. Analyze the causes  |---> 5 Whys method / Ishikawa
    +------------------------+
            |
            v
    +------------------------+
    | 3. Identify the root   |---> Root cause documented
    |    cause               |
    +------------------------+
            |
            v
    +------------------------+
    | 4. Define the          |---> What, who, when
    |    corrective action   |
    +------------------------+
            |
            v
    +------------------------+
    | 5. Implement           |---> Application of the action
    +------------------------+
            |
            v
    +------------------------+
    | 6. Verify effectiveness|---> NC recurring? YES/NO
    +------------------------+
            |
       NC eliminated?
       /          \
     YES          NO
      |             |
      v             v
  +--------+   +-----------------+
  | Close  |   | New cause       |
  | the    |   | analysis        |
  | form   |   |                 |
  +--------+   +-----------------+
```

### 5.2 Detailed steps

**Step 1 - Open the CA form**

- Assign a number: CA-[YYYY]-[NNN]
- Link to the originating NC (NC-[YYYY]-[NNN])
- Describe the problem

**Step 2 - Analyze the causes**

Use one of the following methods:

#### 5 Whys Method (recommended for DUMMY Sarl)

| # | Why? | Answer |
|---|---|---|
| 1 | Why did the NC occur? | [Answer 1] |
| 2 | Why [Answer 1]? | [Answer 2] |
| 3 | Why [Answer 2]? | [Answer 3] |
| 4 | Why [Answer 3]? | [Answer 4] |
| 5 | Why [Answer 4]? | [Answer 5 = probable root cause] |

**Concrete example:**

| # | Why? | Answer |
|---|---|---|
| 1 | Why are the parts nonconforming? | The dimensions do not match the drawing |
| 2 | Why do the dimensions not match? | The partner used an incorrect machine setting |
| 3 | Why an incorrect setting? | The specifications did not specify the tolerances |
| 4 | Why were the tolerances not specified? | The specifications template does not include this section |
| 5 | **Root cause** | **The specifications template is incomplete** |

-> **Corrective action**: Update the specifications template to systematically include dimensional tolerances.

#### Ishikawa Diagram (cause and effect) - for complex cases

```
    Manpower        Method          Material
         |              |              |
         v              v              v
    +----|--------------|--------------|----+
    |                                       |
    |           PROBLEM (NC)                |
    |                                       |
    +----|--------------|--------------|----+
         ^              ^              ^
         |              |              |
    Environment      Machine      Measurement
```

Categories to analyze:
- **Manpower**: skills, training, communication
- **Method**: procedures, instructions, specifications
- **Material**: raw material, components, supplier
- **Environment**: environment, transport/storage conditions
- **Machine**: equipment, tooling, mold
- **Measurement**: instruments, inspection method, criteria

**Step 3 - Identify the root cause**

- Select the most probable cause
- Verify with data/evidence if possible

**Step 4 - Define the corrective action**

The corrective action must:
- Act on the root cause (not on the symptom)
- Be realistic and proportionate
- Have a responsible person and a deadline

**Step 5 - Implement**

- Carry out the action
- Document what was done
- Communicate if necessary (Chinese partner, customer)

**Step 6 - Verify effectiveness**

- Wait a sufficient period (generally 1 to 3 months)
- Verify that the NC has not recurred
- If the NC recurs: restart the cause analysis

## 6. Corrective Action Form (template)

### Identification

| Element | Detail |
|---|---|
| **CA No.** | CA-[YYYY]-[NNN] |
| **Opening date** | [DD/MM/YYYY] |
| **Originating NC** | NC-[YYYY]-[NNN] |
| **Source** | [ ] Incoming inspection [ ] Customer complaint [ ] Internal audit [ ] External audit [ ] Other |

### Problem description

| Element | Detail |
|---|---|
| **Description** | [Factual description of the problem] |
| **Impact** | [Consequences of the NC] |
| **Frequency/Recurrence** | [First occurrence / Recurring (how many times)] |

### Cause analysis

| Element | Detail |
|---|---|
| **Method used** | [ ] 5 Whys [ ] Ishikawa [ ] Other |
| **Analysis detail** | [See 5 Whys table or diagram] |
| **Identified root cause** | [Description of the root cause] |

### Action plan

| # | Corrective action | Responsible | Deadline | Status |
|---|---|---|---|---|
| 1 | [Description of the action] | [Who] | [Date] | [ ] Planned [ ] In progress [ ] Completed |
| 2 | [Description of the action] | [Who] | [Date] | [ ] Planned [ ] In progress [ ] Completed |
| 3 | [Description of the action] | [Who] | [Date] | [ ] Planned [ ] In progress [ ] Completed |

### Effectiveness verification

| Element | Detail |
|---|---|
| **Verification date** | [DD/MM/YYYY] (at least 1-3 months after implementation) |
| **Verification method** | [How you verify that the NC does not recur] |
| **Result** | [ ] Effective (NC not recurring) [ ] Not effective (NC recurring) |
| **Comment** | [Observations] |

### Closure

| Element | Detail |
|---|---|
| **Closure date** | [DD/MM/YYYY] |
| **Closed by** | [Name] |
| **Final status** | [ ] Closed [ ] In progress [ ] Reopening required |

---

## 7. Corrective actions register

| CA No. | Open date | Related NC | Root cause | Action | Deadline | Effective? | Status |
|---|---|---|---|---|---|---|---|
| CA-[YYYY]-001 | [date] | NC-xxx | [summary] | [summary] | [date] | [Y/N/In progress] | [Open/Closed] |
| CA-[YYYY]-002 | | | | | | | |
| CA-[YYYY]-003 | | | | | | | |

---

## 8. Indicators

| Indicator | Target | Frequency |
|---|---|---|
| Number of open CAs | Information | Quarterly |
| On-time closure rate | [> 80%] | Quarterly |
| CA effectiveness rate | [> 90%] | Annual |

---

> **Filling instructions:**
> 1. Only open a CA if it is justified (major NC, recurring, or from an audit)
> 2. Take the time to properly analyze the root cause - this is the key step
> 3. The 5 Whys method is simple and effective for a micro-enterprise
> 4. Involve the Chinese partner in the analysis when the NC comes from manufacturing
> 5. The auditor will verify that your CAs are effective (not just on paper)
