# Git Stash

## What is Stash?

`git stash` temporarily saves your uncommitted changes so you can work on something else without creating a commit.

---

## Save Current Changes

```bash
git stash
```

---

## View Saved Stashes

```bash
git stash list
```

---

## Restore the Latest Stash

```bash
git stash pop
```

Restores the changes and removes them from the stash list.

---

## Restore Without Removing

```bash
git stash apply
```

Restores the changes but keeps the stash.

---

## Typical Workflow

```text
Working on Feature A
        │
        ▼
git stash
        │
        ▼
Switch Branch
        │
        ▼
Fix Bug
        │
        ▼
git stash pop
        │
        ▼
Continue Feature A
```

---

## Summary

* `git stash` temporarily saves uncommitted changes.
* `git stash pop` restores and removes the latest stash.
* `git stash apply` restores without removing it.
* Useful when you need to switch branches without committing unfinished work.
