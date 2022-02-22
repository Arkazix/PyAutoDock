from src.pyAutoDockParser import Parser
from src.markdown import MarkDown
from src.options import Options
import sys

EXIT_SUCCESS = 0
EXIT_FAILURE = 1


def read_file(path: str) -> Parser:
    with open(path, "r") as f:
        lines = f.readlines()
    parser = Parser(lines)
    parser.parse()

    return parser


if __name__ == '__main__':
    options = Options(sys.argv)
    if options.get_argc() <= 1:
        options.unexpected_argument()
        sys.exit(EXIT_SUCCESS)

    if options.is_in_argv("--help"):
        options.help__()
        sys.exit(EXIT_SUCCESS)

    if options.process_argument() != 0:
        sys.exit(EXIT_FAILURE)

    path = options.get_path()

    if options.is_file(path):
        nodes = read_file(path)

        markdown = MarkDown("AutoDock.md")
        markdown.add_freestanding_functions(nodes.node_functions)
        markdown.add_class(nodes.node_class)
        markdown.save()
    else:
        print("Directory read not yet implemented.")
