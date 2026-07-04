# Django URLs

`urls.py` is responsible for routing incoming HTTP requests to the appropriate view.

---

## URL Routing

Every request passes through Django's URL dispatcher before reaching a view.

```text
Request → urls.py → View → Response
```

---

## `path()`

Defines a URL pattern.

```python
path("blog/", views.blog, name="blog")
```

---

## `include()`

Splits URL configurations into multiple files for better project organization.

```python
path("blog/", include("blog.urls"))
```

---

## URL Parameters

Pass dynamic values through the URL.

```python
path("post/<int:id>/", views.post_detail)
```

Common converters:

* `int`
* `str`
* `slug`
* `uuid`
* `path`

---

## URL Names

Assign a unique name to every URL.

```python
path("login/", views.login_view, name="login")
```

Using names avoids hardcoded URLs.

---

## Namespace

Namespaces prevent URL name conflicts between applications.

```python
app_name = "blog"
```

Example:

```text
blog:post_detail
```

---

## `reverse()`

Generates a URL from its name.

```python
reverse("blog:post_detail", args=[1])
```

---

## `reverse_lazy()`

Lazy version of `reverse()`, commonly used in class-based views.

---

# Best Practices

* Use `include()` to organize large projects.
* Always define `name` for URLs.
* Avoid hardcoded URL paths.
* Use namespaces for reusable apps.
