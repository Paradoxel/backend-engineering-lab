# Remote Repository

## What is a Remote?

A **remote repository** is a Git repository hosted on another machine or a platform like GitHub.

It allows developers to:

* Backup their code
* Collaborate with others
* Synchronize changes between local and remote repositories

---

## Local vs Remote Repository

```text
Local Repository (Your Computer)
        │
        │  git push / git pull
        ▼
Remote Repository (GitHub)
```

---

## Origin

When you clone a repository, Git automatically creates a remote called:

```text
origin
```

`origin` is simply the default name of the remote repository.

---

## Useful Commands

### Show remotes

```bash
git remote -v
```

Displays all configured remote repositories.

---

### Add a remote

```bash
git remote add origin <repository-url>
```

Example:

```bash
git remote add origin https://github.com/username/project.git
```

---

### Remove a remote

```bash
git remote remove origin
```

---

### Rename a remote

```bash
git remote rename origin upstream
```

---

## Summary

* A remote repository is an online copy of your Git repository.
* `origin` is the default remote name.
* Use `git remote -v` to view configured remotes.
* Use `git remote add` to connect your local project to GitHub.
