# Pydantic Models in FastAPI

## What is Pydantic?

Pydantic is a Python library used for **data validation, data parsing, and serialization**.

In FastAPI, Pydantic models are used to define the expected structure of data that enters or leaves the application.

A Pydantic model works as a **data contract** between the client and the server.

It defines:

- What fields are expected.
- What data types are allowed.
- Which fields are required or optional.

---

## BaseModel

Pydantic models are created by inheriting from `BaseModel`.

Example:

```python
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str
```

Here, we created a model that represents a User.

The model expects:

- `name` → string
- `age` → integer
- `email` → string

---

## Why Do We Use Pydantic Models?

Without Pydantic models, we usually work with plain dictionaries:

```python
user = {
    "name": "Ali",
    "age": 25
}
```

The application does not know:

- If required fields exist.
- If the data types are correct.
- If the data structure is valid.

With Pydantic:

```python
class User(BaseModel):
    name: str
    age: int
```

Pydantic automatically:

- Validates the received data.
- Converts compatible data types.
- Provides clear validation errors.
- Keeps the data structure consistent.

---

## Data Validation

Pydantic checks whether the provided data matches the defined model.

Example:

```python
class User(BaseModel):
    name: str
    age: int
```

Valid data:

```python
user = User(
    name="Ali",
    age=25
)
```

Invalid data:

```python
user = User(
    name="Ali",
    age="hello"
)
```

The second example will raise a validation error because `age` must be an integer.

---

## Optional Fields

Some fields are not always required.

We can define optional fields using `Optional`.

Example:

```python
from typing import Optional


class User(BaseModel):
    name: str
    age: int
    phone: Optional[str] = None
```

In this example:

- `name` is required.
- `age` is required.
- `phone` is optional.

---

## Default Values

Pydantic models can also define default values.

Example:

```python
class User(BaseModel):
    name: str
    active: bool = True
```

If the client does not provide the `active` field, Pydantic will use the default value:

```python
active = True
```

---

## Using Pydantic Models in FastAPI

Pydantic models are commonly used with Request Body.

Example:

```python
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    name: str
    age: int


@app.post("/users")
def create_user(user: User):
    return user
```

FastAPI receives the JSON data and automatically converts it into a `User` object.

---

## Model Reusability

One of the main advantages of models is avoiding duplicated code.

Instead of defining the same fields multiple times:

```python
name: str
age: int
email: str
```

We can create one reusable model:

```python
class User(BaseModel):
    name: str
    age: int
    email: str
```

Then use it wherever we need user data.

This follows the **DRY (Don't Repeat Yourself)** principle.

---

## Important Notes

- Pydantic models define the structure of application data.
- `BaseModel` provides validation features.
- Type hints are used as validation rules.
- FastAPI uses Pydantic models for automatic API documentation.
- Models make applications easier to maintain and scale.
- A model represents the expected shape of data.

---

## Common Mistakes

❌ Using dictionaries for important data structures:

```python
user = {
    "name": "Ali",
    "age": 25
}
```

Problems:

- No automatic validation.
- No clear schema.
- Harder to maintain.

✅ Using Pydantic models:

```python
class User(BaseModel):
    name: str
    age: int
```

Benefits:

- Validation.
- Clear structure.
- Better maintainability.

---

## Related Topics

- Request Body
- Response Models
- Data Validation
- Type Hints
- Serialization