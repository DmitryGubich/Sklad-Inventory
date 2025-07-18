shell := uv run

.PHONY: pre-commit
pre-commit:
	$(shell) pre-commit run --all-files

.PHONY: type-checking
type-checking:
	$(shell) pyre

.PHONY: run
run:
	docker compose up

.PHONY: create-migration
create-migration:
	docker compose exec inventory alembic revision --autogenerate -m "" # <-- put a name here

.PHONY: migrate
migrate:
	docker compose exec inventory alembic upgrade head
