from src.pyAutoDockParser import Parser
from src.markdown import MarkDown
from typing import List


def get_lines(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return f.readlines()

if __name__ == '__main__':
    filename = "test/test.py"
    lines = get_lines(filename)

    parser = Parser(lines)
    parser.parse()

    markdown = MarkDown("AutoDock.md")
    markdown.add_freestanding_functions(parser.node_functions)
    markdown.add_class(parser.node_class)
    markdown.save()
