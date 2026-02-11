# Document and Records Control Procedure

| | |
|---|---|
| **Reference** | PRO-DOC-001 |
| **Version** | 0.2 |
| **Creation date** | 10/02/2026 |
| **Revision date** | 10/02/2026 |
| **Written by** | Roxane Wicky |
| **Approved by** | Roxane Wicky |

---

## 1. Purpose

Define the rules for creation, approval, distribution, updating, and archiving of all documents and records of the Quality Management System (QMS) of Plus Sarl.

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
| Creation and updating of documents | Roxane Wicky (managing director) |
| Approval of documents | Roxane Wicky (managing director) |
| Distribution and archiving | Roxane Wicky (managing director) |
| Retention of manufacturing technical data | Chinese partners (Yuyao Mould Factory and second specialized partner) |

> **Note:** As Plus Sarl is a sole proprietorship, all document management responsibilities rest with the managing director, Roxane Wicky.

## 4. Document Types

| Type | Codification | Example |
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
| Management list | LST-XXX-NNN | LST-DOC-001 |
| External document | EXT-XXX-NNN | EXT-NRM-001 |

**Legend:** XXX = domain (QUA=quality, DOC=documents, AUD=audit, NCF=nonconformity, ACR=corrective actions, ACH=purchasing, EVF=supplier evaluation, SAT=satisfaction, RDR=management review, CMP=competencies, RCL=complaints, CTR=inspection)

## 5. Document Management Procedure

### 5.1 Document Creation

1. Identify the need to create a new document
2. Draft the document using the appropriate template (templates stored in the QMS folder)
3. Assign a reference according to the codification defined in section 4
4. Indicate the version (1.0 for initial creation)
5. Date and approve (signature of Roxane Wicky)

### 5.2 Approval

- All QMS documents are approved by the managing director, Roxane Wicky, before distribution
- Approval is evidenced by the signature and date on the document

### 5.3 Distribution and Storage

Approved documents are stored on the following media:

| Storage Medium | Content | Responsible |
|---|---|---|
| **FileMaker** (main software) | Product library, order tracking, pricing, transport tracking | Roxane Wicky |
| **Local computer files** (computer) | QMS documents, procedures, forms, quality records | Roxane Wicky |
| **Email archives** | Communications with customers, carriers, customs | Roxane Wicky |
| **WeChat** | Operational communications with Chinese partners | Roxane Wicky |
| **Files at the Chinese partner** | Manufacturing technical data, drawings, moulds, production specifications | Yuyao Mould Factory / second partner |

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
- Minimum retention period for archives: 3 years

### 5.6 Documents of External Origin

| External Document | Source | Storage Location | Responsible for Updating |
|---|---|---|---|
| ISO 9001:2015 standard | SNV / ISO | QMS folder > 06_External_documents > Standards | Roxane Wicky |
| Customer technical specifications | European customers | QMS folder > 06_External_documents > Customer_specifications + FileMaker | Roxane Wicky |
| Manufacturing technical data (drawings, moulds) | Yuyao Mould Factory / second partner | Files at the Chinese partner + local copy | Roxane Wicky / Chinese partner |
| Customs and regulatory documents | Customs authorities / freight forwarders | Email archives + local folder | Roxane Wicky |
| Supplier inspection reports | Chinese partners | QMS folder > 06_External_documents > Supplier_documents | Roxane Wicky |

## 6. Records Management

### 6.1 Operational Documents Generated by Business Activities

| Type of Operational Document | Creation Medium | Storage Location |
|---|---|---|
| Customs invoices | Software / email | Email archives + local folder |
| Customer invoices | FileMaker / accounting software | FileMaker + local folder |
| Delivery notes | FileMaker / email | FileMaker + email archives |
| Order acknowledgements | Email | Email archives |
| Transport tracking | FileMaker | FileMaker |
| Communications with Chinese partners | WeChat / email | WeChat + email archives |

### 6.2 Retention Period

