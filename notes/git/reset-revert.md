# Git Reset & Revert

## Git Reset

`git reset` moves the current branch to another commit and can also change the staging area and working directory.

### `--soft`

Moves `HEAD` but keeps changes staged.

```bash
git reset --soft HEAD~1
```

Useful when you want to undo the last commit but keep its changes ready to commit again.

---

### `--mixed`

Moves `HEAD` and unstages the changes, but keeps them in the working directory.

```bash
git reset --mixed HEAD~1
```

This is the default behavior of `git reset`.

---

### `--hard`

Moves `HEAD` and removes the changes from the staging area and working directory.

```bash
git reset --hard HEAD~1
```

⚠️ Use carefully because uncommitted changes can be lost.

---

## Git Revert

`git revert` creates a **new commit** that reverses the changes introduced by an earlier commit.

```bash
git revert <commit-hash>
```

Unlike `reset`, it does not remove the original commit from history.

---

## Reset vs Revert

| Command         | What it does                            | History           |
| --------------- | --------------------------------------- | ----------------- |
| `reset --soft`  | Move `HEAD`, keep changes staged        | Rewrites history  |
| `reset --mixed` | Move `HEAD`, unstage changes            | Rewrites history  |
| `reset --hard`  | Move `HEAD`, discard changes            | Rewrites history  |
| `revert`        | Create a new commit that undoes changes | Preserves history |

---

## When Should I Use Them?

### Use `reset`

Usually for **local commits** that have not been shared with others.

```text
Local branch
    ↓
Reset
    ↓
Rewrite history
```

### Use `revert`

Prefer it when the commit has already been pushed or shared.

```text
Shared history
      ↓
   Revert
      ↓
New commit
      ↓
Original history preserved
```

---

## Mental Model

Git can be viewed as three main areas:

```text
Working Directory
       ↓ git add
Staging Area
       ↓ git commit
Repository
```

`reset` can affect one or more of these areas depending on the selected option.

---

## Summary

* `reset` rewrites commit history.
* `--soft` keeps changes staged.
* `--mixed` keeps changes but unstages them.
* `--hard` discards changes.
* `revert` creates a new commit to undo an earlier commit.
* Use `reset` mainly for local history.
* Use `revert` when working with shared history.
