# Query Parameters

## What is a Query Parameter?

A **Query Parameter** is an optional value passed through the URL after `?`.

Example:

```text
/posts?page=2
```

Here:

```text
page=2
```

is a query parameter.

Multiple query parameters are separated using `&`:

```text
/posts?page=2&limit=10
```

---

## Basic Syntax

FastAPI automatically detects function parameters that are not part of the path as query parameters.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/posts")
def get_posts(page: int = 1):
    return {"page": page}
```

Request:

```text
GET /posts?page=2
```

Response:

```json
{
    "page": 2
}
```

---

## Query Parameters Are Optional by Default

A default value makes a query parameter optional:

```python
@app.get("/posts")
def get_posts(page: int = 1):
    ...
```

Both requests are valid:

```text
/posts
/posts?page=2
```

If `page` is not provided:

```python
page = 1
```

---

## Required Query Parameters

A query parameter becomes required when it doesn't have a default value.

```python
@app.get("/posts")
def search_posts(search: str):
    return {"search": search}
```

Valid:

```text
/posts?search=django
```

Without `search`, FastAPI returns a validation error.

---

## Multiple Query Parameters

You can define multiple query parameters:

```python
@app.get("/posts")
def get_posts(
    page: int = 1,
    limit: int = 10,
    search: str | None = None
):
    return {
        "page": page,
        "limit": limit,
        "search": search
    }
```

Example:

```text
/posts?page=2&limit=20&search=django
```

---

## Query Parameter Validation

FastAPI can validate query parameters using `Query`.

```python
from typing import Annotated
from fastapi import Query


@app.get("/posts")
def get_posts(
    page: Annotated[int, Query(gt=0)] = 1
):
    return {"page": page}
```

Now:

```text
?page=2
```

is valid.

But:

```text
?page=0
```

is rejected because `page` must be greater than `0`.

---

## Common Use Cases

Query parameters are commonly used for:

- Filtering
- Searching
- Pagination
- Sorting
- Limiting results

Example:

```text
/posts?category=django&page=2&limit=10
```

---

## Path Parameters vs Query Parameters

### Path Parameter

Usually identifies a specific resource:

```text
/posts/15
```

```python
@app.get("/posts/{post_id}")
def get_post(post_id: int):
    ...
```

### Query Parameter

Usually controls how resources are retrieved:

```text
/posts?page=2&limit=10
```

```python
@app.get("/posts")
def get_posts(
    page: int = 1,
    limit: int = 10
):
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

## Query Parameters and Type Hints

FastAPI uses type hints to parse and validate query parameters.

```python
@app.get("/posts")
def get_posts(page: int = 1):
    ...
```

Request:

```text
/posts?page=2
```

FastAPI converts:

```text
"2"
```

from the URL into:

```python
2
```

as an integer.

If the value cannot be converted:

```text
/posts?page=abc
```

FastAPI returns a validation error.

---

## Summary

- Query Parameters are passed after `?`.
- Multiple parameters are separated with `&`.
- They are optional when a default value is provided.
- Type hints control parsing and validation.
- `Query()` provides additional validation and metadata.
- They are commonly used for filtering, searching, pagination, and sorting.