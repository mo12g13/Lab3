from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from base import Base
"""The Record Clas and sets up the primary_key, record_holder, country, and number_of_cataches"""
class Record(Base):

#Creation of the table
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True)
    record_holder = Column(String)
    country = Column(String)
    number_of_cataches = Column(Integer)
#Return a string representation of the records
    def __repr__(self):
        record_made= "Record: id ={} record holder={} country={} number of catches={}"
        return record_made.format(self.id, self.record_holder,self.country, self.number_of_cataches )
