from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from base import Base

class Record(Base):

    __tablename__ = 'records'

    id = Column(Integer, primary_key=True)
    record_holder = Column(String)
    country = Column(String)
    number_of_cataches = Column(Integer)

    def __repr__(self):
        record_made= "Record: id ={} record holder={} country={} number of catches={}"
        return record_made.format(self.id, self.record_holder,self.country, self.number_of_cataches )
