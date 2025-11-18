from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def write_resume(name, experience, skills, qualifications, photo_path, output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(100, 800, name)

    c.setFont("Helvetica", 12)
    c.drawString(100, 760, "Experience:")
    for i, exp in enumerate(experience):
        c.drawString(120, 740 - (i * 20), f"- {exp}")

    c.drawString(100, 660, "Skills:")
    for i, skill in enumerate(skills):
        c.drawString(120, 640 - (i * 20), f"- {skill}")

    c.drawString(100, 540, "Qualifications:")
    for i, q in enumerate(qualifications):
        c.drawString(120, 520 - (i * 20), f"- {q}")

    if photo_path:
        c.drawImage(photo_path, 400, 650, width=120, height=160)

    c.save()
    return output_path
