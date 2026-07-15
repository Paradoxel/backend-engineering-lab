# Push & Pull

## Git Push

`git push` sends your local commits to the remote repository (e.g., GitHub).

```bash
git push
```

First push for a new branch:

```bash
git push -u origin main
```

After that:

```bash
git push
```

is enough.

---

## Git Pull

`git pull` downloads the latest changes from the remote repository **and merges** them into your local branch.

```bash
git pull
```

Use it before starting work to keep your local repository up to date.

---

## Git Fetch

`git fetch` downloads changes from the remote repository **without merging** them.

```bash
git fetch
```

This lets you review incoming changes before updating your branch.

---

## Fetch vs Pull

| Command     | Downloads Changes | Merges Changes |
| ----------- | ----------------- | -------------- |
| `git fetch` | ✅                 | ❌              |
| `git pull`  | ✅                 | ✅              |

---

## Typical Workflow

```text
Write Code
      │
      ▼
git add
      │
      ▼
git commit
      │
      ▼
git push
```

When returning to the project:

```text
git pull
      │
      ▼
Continue Coding
```

---

## Summary

* `git push` uploads your commits to the remote repository.
* `git pull` downloads and merges the latest changes.
* `git fetch` only downloads changes without modifying your local branch.
* In daily development, the most common commands are `git push` and `git pull`.
