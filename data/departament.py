from sqlalchemy import Column, Integer, String
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
import json

class Departament(SqlAlchemyBase):
    __tablename__ = "departament"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    chief = Column(Integer, nullable=True)
    members = Column(String, nullable=True, default=json.dumps([]))
    email = Column(String, index=True, unique=True, nullable=True)
