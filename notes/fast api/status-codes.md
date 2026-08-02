# HTTP Status Codes

## What are Status Codes?

HTTP Status Codes indicate the result of an HTTP request.

Every API response includes a status code.

---

## Common Status Codes

### 200 OK

The request completed successfully.

```python id="j5jpsf"
@app.get("/users")
def get_users():
    return {"message": "Success"}
```

---

### 201 Created

A new resource was created successfully.

```python id="h02wud"
@app.post("/users", status_code=201)
def create_user():
    return {"message": "User created"}
```

---

### 204 No Content

The request succeeded but returns no response body.

Often used for delete operations.

---

### 400 Bad Request

The client sent an invalid request.

---

### 401 Unauthorized

Authentication is required.

---

### 403 Forbidden

The user is authenticated but does not have permission.

---

### 404 Not Found

The requested resource does not exist.

```python id="e1umgi"
raise HTTPException(status_code=404, detail="User not found")
```

---

### 422 Unprocessable Entity

Validation failed.

FastAPI automatically returns this when request data does not match the Pydantic model.

---

### 500 Internal Server Error

An unexpected server error occurred.

---

## HTTPException

FastAPI provides `HTTPException` for returning error responses.

```python id="svqdmq"
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="User not found",
)
```

---

## Best Practices

* Use the correct status code for every response.
* Do not always return `200 OK`.
* Use `HTTPException` for expected errors.
* Let FastAPI handle validation errors (`422`).

---

## Summary

* Every HTTP response has a status code.
* `200` → Success
* `201` → Resource created
* `204` → No response body
* `400` → Bad request
* `401` → Unauthorized
* `403` → Forbidden
* `404` → Not found
* `422` → Validation error
* `500` → Server error
