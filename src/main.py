from pyAutoDockParser import Parser
from pdf import Pdf


def get_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


if __name__ == '__main__':
    filename = "/home/hugo/Bureau/Wordle/src/game.py"
    lines = get_lines(filename)

    parser = Parser(lines)
    parser.parse()

    pdf = Pdf("Documentation.pdf")
    pdf.add_functions(parser.node_functions)
    pdf.save_pdf()
