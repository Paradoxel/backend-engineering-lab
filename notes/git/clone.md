# Git Clone

## What is Clone?

`git clone` creates a local copy of an existing remote repository.

It downloads:

* Project files
* Commit history
* Branches
* Remote configuration (`origin`)

---

## Basic Syntax

```bash
git clone <repository-url>
```

Example:

```bash
git clone https://github.com/username/project.git
```

---

## Clone into a Custom Folder

```bash
git clone <repository-url> my-project
```

Example:

```bash
git clone https://github.com/username/project.git backend
```

---

## What Happens After Clone?

```text
GitHub Repository
        │
        ▼
git clone
        │
        ▼
Local Repository
```

Git automatically creates a remote named:

```text
origin
```

---

## Summary

* `git clone` downloads an existing repository.
* It copies both the project files and Git history.
* The default remote created after cloning is `origin`.
