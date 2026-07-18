# CBV Life Cycle

## Request Flow

```text
Request
    │
    ▼
URL
    │
    ▼
as_view()
    │
    ▼
dispatch()
    │
    ├── GET  → get()
    ├── POST → post()
    ├── PUT  → put()
    └── ...
    │
    ▼
Response
```

---

## Execution Order

1. URL resolves the View.
2. `as_view()` creates the View instance.
3. `dispatch()` determines the HTTP method.
4. Django calls the corresponding method (`get()`, `post()`, ...).
5. The View returns an `HttpResponse`.

---

## Key Methods

| Method | Purpose |
|--------|---------|
| `as_view()` | Converts the class into a callable view |
| `dispatch()` | Routes the request to the correct HTTP method |
| `get()` | Handles GET requests |
| `post()` | Handles POST requests |

---

## Summary

- Every CBV starts with `as_view()`.
- `dispatch()` decides which method to execute.
- HTTP methods (`get()`, `post()`, ...) contain the view logic.