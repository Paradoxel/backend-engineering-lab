# Docker Volume Commands

## Introduction

Docker provides a set of commands for creating, inspecting, managing, and removing volumes.

These commands help store application data independently from containers.

---

## List Volumes

**Purpose**

List all Docker-managed volumes.

**Syntax**

```bash
docker volume ls
```

**Example**

```bash
docker volume ls
```

---

## Create a Volume

**Purpose**

Create a new Docker volume.

**Syntax**

```bash
docker volume create <volume-name>
```

**Example**

```bash
docker volume create postgres-data
```

Example output:

```text
postgres-data
```

---

## Inspect a Volume

**Purpose**

Display detailed information about a Docker volume.

**Syntax**

```bash
docker volume inspect <volume-name>
```

**Example**

```bash
docker volume inspect postgres-data
```

This command displays information such as:

- Name
- Driver
- Mountpoint
- Labels
- Scope

---

## Remove a Volume

**Purpose**

Remove a specific Docker volume.

**Syntax**

```bash
docker volume rm <volume-name>
```

**Example**

```bash
docker volume rm postgres-data
```

> A volume cannot be removed while it is being used by a container.

---

## Remove Unused Volumes

**Purpose**

Remove all unused Docker volumes.

**Syntax**

```bash
docker volume prune
```

**Example**

```bash
docker volume prune
```

Docker asks for confirmation before deleting unused volumes.

---

## Mount a Volume

**Purpose**

Attach a Docker volume to a container.

**Syntax**

```bash
docker run -v <volume-name>:<container-path> <image>
```

**Example**

```bash
docker run -v postgres-data:/var/lib/postgresql/data postgres
```

Explanation:

- `postgres-data` → Docker volume
- `/var/lib/postgresql/data` → Directory inside the container
- `postgres` → Docker image

Docker automatically mounts the volume before starting the container.

---

## Summary

| Command | Description |
|----------|-------------|
| `docker volume ls` | List all volumes |
| `docker volume create` | Create a new volume |
| `docker volume inspect` | Show volume details |
| `docker volume rm` | Remove a specific volume |
| `docker volume prune` | Remove unused volumes |
| `docker run -v` | Mount a volume to a container |
