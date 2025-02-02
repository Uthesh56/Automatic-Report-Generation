from fpdf import FPDF
def Export(Report):
    Report = Report.replace("\u2013", "-")  
    Pdf = FPDF()
    Pdf.add_page()
    Pdf.set_font('Arial', 'B', 16)
    Pdf.cell(200, 10, txt="Report Summary", ln=True, align='C')
    Pdf.set_font('Arial', '', 12)
    Pdf.ln(10)
    Pdf.multi_cell(0, 10, txt=Report)
    Pdf.output("Report.pdf")