# Git Merge

## What is Merge?

**Merge** is the process of combining changes from one branch into another.

It is commonly used to integrate a completed feature branch back into the `main` branch.

---

## Why Merge?

Merge allows developers to:

* Combine completed work.
* Keep the main branch up to date.
* Collaborate without losing changes.

---

## Merge Workflow

```text
main
 │
 ├─────────────┐
 │             │
 ▼             │
feature/auth   │
 │             │
 │ Development │
 │             │
 └────Merge────┘
       │
       ▼
      main
```

---

## Merge Conflict

A **merge conflict** occurs when Git cannot automatically combine changes because the same part of a file was modified in different branches.

The developer must resolve the conflict manually before completing the merge.

---

## Best Practices

* Merge completed branches only.
* Pull the latest changes before merging.
* Resolve conflicts carefully.
* Delete merged branches if they are no longer needed.

---

## Summary

Merge combines the history of two branches into one, allowing completed work to become part of the main project.
