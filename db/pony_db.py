import os
from pony import orm

class PonyDatabase:
    db = orm.Database()
    db.bind(
        provider="postgres",
        host=os.getenv("POSTGRES_HOST", "localhost"),
        database=os.environ['POSTGRES_NAME'],
        user=os.environ['POSTGRES_USERNAME'],
        password=os.environ['POSTGRES_PASSWORD']
    )
