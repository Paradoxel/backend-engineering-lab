# Docker Volumes

## Introduction

Docker containers are designed to be lightweight and disposable.
They can be created, stopped, replaced, and removed easily.

However, containers have a problem:

Any data created inside a container's writable layer will be lost when the container is removed.

Docker Volumes solve this problem by providing persistent storage that exists independently from containers.

The main idea behind Docker Volumes is:

> Containers run applications. Volumes keep data alive.

## The Problem: Container Data Persistence

A container contains everything needed to run an application:

- Application code
- Runtime environment
- Dependencies
- Temporary files

However, the container filesystem is temporary.

Example:

Container:

    container
    |
    ├── app.py
    ├── database.db
    └── uploaded_files/


If the container is removed:

    docker rm <container_id>


All data inside the container disappears.


## What is a Docker Volume?

A Docker Volume is a storage mechanism that allows data to exist outside the container lifecycle.

Volumes are managed by Docker and can be attached to multiple containers.

Architecture:

        Container

            |
            |
            v

        Docker Volume

The container can be deleted, recreated, or replaced while the data remains available.


## Separation of Application and Data

Docker follows the separation of concerns principle.

Containers are responsible for:

- Running application processes
- Executing business logic
- Providing runtime environment


Volumes are responsible for:

- Storing persistent data
- Keeping databases
- Saving uploaded files
- Maintaining application state


This separation creates loose coupling between application logic and data storage.


## Containers vs Volumes

Containers and Volumes have different responsibilities in Docker architecture.

A container is responsible for running an application, while a volume is responsible for storing persistent data.

| Container | Volume |
|------------|--------|
| Runs application processes | Stores persistent data |
| Contains application code and dependencies | Contains databases, uploads, and files |
| Has a short lifecycle | Has a long lifecycle |
| Can be created and removed frequently | Should survive container changes |
| Disposable | Persistent |

Example:

Application:

        Container

        |
        |
        v

        Volume

The container can be replaced without losing important application data.


## Container Lifecycle vs Volume Lifecycle

Containers and volumes have independent lifecycles.

Container lifecycle:

    Create
      |
      v
    Start
      |
      v
    Stop
      |
      v
    Remove


Volume lifecycle:

    Create
      |
      v
    Attach to container
      |
      v
    Store data
      |
      v
    Reuse with another container


Removing a container does not automatically remove its volumes.

Example:

    docker rm my-container


The container is removed, but the volume remains available.


## Docker Storage Architecture

Docker separates application execution from data storage.

Without volumes:

        Container

        |
        ├── app.py
        ├── database.db
        └── uploads/


        Remove container

              ↓

        Data is lost


With volumes:

        Container

        |
        └── Application


        Docker Volume

        |
        ├── database.db
        └── uploads/


        Remove container

              ↓

        Data remains