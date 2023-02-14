from psycopg2.pool import SimpleConnectionPool
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['settings.yaml', '.secrets.yaml'],
    environments=True,
    merge_enabled=True,
)

postgres_connections_pool = SimpleConnectionPool(
    minconn=1,
    maxconn=16,
    host=settings.db.host,
    database=settings.db.database,
    user=settings.db.user,
    password=settings.db.password,
    port=settings.db.port
)
