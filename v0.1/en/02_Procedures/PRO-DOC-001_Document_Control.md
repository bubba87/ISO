# Document and Records Control Procedure

| | |
|---|---|
| **Reference** | PRO-DOC-001 |
| **Version** | 1.0 |
| **Date created** | 10/02/2026 |
| **Date revised** | 10/02/2026 |
| **Written by** | Roxane Wicky |
| **Approved by** | Roxane Wicky |

---

## 1. Purpose

Define the rules for the creation, approval, distribution, updating and archiving of all documents and records of the Quality Management System (QMS) of Plus Sarl.

## 2. Scope

This procedure applies to all QMS documents:
- Quality policy, objectives, process map
- Procedures, work instructions
- Forms and records
- Documents of external origin (standards, customer specifications, customs regulatory requirements, etc.)
- Operational documents (customs invoices, customer invoices, delivery notes, order acknowledgements)

> **Note:** Clause 8.3 (Design and development) is excluded from the scope of the Plus Sarl QMS. The company does not carry out any design activities; it provides industrial coordination between European customers and Chinese manufacturers.

## 3. Responsibilities

| Responsibility | Who |
|---|---|
| Document creation and updating | Roxane Wicky (managing director) |
| Document approval | Roxane Wicky (managing director) |
| Distribution and archiving | Roxane Wicky (managing director) |
| Retention of technical manufacturing data | Chinese partners (Yuyao Mould Factory and second specialised partner) |

> **Note:** Plus Sarl being a sole proprietorship, all document control responsibilities fall to the managing director, Roxane Wicky.

## 4. Document Types

| Type | Coding | Example |
|---|---|---|
| Policy | POL-XXX-NNN | POL-QUA-001 |
| Scope | DOM-XXX-NNN | DOM-QUA-001 |
| Context | CTX-XXX-NNN | CTX-QUA-001 |
| Process map | CRT-XXX-NNN | CRT-QUA-001 |
| Objectives | OBJ-XXX-NNN | OBJ-QUA-001 |
| Process sheet | FIC-PRO-NNN | FIC-PRO-001 |
| Procedure | PRO-XXX-NNN | PRO-DOC-001 |
| Form | FOR-XXX-NNN | FOR-EVF-001 |
| Checklist | CHK-XXX-NNN | CHK-AUD-001 |
| External document | EXT-XXX-NNN | EXT-NRM-001 |

**Legend:** XXX = domain (QUA=quality, DOC=documents, AUD=audit, NCF=nonconformity, ACR=corrective actions, ACH=purchasing, EVF=supplier evaluation, SAT=satisfaction, RDR=management review, CMP=competencies, RCL=complaints, CTR=inspection)

## 5. Document Management Procedure

### 5.1 Document Creation

1. Identify the need to create a new document
2. Draft the document using the corresponding template (templates stored in the QMS folder)
3. Assign a reference according to the coding defined in section 4
4. Indicate the version (1.0 for creation)
5. Date and approve (signature of Roxane Wicky)

### 5.2 Approval

- All QMS documents are approved by the managing director, Roxane Wicky, before distribution
- Approval is evidenced by the signature and date on the document

### 5.3 Distribution and Storage

Approved documents are stored on the following media:

| Storage medium | Content | Responsible |
|---|---|---|
| **FileMaker** (main software) | Product library, order tracking, prices, transport tracking | Roxane Wicky |
| **Local computer files** (computer) | QMS documents, procedures, forms, quality records, correspondence | Roxane Wicky |
| **Email archives** | Exchanges with customers, carriers, customs | Roxane Wicky |
| **WeChat** | Operational exchanges with Chinese partners | Roxane Wicky |
| **Files at the Chinese partner** | Technical manufacturing data, drawings, moulds, production specifications | Yuyao Mould Factory / second partner |

**Storage structure on the computer:**

```
QMS/
|-- 01_Policy_and_objectives/
|-- 02_Context_and_processes/
|-- 03_Procedures/
|-- 04_Blank_forms/
|-- 05_Records/
|   |-- [Year]/
|       |-- Nonconformities/
|       |-- Supplier_evaluations/
|       |-- Customer_satisfaction/
|       |-- Audits/
|       |-- Management_review/
|       |-- Orders/
|-- 06_External_documents/
|   |-- Standards/
|   |-- Customer_specifications/
|   |-- Supplier_documents/
```

