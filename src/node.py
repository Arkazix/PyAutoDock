class NodeComment:

    def __init__(self, text: str) -> None:
        self.text = text

    def __str__(self) -> str:
        return self.text


class NodeFunction:

    def __init__(self, function_name: str, function_parameter: str, NodeComment: NodeComment, is_in_class=False) -> None:
        self.function_name = function_name
        self.function_parameter = function_parameter
        self.node_comment = NodeComment
        self.is_in_class = is_in_class
