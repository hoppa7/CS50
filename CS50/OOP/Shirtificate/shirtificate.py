from fpdf import FPDF

class PDF(FPDF):
    def header(self):

        self.image("image.png", x=30, y=60, w=150)

        self.set_font("helvetica", style="B", size=30)

        self.cell(195, 20, "CS50 Shirtificate", align="C")

    def shirt_text(self, name):
        self.name = name + " Took CS50"
        self.set_text_color(255, 255, 255)

        self.set_font("helvetica", style="B", size=20)
        self.set_xy(30, 140)
        self.cell(153, -50, self.name, align="C")


pdf = PDF()
pdf.add_page()
pdf.shirt_text(input("Input your name: "))
pdf.output("shirtificate.pdf")