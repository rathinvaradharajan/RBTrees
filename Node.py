from NodeColor import NodeColor


class Node:
    def __init__(self, value=None, parent=None, left_child=None,
                 right_child=None, node_color=NodeColor.RED):
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.node_color = node_color
