# easy-commerce-backend

Back-End for EasyCommerce Single vendor e-commerce platform

## Setting up development

### Requirements

- pyinvoke
- docker-compose

### Instructions

- `inv setup-dev` - sets up development environment inside docker
- `inv runserver` - runs the local server at [https://localhost:8000](https://localhost:8000)
- `inv shell` - Spawns a shell inside the docker container
- `inv django-shell` - Spawns a python django REPL
