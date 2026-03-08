#!/usr/bin/env python3
"""
Generator for the vue_ensemble_interactive_v2.drawio diagram
QMS ISO 9001:2015 — Plus Sàrl

Structure:
  Page 1:  Overview swimlane (mapping + integrated chain)
  Page 2:  PM01 Leadership & Management
  Page 3:  P01 Commercial
  Page 4:  P02 Procurement & Subcontracting
  Page 5:  P03 Quality Control
  Page 6:  P04 Logistics & Delivery
  Page 7:  PS01 Document Management
  Page 8:  General Process Chain (swimlane summary, clickable blocks)
  Pages 9-16: BLOC 1-8 Detail (interactive, multi-role mini-swimlanes)
"""

import textwrap

# -- Colors by role ----------------------------------------------------
C = {
    'dir':  {'fill': '#DAE8FC', 'stroke': '#4472C4', 'font': '#4472C4', 'bg': '#4472C4'},
    'sales':{'fill': '#E2EFDA', 'stroke': '#70AD47', 'font': '#70AD47', 'bg': '#70AD47'},
    'achat':{'fill': '#FFF2CC', 'stroke': '#D6B656', 'font': '#D6B656', 'bg': '#D6B656'},
    'deliv':{'fill': '#E1D5E7', 'stroke': '#9673A6', 'font': '#9673A6', 'bg': '#9673A6'},
    'qual': {'fill': '#F8CECC', 'stroke': '#B85450', 'font': '#B85450', 'bg': '#B85450'},
    'sup':  {'fill': '#F5F5F5', 'stroke': '#666666', 'font': '#666666', 'bg': '#666666'},
    'chain':{'fill': '#FFF3E0', 'stroke': '#FF8C00', 'font': '#FF8C00', 'bg': '#FF8C00'},
}

def esc(s):
    """Escape for XML attribute values."""
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace("'", '&apos;').replace('"', '&quot;')

def cell(id, value, style, x, y, w, h, parent="1"):
    return f'        <mxCell id="{id}" value="{esc(value)}" style="{style}" vertex="1" parent="{parent}"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>\n'

def link_overlay(id, link, x, y, w, h, parent="1"):
    """Invisible clickable overlay."""
    return (f'        <UserObject label="" link="data:page/id,{link}" id="{id}_link">\n'
            f'          <mxCell style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=none;opacity=0;cursor=pointer;" vertex="1" parent="{parent}">\n'
            f'            <mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>\n'
            f'          </mxCell>\n'
            f'        </UserObject>\n')

def edge(id, src, tgt, color, parent="1", dashed=False, label="", width=2, points=None):
    dash = "dashed=1;" if dashed else ""
    lbl = esc(label) if label else ""
    font = f"fontSize=9;fontColor={color};" if label else ""
    pts = ""
    if points:
        pts_xml = "".join(f'<mxPoint x="{px}" y="{py}"/>' for px, py in points)
        pts = f"<Array as=\"points\">{pts_xml}</Array>"
    return (f'        <mxCell id="{id}" value="{lbl}" style="edgeStyle=orthogonalEdgeStyle;strokeColor={color};strokeWidth={width};{dash}{font}" edge="1" source="{src}" target="{tgt}" parent="{parent}">\n'
            f'          <mxGeometry relative="1" as="geometry">{pts}</mxGeometry>\n'
            f'        </mxCell>\n')

def edge_pts(id, color, sx, sy, tx, ty, parent="1", dashed=False, label="", width=2, points=None):
    """Edge by coordinates (no source/target cells)."""
    dash = "dashed=1;" if dashed else ""
    lbl = esc(label) if label else ""
    font = f"fontSize=9;fontColor={color};" if label else ""
    pts = ""
    if points:
        pts_xml = "".join(f'<mxPoint x="{px}" y="{py}"/>' for px, py in points)
        pts = f"<Array as=\"points\">{pts_xml}</Array>"
    return (f'        <mxCell id="{id}" value="{lbl}" style="edgeStyle=orthogonalEdgeStyle;strokeColor={color};strokeWidth={width};{dash}{font}" edge="1" parent="{parent}">\n'
            f'          <mxGeometry relative="1" as="geometry"><mxPoint x="{sx}" y="{sy}" as="sourcePoint"/><mxPoint x="{tx}" y="{ty}" as="targetPoint"/>{pts}</mxGeometry>\n'
            f'        </mxCell>\n')

def back_button(link="page-overview", label="Back to Overview"):
    return (f'        <UserObject label="&lt;b&gt;&amp;larr; {esc(label)}&lt;/b&gt;" link="data:page/id,{link}">\n'
            f'          <mxCell style="rounded=1;whiteSpace=wrap;html=1;fillColor=#EEEEEE;strokeColor=#999999;fontSize=10;fontColor=#333333;shadow=1;" vertex="1" parent="1">\n'
            f'            <mxGeometry x="20" y="20" width="200" height="35" as="geometry"/>\n'
            f'          </mxCell>\n'
            f'        </UserObject>\n')

def nav_button(id, label, link, x, y, w=140, h=30, fill="#EEEEEE", stroke="#999999"):
    return (f'        <UserObject label="&lt;b&gt;{esc(label)}&lt;/b&gt;" link="data:page/id,{link}" id="{id}">\n'
            f'          <mxCell style="rounded=1;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};fontSize=10;fontColor=#333333;shadow=1;" vertex="1" parent="1">\n'
            f'            <mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>\n'
            f'          </mxCell>\n'
            f'        </UserObject>\n')

def diagram_start(id, name, dx=2200, dy=1500, pw=2200, ph=1500):
    return (f'  <diagram id="{id}" name="{esc(name)}">\n'
            f'    <mxGraphModel dx="{dx}" dy="{dy}" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{pw}" pageHeight="{ph}" math="0" shadow="0">\n'
            f'      <root>\n'
            f'        <mxCell id="0"/>\n'
            f'        <mxCell id="1" parent="0"/>\n')

def diagram_end():
    return ('      </root>\n'
            '    </mxGraphModel>\n'
            '  </diagram>\n')


