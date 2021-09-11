import peewee as pw

from .manager import manager


class BaseModel(pw.Model):
    class Meta:
        database = manager.database


class Person(BaseModel):
    full_name = pw.CharField()
    github_username = pw.CharField()
    github_repo = pw.CharField()


class Commit(BaseModel):
    author = pw.ForeignKeyField(Person, backref='commits')
    sha = pw.CharField()
