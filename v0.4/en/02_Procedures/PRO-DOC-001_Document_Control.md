# Document and Records Control Procedure

| | |
|---|---|
| **Reference** | PRO-DOC-001 |
| **Version** | 0.4 |
| **Date of creation** | 10/02/2026 |
| **Date of revision** | 22/02/2026 |
| **Written by** | Roxane Wicky |
| **Approved by** | Roxane Wicky |

> **Legend:** :red_circle: [TO BE COMPLETED] = mandatory, missing | :yellow_circle: [RECOMMENDED] = recommended | :green_circle: = already filled | :blue_circle: [TO BE VERIFIED] = to be confirmed

---

## 1. Purpose

Define the rules for creation, approval, distribution, updating and archiving of all documents and records of the Quality Management System (QMS) of Plus Sarl.

> **S1 — Document management: Document control and continual improvement (cf. CTX-QUA-001, section 1.1):** Information related to production and conformity is kept in the FileMaker system and in email and WeChat exchanges. These elements ensure the traceability of operations and feed into the monitoring of nonconformities, internal audit and management review, enabling continual improvement of the quality management system. 🟢

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
| Creation and updating of documents | :green_circle: Roxane Wicky (Managing Director) |
| Approval of documents | :green_circle: Roxane Wicky (Managing Director) |
| Distribution and archiving | :green_circle: Roxane Wicky (Managing Director) |
| Retention of manufacturing technical data | :green_circle: Chinese partners (Yuyao Mould Factory and Oukailuo) |
| Accounting and fiduciary | :green_circle: Paradiso (fiduciary) |

> **Note:** Plus Sarl being a sole proprietorship, all document responsibilities rest with the Managing Director, Roxane Wicky. The fiduciary Paradiso handles accounting management.

## 4. Document Types

| Type | Coding | Example |
|---|---|---|
| Policy | POL-XXX-NNN | POL-QUA-001 |
| Scope | DOM-XXX-NNN | DOM-QUA-001 |
| Context | CTX-XXX-NNN | CTX-QUA-001 |
| Process map | CRT-XXX-NNN | CRT-QUA-001 |
| Objectives | OBJ-XXX-NNN | OBJ-QUA-001 |
| Leadership / Management | M1-XXX-NNN | M1-DIR-001 |
| Process sheet | FIC-PRO-NNN | FIC-PRO-001, FIC-PRO-002 |
| Procedure | PRO-XXX-NNN | PRO-DOC-001 |
| Form | FOR-XXX-NNN | FOR-EVF-001 |
| Checklist | CHK-XXX-NNN | CHK-AUD-001 |
| Management list | LST-XXX-NNN | LST-DOC-001 |
| External document | EXT-XXX-NNN | EXT-NRM-001 |

**Legend:** XXX = domain (QUA=quality, DOC=documents, AUD=audit, NCF=nonconformity, ACR=corrective actions, ACH=purchasing, EVF=supplier evaluation, SAT=satisfaction, RDR=management review, CMP=competencies, RCL=complaints, CTR=inspection, AQF=quality agreement)

## 5. Document Management Procedure

### 5.1 Document Creation

1. Identify the need to create a new document
2. Draft the document using the corresponding template (templates stored in the QMS folder)
3. Assign a reference according to the coding defined in section 4
4. Indicate the version (1.0 for creation)
5. Date and approve (signature of Roxane Wicky)

### 5.2 Approval

- All QMS documents are approved by the Managing Director, Roxane Wicky, before distribution
- Approval is evidenced by the signature and date on the document

### 5.3 Distribution and Storage

Approved documents are stored on the following media:

| Storage medium | Content | Responsible |
|---|---|---|
| **FileMaker** (main software) | Product library, order tracking, prices, transport tracking | :green_circle: Roxane Wicky |
| **Local computer files** (computer) | QMS documents, procedures, forms, quality records | :green_circle: Roxane Wicky |
| **Email archives** | Exchanges with customers, carriers, customs | :green_circle: Roxane Wicky |
| **WeChat** | Operational exchanges with Chinese partners | :green_circle: Roxane Wicky |
| **Files at Chinese partner** | Manufacturing technical data, drawings, moulds, production specifications | :green_circle: Yuyao Mould Factory / Oukailuo |
| **Fiduciary Paradiso** | Accounting documents, tax returns | :green_circle: Paradiso |

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

- Obsolete versions are moved to an "Archive" folder with the marking "OBSOLETE"
- Minimum archive retention period: 3 years

