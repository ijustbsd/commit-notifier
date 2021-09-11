from pathlib import Path

from yoyo import get_backend, read_migrations

from ..config import settings
from .manager import manager
from .models import Commit, Person


def create_tables():
    manager.database.create_tables(
        [
            Commit,
            Person,
        ],
        safe=True,
    )


def apply_migrations():
    backend = get_backend(
        (
            "postgres://",
            f"{settings.DB_USER}:{settings.DB_PASSWORD}"
            "@"
            f"{settings.DB_HOST}:{settings.DB_PORT}"
            f"/{settings.DB_NAME}",
        ),
    )
    migrations = read_migrations((Path(__file__).parent / "migrations").as_posix())

    is_empty_db = manager.database.get_tables() == [
        backend.lock_table,
    ]
    if is_empty_db:
        backend.mark_migrations(migrations)

    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))
