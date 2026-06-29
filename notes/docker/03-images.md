# Docker Images

## What is a Docker Image?

A Docker Image is a read-only template used to create containers.

It packages everything an application needs to run, including:

- Application code
- Runtime
- System libraries
- Dependencies
- Configuration files

An image itself does not run. Instead, it serves as a blueprint for creating one or more containers.

---

## Key Characteristics

Docker Images are:

- Read-only
- Reusable
- Portable
- Immutable

Because images are immutable, they do not change after they are built.

---

## Image vs Container

| Image | Container |
|--------|-----------|
| Template | Running instance |
| Read-only | Read-write |
| Cannot run by itself | Runs an application |
| Reusable | Disposable |
| Can create multiple containers | Created from an image |

---

## Where Do Images Come From?

Docker images can be obtained from:

- Docker Hub
- Private registries
- Images built locally using a Dockerfile

---

## Image Lifecycle

```text
Dockerfile
     │
     ▼
Build Image
     │
     ▼
Store Image
     │
     ▼
Create Container
     │
     ▼
Run Application
```

An image can be used repeatedly to create multiple containers.

---

## Summary

A Docker Image is an immutable, read-only template that contains everything an application needs to run. It serves as the blueprint for creating one or more containers.