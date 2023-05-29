from ..code_analyzer.code_analyzer import CodeAnalyzer, get_class_info, get_func_info, CLASS_INFO
from pathlib import Path
from typing import List
import ast
import os


class DocGenerator:

    def __init__(self, code_analyzers: List[CodeAnalyzer], output_dir: Path) -> None:
        self.code_analyzers = code_analyzers
        self.output_dir = output_dir
        self.standalone_functions: List[ast.FunctionDef] = []

    # Command
    def generate_docs(self) -> None:
        """Generate the markdown files"""
        for analyzer in self.code_analyzers:
            for cls in analyzer.get_classes():
                self._generate_class_doc(cls)
            self.standalone_functions.extend(analyzer.get_functions())
        self._generate_standalone_function_doc(self.standalone_functions)

    def _generate_class_doc(self, cls: ast.ClassDef) -> None:
        """Generate the markdown file for the given class"""
        text = self._generate_class_markdown(get_class_info(cls))
        self._save_text_to_file(text, f'{cls.name}.md')

    def _generate_class_markdown(self, class_info: CLASS_INFO) -> str:
        """Generate markdown for a class"""
        return ""

    def _generate_standalone_function_doc(self, funcs: List[ast.FunctionDef]) -> None:
        """Generate the markdown file for the given functions"""
        pass

    # Utils
    def _save_text_to_file(self, text: str, filename: str) -> None:
        """Save the given text to a file with the given filename in the output directory"""
        with open(os.path.join(self.output_dir, filename), 'w') as file:
            file.write(text)