### 5.6 Documents of External Origin

| External document | Source | Storage location | Responsible for updating |
|---|---|---|---|
| ISO 9001:2015 Standard | SNV / ISO | QMS folder > 06_External_documents > Standards | :green_circle: Roxane Wicky |
| Customer technical specifications | European customers (~10 active customers) | QMS folder > 06_External_documents > Customer_specifications + FileMaker | :green_circle: Roxane Wicky |
| Manufacturing technical data (drawings, moulds) | Yuyao Mould Factory / Oukailuo | Files at the Chinese partner + local copy | :green_circle: Roxane Wicky / Chinese partner |
| Customs and regulatory documents | Customs authorities / freight forwarders | Email archives + local folder | :green_circle: Roxane Wicky |
| Supplier inspection reports | Chinese partners | QMS folder > 06_External_documents > Supplier_documents | :green_circle: Roxane Wicky |
| Accounting documents | Fiduciary Paradiso | Fiduciary + local copy | :green_circle: Paradiso / Roxane Wicky |

## 6. Records Management

### 6.1 Operational Documents Generated by the Activity

| Type of operational document | Creation medium | Storage location |
|---|---|---|
| Customs invoices | Software / email | Email archives + local folder |
| Customer invoices | FileMaker / accounting software | FileMaker + local folder |
| Delivery notes | FileMaker / email | FileMaker + email archives |
| Order acknowledgements | Email | Email archives |
| Transport tracking | FileMaker | FileMaker |
| Exchanges with Chinese partners | WeChat / email | WeChat + email archives |
| Accounting documents | Fiduciary Paradiso | Fiduciary + local copy |

### 6.2 Retention Period

| Type of record | Minimum retention period |
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

:green_circle: Cloud backup, hosted by IT service provider. FileMaker data and QMS files are automatically backed up to the cloud.

Data is protected by:
- **Automatic cloud backup**: FileMaker data and QMS files are automatically backed up to the cloud, hosted by the IT service provider
- **Access management** to FileMaker (access restricted to the Managing Director)

> :yellow_circle: [RECOMMENDED] It is recommended to supplement the cloud backup system with:
> - Periodic (monthly) verification of backup integrity
> - An annual restoration test to validate data recovery capability
> - Documentation of the contract with the cloud service provider (SLA, data location, privacy policy)

## 7. Mould Inventory

:green_circle: A mould inventory exists. The moulds are the property of the customers.

| Element | Detail |
|---|---|
| **Inventory** | :green_circle: Existing |
| **Ownership** | :green_circle: Property of the customers |
| **Storage location** | At the Chinese partners (Yuyao Mould Factory / Oukailuo) |
| **Tracking responsible** | Roxane Wicky (Managing Director) |
| **Retention** | Mould lifespan + 3 years (cf. section 6.2) |

> **Note:** As the moulds are the property of the customers, Plus Sarl ensures the coordination of their storage and maintenance at the Chinese partners. Mould traceability is ensured via FileMaker and exchanges with the partners.

## 8. Master Document List

| Reference | Title | Version | Date | Status |
|---|---|---|---|---|
| POL-QUA-001 | Quality Policy | 0.4 | 18/02/2026 | In force |
| DOM-QUA-001 | Scope | 0.4 | 18/02/2026 | In force |
| CTX-QUA-001 | Context of the Organisation | 0.4 | 18/02/2026 | In force |
| CRT-QUA-001 | Process Map | 0.4 | 18/02/2026 | In force |
| OBJ-QUA-001 | Quality Objectives | 0.4 | 18/02/2026 | In force |
| FIC-PRO-001 | Process Sheet O2 - Purchasing and Subcontracting | 0.4 | 18/02/2026 | In force |
| **FIC-PRO-002** | **Process Sheet O3 - Logistics and Delivery** | **0.4** | **18/02/2026** | **In force** 🟢 |
| **M1-DIR-001** | **Leadership and Assignment of Responsibilities** | **0.4** | **18/02/2026** | **In force** 🟢 |
| PRO-DOC-001 | Document Control | 0.4 | 18/02/2026 | In force |
| PRO-AUD-001 | Internal Audit | 0.4 | 18/02/2026 | In force |
| PRO-NCF-001 | Nonconformities | 0.4 | 18/02/2026 | In force |
| PRO-ACR-001 | Corrective Actions | 0.4 | 18/02/2026 | In force |
| PRO-ACH-001 | Purchasing and Subcontracting | 0.4 | 18/02/2026 | In force |
| **PRO-LOG-001** | **Logistics and Delivery** | **0.4** | **18/02/2026** | **In force** 🟢 |
| FOR-EVF-001 | Supplier Evaluation | 0.4 | 18/02/2026 | In force |
| FOR-SAT-001 | Customer Satisfaction | 0.4 | 18/02/2026 | In force |
| FOR-RDR-001 | Management Review | 0.4 | 18/02/2026 | In force |
| FOR-CMP-001 | Competencies and Training | 0.4 | 18/02/2026 | In force |
| FOR-RCL-001 | Customer Complaints | 0.4 | 18/02/2026 | In force |
| FOR-CTR-001 | Incoming Inspection | 0.4 | 18/02/2026 | In force |
| CHK-AUD-001 | ISO 9001 Audit Checklist | 0.4 | 18/02/2026 | In force |
| FOR-AQF-001 | Quality Agreement — Hardeng Yuyao Mould Factory | 0.4 | 22/02/2026 | Active |
| FOR-AQF-002 | Quality Agreement — Oukailuo | 0.4 | 22/02/2026 | Active |
| LST-DOC-001 | Document Management List | 0.4 | 18/02/2026 | In force |

