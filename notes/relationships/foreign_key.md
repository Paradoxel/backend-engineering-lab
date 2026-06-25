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
