from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Declare database engine
engine = create_engine("postgresql://postgres:root@localhost/EducationalPlatform")

SessionMaker = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

def get_database():
    db = None
    try:
        db = SessionMaker()
        yield db
    finally:
        if db is not None:
            db.close()