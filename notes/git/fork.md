# Git Fork

## What is Fork?

A **fork** creates a copy of someone else's repository under **your own GitHub account**.

Unlike `git clone`, a fork happens on **GitHub**, not on your local machine.

---

## Why Use Fork?

Fork is commonly used when:

* You want to contribute to an open-source project.
* You don't have write access to the original repository.
* You want your own independent copy on GitHub.

---

## Typical Workflow

```text
Original Repository
        │
        ▼
      Fork
        │
        ▼
Your GitHub Repository
        │
        ▼
git clone
        │
        ▼
Your Local Repository
```

---

## Fork vs Clone

| Fork                                   | Clone                                 |
| -------------------------------------- | ------------------------------------- |
| GitHub feature                         | Git command                           |
| Creates a copy on your GitHub account  | Creates a local copy on your computer |
| Used when you don't own the repository | Used to work on a repository locally  |

---

## Summary

* A fork creates your own copy of a repository on GitHub.
* A clone downloads a repository to your local machine.
* A common open-source workflow is: **Fork → Clone → Branch → Commit → Push → Pull Request**.
