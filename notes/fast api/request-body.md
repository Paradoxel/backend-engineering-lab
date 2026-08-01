# Request Body in FastAPI

## What is Request Body?

In FastAPI, the **Request Body** is the data sent by the client inside the HTTP request.

It is commonly used when we need to send structured data to the server, especially for:

- Creating new resources (`POST`)
- Updating existing resources (`PUT`, `PATCH`)

FastAPI uses **Pydantic models** to define and validate request body data.

---

## Basic Example

Let's create an endpoint for creating a new user.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    email: str


@app.post("/users")
def create_user(user: User):
    return user
```

The client can send this JSON body:

```json
{
    "name": "Ali",
    "age": 25,
    "email": "ali@example.com"
}
```

FastAPI automatically:

- Converts JSON data into a Python object.
- Validates the received data.
- Returns validation errors if the data is invalid.

---

## Request Body vs Path Parameters

### Path Parameter

Used to identify a specific resource.

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}
```

Example:

```
GET /users/10
```

---

### Request Body

Used to send data about a resource.

```python
@app.post("/users")
def create_user(user: User):
    return user
```

Example:

```json
{
    "name": "Ali",
    "age": 25
}
```

---

## Important Notes

- Request bodies are usually used with `POST`, `PUT`, and `PATCH` methods.
- Request body models should inherit from `BaseModel`.
- FastAPI automatically performs data validation.
- Type hints define the expected structure of incoming data.

---

## Common Mistakes

❌ Using a plain dictionary for request data:

```python
@app.post("/users")
def create_user(user: dict):
    pass
```

Problems:

- No automatic validation.
- No clear data structure.
- Harder to maintain.

✅ Using a Pydantic model:

```python
class User(BaseModel):
    name: str
    age: int
```

---

## Related Topics

- Path Parameters
- Query Parameters
- Pydantic Models
- Response Models