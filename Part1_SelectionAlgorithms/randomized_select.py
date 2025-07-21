"""
Randomized Quickselect.
Expected time complexity: Θ(n)  |  Worst case: Θ(n²) (rare).
"""

import random

def _partition(arr, lo, hi):
    """Lomuto partition. Returns final pivot index."""
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i


def quickselect(arr, k, lo=0, hi=None):
    """
    :param arr: list (will be modified in‑place)
    :param k:   zero‑based rank to find
    :return:    arr[k] (k‑th smallest)
    """
    if hi is None:
        hi = len(arr) - 1
    if not (0 <= k < len(arr)):
        raise IndexError("k out of range")

    while True:
        # Random pivot to avoid worst‑case patterns
        pivot_idx = random.randint(lo, hi)
        arr[pivot_idx], arr[hi] = arr[hi], arr[pivot_idx]

        p = _partition(arr, lo, hi)

        if p == k:
            return arr[p]
        elif p > k:
            hi = p - 1
        else:
            lo = p + 1
