# Git Tag

## What is a Git Tag?

A Git tag is a reference that points to a specific commit.

It is mainly used to mark important points in a project's history, such as:

* Releases
* Stable versions
* Production deployments

Example:

```text
v1.0.0
v1.1.0
v2.0.0
```

---

## Why Use Tags?

Branches move as new commits are added:

```text
main:

A---B---C---D---E
                ↑
              main
```

A tag stays attached to a specific commit:

```text
A---B---C---D---E
        ↑
      v1.0.0
```

This allows developers to always access a specific version of the project.

---

## Create a Tag

Create a simple tag:

```bash
git tag v1.0.0
```

Create an annotated tag (recommended):

```bash
git tag -a v1.0.0 -m "First stable release"
```

---

## View Tags

```bash
git tag
```

Show information about a tag:

```bash
git show v1.0.0
```

---

## Push Tags to Remote

Tags are not automatically pushed with commits.

Push one tag:

```bash
git push origin v1.0.0
```

Push all tags:

```bash
git push origin --tags
```

---

## Delete a Tag

Delete local tag:

```bash
git tag -d v1.0.0
```

Delete remote tag:

```bash
git push origin --delete v1.0.0
```

---

## Tag Workflow Example

A common release workflow:

```text
Development
     |
     ↓
Commit changes
     |
     ↓
Merge into main
     |
     ↓
Create tag
     |
     ↓
Release version
```

Example:

```bash
git checkout main

git pull origin main

git tag -a v1.0.0 -m "Production release"

git push origin v1.0.0
```

---

## Summary

* A tag marks a specific commit.
* Tags are mainly used for releases and versioning.
* Unlike branches, tags usually do not move.
* Tags help teams identify stable versions of a project.

Example:

```text
v1.0.0 → First production release
v1.1.0 → New features
v2.0.0 → Major changes
```
