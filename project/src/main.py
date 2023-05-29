from .code_analyzer.code_analyzer import CodeAnalyzer
from .command_line_args import CommandLineArgs
from typing import Union, List, Dict
from pathlib import Path


def analyze_files(path: Path) -> List[CodeAnalyzer]:
    """Analyze file / files for the given path."""
    analyze_files: List[CodeAnalyzer] = []
    if path.is_dir():
        analyze_files.extend(
            CodeAnalyzer(child) for child in path.iterdir()
            if child.is_file() and child.suffix == '.py'
        )
    elif path.is_file() and path.suffix == '.py':
        analyze_files.append(CodeAnalyzer(path))
    for analyze_file in analyze_files:
        analyze_file.analyze_file()
    return analyze_files


def main() -> None:
    args_handler = CommandLineArgs()

    args_handler.add_argument(
        "-p", "--path", help="Le chemin du dossier à analyser", required=True
    )
    args_handler.add_argument(
        "-o", "--output", help="Le chemin du dossier de sortie"
    )
    args_handler.parse_args()

    analyze_codes = analyze_files(args_handler.get_input_path())
