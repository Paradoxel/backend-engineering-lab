# Docker Compose Commands

## Start Services

```bash
docker compose up
```

Create and start all services.

---

## Start Services in Detached Mode

```bash
docker compose up -d
```

Start services in the background.

---

## Stop Services

```bash
docker compose stop
```

Stop running services without removing them.

---

## Remove Services

```bash
docker compose down
```

Stop and remove containers and networks.

> Named volumes are not removed by default.

---

## List Services

```bash
docker compose ps
```

Show running services.

---

## View Logs

```bash
docker compose logs
```

Show logs for all services.

```bash
docker compose logs <service>
```

Show logs for a specific service.

---

## Restart Services

```bash
docker compose restart
```

Restart all services.

```bash
docker compose restart <service>
```

Restart a specific service.

---

## Execute a Command

```bash
docker compose exec <service> <command>
```

Run a command inside a running service.

Example:

```bash
docker compose exec web bash
```

---

## Build Images

```bash
docker compose build
```

Build or rebuild service images.

---

## Summary

| Command | Description |
|---------|-------------|
| `docker compose up` | Start services |
| `docker compose up -d` | Start services in background |
| `docker compose stop` | Stop services |
| `docker compose down` | Remove services |
| `docker compose ps` | List services |
| `docker compose logs` | Show logs |
| `docker compose restart` | Restart services |
| `docker compose exec` | Run a command |
| `docker compose build` | Build images |