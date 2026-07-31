# Django Models

## What is a Model?

A Django model is a Python class that represents a database table. It defines the structure of your data, including its fields, relationships, and behavior.

Each model inherits from `django.db.models.Model`, allowing Django's ORM to map Python objects to database records.

---

## Models in the MVT Architecture

In Django's MVT (Model-View-Template) architecture, the Model is responsible for:

- Defining the database schema
- Managing application data
- Interacting with the database through the ORM
- Providing business logic related to data

```
        User Request
             │
             ▼
          View
             │
             ▼
          Model
             │
             ▼
        Database
             │
             ▼
          View
             │
             ▼
         Template
```

---

## Django ORM

Django uses an Object Relational Mapper (ORM) to communicate with relational databases.

Instead of writing SQL manually, you interact with Python objects, and Django generates the corresponding SQL queries.

### Without ORM

```
Python
   │
SQL Query
   │
Database
```

### With Django ORM

```
Python Object
      │
      ▼
 Django ORM
      │
      ▼
SQL Query
      │
      ▼
Database
```

---

## Model Mapping

| Django | Database |
|---------|----------|
| Model | Table |
| Instance | Row |
| Field | Column |
| Attribute | Cell Value |

---

## Example

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
```

The model above will generate a database table similar to:

| id | title | content |
|----|-------|----------|
| 1 | Hello Django | ... |

---

## Why Use Models?

Models provide several advantages:

- Keep data organized
- Simplify database operations
- Eliminate most raw SQL
- Improve code readability
- Make applications easier to maintain
- Work consistently across different database engines

