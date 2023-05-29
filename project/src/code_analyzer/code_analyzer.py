from typing import Union, List, Dict
from pathlib import Path
import ast


class CodeAnalyzer:

    def __init__(self, path: Union[str, Path]) -> None:
        self.path = Path(path)
        self.classes = []
        self.functions = []
        self.class_functions = set()

    # Request
    def get_classes(self) -> List[ast.ClassDef]:
        """Return the classes found in the code."""
        return self.classes

    def get_functions(self) -> List[ast.FunctionDef]:
        """Return the functions found in the code."""
        return self.functions

    def is_func_in_class(self, func: ast.FunctionDef) -> bool:
        """Return True if the given function is in the classes found in the code."""
        return func in self.class_functions

    def get_func_info(self, func: ast.FunctionDef) -> Dict[str, Union[str, Dict[str, str]]]:
        """Return the information of the given function."""
        func_info = {'name': func.name, 'args': {}}

        for arg in func.args.args:
            func_info['args'][arg.arg] = ""
            if isinstance(arg.annotation, ast.Name):
                func_info['args'][arg.arg] = arg.annotation.id

        if func.returns:
            if isinstance(func.returns, ast.Name):
                func_info['returns'] = func.returns.id
            elif isinstance(func.returns, ast.Constant):
                func_info['returns'] = func.returns.value

        if func.body:
            for node in func.body:
                if isinstance(node, ast.Expr):
                    if isinstance(node.value, ast.Constant):
                        func_info['docstring'] = node.value.value
                    elif isinstance(node.value, ast.Str):
                        func_info['docstring'] = node.value.s

        return func_info

    def get_class_info(self, cls: ast.ClassDef) -> Dict[str, Union[str, List[Union[ast.FunctionDef, str]]]]:
        """Return the information of the given class."""
        class_info = {'name': cls.name, 'methods': [], 'parent': []}

        for node in cls.body:
            if isinstance(node, ast.FunctionDef):
                class_info['methods'].append(node)

        for base in cls.bases:
            if isinstance(base, ast.Name):
                class_info['parent'].append(base.id)

        return class_info

    # Commands
    def analyze(self) -> None:
        """Analyze the code in the given path."""
        # Reset the data
        self.classes.clear()
        self.functions.clear()
        self.class_functions.clear()
        # Analyze the code
        if self.path.is_dir():
            for child in self.path.iterdir():
                if child.is_file() and child.suffix == '.py':
                    self.analyze_file(child)
        elif self.path.is_file() and self.path.suffix == '.py':
            self.analyze_file(self.path)

    def analyze_file(self, path: Path) -> None:
        """Analyze the code in the given file."""
        with open(path, 'r') as file:
            source_code = file.read()

        try:
            tree = ast.parse(source_code)
        except SyntaxError as e:
            raise SyntaxError(f"Syntax error in {path}") from e

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                self.classes.append(node)
                self.class_functions.update(node.body)
            elif isinstance(node, ast.FunctionDef):
                if not self.is_func_in_class(node):
                    self.functions.append(node)
