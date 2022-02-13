class NodeComment:

    def __init__(self, text: str) -> None:
        self.text = text

    def __str__(self) -> str:
        return self.text


class NodeFunction:

    def __init__(self, function_name: str, NodeComment: NodeComment) -> None:
        self.function_name = function_name
        self.node_comment = NodeComment

    def __str__(self) -> str:
        return f"func name: {self.function_name}\n\n" + str(self.node_comment)
