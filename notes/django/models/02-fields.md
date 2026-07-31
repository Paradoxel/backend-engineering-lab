# Django Model Fields

## What is a Model Field?

A model field defines the type of data that can be stored in a database column.

Each field is represented as a class attribute and maps directly to a database column.

---

## Declaring Fields

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
```

---

## How Fields Map to the Database

| Django Field | Database Column |
|---------------|----------------|
| CharField | VARCHAR |
| TextField | TEXT |
| IntegerField | INTEGER |
| BooleanField | BOOLEAN |
| DateTimeField | DATETIME |

---

## Common Field Types

### CharField

Used for short strings.

```python
title = models.CharField(max_length=255)
```

---

### TextField

Used for large amounts of text.

```python
content = models.TextField()
```

---

### IntegerField

Stores integer numbers.

```python
views = models.IntegerField()
```

---

### FloatField

Stores floating-point numbers.

```python
price = models.FloatField()
```

---

### DecimalField

Used for financial values.

```python
price = models.DecimalField(
    max_digits=10,
    decimal_places=2
)
```

---

### BooleanField

Stores True or False.

```python
is_active = models.BooleanField(default=True)
```

---

### DateField

Stores dates.

```python
published_date = models.DateField()
```

---

### DateTimeField

Stores date and time.

```python
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
```

---

### EmailField

```python
email = models.EmailField()
```

---

### URLField

```python
website = models.URLField()
```

---

### UUIDField

```python
import uuid

id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False
)
```

---

### ImageField

```python
image = models.ImageField(upload_to="posts/")
```

Requires Pillow to be installed.

---

### FileField

```python
file = models.FileField(upload_to="uploads/")
```

---

## Choosing the Right Field

| Data | Recommended Field |
|--------|-------------------|
| Name | CharField |
| Description | TextField |
| Price | DecimalField |
| Email | EmailField |
| Website | URLField |
| Avatar | ImageField |
| Document | FileField |
| Published Date | DateField |
| Created Time | DateTimeField |

---
