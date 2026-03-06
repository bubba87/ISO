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

## 1. Purpose and scope

This process describes the document management of the Quality Management System (QMS) of **Plus Sarl**. It covers the creation, revision, approval, distribution, archiving and destruction of QMS documents and records.

---

## 2. Normative references

- ISO 9001:2015, Clause 7.5 (Documented information)
- Plus Sarl Quality Manual (MQ-001)

---

## 3. Roles and responsibilities

| Role                        | Key responsibilities                                                 |
|-----------------------------|----------------------------------------------------------------------|
| **Document Management**     | Administration of the document system, version control, distribution |
| **Process owners**          | Drafting and updating documents for their process                    |
| **Management**              | Approval of strategic documents (Manual, Policy)                     |
| **Quality Manager**         | Verification of document compliance, approval of procedures          |

---

## 4. Coding system

### 4.1 Document types

| Code prefix  | Document type               | Description                                          |
|-------------|---------------------------|------------------------------------------------------|
| **MQ**      | Quality Manual             | Strategic document describing the QMS                |
| **PR**      | Procedure                  | Detailed description of a process                    |
| **IT**      | Work instruction           | Detailed operating procedure for a specific task     |
| **FM**      | Form                       | Template to be completed for recording data          |
| **EN**      | Record                     | Evidence of an activity having been performed        |

### 4.2 Coding convention

The document code follows this structure:

```
[TYPE]-[PROCESS]-[IDENTIFIER]
```

**Examples:**
- `MQ-001`: Quality Manual, main document
- `PR-P01-COM`: Procedure for process P01 Sales
- `IT-P04-ECH`: Work instruction for AQL sampling (P04)
- `FM-P02-AQF`: Supplier Quality Agreement form (P02)
- `EN-P03-POD`: Proofs of delivery record (P03)

### 4.3 Version convention

Versions follow the format **vX.Y**:
- **X** (major): Significant structural or substantive change
- **Y** (minor): Correction, adjustment, minor update

Examples: v0.1, v0.7, v1.0, v1.1, v2.0

---

## 5. Input and output data

### Input data
- Need for document creation or modification
- Normative and regulatory requirements
- Audit findings (internal or external)
- Requests from process owners
- Obsolete documents requiring revision

### Output data
- Approved and distributed documents
- Up-to-date document register (FM-PS01-GD)
- Obsolete documents archived or destroyed
- Version history

---

## 6. Description of activities

### A1 - Identification of document need

The Document Management Role or the Process Owner identifies the need to create, modify or delete a document. The need is formalised and justified.

### A2 - Document drafting or revision

The designated author (generally the relevant Process Owner) drafts or revises the document in compliance with the defined templates and coding conventions. The document is identified with its code, version, date and status.

### A3 - Verification

The Document Management Role verifies the document's compliance: adherence to coding conventions, consistency with the QMS, absence of contradictions, completeness.

### A4 - Approval

The document is approved by the authorised person according to the approval matrix:
- Quality Manual, Policy: Management
- Procedures: Quality Manager
- Work instructions, Forms: Process owner

### A5 - Distribution and availability

The Document Management Role distributes the approved document to the relevant recipients, updates the document register (FM-PS01-GD) and ensures the withdrawal of obsolete versions.

### A6 - Record management and archiving

The Document Management Role ensures the preservation of records according to defined retention periods, under conditions guaranteeing their legibility, integrity and accessibility.

### A7 - Periodic review and destruction

The Document Management Role conducts a periodic review (annual) of the documentation to identify documents requiring update or destruction. Documents beyond their retention period are destroyed in a controlled manner.

---

## 7. Swimlane diagram

```
 PROCESS PS01 - DOCUMENT MANAGEMENT
 ============================================================================

 Role                 | Activity flow
 ============================================================================
                      |
 DOCUMENT             |  [A1 Identify]         [A3 Verify]
 MANAGEMENT           |  document need    ---> document
                      |                        compliance
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
                      |                     destruction
                      |
 ============================================================================
                      |
 PROCESS              |  [A2 Draft / Revise]
 OWNERS               |  the document according to
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
 MANAGEMENT           |  [A4 Approve]
                      |  Quality Manual (MQ)
                      |  Quality Policy
                      |
 ============================================================================
```

---

## 8. Record retention periods

| Record type                          | Retention period | Storage location        |
|--------------------------------------|--------------------|------------------------|
| Quality Manual (previous versions)   | 5 years            | Document server        |
| Procedures (previous versions)       | 3 years            | Document server        |
| Audit reports                        | 5 years            | Document server        |
| Nonconformity reports                | 5 years            | Document server        |
| Inspection reports                   | 5 years            | Document server        |
| Supplier evaluations                 | 3 years            | Document server        |
| Management review minutes           | 5 years            | Document server        |
| Customer satisfaction surveys        | 3 years            | Document server        |
| Purchase orders                      | 5 years            | Document server        |
| Transport documents                  | 5 years            | Document server        |

---

## 9. Interactions with other processes

| Process                | Nature of interaction                                  |
|------------------------|--------------------------------------------------------|
| PM01 - Leadership        | Strategic documents, management review                |
| P01 - Sales            | Quotations, contracts, satisfaction surveys            |
| P02 - Purchasing       | SQAs, supplier evaluations, orders                     |
| P04 - Logistics        | Transport documents, proofs of delivery                |
| P03 - Quality Control  | Inspection reports, NCs, audits                        |

---

## 10. Key Performance Indicators (KPI)

| Indicator                                 | Formula / Method                                | Target         | Frequency    |
|-------------------------------------------|------------------------------------------------|----------------|--------------|
| Rate of up-to-date documents              | Up-to-date documents / Total documents x 100   | 100 %          | Quarterly    |
| Average document processing time          | Sum of times (creation to approval) / Count    | < 10 days      | Quarterly    |
| Document compliance rate                  | Compliant documents / Documents verified x 100 | 100 %          | Semi-annual  |
| Number of obsolete documents in circulation | Count                                         | 0              | Quarterly    |
| Annual review completion rate             | Documents reviewed / Documents to review x 100 | 100 %          | Annual       |

---

## 11. Associated documents and records

| Code         | Title                                 | Type          |
|--------------|---------------------------------------|---------------|
| PR-PS01-GD     | Document Management Procedure        | Procedure     |
| FM-PS01-GD     | Document Register                     | Form          |
| IT-PS01-COD    | Coding Instruction                    | Instruction   |
| FM-PS01-DEM    | Document Change Request               | Form          |

---

## 12. Continual improvement

Improvement of the document management process is based on:
- Annual documentation review
- Audit findings related to documentation
- Simplification of templates and procedures
- Digitalisation and automation of document workflows
- Feedback from document system users

---

*Controlled document - Plus Sarl - ISO 9001:2015 Quality Management System*
*Version v0.7 - 2026-03-04*
