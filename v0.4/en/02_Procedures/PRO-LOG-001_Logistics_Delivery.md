# Logistics and Delivery Procedure

| | |
|---|---|
| **Reference** | PRO-LOG-001 |
| **Version** | 0.4 |
| **Date de creation** | 18/02/2026 |
| **Date de revision** | 18/02/2026 |
| **Redige par** | Roxane Wicky |
| **Approuve par** | Roxane Wicky |

> **Legend:** :red_circle: [TO BE COMPLETED] = mandatory, missing | :yellow_circle: [RECOMMENDED] = recommended | :green_circle: = already completed | :blue_circle: [TO BE VERIFIED] = to be confirmed

---

## 1. Objet

Define the organizational rules, monitoring, and control of international logistics and deliveries, from the notification of ready products by the Chinese partner to the confirmation of receipt by the European customer, including the creation of customs documents compliant with European and Swiss legislation.

> **This procedure is essential for Plus Sarl.** Logistics coordination between China and Europe
> constitutes a critical link in the value chain. Control of lead times, transport, and
> customs formalities directly impacts customer satisfaction and will be examined by the
> certification auditor (SQS).

## 2. Domaine d'application

All product shipments from China to Plus Sarl's European customers (~10 active customers, 50-100 shipments per year):
- Shipments of injection molded plastic parts (from Yuyao Mould Factory)
- Shipments of screws (from Whang, Yuyao)
- Combined or multi-reference shipments
- All transport modes: air, sea, rail
- Management of associated customs documents

## 3. Responsabilites

| Responsabilite | Qui |
|---|---|
| Creation of the delivery record in FileMaker | :green_circle: Roxane Wicky, Managing Director |
| Choice of transport mode | :green_circle: Roxane Wicky, Managing Director |
| Selection and contact of the carrier | :green_circle: Roxane Wicky, Managing Director |
| Preparation of customs documents | :green_circle: Roxane Wicky, Managing Director |
| Shipment tracking and monitoring | :green_circle: Roxane Wicky, Managing Director |
| Management of customs formalities (EU and CH) | :green_circle: Roxane Wicky, Managing Director |
| Confirmation of delivery to the customer | :green_circle: Roxane Wicky, Managing Director |
| Closure of the delivery record in FileMaker | :green_circle: Roxane Wicky, Managing Director |

## 4. Modes de transport

The choice of transport mode is determined by the urgency of delivery and the volume of goods:

| Mode | Usage | Delai indicatif Chine-Europe | Tolerance | Criteres de choix |
|---|---|---|---|---|
| **Aerien** | Urgent, small volumes | :green_circle: 5-10 days | :green_circle: +/- 3 days | Customer urgency, samples, small series |
| **Maritime** | Standard, large volumes | :green_circle: 30-45 days | :green_circle: +/- 10 days | Large volumes, optimized cost, non-critical lead time |
| **Ferroviaire** | Intermediate | :green_circle: 15-25 days | :green_circle: +/- 7 days | Compromise between lead time and cost, medium volumes |

> **Note:** The transport mode is chosen case by case based on customer requirements
> (lead time, cost) and order volume. Sea transport is preferred when lead time
> allows it in order to optimize costs.

### 4.1 Transporteurs et transitaires

| Element | Detail |
|---|---|
| **Modes disponibles** | :green_circle: Air, sea, rail |
| **Criteres de selection** | :green_circle: Reliability, respect of deadlines, geographical coverage, cost |
| **Noms des transporteurs** | :yellow_circle: [RECOMMENDED -- it is recommended to document the names of carriers and freight forwarders used to ensure traceability and evaluation] |

## 5. Procedure de livraison

### 5.1 Logigramme

