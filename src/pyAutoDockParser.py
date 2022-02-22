from src.node import NodeClass, NodeFunction, NodeComment
from typing import Union
import re


class Parser:

    def __init__(self, text: str) -> None:
        self.text = text
        self.node_functions: list[NodeFunction]
        self.node_class: list[NodeClass]

    # COMMANDES
    def parse(self) -> None:
        """
        Parse self.text and init self.node_functions for freestanding functions
        and self.node_class for functions in the class.
        """
        self.node_functions = []
        self.node_class = []
        current_line_index = 0
        while current_line_index < len(self.text):
            to_increase = 1
            current_line = self.text[current_line_index]
            re_function = re.findall("def", current_line)
            re_class = re.findall("class", current_line)
            if re_class:
                to_increase, node_class = self.read_class(current_line_index)
                self.node_class.append(node_class)
            elif re_function:
                node_function = self.read_function(current_line_index)
                self.node_functions.append(node_function)
            current_line_index += to_increase

    def read_class(self, line_index: int) -> Union[int, NodeClass]:
        start_line_idx = line_index
        to_replace = {"\n": "", " ": ""}
        node_functions = []

        class_name = self.get_class_name(self.text[line_index])

        indent = self.get_indent(self.text[line_index])
        line_index += 1
        current_line = self.text[line_index]
        while line_index < len(self.text) - 1 \
                and (self.get_indent(current_line) > indent
                     or len(self.replaces(current_line, to_replace)) == 0):
            re_function = re.findall("def", current_line)
            if re_function:
                node_function = self.read_function(line_index)
                node_functions.append(node_function)
            line_index += 1
            current_line = self.text[line_index]

        return line_index - start_line_idx, NodeClass(class_name, node_functions)

    def read_function(self, line_index: int) -> NodeFunction:
        """Return a NodeFunction class by the line index where function start."""
        indent = self.get_indent(self.text[line_index])
        line_index += 1
        node_comment = self.read_comment(line_index, indent)
        node_function = NodeFunction(
            self.get_func_name(self.text[line_index - 1]),
            self.get_func_parameter(self.text[line_index - 1]),
            node_comment
        )
        return node_function

    def read_comment(self, line_index: int, indent: int) -> NodeComment:
        """Return a NodeComent of a current function with indent and line index."""
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

    def replaces(self, s: str, char_list: dict) -> str:
        for key, value in char_list.items():
            s = s.replace(key, value)
        return s

    # REQUETES
    def get_indent(self, line: str) -> int:
        """Return indent of current line."""
        char = line[0]
        indent = 0
        while char == " " and indent < len(line):
            indent += 1
            char = line[indent]
        return indent

    def get_func_name(self, line: str) -> str:
        """Return function name on the line."""
        start = line.find("def ") + len("def ")
        end = line.find("(")
        return line[start:end]

    def get_func_parameter(self, line: str) -> str:
        """Return function parameter on the line."""
        start = line.find("(")
        end = line.rfind(":")
        return line[start:end]

    def get_class_name(self, line: str) -> str:
        start = line.find("class ") + len("class ")
        end = line.find(":")
        return line[start:end]
