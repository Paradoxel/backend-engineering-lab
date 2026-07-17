# What is a View?

## Definition

A **View** receives an HTTP request and returns an HTTP response.

It decides **what should happen** after a client accesses a URL.

---

## Request Flow

```text
Browser
   │
   ▼
Request
   │
   ▼
URL
   │
   ▼
View
   │
   ▼
Response
```

---

## Responsibilities

A View can:

- Receive requests
- Query the database
- Execute business logic
- Render templates
- Return JSON
- Redirect users

---

## Example

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Django")
```

---

## Summary

- Every request eventually reaches a View.
- A View connects URLs with application logic.
- A View always returns an **HttpResponse**.