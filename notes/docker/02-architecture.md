# Docker Architecture

## Overview

Docker follows a client-server architecture. The Docker Engine is responsible for building, managing, and running containers. It uses images as templates to create containers. If an image is not available locally, Docker downloads it from a registry such as Docker Hub.

---

## Docker Engine

Docker Engine is the core component of Docker.

It is responsible for:

- Building images
- Running containers
- Managing images
- Managing networks
- Managing volumes

Think of Docker Engine as the brain of Docker.

---

## Docker Image

A Docker Image is a read-only template used to create containers.

It contains everything an application needs to run:

- Application code
- Runtime
- Dependencies
- Libraries
- Configuration

One image can be used to create multiple containers.

---

## Docker Container

A Docker Container is a running instance of an image.

Containers provide isolated environments where applications run consistently across different machines.

Containers are lightweight, portable, and disposable.

---

## Docker Hub

Docker Hub is the default public registry for Docker images.

If an image is not available locally, Docker downloads it from Docker Hub.

Developers can also publish their own images to Docker Hub.

---

## How They Work Together

The following diagram illustrates the relationship between the main Docker components.

```text
Developer
     │
     ▼
Docker CLI
     │
     ▼
Docker Engine
     │
     ├──────────► Local Images
     │                 │
     │                 ▼
     │           Create Container
     │
     └──────────► Docker Hub
                     │
                     ▼
             Download Image (if needed)