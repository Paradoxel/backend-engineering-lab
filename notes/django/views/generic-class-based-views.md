# Generic Class-Based Views (Generic CBVs)

## Definition

Generic CBVs are pre-built Class-Based Views that implement common CRUD behavior.

They reduce repetitive code and follow Django conventions.

---

## Why do we need them?

Instead of implementing the same CRUD logic repeatedly, Django provides reusable generic views.

---

## Common Generic Views

| View | Purpose |
|------|---------|
| `View` | Base class for all Class-Based Views |
| `TemplateView` | Render a template |
| `ListView` | Display a list of objects |
| `DetailView` | Display a single object |
| `CreateView` | Create an object |
| `UpdateView` | Update an object |
| `DeleteView` | Delete an object |
---

## Example

```python
class PostListView(ListView):
    model = Post
```

---

## Advantages

- Less boilerplate
- Reusable
- Faster development

---

## Summary

- Generic CBVs are built on top of CBVs.
- They simplify common CRUD operations.
- Prefer them when the default behavior fits your needs.