```
    Notification produits prets
    (depuis processus O2)
            |
            v
    +---------------------------+
    | 1. Recevoir la            |---> The Chinese partner notifies
    |    notification produits  |     that products are ready
    |    prets                  |     for shipment (email/WeChat)
    +---------------------------+
            |
            v
    +---------------------------+
    | 2. Creer la fiche         |---> Recording in FileMaker:
    |    livraison dans         |     references, quantities, customer,
    |    FileMaker              |     desired lead time
    +---------------------------+
            |
            v
    +---------------------------+
    | 3. Choisir le mode de     |---> Air / Sea / Rail
    |    transport              |     according to urgency, volume and
    |                           |     customer requirements
    +---------------------------+
            |
            v
    +---------------------------+
    | 4. Selectionner et        |---> Contact carrier/freight forwarder
    |    contacter le           |     Request quote if necessary
    |    transporteur           |     Confirmation of booking
    +---------------------------+
            |
            v
    +---------------------------+
    | 5. Preparer les documents |---> Customs invoice
    |    douaniers              |     Certificate of origin
    |                           |     Packing list
    |                           |     Other required documents
    +---------------------------+
            |
            v
    +---------------------------+
    | 6. Verifier la conformite |---> Compliance with European (EU)
    |    des documents          |     and Swiss (CH) legislation
    |    douaniers              |     Consistency with customer order
    +---------------------------+
            |
            v
    +---------------------------+
    | 7. Lancer l'expedition    |---> Handover of goods and
    |                           |     documents to carrier
    +---------------------------+
            |
            v
    +---------------------------+
    | 8. Suivre l'expedition    |---> Online tracking
    |                           |     Contact carrier if needed
    |                           |     Update FileMaker
    +---------------------------+
            |
            v
    +---------------------------+
    | 9. Gerer le dedouanement  |---> Monitoring of import customs
    |                           |     formalities (EU/CH)
    |                           |     Resolution of blockages
    +---------------------------+
            |
            v
    +---------------------------+
    | 10. Confirmer la          |---> Contact customer for confirmation
    |     livraison au client   |     of proper receipt
    +---------------------------+
            |
            v
       Probleme signale ?
       /                \
     NON                OUI
      |                   |
      v                   v
    +---------------------------+
    | 11. Cloturer la fiche     |   PRO-NCF-001
    |     dans FileMaker        |   (non-conformite)
    +---------------------------+
```

### 5.2 Detail des etapes

| # | Etape | Description | Outil | Sortie |
|---|---|---|---|---|
| 1 | Receipt of ready products notification | The Chinese partner informs that products are ready for shipment after pre-shipment QC (see PRO-ACH-001, section 8) | Email / WeChat | Notification received |
| 2 | Creation of delivery record | Recording of all delivery information in FileMaker (references, quantities, customer, lead time) | FileMaker | Delivery record created |
| 3 | Choice of transport mode | Selection of transport mode (air, sea, rail) based on urgency, volume and customer requirements | -- | Transport mode defined |
| 4 | Carrier selection | Contact with carrier or freight forwarder, quote request if necessary, booking confirmation | Email | Booking confirmed |
| 5 | Preparation of customs documents | Creation of customs invoice, certificate of origin, packing list and any other required documents | FileMaker / Email | Customs documents ready |
| 6 | Verification of document compliance | Verification of document consistency with customer order and EU and CH customs legislation | -- | Documents validated |
| 7 | Launch of shipment | Handover of goods and documents to carrier | -- | Shipment launched |
| 8 | Shipment tracking | Transport monitoring via online tracking, carrier contact if necessary, status update in FileMaker | FileMaker / Email | Status up to date |
| 9 | Customs clearance management | Monitoring of import customs formalities, resolution of any blockages | Email | Customs clearance completed |
| 10 | Customer delivery confirmation | Contact with customer to confirm proper receipt of goods | Email | Confirmation received |
| 11 | Closure in FileMaker | Closure of delivery record, archiving of associated documents | FileMaker | Record closed |

## 6. Documents douaniers

The following documents are required for each shipment:

| Document | Description | Obligatoire | Responsable |
|---|---|---|---|
| **Facture douaniere** | Commercial invoice detailing goods, quantities, values, incoterms | Yes | :green_circle: Roxane Wicky |
| **Certificat d'origine** | Document certifying the origin of goods (China) | Yes | :green_circle: Roxane Wicky / Chinese partner |
| **Packing list** | Packing list detailing the content of each package (weight, dimensions, references) | Yes | :green_circle: Roxane Wicky / Chinese partner |
| **Bon de livraison** | Document accompanying goods for the customer | Yes | :green_circle: Roxane Wicky |
| **Documents de transport** | AWB (air), B/L (sea), CIM/SMGS (rail) | Yes | :green_circle: Carrier |
| **Declaration en douane** | Import declaration for Switzerland or the EU | Yes | :green_circle: Freight forwarder / Roxane Wicky |
| **Certificats specifiques** | Certificates of conformity, test reports, if required by customer or regulation | Depending on order | :blue_circle: [TO BE VERIFIED -- case by case according to customer and regulatory requirements] |

