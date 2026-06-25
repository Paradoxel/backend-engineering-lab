# What is a ForeignKey?

A **ForeignKey** is a Django field used to create a relationship between two models.

It tells Django that one model is connected to another model.

A ForeignKey represents a **one-to-many relationship**.

---

## The Problem

Imagine we have two models:

* Category
* Product

Without a relationship, Django has no way of knowing which products belong to which category.

For example:

```text
Category:
- Electronics
- Books

Product:
- Laptop
- Keyboard
- Python Book
```

How does Django know that:

* Laptop belongs to Electronics
* Python Book belongs to Books

It doesn't.

We need a way to connect them.

That is exactly what a ForeignKey does.

---

## Mental Model

Think of a ForeignKey as a reference.

Instead of copying all of a category's information into every product, each product simply stores a reference to its category.

```text
Category
──────────────
Electronics
Books

        ▲
        │
        │
Product ──────────────
Laptop  ─────────────► Electronics
Mouse   ─────────────► Electronics
Python Book ─────────► Books
```

The product does not contain the category itself.

It only knows which category it belongs to.

---

## Key Idea

A ForeignKey answers one simple question:

> **"Who does this object belong to?"**

For example:

* A Product belongs to a Category.
* A Comment belongs to a Post.
* An Order belongs to a User.

---

## Summary

A ForeignKey:

* Connects two models.
* Creates a one-to-many relationship.
* Stores a reference to another object instead of duplicating its data.
* Allows Django to understand how objects are related.



---

# Why is a ForeignKey a One-to-Many Relationship?

Ask yourself two simple questions.

## Question 1

Can one category contain multiple products?

For example:

```text
Electronics
├── Laptop
├── Keyboard
├── Mouse
└── Monitor
```

Yes.

A single category can contain many products.

---

## Question 2

Can one product belong to multiple categories?

For example:

```text
Laptop
├── Electronics
├── Books
└── Clothing
```

In most shop applications, the answer is **no**.

A product usually belongs to only one category.

---

## The Relationship

This gives us the following relationship:

```text
Category
    │
    ├── Product
    ├── Product
    ├── Product
    └── Product
```

One Category → Many Products

Each Product → One Category

This is exactly what we call a **one-to-many relationship**.

---

## Why is the ForeignKey placed on Product?

Think about the question a Product needs to answer.

```text
Who is my category?
```

Each product has exactly one answer.

For example:

```text
Laptop
↓
Electronics
```

Therefore, each Product stores a reference to a single Category.

The Category itself does not need to store a list of all its products.

Instead, Django can automatically discover all related products by looking at every Product that references that Category.

---

## Mental Model

Always think from the perspective of the child object.

```text
Product asks:

"Who do I belong to?"
```

The answer is:

```text
Category
```

That is why the ForeignKey is defined on the Product model.

---

## Summary

A ForeignKey represents a one-to-many relationship because:

* One parent object can have many child objects.
* Each child object belongs to only one parent.
* The child stores the reference to the parent.
* Django automatically understands the relationship in both directions.
