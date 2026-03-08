# PS01 - Document Management Process

| **Process**         | PS01 - Document Management                             |
|----------------------|------------------------------------------------------|
| **Type**            | Support                                               |
| **Owner**           | Document Management Role                              |
| **Version**         | v0.7                                                  |
| **Date**            | 2026-03-04                                            |
| **Reference**       | PR-PS01-GD                                              |
| **ISO 9001 Standard** | Clause 7.5                                          |

---

## 1. Purpose and Scope

This process describes the document management of the Quality Management System (QMS) of **Plus Sàrl**. It covers the creation, revision, approval, distribution, archiving, and disposal of QMS documents and records.

---

## 2. Normative References

- ISO 9001:2015, Clause 7.5 (Documented Information)
- Plus Sàrl Quality Manual (MQ-001)

---

## 3. Roles and Responsibilities

| Role                        | Key Responsibilities                                                 |
|-----------------------------|----------------------------------------------------------------------|
| **Document Management**     | Administration of the document system, version control, distribution |
| **Process Owners**          | Drafting and updating documents for their process                    |
| **Executive Management**    | Approval of strategic documents (Manual, Policy)                     |
| **Quality Manager**         | Verification of document compliance, approval of procedures          |

---

## 4. Coding System

### 4.1 Document Types

| Code Prefix | Document Type               | Description                                          |
|-------------|---------------------------|------------------------------------------------------|
| **MQ**      | Quality Manual             | Strategic document describing the QMS                |
| **PR**      | Procedure                  | Detailed description of a process                    |
| **IT**      | Work Instruction           | Detailed operating method for a specific task        |
| **FM**      | Form                       | Template to be completed to record data              |
| **EN**      | Record                     | Evidence of an activity being performed              |

### 4.2 Coding Convention

The document code follows the structure below:

```
[TYPE]-[PROCESS]-[IDENTIFIER]
```

**Examples:**
- `MQ-001`: Quality Manual, main document
- `PR-P01-COM`: P01 Commercial process procedure
- `IT-P04-ECH`: AQL sampling work instruction (P04)
- `FM-P02-AQF`: Supplier Quality Agreement form (P02)
- `EN-P03-POD`: Proof of delivery records (P03)

### 4.3 Version Convention

Versions follow the **vX.Y** format:
- **X** (major): Significant structural or substantive modification
- **Y** (minor): Correction, adjustment, minor update

Examples: v0.1, v0.7, v1.0, v1.1, v2.0

---

## 5. Input and Output Data

### Input Data
- Need for document creation or modification
- Normative and regulatory requirements
- Audit feedback (internal or external)
- Process owner requests
- Obsolete documents requiring revision

### Output Data
- Approved and distributed documents
- Up-to-date document register (FM-PS01-GD)
- Archived or disposed obsolete documents
- Version history

---

## 6. Activity Description

### A1 - Identification of Document Need

The Document Management Role or the Process Owner identifies the need to create, modify, or delete a document. The need is formalized and justified.

### A2 - Document Drafting or Revision

The designated author (generally the relevant Process Owner) drafts or revises the document in accordance with defined templates and coding conventions. The document is identified with its code, version, date, and status.

### A3 - Verification

The Document Management Role verifies document compliance: adherence to coding conventions, consistency with the QMS, absence of contradictions, completeness.

### A4 - Approval

The document is approved by the authorized person according to the approval matrix:
- Quality Manual, Policy: Executive Management
- Procedures: Quality Manager
- Work Instructions, Forms: Process Owner

### A5 - Distribution and Availability

The Document Management Role distributes the approved document to the relevant recipients, updates the document register (FM-PS01-GD), and ensures the withdrawal of obsolete versions.

### A6 - Records Management and Archiving

The Document Management Role ensures the preservation of records according to defined retention periods, under conditions that guarantee their readability, integrity, and accessibility.

### A7 - Periodic Review and Disposal

The Document Management Role conducts a periodic review (annual) of documentation to identify documents requiring update or disposal. Documents beyond their retention period are disposed of in a controlled manner.

---

## 7. Swimlane Diagram

