# FBV vs CBV

## FBV (Function-Based View)

✔ Python function

✔ Simple & explicit

✔ Easy to understand

✔ Best for small views

```python
def home(request):
    ...
```

---

## CBV (Class-Based View)

✔ Python class

✔ Reusable

✔ Supports inheritance

✔ Best for large projects

```python
class HomeView(View):
    ...
```

---

## Comparison

| FBV | CBV |
|------|------|
| Function | Class |
| Simple | Reusable |
| Explicit | More abstraction |
| Easy to learn | Easy to extend |
| Less reusable | Less code duplication |

---

## When to use FBV

- Small projects
- Simple business logic
- Quick prototypes
- Learning Django

---

## When to use CBV

- Large projects
- CRUD applications
- Generic Views
- Reusable logic
- DRY code

---

## Common Misconception

❌ CBV is better than FBV.

✅ Neither is better.

Choose the one that keeps your code **simpler** and **more maintainable**.

---

## Personal Rule

Use **FBV** when:

- The view is simple.
- It will probably never be reused.

Use **CBV** when:

- The view has CRUD behavior.
- You need inheritance.
- You want reusable components.

---

## Summary

- FBV focuses on **simplicity**.
- CBV focuses on **reusability**.
- Both solve the same problem.
- A professional Django developer should know both.