# Docker Storage Types

## Introduction

Docker containers have a temporary writable layer.

However, applications often need to store and access data outside the container lifecycle.

Docker provides different storage mechanisms to connect containers with persistent or external storage.

The two main storage types used in backend development are:

- Volumes
- Bind Mounts


---

## Docker Storage Overview

Docker storage allows containers to access data that exists outside their internal filesystem.

The main difference between storage types is:

- Who manages the storage
- Where the data is stored
- How the storage is used


Architecture:
    |
    |
    +----------------+
    |                |
 Volumes       Bind Mounts



---

# 1. Volumes

Volumes are managed by Docker and are designed for storing persistent application data.

Main characteristics:

- Managed by Docker
- Independent from container lifecycle
- Suitable for production environments
- Used for databases and application state


Common examples:

- PostgreSQL data
- MySQL data
- Redis persistence
- User uploaded files


---

# 2. Bind Mounts

Bind Mounts connect a directory or file from the host machine directly to a container.

Main characteristics:

- Managed by the user
- Uses the host filesystem directly
- Useful for development environments
- Allows live changes between host and container


Common examples:

- Local development
- Hot reload applications
- Sharing source code with containers





---

# Volumes vs Bind Mounts

| Feature | Volumes | Bind Mounts |
|---------|---------|-------------|
| Managed by | Docker | User |
| Storage location | Docker managed area | Host filesystem |
| Container dependency | Low | High |
| Production usage | Recommended | Less common |
| Development usage | Useful | Very common |
| Host filesystem access | No direct access | Direct access |


---

# Choosing the Right Storage Type

Use **Volumes** when:

- You need persistent production data
- You work with databases
- Data should be independent from containers


Use **Bind Mounts** when:

- You are developing locally
- You need live code changes
- You want direct access to project files




---

# Summary

Docker provides different storage mechanisms depending on the application's needs.

Volumes are the preferred solution for persistent production data.

Bind Mounts are commonly used during development because they provide direct access between the host and container.

The main difference:
