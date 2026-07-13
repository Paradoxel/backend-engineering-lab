# Introduction to Django

## What is Django?

Django is a high-level Python web framework designed to help developers build secure, scalable, and maintainable web applications quickly.

Its philosophy is:

> **Focus on building your application, not reinventing common web features.**

---

# Why Django Exists

Building a web application from scratch requires solving many common problems:

* URL routing
* Authentication
* Database access
* Session management
* Security
* Forms
* Admin panel
* Static & media files

Instead of implementing these features repeatedly, Django provides them out of the box.

---

# Django Philosophy

## Don't Repeat Yourself (DRY)

Avoid writing the same logic multiple times.

Every piece of logic should have a single source of truth.

---

## Batteries Included

Django comes with many built-in tools, including:

* ORM
* Authentication
* Admin Panel
* Template Engine
* Session Framework
* Form System
* Security Middleware

This allows developers to focus on business logic rather than infrastructure.

---

# MTV Architecture

Django follows the **MTV (Model–Template–View)** architecture.

```text
Request
    │
    ▼
URLs
    │
    ▼
View
    │
    ▼
Model
    │
    ▼
Database

View
    │
    ▼
Template
    │
    ▼
Response
```

### Model

Responsible for managing and interacting with application data.

### View

Receives the request, executes the application's logic, and returns a response.

### Template

Responsible for presenting data to the user.

---

# Why Django is Popular

* Fast development
* Clean project structure
* Excellent security features
* Scalable architecture
* Large ecosystem
* Strong community
* Excellent documentation

---

# Typical Request Flow

```text
Browser
    │
    ▼
Request
    │
    ▼
urls.py
    │
    ▼
View
    │
    ▼
Model (optional)
    │
    ▼
Database

View
    │
    ▼
Template / JsonResponse / Redirect
    │
    ▼
Response
```

---

# Summary

Django is a framework that provides the common building blocks required for web development, allowing developers to spend more time solving business problems and less time implementing infrastructure.
