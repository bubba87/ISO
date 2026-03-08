# P04 - Logistics and Delivery Process

| **Process**         | P04 - Logistics and Delivery                         |
|----------------------|------------------------------------------------------|
| **Type**            | Core                                                  |
| **Owner**           | Logistics Role                                        |
| **Version**         | v0.7                                                  |
| **Date**            | 2026-03-04                                            |
| **Reference**       | PR-P04-LOG                                            |
| **ISO 9001 Standard** | Clauses 8.5.4, 8.6                                 |

---

## 1. Purpose and Scope

This process describes the logistics activities of **Plus Sàrl** covering shipment planning, international transport coordination, delivery tracking, and receipt confirmation. It applies to all logistics flows related to worldwide industrial follow-up and sourcing operations.

---

## 2. Normative References

- ISO 9001:2015, Clauses 8.5.4 (Preservation), 8.6 (Release of Products and Services)
- Plus Sàrl Quality Manual (MQ-001)
- Applicable international customs and transport regulations

---

## 3. Roles and Responsibilities

| Role                        | Key Responsibilities                                                 |
|-----------------------------|----------------------------------------------------------------------|
| **Logistics**               | Planning, transport coordination, tracking, documentation            |
| **Purchasing**              | Transmission of supplier information, Incoterms conditions           |
| **Commercial**              | Customer communication on timelines and tracking                     |
| **Quality**                 | Release of goods after inspection                                    |
| **Freight Forwarder / Carrier** | Transport execution, customs clearance                           |

---

## 4. Input and Output Data

### Input Data
- Validated and confirmed purchase order (P01/P02)
- Quality release confirmation (P04)
- Supplier information (address, contact, conditions)
- Customer requirements (deadline, location, Incoterms)
- Applicable customs regulations

### Output Data
- Shipment plan
- Transport documents (BL, AWB, CMR, packing list)
- Customs declarations
- Proof of delivery (POD)
- Customer receipt confirmation

---

## 5. Activity Description

### A1 - Shipment Planning

The Logistics Role receives validated order information and plans the shipment: mode of transport (sea, air, road, rail), timelines, volumes, special packaging, and handling requirements.

### A2 - Freight Forwarder / Carrier Selection

The Logistics Role selects the appropriate freight forwarder or carrier from qualified service providers, considering cost, timelines, reliability, and destination.

### A3 - Documentation Preparation

The Logistics Role prepares or coordinates the preparation of required documents: commercial invoice, packing list, certificate of origin, customs documents, bill of lading (BL), or air waybill (AWB).

### A4 - Pickup and Loading Coordination

The Logistics Role coordinates the pickup of goods from the supplier, ensures proper execution of the Loading Check (P04) where applicable, and confirms loading.

### A5 - In-Transit Monitoring

The Logistics Role provides real-time transport monitoring, manages contingencies (delays, damage, customs holds), and proactively communicates updates to the Commercial Role for customer information.

### A6 - Customs Clearance and Final Delivery

The Logistics Role coordinates customs clearance operations at destination, organizes final delivery to the customer, and ensures compliance with agreed conditions.

### A7 - Delivery Confirmation and Closure

The Logistics Role obtains the proof of delivery (POD), confirms successful receipt to the Commercial Role and the customer, archives documents, and closes the logistics file.

---

## 6. Swimlane Diagram

```
 PROCESS P04 - LOGISTICS AND DELIVERY
 ============================================================================

 Role                 | Activity Flow
 ============================================================================
                      |
 LOGISTICS            |  [A1 Plan]         [A2 Select]          [A3 Prepare]
                      |  the shipment ---> freight forwarder --> documentation
                      |  (mode, timeline,  / carrier             (BL, AWB,
                      |   volumes)         qualified              packing list)
                      |                                              |
                      |                                              v
                      |                                    [A4 Coordinate]
                      |                                    pickup and
                      |                                    loading
                      |                                         |
                      |                                         v
                      |                                    [A5 Monitor]
                      |                                    in-transit
                      |                                    transport
                      |                                         |
                      |                                         v
                      |                                    [A6 Clear customs]
                      |                                    and deliver
                      |                                         |
                      |                                         v
                      |                                    [A7 Confirm]
                      |                                    delivery and
                      |                                    close (POD)
                      |
 ============================================================================
                      |
 PURCHASING           |  Transmit       ---> Provide          Report
                      |  supplier            Incoterms        supplier
                      |  information         conditions       contingencies
                      |
 ============================================================================
                      |
 COMMERCIAL           |  Communicate   ---> Inform the   ---> Confirm
                      |  customer           customer on       successful
                      |  requirements       transport         receipt to
                      |  (timeline,         tracking          the customer
                      |  destination)
                      |
 ============================================================================
                      |
 QUALITY              |  Release goods after inspection (P04)
                      |  Validate Loading Check before loading
                      |
 ============================================================================
                      |
 FREIGHT FORWARDER /  |  Execute the  ---> Handle        ---> Deliver to
 CARRIER              |  transport         customs            final
                      |                    clearance          recipient
                      |
 ============================================================================
```

---

## 7. Interactions with Other Processes

| Process                | Nature of Interaction                                  |
|------------------------|--------------------------------------------------------|
| PM01 - Leadership      | Logistics performance reporting, transport budgets     |
| P01 - Commercial       | Customer requirements, tracking communication, confirmation |
| P02 - Purchasing       | Supplier information, pickup conditions                |
| P03 - Quality Control  | Loading Check, goods release                           |
| PS01 - Document Management | Archiving of transport documents                    |

---

## 8. Key Performance Indicators (KPI)

| Indicator                                 | Formula / Method                                   | Target         | Frequency    |
|-------------------------------------------|---------------------------------------------------|----------------|--------------|
| On-time delivery rate                     | On-time deliveries / Total deliveries x 100        | >= 95%         | Monthly      |
| Transport damage rate                     | Deliveries with damage / Total deliveries x 100    | < 1%           | Monthly      |
| Average transit time                      | Sum of transit times / Number of shipments          | Per destination | Monthly     |
| Documentation completeness rate           | Complete files / Total files x 100                 | 100%           | Monthly      |
| Average logistics cost per shipment       | Total logistics costs / Number of shipments        | Downward trend | Quarterly    |
| Transport-related complaint rate          | Transport complaints / Total deliveries x 100      | < 2%           | Monthly      |

---

## 9. Associated Documents and Records

| Code         | Title                                 | Type          |
|--------------|---------------------------------------|---------------|
| PR-P04-LOG   | Logistics and Delivery Procedure      | Procedure     |
| FM-P04-EXP   | Shipment Form                         | Form          |
| FM-P04-SUI   | Shipment Tracking Table               | Form          |
| EN-P04-POD   | Proofs of Delivery                    | Record        |
| EN-P04-DOC   | Transport Documentation Files         | Record        |

---

## 10. Continual Improvement

Improvement of the logistics process is based on:
- Analysis of delays and their root causes
- Optimization of routes and transport modes
- Regular evaluation of freight forwarders and carriers
- Digitalization of shipment tracking
- Lessons learned from transport incidents

---

*Controlled document - Plus Sàrl - ISO 9001:2015 Quality Management System*
*Version v0.7 - 2026-03-04*
