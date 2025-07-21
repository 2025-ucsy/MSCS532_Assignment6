"""Dynamic Array + simple 2‑D Matrix wrappers (educational)."""

class DynamicArray:
    def __init__(self):
        self._data = []

    # ---------- Core operations ----------
    def insert(self, index, value):
        """Insert value at index (amortized O(n))."""
        self._data.insert(index, value)

    def delete(self, index):
        """Delete element at index and return it (O(n))."""
        return self._data.pop(index)

    def access(self, index):
        """Access element at index (O(1))."""
        return self._data[index]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"DynamicArray({self._data})"


class Matrix:
    """Very small wrapper to illustrate 2‑D access."""
    def __init__(self, rows, cols, fill=0):
        self._rows = rows
        self._cols = cols
        self._data = [[fill for _ in range(cols)] for _ in range(rows)]

    def set(self, r, c, value):
        self._data[r][c] = value

    def get(self, r, c):
        return self._data[r][c]

    def __repr__(self):
        return "\n".join(" ".join(map(str, row)) for row in self._data)
