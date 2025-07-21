"""
Deterministic linear‑time selection (Median‑of‑Medians).
Returns the k‑th smallest element (0‑indexed).
Worst‑case time complexity: Θ(n)
"""

from math import ceil

def _partition(arr, pivot):
    """Partition arr into (< pivot, == pivot, > pivot) lists."""
    less, equal, greater = [], [], []
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x > pivot:
            greater.append(x)
        else:
            equal.append(x)
    return less, equal, greater


def select(arr, k):
    """
    :param arr: list of comparable items
    :param k:   zero‑based index of order statistic (0 ≤ k < len(arr))
    :return:    the k‑th smallest element
    """
    if not (0 <= k < len(arr)):
        raise IndexError("k out of range")

    # Base case: small arrays -> sort directly
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Step 1: split into groups of five and compute medians
    medians = []
    for i in range(0, len(arr), 5):
        group = sorted(arr[i:i + 5])
        medians.append(group[len(group) // 2])

    # Step 2: recursively find true median of medians
    pivot = select(medians, len(medians) // 2)

    # Step 3: partition around pivot
    less, equal, greater = _partition(arr, pivot)

    if k < len(less):
        return select(less, k)
    elif k < len(less) + len(equal):
        return pivot                    # k is in the pivot block
    else:
        return select(greater, k - len(less) - len(equal))
