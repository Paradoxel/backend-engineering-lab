# Django Views

A **View** is a Python function or class responsible for handling an incoming HTTP request, executing the application's logic, and returning an HTTP response.

A view is the place where Django decides **what should happen** after a request reaches the application.

---

# Request Lifecycle

Every request follows this flow:

```text
Browser
    │
    ▼
Request
    │
    ▼
urls.py
    │
    ▼
View
    │
    ▼
Response
    │
    ▼
Browser
```

* `urls.py` decides **which view** should handle the request.
* The view processes the request.
* The view returns an HTTP response.

---

# Types of Views

Django provides two main ways to write views.

## Function-Based Views (FBV)

A Function-Based View is simply a Python function.

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")
```

Characteristics:

* Easy to understand.
* Explicit flow.
* Good for simple logic.
* Full control over implementation.

---

## Class-Based Views (CBV)

A Class-Based View organizes logic inside a class.

```python
from django.views import View
from django.http import HttpResponse

class HomeView(View):

    def get(self, request):
        return HttpResponse("Hello, World!")
```

Characteristics:

* Better for reusable code.
* Supports inheritance.
* Less repetitive for CRUD operations.
* Used heavily with Django's Generic Views.

---

# FBV vs CBV

| FBV                    | CBV                           |
| ---------------------- | ----------------------------- |
| Function               | Class                         |
| Simple                 | More structured               |
| Easier to learn        | Easier to reuse               |
| Better for small views | Better for large applications |

Neither is "better". The choice depends on the project's complexity.

---

# Request Object

Every view receives a `request` object.

Common attributes:

```python
request.method
request.GET
request.POST
request.user
request.session
request.FILES
```

Examples:

* `request.method` → HTTP method (`GET`, `POST`, etc.)
* `request.GET` → Query parameters.
* `request.POST` → Submitted form data.
* `request.user` → Current authenticated user.
* `request.session` → Session data.
* `request.FILES` → Uploaded files.

---

# Response Objects

Every Django view **must return an HTTP response**.

If a view doesn't return a response, Django raises an error.

Common response classes include:

* `HttpResponse`
* `JsonResponse`
* `FileResponse`
* `StreamingHttpResponse`
* `HttpResponseRedirect`

---

# HttpResponse

`HttpResponse` represents the response sent back to the client.

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome!")
```

Most other response classes inherit from `HttpResponse`.

---

# render()

`render()` is a shortcut that renders a template and returns an `HttpResponse`.

```python
from django.shortcuts import render

def home(request):
    return render(request, "home.html")
```

With context:

```python
return render(
    request,
    "home.html",
    {
        "title": "Home Page",
    },
)
```

Use `render()` when returning HTML pages.

---

# redirect()

`redirect()` returns an HTTP redirect response.

```python
from django.shortcuts import redirect

def home(request):
    return redirect("blog:index")
```

The browser receives the redirect response and automatically sends a new request to the destination URL.

Use `redirect()` when you want the user to navigate to another page.

---

# get_object_or_404()

Safely retrieves a single object.

```python
from django.shortcuts import get_object_or_404

post = get_object_or_404(Post, pk=id)
```

If the object does not exist, Django automatically returns a **404 Not Found** response.

---

# Best Practices

* Keep views focused on one responsibility.
* Avoid placing complex business logic directly inside views.
* Use `render()` for HTML responses.
* Use `redirect()` after successful actions (such as creating or updating data).
* Prefer `get_object_or_404()` instead of manually handling `DoesNotExist`.
* Choose FBV or CBV based on readability and project complexity.

---

# Summary

A Django View:

* Receives an HTTP request.
* Executes application logic.
* Returns an HTTP response.

Common shortcuts:

* `HttpResponse()` → Plain HTTP response.
* `render()` → Render a template.
* `redirect()` → Redirect to another URL.
* `get_object_or_404()` → Retrieve an object safely.

Django supports two styles of writing views:

* Function-Based Views (FBV)
* Class-Based Views (CBV)
