# Path Parameters

## What is a Path Parameter?

A **Path Parameter** is a dynamic value included directly in the URL path.

For example:

```text
/posts/15
```

Here, `15` identifies a specific post.

---

## Basic Syntax

In FastAPI, path parameters are defined using `{}`:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    return {"post_id": post_id}
```

Request:

```text
GET /posts/15
```

Response:

```json
{
    "post_id": 15
}
```

The `{post_id}` in the path is connected to the `post_id` parameter of the function.

---

## Type Hints

The type hint determines how FastAPI parses and validates the parameter.

```python
@app.get("/posts/{post_id}")
def get_post(post_id: int):
    ...
```

Here `post_id` must be an integer.

```text
/posts/15
```

is valid.

But:

```text
/posts/abc
```

is invalid because `"abc"` cannot be converted to an integer.

FastAPI automatically returns a validation error.

---

## Multiple Path Parameters

A route can contain multiple parameters:

```python
@app.get("/users/{user_id}/posts/{post_id}")
def get_post(user_id: int, post_id: int):
    return {
        "user_id": user_id,
        "post_id": post_id
    }
```

Example:

```text
GET /users/10/posts/25
```

Result:

```json
{
    "user_id": 10,
    "post_id": 25
}
```

---

## Path Parameters Are Required

A Path Parameter is part of the URL structure, so it is required.

```python
@app.get("/posts/{post_id}")
def get_post(post_id: int):
    ...
```

This endpoint:

```text
/posts/15
```

exists.

But:

```text
/posts/
```

does not match the same route.

---

## Path Parameter Validation

FastAPI can validate parameters using type hints and additional constraints.

For example:

```python
from typing import Annotated
from fastapi import Path


@app.get("/posts/{post_id}")
def get_post(
    post_id: Annotated[int, Path(gt=0)]
):
    return {"post_id": post_id}
```

Now:

```text
/posts/10
```

is valid.

But:

```text
/posts/0
```

is rejected because `post_id` must be greater than `0`.

---

## Path Parameters vs Query Parameters

These two are commonly confused.

### Path Parameter

Used to identify a specific resource.

```text
/posts/15
```

```python
@app.get("/posts/{post_id}")
def get_post(post_id: int):
    ...
```

### Query Parameter

Usually used for filtering, searching, sorting, or pagination.

```text
/posts?page=2
```

```python
@app.get("/posts")
def get_posts(page: int = 1):
    ...
```

A useful mental model:

```text
Path Parameter
    ↓
Which resource?

Query Parameter
    ↓
How should I retrieve it?
```

---

## Path Parameter vs Query Parameter Example

Imagine a blog API.

```text
/posts/15
```

means:

> Give me post number 15.

While:

```text
/posts?category=django&page=2
```

means:

> Give me posts filtered by Django, on page 2.

---

## Path Order Matters

Consider:

```python
@app.get("/posts/{post_id}")
def get_post(post_id: int):
    ...


@app.get("/posts/latest")
def get_latest_post():
    ...
```

The order of route definitions can matter when a dynamic path could also match a static path.

A static route should generally be declared before a dynamic route when they could conflict:

```python
@app.get("/posts/latest")
def get_latest_post():
    ...


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    ...
```

This makes the intended route matching explicit.

---

## Summary

- Path Parameters are values inside the URL path.
- They are defined using `{}`.
- Type hints control parsing and validation.
- Path Parameters are required.
- `Path()` provides additional validation and metadata.
- Use Path Parameters mainly to identify resources.
- Use Query Parameters for filtering, searching, pagination, and similar options.