# FastAPI Versions & Core Modules

## Semantic Versioning

FastAPI follows **Semantic Versioning (SemVer)** to manage releases.

```text
MAJOR.MINOR.PATCH
```

Example:

```text
1.5.4
```

* **MAJOR** → Introduces breaking changes that may require updating existing code.
* **MINOR** → Adds new features while remaining backward compatible.
* **PATCH** → Includes bug fixes, security patches, and small improvements.

> Although FastAPI is still in the **0.x.x** series, it is stable, production-ready, and widely adopted by many companies and open-source projects.

---

# FastAPI Architecture

FastAPI is not a standalone framework. It is built on top of several powerful libraries, each responsible for a specific task.

```text
Your Application
        │
        ▼
     FastAPI
     ├─────────────┐
     ▼             ▼
 Starlette     Pydantic
        │
        ▼
     Uvicorn
```

This modular architecture is one of the reasons FastAPI is both **fast** and **easy to use**.

---

# Core Modules

## FastAPI

The main framework responsible for building APIs.

Key features:

* API routing
* Request & response handling
* Dependency Injection
* Automatic data validation
* OpenAPI specification generation
* Interactive Swagger UI (`/docs`)
* ReDoc documentation (`/redoc`)

---

## Starlette

The lightweight ASGI framework that powers FastAPI.

It provides the core web functionality, including:

* Routing
* Middleware
* Request & Response objects
* WebSockets
* Background Tasks

---

## Pydantic

Responsible for working with data.

It uses Python **type hints** to:

* Validate incoming data
* Serialize responses
* Convert data types automatically
* Produce clear validation errors

---

## Uvicorn

An **ASGI server** that runs the FastAPI application.

Its responsibilities include:

* Starting the application
* Receiving HTTP requests
* Passing requests to FastAPI
* Returning responses to the client

Without an ASGI server such as Uvicorn, a FastAPI application cannot serve requests.

---

# Installation

```bash
pip install fastapi "uvicorn[standard]"
```

---

# Summary

| Component     | Responsibility                                        |
| ------------- | ----------------------------------------------------- |
| **FastAPI**   | API framework and application logic                   |
| **Starlette** | ASGI framework, routing, middleware, and web features |
| **Pydantic**  | Data validation and serialization using type hints    |
| **Uvicorn**   | ASGI server that runs the application                 |

---

## Key Takeaways

* FastAPI follows **Semantic Versioning (MAJOR.MINOR.PATCH)**.
* Even though FastAPI is still in the **0.x.x** series, it is considered production-ready.
* FastAPI is built on top of **Starlette** and **Pydantic**, rather than implementing everything from scratch.
* **Uvicorn** is responsible for running the application and serving HTTP requests.
* The combination of these components makes FastAPI **fast, modern, and developer-friendly**.
