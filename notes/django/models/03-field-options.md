# Django Model Field Options

Field options customize the behavior and validation of model fields.

---

## null

Determines whether the database column can store `NULL`.

```python
age = models.IntegerField(null=True)
```

- `null=True` → Database can store `NULL`
- `null=False` → Field is required at the database level

---

## blank

Determines whether the field is required during validation.

```python
bio = models.TextField(blank=True)
```

- `blank=True` → Validation allows an empty value
- `blank=False` → Field is required

---

## null vs blank

| Option | Database | Validation |
|----------|----------|------------|
| null | ✓ | ✗ |
| blank | ✗ | ✓ |

Example:

```python
bio = models.TextField(
    null=True,
    blank=True
)
```

---

## default

Provides a default value.

```python
is_active = models.BooleanField(default=True)
```

Another example:

```python
views = models.IntegerField(default=0)
```

---

## unique

Ensures all values are unique.

```python
email = models.EmailField(unique=True)
```

Equivalent SQL:

```sql
UNIQUE(email)
```

---

## primary_key

Defines the primary key.

```python
id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False
)
```

---

## db_index

Creates a database index.

```python
slug = models.SlugField(db_index=True)
```

Useful for frequently searched fields.

---

## editable

Controls whether the field appears in forms and the Django admin.

```python
created_at = models.DateTimeField(
    auto_now_add=True,
    editable=False
)
```

---

## verbose_name

Provides a human-readable name.

```python
title = models.CharField(
    "Post Title",
    max_length=255
)
```

---

## help_text

Displays helpful information in forms.

```python
slug = models.SlugField(
    help_text="Used in the page URL."
)
```

---

## choices

Restricts the allowed values.

```python
class Status(models.TextChoices):
    DRAFT = "DR", "Draft"
    PUBLISHED = "PB", "Published"

status = models.CharField(
    max_length=2,
    choices=Status.choices,
    default=Status.DRAFT
)
```

---

## Commonly Used Field Options

| Option | Purpose |
|----------|----------|
| null | Allow NULL in the database |
| blank | Allow empty validation |
| default | Default value |
| unique | Prevent duplicate values |
| primary_key | Primary identifier |
| db_index | Improve query performance |
| editable | Show in forms/admin |
| verbose_name | Human-readable name |
| help_text | Display help in forms |
| choices | Restrict possible values |

---

## Best Practices

- Use `blank=True` for optional form fields.
- Prefer `default` over `null` when a sensible default exists.
- Avoid `null=True` on `CharField` and `TextField`.
- Add indexes only when they improve query performance.
- Use `TextChoices` instead of hardcoded choice tuples for better readability.