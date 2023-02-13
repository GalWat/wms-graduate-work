from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['settings.yaml', '.secrets.yaml'],
)

engine = create_engine(
    f"postgresql://"
    f"{settings.db.user}:{settings.db.password}@{settings.db.host}:{settings.db.port}/{settings.db.database}"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
