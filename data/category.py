from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from data.db_session import SqlAlchemyBase


class Category(SqlAlchemyBase):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    jobs = relationship("Jobs", secondary="job_category", backref="category_relations")