## 9. Document Management List (LST-DOC-001)

The document management list below records all QMS documents with their current status. This list is maintained by the Managing Director.

| Document name | Reference/code | Version | Date of update | Responsible | Location |
|---|---|---|---|---|---|
| Quality Policy | POL-QUA-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Scope | DOM-QUA-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Context of the Organisation | CTX-QUA-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Process Map | CRT-QUA-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Quality Objectives | OBJ-QUA-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Process Sheet O2 - Purchasing and Subcontracting | FIC-PRO-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| **Process Sheet O3 - Logistics and Delivery** | **FIC-PRO-002** | **0.4** | **18/02/2026** | **Roxane Wicky** | **Computer / QMS Folder** 🟢 |
| **Leadership and Assignment of Responsibilities** | **M1-DIR-001** | **0.4** | **18/02/2026** | **Roxane Wicky** | **Computer / QMS Folder** 🟢 |
| Document Control | PRO-DOC-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Internal Audit | PRO-AUD-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Nonconformities | PRO-NCF-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Corrective Actions | PRO-ACR-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Purchasing and Subcontracting | PRO-ACH-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| **Logistics and Delivery** | **PRO-LOG-001** | **0.4** | **18/02/2026** | **Roxane Wicky** | **Computer / QMS Folder** 🟢 |
| Supplier Evaluation | FOR-EVF-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Customer Satisfaction | FOR-SAT-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Management Review | FOR-RDR-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Competencies and Training | FOR-CMP-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Customer Complaints | FOR-RCL-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Incoming Inspection | FOR-CTR-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| ISO 9001 Audit Checklist | CHK-AUD-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Quality Agreement — Hardeng Yuyao Mould Factory | FOR-AQF-001 | 0.4 | 22/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Quality Agreement — Oukailuo | FOR-AQF-002 | 0.4 | 22/02/2026 | Roxane Wicky | Computer / QMS Folder |
| Document Management List | LST-DOC-001 | 0.4 | 18/02/2026 | Roxane Wicky | Computer / QMS Folder |

---

## Revision History

| Version | Date | Description of modification | Author |
|---|---|---|---|
| 0.1 | 10/02/2026 | Initial creation | Roxane Wicky |
| 0.2 | 10/02/2026 | Addition of the document management list (LST-DOC-001) aligned with the Managing Director's template. Addition of the LST (Management list) document type. Update of the master list with all QMS documents in version 0.2. | Roxane Wicky |
| 0.3 | 12/02/2026 | Integration of responses (Oukailuo, Paradiso, SQS, cloud, QC sampling). Addition of the field legend system. | Roxane Wicky |
| 0.4 | 18/02/2026 | Integration of UPDATE 2.1 S1: addition of reference to the formalised role of document management (CTX-QUA-001 section 1.1). Addition of 3 new documents to the master list and the management list: M1-DIR-001, FIC-PRO-002, PRO-LOG-001. Addition of the M1 (Leadership) document type. | Roxane Wicky |
| 0.4 | 22/02/2026 | Addition of FOR-AQF-001 and FOR-AQF-002 to master list. Oukailuo replaces Whang. | Roxane Wicky |