| Record Type | Minimum Retention Period |
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
- **Access management** to FileMaker (access restricted to the managing director)

> **[TO BE CONFIRMED - exact backup method]**: The precise backup method (frequency, destination medium, local and/or cloud backup, automation) must be confirmed and documented. It is recommended to implement at minimum:
> - An automatic daily backup (local or cloud)
> - A weekly backup on external media
> - A monthly verification of backup integrity

## 7. Master Document List

| Reference | Title | Version | Date | Status |
|---|---|---|---|---|
| POL-QUA-001 | Quality Policy | 0.2 | 10/02/2026 | In effect |
| DOM-QUA-001 | Scope | 0.2 | 10/02/2026 | In effect |
| CTX-QUA-001 | Context of the Organization | 0.2 | 10/02/2026 | In effect |
| CRT-QUA-001 | Process Map | 0.2 | 10/02/2026 | In effect |
| OBJ-QUA-001 | Quality Objectives | 0.2 | 10/02/2026 | In effect |
| FIC-PRO-001 | Process Sheet (template) | 0.2 | 10/02/2026 | In effect |
| PRO-DOC-001 | Document Control | 0.2 | 10/02/2026 | In effect |
| PRO-AUD-001 | Internal Audit | 0.2 | 10/02/2026 | In effect |
| PRO-NCF-001 | Nonconformities | 0.2 | 10/02/2026 | In effect |
| PRO-ACR-001 | Corrective Actions | 0.2 | 10/02/2026 | In effect |
| PRO-ACH-001 | Purchasing and Subcontracting | 0.2 | 10/02/2026 | In effect |
| FOR-EVF-001 | Supplier Evaluation | 0.2 | 10/02/2026 | In effect |
| FOR-SAT-001 | Customer Satisfaction | 0.2 | 10/02/2026 | In effect |
| FOR-RDR-001 | Management Review | 0.2 | 10/02/2026 | In effect |
| FOR-CMP-001 | Competencies and Training | 0.2 | 10/02/2026 | In effect |
| FOR-RCL-001 | Customer Complaints | 0.2 | 10/02/2026 | In effect |
| FOR-CTR-001 | Incoming Inspection | 0.2 | 10/02/2026 | In effect |
| CHK-AUD-001 | ISO 9001 Audit Checklist | 0.2 | 10/02/2026 | In effect |
| LST-DOC-001 | Document Management List | 0.2 | 10/02/2026 | In effect |

## 8. Document Management List (LST-DOC-001)

The document management list below lists all QMS documents with their current status. This list is maintained by the managing director.

| Document Name | Reference/Code | Version | Update Date | Responsible | Location |
|---|---|---|---|---|---|
| Quality Policy | POL-QUA-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Scope | DOM-QUA-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Context of the Organization | CTX-QUA-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Process Map | CRT-QUA-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Quality Objectives | OBJ-QUA-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Process Sheet (template) | FIC-PRO-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Document Control | PRO-DOC-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Internal Audit | PRO-AUD-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Nonconformities | PRO-NCF-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Corrective Actions | PRO-ACR-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Purchasing and Subcontracting | PRO-ACH-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Supplier Evaluation | FOR-EVF-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Customer Satisfaction | FOR-SAT-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Management Review | FOR-RDR-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Competencies and Training | FOR-CMP-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Customer Complaints | FOR-RCL-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Incoming Inspection | FOR-CTR-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| ISO 9001 Audit Checklist | CHK-AUD-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Document Management List | LST-DOC-001 | 0.2 | 10/02/2026 | Roxane Wicky | Computer / QMS Folder |

---

## Revision History

| Version | Date | Description of Modification | Author |
|---|---|---|---|
| 0.1 | 10/02/2026 | Initial creation | Roxane Wicky |
| 0.2 | 10/02/2026 | Addition of the document management list (LST-DOC-001) aligned with the managing director's template. Addition of the LST (Management list) document type. Update of the master list with all QMS documents in version 0.2. | Roxane Wicky |
