# Quality Manual - Chapter 3: Quality Management System Support

| **Document**       | MQ_03_Support_SMQ                        |
|--------------------|------------------------------------------|
| **Version**        | v0.7                                     |
| **Date**           | 2026-03-04                               |
| **Classification** | Internal                                 |
| **Process**        | All processes                            |
| **Drafted by**     | Quality Role                             |
| **Approved by**    | Management                               |

---

## 3.1 QMS Organizational Structure

The Quality Management System of Plus Sarl is based on a functional role-based organization. Each role is defined by its responsibilities, authorities and interactions with other roles. The detailed competency matrix is managed in process PS02 - Competence Management (FM-PS02-MCO).

---

## 3.2 Role Map

### 3.2.1 Management

| Attribute             | Description                                                         |
|-----------------------|---------------------------------------------------------------------|
| **Mission**           | Drive the company strategy and ensure the effectiveness of the QMS  |
| **Responsibilities**  | Definition of the quality policy, resource allocation, management review, commitment to customer satisfaction |
| **Authority**         | Strategic decisions, approval of QMS documents, validation of quality objectives |
| **Processes managed** | PM01 - Strategic management, PS02 - Competence management           |

### 3.2.2 Commercial Role

| Attribute             | Description                                                         |
|-----------------------|---------------------------------------------------------------------|
| **Mission**           | Manage customer relations and ensure business development            |
| **Responsibilities**  | Analysis of customer requests, issuance of quotations, order tracking, customer complaint management |
| **Authority**         | Validation of commercial offers, acceptance of orders within the defined framework |
| **Processes managed** | P01 - Sales management                                               |

### 3.2.3 Purchasing Role

| Attribute             | Description                                                         |
|-----------------------|---------------------------------------------------------------------|
| **Mission**           | Select, qualify and manage international suppliers                   |
| **Responsibilities**  | Supplier prospecting, initial qualification, negotiation, order placement, periodic supplier evaluation |
| **Authority**         | Supplier selection, suspension of a nonconforming supplier           |
| **Processes managed** | P02 - Purchasing and sourcing                                        |

### 3.2.4 Logistics Role

| Attribute             | Description                                                         |
|-----------------------|---------------------------------------------------------------------|
| **Mission**           | Coordinate logistics operations and international shipments          |
| **Responsibilities**  | Transport planning, shipment tracking, customs documentation management, coordination with freight forwarders |
| **Authority**         | Choice of transport modes, validation of shipping documents          |
| **Processes managed** | P04 - Logistics and shipping                                         |

### 3.2.5 Quality Role

| Attribute             | Description                                                         |
|-----------------------|---------------------------------------------------------------------|
| **Mission**           | Ensure product conformity and QMS effectiveness                      |
| **Responsibilities**  | Inspection planning and execution, nonconformity management, internal audits, quality indicator monitoring, continual improvement |
| **Authority**         | Blocking of nonconforming products, initiation of corrective actions, product release decisions |
| **Processes managed** | P03 - Monitoring and quality control                                 |

### 3.2.6 Document Management Role

| Attribute             | Description                                                         |
|-----------------------|---------------------------------------------------------------------|
| **Mission**           | Ensure QMS document control                                          |
| **Responsibilities**  | Creation, revision and distribution of documents, records management, archiving, version control |
| **Authority**         | Validation of document compliance, withdrawal of obsolete documents  |
| **Processes managed** | PS01 - Document management                                          |

---

## 3.3 Role Interaction Matrix

| Sender Role / Receiver Role       | Management | Commercial Role | Purchasing Role | Logistics Role | Quality Role | Document Mgmt Role |
|--------------------------------------|-----------|-----------------|-------------|-----------------|--------------|---------------------|
| **Management**                       | -         | Strategic directions | Purchasing budgets | Logistics objectives | Quality policy | Document requirements |
| **Commercial Role**                  | Sales reports | - | Customer specifications | Shipping needs | Customer quality requirements | Document requests |
| **Purchasing Role**                  | Purchasing reporting | Supplier confirmations | - | Supplier information | Qualification files | Supplier records |
| **Logistics Role**                   | Logistics reporting | Shipping confirmations | Transport coordination | - | Transport documents | Customs documents |
| **Quality Role**                     | Quality indicators | Inspection reports | Supplier evaluations | Shipment authorization | - | Reports and records |
| **Document Mgmt Role**              | Document dashboard | Applicable documents | Applicable documents | Applicable documents | Applicable documents | - |

