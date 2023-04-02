from fpdf import FPDF

# Instance of the class
pdf = FPDF(orientation='P', unit='mm', format='A4')


# creating a page
pdf.add_page()

# Page settings
pdf.set_font(family='Times', style='B', size=12)
pdf.cell(w=0, h=12, txt='Hello there', align='L', ln=1, border=1)
pdf.set_font(family='Times', style='B', size=10)
pdf.cell(w=0, h=12, txt='Hi there ', align='L', ln=1, border=1)

# to add new page we need to add additional add_page

pdf.add_page()

pdf.set_font(family='Times', style='B', size=12)
pdf.cell(w=0, h=12, txt='Hello there', align='L', ln=1, border=1)
pdf.set_font(family='Times', style='B', size=10)
pdf.cell(w=0, h=12, txt='Hi there ', align='L', ln=1, border=1)

pdf.output("output.pdf")
