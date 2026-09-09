"""Builds DemoPack_NightSchools_Jharia.pdf from the markdown in docs/demo/.

A deliberately small markdown -> PDF renderer (headings, paragraphs, bullets, tables,
blockquotes, fenced code, rules), styled to match build_qa_pdf.py, so the demo pack's three
documents stay ONE source of truth: edit the markdown, re-run this, never hand-edit the PDF.

    python3 build_demo_pack_pdf.py

DejaVu is registered instead of Helvetica because these documents use ->, >=, Rs and curly
quotes; a submission PDF with black boxes where a glyph should be is exactly the avoidable
embarrassment this file exists to prevent.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    HRFlowable,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "DemoPack_NightSchools_Jharia.pdf")

DOCS = [
    ("PART A — PROBLEM STATEMENT", "docs/demo/PROBLEM_STATEMENT.md"),
    ("PART B — SOLUTION", "docs/demo/SOLUTION.md"),
    ("PART C — INDUSTRY UPLOAD SPEC", "docs/demo/INDUSTRY_UPLOAD_SPEC.md"),
]

NAVY = HexColor("#0F2A33")
TEAL = HexColor("#0E6B6B")
AMBER = HexColor("#B8741A")
INK = HexColor("#1B1B1B")
SOFT = HexColor("#5A5A5A")
LINE = HexColor("#D8D8D8")
BAND = HexColor("#F4F1EA")
ROWALT = HexColor("#F7F9F9")
FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def register_fonts():
    try:
        pdfmetrics.registerFont(TTFont("Body", os.path.join(FONT_DIR, "DejaVuSans.ttf")))
        pdfmetrics.registerFont(TTFont("Body-Bold", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))
        pdfmetrics.registerFont(TTFont("Mono", os.path.join(FONT_DIR, "DejaVuSansMono.ttf")))
        pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold")
        return "Body", "Body-Bold", "Mono"
    except Exception as exc:  # font-less machine: keep going, glyphs may suffer
        print(f"  ! font fallback ({exc}); using Helvetica", file=sys.stderr)
        return "Helvetica", "Helvetica-Bold", "Courier"


REG, BOLD, MONO = register_fonts()
base = getSampleStyleSheet()


def st(key, **kw):
    parent = kw.pop("parent", base["BodyText"])
    return ParagraphStyle(key, parent=parent, **kw)


S = {
    "title": st("title", parent=base["Title"], fontName=BOLD, fontSize=21, leading=26,
                textColor=NAVY, alignment=TA_LEFT, spaceAfter=4),
    "subtitle": st("subtitle", parent=base["Normal"], fontName=REG, fontSize=11.5, leading=15,
                   textColor=SOFT, spaceAfter=12),
    "part": st("part", parent=base["Heading1"], fontName=BOLD, fontSize=12, leading=15,
               textColor=white, backColor=NAVY, borderPadding=(5, 7, 5, 7), spaceBefore=0, spaceAfter=10),
    "h1": st("h1", parent=base["Heading1"], fontName=BOLD, fontSize=14, leading=18,
             textColor=white, backColor=TEAL, borderPadding=(5, 7, 5, 7), spaceBefore=12, spaceAfter=7),
    "h2": st("h2", parent=base["Heading2"], fontName=BOLD, fontSize=11.5, leading=14.5,
             textColor=NAVY, spaceBefore=10, spaceAfter=4),
    "h3": st("h3", parent=base["Heading3"], fontName=BOLD, fontSize=10, leading=13,
             textColor=AMBER, spaceBefore=8, spaceAfter=3),
    "body": st("body", fontName=REG, fontSize=9.3, leading=13, textColor=INK,
               alignment=TA_JUSTIFY, spaceAfter=5),
    "bullet": st("bullet", fontName=REG, fontSize=9.3, leading=12.6, textColor=INK,
                 leftIndent=15, bulletIndent=3, spaceAfter=3.5, alignment=TA_LEFT),
    "quote": st("quote", fontName=REG, fontSize=9.3, leading=13, textColor=HexColor("#3A3A3A"),
                backColor=BAND, borderPadding=(6, 8, 6, 8), leftIndent=4, spaceBefore=3,
                spaceAfter=7, alignment=TA_JUSTIFY),
    "code": st("code", parent=base["Code"], fontName=MONO, fontSize=7.5, leading=10,
               textColor=NAVY, backColor=BAND, borderPadding=(6, 7, 6, 7), spaceAfter=8),
    "cell": st("cell", parent=base["Normal"], fontName=REG, fontSize=7.5, leading=9.6, textColor=INK),
    "cellhead": st("cellhead", parent=base["Normal"], fontName=BOLD, fontSize=7.6, leading=9.6,
                   textColor=white),
}

PIPE = "\x00"


def inline(text: str) -> str:
    """Escape first, format second — never the other way round."""
    text = text.replace("\\|", PIPE)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"`([^`]+)`", rf'<font face="{MONO}" size="8">\1</font>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<i>\1</i>", text)
    return text.replace(PIPE, "|")


def table_style(ncol: int) -> TableStyle:
    return TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TEAL),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, ROWALT]),
        ("GRID", (0, 0), (-1, -1), 0.35, LINE),
        ("BOX", (0, 0), (-1, -1), 0.6, TEAL),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4.5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4.5),
        ("TOPPADDING", (0, 0), (-1, -1), 3.4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.4),
    ])


def render_table(rows, avail: float) -> Table:
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    weight = [max(6, min(48, max(len(r[i]) for r in rows))) for i in range(ncol)]
    total = float(sum(weight))

    # Start every column at its widest UNBREAKABLE word (measured in the real font),
    # then distribute the leftover space by content weight. Starting from the floors
    # is the fix: a proportional rescale afterwards can shrink a column back under
    # its own longest word and wrap "Cap." onto two lines.
    def widest_word(col: int) -> float:
        best = 11.0
        for r in rows:
            for w in re.split(r"[\s,;()|.]+", re.sub(r"[*`_\\]", "", r[col])):
                if w:
                    best = max(best, stringWidth(w, REG, 7.6))
        return best + 9.0

    floors = [min(widest_word(i), avail * 0.40) for i in range(ncol)]
    if sum(floors) >= avail:                      # degenerate: just share it evenly
        widths = [avail / ncol] * ncol
    else:
        slack = avail - sum(floors)
        widths = [f + slack * w / total for f, w in zip(floors, weight)]
        widths = [avail * w / sum(widths) for w in widths]

    data = [[Paragraph(inline(c), S["cellhead"]) for c in rows[0]]]
    data += [[Paragraph(inline(c), S["cell"]) for c in r] for r in rows[1:]]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(table_style(ncol))
    return t


def md_to_flow(md: str, avail: float) -> list:
    out: list = []
    para: list[str] = []
    bullets: list[list[str]] = []
    tbl: list[list[str]] = []
    quote: list[str] = []
    code: list[str] = []
    in_code = False

    def flush_para():
        if para:
            out.append(Paragraph(inline(" ".join(para)), S["body"]))
            para.clear()

    def flush_bullets():
        for mark, txt in bullets:
            out.append(Paragraph(inline(txt), S["bullet"], bulletText=mark))
        bullets.clear()

    def flush_table():
        if tbl:
            out.append(render_table(list(tbl), avail))
            out.append(Spacer(1, 0.28 * cm))
        tbl.clear()

    def flush_quote():
        if quote:
            out.append(Paragraph(inline(" ".join(quote)), S["quote"]))
        quote.clear()

    def flush_code():
        if code:
            esc = [c.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;") or "&nbsp;"
                   for c in code]
            out.append(Paragraph("<br/>".join(esc), S["code"]))
        code.clear()

    def flush_all():
        flush_para(); flush_bullets(); flush_table(); flush_quote()

    for raw in md.split("\n"):
        line = raw.rstrip()
        s = line.strip()

        if s.startswith("```"):
            flush_para(); flush_bullets(); flush_table(); flush_quote()
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code.append(line)
            continue

        if not s:
            flush_all()
            continue
        if set(s) <= {"-", "="} and len(s) >= 3:
            flush_all()
            out.append(HRFlowable(width="100%", thickness=0.5, color=LINE, spaceBefore=3, spaceAfter=7))
            continue
        if s.startswith("|"):
            flush_para(); flush_bullets(); flush_quote()
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", s.strip("|"))]
            if not all(re.fullmatch(r":?-{2,}:?", c or "-") for c in cells):
                tbl.append(cells)
            continue
        if tbl:
            flush_table()
        if s.startswith("# "):
            flush_all(); out.append(Paragraph(inline(s[2:]), S["title"]))
        elif s.startswith("## "):
            flush_all(); out.append(Paragraph(inline(s[3:]), S["h1"]))
        elif s.startswith("### "):
            flush_all(); out.append(Paragraph(inline(s[4:]), S["h2"]))
        elif s.startswith("#### "):
            flush_all(); out.append(Paragraph(inline(s[5:]), S["h3"]))
        elif s.startswith("> "):
            flush_para(); flush_bullets(); quote.append(s[2:])
        elif re.match(r"^[-*] ", s):
            flush_para(); flush_table(); flush_quote(); bullets.append(["\u2022", s[2:]])
        elif re.match(r"^\d+[.)] ", s):
            flush_para(); flush_table(); flush_quote()
            num, txt = re.split(r"[.)]\s", s, maxsplit=1)
            bullets.append([f"{num}.", txt])
        else:
            if bullets:                      # lazy continuation of an open bullet
                bullets[-1][1] += " " + s
                continue
            flush_table(); flush_quote(); para.append(s)

    flush_all()
    if in_code:
        flush_code()
    return out


def git_sha() -> str:
    try:
        r = subprocess.run(["git", "-C", ROOT, "rev-parse", "--short", "HEAD"],
                           capture_output=True, text=True, timeout=10)
        return (r.stdout.strip() or "dev")
    except Exception:
        return "dev"


SHA = git_sha()


def decorate(canv, doc):
    canv.saveState()
    w, h = A4
    canv.setFillColor(NAVY)
    canv.rect(0, h - 1.35 * cm, w, 1.35 * cm, fill=1, stroke=0)
    canv.setFillColor(AMBER)
    canv.rect(0, h - 1.48 * cm, w, 0.13 * cm, fill=1, stroke=0)
    canv.setFillColor(white)
    canv.setFont(BOLD, 9)
    canv.drawString(1.8 * cm, h - 0.9 * cm, "MILAN  \u00b7  Demo Pack  \u00b7  Jharia night schools")
    canv.setFont(REG, 8.5)
    canv.drawRightString(w - 1.8 * cm, h - 0.9 * cm,
                         "SIH26043  \u00b7  Smart Education  \u00b7  Software")
    canv.setStrokeColor(LINE)
    canv.setLineWidth(0.4)
    canv.line(1.8 * cm, 1.25 * cm, w - 1.8 * cm, 1.25 * cm)
    canv.setFillColor(SOFT)
    canv.setFont(REG, 7.6)
    canv.drawString(1.8 * cm, 0.95 * cm,
                    f"Built from docs/demo/*.md @ {SHA} \u2014 regenerate: python3 build_demo_pack_pdf.py")
    canv.drawRightString(w - 1.8 * cm, 0.95 * cm, f"Page {doc.page}")
    canv.restoreState()


def cover(story: list, avail: float) -> None:
    story.append(Spacer(1, 0.35 * cm))
    story.append(Paragraph("MILAN", S["title"]))
    story.append(Paragraph("An owner, a clock and a receipt for every broken community asset", S["subtitle"]))
    band = Table([[Paragraph(
        "<b>Demo pack \u00b7 three parts</b><br/>"
        "A \u00b7 Problem statement \u2014 the night school that closed when the solar lights broke<br/>"
        "B \u00b7 Solution \u2014 title, abstraction, and the instance walked through the platform<br/>"
        "C \u00b7 Industry upload spec \u2014 what a funder files, and what gets returned to them",
        st("cv", parent=base["Normal"], fontSize=10, leading=15, textColor=NAVY, alignment=TA_LEFT))]],
        colWidths=[avail])
    band.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), BAND),
                              ("BOX", (0, 0), (-1, -1), 0.8, AMBER),
                              ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                              ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 9)]))
    story.append(band)
    story.append(Spacer(1, 0.45 * cm))

    meta = [
        ["Parent problem statement",
         "SIH26043 \u2014 *A digital platform to crowdsource societal challenges and facilitate collaborative "
         "problem solving through universities and industry partnerships*"],
        ["Sponsoring organisation", "Government of Jharkhand \u00b7 Dept. of Higher & Technical Education"],
        ["Theme \u00b7 Category", "Smart Education \u00b7 Software"],
        ["Portal deadline (idea submission)", "30 September 2026"],
        ["Demo instance", "Jharia block (`DHN-JHA`), Dhanbad district \u2014 night classes for working children"],
        ["Domain \u00b7 severity \u00b7 priority",
         "`EDUCATION` \u00b7 0.82 (S2) \u00b7 **66.43 / 100** (S4, zero model calls)"],
        ["Routed to", "NIT Jamshedpur \u00b7 BIT Mesra \u00b7 BIT Sindri (claimed) \u2014 top 3 distinct orgs"],
        ["Seed data used", "12 HEIs \u00b7 51 capability labs \u00b7 24 districts \u00b7 263 blocks \u00b7 8 industry orgs"],
        ["Team ID / institution", "*(fill in before upload)*"],
        ["Document built from", f"`docs/demo/*.md` @ `{SHA}`"],
    ]
    rows = [[Paragraph("Field", S["cellhead"]), Paragraph("Value", S["cellhead"])]]
    rows += [[Paragraph(inline(a), S["cell"]), Paragraph(inline(b), S["cell"])] for a, b in meta]
    t = Table(rows, colWidths=[avail * 0.28, avail * 0.72], hAlign="LEFT", repeatRows=1)
    t.setStyle(table_style(2))
    story.append(t)
    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph(
        "<b>How to read this pack.</b> Parts A and B are the submission text: the problem as a citizen files "
        "it, and the platform answer to SIH26043, with the arithmetic shown rather than asserted. Part C is "
        "the operating rule for the industry side \u2014 which is where challenge platforms quietly die, because "
        "a funder with no evidence obligation produces a press release instead of an outcome. Figures marked "
        "*[demo]* are seeded for the demonstration; the geography, institutions, companies and laboratory "
        "capabilities are the rows this repository actually runs on.", S["quote"]))
    story.append(Spacer(1, 0.25 * cm))
    for n, sent in enumerate([
        "Communities hold the problems; universities hold the researchers. We are the pipeline between them.",
        "CPGRAMS routes complaints to officers. Milan routes unsolved problems to labs, with a clock.",
        "Discovery is never luck: every problem is pushed to matched departments, and every state escalates.",
        "200,000 Indian students invent a fake final-year project a year. We give them real ones.",
        "We do not stop people from sharing work. We make it impossible to erase who did it.",
    ], 1):
        story.append(Paragraph(f"<b>{n}.</b> {inline(sent)}", S["body"]))
    story.append(PageBreak())


def main() -> None:
    doc = SimpleDocTemplate(
        OUT, pagesize=A4, leftMargin=1.8 * cm, rightMargin=1.8 * cm, topMargin=2.0 * cm,
        bottomMargin=1.75 * cm, title="MILAN \u2014 Demo Pack: Jharia night schools (SIH26043)",
        author="Team Milan", subject="SIH26043 Smart Education \u2014 problem statement, solution, industry spec")
    avail = doc.width
    story: list = []
    cover(story, avail)
    for part, rel in DOCS:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            print(f"  ! missing {rel} \u2014 skipped", file=sys.stderr)
            continue
        story.append(Paragraph(part, S["part"]))
        story.extend(md_to_flow(open(path, encoding="utf-8").read(), avail))
        story.append(PageBreak())
    while story and isinstance(story[-1], PageBreak):
        story.pop()
    doc.build(story, onFirstPage=decorate, onLaterPages=decorate)

    blob = open(OUT, "rb").read()
    pages = blob.count(b"/Type /Page") - blob.count(b"/Type /Pages")
    print(f"Wrote {os.path.relpath(OUT, ROOT)}  \u2014  {len(blob)/1024:.0f} KB, {pages} pages")


if __name__ == "__main__":
    main()