---

## 3.4 Information and Decision Flow

### 3.4.1 Upward Flow (to Management)

| Source             | Type of Information                       | Frequency         |
|--------------------|-------------------------------------------|-------------------|
| Commercial Role    | Revenue, customer satisfaction             | Monthly           |
| Purchasing Role    | Supplier performance, purchasing costs     | Monthly           |
| Logistics Role     | On-time delivery rate, incidents           | Monthly           |
| Quality Role       | NC rate, inspection results, KPIs          | Monthly           |
| Document Mgmt Role | Documentation status, document audits      | Quarterly         |

### 3.4.2 Downward Flow (from Management)

| Recipient          | Type of Information                        | Frequency         |
|--------------------|--------------------------------------------|-------------------|
| All roles          | Quality policy, strategic objectives        | Annual            |
| All roles          | Management review results                   | Semi-annual       |
| Relevant role      | Resource allocation decisions               | As needed         |
| Relevant role      | Strategic corrective actions                | As needed         |

### 3.4.3 Cross-functional Flow (between operational roles)

| Sender             | Receiver           | Information                              | Trigger               |
|--------------------|--------------------|------------------------------------------|-----------------------|
| Commercial Role    | Purchasing Role    | Validated new order                      | Order acceptance      |
| Purchasing Role    | Quality Role       | Supplier order placed                    | Order confirmation    |
| Quality Role       | Logistics Role     | Product release authorization            | Successful inspection |
| Quality Role       | Purchasing Role    | Supplier nonconformity                   | NC detection          |
| Logistics Role     | Commercial Role    | Shipping confirmation                    | Goods departure       |

---

## 3.5 Authority Matrix

| Decision                                      | Management | Commercial Role | Purchasing Role | Quality Role | Logistics Role | Document Mgmt Role |
|-----------------------------------------------|-----------|-----------------|-------------|--------------|-----------------|---------------------|
| Quality policy approval                        | A         | I               | I           | C            | I               | I                   |
| Customer order acceptance                      | I         | A               | C           | C            | C               | -                   |
| New supplier selection                         | I         | I               | A           | C            | -               | -                   |
| Supplier suspension                            | C         | I               | A           | R            | -               | -                   |
| Product lot release                            | -         | I               | I           | A            | I               | -                   |
| Nonconformity hold                             | I         | I               | I           | A            | I               | -                   |
| QMS document validation                        | A         | -               | -           | C            | -               | R                   |
| Corrective action initiation                   | I         | -               | -           | A            | -               | I                   |
| Resource allocation                            | A         | -               | -           | C            | -               | -                   |

**Legend**: A = Approves / R = Responsible / C = Consulted / I = Informed

---

## 3.6 Competencies by Role

The detailed competency matrix is documented in process PS02 - Competence Management (FM-PS02-MCO). The table below presents the key competency areas required by role.

| Role                     | Key Competency Areas                                                  |
|--------------------------|-----------------------------------------------------------------------|
| Management               | Strategic management, financial management, leadership, ISO standards |
| Commercial Role          | Commercial negotiation, customer relations, foreign languages, international trade |
| Purchasing Role          | International sourcing, supplier negotiation, product knowledge, supplier evaluation |
| Logistics Role           | International logistics, customs regulations, Incoterms, transport management |
| Quality Role             | ISO 9001 quality standards, inspection techniques, metrology, audit, NC management |
| Document Management Role | Document management, digital tools, archiving, records control        |

---

## Normative References

| ISO 9001:2015 Clause | Requirement                                                 |
|-----------------------|---------------------------------------------------------|
| 5.3                   | Roles, responsibilities and authorities within the organization |
| 7.1.2                 | People                                                       |
| 7.2                   | Competence                                                   |
| 7.4                   | Communication                                                |
| 4.4.1                 | The organization shall establish the necessary processes     |

---

*Controlled document - Any printed copy is considered uncontrolled.*
*Plus Sarl - Quality Management System ISO 9001:2015 - v0.7*