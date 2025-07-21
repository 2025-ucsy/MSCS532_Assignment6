"""Singly linked list with common operations."""

class Node:
    __slots__ = "data", "next"
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # ---------- insertion ----------
    def insert_front(self, value):
        self.head = Node(value, self.head)

    def insert_end(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(value)

    # ---------- deletion ----------
    def delete_value(self, value):
        prev, cur = None, self.head
        while cur:
            if cur.data == value:
                if prev: prev.next = cur.next
                else:    self.head = cur.next
                return True
            prev, cur = cur, cur.next
        return False  # not found

    # ---------- traversal ----------
    def traverse(self):
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next

    def search(self, value):
        return any(x == value for x in self.traverse())

    def __repr__(self):
        return "LinkedList:[" + " → ".join(map(str, self.traverse())) + "]"
