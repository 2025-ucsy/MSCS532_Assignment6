# MSCS532 — Assignment 6  
**Medians & Order Statistics + Elementary Data Structures**

---

## 1 . Overview  
This assignment is split into two completely independent parts:

| Part | Goal | Key Files |
|------|------|-----------|
| **Part 1 – Selection Algorithms** | Implement and evaluate two order–statistics algorithms that return the *k*‑th smallest value.  • `deterministic_select.py` – worst‑case Θ(n) (Median‑of‑Medians)  • `randomized_select.py` – expected Θ(n) (Randomized Quick‑Select) | `Part1_SelectionAlgorithms/` |
| **Part 2 – Elementary Data Structures** | Build fundamental data‑structure building blocks from scratch and micro‑benchmark their operations: dynamic array, stack, queue, singly linked list, and a simple rooted tree. | `Part2_DataStructures/` |

Each part has its own driver/analysis script that produces plain‑text output which is captured in `*_output results.txt`.

---

## 2 . Repository Layout
```text
MSCS532_Assignment6/
├── Part1_SelectionAlgorithms
│   ├── deterministic_select.py
│   ├── randomized_select.py
│   ├── selection_analysis.py      # driver – prints timing table
│   └── part1_output results.txt   # saved console output
│
├── Part2_DataStructures
│   ├── array_ops.py               # dynamic array implementation + micro‑benchmarks
│   ├── stack_queue.py             # stack & queue built on the dynamic array
│   ├── linked_list.py
│   ├── tree_structure.py
│   ├── datastructures_demo.py     # driver – demos + timings
│   └── part2_output result.txt
│
└── README.md
``` 


## 3 . How to Run Everything

> **Prerequisites:** Python 3.8 + (only `time` from stdlib is required)
>
> Clone the repo and move into the folder first.

```bash
# ----- Part 1 -----
cd Part1_SelectionAlgorithms
python selection_analysis.py          # prints timing table
# also writes the same table to part1_output results.txt

# ----- Part 2 -----
cd ../Part2_DataStructures
python datastructures_demo.py         # prints micro‑benchmarks + small demo
# output is additionally stored in part2_output result.txt
``` 

## Part 1 output results
<img width="1920" height="1028" alt="image" src="https://github.com/user-attachments/assets/b37e775e-61ed-45ba-9fbf-d2202f7ada1c" />

## Part 2 output results
<img width="1920" height="1028" alt="image" src="https://github.com/user-attachments/assets/2c06a26f-8a59-407b-b1de-ba460a437691" />


