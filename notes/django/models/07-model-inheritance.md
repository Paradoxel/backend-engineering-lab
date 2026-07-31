# Django Model Inheritance

## What is Model Inheritance?

Model inheritance allows Django models to reuse fields and behavior from another model.

It helps avoid duplicated code and creates reusable model structures.

Example:

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
```

---

# Types of Model Inheritance

Django mainly provides two common types:

1. Abstract Base Models
2. Multi-table Inheritance

---

# Abstract Base Models

Abstract models are used to share common fields and behaviors between models.

They do not create their own database table.

Example:

```python
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True
```

Usage:

```python
class Post(TimeStampedModel):
    title = models.CharField(max_length=200)
```

Database:

```
Post
----
id
title
created_at
updated_at
```

`TimeStampedModel` does not create a table.

Common use cases:

- created_at
- updated_at
- is_deleted
- created_by

---

# Multi-table Inheritance

Multi-table inheritance is used when one model is a specialized version of another model.

Each model has its own database table.

Example:

```python
class Person(models.Model):
    name = models.CharField(max_length=100)


class Employee(Person):
    salary = models.IntegerField()
```

Database:

```
person
------
id
name


employee
--------
person_ptr_id
salary
```

Django creates a One-to-One relationship between parent and child models.

---

# Abstract Model vs Multi-table Inheritance

| Type | Creates Table | Purpose |
|------|---------------|---------|
| Abstract Model | No | Reuse fields and behavior |
| Multi-table Inheritance | Yes | Create specialized models |

---

# Best Practices

- Prefer Abstract Base Models for shared fields.
- Use Multi-table Inheritance only for real "is-a" relationships.
- Avoid unnecessary inheritance complexity.

Example:

Good:

```text
TimeStampedModel
        |
 ----------------
 |              |
Post        Product
```

Because both models only share common fields.

---

Also good:

```text
Person
  |
Employee
```

Because an Employee is a type of Person.