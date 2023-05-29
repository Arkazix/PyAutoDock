from pathlib import Path
import argparse


class CommandLineArgs:

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Outil de documentation automatisée pour les projets Python."
        )
        self.input_path = Path()
        self.output_path = Path()

    # Request
    def get_input_path(self) -> Path:
        """Return the input path."""
        return self.input_path

    def get_output_path(self) -> Path:
        """Return the output path."""
        return self.output_path

    # Commands
    def add_argument(self, *args, **kwargs) -> None:
        """Add an argument to the parser"""
        self.parser.add_argument(*args, **kwargs)

    def parse_args(self) -> None:
        """Parse the arguments and set the input and output paths"""
        args = self.parser.parse_args()
        self.input_path = Path(args.path)
        self.output_path = Path(args.output) if args.output else \
            Path(__file__).parent.parent / "output"
