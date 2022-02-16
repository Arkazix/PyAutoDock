from src.node import NodeClass, NodeFunction, NodeComment
from typing import List

class MarkDown:

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.text = ""

    # REQUETES
    def get_func_title(self, func: NodeFunction) -> str:
        """Return title bound to function func."""
        title = func.function_name.capitalize()
        return title

    def get_func_parameter(self, func: NodeFunction) -> str:
        """Return parameter bound to function func."""
        return func.function_parameter

    def get_func_desc(self, comment: NodeComment) -> str:
        """Return description bound to function func."""

        # Remove empty string
        func_desc_list = [d for d in str(
            comment).splitlines() if not d.isspace()]

        # Add all line
        func_desc = ""
        for desc in func_desc_list:
            new_line = "\n" if desc != func_desc_list[-1] else ""
            func_desc = func_desc + " ".join(desc.split()) + new_line
        return func_desc

    # COMMANDES
    def add_freestanding_function(self, node_function: NodeFunction) -> None:
        func_title = self.get_func_title(node_function)
        func_parameter = self.get_func_parameter(node_function)
        func_desc = self.get_func_desc(node_function.node_comment)
        if func_desc == "":
            return

        self.text += '\t\t<div style="background-color: white;'\
                     'color: #404040;border: 1px solid grey;' \
                     'border-radius:5px;' \
                     'padding-left:15px;padding-right:15px;' \
                     'margin-bottom:15px;">\n'

        self.text += '\t\t\t<h3 style="color:black;font-weight:bold;">' \
                     f'{func_title}</h3>\n'

        self.text += '\t\t\t<div style="background-color:black;' \
                     'color:#E5E6D3;padding-left:5px;padding-right:5px;' \
                     'display: inline-block;border: 2px solid black;' \
                     f'border-radius:5px">\n\t\t\t\t{func_title + func_parameter}\n'
        self.text += '\t\t\t</div>\n'

        self.text += '\t\t\t<p style="color:black;word-break:break-word;' \
                     f'margin-top:10px;">{func_desc}</p>\n'

        self.text += '\t\t</div>\n'

    def add_freestanding_functions(self, node_functions: List[NodeFunction]) -> None:
        self.text += '<h1 style="color:#FFF;">Freestanding functions</h1>\n'
        self.text += '<ul style="list-style-type: none;">\n'
        self.text += '\t<li>\n'
        for node_function in node_functions:
            if not node_function.is_in_class:
                self.add_freestanding_function(node_function)
        self.text = self.text + '\t</li>\n'
        self.text = self.text + '</ul>\n'

    def add_class(self, node_class: List[NodeClass]) -> None:

        for class_ in node_class:
            self.text += f'<h1 style="color:#FFF;">Class: {class_.class_name}</h1>\n'
            self.text += '<ul style="list-style-type: none;">\n'
            self.text += '\t<li>\n'
            for node_function in class_.functions:
                self.add_freestanding_function(node_function)
            self.text = self.text + '\t</li>\n'
            self.text = self.text + '</ul>\n'

    def save(self):
        with open(self.filename, "w") as f:
            f.write(self.text)
