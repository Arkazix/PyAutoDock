from src.pyAutoDockParser import Parser
from src.markdown import MarkDown


def get_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


if __name__ == '__main__':
    filename = ""
    lines = get_lines(filename)

    parser = Parser(lines)
    parser.parse()

    markdown = MarkDown("AutoDock.md")
    markdown.add_freestanding_functions(parser.node_functions)
    markdown.save()