```
 PROCESS PS01 - DOCUMENT MANAGEMENT
 ============================================================================

 Role                 | Activity Flow
 ============================================================================
                      |
 DOCUMENT             |  [A1 Identify]         [A3 Verify]
 MANAGEMENT           |  the document     ---> document
                      |  need                  compliance
                      |       |                       |
                      |       |                       v
                      |       |                  Compliant?
                      |       |                  YES --> [A5]
                      |       |                  NO  --> Return to
                      |       |                          author
                      |       |                       |
                      |       |                       v
                      |       |              [A5 Distribute]
                      |       |              and make
                      |       |              available
                      |       |              (FM-PS01-GD)
                      |       |                   |
                      |       |                   v
                      |       |              [A6 Archive]
                      |       |              records
                      |       |              (retention periods)
                      |       |                   |
                      |       |                   v
                      |       +------------>[A7 Periodic review]
                      |                     and controlled
                      |                     disposal
                      |
 ============================================================================
                      |
 PROCESS              |  [A2 Draft / Revise]
 OWNERS               |  the document per
                      |  templates and coding
                      |  (MQ/PR/IT/FM/EN)
                      |       |
                      |       v
                      |  Submit for
                      |  verification (A3)
                      |
 ============================================================================
                      |
 QUALITY              |  [A4 Approve]
 MANAGER              |  Procedures (PR)
                      |  Verify QMS compliance
                      |
 ============================================================================
                      |
 EXECUTIVE            |  [A4 Approve]
 MANAGEMENT           |  Quality Manual (MQ)
                      |  Quality Policy
                      |
 ============================================================================
```

---

## 8. Record Retention Periods

| Record Type                         | Retention Period | Storage Location         |
|--------------------------------------|------------------|--------------------------|
| Quality Manual (previous versions)   | 5 years          | Document server          |
| Procedures (previous versions)       | 3 years          | Document server          |
| Audit reports                        | 5 years          | Document server          |
| Non-conformity reports               | 5 years          | Document server          |
| Inspection reports                   | 5 years          | Document server          |
| Supplier evaluations                 | 3 years          | Document server          |
| Management review minutes           | 5 years          | Document server          |
| Customer satisfaction surveys        | 3 years          | Document server          |
| Purchase orders                      | 5 years          | Document server          |
| Transport documents                  | 5 years          | Document server          |

---

## 9. Interactions with Other Processes

| Process                | Nature of Interaction                                  |
|------------------------|--------------------------------------------------------|
| PM01 - Leadership      | Strategic documents, management review                 |
| P01 - Commercial       | Proposals, contracts, satisfaction surveys              |
| P02 - Purchasing       | SQAs, supplier evaluations, orders                     |
| P04 - Logistics        | Transport documents, proofs of delivery                |
| P03 - Quality Control  | Inspection reports, NCs, audits                        |

---

## 10. Key Performance Indicators (KPI)

| Indicator                                 | Formula / Method                                   | Target         | Frequency    |
|-------------------------------------------|---------------------------------------------------|----------------|--------------|
| Up-to-date document rate                  | Up-to-date documents / Total documents x 100       | 100%           | Quarterly    |
| Average document processing time          | Sum of times (creation to approval) / Number       | < 10 days      | Quarterly    |
| Document compliance rate                  | Compliant documents / Verified documents x 100     | 100%           | Semi-annual  |
| Number of obsolete documents in circulation | Count                                            | 0              | Quarterly    |
| Annual review completion rate             | Documents reviewed / Documents to review x 100     | 100%           | Annual       |

---

## 11. Associated Documents and Records

| Code         | Title                                 | Type          |
|--------------|---------------------------------------|---------------|
| PR-PS01-GD   | Document Management Procedure         | Procedure     |
| FM-PS01-GD   | Document Register                     | Form          |
| IT-PS01-COD  | Coding Instruction                    | Instruction   |
| FM-PS01-DEM  | Document Modification Request         | Form          |

---

## 12. Continual Improvement

Improvement of the document management process is based on:
- Annual documentation review
- Audit findings related to documentation
- Simplification of templates and procedures
- Digitalization and automation of document workflows
- Feedback from document system users

---

*Controlled document - Plus Sàrl - ISO 9001:2015 Quality Management System*
*Version v0.7 - 2026-03-04*
