"""Array‑based stack and queue implementations."""

class ArrayStack:
    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __repr__(self):
        return f"Stack(top→bottom): {list(reversed(self._data))}"


class ArrayQueue:
    def __init__(self):
        self._data = []
        self._front = 0      # circular queue pointer

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self._data[self._front]
        self._front += 1
        # Periodic cleanup to avoid unbounded growth
        if self._front > len(self._data) // 2:
            self._data = self._data[self._front:]
            self._front = 0
        return value

    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._data[self._front]

    def is_empty(self):
        return self._front >= len(self._data)

    def __repr__(self):
        return f"Queue(front→back): {self._data[self._front:]}"