### 5.4 Updating (Revision)

1. Identify the need for modification
2. Modify the document
3. Increment the version number (1.0 -> 1.1 for minor modification, 1.0 -> 2.0 for major modification)
4. Update the revision date
5. Record the modification in the revision history
6. Approve and replace the previous version

### 5.5 Obsolete Documents

- Obsolete versions are moved to an "Archive" folder with the label "OBSOLETE"
- Minimum archive retention period: 3 years

### 5.6 Documents of External Origin

| External document | Source | Storage location | Responsible for updating |
|---|---|---|---|
| ISO 9001:2015 standard | SNV / ISO | QMS folder > 06_External_documents > Standards | Roxane Wicky |
| Customer technical specifications | European customers | QMS folder > 06_External_documents > Customer_specifications + FileMaker | Roxane Wicky |
| Technical manufacturing data (drawings, moulds) | Yuyao Mould Factory / second partner | Files at the Chinese partner + local copy | Roxane Wicky / Chinese partner |
| Customs and regulatory documents | Customs authorities / freight forwarders | Email archives + local folder | Roxane Wicky |
| Supplier inspection reports | Chinese partners | QMS folder > 06_External_documents > Supplier_documents | Roxane Wicky |

## 6. Records Management

### 6.1 Operational Documents Generated by the Business

| Type of operational document | Creation medium | Storage location |
|---|---|---|
| Customs invoices | Software / email | Email archives + local folder |
| Customer invoices | FileMaker / accounting software | FileMaker + local folder |
| Delivery notes | FileMaker / email | FileMaker + email archives |
| Order acknowledgements | Email | Email archives |
| Transport tracking | FileMaker | FileMaker |
| Exchanges with Chinese partners | WeChat / email | WeChat + email archives |

### 6.2 Retention Period

| Record type | Minimum retention period |
|---|---|
| Quality policy (successive versions) | Duration of certification + 1 year |
| Management review | 3 years |
| Internal audits | 3 years |
| Nonconformities and corrective actions | 3 years |
| Supplier evaluations | 3 years |
| Customer complaints | 3 years |
| Customer satisfaction | 3 years |
| Customer orders | 5 years (Swiss legal requirement) |
| Invoices | 10 years (Swiss legal requirement) |
| Product technical data (moulds) | Mould lifespan + 3 years |

### 6.3 Backup

FileMaker data is protected by:
- **Digital backup** of FileMaker databases
- **Access management** for FileMaker (access restricted to the managing director)

> **[TO BE CONFIRMED - exact backup method]**: The precise backup method (frequency, destination medium, local and/or cloud backup, automation) must be confirmed and documented. It is recommended to implement at a minimum:
> - An automatic daily backup (local or cloud)
> - A weekly backup to an external medium
> - A monthly verification of backup integrity

## 7. Master List of Documents

| Reference | Title | Version | Date | Status |
|---|---|---|---|---|
| POL-QUA-001 | Quality Policy | 1.0 | 10/02/2026 | In force |
| DOM-QUA-001 | Scope | 1.0 | 10/02/2026 | In force |
| CTX-QUA-001 | Context of the Organisation | 1.0 | 10/02/2026 | In force |
| CRT-QUA-001 | Process Map | 1.0 | 10/02/2026 | In force |
| OBJ-QUA-001 | Quality Objectives | 1.0 | 10/02/2026 | In force |
| FIC-PRO-001 | Process Sheet (template) | 1.0 | 10/02/2026 | In force |
| PRO-DOC-001 | Document Control | 1.0 | 10/02/2026 | In force |
| PRO-AUD-001 | Internal Audit | 1.0 | 10/02/2026 | In force |
| PRO-NCF-001 | Nonconformities | 1.0 | 10/02/2026 | In force |
| PRO-ACR-001 | Corrective Actions | 1.0 | 10/02/2026 | In force |
| PRO-ACH-001 | Purchasing and Subcontracting | 1.0 | 10/02/2026 | In force |

---

## Revision History

| Version | Date | Description of change | Author |
|---|---|---|---|
| 1.0 | 10/02/2026 | Initial creation | Roxane Wicky |
