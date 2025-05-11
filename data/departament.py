from sqlalchemy import Column, Integer, String, ForeignKey
from .db_session import SqlAlchemyBase
from sqlalchemy.orm import relationship
import json


class Departament(SqlAlchemyBase):
    __tablename__ = "departament"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    chief = Column(Integer, ForeignKey('users.id'), nullable=False)  # Явное указание ForeignKey
    members = Column(String, nullable=True, default=json.dumps([]))
    email = Column(String, index=True, unique=True, nullable=False)

    chief_user = relationship("User")  # Связь с моделью User