# IT-P03-PSI — Pre-Shipment Inspection (PSI)

| **Document**         | Work Instruction — PSI Inspection                    |
|----------------------|------------------------------------------------------|
| **Code**            | IT-P03-PSI                                            |
| **Process**         | P03 - Quality Control                                 |
| **Version**         | v0.7                                                  |
| **Date**            | 2026-03-08                                            |
| **ISO 9001 Standard** | Clauses 8.6, 8.7                                   |

---

## 1. Purpose

This work instruction describes the procedure for conducting a **Pre-Shipment Inspection (PSI)** at the supplier's facility once production is 100% complete and goods are packed and ready for shipment. The PSI is the final quality gate before release for shipment.

---

## 2. Scope

This instruction applies to all orders requiring a PSI as defined in the inspection plan (A1 of process P03). PSI is mandatory for all orders unless explicitly waived by Management.

---

## 3. Sampling Plan

The PSI uses statistical sampling per **ISO 2859-1 (AQL)** as defined in instruction IT-P03-ECH.

| Order Quantity       | Inspection Level | AQL (Major) | AQL (Minor) |
|----------------------|------------------|-------------|-------------|
| 2 - 150              | General Level II | 2.5         | 4.0         |
| 151 - 1200           | General Level II | 2.5         | 4.0         |
| 1201 - 10000         | General Level II | 2.5         | 4.0         |
| > 10000              | General Level II | 1.5         | 2.5         |

> **Note**: Tightened inspection may be applied for suppliers under enhanced surveillance or after a previous PSI failure.

---

## 4. Preparation

| Step | Action                                   | Responsible   | Documents                     |
|------|------------------------------------------|---------------|-------------------------------|
| 1    | Confirm production is 100% complete      | Quality Role  | Supplier confirmation         |
| 2    | Review previous IPC/DUPRO results        | Quality Role  | FM-P03-IPC / FM-P03-DUPRO     |
| 3    | Prepare PSI checklist per specifications | Quality Role  | FM-P03-PSI template           |
| 4    | Determine sample size per AQL table      | Quality Role  | IT-P03-ECH                    |
| 5    | Prepare measurement tools               | Quality Role  | Calibration certificates      |
| 6    | Confirm inspection date with supplier    | Quality Role  | Communication record          |

---

## 5. Inspection Procedure

### 5.1 Quantity Verification

| Check Point                          | Method                                               | Acceptance Criteria              |
|--------------------------------------|------------------------------------------------------|----------------------------------|
| Total quantity produced              | Count / packing list                                 | Match with purchase order        |
| Carton / pallet count                | Physical count                                       | Match with packing list          |
| Pieces per carton                    | Random check (minimum 5 cartons)                     | Consistent with packing list     |

### 5.2 Visual Inspection (on sample)

| Check Point                          | Method                                               | Acceptance Criteria              |
|--------------------------------------|------------------------------------------------------|----------------------------------|
| General appearance                   | Visual comparison with approved sample               | No visible defects               |
| Surface finish                       | Visual inspection                                    | Per specification                |
| Color consistency                    | Visual comparison                                    | Match with reference             |
| Marking / branding                   | Visual verification                                  | Correct and legible              |

### 5.3 Dimensional Inspection (on sample)

| Check Point                          | Method                                               | Acceptance Criteria              |
|--------------------------------------|------------------------------------------------------|----------------------------------|
| Critical dimensions                  | Caliper / micrometer / gauge                         | Within drawing tolerances        |
| Assembly fit (if applicable)         | Trial assembly                                       | Proper fit                       |
| Weight (if specified)                | Weighing                                             | Within tolerance                 |

### 5.4 Functional Tests (on sample, if applicable)

| Check Point                          | Method                                               | Acceptance Criteria              |
|--------------------------------------|------------------------------------------------------|----------------------------------|
| Functional performance               | Per test protocol                                    | Meet specification               |
| Safety requirements                  | Per applicable standard                              | Compliant                        |
| Durability / stress test             | Per specification (if required)                      | Pass                             |

### 5.5 Packaging and Labeling

| Check Point                          | Method                                               | Acceptance Criteria              |
|--------------------------------------|------------------------------------------------------|----------------------------------|
| Inner packaging                      | Visual inspection                                    | Adequate product protection      |
| Outer carton quality                 | Visual + drop test indication                        | Sturdy, undamaged                |
| Labeling (shipping marks)            | Visual verification                                  | Correct, legible, per spec       |
| Barcode / QR code (if applicable)    | Scanner test                                         | Readable and correct             |
| Shipping documents                   | Document review                                      | Complete and accurate            |

---

## 6. Decision

| Result          | Action                                               |
|-----------------|------------------------------------------------------|
| **PASS**        | Product released for shipment. FM-P03-PSI signed and sent to Logistics (P04). |
| **PENDING**     | Minor defects found within AQL limits. Sorting or rework required. Re-inspection scheduled. |
| **FAIL**        | Major or critical defects exceed AQL. Lot rejected. NC report opened (FM-P03-NC). Shipment blocked. |

---

## 7. Reporting

| Action                               | Timeline    | Responsible   |
|--------------------------------------|-------------|---------------|
| Complete FM-P03-PSI report           | Same day    | Quality Role  |
| Send PASS result to Logistics Role   | Same day    | Quality Role  |
| Send report to supplier              | 24 hours    | Quality Role  |
| Send report to Purchasing Role       | 24 hours    | Quality Role  |
| Inform Commercial Role of result     | 24 hours    | Quality Role  |
| Open NC if applicable                | 24 hours    | Quality Role  |
| Archive report                       | 48 hours    | Document Management Role |

---

## 8. Associated Documents

| Code         | Title                                 |
|--------------|---------------------------------------|
| FM-P03-PSI   | PSI Report Form                       |
| FM-P03-NC    | Non-Conformity Report                 |
| IT-P03-ECH   | AQL Sampling Instruction              |
| PR-P03-CQ    | Quality Control Procedure             |

---

*Controlled document - Plus Sàrl - ISO 9001:2015 Quality Management System*
*Version v0.7 - 2026-03-08*
