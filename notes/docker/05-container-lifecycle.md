# Docker Container Lifecycle

## Overview

A Docker container goes through several states during its lifetime.

Understanding the container lifecycle helps explain how Docker commands work and how containers are managed.

---

## Lifecycle Diagram

```text
Image
   │
   ▼
Created
   │
   ▼
Running
   │
   ▼
Stopped
   │
   ▼
Removed
```

Each state represents a different stage in the life of a container.

---

## 1. Created

A container is created from a Docker image.

At this stage, the container exists but the application is not running yet.

A container must always be created from an image.

---

## 2. Running

When the container starts, Docker launches the main application process inside it.

As long as the main process is running, the container remains in the **Running** state.

For example:

```bash
docker run nginx
```

The Nginx process starts and the container keeps running.

---

## 3. Stopped

A container enters the **Stopped** state when:

* The main process finishes.
* The user manually stops the container.

For example:

```bash
docker container stop <container-id>
```

Stopped containers still exist on the system and can be started again.

---

## 4. Removed

A removed container no longer exists on the system.

Removing a container permanently deletes its writable layer and metadata.

For example:

```bash
docker container rm <container-id>
```

Only stopped containers can be removed.

---

## Lifecycle Commands

| State                   | Docker Command                            |
| ----------------------- | ----------------------------------------- |
| Create & Run            | `docker container run <image>`            |
| List Running Containers | `docker container ls`                     |
| List All Containers     | `docker container ls -a`                  |
| Stop                    | `docker container stop <container-id>`    |
| Start                   | `docker container start <container-id>`   |
| Restart                 | `docker container restart <container-id>` |
| Remove                  | `docker container rm <container-id>`      |

---

## Important Notes

* An image is a template.
* A container is a running instance of an image.
* One image can create multiple containers.
* A stopped container is **not** removed automatically.
* A container remains running only while its main process is running.

---

## Summary

A Docker container moves through several lifecycle states: **Created**, **Running**, **Stopped**, and **Removed**. Understanding these states makes Docker commands easier to learn because each command transitions the container from one state to another.