# ===================================================================
# PAGE 1: OVERVIEW IN SWIMLANE
# ===================================================================
def page1_overview():
    o = ""
    o += '  <!-- ================================================================ -->\n'
    o += '  <!-- PAGE 1: OVERVIEW - SWIMLANE BY ROLE                              -->\n'
    o += '  <!-- ================================================================ -->\n'
    o += diagram_start("page-overview", "OVERVIEW v2", dx=2400, dy=1600, pw=2400, ph=1600)

    # TITLE
    o += cell("ov_title",
        "<b style='font-size:18px'>QMS MAPPING ISO 9001:2015</b><br>"
        "Plus Sarl - Industrial follow-up and sourcing Worldwide<br>"
        "v0.7 - 2026-03-05<br>"
        "<i style='color:#888'>Click on each element to access the detail</i>",
        "text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=12;",
        500, 10, 1200, 80)

    # -- CUSTOMER INPUT --
    o += cell("ov_cin", "<b>CUSTOMERS</b><br>(International)<br><br>Needs<br>Requirements<br>Orders",
        "shape=trapezoid;perimeter=trapezoidPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#E2EFDA;strokeColor=#70AD47;fontSize=11;shadow=1;",
        20, 450, 130, 140)

    # -- CUSTOMER OUTPUT --
    o += cell("ov_cout", "<b>CUSTOMERS</b><br>(International)<br><br>Satisfaction<br>Conforming products<br>On-time delivery",
        "shape=trapezoid;perimeter=trapezoidPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#E2EFDA;strokeColor=#70AD47;fontSize=11;shadow=1;",
        2240, 450, 130, 140)

    # -- SUPPLIERS --
    o += cell("ov_fourn", "<b>SUPPLIERS</b><br>(International)<br><br>Production<br>Delivery",
        "shape=trapezoid;perimeter=trapezoidPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=11;shadow=1;",
        2240, 640, 130, 110)

    # =================== SWIMLANES ===================
    sw_x = 170; sw_w = 2050

    # -- SWIMLANE MANAGEMENT (Management) --
    y_dir = 100; h_dir = 150
    o += cell("sw_dir", "<b>MANAGEMENT</b>",
        f"swimlane;startSize=30;horizontal=1;fillColor={C['dir']['fill']};strokeColor={C['dir']['stroke']};fontStyle=1;fontSize=12;swimlaneLine=1;",
        sw_x, y_dir, sw_w, h_dir)
    # PM01
    o += cell("ov_pm01", "<b>PM01</b><br>Leadership &amp; Management<br><i>Policy | Objectives | Risks<br>Management review | KPIs</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['dir']['fill']};strokeColor={C['dir']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        40, 40, 280, 95, parent="sw_dir")
    o += link_overlay("ov_pm01", "page-m1", 40, 40, 280, 95, parent="sw_dir")
    # PS03
    o += cell("ov_ps03", "<b>PS03</b><br>Continuous Improvement<br><i>PDCA | Annual program</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['dir']['fill']};strokeColor={C['dir']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        360, 40, 230, 95, parent="sw_dir")
    # Arrows PM01
    o += cell("ov_dir_pdca", "PDCA &#8635;",
        f"text;html=1;align=center;fontSize=10;fontColor={C['dir']['font']};fillColor=none;strokeColor=none;fontStyle=2;",
        630, 70, 60, 20, parent="sw_dir")

    # -- SWIMLANE COMMERCIAL (SALES) --
    y_sales = 260; h_sales = 210
    o += cell("sw_sales", "<b>01 SALES — Sales Role</b>",
        f"swimlane;startSize=30;horizontal=1;fillColor={C['sales']['fill']};strokeColor={C['sales']['stroke']};fontStyle=1;fontSize=12;swimlaneLine=1;",
        sw_x, y_sales, sw_w, h_sales)
    # P01
    o += cell("ov_p01", "<b>P01</b><br>Commercial<br><i>Quotation | Contract<br>Follow-up | Satisfaction</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['sales']['fill']};strokeColor={C['sales']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        20, 40, 170, 80, parent="sw_sales")
    o += link_overlay("ov_p01", "page-p01", 20, 40, 170, 80, parent="sw_sales")

    # Chain blocs in SALES
    bx = 230; bw = 140; bh = 70; by_s = 45
    for bid, bname, bpage in [("ov_b1","BLOC 1<br>Order<br>Reception","page-bloc1"),
                                ("ov_b2","BLOC 2<br>Order<br>Sheet","page-bloc2")]:
        o += cell(bid, f"<b>{bname}</b>",
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['sales']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
            bx, by_s, bw, bh, parent="sw_sales")
        o += link_overlay(bid, bpage, bx, by_s, bw, bh, parent="sw_sales")
        bx += bw + 20

    # B5
    o += cell("ov_b5", "<b>BLOC 5<br>Order<br>Validation</b>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['sales']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        730, by_s, bw, bh, parent="sw_sales")
    o += link_overlay("ov_b5", "page-bloc5", 730, by_s, bw, bh, parent="sw_sales")

    # B7 SALES part (dashed)
    o += cell("ov_b7s", "<b>BLOC 7</b><br><i>Invoice +<br>Customer info</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['sales']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=1;dashed=1;shadow=0;fontSize=9;",
        1200, by_s, 130, bh, parent="sw_sales")
    o += link_overlay("ov_b7s", "page-bloc7", 1200, by_s, 130, bh, parent="sw_sales")

    # B8 SALES part (dashed)
    o += cell("ov_b8s", "<b>BLOC 8</b><br><i>Invoice | Customs<br>Payment | Closure</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['sales']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=1;dashed=1;shadow=0;fontSize=9;",
        1370, by_s, 140, bh, parent="sw_sales")
    o += link_overlay("ov_b8s", "page-bloc8", 1370, by_s, 140, bh, parent="sw_sales")

    # Arrows within SALES
    o += edge("ov_e_p01_b1", "ov_p01", "ov_b1", C['sales']['stroke'], parent="sw_sales")
    o += edge("ov_e_b1_b2", "ov_b1", "ov_b2", C['sales']['stroke'], parent="sw_sales")
    o += edge("ov_e_b7s_b8s", "ov_b7s", "ov_b8s", C['sales']['stroke'], parent="sw_sales")

    # -- SWIMLANE PROCUREMENT (MANUFACTURE) --
    y_achat = 480; h_achat = 180
    o += cell("sw_achat", "<b>02 MANUFACTURE — Procurement Role</b>",
        f"swimlane;startSize=30;horizontal=1;fillColor={C['achat']['fill']};strokeColor={C['achat']['stroke']};fontStyle=1;fontSize=12;swimlaneLine=1;",
        sw_x, y_achat, sw_w, h_achat)
    o += cell("ov_p02", "<b>P02</b><br>Procurement &amp;<br>Subcontracting<br><i>Evaluation | QAA | Follow-up</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['achat']['fill']};strokeColor={C['achat']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        20, 40, 170, 80, parent="sw_achat")
    o += link_overlay("ov_p02", "page-p02", 20, 40, 170, 80, parent="sw_achat")

    # B4
    o += cell("ov_b4", "<b>BLOC 4<br>Technical Study<br>Suppliers</b>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['achat']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        550, 45, bw, bh, parent="sw_achat")
    o += link_overlay("ov_b4", "page-bloc4", 550, 45, bw, bh, parent="sw_achat")

    # B6 MANUFACTURE part
    o += cell("ov_b6m", "<b>BLOC 6</b><br><i>Supplier<br>Production</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['achat']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        950, 45, bw, bh, parent="sw_achat")
    o += link_overlay("ov_b6m", "page-bloc6", 950, 45, bw, bh, parent="sw_achat")

    o += edge("ov_e_b4_b6m", "ov_b4", "ov_b6m", C['achat']['stroke'], parent="sw_achat")

    # -- SWIMLANE LOGISTICS (DELIVERY) --
    y_deliv = 670; h_deliv = 180
    o += cell("sw_deliv", "<b>03 DELIVERY — Logistics Role</b>",
        f"swimlane;startSize=30;horizontal=1;fillColor={C['deliv']['fill']};strokeColor={C['deliv']['stroke']};fontStyle=1;fontSize=12;swimlaneLine=1;",
        sw_x, y_deliv, sw_w, h_deliv)
    o += cell("ov_p04", "<b>P04</b><br>Logistics &amp;<br>Delivery<br><i>Transport | Customs</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['deliv']['fill']};strokeColor={C['deliv']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        20, 40, 170, 80, parent="sw_deliv")
    o += link_overlay("ov_p04", "page-p04", 20, 40, 170, 80, parent="sw_deliv")

    # B3
    o += cell("ov_b3", "<b>BLOC 3<br>Transport<br>Sheet</b>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['deliv']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        550, 45, bw, bh, parent="sw_deliv")
    o += link_overlay("ov_b3", "page-bloc3", 550, 45, bw, bh, parent="sw_deliv")

    # B7 DELIVERY part
    o += cell("ov_b7d", "<b>BLOC 7</b><br><i>Delivery<br>Customs</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['deliv']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        1200, 45, 130, bh, parent="sw_deliv")
    o += link_overlay("ov_b7d", "page-bloc7", 1200, 45, 130, bh, parent="sw_deliv")

    o += edge("ov_e_b3_b7d", "ov_b3", "ov_b7d", C['deliv']['stroke'], parent="sw_deliv")

    # -- SWIMLANE QUALITY (QUALITY) --
    y_qual = 860; h_qual = 180
    o += cell("sw_qual", "<b>04 QUALITY — Quality Role</b>",
        f"swimlane;startSize=30;horizontal=1;fillColor={C['qual']['fill']};strokeColor={C['qual']['stroke']};fontStyle=1;fontSize=12;swimlaneLine=1;",
        sw_x, y_qual, sw_w, h_qual)
    o += cell("ov_p03", "<b>P03</b><br>Quality Control<br><i>IPC | DUPRO | PSI<br>NC | Corrective actions</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['qual']['fill']};strokeColor={C['qual']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        20, 40, 170, 80, parent="sw_qual")
    o += link_overlay("ov_p03", "page-p03", 20, 40, 170, 80, parent="sw_qual")

    # B6 QUALITY part
    o += cell("ov_b6q", "<b>BLOC 6</b><br><i>Conformity<br>Validation</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['qual']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        950, 45, bw, bh, parent="sw_qual")
    o += link_overlay("ov_b6q", "page-bloc6", 950, 45, bw, bh, parent="sw_qual")

    # B8 QUALITY part
    o += cell("ov_b8q", "<b>BLOC 8</b><br><i>Goods<br>Acceptance</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['qual']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        1370, 45, bw, bh, parent="sw_qual")
    o += link_overlay("ov_b8q", "page-bloc8", 1370, 45, bw, bh, parent="sw_qual")

    o += edge("ov_e_b6q_b8q", "ov_b6q", "ov_b8q", C['qual']['stroke'], parent="sw_qual")

    # -- SWIMLANE SUPPORT --
    y_sup = 1050; h_sup = 130
    o += cell("sw_sup", "<b>SUPPORT</b>",
        f"swimlane;startSize=30;horizontal=1;fillColor={C['sup']['fill']};strokeColor={C['sup']['stroke']};fontStyle=1;fontSize=12;swimlaneLine=1;",
        sw_x, y_sup, sw_w, h_sup)
    o += cell("ov_ps01", "<b>PS01</b><br>Document Management<br><i>Create | Control | Archive</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['sup']['fill']};strokeColor={C['sup']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        20, 40, 230, 75, parent="sw_sup")
    o += link_overlay("ov_ps01", "page-s1", 20, 40, 230, 75, parent="sw_sup")
    o += cell("ov_ps02", "<b>PS02</b><br>Competence Management<br><i>Matrix | Training</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['sup']['fill']};strokeColor={C['sup']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        280, 40, 230, 75, parent="sw_sup")

    # =========== INTER-SWIMLANE ARROWS (chain flow) ===========
    # These use absolute coordinates since they cross swimlanes
    # B2 -> B3 (Sales -> Delivery) and B2 -> B4 (Sales -> Manufacture)
    # B2 bottom edge: sw_x + 390 + 70 = ~630, y_sales + 30 + 45 + 70 = ~415
    b2_out_x = sw_x + 460; b2_out_y = y_sales + h_sales  # bottom of B2
    b3_in_x = sw_x + 620; b3_in_y = y_deliv + 75   # top of B3
    b4_in_x = sw_x + 620; b4_in_y = y_achat + 75   # top of B4

    o += edge_pts("ov_ie_b2_b4", C['chain']['stroke'],
        b2_out_x, b2_out_y - 5, b4_in_x, b4_in_y,
        dashed=True, label="Manufacturing", points=[(b2_out_x, y_achat + 40)])

    o += edge_pts("ov_ie_b2_b3", C['chain']['stroke'],
        b2_out_x - 40, b2_out_y - 5, b3_in_x - 40, b3_in_y,
        dashed=True, label="Transport")

    # B3 + B4 -> B5 (lead time feedback to Sales)
    b5_in_x = sw_x + 800; b5_in_y = y_sales + h_sales  # bottom of B5 area
    o += edge_pts("ov_ie_b4_b5", C['chain']['stroke'],
        sw_x + 690 + 70, y_achat + 75, b5_in_x, y_sales + h_sales - 5,
        dashed=True, label="Lead time feedback", points=[(sw_x + 770, y_achat + 50), (sw_x + 770, y_sales + h_sales - 5)])

    # B5 -> B6m (Sales -> Manufacture: confirmation)
    o += edge_pts("ov_ie_b5_b6m", C['chain']['stroke'],
        sw_x + 870, y_sales + h_sales - 5, sw_x + 1020, y_achat + 75,
        dashed=True, label="Confirmation")

    # B6m -> B6q (Manufacture -> Quality)
    o += edge_pts("ov_ie_b6m_b6q", C['chain']['stroke'],
        sw_x + 1020, y_achat + h_achat - 5, sw_x + 1020, y_qual + 75,
        dashed=True, label="QC Validation", points=[(sw_x + 1020, y_deliv + h_deliv//2)])

    # B6q -> B7d (Quality -> Delivery: release)
    o += edge_pts("ov_ie_b6q_b7d", C['chain']['stroke'],
        sw_x + 1090, y_qual + 75, sw_x + 1270, y_deliv + 115,
        dashed=True, label="Release", points=[(sw_x + 1150, y_qual + 75), (sw_x + 1150, y_deliv + 115)])

    # B7d -> B7s (Delivery -> Sales)
    o += edge_pts("ov_ie_b7d_b7s", C['chain']['stroke'],
        sw_x + 1265, y_deliv + 75, sw_x + 1265, y_sales + h_sales - 5,
        dashed=True, label="Docs")

    # B8q -> B8s (Quality -> Sales)
    o += edge_pts("ov_ie_b8q_b8s", C['chain']['stroke'],
        sw_x + 1440, y_qual + 75, sw_x + 1440, y_sales + h_sales - 5,
        dashed=True, label="Closure")

    # Client IN -> P01
    o += edge("ov_e_cin_sw", "ov_cin", "ov_p01", C['sales']['stroke'], width=3)

    # B8s -> Client OUT
    o += edge_pts("ov_e_out", C['sales']['stroke'],
        sw_x + sw_w, y_sales + 110, 2240, 520, width=3)

    # P02 -> Suppliers
    o += edge_pts("ov_e_fourn", C['achat']['stroke'],
        sw_x + sw_w, y_achat + 90, 2240, 695, width=2)

    # =========== LEGEND ===========
    ly = 1200
    o += cell("ov_leg_box", "",
        "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;strokeWidth=1;",
        sw_x, ly, 900, 160)
    o += cell("ov_leg_title", "<b>LEGEND</b>",
        "text;html=1;align=left;fontSize=11;fillColor=none;strokeColor=none;", sw_x+10, ly+5, 100, 25)

    colors_legend = [
        (C['dir'], "Management — Management Process"),
        (C['sales'], "Commercial (SALES) — P01"),
        (C['achat'], "Procurement (MANUFACTURE) — P02"),
        (C['deliv'], "Logistics (DELIVERY) — P04"),
        (C['qual'], "Quality (QUALITY) — P03"),
        (C['sup'], "Support — PS01, PS02, PS03"),
    ]
    for i, (c, lbl) in enumerate(colors_legend):
        col = 0 if i < 3 else 1
        row = i % 3
        ox = sw_x + 20 + col * 350
        oy = ly + 35 + row * 22
        o += cell(f"ov_lc{i}", "", f"rounded=1;fillColor={c['fill']};strokeColor={c['stroke']};", ox, oy, 20, 15)
        o += cell(f"ov_lt{i}", lbl, f"text;html=1;align=left;fontSize=10;fillColor=none;strokeColor=none;", ox+30, oy-2, 280, 20)

    # Chain legend
    o += cell("ov_lc_ch", "", f"rounded=1;fillColor={C['chain']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;",
        sw_x + 20, ly + 105, 20, 15)
    o += cell("ov_lt_ch", "Orange border = General Process Chain Block (clickable)",
        f"text;html=1;align=left;fontSize=10;fillColor=none;strokeColor=none;fontColor={C['chain']['font']};",
        sw_x + 50, ly + 103, 400, 20)
    o += cell("ov_lt_note",
        "<i>Click on each colored block to navigate to the detailed sub-diagram.<br>"
        "The dashed orange arrows show the inter-role operational flow.</i>",
        "text;html=1;align=left;fontSize=9;fillColor=none;strokeColor=none;fontColor=#666666;",
        sw_x + 20, ly + 130, 600, 30)

    # -- Link to full chain --
    o += nav_button("ov_goto_chain", "View Full Process Chain &#8594;", "page-chain",
        sw_x + 1550, ly + 10, 250, 40, fill=C['chain']['fill'], stroke=C['chain']['stroke'])

    o += diagram_end()
    return o


# ===================================================================
# PAGES 2-7: PROCESS DETAIL (from v1 with improvements)
# ===================================================================

def process_detail_page(page_id, name, role, color_key, steps, iso_refs=""):
    c = C[color_key]
    o = diagram_start(page_id, name, dx=1600, dy=900, pw=1600, ph=900)
    o += back_button()

    o += cell("pd_title", f"<b style='font-size:16px'>{esc(name)}</b><br>{esc(role)}<br>ISO 9001:2015",
        "text;html=1;align=center;verticalAlign=middle;fillColor=none;strokeColor=none;fontSize=12;",
        400, 15, 600, 60)
    o += cell("pd_role", f"<b>{esc(role)}</b>",
        f"rounded=0;whiteSpace=wrap;html=1;fillColor={c['bg']};fontColor=#FFFFFF;strokeColor={c['bg']};fontSize=11;",
        40, 100, 130, 40)

    for i, (label, detail) in enumerate(steps):
        x = 40 + i * 175
        o += cell(f"pd_a{i}", f"<b>{esc(label)}</b><br><br><i>{esc(detail)}</i>",
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={c['fill']};strokeColor={c['stroke']};fontSize=10;",
            x, 170, 155, 95)
        if i > 0:
            o += edge(f"pd_e{i}", f"pd_a{i-1}", f"pd_a{i}", c['stroke'])

    # PDCA loop
    if len(steps) > 1:
        o += cell("pd_pdca", "PDCA &#8635;",
            f"text;html=1;align=center;fontSize=10;fontColor={c['font']};fillColor=none;strokeColor=none;fontStyle=2;",
            40 + len(steps)*175//2 - 40, 300, 80, 25)

    o += diagram_end()
    return o


def page2_m1():
    return process_detail_page("page-m1", "PM01 - Leadership & Management", "Management", "dir", [
        ("Analyze context", "(s4.1) Interested parties\nInternal/external issues"),
        ("Define policy", "(s5.2) Management commitment\nCustomer focus"),
        ("Set objectives", "(s6.2) Measurable, consistent\nwith policy"),
        ("Allocate resources", "(s7.1) Human, material\nfinancial"),
        ("Manage risks", "(s6.1) Risk matrix\nOpportunities"),
        ("Management review", "(s9.3) Periodic assessment\nDecisions"),
        ("Improve", "(s10.3) PDCA\nPreventive actions"),
        ("Monitor KPIs", "(s9.1) Dashboards\nPerformance monitoring"),
    ])

def page3_p01():
    return process_detail_page("page-p01", "P01 - Commercial", "Sales Role", "sales", [
        ("Request reception", "Email / phone\nCRM registration"),
        ("Feasibility analysis", "Technical verification\nSupplier capacity"),
        ("Quotation & proposal", "Price, lead time, conditions\nSent to customer"),
        ("Contract review", "Requirements validation\nCommercial agreement"),
        ("Order confirmed", "PO received\nProcess launch"),
        ("Order follow-up", "Dashboard\nCustomer communication"),
        ("Invoicing", "Customer invoice\nCustoms declaration"),
        ("Satisfaction", "Customer survey\nFeedback analysis"),
    ])

def page4_p02():
    return process_detail_page("page-p02", "P02 - Procurement & Subcontracting", "Procurement Role", "achat", [
        ("Identify suppliers", "Market research\nSelection criteria"),
        ("Evaluate & qualify", "Supplier audit\nEvaluation grid"),
        ("Sign QAA", "Quality Assurance\nAgreement"),
        ("Issue order", "Supplier PO\nSpecifications"),
        ("Monitor production", "Supplier contact\nProduction status"),
        ("Re-evaluate suppliers", "Annual review\nQCDM rating"),
        ("Manage supplier NC", "NC sheets\nAction follow-up"),
        ("Panel A/B/C", "Supplier\nclassification"),
    ])

def page5_p03():
    return process_detail_page("page-p03", "P03 - Quality Control", "Quality Role", "qual", [
        ("Plan QC", "Inspection planning\nAssignment"),
        ("IPC", "Initial Production\nCheck"),
        ("DUPRO", "During Production\nInspection"),
        ("PSI", "Pre-Shipment\nInspection"),
        ("Loading Check", "Loading control\nContainer"),
        ("Detect NC", "Non-conformities\nInspection report"),
        ("Process NC", "Accept / rework\nreject"),
        ("Corrective actions", "Root cause\nAction plan"),
    ])

def page6_p04():
    return process_detail_page("page-p04", "P04 - Logistics & Delivery", "Logistics Role", "deliv", [
        ("Plan shipment", "Date, volume\nTransport mode"),
        ("Select carrier", "Transport quotation\nCarrier selection"),
        ("Transport documents", "BL, packing list\nCertificates"),
        ("Shipment follow-up", "Tracking\nCommunication"),
        ("Customs management", "Customs declaration\nCustoms agent"),
        ("Delivery confirmation", "Customer reception\nProof of delivery"),
        ("Archiving", "Complete file\nDocument retention"),
    ])

def page7_s1():
    return process_detail_page("page-s1", "PS01 - Document Management", "Support", "sup", [
        ("Create documents", "Procedures, forms\nInstructions"),
        ("Review & approve", "Technical review\nManagement approval"),
        ("Distribute", "Make available\nCommunication"),
        ("Control versions", "Revision index\nChange history"),
        ("Archive", "Retention\nRetention period"),
        ("Audit compliance", "Verification\nDocument gaps"),
        ("Improve doc. system", "User feedback\nSimplification"),
    ])


# ===================================================================
# PAGE 8: GENERAL PROCESS CHAIN — Swimlane summary view
# ===================================================================

def page8_chain():
    o = '  <!-- ================================================================ -->\n'
    o += '  <!-- PAGE 8: GENERAL PROCESS CHAIN - SWIMLANE SUMMARY                -->\n'
    o += '  <!-- ================================================================ -->\n'
    o += diagram_start("page-chain", "General Process Chain", dx=1800, dy=1000, pw=1800, ph=1000)
    o += back_button()

    o += cell("ch_title",
        "<b style='font-size:16px'>GENERAL PROCESS CHAIN</b><br>"
        "Existing Product Order (CHAIN-01)<br>"
        "<i style='color:#888'>Click on each BLOC to see the detail</i>",
        "text;html=1;align=center;verticalAlign=middle;fillColor=none;strokeColor=none;fontSize=12;",
        400, 10, 800, 60)

    # Client in
    o += cell("ch_cin", "<b>CUSTOMER</b><br>Order",
        "shape=trapezoid;perimeter=trapezoidPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#E2EFDA;strokeColor=#70AD47;fontSize=10;shadow=1;",
        20, 175, 100, 60)

    # Mini swimlane labels (horizontal bands)
    sw_x = 140; sw_w = 1500
    lanes = [
        ("ch_sw_s", "SALES", C['sales'], 100, 200),
        ("ch_sw_m", "MANUFACTURE", C['achat'], 310, 170),
        ("ch_sw_d", "DELIVERY", C['deliv'], 490, 170),
        ("ch_sw_q", "QUALITY", C['qual'], 670, 150),
    ]
    for lid, lname, lc, ly, lh in lanes:
        o += cell(lid, f"<b>{lname}</b>",
            f"swimlane;startSize=25;horizontal=1;fillColor={lc['fill']};strokeColor={lc['stroke']};fontStyle=1;fontSize=11;swimlaneLine=1;",
            sw_x, ly, sw_w, lh)

    # Blocs (positioned in swimlanes)
    blocs = [
        ("ch_b1", "B1\nOrder\nReception", "ch_sw_s", 40, 35, 120, 60, "page-bloc1", C['sales']),
        ("ch_b2", "B2\nOrder\nSheet", "ch_sw_s", 190, 35, 120, 60, "page-bloc2", C['sales']),
        ("ch_b5", "B5\nOrder\nValidation", "ch_sw_s", 530, 35, 120, 60, "page-bloc5", C['sales']),
        ("ch_b7s", "B7 (Sales)\nInvoice\nCustomer info", "ch_sw_s", 900, 35, 110, 60, "page-bloc7", C['sales']),
        ("ch_b8s", "B8 (Sales)\nInvoice\nClosure", "ch_sw_s", 1050, 35, 110, 60, "page-bloc8", C['sales']),
        ("ch_b4", "B4\nTech. Study\nSuppliers", "ch_sw_m", 340, 35, 120, 60, "page-bloc4", C['achat']),
        ("ch_b6m", "B6 (Manuf.)\nSupplier\nProduction", "ch_sw_m", 700, 35, 120, 60, "page-bloc6", C['achat']),
        ("ch_b3", "B3\nTransport\nSheet", "ch_sw_d", 340, 35, 120, 60, "page-bloc3", C['deliv']),
        ("ch_b7d", "B7 (Deliv.)\nDelivery\nCustoms", "ch_sw_d", 900, 35, 110, 60, "page-bloc7", C['deliv']),
        ("ch_b6q", "B6 (Qual.)\nConformity\nValidation", "ch_sw_q", 700, 35, 120, 60, "page-bloc6", C['qual']),
        ("ch_b8q", "B8 (Qual.)\nGoods\nAcceptance", "ch_sw_q", 1050, 35, 110, 60, "page-bloc8", C['qual']),
    ]

    for bid, bname, parent, bx, by, bw, bh, bpage, bc in blocs:
        o += cell(bid, f"<b>{esc(bname)}</b>",
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={bc['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;shadow=1;fontSize=9;",
            bx, by, bw, bh, parent=parent)
        o += link_overlay(bid, bpage, bx, by, bw, bh, parent=parent)

    # Intra-lane arrows
    o += edge("ch_e_b1b2", "ch_b1", "ch_b2", C['sales']['stroke'], parent="ch_sw_s")
    o += edge("ch_e_b7sb8s", "ch_b7s", "ch_b8s", C['sales']['stroke'], parent="ch_sw_s")
    o += edge("ch_e_b4b6m", "ch_b4", "ch_b6m", C['achat']['stroke'], parent="ch_sw_m")
    o += edge("ch_e_b3b7d", "ch_b3", "ch_b7d", C['deliv']['stroke'], parent="ch_sw_d")
    o += edge("ch_e_b6qb8q", "ch_b6q", "ch_b8q", C['qual']['stroke'], parent="ch_sw_q")

    # Inter-lane arrows (absolute coords)
    # B2->B4 (Sales->Manuf), B2->B3 (Sales->Deliv)
    o += edge_pts("ch_ie1", C['chain']['stroke'], 390, 295, 510, 345, dashed=True, label="Manufacturing")
    o += edge_pts("ch_ie2", C['chain']['stroke'], 370, 295, 510, 525, dashed=True, label="Transport")
    # B4+B3 -> B5
    o += edge_pts("ch_ie3", C['chain']['stroke'], 600, 345, 670, 160, dashed=True, label="Lead time feedback",
        points=[(620, 300), (640, 300), (640, 160)])
    # B5 -> B6m
    o += edge_pts("ch_ie4", C['chain']['stroke'], 790, 200, 840, 345, dashed=True, label="Confirmation")
    # B6m -> B6q
    o += edge_pts("ch_ie5", C['chain']['stroke'], 900, 410, 900, 705, dashed=True, label="QC Validation",
        points=[(900, 550)])
    # B6q -> B7d
    o += edge_pts("ch_ie6", C['chain']['stroke'], 960, 720, 1040, 560, dashed=True, label="Release",
        points=[(980, 680), (980, 560)])
    # B7d -> B7s
    o += edge_pts("ch_ie7", C['chain']['stroke'], 1080, 530, 1060, 195, dashed=True, label="Docs")
    # B8q -> B8s
    o += edge_pts("ch_ie8", C['chain']['stroke'], 1210, 720, 1190, 195, dashed=True, label="Closure")

    # Client arrows
    o += edge_pts("ch_e_cin", C['sales']['stroke'], 120, 205, 180, 160, width=3)

    # Client out
    o += cell("ch_cout", "<b>CUSTOMER</b><br>Product delivered",
        "shape=trapezoid;perimeter=trapezoidPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#E2EFDA;strokeColor=#70AD47;fontSize=10;shadow=1;",
        1670, 175, 100, 60)
    o += edge_pts("ch_e_cout", C['sales']['stroke'], 1300, 160, 1670, 205, width=3)

    # Legend
    o += cell("ch_note",
        "<i>This diagram shows the operational flow CHAIN-01 (Existing Product Order).<br>"
        "Each BLOC is clickable to see the detail of actions.</i>",
        "text;html=1;align=left;fontSize=9;fillColor=none;strokeColor=none;fontColor=#666666;",
        140, 860, 600, 30)

    o += diagram_end()
    return o


# ===================================================================
# PAGES 9-16: DETAIL OF EACH BLOC
# ===================================================================

def bloc_detail_page(page_id, bloc_num, bloc_title, bloc_ref, roles, actions_by_role,
                     prev_bloc=None, next_bloc=None, iso_clause="", doc_refs=None):
    """
    roles: list of (role_name, color_key)
    actions_by_role: dict { color_key: [(action_name, detail), ...] }
    """
    o = f'  <!-- PAGE: BLOC {bloc_num} -->\n'
    o += diagram_start(page_id, f"BLOC {bloc_num} - {bloc_title}", dx=1600, dy=900, pw=1600, ph=900)
    o += back_button("page-chain", "Back to Chain")

    # Also add link to overview
    o += nav_button("bn_ov", "Overview", "page-overview", 230, 20, 140, 35)

    o += cell("bt_title",
        f"<b style='font-size:16px'>BLOC {bloc_num} — {esc(bloc_title)}</b><br>"
        f"<i>{esc(bloc_ref)}</i>"
        f"{'<br>ISO 9001: ' + esc(iso_clause) if iso_clause else ''}",
        "text;html=1;align=center;verticalAlign=middle;fillColor=none;strokeColor=none;fontSize=12;",
        450, 10, 600, 65)

    if len(roles) == 1:
        # Single role — no swimlane needed
        rname, rkey = roles[0]
        c = C[rkey]
        o += cell("bt_role", f"<b>{esc(rname)}</b>",
            f"rounded=0;whiteSpace=wrap;html=1;fillColor={c['bg']};fontColor=#FFFFFF;strokeColor={c['bg']};fontSize=11;",
            40, 90, 130, 35)
        actions = actions_by_role[rkey]
        for i, (aname, adetail) in enumerate(actions):
            x = 40 + i * 170
            o += cell(f"bt_a{i}", f"<b>{esc(aname)}</b><br><br><i>{esc(adetail)}</i>",
                f"rounded=1;whiteSpace=wrap;html=1;fillColor={c['fill']};strokeColor={c['stroke']};fontSize=10;shadow=1;",
                x, 145, 150, 90)
            if i > 0:
                o += edge(f"bt_e{i}", f"bt_a{i-1}", f"bt_a{i}", c['stroke'])
    else:
        # Multi-role — use mini swimlanes
        sw_y = 85
        for ri, (rname, rkey) in enumerate(roles):
            c = C[rkey]
            sh = 150
            o += cell(f"bt_sw{ri}", f"<b>{esc(rname)}</b>",
                f"swimlane;startSize=25;horizontal=1;fillColor={c['fill']};strokeColor={c['stroke']};fontStyle=1;fontSize=11;swimlaneLine=1;",
                40, sw_y, 1500, sh)
            actions = actions_by_role.get(rkey, [])
            for i, (aname, adetail) in enumerate(actions):
                x = 30 + i * 170
                o += cell(f"bt_a{ri}_{i}", f"<b>{esc(aname)}</b><br><br><i>{esc(adetail)}</i>",
                    f"rounded=1;whiteSpace=wrap;html=1;fillColor={c['fill']};strokeColor={c['stroke']};fontSize=10;shadow=1;",
                    x, 35, 150, 95, parent=f"bt_sw{ri}")
                if i > 0:
                    o += edge(f"bt_e{ri}_{i}", f"bt_a{ri}_{i-1}", f"bt_a{ri}_{i}", c['stroke'], parent=f"bt_sw{ri}")
            sw_y += sh + 10

    # Doc references
    if doc_refs:
        doc_y = 700
        o += cell("bt_docs", "<b>Associated documents:</b><br>" + "<br>".join(esc(d) for d in doc_refs),
            "text;html=1;align=left;fontSize=10;fillColor=#FAFAFA;strokeColor=#CCCCCC;rounded=1;",
            40, doc_y, 500, 20 + len(doc_refs) * 18)

    # Navigation prev/next
    nav_y = 830
    if prev_bloc:
        o += nav_button("bn_prev", f"&larr; BLOC {bloc_num-1}", prev_bloc, 40, nav_y, 130, 30)
    if next_bloc:
        o += nav_button("bn_next", f"BLOC {bloc_num+1} &rarr;", next_bloc, 1400, nav_y, 130, 30)

    o += diagram_end()
    return o


def page9_bloc1():
    return bloc_detail_page("page-bloc1", 1, "ORDER RECEPTION", "CH-BLOC-001",
        [("Sales Role (SALES)", "sales")],
        {"sales": [
            ("Download order", "Register in\nORDER_20XX"),
            ("Identify type", "4 order types\n(existing product,\ntooling modification,\nnew tooling,\nsourcing)"),
            ("Route to\nappropriate chain", "CHAIN-01, 02, 03\nor 04"),
        ]},
        next_bloc="page-bloc2",
        iso_clause="8.2.1",
        doc_refs=["ORDER_20XX folder", "CHAIN-01 to CHAIN-04"])

def page10_bloc2():
    return bloc_detail_page("page-bloc2", 2, "ORDER SHEET CREATION", "CH-BLOC-002",
        [("Sales Role (SALES)", "sales")],
        {"sales": [
            ("Create order\nsheet", "New order\nfolder"),
            ("Add order\nPDF", "Original customer\ndocument"),
            ("Customer, date,\ndeadline", "Identification\ninformation"),
            ("Product selection", "Existing product\nlibrary"),
            ("Ordered quantity", "Volume and\nunits"),
            ("Final quantity\n= identical", "Consistency\nverification"),
            ("Order ref.\n= customer ref.", "Customer\ntraceability"),
        ]},
        prev_bloc="page-bloc1", next_bloc="page-bloc3",
        iso_clause="8.2.2, 8.2.3",
        doc_refs=["Internal order sheet", "Customer PO (PDF)", "Product library"])

def page11_bloc3():
    return bloc_detail_page("page-bloc3", 3, "TRANSPORT SHEET CREATION", "CH-BLOC-003",
        [("Logistics Role (DELIVERY)", "deliv")],
        {"deliv": [
            ("Create transport sheet", "New or add\nto existing"),
            ("Lead time validation", "Confirmation by\ncarrier"),
            ("Delivery type", "Sea, air,\nroad, express"),
        ]},
        prev_bloc="page-bloc2", next_bloc="page-bloc4",
        iso_clause="8.5.4",
        doc_refs=["Transport sheet", "Carrier quotation"])

def page12_bloc4():
    return bloc_detail_page("page-bloc4", 4, "SUPPLIER TECHNICAL STUDY", "CH-BLOC-004",
        [("Procurement Role (MANUFACTURE)", "achat")],
        {"achat": [
            ("Define order\nstatus", "Drop-down list\n(in progress, validated, etc.)"),
            ("Send info to\nsuppliers", "Required technical\nspecifications"),
            ("Production lead\ntime validation", "Confirmation by\nsupplier"),
        ]},
        prev_bloc="page-bloc3", next_bloc="page-bloc5",
        iso_clause="8.4.2, 8.4.3",
        doc_refs=["Technical specifications", "Supplier lead time confirmation"])

def page13_bloc5():
    return bloc_detail_page("page-bloc5", 5, "ORDER VALIDATION", "CH-BLOC-005",
        [("Sales Role (SALES)", "sales")],
        {"sales": [
            ("Print acknowledgment", "Acknowledgment of receipt\nfor validation"),
            ("Send acknowledgment\nto customer", "With delivery lead time\nand confirmed price"),
            ("Customer feedback", "Acceptance\nor Rejection"),
        ]},
        prev_bloc="page-bloc4", next_bloc="page-bloc6",
        iso_clause="8.2.3.1",
        doc_refs=["Acknowledgment of receipt (AR)", "Signed customer confirmation"])

def page14_bloc6():
    return bloc_detail_page("page-bloc6", 6, "PRODUCTION & QUALITY", "CH-BLOC-006",
        [("Procurement Role (MANUFACTURE)", "achat"), ("Quality Role (QUALITY)", "qual")],
        {
            "achat": [
                ("Production\nconfirmation", "Email to supplier\nGO production"),
                ("Progress follow-up", "Regular supplier\ncontact"),
            ],
            "qual": [
                ("Plan inspections", "IPC / DUPRO / PSI\nper quality plan"),
                ("Conformity validation", "Supplier quality\ncontrol"),
                ("Release decision", "Conforming: release\nNC: process"),
            ],
        },
        prev_bloc="page-bloc5", next_bloc="page-bloc7",
        iso_clause="8.5.1, 8.6, 8.7",
        doc_refs=["Inspection report (IPC/DUPRO/PSI)", "NC sheet (FM-P04-NC)", "Quality Assurance Agreement"])

def page15_bloc7():
    return bloc_detail_page("page-bloc7", 7, "DELIVERY & CUSTOMS", "CH-BLOC-007",
        [("Logistics Role (DELIVERY)", "deliv"), ("Sales Role (SALES)", "sales")],
        {
            "deliv": [
                ("Create delivery\nnote", "BL / Packing List"),
                ("Supplier\nspecifics", "Lead times, holidays\nconditions"),
                ("Shipment tracking", "Tracking with\ncarrier"),
                ("Customs tracking", "Carrier +\ncustoms agent"),
            ],
            "sales": [
                ("Commercial invoice", "To carrier\nfor customs clearance"),
                ("Inform customer", "Confirmed delivery\ndate"),
            ],
        },
        prev_bloc="page-bloc6", next_bloc="page-bloc8",
        iso_clause="8.5.4, 8.5.5",
        doc_refs=["Delivery note (BL)", "Packing list", "Commercial invoice", "Customs documents"])

def page16_bloc8():
    return bloc_detail_page("page-bloc8", 8, "GOODS ACCEPTANCE & CLOSURE", "CH-BLOC-008",
        [("Quality Role (QUALITY)", "qual"), ("Sales Role (SALES)", "sales")],
        {
            "qual": [
                ("Conformity\nconfirmation email", "To customer\ncontrol result"),
            ],
            "sales": [
                ("Send invoice\nto customer", "Final invoice"),
                ("Customs\ndeclaration", "Administrative\ndocuments"),
                ("Customer payment", "Collection follow-up"),
                ("Close file", "Complete\narchiving"),
            ],
        },
        prev_bloc="page-bloc7",
        iso_clause="8.5.5, 9.1.2",
        doc_refs=["Customer invoice", "Customs declaration", "Satisfaction survey (FM-P01-SAT)", "Archived file"])


# ===================================================================
# FINAL ASSEMBLY
# ===================================================================

def generate():
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<mxfile host="app.diagrams.net" modified="2026-03-05T14:00:00.000Z" agent="Claude" version="21.0.0" type="device">\n'

    xml += page1_overview()
    xml += page2_m1()
    xml += page3_p01()
    xml += page4_p02()
    xml += page5_p03()
    xml += page6_p04()
    xml += page7_s1()
    xml += page8_chain()
    xml += page9_bloc1()
    xml += page10_bloc2()
    xml += page11_bloc3()
    xml += page12_bloc4()
    xml += page13_bloc5()
    xml += page14_bloc6()
    xml += page15_bloc7()
    xml += page16_bloc8()

    xml += '</mxfile>\n'
    return xml


if __name__ == "__main__":
    import os
    output_path = os.path.join(os.path.dirname(__file__), "vue_ensemble_interactive_v2.drawio")
    content = generate()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {output_path}")
    print(f"  Pages: 16")
    print(f"  Size: {len(content):,} bytes")
