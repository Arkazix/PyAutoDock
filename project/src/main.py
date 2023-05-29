from .code_analyzer.code_analyzer import CodeAnalyzer
from .command_line_args import CommandLineArgs
import ast


def main() -> None:
    args_handler = CommandLineArgs()

    args_handler.add_argument(
        "-p", "--path", help="Le chemin du dossier à analyser", required=True
    )
    args_handler.add_argument(
        "-o", "--output", help="Le chemin du dossier de sortie"
    )
    args_handler.parse_args()

    code_analyzer = CodeAnalyzer(args_handler.get_input_path())
    code_analyzer.analyze()

    for func in code_analyzer.get_functions():
        print(code_analyzer.get_func_info(func))

    for cls in code_analyzer.get_classes():
        print(code_analyzer.get_class_info(cls))