> **Note:** Customs documents must comply with both European legislation
> (for direct deliveries to EU customers) and Swiss legislation (for shipments
> transiting through Switzerland). Consistency between customs documents and customer orders
> is systematically verified before each shipment.

## 7. Indicateurs de performance

| Indicateur | Objectif | Statut | Methode de mesure |
|---|---|---|---|
| Rate of on-time deliveries | >= 95% | :green_circle: | Comparison of announced lead time vs. actual lead time in FileMaker |
| Respect of sea/rail transport tolerance | +/- 10 days | :green_circle: | Tracking of deviations in FileMaker |
| Respect of air transport tolerance | +/- 3 days | :green_circle: | Tracking of deviations in FileMaker |
| Rate of customs document errors | < 5% | :green_circle: | Number of rejections or corrections relative to total number of shipments |
| Customer complaints related to delivery | 0 major complaints per year | :green_circle: | Tracking of complaints in FileMaker |

> **Review frequency:** Indicators are reviewed during the annual management review
> and continuously by the Managing Director as part of daily operational monitoring.

## 8. Risques et actions

| Risque | Impact | Probabilite | Action preventive | Action corrective |
|---|---|---|---|---|
| Transport delay (weather, port congestion, logistical disruptions) | Late delivery to customer | Medium | Integrate safety margins in lead times announced to customer; diversify transport modes | Inform customer immediately; seek alternative solution (change of transport mode) |
| Customs blockage (incomplete or non-compliant documents) | Delivery delay, additional costs | Low | Systematically verify document compliance before shipment (step 6); stay informed of regulatory changes | Correct documents and resubmit; contact freight forwarder to resolve the situation |
| Loss or damage of goods during transport | Financial loss, customer dissatisfaction | Low | Select reliable carriers; verify packaging before shipment | Declare incident to carrier; arrange replacement if possible; record NC (PRO-NCF-001) |
| Error in customs documents (amounts, references, quantities) | Customs blockage, penalties | Low | Double verification of documents before sending (step 6) | Correct immediately; inform freight forwarder and customer |
| Change in customs regulations (EU or CH) | Non-compliance of documents | Low | Regulatory monitoring; regular contact with freight forwarder | Adapt documents and processes; provide training if necessary |

## 9. Interfaces avec les autres processus

| Processus | Interface | Description |
|---|---|---|
| **O1 -- Relation client** | Input / Output | Receipt of customer requirements (lead times, address, incoterms); delivery confirmation to customer; handling of delivery-related complaints |
| **O2 -- Production et suivi de fabrication** | Input | Receipt of notification of products ready for shipment after pre-shipment QC |
| **O4 -- Facturation** | Output | Transmission of delivery information for invoicing (references, quantities, delivery date) |
| **S1 -- Maitrise documentaire** | Support | Archiving of customs documents, delivery records and tracking evidence in accordance with PRO-DOC-001 |
| **PRO-ACH-001** | Link | Carriers and freight forwarders are Class B suppliers evaluated according to PRO-ACH-001 |
| **PRO-NCF-001** | Link | In case of delivery problem (major delay, loss, damage), a non-conformity is recorded according to PRO-NCF-001 |

---

> **Instructions de remplissage :**
> 1. Record ALL shipments in FileMaker with references, lead times, transport mode and status
> 2. Keep ALL customs documents (invoices, certificates of origin, packing lists) -- these are proof of process control
> 3. Keep proof of transport tracking (tracking, carrier emails) -- the auditor (SQS) will want to see them
> 4. In case of significant delay, inform the customer immediately and document the incident
> 5. Systematically verify consistency between customs documents and customer orders before each shipment
> 6. Lead time tolerances (+/- 3 days air, +/- 10 days sea) must be communicated to customers when confirming orders

---

## Historique des revisions

| Version | Date | Description de la modification | Auteur |
|---|---|---|---|
| 0.4 | 18/02/2026 | Initial creation. Logistics and delivery procedure covering transport modes, customs documents, shipment tracking and performance indicators. Integration of field legend system. | Roxane Wicky |
