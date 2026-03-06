# P04 - Logistics and Delivery Process

| **Process**         | P04 - Logistics and Delivery                         |
|----------------------|------------------------------------------------------|
| **Type**            | Operational                                           |
| **Owner**           | Logistics Role                                        |
| **Version**         | v0.7                                                  |
| **Date**            | 2026-03-04                                            |
| **Reference**       | PR-P04-LOG                                            |
| **ISO 9001 Standard** | Clauses 8.5.4, 8.6                                 |

---

## 1. Purpose and scope

This process describes the logistics activities of **Plus Sarl** covering shipment planning, international transport coordination, delivery tracking and confirmation of receipt. It applies to all logistics flows related to worldwide industrial monitoring and sourcing operations.

---

## 2. Normative references

- ISO 9001:2015, Clauses 8.5.4 (Preservation), 8.6 (Release of products and services)
- Plus Sarl Quality Manual (MQ-001)
- Applicable international customs and transport regulations

---

## 3. Roles and responsibilities

| Role                        | Key responsibilities                                                 |
|-----------------------------|----------------------------------------------------------------------|
| **Logistics**               | Planning, transport coordination, tracking, documentation            |
| **Purchasing**              | Transmission of supplier information, Incoterms conditions           |
| **Sales**                   | Customer communication on lead times and tracking                    |
| **Quality**                 | Release of goods after inspection                                    |
| **Freight forwarder / Carrier** | Transport execution, customs clearance                           |

---

## 4. Input and output data

### Input data
- Validated and confirmed purchase order (P01/P02)
- Quality release confirmation (P04)
- Supplier information (address, contact, conditions)
- Customer requirements (lead time, destination, Incoterms)
- Applicable customs regulations

### Output data
- Shipment plan
- Transport documents (BL, AWB, CMR, packing list)
- Customs declarations
- Proof of delivery (POD)
- Customer receipt confirmation

---

## 5. Description of activities

### A1 - Shipment planning

The Logistics Role receives the validated order information and plans the shipment: transport mode (sea, air, road, rail), lead times, volumes, special packaging and handling requirements.

### A2 - Selection of freight forwarder / carrier

The Logistics Role selects the appropriate freight forwarder or carrier from qualified service providers, taking into account cost, lead times, reliability and destination.

### A3 - Documentation preparation

The Logistics Role prepares or coordinates the preparation of the necessary documents: commercial invoice, packing list, certificate of origin, customs documents, bill of lading (BL) or air waybill (AWB).

### A4 - Coordination of collection and loading

The Logistics Role coordinates the collection of goods from the supplier, ensures proper execution of the Loading Check (P04) where applicable, and confirms loading.

### A5 - In-transit transport tracking

The Logistics Role provides real-time transport tracking, manages contingencies (delays, damage, customs holds) and proactively communicates updates to the Sales Role for customer information.

### A6 - Customs clearance and final delivery

The Logistics Role coordinates customs clearance operations at destination, organises final delivery to the customer and ensures compliance with agreed conditions.

### A7 - Delivery confirmation and closure

The Logistics Role obtains the proof of delivery (POD), confirms receipt to the Sales Role and the customer, archives documents and closes the logistics file.

---

## 6. Swimlane diagram

```
 PROCESS P04 - LOGISTICS AND DELIVERY
 ============================================================================

 Role                 | Activity flow
 ============================================================================
                      |
 LOGISTICS            |  [A1 Plan]         [A2 Select]        [A3 Prepare]
                      |  the shipment ---> freight forwarder/  documentation
                      |  (mode, lead       carrier         --> (BL, AWB,
                      |   time, volumes)   qualified            packing list)
                      |                                              |
                      |                                              v
                      |                                    [A4 Coordinate]
                      |                                    collection and
                      |                                    loading
                      |                                         |
                      |                                         v
                      |                                    [A5 Track]
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
 PURCHASING           |  Transmit       --> Provide          Report
                      |  supplier           Incoterms        supplier
                      |  information        conditions       contingencies
                      |
 ============================================================================
                      |
 SALES                |  Communicate   --> Inform the   --> Confirm
                      |  customer          customer on      receipt to
                      |  requirements      transport        the customer
                      |  (lead time,       tracking
                      |  destination)
                      |
 ============================================================================
                      |
 QUALITY              |  Release goods after inspection (P04)
                      |  Validate Loading Check before loading
                      |
 ============================================================================
                      |
 FREIGHT FORWARDER /  |  Execute the  --> Handle        --> Deliver to
 CARRIER              |  transport        customs           final
                      |                   clearance         consignee
                      |
 ============================================================================
```

---

## 7. Interactions with other processes

| Process                | Nature of interaction                                  |
|------------------------|--------------------------------------------------------|
| PM01 - Leadership        | Logistics performance reporting, transport budgets    |
| P01 - Sales            | Customer requirements, tracking communication, confirmation |
| P02 - Purchasing       | Supplier information, collection conditions            |
| P03 - Quality Control  | Loading Check, release of goods                        |
| PS01 - Document Management | Archiving of transport documents                     |

---

## 8. Key Performance Indicators (KPI)

| Indicator                                 | Formula / Method                                  | Target         | Frequency    |
|-------------------------------------------|--------------------------------------------------|----------------|--------------|
| On-time delivery rate                     | On-time deliveries / Total deliveries x 100      | >= 95 %        | Monthly      |
| Transport damage rate                     | Deliveries with damage / Total deliveries x 100  | < 1 %          | Monthly      |
| Average transit time                      | Sum of transit times / Number of shipments       | Per destination | Monthly     |
| Documentation completeness rate           | Complete files / Total files x 100               | 100 %          | Monthly      |
| Average logistics cost per shipment       | Total logistics costs / Number of shipments      | Downward trend | Quarterly    |
| Transport-related complaint rate          | Transport complaints / Total deliveries x 100    | < 2 %          | Monthly      |

---

## 9. Associated documents and records

| Code         | Title                                 | Type          |
|--------------|---------------------------------------|---------------|
| PR-P04-LOG   | Logistics and Delivery Procedure      | Procedure     |
| FM-P04-EXP   | Shipment Form                         | Form          |
| FM-P04-SUI   | Shipment Tracking Table               | Form          |
| EN-P04-POD   | Proofs of Delivery                    | Record        |
| EN-P04-DOC   | Transport Documentation Files         | Record        |

---

## 10. Continual improvement

Improvement of the logistics process is based on:
- Analysis of delays and their root causes
- Optimisation of routes and transport modes
- Regular evaluation of freight forwarders and carriers
- Digitalisation of shipment tracking
- Feedback on transport incidents

---

*Controlled document - Plus Sarl - ISO 9001:2015 Quality Management System*
*Version v0.7 - 2026-03-04*
