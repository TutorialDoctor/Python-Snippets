from sqlalchemy import create_engine,ForeignKey,Column,Date,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,backref,sessionmaker

db_uri = "sqlite:///people.db"
db_engine = create_engine(db_uri,echo=True) #echo - prints queries to console
db_session = sessionmaker(bind=db_engine)
session = db_session()

Base = declarative_base() #Like d.model in flask_sqlalchemy

class Person(Base):
	__tablename__ = "person"
	id = Column(Integer, primary_key=True)
	name = Column(String(250),nullable=False)
	
	def __repr__(self):
		return str(self.name)
	#print(instance) - returns the name of the instance
	
class Address(Base):
	__tablename__ = "address"
	id = Column(Integer, primary_key=True)
	street_name = Column(String(250))
	street_number = Column(String(250))
	post_code = Column(String(250),nullable=False)
	person_id = Column(Integer,ForeignKey('person.id'))
	person = relationship(Person,backref='address') #backref allows Person.address
		
	def __repr__(self):
		return str(self.id)
	#print(instance): returns the id of the instance. 
	#You could also do: return str(self.street_name)
		
#Create tables from class metadata
Base.metadata.create_all(db_engine) 

#Create a new person named Joe
new_person = Person(name='Joe')

#Add Joe to the session
session.add(new_person)

#Commit the session to the database
session.commit() #this may be redundant

#Create a new address
new_address = Address(post_code='00000',person=new_person)
session.add(new_address)
session.commit()

#Testing
print(new_person)
print(new_person.address)
