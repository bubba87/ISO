#!/usr/bin/env python3
"""
Generator for vue_ensemble_interactive_v3.drawio
QMS ISO 9001:2015 — Plus Sàrl

STRUCTURE (30 pages, all swimlane, fully interactive):
  Page 1:   GLOBAL OVERVIEW — Swimlane by role (all processes + chain blocs)
  Page 2:   PM01 Leadership & Management (swimlane PDCA)
  Page 3:   P01 Commercial (swimlane phases)
  Page 4:   P02 Procurement & Subcontracting (swimlane phases)
  Page 5:   P03 Quality Control (swimlane inspection types)
  Page 6:   P04 Logistics & Delivery (swimlane phases)
  Page 7:   PS01 Document Management (swimlane lifecycle)
  Page 8:   PS02 Competence Management (swimlane lifecycle)
  Page 9:   PS03 Continuous Improvement (swimlane PDCA)
  Page 10:  General Process Chain — Swimlane 4 lines (SALES/MANUF/DELIV/QUAL)
  Page 11:  CHAIN-01 Existing Product Order (swimlane)
  Page 12:  CHAIN-02 Tooling Modification Order (swimlane)
  Page 13:  CHAIN-03 New Tooling Order (swimlane)
  Page 14:  CHAIN-04 Sourcing Order (swimlane)
  Pages 15-22: BLOC 1-8 Detail (swimlane multi-role, sub-actions clickable)
  Pages 23-30: SUB-BLOC Detail (deepest level, swimlane per action group)
"""

# ── Color palette by role ──────────────────────────────────────────────
C = {
    'dir':   {'fill': '#DAE8FC', 'stroke': '#4472C4', 'font': '#4472C4', 'bg': '#4472C4'},
    'sales': {'fill': '#E2EFDA', 'stroke': '#70AD47', 'font': '#70AD47', 'bg': '#70AD47'},
    'achat': {'fill': '#FFF2CC', 'stroke': '#D6B656', 'font': '#D6B656', 'bg': '#D6B656'},
    'deliv': {'fill': '#E1D5E7', 'stroke': '#9673A6', 'font': '#9673A6', 'bg': '#9673A6'},
    'qual':  {'fill': '#F8CECC', 'stroke': '#B85450', 'font': '#B85450', 'bg': '#B85450'},
    'sup':   {'fill': '#F5F5F5', 'stroke': '#666666', 'font': '#666666', 'bg': '#666666'},
    'chain': {'fill': '#FFF3E0', 'stroke': '#FF8C00', 'font': '#FF8C00', 'bg': '#FF8C00'},
}

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace("'", '&apos;').replace('"', '&quot;')

def cell(id, value, style, x, y, w, h, parent="1"):
    return f'        <mxCell id="{id}" value="{esc(value)}" style="{style}" vertex="1" parent="{parent}"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>\n'

def link_overlay(id, link, x, y, w, h, parent="1"):
    return (f'        <UserObject label="" link="data:page/id,{link}" id="{id}_link">\n'
            f'          <mxCell style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=none;opacity=0;cursor=pointer;" vertex="1" parent="{parent}">\n'
            f'            <mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>\n'
            f'          </mxCell>\n'
            f'        </UserObject>\n')

def edge(id, src, tgt, color, parent="1", dashed=False, label="", width=2):
    dash = "dashed=1;" if dashed else ""
    lbl = esc(label) if label else ""
    font = f"fontSize=9;fontColor={color};" if label else ""
    return (f'        <mxCell id="{id}" value="{lbl}" style="edgeStyle=orthogonalEdgeStyle;strokeColor={color};strokeWidth={width};{dash}{font}" edge="1" source="{src}" target="{tgt}" parent="{parent}">\n'
            f'          <mxGeometry relative="1" as="geometry"></mxGeometry>\n'
            f'        </mxCell>\n')

def edge_pts(id, color, sx, sy, tx, ty, parent="1", dashed=False, label="", width=2, points=None):
    dash = "dashed=1;" if dashed else ""
    lbl = esc(label) if label else ""
    font = f"fontSize=9;fontColor={color};" if label else ""
    pts = ""
    if points:
        pts_xml = "".join(f'<mxPoint x="{px}" y="{py}"/>' for px, py in points)
        pts = f'<Array as="points">{pts_xml}</Array>'
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


