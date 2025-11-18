from fpdf import FPDF

class ResumePDFGenerator:
    def create_pdf(self, text: str, output_path: str):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=11)

        for line in text.split("\n"):
            pdf.multi_cell(0, 6, line)

        pdf.output(output_path)
        return output_path
