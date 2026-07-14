# Git Branch

## What is a Branch?

A **branch** is an independent line of development within a Git repository.

It allows developers to work on new features or fixes without affecting the main codebase.

---

## Why Use Branches?

Branches help developers:

* Develop new features safely.
* Fix bugs independently.
* Experiment without risking the main project.
* Collaborate with other developers.

---

## Main Branch

Most repositories have a default branch, usually called:

```text
main
```

The `main` branch should always contain a stable version of the project.

---

## Feature Branch

Instead of working directly on `main`, create a separate branch for each task.

Example:

```text
main
 ├── feature/authentication
 ├── feature/payment
 └── fix/login-bug
```

Each branch focuses on one logical change.

---

## Benefits

* Isolates changes.
* Reduces conflicts.
* Makes collaboration easier.
* Keeps the `main` branch stable.

---

## Best Practices

* Never develop directly on `main`.
* One branch = One feature or bug fix.
* Use clear branch names.
* Delete merged branches when they are no longer needed.

---

## Summary

A branch is an isolated workspace that allows you to develop features or fix bugs safely without affecting the main project.