# ═══════════════════════════════════════════════════════════════════
# PAGE 1: GLOBAL OVERVIEW — SWIMLANE BY ROLE
# ═══════════════════════════════════════════════════════════════════
def page1_overview():
    o = diagram_start("page-overview", "GLOBAL OVERVIEW v3", dx=2400, dy=1600, pw=2400, ph=1600)
    o += cell("ov_title",
        "<b style='font-size:18px'>QMS MAP ISO 9001:2015</b><br>"
        "Plus Sarl - Industrial follow-up &amp; worldwide sourcing<br>"
        "v0.7 - 2026-03-05<br>"
        "<i style='color:#888'>Click on each element to access details</i>",
        "text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontSize=12;",
        500, 10, 1200, 80)

    # CUSTOMER IN
    o += cell("ov_cin", "<b>CUSTOMERS</b><br>(International)<br><br>Needs<br>Requirements<br>Orders",
        "shape=trapezoid;perimeter=trapezoidPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#E2EFDA;strokeColor=#70AD47;fontSize=11;shadow=1;",
        20, 450, 130, 140)
    # CUSTOMER OUT
    o += cell("ov_cout", "<b>CUSTOMERS</b><br>(International)<br><br>Satisfaction<br>Conforming products<br>On-time delivery",
        "shape=trapezoid;perimeter=trapezoidPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#E2EFDA;strokeColor=#70AD47;fontSize=11;shadow=1;",
        2240, 450, 130, 140)
    # SUPPLIERS
    o += cell("ov_fourn", "<b>SUPPLIERS</b><br>(International)<br><br>Production<br>Delivery",
        "shape=trapezoid;perimeter=trapezoidPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=11;shadow=1;",
        2240, 640, 130, 110)

    sw_x = 170; sw_w = 2050

    # ── SWIMLANE MANAGEMENT ──
    o += cell("sw_dir", "<b>MANAGEMENT</b>",
        f"swimlane;startSize=30;horizontal=1;fillColor={C['dir']['fill']};strokeColor={C['dir']['stroke']};fontStyle=1;fontSize=12;swimlaneLine=1;",
        sw_x, 100, sw_w, 150)
    o += cell("ov_pm01", "<b>PM01</b><br>Leadership &amp; Management<br><i>Policy | Objectives | Risks<br>Management review | KPIs</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['dir']['fill']};strokeColor={C['dir']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        40, 40, 280, 95, parent="sw_dir")
    o += link_overlay("ov_pm01", "page-m1", 40, 40, 280, 95, parent="sw_dir")
    o += cell("ov_ps03", "<b>PS03</b><br>Continuous Improvement<br><i>PDCA | Annual program</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['dir']['fill']};strokeColor={C['dir']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        360, 40, 230, 95, parent="sw_dir")
    o += link_overlay("ov_ps03", "page-s3", 360, 40, 230, 95, parent="sw_dir")
    o += cell("ov_dir_pdca", "PDCA &#8635;",
        f"text;html=1;align=center;fontSize=10;fontColor={C['dir']['font']};fillColor=none;strokeColor=none;fontStyle=2;",
        630, 70, 60, 20, parent="sw_dir")

    # ── SWIMLANE SALES ──
    y_sales = 260; h_sales = 210
    o += cell("sw_sales", "<b>01 SALES — Commercial Role</b>",
        f"swimlane;startSize=30;horizontal=1;fillColor={C['sales']['fill']};strokeColor={C['sales']['stroke']};fontStyle=1;fontSize=12;swimlaneLine=1;",
        sw_x, y_sales, sw_w, h_sales)
    o += cell("ov_p01", "<b>P01</b><br>Commercial<br><i>Quotation | Contract<br>Follow-up | Satisfaction</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['sales']['fill']};strokeColor={C['sales']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        20, 40, 170, 80, parent="sw_sales")
    o += link_overlay("ov_p01", "page-p01", 20, 40, 170, 80, parent="sw_sales")

    bw = 140; bh = 70; by_s = 45
    for bid, bname, bpage, bx in [
        ("ov_b1","BLOC 1<br>Order<br>Reception","page-bloc1", 230),
        ("ov_b2","BLOC 2<br>Order<br>Sheet","page-bloc2", 390),
        ("ov_b5","BLOC 5<br>Order<br>Validation","page-bloc5", 730),
    ]:
        o += cell(bid, f"<b>{bname}</b>",
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['sales']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
            bx, by_s, bw, bh, parent="sw_sales")
        o += link_overlay(bid, bpage, bx, by_s, bw, bh, parent="sw_sales")

    o += cell("ov_b7s", "<b>BLOC 7</b><br><i>Invoice +<br>Customer info</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['sales']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=1;dashed=1;shadow=0;fontSize=9;",
        1200, by_s, 130, bh, parent="sw_sales")
    o += link_overlay("ov_b7s", "page-bloc7", 1200, by_s, 130, bh, parent="sw_sales")
    o += cell("ov_b8s", "<b>BLOC 8</b><br><i>Invoice | Customs<br>Payment | Closure</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['sales']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=1;dashed=1;shadow=0;fontSize=9;",
        1370, by_s, 140, bh, parent="sw_sales")
    o += link_overlay("ov_b8s", "page-bloc8", 1370, by_s, 140, bh, parent="sw_sales")

    o += edge("ov_e_p01_b1", "ov_p01", "ov_b1", C['sales']['stroke'], parent="sw_sales")
    o += edge("ov_e_b1_b2", "ov_b1", "ov_b2", C['sales']['stroke'], parent="sw_sales")
    o += edge("ov_e_b7s_b8s", "ov_b7s", "ov_b8s", C['sales']['stroke'], parent="sw_sales")

    # ── SWIMLANE MANUFACTURE ──
    y_achat = 480; h_achat = 180
    o += cell("sw_achat", "<b>02 MANUFACTURE — Procurement Role</b>",
        f"swimlane;startSize=30;horizontal=1;fillColor={C['achat']['fill']};strokeColor={C['achat']['stroke']};fontStyle=1;fontSize=12;swimlaneLine=1;",
        sw_x, y_achat, sw_w, h_achat)
    o += cell("ov_p02", "<b>P02</b><br>Procurement &amp;<br>Subcontracting<br><i>Evaluation | SQA | Follow-up</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['achat']['fill']};strokeColor={C['achat']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        20, 40, 170, 80, parent="sw_achat")
    o += link_overlay("ov_p02", "page-p02", 20, 40, 170, 80, parent="sw_achat")
    o += cell("ov_b4", "<b>BLOC 4<br>Technical Study<br>Suppliers</b>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['achat']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        550, 45, bw, bh, parent="sw_achat")
    o += link_overlay("ov_b4", "page-bloc4", 550, 45, bw, bh, parent="sw_achat")
    o += cell("ov_b6m", "<b>BLOC 6</b><br><i>Supplier<br>Production</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['achat']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        950, 45, bw, bh, parent="sw_achat")
    o += link_overlay("ov_b6m", "page-bloc6", 950, 45, bw, bh, parent="sw_achat")
    o += edge("ov_e_b4_b6m", "ov_b4", "ov_b6m", C['achat']['stroke'], parent="sw_achat")

    # ── SWIMLANE DELIVERY ──
    y_deliv = 670; h_deliv = 180
    o += cell("sw_deliv", "<b>03 DELIVERY — Logistics Role</b>",
        f"swimlane;startSize=30;horizontal=1;fillColor={C['deliv']['fill']};strokeColor={C['deliv']['stroke']};fontStyle=1;fontSize=12;swimlaneLine=1;",
        sw_x, y_deliv, sw_w, h_deliv)
    o += cell("ov_p04", "<b>P04</b><br>Logistics &amp;<br>Delivery<br><i>Transport | Customs</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['deliv']['fill']};strokeColor={C['deliv']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        20, 40, 170, 80, parent="sw_deliv")
    o += link_overlay("ov_p04", "page-p04", 20, 40, 170, 80, parent="sw_deliv")
    o += cell("ov_b3", "<b>BLOC 3<br>Transport<br>Sheet</b>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['deliv']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        550, 45, bw, bh, parent="sw_deliv")
    o += link_overlay("ov_b3", "page-bloc3", 550, 45, bw, bh, parent="sw_deliv")
    o += cell("ov_b7d", "<b>BLOC 7</b><br><i>Delivery<br>Customs</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['deliv']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        1200, 45, 130, bh, parent="sw_deliv")
    o += link_overlay("ov_b7d", "page-bloc7", 1200, 45, 130, bh, parent="sw_deliv")
    o += edge("ov_e_b3_b7d", "ov_b3", "ov_b7d", C['deliv']['stroke'], parent="sw_deliv")

    # ── SWIMLANE QUALITY ──
    y_qual = 860; h_qual = 180
    o += cell("sw_qual", "<b>04 QUALITY — Quality Role</b>",
        f"swimlane;startSize=30;horizontal=1;fillColor={C['qual']['fill']};strokeColor={C['qual']['stroke']};fontStyle=1;fontSize=12;swimlaneLine=1;",
        sw_x, y_qual, sw_w, h_qual)
    o += cell("ov_p03", "<b>P03</b><br>Quality Control<br><i>IPC | DUPRO | PSI<br>NC | Corrective actions</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['qual']['fill']};strokeColor={C['qual']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        20, 40, 170, 80, parent="sw_qual")
    o += link_overlay("ov_p03", "page-p03", 20, 40, 170, 80, parent="sw_qual")
    o += cell("ov_b6q", "<b>BLOC 6</b><br><i>Conformity<br>Validation</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['qual']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        950, 45, bw, bh, parent="sw_qual")
    o += link_overlay("ov_b6q", "page-bloc6", 950, 45, bw, bh, parent="sw_qual")
    o += cell("ov_b8q", "<b>BLOC 8</b><br><i>Goods<br>Acceptance</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['qual']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        1370, 45, bw, bh, parent="sw_qual")
    o += link_overlay("ov_b8q", "page-bloc8", 1370, 45, bw, bh, parent="sw_qual")
    o += edge("ov_e_b6q_b8q", "ov_b6q", "ov_b8q", C['qual']['stroke'], parent="sw_qual")

    # ── SWIMLANE SUPPORT ──
    o += cell("sw_sup", "<b>SUPPORT</b>",
        f"swimlane;startSize=30;horizontal=1;fillColor={C['sup']['fill']};strokeColor={C['sup']['stroke']};fontStyle=1;fontSize=12;swimlaneLine=1;",
        sw_x, 1050, sw_w, 130)
    o += cell("ov_ps01", "<b>PS01</b><br>Document Management<br><i>Create | Control | Archive</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['sup']['fill']};strokeColor={C['sup']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        20, 40, 230, 75, parent="sw_sup")
    o += link_overlay("ov_ps01", "page-s1", 20, 40, 230, 75, parent="sw_sup")
    o += cell("ov_ps02", "<b>PS02</b><br>Competence Management<br><i>Matrix | Training</i>",
        f"rounded=1;whiteSpace=wrap;html=1;fillColor={C['sup']['fill']};strokeColor={C['sup']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
        280, 40, 230, 75, parent="sw_sup")
    o += link_overlay("ov_ps02", "page-s2", 280, 40, 230, 75, parent="sw_sup")

    # ═══ INTER-SWIMLANE ARROWS ═══
    o += edge_pts("ov_ie_b2_b4", C['chain']['stroke'], 630, 465, 790, 555, dashed=True, label="Manufacturing", points=[(630, 520)])
    o += edge_pts("ov_ie_b2_b3", C['chain']['stroke'], 590, 465, 750, 745, dashed=True, label="Transport")
    o += edge_pts("ov_ie_b4_b5", C['chain']['stroke'], 930, 555, 970, 465, dashed=True, label="Delay feedback", points=[(940, 530), (940, 465)])
    o += edge_pts("ov_ie_b5_b6m", C['chain']['stroke'], 1040, 465, 1190, 555, dashed=True, label="Confirmation")
    o += edge_pts("ov_ie_b6m_b6q", C['chain']['stroke'], 1190, 655, 1190, 935, dashed=True, label="QC Validation", points=[(1190, 760)])
    o += edge_pts("ov_ie_b6q_b7d", C['chain']['stroke'], 1260, 935, 1440, 785, dashed=True, label="Release", points=[(1320, 935), (1320, 785)])
    o += edge_pts("ov_ie_b7d_b7s", C['chain']['stroke'], 1435, 745, 1435, 465, dashed=True, label="Docs")
    o += edge_pts("ov_ie_b8q_b8s", C['chain']['stroke'], 1610, 935, 1610, 465, dashed=True, label="Closure")
    o += edge("ov_e_cin_sw", "ov_cin", "ov_p01", C['sales']['stroke'], width=3)
    o += edge_pts("ov_e_out", C['sales']['stroke'], 2220, 370, 2240, 520, width=3)
    o += edge_pts("ov_e_fourn", C['achat']['stroke'], 2220, 570, 2240, 695, width=2)

    # LEGEND
    ly = 1200
    o += cell("ov_leg_box", "", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;strokeWidth=1;", sw_x, ly, 900, 160)
    o += cell("ov_leg_title", "<b>LEGEND</b>", "text;html=1;align=left;fontSize=11;fillColor=none;strokeColor=none;", sw_x+10, ly+5, 100, 25)
    colors_legend = [
        (C['dir'], "Management — Management Process"), (C['sales'], "Commercial (SALES) — P01"),
        (C['achat'], "Procurement (MANUFACTURE) — P02"), (C['deliv'], "Logistics (DELIVERY) — P04"),
        (C['qual'], "Quality (QUALITY) — P03"), (C['sup'], "Support — PS01, PS02, PS03"),
    ]
    for i, (c, lbl) in enumerate(colors_legend):
        col = 0 if i < 3 else 1
        row = i % 3
        ox = sw_x + 20 + col * 350; oy = ly + 35 + row * 22
        o += cell(f"ov_lc{i}", "", f"rounded=1;fillColor={c['fill']};strokeColor={c['stroke']};", ox, oy, 20, 15)
        o += cell(f"ov_lt{i}", lbl, f"text;html=1;align=left;fontSize=10;fillColor=none;strokeColor=none;", ox+30, oy-2, 280, 20)
    o += cell("ov_lc_ch", "", f"rounded=1;fillColor={C['chain']['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;", sw_x+20, ly+105, 20, 15)
    o += cell("ov_lt_ch", "Orange border = General Process Chain Bloc (clickable)",
        f"text;html=1;align=left;fontSize=10;fillColor=none;strokeColor=none;fontColor={C['chain']['font']};", sw_x+50, ly+103, 400, 20)
    o += cell("ov_lt_note", "<i>Click on each colored block to navigate to the detailed sub-diagram.<br>Orange dashed arrows show the inter-role operational flow.</i>",
        "text;html=1;align=left;fontSize=9;fillColor=none;strokeColor=none;fontColor=#666666;", sw_x+20, ly+130, 600, 30)

    # Nav buttons
    o += nav_button("ov_goto_chain", "View Complete Process Chain &#8594;", "page-chain", sw_x+1550, ly+10, 250, 40, fill=C['chain']['fill'], stroke=C['chain']['stroke'])
    o += nav_button("ov_goto_c1", "CHAIN-01 &#8594;", "page-chain01", sw_x+1550, ly+60, 120, 30, fill=C['chain']['fill'], stroke=C['chain']['stroke'])
    o += nav_button("ov_goto_c2", "CHAIN-02 &#8594;", "page-chain02", sw_x+1680, ly+60, 120, 30, fill=C['chain']['fill'], stroke=C['chain']['stroke'])
    o += nav_button("ov_goto_c3", "CHAIN-03 &#8594;", "page-chain03", sw_x+1550, ly+100, 120, 30, fill=C['chain']['fill'], stroke=C['chain']['stroke'])
    o += nav_button("ov_goto_c4", "CHAIN-04 &#8594;", "page-chain04", sw_x+1680, ly+100, 120, 30, fill=C['chain']['fill'], stroke=C['chain']['stroke'])

    o += diagram_end()
    return o


# ═══════════════════════════════════════════════════════════════════
# PROCESS DETAIL PAGES (swimlane format)
# ═══════════════════════════════════════════════════════════════════
def process_swimlane_page(page_id, name, role, color_key, swimlanes_data, back_link="page-overview", back_label="Back to Overview"):
    """
    swimlanes_data: list of (lane_name, [(step_label, detail), ...])
    Each lane becomes a swimlane row with steps as clickable blocks.
    """
    c = C[color_key]
    o = diagram_start(page_id, name, dx=1800, dy=1200, pw=1800, ph=1200)
    o += back_button(back_link, back_label)
    o += cell("pd_title", f"<b style='font-size:16px'>{esc(name)}</b><br>{esc(role)}<br>ISO 9001:2015",
        "text;html=1;align=center;verticalAlign=middle;fillColor=none;strokeColor=none;fontSize=12;", 400, 15, 800, 60)

    sw_y = 90
    for li, (lane_name, steps) in enumerate(swimlanes_data):
        sh = 160
        o += cell(f"pd_sw{li}", f"<b>{esc(lane_name)}</b>",
            f"swimlane;startSize=25;horizontal=1;fillColor={c['fill']};strokeColor={c['stroke']};fontStyle=1;fontSize=11;swimlaneLine=1;",
            40, sw_y, 1700, sh)
        for i, (label, detail) in enumerate(steps):
            x = 30 + i * 185
            o += cell(f"pd_a{li}_{i}", f"<b>{esc(label)}</b><br><br><i>{esc(detail)}</i>",
                f"rounded=1;whiteSpace=wrap;html=1;fillColor={c['fill']};strokeColor={c['stroke']};fontSize=10;shadow=1;",
                x, 35, 165, 100, parent=f"pd_sw{li}")
            if i > 0:
                o += edge(f"pd_e{li}_{i}", f"pd_a{li}_{i-1}", f"pd_a{li}_{i}", c['stroke'], parent=f"pd_sw{li}")
        sw_y += sh + 15

    o += diagram_end()
    return o


def page2_m1():
    return process_swimlane_page("page-m1", "PM01 - Leadership & Management", "Management", "dir", [
        ("PLAN", [
            ("Analyze context", "(§4.1) Interested parties\nInternal/external issues"),
            ("Define policy", "(§5.2) Management commitment\nCustomer focus"),
            ("Set objectives", "(§6.2) Measurable, consistent\nwith policy"),
            ("Allocate resources", "(§7.1) Human, material\nfinancial"),
        ]),
        ("DO", [
            ("Deploy policy", "Communicate to all roles\nEnsure understanding"),
            ("Manage risks", "(§6.1) Risk matrix\nOpportunities"),
            ("Conduct reviews", "(§9.3) Periodic review\nDecisions"),
        ]),
        ("CHECK", [
            ("Monitor KPIs", "(§9.1) Dashboards\nPerformance monitoring"),
            ("Internal audits", "(§9.2) Audit program\nFindings"),
        ]),
        ("ACT", [
            ("Improve", "(§10.3) PDCA\nPreventive actions"),
            ("Update objectives", "Based on review results\nNew targets"),
        ]),
    ])

def page3_p01():
    return process_swimlane_page("page-p01", "P01 - Commercial", "Commercial Role", "sales", [
        ("REQUEST PHASE", [
            ("Request reception", "Email / phone\nCRM registration"),
            ("Feasibility analysis", "Technical verification\nSupplier capacity"),
            ("Quotation", "Price, deadline, conditions\nSent to customer"),
        ]),
        ("ORDER PHASE", [
            ("Contract review", "(§8.2.3) Validate requirements\nCommercial agreement"),
            ("Confirmed order", "PO received\nProcess launch"),
            ("Order follow-up", "Dashboard\nCustomer communication"),
        ]),
        ("COMPLETION PHASE", [
            ("Invoicing", "Customer invoice\nCustoms declaration"),
            ("Satisfaction", "Customer survey\nFeedback analysis"),
        ]),
    ])

def page4_p02():
    return process_swimlane_page("page-p02", "P02 - Procurement & Subcontracting", "Procurement Role", "achat", [
        ("SELECTION", [
            ("Identify suppliers", "Market research\nSelection criteria"),
            ("Evaluate & qualify", "Supplier audit\nEvaluation grid"),
            ("Sign SQA", "Supplier Quality Agreement\n(FM-P02-AQF)"),
        ]),
        ("ORDERING", [
            ("Issue order", "Supplier PO\nSpecifications"),
            ("Track production", "Supplier contact\nProduction status"),
        ]),
        ("MONITORING", [
            ("Re-evaluate suppliers", "Annual review\nQCDM rating"),
            ("Manage supplier NCs", "NC sheets\nAction follow-up"),
            ("Panel A/B/C", "Supplier classification"),
        ]),
    ])

def page5_p03():
    return process_swimlane_page("page-p03", "P03 - Quality Control", "Quality Role", "qual", [
        ("PLANNING", [
            ("Plan QC", "Inspection planning\nAssignment"),
        ]),
        ("INSPECTIONS", [
            ("IPC", "Initial Production\nCheck"),
            ("DUPRO", "During Production\nInspection"),
            ("PSI", "Pre-Shipment\nInspection"),
            ("Loading Check", "Container loading\nControl"),
        ]),
        ("NC MANAGEMENT", [
            ("Detect NC", "Non-conformities\nInspection report"),
            ("Process NC", "Accept / rework\nreject"),
            ("Corrective actions", "Root cause\nAction plan"),
        ]),
    ])

def page6_p04():
    return process_swimlane_page("page-p04", "P04 - Logistics & Delivery", "Logistics Role", "deliv", [
        ("PREPARATION", [
            ("Plan shipment", "Date, volume\nTransport mode"),
            ("Carrier selection", "Transport quotation\nProvider choice"),
            ("Transport documents", "BL, packing list\nCertificates"),
        ]),
        ("EXECUTION", [
            ("Shipment tracking", "Tracking\nCommunication"),
            ("Customs management", "Customs declaration\nCustoms agent"),
        ]),
        ("COMPLETION", [
            ("Delivery confirmation", "Customer receipt\nProof of delivery"),
            ("Archiving", "Complete file\nDocument retention"),
        ]),
    ])

def page7_s1():
    return process_swimlane_page("page-s1", "PS01 - Document Management", "Support", "sup", [
        ("CREATION", [
            ("Create documents", "Procedures, forms\nInstructions"),
            ("Verify & approve", "Technical review\nManagement approval"),
        ]),
        ("DISTRIBUTION", [
            ("Distribute", "Making available\nCommunication"),
            ("Version control", "Revision index\nChange history"),
        ]),
        ("RETENTION", [
            ("Archive", "Retention\nRetention period"),
            ("Audit conformity", "Verification\nDocument gaps"),
            ("Improve doc. system", "User feedback\nSimplification"),
        ]),
    ])

def page8_s2():
    return process_swimlane_page("page-s2", "PS02 - Competence Management", "Support", "sup", [
        ("IDENTIFICATION", [
            ("Define competences", "Role requirements\nCompetence matrix"),
            ("Assess gaps", "Current vs required\nGap analysis"),
        ]),
        ("DEVELOPMENT", [
            ("Training plan", "Annual program\nPriorities"),
            ("Deliver training", "Internal / external\nOn-the-job"),
        ]),
        ("EVALUATION", [
            ("Assess effectiveness", "Post-training eval\nPerformance review"),
            ("Update matrix", "Record evidence\nMaintain records"),
        ]),
    ])

def page9_s3():
    return process_swimlane_page("page-s3", "PS03 - Continuous Improvement", "Management", "dir", [
        ("PLAN", [
            ("Collect data", "KPIs, audits, NCs\nCustomer feedback"),
            ("Analyze trends", "Statistical analysis\nPareto, root cause"),
        ]),
        ("DO", [
            ("Define actions", "Improvement projects\nResource allocation"),
            ("Implement", "Execute action plan\nMonitor progress"),
        ]),
        ("CHECK & ACT", [
            ("Verify effectiveness", "Measure results\nCompare targets"),
            ("Standardize", "Update procedures\nShare best practices"),
            ("Annual review", "Program assessment\nNew objectives"),
        ]),
    ])


# ═══════════════════════════════════════════════════════════════════
# PAGE 10: GENERAL PROCESS CHAIN
# ═══════════════════════════════════════════════════════════════════
def page10_chain():
    o = diagram_start("page-chain", "General Process Chain", dx=1800, dy=1000, pw=1800, ph=1000)
    o += back_button()
    o += cell("ch_title",
        "<b style='font-size:16px'>GENERAL PROCESS CHAIN</b><br>"
        "4 Order Types — Click on each BLOC for details<br>"
        "<i style='color:#888'>Click on each BLOC to view details</i>",
        "text;html=1;align=center;verticalAlign=middle;fillColor=none;strokeColor=none;fontSize=12;", 400, 10, 800, 60)

    o += cell("ch_cin", "<b>CUSTOMER</b><br>Order", "shape=trapezoid;perimeter=trapezoidPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#E2EFDA;strokeColor=#70AD47;fontSize=10;shadow=1;", 20, 175, 100, 60)

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

    blocs = [
        ("ch_b1", "B1\nOrder\nReception", "ch_sw_s", 40, 35, 120, 60, "page-bloc1", C['sales']),
        ("ch_b2", "B2\nOrder\nSheet", "ch_sw_s", 190, 35, 120, 60, "page-bloc2", C['sales']),
        ("ch_b5", "B5\nOrder\nValidation", "ch_sw_s", 530, 35, 120, 60, "page-bloc5", C['sales']),
        ("ch_b7s", "B7 (Sales)\nInvoice\nCustomer info", "ch_sw_s", 900, 35, 110, 60, "page-bloc7", C['sales']),
        ("ch_b8s", "B8 (Sales)\nInvoice\nClosure", "ch_sw_s", 1050, 35, 110, 60, "page-bloc8", C['sales']),
        ("ch_b4", "B4\nTechnical Study\nSuppliers", "ch_sw_m", 340, 35, 120, 60, "page-bloc4", C['achat']),
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

    # Inter-lane arrows
    o += edge_pts("ch_ie1", C['chain']['stroke'], 390, 295, 510, 345, dashed=True, label="Manufacturing")
    o += edge_pts("ch_ie2", C['chain']['stroke'], 370, 295, 510, 525, dashed=True, label="Transport")
    o += edge_pts("ch_ie3", C['chain']['stroke'], 600, 345, 670, 160, dashed=True, label="Delay feedback", points=[(620, 300), (640, 300), (640, 160)])
    o += edge_pts("ch_ie4", C['chain']['stroke'], 790, 200, 840, 345, dashed=True, label="Confirmation")
    o += edge_pts("ch_ie5", C['chain']['stroke'], 900, 410, 900, 705, dashed=True, label="QC Validation", points=[(900, 550)])
    o += edge_pts("ch_ie6", C['chain']['stroke'], 960, 720, 1040, 560, dashed=True, label="Release", points=[(980, 680), (980, 560)])
    o += edge_pts("ch_ie7", C['chain']['stroke'], 1080, 530, 1060, 195, dashed=True, label="Docs")
    o += edge_pts("ch_ie8", C['chain']['stroke'], 1210, 720, 1190, 195, dashed=True, label="Closure")
    o += edge_pts("ch_e_cin", C['sales']['stroke'], 120, 205, 180, 160, width=3)
    o += cell("ch_cout", "<b>CUSTOMER</b><br>Product delivered", "shape=trapezoid;perimeter=trapezoidPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#E2EFDA;strokeColor=#70AD47;fontSize=10;shadow=1;", 1670, 175, 100, 60)
    o += edge_pts("ch_e_cout", C['sales']['stroke'], 1300, 160, 1670, 205, width=3)

    # Chain type nav buttons
    o += nav_button("ch_c1", "CHAIN-01 Existing Product &#8594;", "page-chain01", 140, 860, 200, 30, fill=C['chain']['fill'], stroke=C['chain']['stroke'])
    o += nav_button("ch_c2", "CHAIN-02 Tooling Modif. &#8594;", "page-chain02", 360, 860, 200, 30, fill=C['chain']['fill'], stroke=C['chain']['stroke'])
    o += nav_button("ch_c3", "CHAIN-03 New Tooling &#8594;", "page-chain03", 580, 860, 200, 30, fill=C['chain']['fill'], stroke=C['chain']['stroke'])
    o += nav_button("ch_c4", "CHAIN-04 Sourcing &#8594;", "page-chain04", 800, 860, 200, 30, fill=C['chain']['fill'], stroke=C['chain']['stroke'])

    o += diagram_end()
    return o


# ═══════════════════════════════════════════════════════════════════
# PAGES 11-14: CHAIN DETAIL PAGES (swimlane)
# ═══════════════════════════════════════════════════════════════════
def chain_detail_page(page_id, chain_num, chain_title, blocs_by_lane, status="Active"):
    o = diagram_start(page_id, f"CHAIN-0{chain_num} {chain_title}", dx=1800, dy=900, pw=1800, ph=900)
    o += back_button("page-chain", "Back to Chain")
    o += nav_button("cn_ov", "Overview", "page-overview", 230, 20, 100, 35)
    o += cell("cn_title",
        f"<b style='font-size:16px'>CHAIN-0{chain_num} — {esc(chain_title)}</b><br>Status: {status}",
        "text;html=1;align=center;verticalAlign=middle;fillColor=none;strokeColor=none;fontSize=12;", 400, 10, 800, 50)

    sw_y = 75
    lane_defs = [("SALES", "sales"), ("MANUFACTURE", "achat"), ("DELIVERY", "deliv"), ("QUALITY", "qual")]
    for lane_name, lane_key in lane_defs:
        c = C[lane_key]
        blocs = blocs_by_lane.get(lane_key, [])
        if not blocs:
            continue
        sh = 130
        lid = f"cn_sw_{lane_key}"
        o += cell(lid, f"<b>{lane_name}</b>",
            f"swimlane;startSize=25;horizontal=1;fillColor={c['fill']};strokeColor={c['stroke']};fontStyle=1;fontSize=11;swimlaneLine=1;",
            40, sw_y, 1700, sh)
        for i, (bname, bpage) in enumerate(blocs):
            bx = 30 + i * 200
            o += cell(f"cn_b_{lane_key}_{i}", f"<b>{esc(bname)}</b>",
                f"rounded=1;whiteSpace=wrap;html=1;fillColor={c['fill']};strokeColor={C['chain']['stroke']};strokeWidth=2;shadow=1;fontSize=10;",
                bx, 35, 175, 70, parent=lid)
            o += link_overlay(f"cn_b_{lane_key}_{i}", bpage, bx, 35, 175, 70, parent=lid)
            if i > 0:
                o += edge(f"cn_e_{lane_key}_{i}", f"cn_b_{lane_key}_{i-1}", f"cn_b_{lane_key}_{i}", c['stroke'], parent=lid)
        sw_y += sh + 10

    o += diagram_end()
    return o

def page11_chain01():
    return chain_detail_page("page-chain01", 1, "Existing Product Order", {
        "sales": [("B1 Order Reception", "page-bloc1"), ("B2 Order Sheet", "page-bloc2"), ("B5 Order Validation", "page-bloc5"), ("B7 Invoice", "page-bloc7"), ("B8 Closure", "page-bloc8")],
        "achat": [("B4 Technical Study", "page-bloc4"), ("B6 Production", "page-bloc6")],
        "deliv": [("B3 Transport Sheet", "page-bloc3"), ("B7 Delivery & Customs", "page-bloc7")],
        "qual": [("B6 Conformity", "page-bloc6"), ("B8 Acceptance", "page-bloc8")],
    })

def page12_chain02():
    return chain_detail_page("page-chain02", 2, "Tooling Modification Order", {
        "sales": [("B1 Order Reception", "page-bloc1"), ("B2 Order Sheet", "page-bloc2"), ("B5 Order Validation", "page-bloc5"), ("B8 Closure", "page-bloc8")],
        "achat": [("B4 Technical Study\n+ Tooling specs", "page-bloc4"), ("B6 Modif. Production", "page-bloc6")],
        "qual": [("B6 Validation\n+ Tooling check", "page-bloc6"), ("B8 Acceptance", "page-bloc8")],
    }, status="Active")

def page13_chain03():
    return chain_detail_page("page-chain03", 3, "New Tooling Order", {
        "sales": [("B1 Order Reception", "page-bloc1"), ("B2 Order Sheet", "page-bloc2"), ("B5 Order Validation", "page-bloc5"), ("B8 Closure", "page-bloc8")],
        "achat": [("B4 Technical Study\n+ New tooling design", "page-bloc4"), ("B6 Tooling Production", "page-bloc6")],
        "qual": [("B6 Tooling Validation", "page-bloc6"), ("B8 Acceptance", "page-bloc8")],
    }, status="Active")

def page14_chain04():
    return chain_detail_page("page-chain04", 4, "Sourcing Order", {
        "sales": [("B1 Order Reception", "page-bloc1"), ("B2 Sourcing Brief", "page-bloc2"), ("B5 Proposal Validation", "page-bloc5"), ("B8 Closure", "page-bloc8")],
        "achat": [("B4 Supplier Research\n+ Samples", "page-bloc4"), ("B6 Sample Production", "page-bloc6")],
        "qual": [("B6 Sample Validation", "page-bloc6"), ("B8 Final Acceptance", "page-bloc8")],
    }, status="Active")


# ═══════════════════════════════════════════════════════════════════
# PAGES 15-22: BLOC DETAIL PAGES (swimlane multi-role)
# ═══════════════════════════════════════════════════════════════════
def bloc_detail_page(page_id, bloc_num, bloc_title, bloc_ref, roles, actions_by_role,
                     prev_bloc=None, next_bloc=None, iso_clause="", doc_refs=None, sub_page=None):
    o = f'  <!-- PAGE: BLOC {bloc_num} -->\n'
    o += diagram_start(page_id, f"BLOC {bloc_num} - {bloc_title}", dx=1800, dy=1000, pw=1800, ph=1000)
    o += back_button("page-chain", "Back to Chain")
    o += nav_button("bn_ov", "Overview", "page-overview", 230, 20, 100, 35)
    o += cell("bt_title",
        f"<b style='font-size:16px'>BLOC {bloc_num} — {esc(bloc_title)}</b><br>"
        f"<i>{esc(bloc_ref)}</i>"
        f"{'<br>ISO 9001: ' + esc(iso_clause) if iso_clause else ''}",
        "text;html=1;align=center;verticalAlign=middle;fillColor=none;strokeColor=none;fontSize=12;", 400, 10, 800, 65)

    sw_y = 85
    for ri, (rname, rkey) in enumerate(roles):
        c = C[rkey]
        actions = actions_by_role.get(rkey, [])
        sh = 160
        o += cell(f"bt_sw{ri}", f"<b>{esc(rname)}</b>",
            f"swimlane;startSize=25;horizontal=1;fillColor={c['fill']};strokeColor={c['stroke']};fontStyle=1;fontSize=11;swimlaneLine=1;",
            40, sw_y, 1700, sh)
        for i, (aname, adetail) in enumerate(actions):
            x = 30 + i * 195
            aid = f"bt_a{ri}_{i}"
            o += cell(aid, f"<b>{esc(aname)}</b><br><br><i>{esc(adetail)}</i>",
                f"rounded=1;whiteSpace=wrap;html=1;fillColor={c['fill']};strokeColor={c['stroke']};fontSize=10;shadow=1;",
                x, 35, 175, 100, parent=f"bt_sw{ri}")
            if sub_page and i == 0:
                o += link_overlay(aid, sub_page, x, 35, 175, 100, parent=f"bt_sw{ri}")
            if i > 0:
                o += edge(f"bt_e{ri}_{i}", f"bt_a{ri}_{i-1}", f"bt_a{ri}_{i}", c['stroke'], parent=f"bt_sw{ri}")
        sw_y += sh + 10

    if doc_refs:
        doc_y = sw_y + 10
        o += cell("bt_docs", "<b>Associated documents:</b><br>" + "<br>".join(esc(d) for d in doc_refs),
            "text;html=1;align=left;fontSize=10;fillColor=#FAFAFA;strokeColor=#CCCCCC;rounded=1;",
            40, doc_y, 500, 20 + len(doc_refs) * 18)

    nav_y = 900
    if prev_bloc:
        o += nav_button("bn_prev", f"&larr; BLOC {bloc_num-1}", prev_bloc, 40, nav_y, 130, 30)
    if next_bloc:
        o += nav_button("bn_next", f"BLOC {bloc_num+1} &rarr;", next_bloc, 1600, nav_y, 130, 30)

    o += diagram_end()
    return o


def page15_bloc1():
    return bloc_detail_page("page-bloc1", 1, "ORDER RECEPTION", "CH-BLOC-001",
        [("Commercial Role (SALES)", "sales")],
        {"sales": [
            ("Download order", "Register in\nORDER_20XX"),
            ("Identify type", "4 order types\n(existing product,\ntooling modif.,\nnew tooling,\nsourcing)"),
            ("Route to\nappropriate chain", "CHAIN-01, 02, 03\nor 04"),
        ]},
        next_bloc="page-bloc2", iso_clause="8.2.1",
        doc_refs=["ORDER_20XX folder", "CHAIN-01 to CHAIN-04"],
        sub_page="page-sub-b1")

def page16_bloc2():
    return bloc_detail_page("page-bloc2", 2, "ORDER SHEET CREATION", "CH-BLOC-002",
        [("Commercial Role (SALES)", "sales")],
        {"sales": [
            ("Create order\nsheet", "New order\nfolder"),
            ("Add PDF\norder", "Original customer\ndocument"),
            ("Customer, date,\ndeadline", "Identification\ninformation"),
            ("Product selection", "Existing product\nlibrary"),
            ("Ordered quantity", "Volume and\nunits"),
            ("Final quantity\n= identical", "Consistency\nverification"),
            ("Order reference\n= customer ref.", "Customer\ntraceability"),
        ]},
        prev_bloc="page-bloc1", next_bloc="page-bloc3", iso_clause="8.2.2, 8.2.3",
        doc_refs=["Internal order sheet", "Customer PO (PDF)", "Product library"],
        sub_page="page-sub-b2")

def page17_bloc3():
    return bloc_detail_page("page-bloc3", 3, "TRANSPORT SHEET CREATION", "CH-BLOC-003",
        [("Logistics Role (DELIVERY)", "deliv")],
        {"deliv": [
            ("Create transport sheet", "New or add\nto existing"),
            ("Delay validation", "Confirmed by\nthe carrier"),
            ("Delivery type", "Maritime, air,\nroad, express"),
        ]},
        prev_bloc="page-bloc2", next_bloc="page-bloc4", iso_clause="8.5.4",
        doc_refs=["Transport sheet", "Carrier quotation"])

def page18_bloc4():
    return bloc_detail_page("page-bloc4", 4, "TECHNICAL STUDY SUPPLIERS", "CH-BLOC-004",
        [("Procurement Role (MANUFACTURE)", "achat")],
        {"achat": [
            ("Define order\nstatus", "Drop-down list\n(in progress, validated, etc.)"),
            ("Send info to\nsuppliers", "Technical\nspecifications required"),
            ("Production deadline\nvalidation", "Confirmed by\nthe supplier"),
        ]},
        prev_bloc="page-bloc3", next_bloc="page-bloc5", iso_clause="8.4.2, 8.4.3",
        doc_refs=["Technical specifications", "Supplier deadline confirmation"])

def page19_bloc5():
    return bloc_detail_page("page-bloc5", 5, "ORDER VALIDATION", "CH-BLOC-005",
        [("Commercial Role (SALES)", "sales")],
        {"sales": [
            ("Print AR", "Acknowledgment of receipt\nfor validation"),
            ("Send AR\nto customer", "With delivery deadline\nand confirmed price"),
            ("Customer feedback", "Acceptance\nor Rejection"),
        ]},
        prev_bloc="page-bloc4", next_bloc="page-bloc6", iso_clause="8.2.3.1",
        doc_refs=["Acknowledgment of receipt (AR)", "Signed customer confirmation"])

def page20_bloc6():
    return bloc_detail_page("page-bloc6", 6, "PRODUCTION & QUALITY", "CH-BLOC-006",
        [("Procurement Role (MANUFACTURE)", "achat"), ("Quality Role (QUALITY)", "qual")],
        {"achat": [
            ("Production\nconfirmation", "Email to supplier\nGO production"),
            ("Progress tracking", "Regular contact\nsupplier"),
        ],
        "qual": [
            ("Plan inspections", "IPC / DUPRO / PSI\nper quality plan"),
            ("Conformity validation", "Quality control\nsupplier"),
            ("Release decision", "Conforming: release\nNC: process"),
        ]},
        prev_bloc="page-bloc5", next_bloc="page-bloc7", iso_clause="8.5.1, 8.6, 8.7",
        doc_refs=["Inspection report (IPC/DUPRO/PSI)", "NC sheet (FM-P04-NC)", "Supplier Quality Agreement"],
        sub_page="page-sub-b6")

def page21_bloc7():
    return bloc_detail_page("page-bloc7", 7, "DELIVERY & CUSTOMS", "CH-BLOC-007",
        [("Logistics Role (DELIVERY)", "deliv"), ("Commercial Role (SALES)", "sales")],
        {"deliv": [
            ("Create delivery\nnote", "BL / Packing List"),
            ("Supplier\nspecifics", "Deadlines, holidays\nconditions"),
            ("Shipment tracking", "Tracking with\ncarrier"),
            ("Customs tracking", "Carrier +\ncustoms agent"),
        ],
        "sales": [
            ("Commercial invoice", "To carrier\nfor clearance"),
            ("Inform customer", "Delivery date\nconfirmed"),
        ]},
        prev_bloc="page-bloc6", next_bloc="page-bloc8", iso_clause="8.5.4, 8.5.5",
        doc_refs=["Delivery note (BL)", "Packing list", "Commercial invoice", "Customs documents"])

def page22_bloc8():
    return bloc_detail_page("page-bloc8", 8, "GOODS ACCEPTANCE & CLOSURE", "CH-BLOC-008",
        [("Quality Role (QUALITY)", "qual"), ("Commercial Role (SALES)", "sales")],
        {"qual": [
            ("Confirmation email\nconformity", "To customer\ninspection result"),
        ],
        "sales": [
            ("Send invoice\nto customer", "Final invoice"),
            ("Customs\ndeclaration", "Administrative\ndocuments"),
            ("Customer payment", "Collection follow-up"),
            ("Close file", "Complete\narchiving"),
        ]},
        prev_bloc="page-bloc7", iso_clause="8.5.5, 9.1.2",
        doc_refs=["Customer invoice", "Customs declaration", "Satisfaction survey (FM-P01-SAT)", "Archived file"])


# ═══════════════════════════════════════════════════════════════════
# PAGES 23-30: SUB-BLOC DETAIL PAGES (deepest level)
# ═══════════════════════════════════════════════════════════════════
def sub_bloc_page(page_id, bloc_num, sub_title, back_page, swimlanes_data, color_key, iso_clause=""):
    c = C[color_key]
    o = diagram_start(page_id, f"SUB-BLOC {bloc_num} - {sub_title}", dx=1800, dy=1000, pw=1800, ph=1000)
    o += back_button(back_page, f"Back to BLOC {bloc_num}")
    o += nav_button("sb_ov", "Overview", "page-overview", 230, 20, 100, 35)
    o += nav_button("sb_ch", "Chain", "page-chain", 340, 20, 80, 35)
    o += cell("sb_title",
        f"<b style='font-size:14px'>BLOC {bloc_num} — {esc(sub_title)}</b><br>"
        f"<i>Detailed sub-actions</i>"
        f"{'<br>ISO 9001: ' + esc(iso_clause) if iso_clause else ''}",
        "text;html=1;align=center;verticalAlign=middle;fillColor=none;strokeColor=none;fontSize=11;", 450, 10, 700, 55)

    sw_y = 80
    for li, (lane_name, steps) in enumerate(swimlanes_data):
        sh = 150
        o += cell(f"sb_sw{li}", f"<b>{esc(lane_name)}</b>",
            f"swimlane;startSize=25;horizontal=1;fillColor={c['fill']};strokeColor={c['stroke']};fontStyle=1;fontSize=10;swimlaneLine=1;",
            40, sw_y, 1700, sh)
        for i, (label, detail) in enumerate(steps):
            x = 20 + i * 170
            o += cell(f"sb_a{li}_{i}", f"<b>{esc(label)}</b><br><i>{esc(detail)}</i>",
                f"rounded=1;whiteSpace=wrap;html=1;fillColor={c['fill']};strokeColor={c['stroke']};fontSize=9;shadow=1;",
                x, 30, 155, 95, parent=f"sb_sw{li}")
            if i > 0:
                o += edge(f"sb_e{li}_{i}", f"sb_a{li}_{i-1}", f"sb_a{li}_{i}", c['stroke'], parent=f"sb_sw{li}")
        sw_y += sh + 10

    o += diagram_end()
    return o

def page23_sub_b1():
    return sub_bloc_page("page-sub-b1", 1, "Order Reception — Details", "page-bloc1", [
        ("RECEPTION", [
            ("Open email", "Check inbox\nDaily review"),
            ("Download PO", "Save to\nORDER_20XX folder"),
            ("Log in CRM", "Create entry\nCustomer reference"),
        ]),
        ("CLASSIFICATION", [
            ("Read specifications", "Product type\nQuantities\nDeadlines"),
            ("Identify order type", "Type 1: Existing\nType 2: Modif.\nType 3: New\nType 4: Sourcing"),
            ("Assign to chain", "Route to\nCHAIN-01/02/03/04"),
            ("Notify team", "Email to roles\nDeadline alert"),
        ]),
    ], "sales", iso_clause="8.2.1")

def page24_sub_b2():
    return sub_bloc_page("page-sub-b2", 2, "Order Sheet — Details", "page-bloc2", [
        ("DATA ENTRY", [
            ("Create folder", "New order folder\nNaming convention"),
            ("Attach PO PDF", "Original customer\ndocument"),
            ("Enter customer data", "Name, contact\nDelivery address"),
            ("Set deadline", "Requested date\nBuffer calculation"),
        ]),
        ("PRODUCT DETAILS", [
            ("Select product", "From library\nExisting reference"),
            ("Enter quantities", "Ordered qty\nUnit of measure"),
            ("Verify consistency", "Final qty = ordered\nRef = customer ref"),
            ("Generate order ref", "Internal reference\nSequential number"),
        ]),
    ], "sales", iso_clause="8.2.2, 8.2.3")

def page25_sub_b6():
    return sub_bloc_page("page-sub-b6", 6, "Production & Quality — Details", "page-bloc6", [
        ("PRODUCTION LAUNCH", [
            ("Send GO email", "To supplier\nWith specifications"),
            ("Confirm deadlines", "Production schedule\nMilestones"),
            ("Track progress", "Weekly contact\nStatus updates"),
        ]),
        ("QUALITY INSPECTIONS", [
            ("Schedule IPC", "Initial check\nFirst articles"),
            ("Conduct DUPRO", "During production\nSampling plan"),
            ("Execute PSI", "Pre-shipment\n100% or AQL"),
            ("Loading check", "Container loading\nFinal verification"),
        ]),
        ("RELEASE DECISION", [
            ("Review reports", "All inspection\nresults compiled"),
            ("Conforming?", "Yes: Release\nNo: NC process"),
            ("Issue release", "Authorization to\nship goods"),
        ]),
    ], "qual", iso_clause="8.5.1, 8.6, 8.7")

def page26_sub_b3():
    return sub_bloc_page("page-sub-b3", 3, "Transport Sheet — Details", "page-bloc3", [
        ("CREATION", [
            ("Open transport form", "Template or\nexisting sheet"),
            ("Enter shipment data", "Origin, destination\nWeight, volume"),
            ("Select transport mode", "Sea / Air / Road\nExpress / Combined"),
        ]),
        ("VALIDATION", [
            ("Request carrier quote", "Multiple quotes\nCompare options"),
            ("Confirm deadline", "Carrier confirmation\nTransit time"),
            ("Finalize sheet", "Approved by\nlogistics role"),
        ]),
    ], "deliv", iso_clause="8.5.4")

def page27_sub_b4():
    return sub_bloc_page("page-sub-b4", 4, "Technical Study — Details", "page-bloc4", [
        ("PREPARATION", [
            ("Review order specs", "Customer requirements\nTechnical drawings"),
            ("Define status", "In progress / Validated\nOn hold / Cancelled"),
        ]),
        ("SUPPLIER ENGAGEMENT", [
            ("Send RFQ", "To qualified suppliers\nWith specifications"),
            ("Receive quotes", "Price, deadline\nCapacity confirmation"),
            ("Compare offers", "Technical + commercial\nEvaluation matrix"),
        ]),
        ("VALIDATION", [
            ("Select supplier", "Best offer\nQCDM criteria"),
            ("Confirm deadline", "Production timeline\nFeedback to SALES"),
        ]),
    ], "achat", iso_clause="8.4.2, 8.4.3")

def page28_sub_b5():
    return sub_bloc_page("page-sub-b5", 5, "Order Validation — Details", "page-bloc5", [
        ("PREPARATION", [
            ("Compile data", "Price confirmed\nDeadline confirmed\nSpecs validated"),
            ("Generate AR", "Acknowledgment\nof receipt document"),
        ]),
        ("CUSTOMER INTERACTION", [
            ("Send AR to customer", "Email with AR\nDelivery date + price"),
            ("Await response", "Track response\nFollow-up if needed"),
            ("Process response", "Accept: proceed\nReject: negotiate"),
        ]),
    ], "sales", iso_clause="8.2.3.1")

def page29_sub_b7():
    return sub_bloc_page("page-sub-b7", 7, "Delivery & Customs — Details", "page-bloc7", [
        ("SHIPPING DOCS", [
            ("Create BL", "Bill of Lading\nShipping details"),
            ("Packing list", "Item details\nWeight/dimensions"),
            ("Commercial invoice", "For customs\nclearance"),
        ]),
        ("TRACKING", [
            ("Monitor shipment", "Carrier tracking\nETD/ETA updates"),
            ("Customs process", "Agent coordination\nDuty/tax handling"),
            ("Inform customer", "Delivery date\nTracking number"),
        ]),
    ], "deliv", iso_clause="8.5.4, 8.5.5")

def page30_sub_b8():
    return sub_bloc_page("page-sub-b8", 8, "Goods Acceptance — Details", "page-bloc8", [
        ("QUALITY CONFIRMATION", [
            ("Send conformity email", "Inspection results\nTo customer"),
            ("Resolve any issues", "If NC detected\nCorrective actions"),
        ]),
        ("COMMERCIAL CLOSURE", [
            ("Issue final invoice", "To customer\nPayment terms"),
            ("Customs declaration", "Administrative docs\nArchive"),
            ("Track payment", "Follow-up\nCollection"),
            ("Close order file", "Complete dossier\nArchive per PS01"),
        ]),
        ("SATISFACTION", [
            ("Send survey", "FM-P01-SAT\nCustomer feedback"),
            ("Analyze results", "Improve process\nFeed into PS03"),
        ]),
    ], "sales", iso_clause="8.5.5, 9.1.2")


# ═══════════════════════════════════════════════════════════════════
# FINAL ASSEMBLY
# ═══════════════════════════════════════════════════════════════════
def generate():
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<mxfile host="app.diagrams.net" modified="2026-03-05T18:00:00.000Z" agent="Claude" version="21.0.0" type="device">\n'

    # Page 1: Global Overview
    xml += page1_overview()
    # Pages 2-9: Process Details (swimlane)
    xml += page2_m1()
    xml += page3_p01()
    xml += page4_p02()
    xml += page5_p03()
    xml += page6_p04()
    xml += page7_s1()
    xml += page8_s2()
    xml += page9_s3()
    # Page 10: General Process Chain
    xml += page10_chain()
    # Pages 11-14: Chain Details
    xml += page11_chain01()
    xml += page12_chain02()
    xml += page13_chain03()
    xml += page14_chain04()
    # Pages 15-22: Bloc Details
    xml += page15_bloc1()
    xml += page16_bloc2()
    xml += page17_bloc3()
    xml += page18_bloc4()
    xml += page19_bloc5()
    xml += page20_bloc6()
    xml += page21_bloc7()
    xml += page22_bloc8()
    # Pages 23-30: Sub-Bloc Details
    xml += page23_sub_b1()
    xml += page24_sub_b2()
    xml += page25_sub_b6()
    xml += page26_sub_b3()
    xml += page27_sub_b4()
    xml += page28_sub_b5()
    xml += page29_sub_b7()
    xml += page30_sub_b8()

    xml += '</mxfile>\n'
    return xml


if __name__ == "__main__":
    import os
    output_path = os.path.join(os.path.dirname(__file__), "vue_ensemble_interactive_v3.drawio")
    content = generate()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: {output_path}")
    print(f"  Pages: 30")
    print(f"  Size: {len(content):,} bytes")
