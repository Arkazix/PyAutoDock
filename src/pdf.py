from fpdf import FPDF
from node import NodeFunction


class Pdf(FPDF):

    def __init__(self, filename: str) -> None:
        super().__init__()
        self.filename = filename
        self.pdf = FPDF()
        self.pdf.add_page()

    def __add_function(self, node_function: NodeFunction) -> None:
        self.pdf.set_font("Arial", size=18)
        self.pdf.cell(w=0, txt=node_function.function_name, align="C")
        self.pdf.ln(15)
        self.pdf.set_font("Arial", size=15)
        self.pdf.cell(w=0, txt=str(node_function.node_comment))
        self.pdf.ln(20)

    def add_functions(self, node_functions: list[NodeFunction]) -> None:
        for node_function in node_functions:
            if len(str(node_function.node_comment)) != 0:  
                self.__add_function(node_function)


    def save_pdf(self) -> None:
        self.pdf.output(self.filename)
