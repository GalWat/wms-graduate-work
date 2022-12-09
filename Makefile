# --------------------------------------------------- Yandex.Cloud

.PHONY: start-remote
start-remote:
	yc compute instance start --name galwat-remote

.PHONY: stop-remote
stop-remote:
	yc compute instance stop --name galwat-remote

# --------------------------------------------------- Docker Compose

.PHONY: up
up:
	docker compose up -V -d

.PHONY: up-no-d
up-no-d:
	docker compose up -V

.PHONY: up-build
up-build:
	docker compose up -V --build -d

.PHONY: up-build-no-d
up-build-no-d:
	docker compose up -V --build

.PHONY: up-recreate
up-recreate:
	docker compose up -V --force-recreate --build -d

.PHONY: up-recreate-no-d
up-recreate-no-d:
	docker compose up -V --force-recreate --build

.PHONY: down
down:
	docker compose down