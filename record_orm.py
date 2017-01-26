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

# Query that return 0 rows - difference between first() and one()
print(search_session.query(Record).filter_by(id=20).first())

#Querying the database for records that is more than one, results in an error
try:
    print(search_session.query(Record).filter_by(id=400).one())

except:
    print("Calling one when there are 0 or 2+ results causes an error")


print('One or none')
#Or, can use one_or_none. Returns None, or the first matching object, if found.
print(search_session.query(Record).filter_by(id=4).one_or_none())   # Phone 3 data
print(search_session.query(Record).filter_by(id=4000).one_or_none())   # None

results = search_session.query(Record).all()
print(results)
for record in results:
    print(record)

# Fetch only named columns as a tuple
for holder, country, catches in search_session.query(Record.record_holder, Record.country, Record.number_of_cataches):
    print(holder, country, catches)

#Search and return the record where the country name equal to France
for record in search_session.query(Record).filter_by(country='France'):
    print(record)
search_session.close()

#update the number_of_cataches of this record holder
update_session = Session()
old_record = update_session.query(Record).filter(Record.country=='France')
for record in old_record:
    record.number_of_cataches +=13
    update_session.commit()
    update_session.close()

for record in search_session.query(Record).filter_by(country='France'):
    print(record)

#a delete object of session class
delete_session = Session()
#Delete the record whose country is equals to France.
for record in delete_session.query(Record).filter_by(country='France'):
    delete_session.delete(record)
    delete_session.commit()
for record in results:
    print(record)








results = search_session.query(Record).all()
