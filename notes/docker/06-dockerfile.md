# Dockerfile

## What is a Dockerfile?

A Dockerfile is a text file that contains a set of instructions for building a Docker image.

Instead of manually installing dependencies and configuring an application, a Dockerfile automates the entire process.

Docker reads the Dockerfile from top to bottom and executes each instruction in order.

---

## Why Do We Need a Dockerfile?

Without a Dockerfile, creating an image would require many manual steps.

A Dockerfile makes the build process:

* Repeatable
* Consistent
* Automated
* Easy to share

This allows anyone to build the same image using the same instructions.

---

## How Docker Builds an Image

The image-building process follows these steps:

```text
Dockerfile
     │
     ▼
Docker Build
     │
     ▼
Docker Image
     │
     ▼
Docker Container
```

The Dockerfile defines **how** the image should be built.

The image is then used to create one or more containers.

---

## Common Dockerfile Instructions

### FROM

Specifies the base image.

Every Dockerfile starts with a `FROM` instruction.

Example:

```dockerfile
FROM python:3.13
```

---

### WORKDIR

Sets the working directory inside the container.

Example:

```dockerfile
WORKDIR /app
```

---

### COPY

Copies files from the host machine into the image.

Example:

```dockerfile
COPY . .
```

---

### RUN

Executes commands while building the image.

It is commonly used to install dependencies.

Example:

```dockerfile
RUN pip install -r requirements.txt
```

---

### EXPOSE

Documents the port used by the application.

Example:

```dockerfile
EXPOSE 8000
```

---

### CMD

Specifies the default command that runs when a container starts.

Example:

```dockerfile
CMD ["python", "app.py"]
```

---

## Building an Image

After creating a Dockerfile, build the image with:

```bash
docker build -t my-app .
```

* `-t` assigns a name (tag) to the image.
* `.` tells Docker to use the current directory as the build context.

---

## Dockerfile Workflow

```text
Write Dockerfile
        │
        ▼
docker build
        │
        ▼
Docker Image
        │
        ▼
docker run
        │
        ▼
Docker Container
```

---

## Summary

A Dockerfile is a blueprint for building Docker images. It automates the image creation process using a sequence of instructions. Once an image is built, Docker can create one or more containers from it.
