# Function-Based Views (FBV)

## Definition

A Function-Based View (FBV) is a **Python function** that receives an HTTP request and returns an HTTP response.

---

## Syntax

```python
def my_view(request):
    ...
    return response
```

---

## Example

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Django")
```

---

## Advantages

- Simple
- Easy to read
- Explicit
- Great for small views

---

## Disadvantages

- Code duplication
- Harder to reuse
- Becomes messy in large projects

---

## When should I use FBVs?

- Small projects
- Simple logic
- Learning Django
- Views with little complexity

---

## Summary

- FBVs are normal Python functions.
- They receive a `request`.
- They return an `HttpResponse`.
- They are simple but less reusable than CBVs.