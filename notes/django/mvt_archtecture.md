# Django MTV Architecture

## What is an Architecture?

Architecture defines how different parts of an application are organized and how they communicate with each other.

Its purpose is to separate responsibilities, making applications easier to develop and maintain.

---

# What is MTV?

Django follows the **MTV (Model – Template – View)** architecture.

It separates an application into three main components:

* **Model** → Manages application data.
* **View** → Handles requests and application logic.
* **Template** → Displays data to the user.

---

# Request Flow

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
Template
    │
    ▼
Response
```

---

# Components

## Model

* Represents application data.
* Communicates with the database.
* Uses Django ORM.

---

## View

* Receives the HTTP request.
* Executes business logic.
* Returns an HTTP response.

---

## Template

* Responsible for presentation.
* Generates the final HTML shown to the user.

---

# Responsibilities

| Component | Responsibility |
| --------- | -------------- |
| Model     | Data           |
| View      | Business Logic |
| Template  | Presentation   |

---

# Best Practices

* Keep business logic inside **Views** (or dedicated service layers when projects grow).
* Keep database operations inside **Models**.
* Keep **Templates** focused on presentation only.

---

# Summary

The MTV architecture separates an application into independent layers:

* **Model** manages data.
* **View** processes requests.
* **Template** presents the final output.

This separation improves readability, maintainability, and scalability.
