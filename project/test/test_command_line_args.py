from src.command_line_args import CommandLineArgs
from unittest.mock import MagicMock
from pathlib import Path
import argparse


def test_CommandLineArgs_add_argument():
    cla = CommandLineArgs()
    cla.add_argument(
        "-p", "--path", help="Le chemin du dossier à analyser", required=True
    )
    assert any(arg for arg in cla.parser._actions if arg.dest == "path")


def test_CommandLineArgs_parse_args():
    cla = CommandLineArgs()
    cla.parser.parse_args = MagicMock(
        return_value=argparse.Namespace(path='path/to/input', output=None)
    )
    cla.add_argument(
        "-p", "--path", help="Le chemin du dossier à analyser", required=True
    )
    cla.add_argument("-o", "--output", help="Le chemin du dossier de sortie")
    cla.parse_args()
    assert cla.input_path == Path("path/to/input")
    assert cla.output_path == Path(__file__).parent.parent / "output"
