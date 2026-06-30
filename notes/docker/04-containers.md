# Docker Containers

## What is a Docker Container?

A Docker Container is a running instance of a Docker image.

When you run an image, Docker creates a container and starts the application inside it.

For example:

```bash
docker run nginx
```

Docker creates a new container from the `nginx` image and starts the Nginx web server.

---

## Image vs Container

| Image                          | Container              |
| ------------------------------ | ---------------------- |
| Blueprint (Template)           | Running instance       |
| Read-only                      | Read-write             |
| Static                         | Dynamic                |
| Reusable                       | Temporary              |
| Can create multiple containers | Created from one image |

An image is like a blueprint, while a container is the actual running application.

---

## Container Lifecycle

A container goes through several states during its lifetime.

```text
Created
   │
   ▼
Running
   │
   ▼
Stopped
   │
   ├──► Started Again
   │
   ▼
Removed
```

Each stage can be managed using Docker commands.

---

## Container Isolation

Containers run in isolated environments.

Each container has its own:

* Filesystem
* Processes
* Network configuration
* Environment variables

This isolation allows multiple applications to run on the same machine without interfering with one another.

---

## Why Are Containers Lightweight?

Containers share the host operating system's kernel instead of running a complete operating system.

As a result, they:

* Start quickly
* Use fewer system resources
* Consume less disk space than virtual machines

---

## Key Characteristics

* Lightweight
* Portable
* Isolated
* Fast to start
* Easy to create and remove

---

## Summary

A Docker Container is a lightweight, isolated, running instance of a Docker image. Containers provide a consistent environment for applications and can be started, stopped, restarted, and removed throughout their lifecycle.
