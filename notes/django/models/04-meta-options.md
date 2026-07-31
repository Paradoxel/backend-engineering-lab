# Django Model Meta Options

## What is the Meta Class?

The `Meta` class is an inner class inside a Django model that defines metadata and configuration options.

It controls how Django handles the model at the database and application level.

Example:

```python
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        ordering = ["-created_at"]
```

---

## Common Meta Options


## db_table

Defines the database table name.

Default:

```text
appname_modelname
```

Example:

```python
class Meta:
    db_table = "blog_posts"
```

---

## ordering

Defines the default ordering for QuerySets.

Example:

```python
class Meta:
    ordering = ["-created_at"]
```

Equivalent to:

```python
Post.objects.all().order_by("-created_at")
```

---

## verbose_name

Defines the human-readable singular name.

Example:

```python
class Meta:
    verbose_name = "Blog Post"
```

---

## verbose_name_plural

Defines the plural name.

Example:

```python
class Meta:
    verbose_name_plural = "Blog Posts"
```

---

## constraints

Adds database-level constraints.

Example:

```python
class Meta:
    constraints = [
        models.UniqueConstraint(
            fields=["email"],
            name="unique_email"
        )
    ]
```

---

## indexes

Creates database indexes.

Example:

```python
class Meta:
    indexes = [
        models.Index(
            fields=["created_at"]
        )
    ]
```

---

## permissions

Defines custom permissions.

Example:

```python
class Meta:
    permissions = [
        ("can_publish", "Can publish posts")
    ]
```

---

## managed

Controls whether Django manages the database table.

Example:

```python
class Meta:
    managed = False
```

Useful when working with existing database tables.

---

# Example Model

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        db_table = "posts"
```

---

# Best Practices

- Use `ordering` when a model has a natural default order.
- Use indexes for frequently queried fields.
- Avoid changing `db_table` without a reason.
- Use constraints instead of handling everything in Python code.
- Keep Meta options organized and readable.