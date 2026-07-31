# Django Model Methods

## What are Model Methods?

Model methods are custom Python methods defined inside a Django model.

They allow models to contain behavior and business logic related to their data.

Example:

```python
class Post(models.Model):
    title = models.CharField(max_length=200)

    def get_title_length(self):
        return len(self.title)
```

Usage:

```python
post.get_title_length()
```

---

# Why Use Model Methods?

Model methods help to:

- Keep related logic close to the data
- Avoid repeating code in views
- Improve code readability
- Make models more maintainable

---

# The `__str__()` Method

Every Django model should define a `__str__()` method.

It controls how the object is represented as a string.

Example:

```python
class Post(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
```

Without `__str__`:

```
Post object (1)
```

With `__str__`:

```
Django Tutorial
```

Useful in:

- Django Admin
- Shell
- Debugging

---

# Custom Model Methods

You can create custom methods for model-specific behavior.

Example:

```python
class Product(models.Model):
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    discount = models.IntegerField(
        default=0
    )

    def final_price(self):
        return self.price - self.discount
```

Usage:

```python
product.final_price()
```

---

# Using Model Methods in Templates

Example:

Model:

```python
def is_published(self):
    return self.published_at is not None
```

Template:

```html
{% if post.is_published %}
    Published
{% endif %}
```

---

# Model Methods vs Functions

## Function

Usually used for:

- General reusable logic
- Logic unrelated to one model

Example:

```python
def calculate_tax(price):
    ...
```

---

## Model Method

Used when logic belongs to a specific object.

Example:

```python
post.publish()
```

The Post object knows how to publish itself.

---

# Business Logic in Models

Good example:

```python
class Order(models.Model):

    def calculate_total(self):
        ...
```

The Order knows how to calculate its total.

---

Avoid:

```python
def calculate_order_total(order):
    ...
```

when the logic only belongs to Order.

---

# Best Practices

- Keep model methods focused.
- Use methods for behavior related to the model.
- Avoid putting complex unrelated logic inside models.
- Use services for large business workflows.