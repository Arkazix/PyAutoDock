import re
from src.node import NodeFunction, NodeComment


class Parser:

    def __init__(self, text: str) -> None:
        self.text = text
        self.node_functions: list[NodeFunction]

    def parse(self):
        self.node_functions = []
        current_line_index = 0
        while current_line_index < len(self.text):
            current_line = self.text[current_line_index]
            re_function = re.findall("def", current_line)
            if re_function:
                indent = self.get_indent(current_line)
                current_line_index += 1
                node_comment = self.read_comment(current_line_index, indent)
                self.node_functions.append(NodeFunction(
                    self.get_func_name(current_line),
                    self.get_func_parameter(current_line), 
                    node_comment)
                )

            current_line_index += 1

    def read_comment(self, line_index: int, indent: int) -> NodeComment:
        comment = ""
        is_comment = False
        while line_index < len(self.text) and self.get_indent(self.text[line_index]) > indent:
            current_line = self.text[line_index]
            re_comment = re.findall('"""', current_line)
            if not re_comment and is_comment:
                comment += current_line
            if re_comment:
                is_comment = (not is_comment and len(re_comment) < 2)
                comment = comment + current_line.replace('"', "")
            line_index += 1

        return NodeComment(comment)

    def get_indent(self, line):
        char = line[0]
        indent = 0
        while char == " " and indent < len(line):
            indent += 1
            char = line[indent]
        return indent

    def get_func_name(self, line: str) -> str:
        start = line.find("def ") + len("def ")
        end = line.find("(")
        return line[start:end]

    def get_func_parameter(self, line: str) -> str:
        start = line.find("(")
        end = line.rfind(":")
        return line[start:end]
