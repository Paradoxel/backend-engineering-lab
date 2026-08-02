# Response Models

## What is a Response Model?

A **Response Model** defines the structure of the data returned by an API endpoint.

It is specified using the `response_model` parameter in a route decorator.

```python
@app.get("/users/{id}", response_model=UserResponse)
```

---

## Why Use Response Models?

Using a response model provides several benefits:

* Validates response data
* Automatically serializes objects to JSON
* Filters unwanted fields
* Improves API documentation

---

## Example

```python
from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    email: str
    first_name: str


@app.get("/users/{id}", response_model=UserResponse)
def get_user(id: int):
    return {
        "id": 1,
        "email": "user@example.com",
        "first_name": "John",
    }
```

FastAPI ensures the returned data matches the schema.

---

## Request Model vs Response Model

| Request Model           | Response Model          |
| ----------------------- | ----------------------- |
| Validates incoming data | Validates outgoing data |
| Used for client input   | Used for API output     |

---

## Hiding Sensitive Data

A response model helps prevent exposing confidential information.

```python
class User(BaseModel):
    id: int
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
```

Even if the returned object contains a password, FastAPI only returns the fields defined in `UserResponse`.

---

## Best Practices

* Always define a response model for public APIs.
* Keep request and response models separate.
* Never expose sensitive fields such as passwords or tokens.

---

## Summary

* A response model defines the API output.
* It validates and serializes returned data.
* It improves documentation.
* It protects sensitive information.
* It should be used for almost every API endpoint.
