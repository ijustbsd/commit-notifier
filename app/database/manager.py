import peewee_async
import peewee_asyncext

from ..config import settings

manager = peewee_async.Manager(
    database=peewee_asyncext.PooledPostgresqlExtDatabase(
        database=settings.DB_NAME,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        max_connections=settings.DB_MAX_CONNECTIONS,
    ),
)

manager.database.set_allow_sync(False)
