from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_string = "postgresql://user:userservice@db:5432/user"

db = create_engine(db_string)
base = declarative_base()
Session = sessionmaker(db)
session = Session()

from app.models.tables import User

base.metadata.create_all(db)
