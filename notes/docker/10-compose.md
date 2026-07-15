# Docker Compose

## Introduction

Docker Compose is a tool for defining, configuring, and managing multi-container Docker applications.

While Docker allows you to create and run individual containers, real-world applications usually consist of multiple services working together. A typical backend application may include a web server, a database, a cache, and background workers, each running inside its own container.

Without Docker Compose, every service must be started manually using separate `docker run` commands. In addition, developers need to configure networks, attach volumes, expose ports, and set environment variables for each container individually. As the number of services grows, managing the application becomes increasingly complex and error-prone.

Docker Compose solves this problem by allowing developers to describe the entire application architecture inside a single configuration file, usually named `compose.yml` or `docker-compose.yml`.

This file defines:

- Application services
- Images or build instructions
- Networks
- Volumes
- Port mappings
- Environment variables
- Restart policies and other configuration options

Once the configuration file is ready, the entire application can be created and managed using a single command.

The main idea behind Docker Compose is:

> Docker manages individual containers, while Docker Compose manages the entire application.

Instead of thinking about containers separately, Docker Compose treats all related containers as one logical project. It automatically creates the required resources, connects services through networks, mounts persistent volumes, and starts containers in the correct configuration.

Docker Compose is widely used in backend development because most modern applications are built using multiple services. For example, a typical Django application may consist of:

- Django application
- PostgreSQL database
- Redis server
- Celery worker
- Nginx reverse proxy

Rather than managing each service independently, Docker Compose orchestrates them as a single application, making development, testing, and deployment significantly simpler and more consistent.