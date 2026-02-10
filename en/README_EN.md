# ISO 9001:2015 Certification Project - DUMMY Sarl

## Objective

This repository contains all the documents required to implement a Quality Management System (QMS) compliant with ISO 9001:2015 for **DUMMY Sarl**.

## Company Profile

| Item | Detail |
|---|---|
| Company name | DUMMY Sarl |
| Country | Switzerland |
| Headcount | 1 employee (managing director) |
| Shareholders | 3 (including the managing director) |
| Premises | 1 office |
| Activity | Development of molds for plastic injection and delivery |
| Manufacturing | Outsourced in China (partner) |
| Customers | Swiss and European (B2B) |
| Motivation | Customer requirement for supplier certification |

## Repository Structure

```
ISO/
|-- README.md                              # This file (French)
|-- GUIDE_CERTIFICATION.md                 # Step-by-step guide (French)
|-- PLANNING.md                            # Detailed 12-month planning (French)
|
|-- en/                                    # ENGLISH VERSION
|   |-- README_EN.md                       # This file (English)
|   |-- CERTIFICATION_GUIDE.md             # Step-by-step guide (English)
|   |-- PLANNING.md                        # Detailed 12-month planning (English)
|   |
|   |-- templates/
|       |-- 01_Mandatory_Documents/
|       |   |-- POL-QUA-001_Quality_Policy.md
|       |   |-- SCP-QUA-001_Scope.md
|       |   |-- CTX-QUA-001_Organization_Context.md
|       |   |-- MAP-QUA-001_Process_Map.md
|       |   |-- OBJ-QUA-001_Quality_Objectives.md
|       |   |-- SHT-PRO-001_Process_Sheet_Template.md
|       |
|       |-- 02_Procedures/
|       |   |-- PRO-DOC-001_Document_Control.md
|       |   |-- PRO-AUD-001_Internal_Audit.md
|       |   |-- PRO-NCR-001_Nonconformities.md
|       |   |-- PRO-CAR-001_Corrective_Actions.md
|       |   |-- PRO-PUR-001_Purchasing_Subcontracting.md
|       |
|       |-- 03_Forms_Records/
|       |   |-- FOR-SUE-001_Supplier_Evaluation.md
|       |   |-- FOR-CSA-001_Customer_Satisfaction.md
|       |   |-- FOR-MRV-001_Management_Review.md
|       |   |-- FOR-CMP-001_Competence_Training.md
|       |   |-- FOR-CCM-001_Customer_Complaints.md
|       |   |-- FOR-INC-001_Incoming_Inspection.md
|       |
|       |-- 04_Checklists/
|           |-- CHK-AUD-001_Internal_Audit_Checklist.md
|
|-- modeles/                               # FRENCH VERSION
    |-- 01_Documents_Obligatoires/
    |-- 02_Procedures/
    |-- 03_Formulaires_Registres/
    |-- 04_Checklists/
```

## How to Use This Repository

1. **Read the guide**: Start with `CERTIFICATION_GUIDE.md` (or `GUIDE_CERTIFICATION.md` for French)
2. **Follow the planning**: Respect the steps in `PLANNING.md`
3. **Fill in the templates**: Complete each document in `templates/` (or `modeles/`)
4. **Replace `[...]`**: Each field in brackets must be customized
5. **Keep versions**: Use git to track changes

## Document Coding

| Prefix | Document Type |
|---|---|
| POL | Policy |
| SCP | Scope |
| CTX | Context |
| MAP | Map |
| OBJ | Objectives |
| SHT | Sheet |
| PRO | Procedure |
| FOR | Form |
| CHK | Checklist |
