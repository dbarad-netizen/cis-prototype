from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

ACCENT=colors.HexColor("#1f5fbf"); INK=colors.HexColor("#1a1f2b"); MUTE=colors.HexColor("#5b6473")
RULE=colors.HexColor("#d7dce4"); BOXBG=colors.HexColor("#eef3fb"); GOODBG=colors.HexColor("#e8f6ef")
styles=getSampleStyleSheet()
def S(n,**kw):
    base=kw.pop("parent",styles["Normal"]); return ParagraphStyle(n,parent=base,**kw)
body=S("body",fontName="Helvetica",fontSize=8.7,leading=11.6,textColor=INK)
h2=S("h2",fontName="Helvetica-Bold",fontSize=9.4,leading=11,textColor=ACCENT,spaceBefore=7,spaceAfter=2.5)
title=S("title",fontName="Helvetica-Bold",fontSize=20,leading=21,textColor=INK,spaceAfter=1)
promise=S("promise",fontName="Helvetica-Bold",fontSize=11,leading=13,textColor=ACCENT,spaceAfter=1)
sub=S("sub",fontName="Helvetica",fontSize=8.6,leading=10.6,textColor=MUTE)
callh=S("callh",fontName="Helvetica-Bold",fontSize=8.8,leading=11,textColor=ACCENT,spaceAfter=1.5)
callb=S("callb",fontName="Helvetica",fontSize=8.5,leading=11,textColor=INK)
foot=S("foot",fontName="Helvetica-Oblique",fontSize=7.3,leading=9,textColor=MUTE)
li=S("li",parent=body,leftIndent=9,spaceAfter=1.5)
def bullet(t): return Paragraph(f'<font color="#1f5fbf">•</font>&nbsp;&nbsp;{t}',li)
def box(hdr,txt,bg=BOXBG):
    inner=[[Paragraph(hdr,callh)],[Paragraph(txt,callb)]]
    t=Table(inner,colWidths=[W-14]); t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),bg),("LINEBEFORE",(0,0),(0,-1),2.2,ACCENT),
        ("LEFTPADDING",(0,0),(-1,-1),9),("RIGHTPADDING",(0,0),(-1,-1),9),
        ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),6)])); return t

doc=SimpleDocTemplate("MAVEN_one_pager.pdf",pagesize=letter,leftMargin=0.6*inch,rightMargin=0.6*inch,topMargin=0.5*inch,bottomMargin=0.42*inch)
W=doc.width; story=[]

story.append(Paragraph("MAVEN",title))
story.append(Paragraph("Turning evidence into better marketing decisions.",promise))
story.append(Paragraph("<i>Given everything we know, what should we do next?</i> — the question marketers ask every day. MAVEN is the system that answers it, powered by ORION, the judgment engine.",sub))
story.append(Spacer(1,4)); story.append(HRFlowable(width="100%",thickness=1.4,color=ACCENT,spaceAfter=5))

story.append(box("Why now",
  "The idea isn't new — marketers have wanted to connect all of this evidence for decades. What's new is that <b>large language models, modern APIs, near-real-time data, and calibration techniques</b> finally make cross-source evidence synthesis <b>operational rather than aspirational</b>. The technology has caught up to the vision. "
  "<b>Past:</b> evidence sat in silos. <b>Present:</b> it can finally be connected — and it must be, as fragmentation and privacy erosion make any single metric less trustworthy and AI-generated creative multiplies the decisions. "
  "<b>Future:</b> decisions improve because AI reasons <i>across</i> evidence instead of optimizing one metric. <b>AI isn't the purpose — better marketing decisions are. AI is simply what finally makes this possible.</b>"))
story.append(Spacer(1,5))

story.append(Paragraph("What MAVEN is",h2))
story.append(Paragraph("Not another dashboard or score. MAVEN synthesizes the <b>marketing evidence organizations already collect but rarely connect</b> — creative, media, consumer, brand, context, competitive, business outcomes, first-party data — and runs it through one spine: <b>Evidence &#8594; Judgment &#8594; Recommendation &#8594; Decision</b>. Every methodology (Ace Metrix, iSpot, System1, EDO, Ad Meter, press, social, your own data) is an <b>expert witness</b>; none is privileged for coming from one vendor. MAVEN reasons across them. <i>Creative effectiveness is where we enter — not what defines us.</i>",body))

story.append(box("The core principle",
  "<b>MAVEN does not collect sources — it collects evidence that supports or challenges specific claims.</b><br/>"
  "<i>A claim that can't be challenged isn't evidence-based reasoning — it's advocacy.</i> And every methodology is valid for one question: the error is borrowing its authority on the question it was built for to answer one it wasn't."))
story.append(Spacer(1,5))

story.append(Paragraph("How it works",h2))
story.append(bullet("<b>ORION, an executive council</b> of six domain intelligences (Creative, Media, Consumer, Brand, Business, Context) — each an instrument valid for one question. ORION synthesizes; MAVEN delivers the decision."))
story.append(bullet("<b>Enterprise architecture:</b> private client evidence stays isolated (never pooled or used to train a shared model); ORION reasons over it using a shared knowledge layer built only from public science + vendor norms."))
story.append(bullet("<b>Judgment is the enduring artifact</b> (recommendations are situational). Provenance is always tagged — measured / AI-derived / unavailable — and gaps are named, not hidden."))

story.append(Paragraph("Proof — Recommendation #001",h2))
story.append(Paragraph("Budweiser “Puppy Love”: from 470 real verbatims + public evidence, MAVEN produced a credible, CMO-ready point of view that <b>challenged a popular belief on the evidence</b> — flagging that the ad's fame doesn't establish it sold beer, and marking “needed more product” as <i>not supported</i>. A recommendation that can argue <i>against</i> a claim, with provenance, is a decision process — not a summary.",body))

# two-col: moat + GTM
moat=[Paragraph("The moat",h2),
      Paragraph("Because client data is never pooled, the moat isn't the data or the raw reasoning (LLMs commoditize that). It's the <b>ontology + methodology</b>, the accumulating <b>decision history</b> (judgments &#8594; outcomes), the curated knowledge layer, and the <b>neutral, cross-source position</b> — the one seat from which synthesis is credible.",body)]
gtm=[Paragraph("Go-to-market",h2),
     Paragraph("Beachhead: <b>agencies</b> — they hold the tool subscriptions across many clients, feel the fragmentation daily, and give multiple campaigns per logo. Connect on the customer's own subscriptions (their credentials, their consent); MAVEN acts as their tool. Land agencies; expand to in-house CMO teams.",body)]
cols=Table([[moat,gtm]],colWidths=[W*0.5,W*0.5])
cols.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(0,0),0),("RIGHTPADDING",(0,0),(0,0),12),("LEFTPADDING",(1,0),(1,0),0),("RIGHTPADDING",(1,0),(1,0),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0)]))
story.append(Spacer(1,2)); story.append(cols)

story.append(Spacer(1,7)); story.append(HRFlowable(width="100%",thickness=0.6,color=RULE,spaceAfter=3))
story.append(Paragraph("A company whose purpose predates its technology outlasts the technology. MAVEN — a Marketing Evidence Orchestrator. Working strategy brief; the reasoning behind Recommendation #001 is documented in the Founder's Wiki.",foot))

doc.build(story)
print("built MAVEN_one_pager.pdf")
