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
