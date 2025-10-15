from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import docx, tempfile

def make_docx(text):
    doc = docx.Document()
    for para in text.split("\n"):
        doc.add_paragraph(para)
    output = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
    doc.save(output.name)
    return output.name

def make_pdf(text):
    output = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    c = canvas.Canvas(output.name, pagesize=A4)
    t = c.beginText(50, 800)
    for line in text.split("\n"):
        t.textLine(line)
    c.drawText(t)
    c.save()
    return output.name
