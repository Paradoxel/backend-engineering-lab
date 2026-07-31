# Django Model Managers

## What is a Manager?

A Manager is the interface between a Django model and the database.

It is responsible for retrieving objects from the database.

Every Django model automatically has a default manager called `objects`.

Example:

```python
posts = Post.objects.all()
```

Here:

- `Post` is the model.
- `objects` is the manager.
- `all()` returns a QuerySet.

---

## Default Manager

If you do not define a custom manager, Django automatically creates one.

Example:

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
```

Usage:

```python
Post.objects.all()
Post.objects.filter(title__icontains="django")
Post.objects.get(id=1)
```

---

## Why Create a Custom Manager?

Custom managers allow you to encapsulate common database queries.

Instead of writing:

```python
Post.objects.filter(is_published=True)
```

everywhere,

you can write:

```python
Post.published.all()
```

---

## Creating a Custom Manager

```python
from django.db import models


class PublishedManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(
            is_published=True
        )
```

Use it in the model:

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)

    objects = models.Manager()
    published = PublishedManager()
```

Usage:

```python
Post.objects.all()      # all posts
Post.published.all()    # only published posts
```

---

## Adding Custom Manager Methods

Managers can define reusable query methods.

Example:

```python
class PostManager(models.Manager):

    def published(self):
        return self.filter(is_published=True)

    def featured(self):
        return self.filter(is_featured=True)
```

Usage:

```python
Post.objects.published()
Post.objects.featured()
```

---

## Manager vs QuerySet

Manager

- Entry point to the database
- Lives on the model class

Example:

```python
Post.objects
```

QuerySet

- Represents a collection of model instances

Example:

```python
Post.objects.filter(is_active=True)
```

---

## Best Practices

- Keep reusable queries inside managers.
- Avoid duplicating filters across views.
- Use managers for database access.
- Use model methods for object behavior.