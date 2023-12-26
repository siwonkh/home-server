# Docker Services Configuration Repository

## Overview

This repository contains Docker Compose configurations for a suite of services including web servers, databases, and game servers. Each service is defined in its own Docker Compose YAML file for easy management and deployment.


## Services

Below are the services included in this repository:
- Mindustry Server: Configured in mindustry/docker-compose.yml


## Running a Service
To run a specific service, use the following command in the terminal:
```bash
docker compose -f [service-dir]/docker-compose.yml up
```
For example, to start the Mindustry server, use:
```bash
docker compose -f mindustry/docker-compose.yml up
```
## Stopping a Service
To stop a running service, use:
```bash
docker compose -f [service-dir]/docker-compose.yml down
```
