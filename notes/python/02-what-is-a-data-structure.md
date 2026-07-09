# What is a Data Structure?

## What is a Data Structure? (Recap)

A data structure is a specific arrangement of data in memory, governed by defined rules that guarantee predictable behavior for operations like access, search, insertion, and deletion. It's the *noun* — the shape data takes, not the process that builds it.

---

## Why Classify Data Structures?

Not all data structures serve the same purpose. Knowing how they're classified helps you quickly narrow down *which* structure fits a given problem, instead of memorizing dozens of unrelated names.

---

## Classification 1: Linear vs Non-Linear

- **Linear** — elements are arranged sequentially; each element (except the first/last) has exactly one predecessor and one successor.
  - Examples: Array, Linked List, Stack, Queue
- **Non-Linear** — elements are connected in a hierarchical or networked way; an element can connect to multiple others.
  - Examples: Tree, Graph, Heap

---

## Classification 2: Primitive vs Non-Primitive

- **Primitive** — basic data types built directly into the language (int, float, char, boolean). These are the raw material.
- **Non-Primitive** — structures built by combining primitives (Array, Linked List, Stack, Tree, etc.).

---

## Classification 3: Static vs Dynamic

- **Static** — fixed size, decided at creation time (e.g., a traditional array in C).
  - Fast access, but wastes memory if underused, or overflows if undersized.
- **Dynamic** — size can grow/shrink at runtime (e.g., Python's `list`, Linked List).
  - Flexible, but often with extra memory/time overhead for resizing.

---

## Classification 4: Linear Data Structures Overview

| Structure    | Access | Insert (end) | Insert (start) | Search |
|--------------|--------|---------------|-----------------|--------|
| Array        | O(1)   | O(1)*         | O(n)            | O(n)   |
| Linked List  | O(n)   | O(1)          | O(1)            | O(n)   |
| Stack        | O(n)   | O(1) (top)    | —               | O(n)   |
| Queue        | O(n)   | O(1) (rear)   | O(1) (front)    | O(n)   |

*Array insert at end is O(1) only if there's free space; otherwise O(n) due to resizing.

---

## Classification 5: Non-Linear Data Structures Overview

| Structure | Typical Use Case                          |
|-----------|--------------------------------------------|
| Tree      | Hierarchical data (file systems, DOM, DB indexes) |
| Graph     | Networked relationships (social networks, maps, routing) |
| Heap      | Priority-based access (priority queues, scheduling) |

---

## The Core Trade-off: Time vs Space

Every data structure makes a trade-off between:

- **Time efficiency** — how fast operations run
- **Space efficiency** — how much memory is used

Example: a Hash Table gives near O(1) lookup (time win) but uses extra memory for the hash table itself (space cost) compared to a plain array.

There's no single "best" structure — only the *right* structure for the specific operations your problem needs most.

---

## How to Choose a Data Structure

Ask these questions:

1. Do I need fast lookups by index/key? → Array or Hash Table
2. Do I need fast insertion/deletion at the ends? → Linked List, Stack, Queue
3. Is my data hierarchical? → Tree
4. Is my data a network of relationships? → Graph
5. Do I need to always access the smallest/largest element quickly? → Heap

---

## Key Concepts

- Linear vs Non-Linear
- Primitive vs Non-Primitive
- Static vs Dynamic
- Time-Space Trade-off

---

## Summary

Data structures are classified by how they're arranged (linear vs non-linear), how they're built (primitive vs non-primitive), and how they behave at runtime (static vs dynamic). Choosing the right one always comes down to a trade-off between time and space efficiency, matched to the specific operations your problem demands most.