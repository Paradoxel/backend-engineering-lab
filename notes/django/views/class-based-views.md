# Class-Based Views (CBV)

## Definition

A Class-Based View (CBV) is a **Python class** that handles HTTP requests and returns HTTP responses.

Instead of writing a function, you define a class that inherits from Django's `View`.

---

## Syntax

```python
from django.views import View

class HomeView(View):

    def get(self, request):
        ...
```

---

## Example

```python
from django.http import HttpResponse
from django.views import View

class HomeView(View):

    def get(self, request):
        return HttpResponse("Hello Django")
```

---

## Advantages

- Reusable
- Less code duplication
- Easy to extend
- Supports inheritance

---

## Disadvantages

- More abstraction
- Harder for beginners
- Request flow is less obvious

---

## When should I use CBVs?

- Large projects
- Reusable views
- Generic Views
- DRY code

---

## Summary

- CBVs are Python classes.
- They inherit from Django's `View`.
- HTTP methods (`GET`, `POST`, etc.) are implemented as class methods.
- They are more scalable than FBVs.