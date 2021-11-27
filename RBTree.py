from Node import Node
from NodeColor import NodeColor


class RBTree:
    def __init__(self):
        self.root = None

    def __left_rotate(self, node):
        y = node.right_child
        node.right_child = y.left_child
        if y.left_child is not None:
            y.left_child.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node.parent.left_child == node:
            node.parent.left_child = y
        else:
            node.parent.right_child = y
        y.left_child = node
        node.parent = y

    def __right_rotate(self, node):
        y = node.left_child
        node.left_child = y.right_child
        if y.right_child is not None:
            y.right_child.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node.parent.left_child == node:
            node.parent.left_child = y
        else:
            node.parent.right_child = y
        y.right_child = node
        node.parent = y

    def __insert_fix_up(self, node):
        while node and node.parent and node.parent.node_color == NodeColor.RED:
            if node.parent == node.parent.parent.left_child:
                y = node.parent.parent.right_child
                if y and y.node_color == NodeColor.RED:
                    node.parent.node_color = NodeColor.BLACK
                    y.node_color = NodeColor.BLACK
                    node.parent.parent.node_color = NodeColor.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right_child:
                        node = node.parent
                        self.__left_rotate(node)

                    node.parent.node_color = NodeColor.BLACK
                    node.parent.parent.node_color = NodeColor.RED
                    self.__right_rotate(node.parent.parent)
            else:
                y = node.parent.parent.left_child
                if y and y.node_color == NodeColor.RED:
                    node.parent.node_color = NodeColor.BLACK
                    y.node_color = NodeColor.BLACK
                    node.parent.parent.node_color = NodeColor.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right_child:
                        node = node.parent
                        self.__left_rotate(node)

                    node.parent.node_color = NodeColor.BLACK
                    node.parent.parent.node_color = NodeColor.RED
                    self.__right_rotate(node.parent.parent)
        self.root.node_color = NodeColor.BLACK

    def insert(self, value):
        if self.root is None:
            self.root = Node(value, None, None, None, NodeColor.BLACK)
            return
        parent = None
        node = self.root
        while node is not None:
            if value > node.value:
                parent = node
                node = node.right_child
            elif value < node.value:
                parent = node
                node = node.left_child
            else:
                return
        node = Node(value, parent, None, None)
        if value < parent.value:
            parent.left_child = node
        else:
            parent.right_child = node

        if node.parent.parent is not None:
            self.__insert_fix_up(node)

    def __height(self, node) -> int:
        if node is None:
            return 0
        height = 1 + max(self.__height(node.left_child), self.__height(node.right_child))
        return height

    def height(self) -> int:
        return self.__height(self.root)

    @staticmethod
    def __min(node):
        while node.left_child is not None:
            node = node.left_child
        return node.value

    def min(self):
        return self.__min(self.root)

    @staticmethod
    def __max(node):
        while node.right_child is not None:
            node = node.right_child
        return node.value

    def max(self):
        return self.__max(self.root)

    def successor(self, value) -> int:
        node = self.root
        while node is not None:
            if value > node.value:
                node = node.right_child
            elif value < node.value:
                node = node.left_child
            else:
                break
        if node is None:
            return -1
        if node.right_child is not None:
            return self.__min(node.right_child)
        y = node.parent
        while y is not None and node == y.right_child:
            node = y
            y = y.parent
        return y.value if y is not None else -1

    def predecessor(self, value) -> int:
        node = self.root
        while node is not None:
            if value > node.value:
                node = node.right_child
            elif value < node.value:
                node = node.left_child
            else:
                break
        if node is None:
            return -1
        if node.left_child is not None:
            return self.__max(node.left_child)
        y = node.parent
        while y is not None and node == y.left_child:
            node = y
            y = y.parent
        return y.value if y is not None else -1

    def search(self, value) -> bool:
        node = self.root
        while node is not None:
            if value > node.value:
                node = node.right_child
            elif value < node.value:
                node = node.left_child
            else:
                return True
        return False

    def __sort(self, node, acc):
        if node is None:
            return acc
        self.__sort(node.left_child, acc)
        val = str(node.value) + "-" + str(node.node_color)
        acc.append(val)
        self.__sort(node.right_child, acc)
        return acc

    def sort(self) -> []:
        return self.__sort(self.root, [])
