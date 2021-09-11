import peewee as pw
from playhouse.migrate import PostgresqlMigrator, migrate

from .manager import manager

migrator = PostgresqlMigrator(manager.database)


def apply_migrations():
    with manager.database.atomic():
        migrate(
            migrator.add_column("person", "tg_chat_id", pw.CharField(null=True)),
        )
