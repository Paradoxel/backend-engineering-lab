# Routing

## What is Routing?

Routing is the process of mapping an HTTP request to a specific function that handles it.

In FastAPI, a route is defined using a **path operation decorator**.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/posts")
def get_posts():
    return {"message": "All posts"}
```

Here:

- `@app.get()` → HTTP method
- `"/posts"` → URL path
- `get_posts()` → function that handles the request

---

## Path Operation

A FastAPI route is commonly called a **Path Operation**.

The main HTTP methods are:

```python
@app.get("/posts")
@app.post("/posts")
@app.put("/posts/{post_id}")
@app.patch("/posts/{post_id}")
@app.delete("/posts/{post_id}")
```

They represent different operations:

| Method | Purpose |
|---|---|
| `GET` | Retrieve data |
| `POST` | Create data |
| `PUT` | Replace data |
| `PATCH` | Partially update data |
| `DELETE` | Delete data |

---

## Path Operation Function

The function below the decorator is called when the matching request is received.

```python
@app.get("/posts")
def get_posts():
    return {"message": "All posts"}
```

The function can return data directly:

```python
@app.get("/health")
def health_check():
    return {"status": "ok"}
```

FastAPI converts the returned Python data into an HTTP response.

---

## Multiple Routes

A FastAPI application can contain multiple path operations:

```python
@app.get("/posts")
def get_posts():
    return {"message": "All posts"}


@app.get("/users")
def get_users():
    return {"message": "All users"}
```

Each route handles a different URL.

---

## APIRouter

For larger applications, routes can be grouped using `APIRouter`.

```python
from fastapi import APIRouter

router = APIRouter(prefix="/posts")


@router.get("/")
def get_posts():
    return {"message": "All posts"}
```

Then register the router:

```python
from fastapi import FastAPI

app = FastAPI()

app.include_router(router)
```

Now the endpoint becomes:

```text
GET /posts/
```

`APIRouter` helps organize routes by feature or resource.

---

## Summary

- Routing maps requests to handler functions.
- FastAPI uses path operation decorators to define routes.
- HTTP methods determine the type of operation.
- `APIRouter` helps organize routes in larger applications.