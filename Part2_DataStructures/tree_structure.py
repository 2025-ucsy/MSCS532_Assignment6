"""Simple rooted tree using linked‑list style children list."""

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def preorder(self):
        yield self.key
        for child in self.children:
            yield from child.preorder()

    def __repr__(self):
        return f"TreeNode({self.key})"
