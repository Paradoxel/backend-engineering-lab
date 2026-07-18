# Mixins

## Definition

A **Mixin** is a reusable class that adds extra functionality to another class through inheritance.

A Mixin is **not intended to be used alone**. It exists to extend another class.

---

## Why do we need Mixins?

Without Mixins:

```python
class PostListView(ListView):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            ...
```

If many Views need the same authentication logic, we would duplicate the code.

Instead, Django provides:

```python
class PostListView(LoginRequiredMixin, ListView):
    ...
```

Now every View can reuse the same behavior.

---

## Mental Model

```text
Mixin
   │
   ▼
Adds a new ability

LoginRequiredMixin
        +
     ListView

        ↓

Authenticated ListView
```

A Mixin **adds behavior**, it does not replace the original class.

---

# Multiple Inheritance

Mixins work because Python supports multiple inheritance.

```python
class A:
    ...

class B:
    ...

class C(A, B):
    ...
```

`C` inherits from both `A` and `B`.

This is exactly what Django uses.

---

# Django Example

```python
class PostListView(
    LoginRequiredMixin,
    ListView
):
    model = Post
```

Here the View inherits from:

- LoginRequiredMixin
- ListView

---

# MRO (Method Resolution Order)

The most important concept.

When multiple parent classes define the same method, Python must decide:

> Which one should execute first?

Python follows the **Method Resolution Order (MRO).**

Example:

```python
class MyView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ListView
):
    ...
```

Execution order:

```text
MyView

↓

LoginRequiredMixin

↓

PermissionRequiredMixin

↓

ListView

↓

View

↓

object
```

Python always searches from **left to right** following the MRO.

You can inspect it:

```python
print(MyView.mro())
```

---

# Why Mixins come first?

Correct:

```python
class PostListView(
    LoginRequiredMixin,
    ListView
):
    ...
```

Wrong:

```python
class PostListView(
    ListView,
    LoginRequiredMixin
):
    ...
```

Because Python resolves methods from left to right.

The authentication logic must execute **before** the normal View logic.

---

# Built-in Django Mixins

| Mixin | Purpose |
|--------|---------|
| `LoginRequiredMixin` | Require authentication |
| `PermissionRequiredMixin` | Require specific permissions |
| `UserPassesTestMixin` | Apply custom access rules |

---

# Custom Mixin

You can create your own reusable behavior.

Example:

```python
class StaffRequiredMixin:

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_staff:
            return HttpResponseForbidden()

        return super().dispatch(request, *args, **kwargs)
```

Usage:

```python
class DashboardView(
    StaffRequiredMixin,
    ListView
):
    ...
```

Now every View that inherits this Mixin automatically requires a staff user.

---

# Advantages

- Reusable
- DRY
- Easy to combine
- Cleaner Views

---

# Best Practices

- One responsibility per Mixin.
- Keep Mixins small.
- Place Mixins before the View class.
- Understand MRO before combining multiple Mixins.

---

# Summary

- A Mixin adds reusable behavior.
- Mixins rely on Python multiple inheritance.
- Python resolves methods using **MRO**.
- Order matters.
- Django uses Mixins extensively for authentication, permissions, and reusable View behavior.