# PostgreSQL Data Service

Python data service with pandas and async PostgreSQL support.

This project was generated from the local Python seed template. It uses a `src/` layout, Python 3.12+, `uv`, pandas, SQLAlchemy async, asyncpg, Alembic, Pydantic Settings, Ruff, mypy, and pytest.

## Dependency policy

- `pyproject.toml` declares direct dependency intent.
- `pandas==2.3.3` is deliberately pinned exactly for this lifecycle lab.
- PostgreSQL libraries use compatible version ranges.
- `uv.lock` records the exact complete dependency graph and should be committed.

## Local setup

```bash
uv sync
cp .env.example .env
uv run python -m postgresql_data_service
```

The default command prints configuration metadata and does not connect to PostgreSQL.

## Database commands

When a PostgreSQL server is available and `DATABASE_URL` is configured:

```bash
uv run alembic upgrade head
```

Creating and applying migrations is not required for the Copier lifecycle demonstration.

## Quality checks

```bash
uv run ruff format --check .
uv run ruff check .
uv run mypy src
uv run pytest
```

