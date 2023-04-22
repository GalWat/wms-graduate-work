from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from concurrent.futures import ProcessPoolExecutor

from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['settings.yaml', '.secrets.yaml'],
    environments=True,
    merge_enabled=True,
)

engine = create_engine(
    f"postgresql://"
    f"{settings.db.user}:{settings.db.password}@{settings.db.host}:{settings.db.port}/{settings.db.database}"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

pool_executor = ProcessPoolExecutor()
