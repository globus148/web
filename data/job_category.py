from sqlalchemy import Column, Integer, ForeignKey
from data.db_session import SqlAlchemyBase


class JobCategory(SqlAlchemyBase):
    __tablename__ = 'job_category'
    job_id = Column(Integer, ForeignKey('jobs.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'), primary_key=True)