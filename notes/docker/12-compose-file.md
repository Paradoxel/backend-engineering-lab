# Docker Compose File

## Introduction

Docker Compose uses a configuration file to define and manage multi-container applications.

The file is usually named:

- compose.yml
- docker-compose.yml

It describes how services should be built, configured, connected, and started.

---

## Example

```yaml
services:
  web:
    build: .
    ports:
      - "8000:5000"

  db:
    image: postgres:17
```

---

## Explanation

### services

Defines all application services.

```yaml
services:
```

---

### build

Build an image from a Dockerfile.

```yaml
build: .
```

---

### image

Use an existing image from a registry.

```yaml
image: postgres:17
```

---

### ports

Map ports between the host and the container.

```yaml
ports:
  - "8000:5000"
```

Format:

```
HOST_PORT:CONTAINER_PORT
```

---

## Architecture

```
compose.yml

        │

        ▼

Services

├── web
└── db

        │

        ▼

Containers
```

---

## Summary

A Compose file defines the entire application.

Instead of manually running multiple `docker run` commands, Docker Compose reads the configuration file and creates all required services automatically.