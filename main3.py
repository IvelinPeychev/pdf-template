from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

file = pd.read_csv('topics.csv')

# We read the file row with pandas
for index, row in file.iterrows():

    # Check main.py for more information
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)

    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # setting the footer and setting it in func
    def add_footer(mm):
        pdf.ln(mm)
        pdf.set_font(family='Times', style='B', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    add_footer(265)

    # we take the number of the pdf based of the number placed in the document and adding blank pages
    # We take -1 because of the title page above
    for number in range(int(row['Pages']) -1):
        pdf.add_page()
        add_footer(277)

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("output2.pdf")