"""
Minimal demo + micro‑benchmark for custom data‑structures.
Run:
    python datastructures_demo.py > output_datastructures.txt
"""

import time
from array_ops import DynamicArray
from stack_queue import ArrayStack, ArrayQueue
from linked_list import LinkedList
from tree_structure import TreeNode


def demo_dynamic_array():
    arr = DynamicArray()
    for i in range(5):
        arr.insert(len(arr), i)
    arr.delete(1)            # remove 2nd element
    return arr


def demo_stack_queue():
    s = ArrayStack()
    q = ArrayQueue()
    for ch in "ABCDE":
        s.push(ch)
        q.enqueue(ch)
    popped = s.pop()
    dequeued = q.dequeue()
    return s, popped, q, dequeued


def demo_linked_list():
    ll = LinkedList()
    for val in (10, 20, 30):
        ll.insert_end(val)
    ll.insert_front(5)
    ll.delete_value(20)
    return ll


def demo_tree():
    root = TreeNode("root")
    child1 = TreeNode("child1")
    child2 = TreeNode("child2")
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(TreeNode("leaf"))
    return list(root.preorder())


def micro_time(fn, *args, repeats=10_000):
    start = time.perf_counter()
    for _ in range(repeats):
        fn(*args)
    return (time.perf_counter() - start) / repeats


def benchmark():
    print("=== Data Structures Demo & Micro‑Benchmarks ===\n")

    # Dynamic array ops
    arr = DynamicArray()
    t_insert = micro_time(arr.insert, 0, 1)
    t_access = micro_time(arr.access, 0)
    t_delete = micro_time(lambda: arr.delete(0))
    print(f"DynamicArray  insert: {t_insert:1.7f}s  access: {t_access:1.7f}s  delete: {t_delete:1.7f}s")

    # Stack/Queue
    s = ArrayStack()
    q = ArrayQueue()
    t_push  = micro_time(s.push, 1)
    t_pop   = micro_time(lambda: s.pop() if not s.is_empty() else s.push(1))
    t_enq   = micro_time(q.enqueue, 1)
    t_deq   = micro_time(lambda: q.dequeue() if not q.is_empty() else q.enqueue(1))
    print(f"ArrayStack    push  : {t_push:1.7f}s  pop  : {t_pop:1.7f}s")
    print(f"ArrayQueue    enque : {t_enq:1.7f}s  deque: {t_deq:1.7f}s\n")

    # Demonstrations
    print("Structure states after small scripted operations:")
    print("DynamicArray →", demo_dynamic_array())
    s_state, pop_val, q_state, deq_val = demo_stack_queue()
    print("Stack        →", s_state, "(popped", pop_val, ")")
    print("Queue        →", q_state, "(dequeued", deq_val, ")")
    print("LinkedList   →", demo_linked_list())
    print("Tree preorder→", demo_tree())


if __name__ == "__main__":
    benchmark()
