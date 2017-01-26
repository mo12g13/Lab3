from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from record_stored import Record

engine = create_engine('sqlite:///record.db', echo=False) # Create a table for all the things that use Base
Base.metadata.create_all(engine)

#Create a Record object. Use named args to set the values of the object
record1 = Record(record_holder="James Gray", country="Agentina", number_of_cataches=12)
#Set the record holder to Sammy
record1.record_holder="Sammy"
print(record1.country)
print(record1.number_of_cataches)
print(record1.record_holder)
#Creation of the season class
Session = sessionmaker(bind=engine)
#Asking of the session object to instantiate a session object
save_session = Session()
#Add the phone but not saved
save_session.add(record1)
#now phone be saved
save_session.commit()
#Create few more Record objects
record2 = Record(record_holder="Brown Gray", country="France", number_of_cataches=99)
record3 = Record(record_holder="Daniel Billy", country="Brazil", number_of_cataches=80)
#Add the various objects. not yet save
save_session.add_all([record2, record3])
#newly added phone
print(save_session.new)
#Anything that has been changed
print(save_session.dirty)
#saved the changes
save_session.commit()
save_session.close()

search_session = Session()
for record in search_session.query(Record):
    print(record)

print(search_session.query(Record).first())

# Expect exactly one result? use one() which will return an object; or an error if there are 0 or 2+ items
#print(search_session.query(Record).filter_by(id=4).one())  # Useful for primary keys, will expect exactly one result

# Query that return 0 rows - difference between first() and one()
print(search_session.query(Record).filter_by(id=20).first())   # None
