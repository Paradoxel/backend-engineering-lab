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
