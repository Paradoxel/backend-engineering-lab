# Git Commit

## What is a Commit?

A **commit** is a snapshot of your project at a specific point in time.

It records the changes you have made and stores them in the repository history.

---

## Why Commit?

Commits allow you to:

* Save your progress.
* Track project history.
* Restore previous versions.
* Understand what changed over time.

---

## Commit Workflow

```text
Working Directory
        ↓
git add
        ↓
Staging Area
        ↓
git commit
        ↓
Repository
```

---

## Good Commit Messages

A good commit should:

* Describe one logical change.
* Be short and meaningful.
* Explain **what** changed.

Examples:

```text
feat(auth): add JWT authentication

fix(blog): resolve pagination bug

refactor(models): simplify product model

docs(notes): update Django views documentation
```

---

## Best Practices

* Keep commits small.
* One commit = One logical change.
* Write clear commit messages.
* Commit frequently during development.

---

## Summary

A commit is a saved snapshot of your project that records a meaningful change in the repository history.
