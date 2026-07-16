# Git Rebase

## What is Rebase?

`git rebase` is a command used to move your branch commits on top of another branch.

The main purpose of rebase is to create a **clean and linear history**.

---

## Rebase Example

Before rebase:

```text
main:

A---B---C---F


feature:

A---B---C---D---E
```

Run:

```bash
git checkout feature
git rebase main
```

After rebase:

```text
A---B---C---F---D'---E'
```

Git takes your feature commits and applies them again on top of the latest `main`.

---

## Merge vs Rebase

### Merge

Merge combines two histories and creates a new merge commit.

```text
A---B---C---F
     \       \
      D---E---M
```

Characteristics:

* Keeps the original history.
* Creates a merge commit.
* Safer for shared branches.
* Does not rewrite history.

---

### Rebase

Rebase moves your commits to a new base.

```text
A---B---C---F---D'---E'
```

Characteristics:

* Creates a linear history.
* Does not create a merge commit.
* Rewrites commit history.
* Best for personal feature branches.

---

## When to Use Rebase?

Good use cases:

* Cleaning a feature branch before a Pull Request.
* Keeping project history simple.
* Updating your local branch with the latest main changes.

Avoid using rebase on shared branches like:

```text
main
develop
```

because it changes commit history.

---

## Simple Rule

```text
Merge:
Combine two histories.

Rebase:
Move your history on top of another branch.
```

---

## Summary

* `merge` is safer and keeps the full history.
* `rebase` creates a cleaner linear history.
* Both combine code changes, but they organize Git history differently.
* For most projects, use merge for final integration and rebase mainly for cleaning personal branches.
