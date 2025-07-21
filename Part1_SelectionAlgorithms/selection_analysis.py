"""
Benchmark deterministic vs. randomized selection plus MergeSort baseline
to illustrate Θ(n) vs. Θ(n log n) behaviour.

Run:
    python selection_analysis.py > output_selection.txt
"""

import random, time, statistics, sys, os
from deterministic_select import select as deterministic_select
from randomized_select import quickselect as randomized_select

sys.setrecursionlimit(10_000)   # enough for 10k Quickselect worst cases


def _time_it(fn, data, k, trials=3):
    """Return average run‑time over <trials> executions."""
    elapsed = []
    for _ in range(trials):
        arr = data.copy()
        t0 = time.perf_counter()
        fn(arr, k)
        elapsed.append(time.perf_counter() - t0)
    return statistics.mean(elapsed)


def benchmark():
    sizes = [1000, 5000, 10_000]
    print("Empirical Timing Benchmark\n")

    for dist in ("Random", "Sorted", "Reverse‑sorted"):
        print(f"=== {dist} arrays ===")
        for n in sizes:
            if dist == "Random":
                arr = [random.randint(0, 10_000_000) for _ in range(n)]
            elif dist == "Sorted":
                arr = list(range(n))
            else:
                arr = list(range(n, 0, -1))

            k = n // 2                           # median
            t_det  = _time_it(deterministic_select, arr, k)
            t_rand = _time_it(randomized_select,  arr, k)
            t_merge = _time_it(lambda a, _: sorted(a)[k], arr, k)  # O(n log n) baseline

            print(f"n={n:6}:  Det  {t_det:0.4f}s │ Rand  {t_rand:0.4f}s │ Merge {t_merge:0.4f}s")
        print()

if __name__ == "__main__":
    benchmark()

    # Save to file if running interactively (stdout already redirected when using >)
    if sys.stdout.isatty():  # interactive
        with open("output_selection.txt", "w", encoding="utf‑8") as f:
            # re‑run so output goes to file
            orig_stdout = sys.stdout
            sys.stdout = f
            benchmark()
            sys.stdout = orig_stdout
            print("\nCreated output_selection.txt")
